#!/usr/bin/env python3
"""Tests for generate_kit_manifest.py.

The fixture is a temporary git repository holding a byte copy of this checkout's consumer/
directory, so the real kit and the real checker are what the generator reads.  Each check has a
test that breaks exactly its subject and asserts RED with the specific message.  Run:

    python scripts/test_generate_kit_manifest.py
"""

from __future__ import annotations

import contextlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
import generate_kit_manifest as gkm  # noqa: E402

MANIFEST = "consumer/KIT_MANIFEST.json"


def git(root: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


class Fixture:
    def __init__(self, case: unittest.TestCase) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="menq-kit-manifest-"))
        case.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        for rel in (*gkm.KIT_FILES, gkm.MANIFEST_NAME):
            self.write(f"consumer/{rel}", (REPO / "consumer" / rel).read_bytes())
        git(self.root, "init", "--quiet")
        git(self.root, "config", "core.autocrlf", "false")
        self.add()

    def write(self, rel: str, data: bytes) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def read(self, rel: str) -> bytes:
        return (self.root / rel).read_bytes()

    def add(self) -> None:
        git(self.root, "add", "--all")

    def manifest(self) -> dict:
        return json.loads(self.read(MANIFEST).decode("utf-8"))

    def change_manifest(self, change) -> None:
        document = self.manifest()
        change(document)
        self.write(MANIFEST, (json.dumps(document, indent=2) + "\n").encode("utf-8"))

    def run(self, mode: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = gkm.main([mode, "--root", str(self.root)])
        return code, out.getvalue()


class Case(unittest.TestCase):
    def assert_red(self, fixture: Fixture, *fragments: str, mode: str = "--check") -> str:
        code, out = fixture.run(mode)
        self.assertNotIn("Traceback", out)
        self.assertEqual(code, 1, out)
        self.assertEqual(out.splitlines()[0], "KIT MANIFEST: RED", out)
        for fragment in fragments:
            self.assertIn(fragment, out)
        return out

    def assert_green(self, fixture: Fixture) -> None:
        code, out = fixture.run("--check")
        self.assertEqual((code, out), (0, f"KIT MANIFEST: GREEN ({len(gkm.KIT_FILES)} kit files)\n"))


class GreenControls(Case):
    def test_this_repository_is_green(self) -> None:
        self.assertEqual(gkm.check(REPO), [])

    def test_fixture_is_green(self) -> None:
        self.assert_green(Fixture(self))

    def test_crlf_checkout_of_a_kit_file_is_not_drift(self) -> None:
        fixture = Fixture(self)
        for rel in gkm.KIT_FILES:
            data = fixture.read(f"consumer/{rel}")
            self.assertNotIn(b"\r\n", data, rel)
            fixture.write(f"consumer/{rel}", data.replace(b"\n", b"\r\n"))
        self.assert_green(fixture)

    def test_write_is_deterministic_and_then_green(self) -> None:
        fixture = Fixture(self)
        fixture.write("consumer/SYNC_FACTS.md", b"# changed\n")
        self.assert_red(fixture, "kit manifest hash drift for SYNC_FACTS.md")
        self.assertEqual(fixture.run("--write"), (0, f"KIT MANIFEST: WRITTEN ({len(gkm.KIT_FILES)} kit files)\n"))
        first = fixture.read(MANIFEST)
        fixture.run("--write")
        self.assertEqual(fixture.read(MANIFEST), first)
        self.assertTrue(first.endswith(b"}\n"))
        self.assertNotIn(b"\r", first)
        self.assert_green(fixture)

    def test_manifest_names_the_hash_rule_of_the_checker(self) -> None:
        document = Fixture(self).manifest()
        checker = gkm.load_checker(REPO)
        self.assertEqual(document["hash"], checker.HASH_RULE)
        self.assertEqual(sorted(document["files"]), sorted(gkm.KIT_FILES))
        self.assertEqual(document["files"]["sync_facts.py"], checker.kit_hash((REPO / "consumer/sync_facts.py").read_bytes()))


class Drift(Case):
    def test_kit_file_changed_after_the_manifest_was_written(self) -> None:
        fixture = Fixture(self)
        fixture.write("consumer/check_conformance.py", fixture.read("consumer/check_conformance.py") + b"# edited\n")
        out = self.assert_red(fixture, "kit manifest hash drift for check_conformance.py: recorded ")
        self.assertEqual(len(out.splitlines()), 2, out)

    def test_manifest_lists_a_file_that_is_not_in_the_kit(self) -> None:
        fixture = Fixture(self)
        fixture.change_manifest(lambda d: d["files"].update({"ghost.py": "0" * 64}))
        self.assert_red(fixture, "kit manifest lists a file that is not in the kit: ghost.py")

    def test_manifest_does_not_list_a_kit_file(self) -> None:
        fixture = Fixture(self)
        fixture.change_manifest(lambda d: d["files"].pop("ADOPTION.md"))
        self.assert_red(fixture, "kit manifest does not list kit file: ADOPTION.md")

    def test_manifest_header_fields(self) -> None:
        for field, value in (("schema_version", 2), ("repository", "someone/Fork"), ("kit_dir", "kit"), ("hash", "sha256 of raw bytes"), ("extra", 1)):
            with self.subTest(field=field):
                fixture = Fixture(self)
                fixture.change_manifest(lambda d, field=field, value=value: d.update({field: value}))
                self.assert_red(fixture, f"kit manifest field '{field}' is {value!r}, expected ")


class ManifestFile(Case):
    def test_missing(self) -> None:
        fixture = Fixture(self)
        (fixture.root / MANIFEST).unlink()
        self.assert_red(fixture, "kit manifest is missing: consumer/KIT_MANIFEST.json")

    def test_not_tracked(self) -> None:
        fixture = Fixture(self)
        git(fixture.root, "rm", "--quiet", "--cached", MANIFEST)
        self.assert_red(fixture, "kit manifest is not tracked by git: consumer/KIT_MANIFEST.json")

    def test_not_json_not_utf8_not_an_object(self) -> None:
        for raw, message in ((b"{", "kit manifest is malformed"), (b"\xff", "kit manifest is malformed"), (b"[]", "top level must be an object")):
            with self.subTest(raw=raw):
                fixture = Fixture(self)
                fixture.write(MANIFEST, raw)
                self.assert_red(fixture, message)

    def test_files_not_an_object(self) -> None:
        fixture = Fixture(self)
        fixture.change_manifest(lambda d: d.update(files=[]))
        self.assert_red(fixture, "kit manifest 'files' must be an object")


class KitDirectory(Case):
    def test_file_dropped_into_the_kit_directory(self) -> None:
        fixture = Fixture(self)
        fixture.write("consumer/extra_tool.py", b"x = 1\n")
        fixture.add()
        for mode in ("--check", "--write"):
            with self.subTest(mode=mode):
                self.assert_red(fixture, "file under consumer/ is neither a declared kit file nor the manifest: consumer/extra_tool.py", mode=mode)

    def test_untracked_file_in_the_kit_directory_is_not_seen(self) -> None:
        # Stated, not hidden: the generator reads tracked files, so an untracked file is invisible to it.
        fixture = Fixture(self)
        fixture.write("consumer/untracked.py", b"x = 1\n")
        self.assert_green(fixture)

    def test_declared_kit_file_not_tracked(self) -> None:
        fixture = Fixture(self)
        git(fixture.root, "rm", "--quiet", "--cached", "consumer/sync_facts.py")
        self.assert_red(fixture, "declared kit file is not tracked by git: consumer/sync_facts.py")

    def test_declared_kit_file_missing_from_the_checkout(self) -> None:
        fixture = Fixture(self)
        (fixture.root / "consumer/templates/menq-standard-update.yml").unlink()
        self.assert_red(fixture, "declared kit file is missing from the checkout: consumer/templates/menq-standard-update.yml")

    def test_file_the_checker_needs_must_be_declared(self) -> None:
        fixture = Fixture(self)
        self.addCleanup(setattr, gkm, "KIT_FILES", gkm.KIT_FILES)
        gkm.KIT_FILES = tuple(rel for rel in gkm.KIT_FILES if rel != "sync_facts.py")
        self.assert_red(fixture, "the checker needs sync_facts.py, which is not a declared kit file")

    def test_kit_file_declared_twice(self) -> None:
        fixture = Fixture(self)
        self.addCleanup(setattr, gkm, "KIT_FILES", gkm.KIT_FILES)
        gkm.KIT_FILES = (*gkm.KIT_FILES, "sync_facts.py")
        self.assert_red(fixture, "a kit file is declared twice")

    def test_checker_that_cannot_be_loaded(self) -> None:
        fixture = Fixture(self)
        fixture.write("consumer/check_conformance.py", b"def broken(:\n")
        self.assert_red(fixture, "cannot load consumer/check_conformance.py: SyntaxError")

    def test_not_a_git_repository(self) -> None:
        fixture = Fixture(self)
        shutil.rmtree(fixture.root / ".git")
        self.assert_red(fixture, "cannot enumerate tracked files with git ls-files -z")


class CommandLine(Case):
    def test_runs_as_a_script_and_exits_non_zero_when_red(self) -> None:
        fixture = Fixture(self)
        command = [sys.executable, str(REPO / "scripts/generate_kit_manifest.py"), "--check", "--root", str(fixture.root)]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual((result.returncode, result.stdout.splitlines()[0]), (0, f"KIT MANIFEST: GREEN ({len(gkm.KIT_FILES)} kit files)"))
        fixture.write("consumer/SYNC_FACTS.md", b"# changed\n")
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual((result.returncode, result.stdout.splitlines()[0]), (1, "KIT MANIFEST: RED"), result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
