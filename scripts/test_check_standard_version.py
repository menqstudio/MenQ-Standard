#!/usr/bin/env python3
"""Tests for check_standard_version.py.

Each check has a test that breaks exactly its subject in a temporary git repository and asserts
RED with the specific message, next to GREEN controls.  Fixture files are written as bytes.  The
ref ``origin/main`` of a fixture is a local ref the test sets; nothing touches the network.  Run:

    python scripts/test_check_standard_version.py
"""

from __future__ import annotations

import contextlib
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
import check_standard_version as csv_gate  # noqa: E402

KIT_FILE = "consumer/check_conformance.py"
REUSABLE = ".github/workflows/consumer-conformance.yml"


def changelog(*versions: str) -> bytes:
    entries = "".join(f"## 2026-10-09 - an entry (MenQ Standard v{version})\n\n- text.\n\n" for version in versions)
    return ("# Changelog\n\n" + entries + "## 2026-07-12 - an entry that names no version\n\n- old.\n").encode("utf-8")


def git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
    return result.stdout.decode("utf-8").strip()


class Fixture:
    """A repository at version 2.0.0 with two commits; ``origin/main`` points at the second, ``base``."""

    def __init__(self, case: unittest.TestCase, version: bytes | None = b"2.0.0\n", origin: bool = True, root_only: bool = False) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="menq-version-"))
        case.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        git(self.root, "init", "--quiet", "--initial-branch", "work")
        for key, value in (("core.autocrlf", "false"), ("user.name", "Fixture"), ("user.email", "fixture@example.invalid")):
            git(self.root, "config", key, value)
        if version is not None:
            self.write("VERSION", version)
        self.write("CHANGELOG.md", changelog("2.0.0"))
        self.write(KIT_FILE, b"print('kit')\n")
        self.write(REUSABLE, b"on: workflow_call\n")
        self.write("README.md", b"# not part of the consumer interface\n")
        self.first = self.commit("root")
        self.base = self.first if root_only else self.commit("base")
        if origin:
            self.set_origin(self.base)

    def write(self, rel: str, data: bytes) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def commit(self, message: str) -> str:
        git(self.root, "add", "--all")
        git(self.root, "commit", "--quiet", "--allow-empty", "--message", message)
        return git(self.root, "rev-parse", "HEAD")

    def set_origin(self, commit: str) -> None:
        git(self.root, "update-ref", "refs/remotes/origin/main", commit)

    def bump(self, version: str) -> None:
        self.write("VERSION", f"{version}\n".encode())
        self.write("CHANGELOG.md", changelog(version, "2.0.0"))

    def run(self, *args: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = csv_gate.main(["--root", str(self.root), *args])
        return code, out.getvalue()


class Case(unittest.TestCase):
    def assert_red(self, fixture: Fixture, *fragments: str) -> str:
        code, out = fixture.run()
        self.assertNotIn("Traceback", out)
        self.assertEqual(code, 1, out)
        self.assertEqual(out.splitlines()[0], "STANDARD VERSION: RED", out)
        for fragment in fragments:
            self.assertIn(fragment, out)
        return out

    def assert_green(self, fixture: Fixture, version: str = "2.0.0") -> str:
        code, out = fixture.run()
        self.assertEqual(code, 0, out)
        self.assertEqual(out.splitlines()[0], f"STANDARD VERSION: GREEN ({version})", out)
        return out


class VersionFile(Case):
    def test_unchanged_repository_is_green(self) -> None:
        fixture = Fixture(self)
        out = self.assert_green(fixture)
        self.assertIn(f"compared the working tree with {fixture.first[:12]}, the first parent of HEAD", out)
        self.assertIn("consumer interface files changed against the base: 0", out)

    def test_this_repository_names_its_version_in_the_changelog(self) -> None:
        errors, version = csv_gate.static_errors(REPO)
        self.assertEqual(errors, [])
        self.assertEqual(version, (REPO / "VERSION").read_bytes().decode("ascii").strip())

    def test_missing(self) -> None:
        fixture = Fixture(self)
        (fixture.root / "VERSION").unlink()
        self.assert_red(fixture, "VERSION is missing")

    def test_not_one_line(self) -> None:
        for raw in (b"2.0.0", b"2.0.0\n2.0.1\n", b"2.0.0\n\n", b"", b"\n2.0.0\n"):
            with self.subTest(raw=raw):
                fixture = Fixture(self)
                fixture.write("VERSION", raw)
                self.assert_red(fixture, "VERSION must be exactly one line ending in a newline")

    def test_not_semantic(self) -> None:
        for raw in ("2.0", "v2.0.0", "02.0.0", "2.0.0-rc1", "2.0.0 ", "two"):
            with self.subTest(raw=raw):
                fixture = Fixture(self)
                fixture.write("VERSION", raw.encode() + b"\n")
                self.assert_red(fixture, f"VERSION is {raw!r}, not MAJOR.MINOR.PATCH")

    def test_not_utf8(self) -> None:
        fixture = Fixture(self)
        fixture.write("VERSION", b"\xff\n")
        self.assert_red(fixture, "VERSION is not valid UTF-8")

    def test_crlf_checkout_reads_the_same_version(self) -> None:
        fixture = Fixture(self)
        fixture.write("VERSION", b"2.0.0\r\n")
        fixture.write("CHANGELOG.md", changelog("2.0.0").replace(b"\n", b"\r\n"))
        self.assert_green(fixture)


class Changelog(Case):
    def test_missing(self) -> None:
        fixture = Fixture(self)
        (fixture.root / "CHANGELOG.md").unlink()
        self.assert_red(fixture, "CHANGELOG.md is missing")

    def test_no_heading_names_the_version(self) -> None:
        fixture = Fixture(self)
        fixture.write("VERSION", b"2.1.0\n")
        self.assert_red(fixture, "CHANGELOG.md has no '## ' heading naming MenQ Standard v2.1.0")

    def test_version_named_only_in_body_text_does_not_count(self) -> None:
        fixture = Fixture(self)
        fixture.write("VERSION", b"2.1.0\n")
        fixture.write("CHANGELOG.md", changelog("2.0.0") + b"\nMenQ Standard v2.1.0 is mentioned in a paragraph.\n")
        self.assert_red(fixture, "CHANGELOG.md has no '## ' heading naming MenQ Standard v2.1.0")

    def test_longer_version_is_not_a_match(self) -> None:
        fixture = Fixture(self)
        fixture.write("CHANGELOG.md", changelog("2.0.01", "2.0.0.1"))
        self.assert_red(fixture, "CHANGELOG.md has no '## ' heading naming MenQ Standard v2.0.0")

    def test_newest_heading_names_another_version(self) -> None:
        fixture = Fixture(self)
        fixture.write("CHANGELOG.md", changelog("2.1.0", "2.0.0"))
        self.assert_red(fixture, "the newest version heading of CHANGELOG.md names MenQ Standard v2.1.0, but VERSION is 2.0.0")

    def test_not_utf8(self) -> None:
        fixture = Fixture(self)
        fixture.write("CHANGELOG.md", b"\xff")
        self.assert_red(fixture, "CHANGELOG.md is not valid UTF-8")


class AgainstTheBase(Case):
    def test_kit_file_edited_and_not_committed(self) -> None:
        fixture = Fixture(self)
        fixture.write(KIT_FILE, b"print('kit, edited')\n")
        out = self.assert_red(fixture, f"the consumer interface changed and VERSION did not: it is 2.0.0 at the base and here; changed: {KIT_FILE}")
        self.assertEqual(len(out.splitlines()), 2, out)

    def test_kit_file_edited_and_committed(self) -> None:
        fixture = Fixture(self)
        fixture.write(KIT_FILE, b"print('kit, edited')\n")
        fixture.commit("a kit change with no version")
        self.assert_red(fixture, f"the consumer interface changed and VERSION did not", f"changed: {KIT_FILE}")

    def test_new_untracked_kit_file(self) -> None:
        fixture = Fixture(self)
        fixture.write("consumer/new_tool.py", b"x = 1\n")
        self.assert_red(fixture, "changed: consumer/new_tool.py")

    def test_kit_file_deleted(self) -> None:
        fixture = Fixture(self)
        (fixture.root / KIT_FILE).unlink()
        self.assert_red(fixture, f"changed: {KIT_FILE}")

    def test_reusable_workflow_changed(self) -> None:
        fixture = Fixture(self)
        fixture.write(REUSABLE, b"on: workflow_call\n# changed\n")
        self.assert_red(fixture, f"changed: {REUSABLE}")

    def test_many_changed_files_are_counted_not_all_listed(self) -> None:
        fixture = Fixture(self)
        for number in range(csv_gate.SHOWN + 3):
            fixture.write(f"consumer/file_{number:02}.py", b"x = 1\n")
        out = self.assert_red(fixture, "consumer/file_00.py", " and 3 more")
        self.assertNotIn(f"consumer/file_{csv_gate.SHOWN:02}.py", out)

    def test_change_outside_the_interface_needs_no_version(self) -> None:
        fixture = Fixture(self)
        fixture.write("README.md", b"# changed\n")
        fixture.write("scripts/tool.py", b"x = 1\n")
        fixture.commit("outside the consumer interface")
        self.assertIn("consumer interface files changed against the base: 0", self.assert_green(fixture))

    def test_kit_change_with_a_higher_version_is_green(self) -> None:
        for version in ("2.0.1", "2.1.0", "3.0.0", "2.10.0"):
            with self.subTest(version=version):
                fixture = Fixture(self)
                fixture.write(KIT_FILE, b"print('kit, edited')\n")
                fixture.bump(version)
                out = self.assert_green(fixture, version)
                self.assertIn(f"version at the base: 2.0.0; here: {version}", out)
                self.assertIn("consumer interface files changed against the base: 1", out)

    def test_version_may_move_without_a_kit_change(self) -> None:
        fixture = Fixture(self)
        fixture.bump("2.0.1")
        self.assert_green(fixture, "2.0.1")

    def test_version_went_backwards(self) -> None:
        fixture = Fixture(self)
        fixture.write("VERSION", b"1.9.9\n")
        fixture.write("CHANGELOG.md", changelog("1.9.9"))
        self.assert_red(fixture, "VERSION went backwards: 2.0.0 at the base, 1.9.9 here")

    def test_versions_compare_as_numbers(self) -> None:
        fixture = Fixture(self, version=b"2.9.0\n")
        fixture.write("CHANGELOG.md", changelog("2.9.0"))
        fixture.set_origin(fixture.commit("base at 2.9.0"))
        fixture.write(KIT_FILE, b"print('kit, edited')\n")
        fixture.bump("2.10.0")
        fixture.write("CHANGELOG.md", changelog("2.10.0", "2.9.0"))
        self.assert_green(fixture, "2.10.0")

    def test_base_without_a_version_file_is_the_introduction(self) -> None:
        fixture = Fixture(self, version=None)
        fixture.write("VERSION", b"2.0.0\n")
        fixture.write(KIT_FILE, b"print('kit, edited')\n")
        out = self.assert_green(fixture)
        self.assertIn("the base has no VERSION: this change introduces the version, at 2.0.0", out)
        self.assertIn(f"compared the working tree with {fixture.base[:12]}, HEAD itself, because HEAD is contained in origin/main", out)
        self.assertIn("consumer interface files changed against the base: 1", out)

    def test_base_with_a_malformed_version(self) -> None:
        fixture = Fixture(self, version=b"two\n")
        fixture.write("VERSION", b"2.0.0\n")
        self.assert_red(fixture, f"VERSION at the base {fixture.base[:12]} is 'two', not MAJOR.MINOR.PATCH")

    def test_branch_is_compared_with_its_merge_base_not_with_the_tip_of_main(self) -> None:
        # main moved on and changed the kit with a version; the branch did not touch the kit.
        fixture = Fixture(self)
        fixture.write("README.md", b"# branch work\n")
        fixture.commit("branch work")
        git(fixture.root, "checkout", "--quiet", "-b", "mainline", fixture.base)
        fixture.write(KIT_FILE, b"print('kit on main')\n")
        fixture.bump("2.1.0")
        fixture.set_origin(fixture.commit("main moved to 2.1.0"))
        git(fixture.root, "checkout", "--quiet", "work")
        out = self.assert_green(fixture)
        self.assertIn(f"compared the working tree with {fixture.base[:12]}, the merge base of HEAD and origin/main", out)

    def test_named_base(self) -> None:
        fixture = Fixture(self, origin=False)
        git(fixture.root, "branch", "release", fixture.base)
        fixture.write(KIT_FILE, b"print('kit, edited')\n")
        code, out = fixture.run("--base", "release")
        self.assertEqual((code, out.splitlines()[0]), (1, "STANDARD VERSION: RED"), out)
        self.assertIn("the consumer interface changed and VERSION did not", out)


class OnMainItself(Case):
    def test_head_contained_in_the_base_is_compared_with_its_first_parent(self) -> None:
        fixture = Fixture(self)
        fixture.write(KIT_FILE, b"print('kit, edited')\n")
        merged = fixture.commit("a kit change that reached main with no version")
        fixture.set_origin(merged)
        out = self.assert_red(fixture, "the consumer interface changed and VERSION did not")
        self.assertIn(f"changed: {KIT_FILE}", out)

    def test_head_contained_in_the_base_and_clean_is_green_and_says_how_it_compared(self) -> None:
        fixture = Fixture(self)
        fixture.write("README.md", b"# changed\n")
        fixture.set_origin(fixture.commit("outside the interface"))
        out = self.assert_green(fixture)
        self.assertIn(f"compared the working tree with {fixture.base[:12]}, the first parent of HEAD, because HEAD is contained in origin/main and the working tree is clean", out)


class NoBase(Case):
    def assert_not_run(self, fixture: Fixture, reason: str) -> None:
        code, out = fixture.run()
        self.assertEqual(code, 1, out)
        self.assertEqual(out.splitlines()[0], "STANDARD VERSION: BASE COMPARISON NOT RUN", out)
        self.assertIn(reason, out)
        self.assertIn("NOT checked: whether the consumer interface changed without a version change", out)
        self.assertNotIn("GREEN", out)
        allowed, out = fixture.run("--allow-no-base")
        self.assertEqual(allowed, 0, out)
        self.assertEqual(out.splitlines()[0], "STANDARD VERSION: BASE COMPARISON NOT RUN", out)
        self.assertNotIn("GREEN", out)

    def test_no_origin_main(self) -> None:
        self.assert_not_run(Fixture(self, origin=False), "the ref origin/main does not exist here")

    def test_root_commit_on_main_has_no_parent(self) -> None:
        self.assert_not_run(Fixture(self, root_only=True), "HEAD is contained in origin/main and has no parent to compare with")

    def test_uncommitted_work_on_a_root_commit_still_has_a_base(self) -> None:
        fixture = Fixture(self, root_only=True)
        fixture.write(KIT_FILE, b"print('kit, edited')\n")
        self.assert_red(fixture, "the consumer interface changed and VERSION did not")

    def test_not_a_git_repository(self) -> None:
        fixture = Fixture(self)
        shutil.rmtree(fixture.root / ".git")
        self.assert_not_run(fixture, "this is not a git repository")

    def test_repository_with_no_commit(self) -> None:
        fixture = Fixture(self)
        shutil.rmtree(fixture.root / ".git")
        git(fixture.root, "init", "--quiet")
        self.assert_not_run(fixture, "the repository has no commit")

    def test_unrelated_histories(self) -> None:
        fixture = Fixture(self, origin=False)
        git(fixture.root, "checkout", "--quiet", "--orphan", "elsewhere")
        fixture.set_origin(fixture.commit("an unrelated root"))
        git(fixture.root, "checkout", "--quiet", "work")
        self.assert_not_run(fixture, "HEAD and origin/main share no history here")

    def test_a_static_fault_is_red_even_without_a_base(self) -> None:
        fixture = Fixture(self, origin=False)
        fixture.write("VERSION", b"2.0\n")
        code, out = fixture.run("--allow-no-base")
        self.assertEqual((code, out.splitlines()[0]), (1, "STANDARD VERSION: RED"), out)


class CommandLine(Case):
    def test_runs_as_a_script(self) -> None:
        fixture = Fixture(self)
        fixture.write(KIT_FILE, b"print('kit, edited')\n")
        command = [sys.executable, str(REPO / "scripts/check_standard_version.py"), "--root", str(fixture.root)]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual((result.returncode, result.stdout.splitlines()[0]), (1, "STANDARD VERSION: RED"), result.stdout + result.stderr)
        fixture.bump("2.0.1")
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual((result.returncode, result.stdout.splitlines()[0]), (0, "STANDARD VERSION: GREEN (2.0.1)"), result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
