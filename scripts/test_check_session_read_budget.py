#!/usr/bin/env python3
"""Tests for check_session_read_budget.py.

Every check in the gate has a test here that breaks exactly that one thing in
a temporary git repository and asserts RED with the specific message, next to
a positive control that is GREEN. Run:

    python scripts/test_check_session_read_budget.py
"""

from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_session_read_budget as gate  # noqa: E402

MANIFEST_REL = gate.MANIFEST_REL
ARMENIAN_NAME = "docs/Հայերեն նշում.md"


def base_manifest() -> dict:
    return {
        "schema_version": 1,
        "total_bytes_max": 1000,
        "core": [
            {"path": "LAW.md", "bytes_max": 300, "why": "the law"},
            {"path": "core/HANDOFF.md", "bytes_max": 300, "why": "the handoff"},
        ],
        "areas": {
            ".": ["NOTES.md"],
            "docs": ["docs/GUIDE.md", ARMENIAN_NAME],
        },
    }


def base_files() -> dict[str, bytes]:
    return {
        "LAW.md": b"# Law\nline two\n",
        "core/HANDOFF.md": b"# Handoff\nnext step\n",
        "NOTES.md": b"# Notes\n",
        "docs/GUIDE.md": b"# Guide\n",
        ARMENIAN_NAME: "# Նշում\n".encode("utf-8"),
        "src/tool.py": b"print('not markdown')\n",
    }


class TempRepo:
    """A throwaway git repository whose files are tracked but never committed."""

    def __init__(self, files: dict[str, bytes] | None = None, manifest: object = None, raw_manifest: bytes | None = None):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        subprocess.run(["git", "init", "--quiet", str(self.root)], check=True, capture_output=True)
        subprocess.run(["git", "config", "core.autocrlf", "false"], cwd=self.root, check=True)
        for rel, content in (base_files() if files is None else files).items():
            self.write(rel, content)
        if raw_manifest is not None:
            self.write(MANIFEST_REL, raw_manifest)
        elif manifest is not False:
            self.write_manifest(base_manifest() if manifest is None else manifest)
        self.add()

    def write(self, rel: str, content: bytes) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)

    def write_manifest(self, data: object) -> None:
        self.write(MANIFEST_REL, json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8"))

    def add(self) -> None:
        subprocess.run(["git", "add", "-A"], cwd=self.root, check=True, capture_output=True)

    def errors(self) -> list[str]:
        return gate.check(self.root)[0]

    def cli(self, *args: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = gate.main(["--root", str(self.root), *args])
        return code, out.getvalue()

    def cleanup(self) -> None:
        self._tmp.cleanup()


class GateTestCase(unittest.TestCase):
    def repo(self, **kwargs) -> TempRepo:
        repo = TempRepo(**kwargs)
        self.addCleanup(repo.cleanup)
        return repo

    def assert_red(self, repo: TempRepo, fragment: str) -> list[str]:
        errors = repo.errors()
        self.assertTrue(
            any(fragment in error for error in errors),
            f"expected a RED line containing {fragment!r}, got {errors!r}",
        )
        code, output = repo.cli()
        self.assertEqual(code, 1, output)
        self.assertIn("SESSION READ BUDGET: RED", output)
        self.assertIn(fragment, output)
        return errors

    def mutated(self, change) -> TempRepo:
        manifest = base_manifest()
        change(manifest)
        return self.repo(manifest=manifest)


class PositiveControl(GateTestCase):
    def test_valid_repository_is_green(self):
        repo = self.repo()
        self.assertEqual(repo.errors(), [])
        code, output = repo.cli()
        self.assertEqual(code, 0, output)
        self.assertIn("SESSION READ BUDGET: GREEN", output)
        self.assertIn("core: 2 files, 35 bytes of 1000 (headroom 965); sum of ceilings 600", output)
        self.assertIn("LAW.md", output)

    def test_untracked_non_markdown_and_tracked_non_markdown_are_not_orphans(self):
        repo = self.repo()
        repo.write("src/other.py", b"x = 1\n")
        repo.write("scratch/untracked.md", b"# not tracked\n")
        self.assertEqual(repo.errors(), [])

    def test_this_repository_is_green_and_inside_the_decided_ceiling(self):
        errors, report = gate.check(gate.DEFAULT_ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(gate.UNIVERSAL_TOTAL_BYTES_MAX, 350_000)
        manifest = json.loads((gate.DEFAULT_ROOT / MANIFEST_REL).read_text(encoding="utf-8"))
        self.assertEqual(manifest["total_bytes_max"], 120_000)
        self.assertTrue(report[0].startswith("core: "))


class ManifestPresenceAndShape(GateTestCase):
    def test_missing_manifest(self):
        repo = self.repo(manifest=False)
        self.assert_red(repo, f"manifest is missing: {MANIFEST_REL}")

    def test_invalid_json(self):
        repo = self.repo(raw_manifest=b'{"schema_version": 1, "core": [')
        self.assert_red(repo, f"manifest is malformed: {MANIFEST_REL}")

    def test_invalid_utf8(self):
        repo = self.repo(raw_manifest=b"\xff\xfe{}")
        self.assert_red(repo, f"manifest is malformed: {MANIFEST_REL}")

    def test_top_level_is_not_an_object(self):
        repo = self.repo(manifest=["core"])
        self.assert_red(repo, "top level must be an object")

    def test_wrong_schema_version(self):
        repo = self.mutated(lambda m: m.update(schema_version=2))
        self.assert_red(repo, "manifest is malformed: schema_version is 2, expected 1")

    def test_total_bytes_max_must_be_a_positive_integer(self):
        for bad in ("1000", 0, -5, True, None, 10.5):
            with self.subTest(bad=bad):
                repo = self.mutated(lambda m, bad=bad: m.update(total_bytes_max=bad))
                self.assert_red(repo, f"manifest is malformed: total_bytes_max is {bad!r}")

    def test_core_must_be_a_non_empty_list(self):
        for bad in ([], {}, None, "LAW.md"):
            with self.subTest(bad=bad):
                repo = self.mutated(lambda m, bad=bad: m.update(core=bad))
                self.assert_red(repo, "manifest is malformed: core must be a non-empty list")

    def test_core_entry_must_be_an_object(self):
        repo = self.mutated(lambda m: m["core"].append("LAW.md"))
        self.assert_red(repo, "manifest is malformed: core[2] is not an object")

    def test_core_path_must_be_clean_and_relative(self):
        cases = {
            "/etc/passwd": "is absolute",
            "core\\HANDOFF.md": "uses a backslash",
            "core/../LAW.md": "is not normalised",
            "./LAW.md": "is not normalised",
            "": "is not a non-empty string",
            ".": "is not a file",
        }
        for bad, reason in cases.items():
            with self.subTest(bad=bad):
                repo = self.mutated(lambda m, bad=bad: m["core"][0].update(path=bad))
                self.assert_red(repo, f"manifest is malformed: core[0].path {bad!r} {reason}")

    def test_core_path_must_be_a_string(self):
        repo = self.mutated(lambda m: m["core"][0].update(path=7))
        self.assert_red(repo, "manifest is malformed: core[0].path 7 is not a non-empty string")

    def test_core_bytes_max_must_be_a_positive_integer(self):
        for bad in ("300", 0, -1, True, None):
            with self.subTest(bad=bad):
                repo = self.mutated(lambda m, bad=bad: m["core"][1].update(bytes_max=bad))
                self.assert_red(repo, f"manifest is malformed: core[1].bytes_max is {bad!r}")

    def test_core_entry_must_say_why(self):
        for bad in ("", "   ", None, 3):
            with self.subTest(bad=bad):
                repo = self.mutated(lambda m, bad=bad: m["core"][0].update(why=bad))
                self.assert_red(repo, "manifest is malformed: core[0].why is empty")

    def test_areas_must_be_an_object(self):
        for bad in ([], None, "docs"):
            with self.subTest(bad=bad):
                repo = self.mutated(lambda m, bad=bad: m.update(areas=bad))
                self.assert_red(repo, "manifest is malformed: areas must be an object")

    def test_area_directory_must_be_clean(self):
        def change(m):
            m["areas"]["docs/"] = m["areas"].pop("docs")

        repo = self.mutated(change)
        self.assert_red(repo, "manifest is malformed: area directory 'docs/' is not normalised")

    def test_area_must_be_a_non_empty_list(self):
        for bad in ([], "docs/GUIDE.md", None):
            with self.subTest(bad=bad):
                repo = self.mutated(lambda m, bad=bad: m["areas"].update(docs=bad))
                self.assert_red(repo, "manifest is malformed: area 'docs' must be a non-empty list of files")

    def test_area_file_must_be_clean_and_relative(self):
        for bad, reason in {"../outside.md": "is not normalised", 5: "is not a non-empty string", ".": "is not a file"}.items():
            with self.subTest(bad=bad):
                repo = self.mutated(lambda m, bad=bad: m["areas"]["docs"].append(bad))
                self.assert_red(repo, f"manifest is malformed: area 'docs' file[2] {bad!r} {reason}")


class CoreChecks(GateTestCase):
    def test_core_file_absent(self):
        repo = self.repo()
        (repo.root / "core/HANDOFF.md").unlink()
        repo.add()
        self.assert_red(repo, "core file is absent: core/HANDOFF.md")

    def test_core_file_not_tracked(self):
        repo = self.repo()
        subprocess.run(["git", "rm", "--cached", "--quiet", "LAW.md"], cwd=repo.root, check=True)
        self.assert_red(repo, "core file is not tracked by git: LAW.md")

    def test_core_file_exceeds_its_ceiling(self):
        repo = self.mutated(lambda m: m["core"][0].update(bytes_max=14))
        errors = self.assert_red(repo, "core file exceeds its ceiling: LAW.md is 15 bytes, bytes_max is 14")
        self.assertEqual(len(errors), 1, errors)

    def test_core_file_exactly_at_its_ceiling_is_green(self):
        repo = self.mutated(lambda m: m["core"][0].update(bytes_max=15))
        self.assertEqual(repo.errors(), [])

    def test_core_total_exceeds_the_budget(self):
        repo = self.mutated(lambda m: m.update(total_bytes_max=34))
        self.assert_red(repo, "core total exceeds the budget: 35 bytes, total_bytes_max is 34")

    def test_core_total_exactly_at_the_budget_is_not_a_total_error(self):
        repo = self.mutated(lambda m: m.update(total_bytes_max=35))
        self.assertFalse(any("core total exceeds" in error for error in repo.errors()))

    def test_sum_of_ceilings_exceeds_the_budget(self):
        repo = self.mutated(lambda m: m.update(total_bytes_max=599))
        errors = self.assert_red(repo, "sum of core bytes_max exceeds the budget: 600 bytes, total_bytes_max is 599")
        self.assertEqual(len(errors), 1, errors)

    def test_sum_of_ceilings_exactly_at_the_budget_is_green(self):
        repo = self.mutated(lambda m: m.update(total_bytes_max=600))
        self.assertEqual(repo.errors(), [])

    def test_budget_above_the_decided_ceiling(self):
        repo = self.mutated(lambda m: m.update(total_bytes_max=gate.UNIVERSAL_TOTAL_BYTES_MAX + 1))
        errors = self.assert_red(repo, "total_bytes_max is 350001, above the universal ceiling 350000 (D-028)")
        self.assertEqual(len(errors), 1, errors)

    def test_budget_exactly_at_the_decided_ceiling_is_green(self):
        repo = self.mutated(lambda m: m.update(total_bytes_max=gate.UNIVERSAL_TOTAL_BYTES_MAX))
        self.assertEqual(repo.errors(), [])

    def test_core_path_listed_twice(self):
        repo = self.mutated(lambda m: m["core"].append({"path": "LAW.md", "bytes_max": 300, "why": "again"}))
        self.assert_red(repo, "core path is listed twice: LAW.md")


class AreaChecks(GateTestCase):
    def test_area_path_listed_twice(self):
        repo = self.mutated(lambda m: m["areas"]["docs"].append("docs/GUIDE.md"))
        errors = self.assert_red(repo, "area docs lists a path twice: docs/GUIDE.md")
        self.assertEqual(len(errors), 1, errors)

    def test_same_file_in_two_areas_is_allowed(self):
        repo = self.mutated(lambda m: m["areas"]["."].append("docs/GUIDE.md"))
        self.assertEqual(repo.errors(), [])

    def test_area_lists_a_core_file(self):
        repo = self.mutated(lambda m: m["areas"]["docs"].append("LAW.md"))
        errors = self.assert_red(repo, "area docs lists a path that is already in the core: LAW.md")
        self.assertEqual(len(errors), 1, errors)

    def test_area_directory_does_not_exist(self):
        repo = self.mutated(lambda m: m["areas"].update({"nowhere/deep": ["NOTES.md"]}))
        errors = self.assert_red(repo, "area names a directory that does not exist: nowhere/deep")
        self.assertEqual(len(errors), 1, errors)

    def test_area_directory_holding_only_nested_files_exists(self):
        repo = self.repo()
        repo.write("a/b/c.md", b"# nested\n")
        manifest = base_manifest()
        manifest["areas"]["a"] = ["a/b/c.md"]
        repo.write_manifest(manifest)
        repo.add()
        self.assertEqual(repo.errors(), [])

    def test_area_file_does_not_exist(self):
        repo = self.mutated(lambda m: m["areas"]["docs"].append("docs/MISSING.md"))
        errors = self.assert_red(repo, "area docs names a file that does not exist: docs/MISSING.md")
        self.assertEqual(len(errors), 1, errors)

    def test_area_file_not_tracked(self):
        repo = self.repo()
        subprocess.run(["git", "rm", "--cached", "--quiet", "docs/GUIDE.md"], cwd=repo.root, check=True)
        self.assert_red(repo, "area docs names a file that is not tracked by git: docs/GUIDE.md")


class OrphanCheck(GateTestCase):
    def test_tracked_markdown_reachable_from_nothing(self):
        repo = self.repo()
        repo.write("docs/ORPHAN.md", b"# nobody is told to read me\n")
        repo.add()
        errors = self.assert_red(repo, "tracked Markdown file is in neither the core nor any area: docs/ORPHAN.md")
        self.assertEqual(len(errors), 1, errors)

    def test_uppercase_extension_is_markdown_too(self):
        repo = self.repo()
        repo.write("docs/SHOUT.MD", b"# loud\n")
        repo.add()
        self.assert_red(repo, "tracked Markdown file is in neither the core nor any area: docs/SHOUT.MD")

    def test_orphan_with_space_and_armenian_name_is_named_exactly(self):
        repo = self.mutated(lambda m: m["areas"]["docs"].remove(ARMENIAN_NAME))
        errors = self.assert_red(repo, f"tracked Markdown file is in neither the core nor any area: {ARMENIAN_NAME}")
        self.assertEqual(len(errors), 1, errors)


class FileNames(GateTestCase):
    def test_space_and_armenian_name_in_an_area_is_green(self):
        repo = self.repo()
        self.assertIn(ARMENIAN_NAME, gate.tracked_files(repo.root))
        self.assertEqual(repo.errors(), [])

    def test_space_and_armenian_name_in_the_core_is_measured(self):
        def change(m):
            m["areas"]["docs"].remove(ARMENIAN_NAME)
            m["core"].append({"path": ARMENIAN_NAME, "bytes_max": 12, "why": "a non-ASCII core path"})

        repo = self.mutated(change)
        self.assert_red(repo, f"core file exceeds its ceiling: {ARMENIAN_NAME} is 13 bytes, bytes_max is 12")


class LineEndings(GateTestCase):
    def crlf_pair(self) -> tuple[TempRepo, TempRepo]:
        lf = base_files()
        crlf = {rel: content.replace(b"\n", b"\r\n") for rel, content in lf.items()}
        return self.repo(files=lf), self.repo(files=crlf)

    def test_crlf_checkout_counts_the_same_bytes(self):
        lf, crlf = self.crlf_pair()
        self.assertNotEqual((lf.root / "LAW.md").stat().st_size, (crlf.root / "LAW.md").stat().st_size)
        self.assertEqual(gate.check(lf.root), gate.check(crlf.root))
        self.assertIn("core: 2 files, 35 bytes of 1000", gate.check(crlf.root)[1][0])

    def test_crlf_file_at_its_lf_ceiling_is_green(self):
        files = {rel: content.replace(b"\n", b"\r\n") for rel, content in base_files().items()}
        manifest = base_manifest()
        manifest["core"][0]["bytes_max"] = 15
        manifest["core"][1]["bytes_max"] = 20
        manifest["total_bytes_max"] = 35
        repo = self.repo(files=files, manifest=manifest)
        self.assertEqual((repo.root / "LAW.md").stat().st_size, 17)
        self.assertEqual(repo.errors(), [])

    def test_crlf_checkout_has_the_same_receipt(self):
        lf, crlf = self.crlf_pair()
        self.assertEqual(gate.receipt(lf.root), gate.receipt(crlf.root))

    def test_area_bytes_are_normalised_too(self):
        lf, crlf = self.crlf_pair()
        files = base_manifest()["areas"]["docs"]
        self.assertEqual(gate.area_bytes(lf.root, files), gate.area_bytes(crlf.root, files))


class Receipt(GateTestCase):
    def test_receipt_is_a_stable_sha256(self):
        first, second = self.repo(), self.repo()
        digest = gate.receipt(first.root)
        self.assertRegex(digest, r"^[0-9a-f]{64}$")
        self.assertEqual(digest, gate.receipt(second.root))
        code, output = first.cli("--receipt")
        self.assertEqual((code, output.strip()), (0, digest))

    def test_receipt_changes_with_core_content(self):
        repo = self.repo()
        before = gate.receipt(repo.root)
        repo.write("core/HANDOFF.md", b"# Handoff\nnext stop\n")
        self.assertNotEqual(before, gate.receipt(repo.root))

    def test_receipt_ignores_area_content(self):
        repo = self.repo()
        before = gate.receipt(repo.root)
        repo.write("docs/GUIDE.md", b"# Guide, rewritten\n")
        self.assertEqual(before, gate.receipt(repo.root))

    def test_receipt_changes_with_core_order(self):
        repo = self.repo()
        before = gate.receipt(repo.root)
        manifest = base_manifest()
        manifest["core"].reverse()
        repo.write_manifest(manifest)
        self.assertNotEqual(before, gate.receipt(repo.root))

    def test_receipt_binds_the_path_not_only_the_bytes(self):
        files = base_files()
        files["core/RENAMED.md"] = files.pop("core/HANDOFF.md")
        manifest = base_manifest()
        manifest["core"][1]["path"] = "core/RENAMED.md"
        renamed = self.repo(files=files, manifest=manifest)
        self.assertEqual(renamed.errors(), [])
        self.assertNotEqual(gate.receipt(self.repo().root), gate.receipt(renamed.root))

    def test_receipt_separates_one_file_from_the_next(self):
        def repo_with(first: bytes, second: bytes) -> TempRepo:
            files = base_files()
            files["LAW.md"], files["core/HANDOFF.md"] = first, second
            return self.repo(files=files)

        left = repo_with(b"alpha\nbeta\n", b"gamma\n")
        right = repo_with(b"alpha\n", b"beta\ngamma\n")
        self.assertNotEqual(gate.receipt(left.root), gate.receipt(right.root))

    def test_receipt_frames_content_by_length(self):
        # Without the length field the stream is path NUL NUL content, and
        # content holding "next path NUL NUL" could be re-cut into two
        # different cores with one digest. The length makes the cut explicit.
        boundary = b"core/HANDOFF.md\0\0"

        def repo_with(first: bytes, second: bytes) -> TempRepo:
            files = base_files()
            files["LAW.md"], files["core/HANDOFF.md"] = first, second
            return self.repo(files=files)

        left = repo_with(b"x", b"y" + boundary + b"z")
        right = repo_with(b"x" + boundary + b"y", b"z")
        self.assertNotEqual(gate.receipt(left.root), gate.receipt(right.root))

    def test_verify_receipt_accepts_the_current_digest(self):
        repo = self.repo()
        digest = gate.receipt(repo.root)
        code, output = repo.cli("--verify-receipt", digest.upper())
        self.assertEqual(code, 0, output)
        self.assertIn(f"SESSION READ RECEIPT: GREEN ({digest})", output)

    def test_verify_receipt_rejects_a_stale_digest(self):
        repo = self.repo()
        stale = gate.receipt(repo.root)
        repo.write("LAW.md", b"# Law\nline 2\n")
        code, output = repo.cli("--verify-receipt", stale)
        self.assertEqual(code, 1, output)
        self.assertIn("SESSION READ RECEIPT: RED", output)
        self.assertIn(f"receipt does not match the current core: offered {stale}, current {gate.receipt(repo.root)}", output)

    def test_verify_receipt_rejects_garbage(self):
        code, output = self.repo().cli("--verify-receipt", "not-a-digest")
        self.assertEqual(code, 1, output)
        self.assertIn("receipt does not match the current core", output)

    def test_no_receipt_is_issued_for_a_red_repository(self):
        repo = self.mutated(lambda m: m["core"][0].update(bytes_max=1))
        for args in (("--receipt",), ("--verify-receipt", gate.receipt(repo.root))):
            with self.subTest(args=args):
                code, output = repo.cli(*args)
                self.assertEqual(code, 1, output)
                self.assertIn("SESSION READ BUDGET: RED", output)
                self.assertNotIn("GREEN", output)


class Environment(GateTestCase):
    def test_directory_that_is_not_a_git_repository(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / MANIFEST_REL
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps(base_manifest()), encoding="utf-8")
            errors, _ = gate.check(root)
        self.assertEqual(len(errors), 1, errors)
        self.assertIn("cannot enumerate tracked files with git ls-files -z", errors[0])

    def test_command_line_runs_as_a_script(self):
        repo = self.repo()
        result = subprocess.run(
            [sys.executable, str(Path(gate.__file__)), "--root", str(repo.root)],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("SESSION READ BUDGET: GREEN", result.stdout)

    def test_script_exits_non_zero_when_red(self):
        repo = self.repo(manifest=False)
        result = subprocess.run(
            [sys.executable, str(Path(gate.__file__)), "--root", str(repo.root)],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("SESSION READ BUDGET: RED", result.stdout)


if __name__ == "__main__":
    unittest.main()
