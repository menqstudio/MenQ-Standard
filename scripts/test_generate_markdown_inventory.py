#!/usr/bin/env python3
"""Tests for generate_markdown_inventory.py.

Every check in ``--check`` has a test here that breaks exactly its subject in a temporary git
repository and asserts RED with the specific message, next to positive controls that are GREEN.
The fixture is a copy of this repository's own tracked files.  Fixture files are written as
bytes, never as text, so the tests behave the same on a platform that checks out with CRLF.  Run:

    python scripts/test_generate_markdown_inventory.py
"""

from __future__ import annotations

import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
import generate_markdown_inventory as gen  # noqa: E402

SCRIPT = "scripts/generate_markdown_inventory.py"
INVENTORY = "foundation/ai-collaboration/MARKDOWN_INVENTORY.json"
END = re.compile(r"\n*<!-- END: [A-Za-z0-9_.-]+ -->\s*$")
_BASE: Path | None = None


def _force_remove(function, path, _info) -> None:
    os.chmod(path, stat.S_IWRITE)
    function(path)


def setUpModule() -> None:
    """Copy the tracked files of the real repository into one base git repository."""
    global _BASE
    _BASE = Path(tempfile.mkdtemp(prefix="menq-inventory-base-"))
    listing = subprocess.run(["git", "ls-files", "-z"], cwd=REPO, check=True, capture_output=True).stdout
    for rel in filter(None, listing.decode("utf-8").split("\0")):
        if (REPO / rel).is_file():
            (_BASE / rel).parent.mkdir(parents=True, exist_ok=True)
            (_BASE / rel).write_bytes((REPO / rel).read_bytes())
    for args in (("init", "-q"), ("config", "core.autocrlf", "false"), ("config", "core.quotepath", "true"), ("add", "-A")):
        subprocess.run(["git", *args], cwd=_BASE, check=True, capture_output=True)


def tearDownModule() -> None:
    if _BASE is not None:
        shutil.rmtree(_BASE, onerror=_force_remove)


class Repo:
    def __init__(self, root: Path) -> None:
        self.root = root

    def read(self, rel: str) -> str:
        return (self.root / rel).read_bytes().decode("utf-8")

    def write(self, rel: str, text: str | bytes) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text if isinstance(text, bytes) else text.encode("utf-8"))

    def sub(self, rel: str, old: str, new: str, count: int = 1) -> None:
        text = self.read(rel)
        assert old in text, f"{old!r} is not in {rel}: the mutation would change nothing"
        self.write(rel, text.replace(old, new, count))

    def resub(self, rel: str, pattern: str, replacement: str, count: int = 1) -> None:
        text, changed = re.subn(pattern, replacement, self.read(rel), count=count, flags=re.M)
        assert changed, f"{pattern!r} matches nothing in {rel}: the mutation would change nothing"
        self.write(rel, text)

    def before_end(self, rel: str, addition: str) -> None:
        text = self.read(rel)
        match = END.search(text)
        assert match, f"{rel} has no trailing END marker"
        self.write(rel, text[: match.start()] + "\n\n" + addition.strip("\n") + text[match.start():])

    def git(self, *args: str) -> None:
        subprocess.run(["git", *args], cwd=self.root, check=True, capture_output=True)

    def run(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, *args], cwd=self.root, capture_output=True, text=True, encoding="utf-8"
        )


class Case(unittest.TestCase):
    maxDiff = None

    def fresh(self) -> Repo:
        root = Path(tempfile.mkdtemp(prefix="menq-inventory-"))
        self.addCleanup(shutil.rmtree, root, onerror=_force_remove)
        shutil.copytree(_BASE, root, dirs_exist_ok=True)
        return Repo(root)

    def check(self, repo: Repo, add: bool = True) -> subprocess.CompletedProcess:
        if add:
            repo.git("add", "-A")
        return repo.run(SCRIPT, "--check")

    def assertRed(self, result: subprocess.CompletedProcess, *needles: str) -> None:
        output = result.stdout + result.stderr
        self.assertNotIn("Traceback", output)
        self.assertEqual(result.returncode, 1, output)
        self.assertTrue(result.stdout.startswith("MARKDOWN INVENTORY: RED - "), output)
        for needle in needles:
            self.assertIn(needle, result.stdout)

    def assertGreen(self, result: subprocess.CompletedProcess, count: int | None = None) -> None:
        self.assertRegex(result.stdout, r"\AMARKDOWN INVENTORY: GREEN \(\d+ files\)\n\Z")
        self.assertEqual((result.returncode, result.stderr), (0, ""))
        if count is not None:
            self.assertIn(f"({count} files)", result.stdout)


def _manifest(mutate):
    def apply(r: Repo) -> None:
        data = json.loads(r.read(INVENTORY))
        mutate(data)
        r.write(INVENTORY, json.dumps(data, ensure_ascii=False, separators=(",", ":")))

    return apply


NOTE = "# Note / Նշում\n\n**HY:** Հայերեն տեքստ։\n\n**EN:** English text.\n\n<!-- END: NOTE -->\n"

# (test name, mutation, RED lines expected, leave the index alone)
RED_CASES = [
    ("manifest_missing", lambda r: (r.root / INVENTORY).unlink(), ["RED - missing " + INVENTORY], True),
    ("manifest_not_json", lambda r: r.write(INVENTORY, "{not json"), ["RED - manifest is not valid UTF-8 JSON"], False),
    ("manifest_not_utf8", lambda r: r.write(INVENTORY, b'{"files": "\xff"}'), ["RED - manifest is not valid UTF-8 JSON"], False),
    ("manifest_not_an_object", lambda r: r.write(INVENTORY, "[]"), ["RED - manifest must be a JSON object with a 'files' list"], False),
    ("manifest_files_not_a_list", _manifest(lambda d: d.__setitem__("files", {})), ["RED - manifest must be a JSON object with a 'files' list"], False),
    ("manifest_entry_without_path", _manifest(lambda d: d["files"].__setitem__(0, "README.md")), ["manifest contains entries without a path"], False),
    ("tracked_file_not_in_manifest", lambda r: r.write("docs/new.md", NOTE), ["RED - path list does not match tracked Markdown files", "- not in the manifest: docs/new.md"], False),
    ("manifest_lists_untracked_path", _manifest(lambda d: (d["files"].append({"path": "zzz.md", "bytes": 1, "sha256": "0" * 64}), d.__setitem__("file_count", d["file_count"] + 1))), ["RED - path list does not match tracked Markdown files", "- not a tracked Markdown file: zzz.md"], False),
    ("manifest_order_differs", _manifest(lambda d: d["files"].reverse()), ["RED - path list does not match tracked Markdown files", "- same paths, different order or a duplicate"], False),
    ("manifest_entry_stale", lambda r: r.write("ROADMAP.md", r.read("ROADMAP.md") + "\n"), ["RED - stale entry for ROADMAP.md"], False),
    ("manifest_entry_carries_an_extra_key", _manifest(lambda d: d["files"][0].__setitem__("note", "x")), ["RED - stale entry for "], False),
    ("manifest_file_count_wrong", _manifest(lambda d: d.__setitem__("file_count", 1)), ["RED - file_count: manifest=1 expected="], False),
    ("manifest_source_wrong", _manifest(lambda d: d.__setitem__("source", "git ls-files -- *.md *.MD")), ["RED - source: manifest='git ls-files -- *.md *.MD'"], False),
    ("manifest_schema_version_wrong", _manifest(lambda d: d.__setitem__("schema_version", 2)), ["RED - schema_version: manifest=2 expected=1"], False),
    ("manifest_repository_wrong", _manifest(lambda d: d.__setitem__("repository", "x/y")), ["RED - repository: manifest='x/y'"], False),
    ("manifest_not_canonically_serialised", lambda r: r.write(INVENTORY, json.dumps(json.loads(r.read(INVENTORY)), ensure_ascii=False, indent=2)), ["RED - manifest is not in the generator's canonical serialisation; run --write"], False),
    ("tracked_markdown_missing_from_checkout", lambda r: (r.root / "ROADMAP.md").unlink(), ["RED - tracked Markdown file is missing from the checkout: ROADMAP.md"], True),
    ("not_a_git_repository", lambda r: shutil.rmtree(r.root / ".git", onerror=_force_remove), ["RED - cannot enumerate tracked files with git ls-files -z"], True),
]


def _red_test(mutate, needles, leave_index):
    def test(self: Case) -> None:
        repo = self.fresh()
        mutate(repo)
        self.assertRed(self.check(repo, add=not leave_index), *needles)

    return test


class RedCases(Case):
    """Generated: one test per row of RED_CASES."""


for _name, _mutate, _needles, _leave in RED_CASES:
    assert not hasattr(RedCases, "test_" + _name), _name
    setattr(RedCases, "test_" + _name, _red_test(_mutate, _needles, _leave))


class GreenControls(Case):
    def test_real_repository_is_green(self) -> None:
        self.assertGreen(self.check(self.fresh()))

    def test_write_reproduces_the_committed_manifest_byte_for_byte(self) -> None:
        repo = self.fresh()
        committed = (repo.root / INVENTORY).read_bytes()
        written = repo.run(SCRIPT, "--write")
        self.assertEqual((written.returncode, written.stderr), (0, ""))
        self.assertRegex(written.stdout, r"\AMARKDOWN INVENTORY: WRITTEN \(\d+ files\)\n\Z")
        self.assertEqual((repo.root / INVENTORY).read_bytes(), committed)
        self.assertNotIn(b"\n", committed)
        self.assertNotIn(b"\r", committed)

    def test_names_with_a_space_non_ascii_and_upper_case_extension(self) -> None:
        # Item 10: a non-ASCII name was a RuntimeError; item 9: "NOTE.MD" must be listed by both scripts.
        repo = self.fresh()
        before = json.loads(repo.read(INVENTORY))["file_count"]
        names = ["docs/NOTE.MD", "docs/my note.md", "docs/նշում.md"]
        for rel in names:
            repo.write(rel, NOTE)
        repo.write("docs/not-markdown.mdx", NOTE)
        repo.git("add", "-A")
        self.assertRed(repo.run(SCRIPT, "--check"), "- not in the manifest: docs/նշում.md", "- not in the manifest: docs/my note.md", "- not in the manifest: docs/NOTE.MD")
        self.assertEqual(repo.run(SCRIPT, "--write").returncode, 0)
        self.assertGreen(self.check(repo), before + 3)
        listed = [entry["path"] for entry in json.loads(repo.read(INVENTORY))["files"]]
        self.assertEqual(listed, sorted(listed))
        self.assertTrue(set(names) <= set(listed))
        self.assertNotIn("docs/not-markdown.mdx", listed)

    def test_untracked_markdown_is_not_inventoried(self) -> None:
        repo = self.fresh()
        repo.write("docs/untracked.md", NOTE)
        self.assertGreen(self.check(repo, add=False))

    def test_write_refuses_without_writing_when_a_tracked_file_is_missing(self) -> None:
        repo = self.fresh()
        committed = (repo.root / INVENTORY).read_bytes()
        (repo.root / "ROADMAP.md").unlink()
        result = repo.run(SCRIPT, "--write")
        self.assertRed(result, "RED - tracked Markdown file is missing from the checkout: ROADMAP.md")
        self.assertEqual((repo.root / INVENTORY).read_bytes(), committed)

    def test_exactly_one_mode_is_required(self) -> None:
        repo = self.fresh()
        for args in ((), ("--write", "--check")):
            result = repo.run(SCRIPT, *args)
            self.assertEqual(result.returncode, 2)
            self.assertIn("choose exactly one of --write or --check", result.stderr)

    def test_entries_record_size_and_digest_of_the_bytes_on_disk(self) -> None:
        import hashlib

        repo = self.fresh()
        for entry in json.loads(repo.read(INVENTORY))["files"][:5]:
            data = (repo.root / entry["path"]).read_bytes()
            self.assertEqual((entry["bytes"], entry["sha256"]), (len(data), hashlib.sha256(data).hexdigest()))
        self.assertEqual(json.loads(repo.read(INVENTORY))["source"], gen.SOURCE)


class Guard(unittest.TestCase):
    def test_an_unexpected_exception_in_a_check_is_a_red_line_not_a_traceback(self) -> None:
        import contextlib
        import io

        def boom(*_args):
            raise RuntimeError("boom")

        self.addCleanup(setattr, gen, "check", gen.check)
        gen.check = boom
        self.addCleanup(setattr, sys, "argv", sys.argv)
        sys.argv = ["generate_markdown_inventory.py", "--check"]
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            code = gen.main()
        self.assertEqual(code, 1)
        self.assertIn("MARKDOWN INVENTORY: RED - internal error: RuntimeError: boom\n", captured.getvalue())


if __name__ == "__main__":
    unittest.main()
