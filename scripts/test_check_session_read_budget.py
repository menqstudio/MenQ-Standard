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
import os
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
        self.assertEqual(
            errors,
            [
                "tracked Markdown file is in neither the core nor any area: docs/ORPHAN.md; "
                "list it in an area, or run this gate with --sync-areas"
            ],
        )

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


class OneImplementation(GateTestCase):
    """This file tests the gate through MenQ Standard's entry point.  The implementation is the
    consumer-kit file; these tests hold the two together and test the kit's own defaults (D-029)."""

    KIT_GATE = Path(gate.__file__).resolve().parents[1] / "consumer" / "check_session_read_budget.py"

    def kit_repo(self) -> TempRepo:
        """A repository laid out as a product repository: the manifest at its root."""
        repo = self.repo(manifest=False)
        repo.write(gate.kit.MANIFEST_REL, json.dumps(base_manifest(), ensure_ascii=False).encode("utf-8"))
        repo.add()
        return repo

    def run_kit(self, cwd: Path, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(self.KIT_GATE), *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8")

    def test_the_entry_point_holds_the_kits_objects_not_copies(self):
        self.assertEqual(Path(gate.kit.__file__).resolve(), self.KIT_GATE)
        for name in ("Refusal", "normalised", "tracked_files", "is_positive_int", "path_problem", "load_manifest", "shape_errors", "core_measurements", "area_bytes", "is_markdown", "own_area", "repaired_areas"):
            with self.subTest(name=name):
                self.assertIs(getattr(gate, name), getattr(gate.kit, name))
        self.assertEqual((gate.UNIVERSAL_TOTAL_BYTES_MAX, gate.SCHEMA_VERSION, gate.ROOT_AREA), (gate.kit.UNIVERSAL_TOTAL_BYTES_MAX, gate.kit.SCHEMA_VERSION, gate.kit.ROOT_AREA))

    def test_the_entry_point_defines_nothing_but_its_two_defaults(self):
        source = Path(gate.__file__).read_text(encoding="utf-8")
        self.assertNotIn("git ls-files", source)
        self.assertNotIn("hashlib", source)
        self.assertNotIn("350", source)
        self.assertEqual(gate.MANIFEST_REL, "foundation/ai-collaboration/SESSION_READ_MANIFEST.json")
        self.assertEqual(gate.DEFAULT_ROOT, Path(gate.__file__).resolve().parents[1])

    def test_the_kits_default_manifest_is_at_the_repository_root(self):
        self.assertEqual(gate.kit.MANIFEST_REL, "SESSION_READ_MANIFEST.json")
        repo = self.kit_repo()
        self.assertEqual(gate.kit.check(repo.root), ([], gate.kit.check(repo.root)[1]))
        self.assertEqual(gate.kit.receipt(repo.root), gate.receipt(self.repo().root))
        errors, _ = gate.kit.check(self.repo().root)
        self.assertEqual(errors, ["manifest is missing: SESSION_READ_MANIFEST.json"])

    def test_the_kit_run_as_a_script_checks_the_current_directory(self):
        repo = self.kit_repo()
        result = self.run_kit(repo.root)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("SESSION READ BUDGET: GREEN", result.stdout)
        self.assertIn("core: 2 files, 35 bytes of 1000", result.stdout)
        elsewhere = self.repo(manifest=False)
        result = self.run_kit(elsewhere.root, "--root", str(repo.root))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result = self.run_kit(elsewhere.root)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("manifest is missing: SESSION_READ_MANIFEST.json", result.stdout)

    def test_the_kit_takes_the_manifest_path_as_a_parameter(self):
        repo = self.repo()
        result = self.run_kit(repo.root, "--manifest", MANIFEST_REL)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result = self.run_kit(repo.root, "--manifest", "config/no-such.json")
        self.assertEqual(result.returncode, 1)
        self.assertIn("manifest is missing: config/no-such.json", result.stdout)

    def test_the_universal_ceiling_binds_a_product_repository_too(self):
        repo = self.repo(manifest=False)
        manifest = base_manifest()
        manifest["total_bytes_max"] = 350_001
        repo.write(gate.kit.MANIFEST_REL, json.dumps(manifest, ensure_ascii=False).encode("utf-8"))
        repo.add()
        result = self.run_kit(repo.root)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("total_bytes_max is 350001, above the universal ceiling 350000 (D-028)", result.stdout)

    def test_an_entry_point_without_its_implementation_is_red_not_green(self):
        with tempfile.TemporaryDirectory() as tmp:
            scripts = Path(tmp) / "scripts"
            scripts.mkdir()
            (scripts / "check_session_read_budget.py").write_bytes(Path(gate.__file__).read_bytes())
            result = subprocess.run([sys.executable, str(scripts / "check_session_read_budget.py")], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(result.stdout.splitlines()[0], "SESSION READ BUDGET: RED")
        self.assertIn("the gate's implementation cannot be loaded: consumer/check_session_read_budget.py", result.stdout)
        self.assertNotIn("Traceback", result.stdout + result.stderr)


ORPHAN_LINE = (
    "tracked Markdown file is in neither the core nor any area: {}; "
    "list it in an area, or run this gate with --sync-areas"
)


def canonical(data: object, newline: str = "\n") -> bytes:
    """The bytes --sync-areas writes for a manifest."""
    return (json.dumps(data, ensure_ascii=False, indent=2) + "\n").replace("\n", newline).encode("utf-8")


class SyncAreas(GateTestCase):
    """--sync-areas repairs "areas" and nothing else; it never regenerates what a person wrote."""

    def manifest(self, repo: TempRepo) -> dict:
        return json.loads(self.raw(repo).decode("utf-8"))

    def raw(self, repo: TempRepo) -> bytes:
        return (repo.root / MANIFEST_REL).read_bytes()

    def sync(self, repo: TempRepo) -> tuple[int, str]:
        code, output = repo.cli("--sync-areas")
        self.assertNotIn("Traceback", output)
        return code, output

    def with_areas(self, areas: dict, files: dict[str, bytes] | None = None) -> TempRepo:
        manifest = base_manifest()
        manifest["areas"] = areas
        return self.repo(files=files, manifest=manifest)

    def assert_refused(self, repo: TempRepo, fragment: str) -> None:
        path = repo.root / MANIFEST_REL
        before = path.read_bytes() if path.is_file() else None
        code, output = self.sync(repo)
        self.assertEqual(code, 1, output)
        self.assertEqual(output.splitlines()[0], "SESSION READ AREAS: RED", output)
        self.assertIn(fragment, output)
        self.assertEqual(output.splitlines()[-1], "- nothing was written", output)
        self.assertNotIn("WRITTEN", output)
        self.assertEqual(path.read_bytes() if path.is_file() else None, before)

    # --- what it writes -----------------------------------------------------------------------

    def test_empty_areas_become_a_per_directory_listing_and_the_gate_turns_green(self):
        repo = self.with_areas({})
        self.assertEqual(len(repo.errors()), 3, repo.errors())
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertEqual(
            output.splitlines(),
            [
                f"SESSION READ AREAS: WRITTEN (3 area files in 2 directories; 3 added, 0 removed) to {MANIFEST_REL}",
                f"added, each to the area of its own directory: NOTES.md, docs/GUIDE.md, {ARMENIAN_NAME}",
            ],
        )
        self.assertEqual(list(self.manifest(repo)["areas"].items()), [(".", ["NOTES.md"]), ("docs", ["docs/GUIDE.md", ARMENIAN_NAME])])
        self.assertEqual(repo.errors(), [])
        code, output = repo.cli()
        self.assertEqual(code, 0, output)
        self.assertIn("SESSION READ BUDGET: GREEN", output)

    def test_a_repository_red_only_for_an_unreachable_file_is_green_afterwards(self):
        repo = self.repo()
        repo.write("docs/ORPHAN.md", b"# nobody is told to read me\n")
        repo.add()
        self.assertEqual(repo.errors(), [ORPHAN_LINE.format("docs/ORPHAN.md")])
        receipt_before = gate.receipt(repo.root)
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertIn("1 added, 0 removed", output)
        self.assertIn("added, each to the area of its own directory: docs/ORPHAN.md", output)
        self.assertEqual(self.manifest(repo)["areas"]["docs"], ["docs/GUIDE.md", ARMENIAN_NAME, "docs/ORPHAN.md"])
        self.assertEqual(repo.cli()[0], 0)
        self.assertEqual(gate.receipt(repo.root), receipt_before)

    def test_the_written_file_is_indented_utf8_json_with_a_trailing_newline(self):
        repo = self.with_areas({})
        self.sync(repo)
        expected = base_manifest()
        raw = self.raw(repo)
        self.assertEqual(raw, canonical(expected))
        self.assertTrue(raw.endswith(b"\n}\n"))
        self.assertIn(b'\n  "schema_version": 1,\n', raw)
        self.assertIn(ARMENIAN_NAME.encode("utf-8"), raw)
        self.assertNotIn(b"\\u", raw)
        self.assertNotIn(b"\r", raw)

    def test_everything_but_areas_is_kept_byte_for_byte_and_in_its_order(self):
        manifest = {
            "schema_version": 1,
            "նշում": "an unknown key, before the core",
            "total_bytes_max": 1000,
            "core": [
                {"why": "the law, with its fields in another order", "path": "LAW.md", "bytes_max": 300, "extra": [1, {"k": None}]},
                {"path": "core/HANDOFF.md", "bytes_max": 300, "why": "the handoff"},
            ],
            "areas": {".": ["NOTES.md"]},
            "trailer": {"unknown": ["after", "areas"]},
        }
        repo = self.repo(raw_manifest=canonical(manifest))
        before = self.raw(repo)
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        after = self.raw(repo)
        self.assertNotEqual(before, after)
        self.assertEqual(after.split(b'"areas"')[0], before.split(b'"areas"')[0])
        self.assertEqual(after[after.index(b'"trailer"'):], before[before.index(b'"trailer"'):])
        written = self.manifest(repo)
        self.assertEqual(list(written), list(manifest))
        self.assertEqual([list(entry) for entry in written["core"]], [list(entry) for entry in manifest["core"]])
        self.assertEqual({k: v for k, v in written.items() if k != "areas"}, {k: v for k, v in manifest.items() if k != "areas"})
        self.assertEqual(written["areas"], {".": ["NOTES.md"], "docs": ["docs/GUIDE.md", ARMENIAN_NAME]})

    # --- what it keeps ------------------------------------------------------------------------

    def test_curated_entries_their_order_and_duplicates_across_areas_are_kept(self):
        curated = {
            ".": ["docs/GUIDE.md", "NOTES.md"],
            "docs": [ARMENIAN_NAME, "docs/GUIDE.md", "NOTES.md"],
            "src": ["NOTES.md", "docs/GUIDE.md"],
        }
        repo = self.with_areas(curated)
        self.assertEqual(repo.errors(), [])
        for rel in ("docs/Z.md", "docs/A.md", "a/b/c.md"):
            repo.write(rel, b"# new\n")
        repo.add()
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertEqual(
            list(self.manifest(repo)["areas"].items()),
            [
                (".", ["docs/GUIDE.md", "NOTES.md"]),
                ("a/b", ["a/b/c.md"]),
                ("docs", [ARMENIAN_NAME, "docs/GUIDE.md", "NOTES.md", "docs/A.md", "docs/Z.md"]),
                ("src", ["NOTES.md", "docs/GUIDE.md"]),
            ],
        )
        self.assertIn("6 area files in 4 directories; 3 added, 0 removed", output)
        self.assertEqual(repo.errors(), [])

    def test_a_file_reached_only_from_another_directorys_area_is_not_added_to_its_own(self):
        repo = self.with_areas({"src": ["NOTES.md", "docs/GUIDE.md", ARMENIAN_NAME]})
        before = self.raw(repo)
        code, output = self.sync(repo)
        self.assertEqual((code, output.splitlines()[0]), (0, "SESSION READ AREAS: UNCHANGED (3 area files in 1 directories); the manifest was not written"))
        self.assertEqual(self.raw(repo), before)

    def test_nothing_to_do_says_unchanged_and_does_not_touch_the_file(self):
        repo = self.repo()
        path = repo.root / MANIFEST_REL
        before = path.read_bytes()
        self.assertFalse(before.endswith(b"\n"), "the fixture is deliberately not in the written form")
        os.utime(path, ns=(1_000_000_000_000_000_000, 1_000_000_000_000_000_000))
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertEqual(output.splitlines(), ["SESSION READ AREAS: UNCHANGED (3 area files in 2 directories); the manifest was not written"])
        self.assertEqual(path.stat().st_mtime_ns, 1_000_000_000_000_000_000)
        self.assertEqual(path.read_bytes(), before)

    def test_running_it_twice_changes_nothing_the_second_time(self):
        repo = self.with_areas({})
        self.assertIn("WRITTEN", self.sync(repo)[1])
        first = self.raw(repo)
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertIn("UNCHANGED", output)
        self.assertEqual(self.raw(repo), first)

    # --- what it adds -------------------------------------------------------------------------

    def test_an_untracked_markdown_file_and_a_tracked_other_file_are_not_added(self):
        repo = self.repo()
        repo.write("scratch/untracked.md", b"# not tracked\n")
        repo.write("docs/tracked.txt", b"not markdown\n")
        subprocess.run(["git", "add", "docs/tracked.txt"], cwd=repo.root, check=True)
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertIn("UNCHANGED", output)
        self.assertEqual(self.manifest(repo), base_manifest())

    def test_uppercase_extension_is_added(self):
        repo = self.repo()
        repo.write("docs/SHOUT.MD", b"# loud\n")
        repo.add()
        self.sync(repo)
        self.assertEqual(self.manifest(repo)["areas"]["docs"], ["docs/GUIDE.md", ARMENIAN_NAME, "docs/SHOUT.MD"])
        self.assertEqual(repo.errors(), [])

    def test_a_core_file_is_never_added_to_an_area(self):
        repo = self.with_areas({})
        self.sync(repo)
        areas = self.manifest(repo)["areas"]
        self.assertNotIn("core", areas)
        self.assertEqual([rel for files in areas.values() for rel in files if rel in ("LAW.md", "core/HANDOFF.md")], [])

    def test_a_new_area_takes_its_sorted_place_and_no_existing_key_moves(self):
        files = {**base_files(), "zeta/x.py": b"x = 1\n"}
        cases = {
            "middle": ({".": ["NOTES.md"], "zeta": ["NOTES.md"]}, [".", "docs", "zeta"]),
            "end": ({".": ["NOTES.md", "docs/GUIDE.md", ARMENIAN_NAME]}, [".", "mid"]),
            "before unsorted keys": ({"zeta": ["NOTES.md"], ".": ["NOTES.md"]}, ["docs", "zeta", "."]),
        }
        for name, (areas, expected) in cases.items():
            with self.subTest(name=name):
                repo = self.with_areas(areas, files=files)
                if name == "end":
                    repo.write("mid/README.md", b"# mid\n")
                    repo.add()
                code, output = self.sync(repo)
                self.assertEqual(code, 0, output)
                self.assertEqual(list(self.manifest(repo)["areas"]), expected)
                self.assertEqual(repo.errors(), [])

    def test_added_files_are_appended_in_sorted_order_whatever_order_git_gives(self):
        repo = self.with_areas({})
        tracked = sorted(gate.tracked_files(repo.root), reverse=True)
        areas, changes = gate.repaired_areas(repo.root, base_manifest() | {"areas": {}}, tracked)
        self.assertEqual(list(areas.items()), [(".", ["NOTES.md"]), ("docs", ["docs/GUIDE.md", ARMENIAN_NAME])])
        self.assertEqual(changes["added"], [(".", "NOTES.md"), ("docs", "docs/GUIDE.md"), ("docs", ARMENIAN_NAME)])

    # --- what it removes ----------------------------------------------------------------------

    def test_an_entry_for_a_deleted_file_is_removed(self):
        repo = self.repo()
        subprocess.run(["git", "rm", "--force", "--quiet", "docs/GUIDE.md"], cwd=repo.root, check=True)
        self.assertTrue(any("does not exist: docs/GUIDE.md" in error for error in repo.errors()))
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertEqual(
            output.splitlines(),
            [
                f"SESSION READ AREAS: WRITTEN (2 area files in 2 directories; 0 added, 1 removed) to {MANIFEST_REL}",
                "removed, no longer tracked or no longer in the checkout: docs/GUIDE.md",
            ],
        )
        self.assertEqual(self.manifest(repo)["areas"], {".": ["NOTES.md"], "docs": [ARMENIAN_NAME]})
        self.assertEqual(repo.errors(), [])

    def test_an_entry_for_a_file_that_is_no_longer_tracked_is_removed_with_its_emptied_area(self):
        repo = self.repo()
        subprocess.run(["git", "rm", "--cached", "--quiet", "NOTES.md"], cwd=repo.root, check=True)
        self.assertTrue((repo.root / "NOTES.md").is_file())
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertIn("removed, no longer tracked or no longer in the checkout: NOTES.md", output)
        self.assertEqual(output.splitlines()[-1], "removed areas left empty: .")
        self.assertEqual(list(self.manifest(repo)["areas"]), ["docs"])
        self.assertEqual(repo.errors(), [])

    def test_an_area_emptied_and_refilled_in_one_run_is_not_reported_as_removed(self):
        repo = self.repo()
        subprocess.run(["git", "rm", "--force", "--quiet", "docs/GUIDE.md", ARMENIAN_NAME], cwd=repo.root, check=True)
        repo.write("docs/NEW.md", b"# new\n")
        repo.add()
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertEqual(
            output.splitlines(),
            [
                f"SESSION READ AREAS: WRITTEN (2 area files in 2 directories; 1 added, 2 removed) to {MANIFEST_REL}",
                "added, each to the area of its own directory: docs/NEW.md",
                f"removed, no longer tracked or no longer in the checkout: docs/GUIDE.md, {ARMENIAN_NAME}",
            ],
        )
        self.assertEqual(list(self.manifest(repo)["areas"].items()), [(".", ["NOTES.md"]), ("docs", ["docs/NEW.md"])])
        self.assertEqual(repo.errors(), [])

    def test_a_dead_entry_is_removed_from_every_area_that_lists_it(self):
        repo = self.with_areas({".": ["NOTES.md", "docs/GUIDE.md"], "docs": ["docs/GUIDE.md", ARMENIAN_NAME], "src": ["docs/GUIDE.md"]})
        subprocess.run(["git", "rm", "--force", "--quiet", "docs/GUIDE.md"], cwd=repo.root, check=True)
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertEqual(self.manifest(repo)["areas"], {".": ["NOTES.md"], "docs": [ARMENIAN_NAME]})
        self.assertIn("0 added, 3 removed", output)
        self.assertIn("docs/GUIDE.md (in area .), docs/GUIDE.md, docs/GUIDE.md (in area src)", output)
        self.assertIn("removed areas left empty: src", output)

    def test_a_tracked_file_missing_from_the_checkout_is_removed_and_not_added_back(self):
        repo = self.repo()
        (repo.root / "docs/GUIDE.md").unlink()
        self.assertIn("docs/GUIDE.md", gate.tracked_files(repo.root))
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertEqual(self.manifest(repo)["areas"]["docs"], [ARMENIAN_NAME])
        self.assertIn("removed, no longer tracked or no longer in the checkout: docs/GUIDE.md", output)
        self.assertIn("NOT added: tracked Markdown that is missing from the checkout, so the default mode stays RED for it: docs/GUIDE.md", output)
        self.assertEqual(repo.errors(), [ORPHAN_LINE.format("docs/GUIDE.md")])
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertIn("UNCHANGED", output)
        self.assertIn("NOT added", output)

    def test_a_core_path_is_removed_from_an_area_and_named(self):
        repo = self.with_areas({".": ["NOTES.md"], "docs": ["docs/GUIDE.md", "LAW.md", ARMENIAN_NAME], "core": ["core/HANDOFF.md"]})
        self.assertEqual(len(repo.errors()), 2, repo.errors())
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertEqual(
            output.splitlines(),
            [
                f"SESSION READ AREAS: WRITTEN (3 area files in 2 directories; 0 added, 2 removed) to {MANIFEST_REL}",
                "removed, already in the core: LAW.md (in area docs), core/HANDOFF.md",
                "removed areas left empty: core",
            ],
        )
        self.assertEqual(self.manifest(repo)["areas"], base_manifest()["areas"])
        self.assertEqual(self.manifest(repo)["core"], base_manifest()["core"])
        self.assertEqual(repo.errors(), [])

    # --- what it does not repair --------------------------------------------------------------

    def test_an_area_whose_directory_is_gone_but_whose_entries_are_live_is_left_and_named(self):
        areas = {**base_manifest()["areas"], "gone/dir": ["NOTES.md", "docs/GUIDE.md"]}
        repo = self.with_areas(areas)
        before = self.raw(repo)
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertEqual(
            output.splitlines(),
            [
                "SESSION READ AREAS: UNCHANGED (3 area files in 3 directories); the manifest was not written",
                "NOT repaired: an area names a directory that does not exist while its entries are live; "
                "it is left as it is and the default mode reports it: gone/dir",
            ],
        )
        self.assertEqual(self.raw(repo), before)
        self.assertEqual(repo.errors(), ["area names a directory that does not exist: gone/dir"])
        repo.write("docs/ORPHAN.md", b"# orphan\n")
        repo.add()
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertIn("WRITTEN", output)
        self.assertIn("NOT repaired", output)
        self.assertEqual(self.manifest(repo)["areas"]["gone/dir"], ["NOTES.md", "docs/GUIDE.md"])
        self.assertEqual(repo.errors(), ["area names a directory that does not exist: gone/dir"])

    def test_an_area_whose_directory_is_gone_and_whose_entries_are_all_dead_is_removed(self):
        repo = self.with_areas({**base_manifest()["areas"], "gone": ["gone/OLD.md"]})
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        self.assertNotIn("NOT repaired", output)
        self.assertEqual(self.manifest(repo)["areas"], base_manifest()["areas"])

    def test_long_lists_are_cut_with_a_count(self):
        files = {**base_files(), **{f"docs/F{index:02}.md": b"# f\n" for index in range(15)}}
        repo = self.with_areas({f"gone{index:02}": ["NOTES.md"] for index in range(14)}, files=files)
        code, output = self.sync(repo)
        self.assertEqual(code, 0, output)
        lines = output.splitlines()
        self.assertIn("17 added, 0 removed", lines[0])
        self.assertTrue(lines[1].endswith("docs/F09.md, docs/F10.md, docs/F11.md and 5 more"), lines[1])
        self.assertTrue(lines[2].endswith("gone10, gone11 and 2 more"), lines[2])
        self.assertEqual(gate.kit.SHOWN, 12)

    # --- line endings -------------------------------------------------------------------------

    def test_a_crlf_manifest_stays_crlf_and_an_lf_one_stays_lf(self):
        for newline in ("\r\n", "\n"):
            with self.subTest(newline=newline):
                start = base_manifest()
                start["areas"] = {}
                repo = self.repo(raw_manifest=canonical(start, newline))
                code, output = self.sync(repo)
                self.assertEqual(code, 0, output)
                raw = self.raw(repo)
                self.assertEqual(raw, canonical(base_manifest(), newline))
                self.assertEqual(raw.count(b"\r\n"), raw.count(b"\n") if newline == "\r\n" else 0)
                self.assertEqual(repo.errors(), [])

    def test_a_manifest_with_mixed_line_endings_is_refused(self):
        start = base_manifest()
        start["areas"] = {}
        for name, raw in {
            "one CRLF": canonical(start).replace(b"\n", b"\r\n", 1),
            "one LF": canonical(start, "\r\n").replace(b"\r\n", b"\n", 1),
        }.items():
            with self.subTest(name=name):
                repo = self.repo(raw_manifest=raw)
                self.assert_refused(repo, f"manifest mixes line endings: {MANIFEST_REL} has")
        code, output = self.sync(self.repo(raw_manifest=canonical(start).replace(b"\n", b"\r\n", 1)))
        self.assertIn(f"- manifest mixes line endings: {MANIFEST_REL} has 1 CRLF and 16 LF; --sync-areas rewrites the whole file", output)

    def test_mixed_line_endings_are_refused_even_when_nothing_would_change(self):
        repo = self.repo(raw_manifest=canonical(base_manifest()).replace(b"\n", b"\r\n", 1))
        self.assertEqual(repo.errors(), [])
        self.assert_refused(repo, "manifest mixes line endings")

    # --- refusals -----------------------------------------------------------------------------

    def test_a_missing_manifest_is_refused_and_none_is_created(self):
        repo = self.repo(manifest=False)
        self.assert_refused(repo, f"- manifest is missing: {MANIFEST_REL}")
        self.assertFalse((repo.root / MANIFEST_REL).exists())

    def test_a_manifest_that_is_not_json_is_refused(self):
        self.assert_refused(self.repo(raw_manifest=b'{"schema_version": 1, "core": ['), f"- manifest is malformed: {MANIFEST_REL}")

    def test_a_malformed_manifest_is_refused_and_no_core_is_invented(self):
        cases = {
            "manifest is malformed: core must be a non-empty list": lambda m: m.update(core=[]),
            "manifest is malformed: core must be a non-empty list ": lambda m: m.pop("core"),
            "manifest is malformed: core[0].why is empty": lambda m: m["core"][0].pop("why"),
            "manifest is malformed: core[1].bytes_max is '300'": lambda m: m["core"][1].update(bytes_max="300"),
            "manifest is malformed: core[0].path '../LAW.md' is not normalised": lambda m: m["core"][0].update(path="../LAW.md"),
            "manifest is malformed: schema_version is 2, expected 1": lambda m: m.update(schema_version=2),
            "manifest is malformed: total_bytes_max is None": lambda m: m.pop("total_bytes_max"),
        }
        for fragment, change in cases.items():
            with self.subTest(fragment=fragment):
                manifest = base_manifest()
                manifest["areas"] = {}
                change(manifest)
                self.assert_refused(self.repo(manifest=manifest), "- " + fragment.strip())

    def test_absent_or_malformed_areas_are_refused_not_read_as_empty(self):
        cases = {
            "absent": lambda m: m.pop("areas"),
            "null": lambda m: m.update(areas=None),
            "a list": lambda m: m.update(areas=["NOTES.md"]),
        }
        for name, change in cases.items():
            with self.subTest(name=name):
                manifest = base_manifest()
                change(manifest)
                self.assert_refused(self.repo(manifest=manifest), "- manifest is malformed: areas must be an object")
        manifest = base_manifest()
        manifest["areas"]["docs"] = []
        self.assert_refused(self.repo(manifest=manifest), "- manifest is malformed: area 'docs' must be a non-empty list of files")

    def test_a_directory_that_is_not_a_git_repository_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / MANIFEST_REL
            path.parent.mkdir(parents=True)
            start = base_manifest()
            start["areas"] = {}
            path.write_bytes(canonical(start))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = gate.main(["--root", str(root), "--sync-areas"])
            self.assertEqual(code, 1, out.getvalue())
            self.assertIn("cannot enumerate tracked files with git ls-files -z", out.getvalue())
            self.assertEqual(path.read_bytes(), canonical(start))

    def test_a_manifest_that_cannot_be_written_is_refused(self):
        repo = self.with_areas({})
        errors, lines = gate.sync_areas(repo.root, "no/such/dir.json")
        self.assertEqual((errors, lines), (["manifest is missing: no/such/dir.json"], []))
        path = repo.root / MANIFEST_REL
        before = path.read_bytes()
        path.chmod(0o444)
        self.addCleanup(path.chmod, 0o644)
        if os.access(path, os.W_OK):
            self.skipTest("this user can write a read-only file")
        self.assert_refused(repo, f"- manifest cannot be written: {MANIFEST_REL}")
        self.assertEqual(path.read_bytes(), before)

    def test_sync_areas_excludes_the_receipt_modes(self):
        repo = self.with_areas({})
        before = self.raw(repo)
        for other in (["--receipt"], ["--verify-receipt", "0" * 64]):
            for argv in (["--sync-areas", *other], [*other, "--sync-areas"]):
                with self.subTest(argv=argv):
                    err = io.StringIO()
                    with self.assertRaises(SystemExit) as raised, contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
                        gate.main(["--root", str(repo.root), *argv])
                    self.assertEqual(raised.exception.code, 2)
                    self.assertIn("not allowed with argument", err.getvalue())
                    self.assertEqual(self.raw(repo), before)

    def test_the_default_mode_does_not_write_and_does_not_require_the_synced_grouping(self):
        repo = self.with_areas({"src": ["NOTES.md", "docs/GUIDE.md", ARMENIAN_NAME]})
        before = self.raw(repo)
        self.assertEqual(repo.cli()[0], 0)
        self.assertEqual(self.raw(repo), before)

    # --- the two entry points and this repository --------------------------------------------

    def test_the_standards_own_manifest_is_a_fixed_point(self):
        manifest = json.loads((gate.DEFAULT_ROOT / MANIFEST_REL).read_text(encoding="utf-8"))
        self.assertEqual(gate.shape_errors(manifest), [])
        areas, changes = gate.repaired_areas(gate.DEFAULT_ROOT, manifest, gate.tracked_files(gate.DEFAULT_ROOT))
        self.assertEqual(list(areas.items()), list(manifest["areas"].items()))
        self.assertEqual(changes, {"added": [], "dead": [], "core": [], "emptied": [], "absent": [], "no_directory": []})

    def test_both_entry_points_run_the_mode_as_scripts(self):
        start = base_manifest()
        start["areas"] = {}
        entry = self.repo(manifest=start)
        result = subprocess.run(
            [sys.executable, str(Path(gate.__file__)), "--root", str(entry.root), "--sync-areas"],
            capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"SESSION READ AREAS: WRITTEN (3 area files in 2 directories; 3 added, 0 removed) to {MANIFEST_REL}", result.stdout)
        self.assertEqual(self.manifest(entry)["areas"], base_manifest()["areas"])

        product = self.repo(manifest=False)
        product.write(gate.kit.MANIFEST_REL, canonical(start))
        product.add()
        kit_gate = OneImplementation.KIT_GATE
        result = subprocess.run([sys.executable, str(kit_gate), "--sync-areas"], cwd=product.root, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("SESSION READ AREAS: WRITTEN (3 area files in 2 directories; 3 added, 0 removed) to SESSION_READ_MANIFEST.json", result.stdout)
        self.assertEqual((product.root / gate.kit.MANIFEST_REL).read_bytes(), canonical(base_manifest()))
        result = subprocess.run([sys.executable, str(kit_gate)], cwd=product.root, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        refused = self.repo(manifest=False)
        result = subprocess.run([sys.executable, str(kit_gate), "--sync-areas"], cwd=refused.root, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(result.stdout.splitlines(), ["SESSION READ AREAS: RED", "- manifest is missing: SESSION_READ_MANIFEST.json", "- nothing was written"])


if __name__ == "__main__":
    unittest.main()
