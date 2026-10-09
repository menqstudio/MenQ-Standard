#!/usr/bin/env python3
"""Tests for consumer/check_conformance.py, the checker a product repository runs (decision D-029).

Every check has a test that breaks exactly its subject and asserts RED with the specific message,
next to GREEN controls.  The fixtures are two real git repositories in a temporary directory: a
stand-in for MenQ Standard that holds the REAL kit files of this checkout, and a product
repository that adopted it through the real ``install`` command.  Every fixture file is written
as bytes.  Nothing touches the network.  Run:

    python scripts/test_check_conformance.py
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
KIT_SRC = REPO / "consumer"
sys.path.insert(0, str(REPO / "scripts"))
import generate_kit_manifest as gkm  # noqa: E402
import validate_foundation as vf  # noqa: E402

_spec = importlib.util.spec_from_file_location("menq_kit_check_conformance_under_test", KIT_SRC / "check_conformance.py")
cc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cc)

PIN = ".menq-standard.json"
KIT = "menq-standard"
CONFORMANCE = ".github/workflows/menq-standard-conformance.yml"
UPDATE = ".github/workflows/menq-standard-update.yml"
MANIFEST = "SESSION_READ_MANIFEST.json"
CHANGELOG_200 = (
    b"# Changelog\n\n"
    b"## 2026-10-09 - the consumer layer (MenQ Standard v2.0.0)\n\n- The kit.\n\n"
    b"## 2026-10-01 - an older entry\n\n- Older.\n"
)
_BASE: Path | None = None


def _force_remove(function, path, _info) -> None:
    os.chmod(path, stat.S_IWRITE)
    function(path)


def git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
    return result.stdout.decode("utf-8").strip()


def init(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    git(root, "init", "--quiet", "--initial-branch", "main")
    for key, value in (("core.autocrlf", "false"), ("user.name", "Fixture"), ("user.email", "fixture@example.invalid")):
        git(root, "config", key, value)


class Std:
    """A stand-in for MenQ Standard: the real kit, a VERSION, a changelog, real commits on main."""

    def __init__(self, root: Path) -> None:
        self.root = root

    def write(self, rel: str, data: bytes) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def read(self, rel: str) -> bytes:
        return (self.root / rel).read_bytes()

    def write_manifest(self) -> None:
        kit = self.root / "consumer"
        files = {
            path.relative_to(kit).as_posix(): cc.kit_hash(path.read_bytes())
            for path in sorted(kit.rglob("*"))
            if path.is_file() and path.name != "KIT_MANIFEST.json"
        }
        document = {"schema_version": 1, "repository": cc.STANDARD_REPOSITORY, "kit_dir": "consumer", "hash": cc.HASH_RULE, "files": files}
        self.write("consumer/KIT_MANIFEST.json", (json.dumps(document, indent=2) + "\n").encode("utf-8"))

    def commit(self, message: str) -> str:
        git(self.root, "add", "--all")
        git(self.root, "commit", "--quiet", "--message", message)
        return git(self.root, "rev-parse", "HEAD")

    def release(self, version: str, changes: dict[str, bytes | None], note: str = "a change") -> str:
        """Change kit files, move VERSION, name the version in the changelog, commit."""
        for rel, data in changes.items():
            if data is None:
                (self.root / "consumer" / rel).unlink()
            else:
                self.write(f"consumer/{rel}", data)
        self.write_manifest()
        self.write("VERSION", f"{version}\n".encode())
        old = self.read("CHANGELOG.md")
        head, _, rest = old.partition(b"## ")
        entry = f"## 2026-11-01 - {note} (MenQ Standard v{version})\n\n- {note}.\n\n".encode()
        self.write("CHANGELOG.md", head + entry + b"## " + rest)
        return self.commit(f"MenQ Standard {version}")

    @property
    def head(self) -> str:
        return git(self.root, "rev-parse", "HEAD")


def session_manifest(total: int = 20000, readme: int = 20000) -> dict:
    return {
        "schema_version": 1,
        "total_bytes_max": total,
        "core": [{"path": "README.md", "bytes_max": readme, "why": "What the repository is."}],
        "areas": {
            "docs": ["docs/GUIDE.md"],
            KIT: [f"{KIT}/ADOPTION.md", f"{KIT}/CONSUMER_CONTRACT.md", f"{KIT}/SYNC_FACTS.md"],
        },
    }


class Product:
    """A product repository.  ``run`` calls the checker of THIS checkout, as the reusable workflow does."""

    def __init__(self, root: Path, std: Std) -> None:
        self.root = root
        self.std = std

    def write(self, rel: str, data: bytes) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def read(self, rel: str) -> bytes:
        return (self.root / rel).read_bytes()

    def add(self) -> None:
        git(self.root, "add", "--all")

    def pin(self) -> dict:
        return json.loads(self.read(PIN).decode("utf-8"))

    def write_pin(self, pin: object) -> None:
        self.write(PIN, (json.dumps(pin, indent=2) + "\n").encode("utf-8"))

    def change_pin(self, change) -> None:
        pin = self.pin()
        change(pin)
        self.write_pin(pin)

    def write_session_manifest(self, document: dict, rel: str = MANIFEST) -> None:
        self.write(rel, (json.dumps(document, indent=2) + "\n").encode("utf-8"))
        self.add()

    def run(self, command: str, *args: str, standard: bool | str = True, consumer: bool = True) -> tuple[int, str, str]:
        argv = [command]
        if consumer:
            argv += ["--consumer", str(self.root)]
        if standard:
            argv += ["--standard", str(self.std.root), "--standard-ref", standard if isinstance(standard, str) else "main"]
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = cc.main([*argv, *args])
        return code, out.getvalue(), err.getvalue()

    def snapshot(self) -> dict[str, bytes]:
        return {
            path.relative_to(self.root).as_posix(): path.read_bytes()
            for path in sorted(self.root.rglob("*"))
            if path.is_file() and ".git/" not in path.relative_to(self.root).as_posix() + "/"
        }


def setUpModule() -> None:
    """One standard at 2.0.0 and one product that adopted it; every test works on a copy."""
    global _BASE
    _BASE = Path(tempfile.mkdtemp(prefix="menq-conformance-base-"))
    std = Std(_BASE / "std")
    init(std.root)
    std.write("README.md", b"# A stand-in for MenQ Standard\n")
    std.commit("before the consumer kit")
    for rel in gkm.KIT_FILES:
        std.write(f"consumer/{rel}", (KIT_SRC / rel).read_bytes())
    std.write("CHANGELOG.md", CHANGELOG_200)
    std.release("2.0.0", {}, "unused")
    std.write("CHANGELOG.md", CHANGELOG_200)
    git(std.root, "add", "--all")
    git(std.root, "commit", "--quiet", "--amend", "--no-edit")

    product = Product(_BASE / "product", std)
    init(product.root)
    product.write("README.md", b"# Product\n\nA product repository.\n")
    product.write("docs/GUIDE.md", b"# Guide\n")
    code, out, err = product.run("install", "--with-update-workflow")
    assert code == 0, out + err
    product.write_session_manifest(session_manifest())


def tearDownModule() -> None:
    if _BASE is not None:
        shutil.rmtree(_BASE, onerror=_force_remove)


class Case(unittest.TestCase):
    maxDiff = None

    def world(self) -> Product:
        root = Path(tempfile.mkdtemp(prefix="menq-conformance-"))
        self.addCleanup(shutil.rmtree, root, onerror=_force_remove)
        shutil.copytree(_BASE, root, dirs_exist_ok=True)
        return Product(root / "product", Std(root / "std"))

    def assert_green(self, product: Product, standard: bool | str = True) -> str:
        code, out, err = product.run("check", standard=standard)
        self.assertEqual((code, err), (0, ""), out)
        self.assertEqual(out.splitlines()[0], "MENQ STANDARD CONFORMANCE: GREEN", out)
        return out

    def assert_red(self, product: Product, *fragments: str, standard: bool | str = True) -> str:
        code, out, err = product.run("check", standard=standard)
        self.assertNotIn("Traceback", out + err)
        self.assertEqual(code, 1, out)
        self.assertEqual(out.splitlines()[0], "MENQ STANDARD CONFORMANCE: RED", out)
        for fragment in fragments:
            self.assertIn(fragment, out)
        return out


class GreenControls(Case):
    def test_adopted_repository_is_green_against_the_standard(self) -> None:
        product = self.world()
        out = self.assert_green(product)
        self.assertIn(f"pin: menqstudio/MenQ-Standard 2.0.0 @ {product.std.head}", out)
        self.assertIn("kit: 9 files in menq-standard/ match the pin, and nothing else is there", out)
        self.assertIn("session read: SESSION_READ_MANIFEST.json: core: 1 files", out)
        self.assertIn("sync_facts: NOT CONFIGURED", out)
        self.assertIn("standard: the pin's commit is on main, and its version, 9 kit hashes and 2 workflow hash(es)", out)

    def test_without_a_standard_green_says_what_was_not_checked(self) -> None:
        out = self.assert_green(self.world(), standard=False)
        self.assertIn("standard: NOT CHECKED", out)
        self.assertNotIn("the pin's commit is on", out)

    def test_the_fixture_kit_is_the_declared_kit(self) -> None:
        product = self.world()
        self.assertEqual(sorted(product.pin()["files"]), sorted(gkm.KIT_FILES))
        self.assertEqual(len(gkm.KIT_FILES), 9)

    def test_the_repository_copy_runs_as_a_script(self) -> None:
        product = self.world()
        base = [sys.executable, str(product.root / KIT / "check_conformance.py"), "check"]
        result = subprocess.run(base, cwd=product.root, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("MENQ STANDARD CONFORMANCE: GREEN", result.stdout)
        (product.root / MANIFEST).unlink()
        result = subprocess.run(base, cwd=product.root, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("MENQ STANDARD CONFORMANCE: RED", result.stdout)


class PinShape(Case):
    def test_pin_missing(self) -> None:
        product = self.world()
        (product.root / PIN).unlink()
        out = self.assert_red(product, "pin is missing: .menq-standard.json")
        self.assertEqual(len(out.splitlines()), 2, out)

    def test_pin_not_json_and_not_utf8(self) -> None:
        for raw in (b'{"schema_version": 1,', b"\xff\xfe{}"):
            with self.subTest(raw=raw):
                product = self.world()
                product.write(PIN, raw)
                self.assert_red(product, "pin is malformed: .menq-standard.json")

    def test_pin_top_level_not_an_object(self) -> None:
        product = self.world()
        product.write_pin(["files"])
        self.assert_red(product, "pin is malformed: top level must be an object")

    def test_each_malformed_field_is_named(self) -> None:
        sha = "0" * 64
        bad_commit = "A" * 40
        cases = {
            "unknown field": (lambda p: p.update(extra=1), "pin is malformed: unknown field 'extra'"),
            "schema version": (lambda p: p.update(schema_version=2), "pin is malformed: schema_version is 2, expected 1"),
            "standard not an object": (lambda p: p.update(standard="x"), "standard must be an object with exactly repository, version and commit"),
            "standard extra key": (lambda p: p["standard"].update(tag="v2"), "standard must be an object with exactly repository, version and commit"),
            "another repository": (lambda p: p["standard"].update(repository="someone/Fork"), "standard.repository is 'someone/Fork', expected 'menqstudio/MenQ-Standard'"),
            "version two parts": (lambda p: p["standard"].update(version="2.0"), "standard.version '2.0' is not MAJOR.MINOR.PATCH"),
            "version leading zero": (lambda p: p["standard"].update(version="2.00.0"), "standard.version '2.00.0' is not MAJOR.MINOR.PATCH"),
            "version not text": (lambda p: p["standard"].update(version=2), "standard.version 2 is not MAJOR.MINOR.PATCH"),
            "short commit": (lambda p: p["standard"].update(commit="abc1234"), "standard.commit 'abc1234' is not a full 40-character commit SHA"),
            "upper-case commit": (lambda p: p["standard"].update(commit=bad_commit), f"standard.commit '{bad_commit}' is not a full"),
            "kit dir nested": (lambda p: p.update(kit_dir="tools/menq"), "kit_dir 'tools/menq' must be one directory name"),
            "kit dir parent": (lambda p: p.update(kit_dir=".."), "kit_dir '..' must be one directory name"),
            "kit dir hidden": (lambda p: p.update(kit_dir=".git"), "kit_dir '.git' must be one directory name"),
            "kit dir not text": (lambda p: p.update(kit_dir=7), "kit_dir 7 must be one directory name"),
            "kit dir empty": (lambda p: p.update(kit_dir=""), "kit_dir '' must be one directory name"),
            "manifest outside": (lambda p: p.update(session_read_manifest="../M.json"), "session_read_manifest '../M.json' is not normalised"),
            "manifest absolute": (lambda p: p.update(session_read_manifest="/etc/M.json"), "session_read_manifest '/etc/M.json' is absolute"),
            "hash rule": (lambda p: p.update(hash="sha256 of the raw bytes"), "pin is malformed: hash is 'sha256 of the raw bytes'"),
            "files not an object": (lambda p: p.update(files=[]), "files must be a non-empty object"),
            "files empty": (lambda p: p.update(files={}), "files must be a non-empty object"),
            "file path escapes": (lambda p: p["files"].update({"../evil.py": sha}), "files path '../evil.py' is not normalised"),
            "file path backslash": (lambda p: p["files"].update({"a\\b.py": sha}), "files path 'a\\\\b.py' uses a backslash"),
            "file digest not hex": (lambda p: p["files"].update({"sync_facts.py": "abc"}), "files['sync_facts.py'] is not a sha256"),
            "file digest upper case": (lambda p: p["files"].update({"sync_facts.py": "A" * 64}), "files['sync_facts.py'] is not a sha256"),
            "workflows not an object": (lambda p: p.update(workflows=[]), "workflows must be an object"),
            "workflow not rendered by the kit": (lambda p: p["workflows"].update({".github/workflows/ci.yml": p["workflows"][CONFORMANCE]}), "workflows names '.github/workflows/ci.yml', which is not a workflow the kit renders"),
            "workflow record keys": (lambda p: p["workflows"][CONFORMANCE].pop("commit"), f"workflows['{CONFORMANCE}'] must have exactly template, commit and sha256"),
            "workflow template": (lambda p: p["workflows"][CONFORMANCE].update(template="templates/menq-standard-update.yml"), f"workflows['{CONFORMANCE}'].template is 'templates/menq-standard-update.yml'"),
            "workflow commit": (lambda p: p["workflows"][CONFORMANCE].update(commit="main"), f"workflows['{CONFORMANCE}'].commit is not a full 40-character commit SHA"),
            "workflow digest": (lambda p: p["workflows"][CONFORMANCE].update(sha256="x"), f"workflows['{CONFORMANCE}'].sha256 is not a sha256"),
            "conformance workflow not listed": (lambda p: p["workflows"].pop(CONFORMANCE), f"workflows does not list '{CONFORMANCE}'; conformance must run in CI"),
        }
        for name, (change, message) in cases.items():
            with self.subTest(case=name):
                product = self.world()
                product.change_pin(change)
                self.assert_red(product, message)

    def test_each_missing_field_is_named(self) -> None:
        for field in ("schema_version", "standard", "kit_dir", "session_read_manifest", "hash", "files", "workflows"):
            with self.subTest(field=field):
                product = self.world()
                product.change_pin(lambda p, field=field: p.pop(field))
                self.assert_red(product, f"pin is malformed: field '{field}' is missing")

    def test_each_file_the_checker_needs_must_be_pinned(self) -> None:
        for rel in cc.REQUIRED_KIT_FILES:
            with self.subTest(rel=rel):
                product = self.world()
                product.change_pin(lambda p, rel=rel: p["files"].pop(rel))
                self.assert_red(product, f"files does not list '{rel}', which the checker itself needs")
        self.assertEqual(len(cc.REQUIRED_KIT_FILES), 5)

    def test_the_update_workflow_is_optional(self) -> None:
        product = self.world()
        product.change_pin(lambda p: p["workflows"].pop(UPDATE))
        (product.root / UPDATE).unlink()
        self.assert_green(product)


class KitFiles(Case):
    def test_kit_file_edited_locally_is_named(self) -> None:
        product = self.world()
        rel = f"{KIT}/check_session_read_budget.py"
        product.write(rel, product.read(rel).replace(b"350_000", b"950_000"))
        out = self.assert_red(product, f"kit file does not match its pin: {rel} (pinned ", "a kit file is never edited", standard=False)
        self.assertEqual(len([line for line in out.splitlines() if line.startswith("- ")]), 1, out)

    def test_kit_file_deleted_is_named(self) -> None:
        product = self.world()
        (product.root / KIT / "SYNC_FACTS.md").unlink()
        out = self.assert_red(product, f"kit file is missing: {KIT}/SYNC_FACTS.md", standard=False)
        self.assertNotIn("does not match its pin", out)

    def test_nested_kit_file_deleted_is_named(self) -> None:
        product = self.world()
        (product.root / KIT / "templates/menq-standard-update.yml").unlink()
        self.assert_red(product, f"kit file is missing: {KIT}/templates/menq-standard-update.yml", standard=False)

    def test_pin_naming_a_hash_the_file_does_not_have(self) -> None:
        product = self.world()
        product.change_pin(lambda p: p["files"].update({"sync_facts.py": "0" * 64}))
        self.assert_red(product, f"kit file does not match its pin: {KIT}/sync_facts.py (pinned {'0' * 64}, found ", standard=False)

    def test_file_added_to_the_kit_directory_is_named(self) -> None:
        product = self.world()
        product.write(f"{KIT}/local_patch.py", b"print('mine')\n")
        self.assert_red(product, f"file in the kit directory is not listed in the pin: {KIT}/local_patch.py", standard=False)

    def test_bytecode_cache_in_the_kit_directory_is_not_a_kit_file(self) -> None:
        product = self.world()
        product.write(f"{KIT}/__pycache__/sync_facts.cpython-312.pyc", b"\x00")
        self.assert_green(product)

    def test_crlf_checkout_of_the_kit_and_workflows_is_not_an_edit(self) -> None:
        product = self.world()
        converted = 0
        for rel in [f"{KIT}/{name}" for name in product.pin()["files"]] + [CONFORMANCE, UPDATE]:
            data = product.read(rel)
            self.assertNotIn(b"\r\n", data)
            product.write(rel, data.replace(b"\n", b"\r\n"))
            self.assertNotEqual(product.read(rel), data)
            converted += 1
        self.assertEqual(converted, 11)
        self.assert_green(product)

    def test_hash_is_over_lf_normalised_bytes(self) -> None:
        self.assertEqual(cc.kit_hash(b"a\r\nb\r\n"), cc.kit_hash(b"a\nb\n"))
        self.assertNotEqual(cc.kit_hash(b"a\nb\n"), cc.kit_hash(b"a\nb"))
        self.assertNotEqual(cc.kit_hash(b"a\rb\n"), cc.kit_hash(b"a\nb\n"))
        self.assertEqual(cc.kit_hash(b"x\n"), "73cb3858a687a8494ca3323053016282f3dad39d42cf62ca4e79dda2aac7d9ac")


class Workflows(Case):
    def test_workflow_edited_is_named(self) -> None:
        product = self.world()
        product.write(CONFORMANCE, product.read(CONFORMANCE).replace(b"pull_request:", b"workflow_dispatch:"))
        self.assert_red(product, f"workflow file does not match its pin: {CONFORMANCE} (pinned ", "never edited", standard=False)

    def test_workflow_deleted_is_named(self) -> None:
        product = self.world()
        (product.root / CONFORMANCE).unlink()
        self.assert_red(product, f"workflow file is missing: {CONFORMANCE}", standard=False)

    def test_rendered_workflows_carry_the_commit_and_the_kit_directory(self) -> None:
        product = self.world()
        commit = product.std.head
        self.assertIn(f"consumer-conformance.yml@{commit}".encode(), product.read(CONFORMANCE))
        self.assertIn(f'checker="{KIT}/check_conformance.py"'.encode(), product.read(UPDATE))
        for rel in (CONFORMANCE, UPDATE):
            self.assertNotIn(b"__MENQ_", product.read(rel))

    def test_forged_workflow_is_green_alone_and_red_against_the_standard(self) -> None:
        # A repository rewrites its conformance workflow and re-pins the hash to match.
        product = self.world()
        forged = product.read(CONFORMANCE).replace(b"pull_request:", b"workflow_dispatch:")
        product.write(CONFORMANCE, forged)
        product.change_pin(lambda p: p["workflows"][CONFORMANCE].update(sha256=cc.kit_hash(forged)))
        self.assert_green(product, standard=False)
        self.assert_red(product, f"pin records a hash for {CONFORMANCE} that is not the standard's template rendered at ")

    def test_workflow_commit_that_is_not_in_the_standard(self) -> None:
        product = self.world()
        product.change_pin(lambda p: p["workflows"][UPDATE].update(commit="1" * 40))
        self.assert_red(product, f"pin names a workflow commit that does not exist in the standard: {UPDATE} at {'1' * 40}")

    def test_workflow_commit_that_is_not_on_main(self) -> None:
        product = self.world()
        git(product.std.root, "checkout", "--quiet", "-b", "side")
        side = product.std.release("2.0.1", {"SYNC_FACTS.md": b"# side\n"})
        git(product.std.root, "checkout", "--quiet", "main")
        product.change_pin(lambda p: p["workflows"][UPDATE].update(commit=side))
        self.assert_red(product, f"pin names a workflow commit that is not on the standard's main: {UPDATE} at {side}")


class SessionRead(Case):
    def test_manifest_missing(self) -> None:
        product = self.world()
        (product.root / MANIFEST).unlink()
        self.assert_red(product, "session-read manifest is missing: SESSION_READ_MANIFEST.json (D-028", standard=False)

    def test_read_set_over_its_declared_budget(self) -> None:
        product = self.world()
        product.write("README.md", b"# Product\n\n" + b"word " * 5000)
        product.add()
        out = self.assert_red(product, "session-read budget gate is RED: core total exceeds the budget: 25011 bytes, total_bytes_max is 20000", standard=False)
        self.assertIn("session-read budget gate is RED: core file exceeds its ceiling: README.md is 25011 bytes", out)

    def test_declared_budget_over_the_universal_ceiling(self) -> None:
        product = self.world()
        product.write_session_manifest(session_manifest(total=350_001))
        self.assert_red(product, "session-read budget gate is RED: total_bytes_max is 350001, above the universal ceiling 350000 (D-028)", standard=False)

    def test_declared_budget_at_the_universal_ceiling_is_green(self) -> None:
        product = self.world()
        product.write_session_manifest(session_manifest(total=350_000, readme=350_000))
        self.assert_green(product)

    def test_markdown_nobody_is_told_to_read(self) -> None:
        product = self.world()
        product.write("docs/ORPHAN.md", b"# orphan\n")
        product.add()
        self.assert_red(product, "session-read budget gate is RED: tracked Markdown file is in neither the core nor any area: docs/ORPHAN.md", standard=False)

    def test_manifest_that_is_not_json(self) -> None:
        product = self.world()
        product.write(MANIFEST, b"{")
        self.assert_red(product, "session-read budget gate is RED: manifest is malformed: SESSION_READ_MANIFEST.json", standard=False)

    def test_manifest_at_the_path_the_pin_names(self) -> None:
        product = self.world()
        document = product.read(MANIFEST)
        (product.root / MANIFEST).unlink()
        product.write("config/read.json", document)
        product.add()
        self.assert_red(product, "session-read manifest is missing: SESSION_READ_MANIFEST.json", standard=False)
        product.change_pin(lambda p: p.update(session_read_manifest="config/read.json"))
        self.assertIn("session read: config/read.json: core: 1 files", self.assert_green(product))

    def test_the_gate_that_judges_is_the_one_beside_the_checker(self) -> None:
        # The repository goes over budget, replaces its own gate with one that always says GREEN,
        # and re-pins the hash.  Alone that is "conformant"; judged from the standard it is RED twice.
        product = self.world()
        product.write("README.md", b"# Product\n\n" + b"word " * 5000)
        stub = b"print('SESSION READ BUDGET: GREEN')\n"
        product.write(f"{KIT}/check_session_read_budget.py", stub)
        product.change_pin(lambda p: p["files"].update({"check_session_read_budget.py": cc.kit_hash(stub)}))
        product.add()
        own = subprocess.run(
            [sys.executable, str(product.root / KIT / "check_conformance.py"), "check"],
            cwd=product.root, capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(own.returncode, 0, own.stdout + own.stderr)
        self.assert_red(
            product,
            "session-read budget gate is RED: core total exceeds the budget",
            "for check_session_read_budget.py; the standard at ",
        )


class Facts(Case):
    def configure(self, product: Product, value: str) -> None:
        config = {"facts": {"release": {"source": {"value": value}}}, "documents": ["README.md"]}
        product.write("config/doc-facts.json", json.dumps(config).encode("utf-8"))
        product.write("README.md", b"# Product\n\nRelease <!-- fact:release -->1.4.0<!-- /fact -->.\n")
        product.add()

    def test_configured_and_current_is_reported(self) -> None:
        product = self.world()
        self.configure(product, "1.4.0")
        self.assertIn("sync_facts: GREEN: every use of a declared fact equals its source; 1 fact(s), 1 use(s) in 1 file(s).", self.assert_green(product))

    def test_stale_fact_is_red_and_named(self) -> None:
        product = self.world()
        self.configure(product, "1.5.0")
        self.assert_red(
            product,
            "sync_facts --check is RED: README.md:3: `release` says `1.4.0`, the source says `1.5.0`",
            "sync_facts --check is RED: RED: 1 stale use(s)",
            standard=False,
        )
        self.assertIn(b">1.4.0<", product.read("README.md"), "a check must not write")

    def test_refused_configuration_is_red(self) -> None:
        product = self.world()
        self.configure(product, "1.4.0")
        product.write("config/doc-facts.json", b'{"facts": {}, "documents": ["README.md"]}')
        self.assert_red(product, "sync_facts --check is RED: RED: config/doc-facts.json declares no facts", standard=False)


class AgainstTheStandard(Case):
    def test_commit_that_does_not_exist_in_the_standard(self) -> None:
        product = self.world()
        product.change_pin(lambda p: p["standard"].update(commit="2" * 40))
        out = self.assert_red(product, f"pin names a commit that does not exist in the standard: {'2' * 40}")
        self.assertEqual(len([line for line in out.splitlines() if line.startswith("- ")]), 1, out)
        self.assert_green(product, standard=False)

    def test_commit_of_an_unmerged_branch(self) -> None:
        product = self.world()
        git(product.std.root, "checkout", "--quiet", "-b", "proposal")
        side = product.std.release("2.1.0", {"SYNC_FACTS.md": b"# not approved\n"})
        git(product.std.root, "checkout", "--quiet", "main")
        code, out, err = product.run("install", standard="proposal")
        self.assertEqual(code, 0, out + err)
        product.write_session_manifest(session_manifest())
        self.assert_green(product, standard="proposal")
        self.assert_red(product, f"pin names a commit that is not on the standard's main: {side}")

    def test_version_the_commit_does_not_have(self) -> None:
        product = self.world()
        product.change_pin(lambda p: p["standard"].update(version="2.5.0"))
        self.assert_red(product, "pin names version 2.5.0, but the standard at ", " is version 2.0.0")

    def test_kit_file_forged_together_with_its_pin(self) -> None:
        product = self.world()
        forged = product.read(f"{KIT}/sync_facts.py") + b"# local\n"
        product.write(f"{KIT}/sync_facts.py", forged)
        product.change_pin(lambda p: p["files"].update({"sync_facts.py": cc.kit_hash(forged)}))
        self.assert_green(product, standard=False)
        self.assert_red(product, f"pin records {cc.kit_hash(forged)} for sync_facts.py; the standard at ", " has ")

    def test_kit_file_dropped_together_with_its_pin(self) -> None:
        product = self.world()
        (product.root / KIT / "ADOPTION.md").unlink()
        product.change_pin(lambda p: p["files"].pop("ADOPTION.md"))
        document = session_manifest()
        document["areas"][KIT].remove(f"{KIT}/ADOPTION.md")
        product.write_session_manifest(document)
        self.assert_green(product, standard=False)
        self.assert_red(product, "pin does not list kit file ADOPTION.md, which the standard has at ")

    def test_file_pinned_that_the_standard_does_not_ship(self) -> None:
        product = self.world()
        product.write(f"{KIT}/extra.py", b"x = 1\n")
        product.change_pin(lambda p: p["files"].update({"extra.py": cc.kit_hash(b"x = 1\n")}))
        self.assert_green(product, standard=False)
        self.assert_red(product, "pin lists extra.py, which is not a kit file of the standard at ")

    def test_commit_older_than_the_kit(self) -> None:
        product = self.world()
        first = git(product.std.root, "rev-list", "--max-parents=0", "HEAD")
        product.change_pin(lambda p: p["standard"].update(commit=first))
        self.assert_red(product, f"the standard at {first[:12]} has no VERSION file: it predates the consumer kit")

    def test_standard_that_is_not_a_checkout_or_has_no_such_ref(self) -> None:
        product = self.world()
        code, out, _ = product.run("check", standard="no-such-branch")
        self.assertEqual((code, out.splitlines()[0]), (1, "MENQ STANDARD CONFORMANCE: RED"), out)
        self.assertIn("has no ref 'no-such-branch'", out)
        out_buffer = io.StringIO()
        with contextlib.redirect_stdout(out_buffer):
            plain = product.root.parent / "plain"
            plain.mkdir()
            code = cc.main(["check", "--consumer", str(product.root), "--standard", str(plain)])
        self.assertEqual(code, 1)
        self.assertIn("--standard is not a git checkout", out_buffer.getvalue())

    def test_kit_manifest_of_another_schema_is_refused(self) -> None:
        product = self.world()
        std = product.std
        document = json.loads(std.read("consumer/KIT_MANIFEST.json"))
        document["schema_version"] = 2
        std.write("consumer/KIT_MANIFEST.json", json.dumps(document).encode("utf-8"))
        std.write("VERSION", b"3.0.0\n")
        std.commit("a kit this checker does not know")
        code, out, _ = product.run("status")
        self.assertEqual(code, 1, out)
        self.assertIn("has kit manifest schema_version 2; this checker knows 1", out)


    def test_kit_manifest_that_is_not_json_or_not_a_hash_table_is_refused(self) -> None:
        for raw, message in (
            (b"{", "has a malformed consumer/KIT_MANIFEST.json:"),
            (b'{"schema_version": 1, "files": {"sync_facts.py": "not-a-digest"}}', "has a malformed consumer/KIT_MANIFEST.json: files is not a path-to-sha256 object"),
            (b'{"schema_version": 1, "files": {}}', "files is not a path-to-sha256 object"),
            (b'{"schema_version": 1, "files": {"../x.py": "' + b"0" * 64 + b'"}}', "files is not a path-to-sha256 object"),
        ):
            with self.subTest(raw=raw[:30]):
                product = self.world()
                product.std.write("consumer/KIT_MANIFEST.json", raw)
                product.std.write("VERSION", b"2.1.0\n")
                product.std.commit("a broken manifest")
                code, out, _ = product.run("status")
                self.assertEqual((code, out.splitlines()[0]), (1, "MENQ STANDARD STATUS: RED"), out)
                self.assertIn(message, out)

    def test_version_file_of_the_standard_that_is_not_a_version(self) -> None:
        product = self.world()
        product.std.write("VERSION", b"next\n")
        product.std.commit("a broken version")
        code, out, _ = product.run("status")
        self.assertEqual(code, 1, out)
        self.assertIn("has a VERSION that is not MAJOR.MINOR.PATCH: 'next'", out)

    def test_standard_without_a_kit_manifest(self) -> None:
        product = self.world()
        (product.std.root / "consumer/KIT_MANIFEST.json").unlink()
        product.std.commit("the manifest was deleted")
        code, out, _ = product.run("status")
        self.assertEqual(code, 1, out)
        self.assertIn("carries no consumer kit (consumer/KIT_MANIFEST.json is absent)", out)


class Status(Case):
    def test_current(self) -> None:
        product = self.world()
        code, out, _ = product.run("status")
        self.assertEqual(code, 0, out)
        self.assertEqual(out.splitlines()[0], "MENQ STANDARD STATUS: CURRENT")
        self.assertIn("kit files that differ: none", out)

    def test_standard_moved_without_a_new_version_is_current(self) -> None:
        product = self.world()
        product.std.write("README.md", b"# A stand-in, edited\n")
        moved = product.std.commit("a change outside the kit")
        code, out, _ = product.run("status")
        self.assertEqual(code, 0, out)
        self.assertIn(f"standard: 2.0.0 @ {moved} (main)", out)

    def test_behind_lists_exactly_the_files_that_differ(self) -> None:
        product = self.world()
        old = product.std.head
        new = product.std.release(
            "2.1.0",
            {"SYNC_FACTS.md": b"# rewritten\n", "NEW_TOOL.py": b"print('new')\n", "test_sync_facts.py": None},
            "three kit changes",
        )
        code, out, _ = product.run("status")
        self.assertEqual(code, cc.EXIT_BEHIND, out)
        self.assertEqual(
            out.splitlines(),
            [
                "MENQ STANDARD STATUS: BEHIND",
                f"pin:      2.0.0 @ {old}",
                f"standard: 2.1.0 @ {new} (main)",
                "kit files that differ (3):",
                "  added    NEW_TOOL.py",
                "  changed  SYNC_FACTS.md",
                "  removed  test_sync_facts.py",
            ],
        )

    def test_behind_with_no_kit_change_says_so(self) -> None:
        product = self.world()
        product.std.release("2.0.1", {}, "a law changed, the kit did not")
        code, out, _ = product.run("status")
        self.assertEqual(code, cc.EXIT_BEHIND, out)
        self.assertIn("kit files that differ: none (the version moved, the kit did not)", out)

    def test_behind_names_a_workflow_a_person_must_re_render(self) -> None:
        product = self.world()
        old = product.std.head
        template = product.std.read("consumer/templates/menq-standard-conformance.yml")
        product.std.release("3.0.0", {"templates/menq-standard-conformance.yml": template + b"# changed\n"})
        code, out, _ = product.run("status")
        self.assertEqual(code, cc.EXIT_BEHIND, out)
        self.assertIn("workflows a person must re-render and push", out)
        self.assertIn(f"  {CONFORMANCE}  (template templates/menq-standard-conformance.yml changed since {old[:12]})", out)
        self.assertNotIn(f"  {UPDATE}  ", out)

    def test_kit_changed_without_a_version_is_the_standards_defect(self) -> None:
        product = self.world()
        product.std.write("consumer/SYNC_FACTS.md", b"# changed quietly\n")
        product.std.write_manifest()
        product.std.commit("a kit change with no version")
        code, out, _ = product.run("status")
        self.assertEqual(code, 1, out)
        self.assertIn("the standard changed kit files between the pin and main without changing VERSION", out)
        self.assertIn("  changed  SYNC_FACTS.md", out)

    def test_pin_newer_than_the_standard(self) -> None:
        product = self.world()
        product.std.write("VERSION", b"1.9.0\n")
        product.std.commit("the version went backwards")
        code, out, _ = product.run("status")
        self.assertEqual(code, 1, out)
        self.assertIn("pin names version 2.0.0, newer than 1.9.0 at main", out)

    def test_versions_compare_as_numbers_in_status_and_install(self) -> None:
        # As text "2.10.0" sorts before "2.9.0": the pin would look newer than the standard.
        product = self.world()
        product.std.release("2.9.0", {"SYNC_FACTS.md": b"# 2.9.0\n"})
        self.assertEqual(product.run("install")[0], 0)
        new = product.std.release("2.10.0", {"SYNC_FACTS.md": b"# 2.10.0\n"})
        code, out, _ = product.run("status")
        self.assertEqual((code, out.splitlines()[0]), (cc.EXIT_BEHIND, "MENQ STANDARD STATUS: BEHIND"), out)
        code, out, err = product.run("install")
        self.assertEqual(code, 0, out + err)
        self.assertIn(f"INSTALLED: MenQ Standard 2.9.0 -> 2.10.0 @ {new}", out)

    def test_status_refuses_a_pin_that_is_not_true(self) -> None:
        product = self.world()
        product.change_pin(lambda p: p["standard"].update(commit="3" * 40))
        code, out, _ = product.run("status")
        self.assertEqual((code, out.splitlines()[0]), (1, "MENQ STANDARD STATUS: RED"), out)
        self.assertIn("does not exist in the standard", out)
        (product.root / PIN).unlink()
        code, out, _ = product.run("status")
        self.assertEqual(code, 1, out)
        self.assertIn("pin is missing", out)


class Install(Case):
    def fresh(self) -> Product:
        product = self.world()
        root = product.root.parent / "fresh"
        init(root)
        fresh = Product(root, product.std)
        fresh.write("README.md", b"# Fresh\n")
        fresh.write("docs/GUIDE.md", b"# Guide\n")
        return fresh

    def test_adoption_writes_the_kit_the_pin_and_only_the_conformance_workflow(self) -> None:
        fresh = self.fresh()
        code, out, err = fresh.run("install")
        self.assertEqual(code, 0, out + err)
        self.assertIn(f"INSTALLED: MenQ Standard 2.0.0 @ {fresh.std.head}", out)
        self.assertIn("NOT DONE: SESSION_READ_MANIFEST.json does not exist", out)
        self.assertEqual(sorted(fresh.pin()["workflows"]), [CONFORMANCE])
        self.assertFalse((fresh.root / UPDATE).exists())
        for rel in gkm.KIT_FILES:
            self.assertEqual(fresh.read(f"{KIT}/{rel}"), (KIT_SRC / rel).read_bytes(), rel)
        self.assert_red(fresh, "session-read manifest is missing")
        fresh.write_session_manifest(session_manifest())
        self.assert_green(fresh)

    def test_adoption_into_a_named_directory_and_manifest_path(self) -> None:
        fresh = self.fresh()
        code, out, err = fresh.run("install", "--kit-dir", "standard-kit", "--manifest", "config/read.json", "--with-update-workflow")
        self.assertEqual(code, 0, out + err)
        self.assertIn(b'checker="standard-kit/check_conformance.py"', fresh.read(UPDATE))
        document = session_manifest()
        document["areas"]["standard-kit"] = [name.replace(KIT, "standard-kit") for name in document["areas"].pop(KIT)]
        fresh.write_session_manifest(document, "config/read.json")
        self.assertIn("kit: 9 files in standard-kit/ match the pin", self.assert_green(fresh))

    def test_update_moves_the_kit_and_the_pin_and_leaves_the_workflows(self) -> None:
        product = self.world()
        old = product.std.head
        workflows = (product.read(CONFORMANCE), product.read(UPDATE))
        new = product.std.release("2.1.0", {"check_session_read_budget.py": product.std.read("consumer/check_session_read_budget.py") + b"# 2.1.0\n", "test_sync_facts.py": None})
        code, out, err = product.run("install")
        self.assertEqual(code, 0, out + err)
        self.assertIn(f"INSTALLED: MenQ Standard 2.0.0 -> 2.1.0 @ {new}", out)
        self.assertIn("1 removed (test_sync_facts.py)", out)
        self.assertIn(f"workflows left as they were: {CONFORMANCE}, {UPDATE}", out)
        pin = product.pin()
        self.assertEqual((pin["standard"]["version"], pin["standard"]["commit"]), ("2.1.0", new))
        self.assertEqual({record["commit"] for record in pin["workflows"].values()}, {old})
        self.assertEqual((product.read(CONFORMANCE), product.read(UPDATE)), workflows)
        self.assertFalse((product.root / KIT / "test_sync_facts.py").exists())
        self.assertTrue(product.read(f"{KIT}/check_session_read_budget.py").endswith(b"# 2.1.0\n"))
        product.add()
        self.assert_green(product)
        code, out, _ = product.run("status")
        self.assertEqual((code, out.splitlines()[0]), (0, "MENQ STANDARD STATUS: CURRENT"), out)

    def test_render_workflows_moves_them_to_the_new_commit(self) -> None:
        product = self.world()
        new = product.std.release("2.1.0", {"SYNC_FACTS.md": b"# changed\n"})
        code, out, err = product.run("install", "--render-workflows")
        self.assertEqual(code, 0, out + err)
        self.assertEqual({record["commit"] for record in product.pin()["workflows"].values()}, {new})
        self.assertIn(f"consumer-conformance.yml@{new}".encode(), product.read(CONFORMANCE))
        product.add()
        self.assert_green(product)

    def test_install_overwrites_a_locally_edited_kit_file(self) -> None:
        product = self.world()
        product.write(f"{KIT}/sync_facts.py", b"# edited\n")
        self.assert_red(product, "kit file does not match its pin")
        self.assertEqual(product.run("install")[0], 0)
        self.assert_green(product)

    def refused(self, product: Product, fragment: str, *args: str, standard: bool | str = True) -> None:
        before = product.snapshot()
        code, out, err = product.run("install", *args, standard=standard)
        self.assertNotIn("Traceback", out + err)
        self.assertEqual(code, 1, out + err)
        self.assertEqual(out.splitlines()[0], "MENQ STANDARD INSTALL: RED", out)
        self.assertIn(fragment, out)
        self.assertEqual(product.snapshot(), before, "a refused install must write nothing")

    def test_refuses_to_install_backwards(self) -> None:
        product = self.world()
        old = product.std.head
        product.std.release("2.1.0", {"SYNC_FACTS.md": b"# changed\n"})
        self.assertEqual(product.run("install")[0], 0)
        self.refused(product, "is version 2.0.0, older than the pinned 2.1.0", standard=old)

    def test_refuses_to_move_the_kit(self) -> None:
        self.refused(self.world(), "the kit lives in menq-standard/; moving it to elsewhere/", "--kit-dir", "elsewhere")

    def test_refuses_over_a_pin_it_cannot_read(self) -> None:
        product = self.world()
        product.write(PIN, b"{")
        self.refused(product, "the existing pin cannot be read, so nothing was written: pin is malformed")

    def test_refuses_a_kit_directory_that_is_not_one_name(self) -> None:
        fresh = self.fresh()
        self.refused(fresh, "kit directory 'a/b' must be one directory name", "--kit-dir", "a/b")
        self.refused(fresh, "session-read manifest path '../m.json' is not normalised", "--manifest", "../m.json")

    def test_refuses_a_standard_whose_kit_does_not_match_its_manifest(self) -> None:
        product = self.world()
        product.std.write("consumer/SYNC_FACTS.md", b"# the manifest was not regenerated\n")
        product.std.write("VERSION", b"2.1.0\n")
        product.std.commit("a broken release")
        self.refused(product, "is inconsistent: consumer/SYNC_FACTS.md does not match consumer/KIT_MANIFEST.json; nothing was written")

    def test_refuses_a_standard_whose_kit_lacks_a_file_the_checker_needs(self) -> None:
        product = self.world()
        product.std.release("3.0.0", {"sync_facts.py": None})
        self.refused(product, "has no kit file sync_facts.py; nothing was written")

    def test_refuses_a_consumer_that_is_not_a_directory(self) -> None:
        product = self.world()
        out_buffer = io.StringIO()
        with contextlib.redirect_stdout(out_buffer):
            code = cc.main(["install", "--consumer", str(product.root / "README.md"), "--standard", str(product.std.root), "--standard-ref", "main"])
        self.assertEqual(code, 1)
        self.assertIn("MENQ STANDARD INSTALL: RED", out_buffer.getvalue())
        self.assertIn("--consumer is not a directory", out_buffer.getvalue())

    def test_refuses_a_standard_without_a_kit(self) -> None:
        fresh = self.fresh()
        first = git(fresh.std.root, "rev-list", "--max-parents=0", "HEAD")
        self.refused(fresh, "has no VERSION file: it predates the consumer kit", standard=first)


class Changelog(Case):
    TEXT = (
        "# Changelog\n\n"
        "## 2026-12-01 - newest (MenQ Standard v2.2.0)\n\n- C.\n\n"
        "## 2026-11-15 - an entry with no version\n\n- B2.\n\n"
        "## 2026-11-01 - middle (MenQ Standard v2.1.0)\n\n- B.\n\n"
        "## 2026-10-09 - first (MenQ Standard v2.0.0)\n\n- A.\n"
    )

    def test_entries_newer_than_a_version(self) -> None:
        cut = cc.changelog_since(self.TEXT, "2.0.0")
        self.assertTrue(cut.startswith("## 2026-12-01 - newest (MenQ Standard v2.2.0)"))
        self.assertIn("- B2.", cut)
        self.assertTrue(cut.endswith("- B.\n"))
        self.assertNotIn("- A.", cut)
        self.assertEqual(cc.changelog_since(self.TEXT, "2.1.0"), "## 2026-12-01 - newest (MenQ Standard v2.2.0)\n\n- C.\n\n## 2026-11-15 - an entry with no version\n\n- B2.\n")

    def test_nothing_newer_is_empty_and_a_skipped_version_stops_at_the_next_older(self) -> None:
        self.assertEqual(cc.changelog_since(self.TEXT, "2.2.0"), "")
        self.assertEqual(cc.changelog_since(self.TEXT, "9.0.0"), "")
        self.assertEqual(cc.changelog_since(self.TEXT, "2.1.5"), cc.changelog_since(self.TEXT, "2.1.0"))

    def test_crlf_changelog_gives_the_same_cut(self) -> None:
        self.assertEqual(cc.changelog_since(self.TEXT.replace("\n", "\r\n"), "2.0.0"), cc.changelog_since(self.TEXT, "2.0.0"))

    def test_version_compared_as_numbers_and_matched_whole(self) -> None:
        text = "## a (MenQ Standard v2.10.0)\n\n- ten.\n\n## b (MenQ Standard v2.9.0)\n\n- nine.\n"
        self.assertEqual(cc.changelog_since(text, "2.9.0"), "## a (MenQ Standard v2.10.0)\n\n- ten.\n")
        self.assertIsNone(cc.VERSION_HEADING.match("## x (MenQ Standard v2.1.0.5)"))
        self.assertIsNone(cc.VERSION_HEADING.match("### x (MenQ Standard v2.1.0)"))

    def test_refusals(self) -> None:
        for text, since, message in (
            (self.TEXT, "2.0", "--since '2.0' is not MAJOR.MINOR.PATCH"),
            (self.TEXT, "1.0.0", "has no heading naming MenQ Standard v1.0.0 or older"),
            ("# Changelog\n\nno entries\n", "2.0.0", "has no '## ' entry"),
        ):
            with self.subTest(since=since):
                with self.assertRaises(cc.Refusal) as raised:
                    cc.changelog_since(text, since)
                self.assertIn(message, str(raised.exception))

    def test_command_reads_the_changelog_of_the_ref(self) -> None:
        product = self.world()
        product.std.release("2.1.0", {"SYNC_FACTS.md": b"# changed\n"}, "the facts manual was rewritten")
        code, out, err = product.run("changelog", "--since", "2.0.0", consumer=False)
        self.assertEqual((code, err), (0, ""), out)
        self.assertEqual(out, "## 2026-11-01 - the facts manual was rewritten (MenQ Standard v2.1.0)\n\n- the facts manual was rewritten.\n")
        code, out, err = product.run("changelog", "--since", "1.0.0", consumer=False)
        self.assertEqual((code, out), (1, ""))
        self.assertIn("MENQ STANDARD CHANGELOG: RED", err)


    def test_standard_without_a_changelog(self) -> None:
        product = self.world()
        (product.std.root / "CHANGELOG.md").unlink()
        product.std.commit("the changelog was deleted")
        code, out, err = product.run("changelog", "--since", "2.0.0", consumer=False)
        self.assertEqual((code, out), (1, ""))
        self.assertIn("the standard at main has no CHANGELOG.md", err)


class PinCommit(Case):
    def test_prints_the_commit_and_nothing_else(self) -> None:
        product = self.world()
        code, out, err = product.run("pin-commit")
        self.assertEqual((code, out, err), (0, product.std.head + "\n", ""))

    def test_refusals_go_to_stderr_and_stdout_stays_empty(self) -> None:
        product = self.world()
        git(product.std.root, "checkout", "--quiet", "-b", "side")
        side = product.std.release("2.1.0", {"SYNC_FACTS.md": b"# side\n"})
        git(product.std.root, "checkout", "--quiet", "main")
        for commit, message in ((side, "is not on the standard's main"), ("4" * 40, "does not exist in the standard")):
            with self.subTest(message=message):
                product.change_pin(lambda p, commit=commit: p["standard"].update(commit=commit))
                code, out, err = product.run("pin-commit")
                self.assertEqual((code, out), (1, ""))
                self.assertIn("MENQ STANDARD CONFORMANCE: RED", err)
                self.assertIn(message, err)
        product.write(PIN, b"[]")
        code, out, err = product.run("pin-commit")
        self.assertEqual((code, out), (1, ""))
        self.assertIn("pin is malformed: top level must be an object", err)


@unittest.skipUnless(shutil.which("bash"), "the update template is a bash script")
class UpdateTemplateAsShell(Case):
    """The steps of the rendered update workflow, run as shell.  GitHub is replaced by two stand-ins:
    the clone of the standard is made from the local fixture, and ``gh`` is a script that records
    its arguments.  What GitHub itself would do is NOT tested here."""

    def prepare(self) -> tuple[Product, Path, dict[str, str], str]:
        product = self.world()
        root = product.root.parent
        git(root, "init", "--quiet", "--bare", "origin.git")
        git(product.root, "remote", "add", "origin", str(root / "origin.git"))
        product.add()
        git(product.root, "commit", "--quiet", "--message", "Adopt MenQ Standard")
        git(product.root, "push", "--quiet", "origin", "main")
        tools = root / "tools"
        tools.mkdir()
        (tools / "gh").write_bytes(b'#!/bin/sh\nprintf "%s\\n" "$@" >> "$GH_LOG"\n')
        (tools / "gh").chmod(0o755)
        (tools / "python").write_bytes(f'#!/bin/sh\nexec "{sys.executable}" "$@"\n'.encode())
        (tools / "python").chmod(0o755)
        runner = root / "runner-temp"
        runner.mkdir()
        tree = vf.parse_workflow_yaml(product.read(UPDATE).decode("utf-8"))
        steps = tree["jobs"]["update"]["steps"]
        self.assertEqual(steps[2]["run"], 'git clone --quiet https://github.com/menqstudio/MenQ-Standard.git "$RUNNER_TEMP/menq-standard"')
        environment = dict(os.environ, PATH=f"{tools}{os.pathsep}{os.environ['PATH']}", RUNNER_TEMP=str(runner), GH_LOG=str(root / "gh.log"))
        return product, root, environment, steps[3]["run"]

    def clone_standard(self, product: Product, runner: Path) -> None:
        shutil.rmtree(runner / "menq-standard", ignore_errors=True)
        git(runner, "clone", "--quiet", str(product.std.root), "menq-standard")

    def run_step(self, product: Product, environment: dict[str, str], script: str) -> subprocess.CompletedProcess:
        return subprocess.run(["bash", "-e", "-c", script], cwd=product.root, env=environment, capture_output=True, text=True, encoding="utf-8")

    def test_current_pin_pushes_nothing(self) -> None:
        product, root, environment, script = self.prepare()
        self.clone_standard(product, root / "runner-temp")
        result = self.run_step(product, environment, script)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("The pin is current. Nothing to do.", result.stdout)
        self.assertFalse((root / "gh.log").exists())
        self.assertEqual(git(root / "origin.git", "for-each-ref", "--format=%(refname:short)", "refs/heads"), "main")

    def test_behind_pin_opens_one_pull_request_and_never_merges(self) -> None:
        product, root, environment, script = self.prepare()
        main_before = git(root / "origin.git", "rev-parse", "main")
        product.std.release("2.1.0", {"SYNC_FACTS.md": product.std.read("consumer/SYNC_FACTS.md") + b"\nA new paragraph.\n"}, "the facts manual gained a paragraph")
        self.clone_standard(product, root / "runner-temp")
        result = self.run_step(product, environment, script)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        branch = "menq-standard/update-2.1.0"
        self.assertEqual(git(root / "origin.git", "rev-parse", "main"), main_before, "main must not move")
        changed = git(root / "origin.git", "diff", "--name-only", "main", branch).splitlines()
        self.assertEqual(changed, [PIN, f"{KIT}/SYNC_FACTS.md"])
        arguments = (root / "gh.log").read_text(encoding="utf-8").splitlines()
        body = root / "runner-temp/menq-standard-update/body.md"
        self.assertEqual(
            arguments,
            ["pr", "create", "--base", "main", "--head", branch, "--title", "MenQ Standard 2.0.0 -> 2.1.0", "--body-file", str(body)],
        )
        text = body.read_text(encoding="utf-8")
        for fragment in (
            "MenQ Standard moved from 2.0.0 to 2.1.0.",
            "Nothing merges it: a person reviews and merges.",
            "MENQ STANDARD STATUS: BEHIND",
            "  changed  SYNC_FACTS.md",
            "as run by the update job (exit 0)",
            "MENQ STANDARD CONFORMANCE: GREEN",
            "## 2026-11-01 - the facts manual gained a paragraph (MenQ Standard v2.1.0)",
        ):
            self.assertIn(fragment, text)

        # The same schedule fires again before anybody merged: nothing new is pushed or opened.
        git(product.root, "checkout", "--quiet", "main")
        tip = git(root / "origin.git", "rev-parse", branch)
        again = self.run_step(product, environment, script)
        self.assertEqual(again.returncode, 0, again.stdout + again.stderr)
        self.assertIn(f"Branch {branch} already exists", again.stdout)
        self.assertEqual(git(root / "origin.git", "rev-parse", branch), tip)
        self.assertEqual(len((root / "gh.log").read_text(encoding="utf-8").splitlines()), len(arguments))

    def test_untrue_pin_stops_the_job_red_and_pushes_nothing(self) -> None:
        product, root, environment, script = self.prepare()
        product.change_pin(lambda p: p["standard"].update(commit="5" * 40))
        self.clone_standard(product, root / "runner-temp")
        result = self.run_step(product, environment, script)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("status is RED (exit 1). No update is attempted.", result.stdout)
        self.assertFalse((root / "gh.log").exists())
        self.assertEqual(git(root / "origin.git", "for-each-ref", "--format=%(refname:short)", "refs/heads"), "main")


if __name__ == "__main__":
    unittest.main()
