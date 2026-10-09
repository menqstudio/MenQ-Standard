#!/usr/bin/env python3
"""Generate or verify consumer/KIT_MANIFEST.json, the list of consumer-kit files and their hashes.

A repository that follows MenQ Standard copies the kit unchanged and pins the hash of every file
(decision D-029).  The manifest is what its pin is compared against, so it may not drift from the
files: ``--check`` is RED when it does, and never answers with a traceback.

    python scripts/generate_kit_manifest.py --write
    python scripts/generate_kit_manifest.py --check

The hash of a kit file is the sha256 of its bytes after CRLF is folded to LF: the same rule
consumer/check_conformance.py applies in a product repository, read from that file, not restated.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KIT_DIR = "consumer"
MANIFEST_NAME = "KIT_MANIFEST.json"
# The kit, declared by name.  A file that appears under consumer/ without being listed here is
# RED: nothing reaches a product repository by being dropped into a directory.
KIT_FILES = (
    "ADOPTION.md",
    "CONSUMER_CONTRACT.md",
    "SYNC_FACTS.md",
    "check_conformance.py",
    "check_session_read_budget.py",
    "sync_facts.py",
    "templates/menq-standard-conformance.yml",
    "templates/menq-standard-update.yml",
    "test_sync_facts.py",
)


class Refusal(Exception):
    """A condition the manifest cannot be built or verified under; printed as a RED line."""


def load_checker(root: Path):
    """The kit's own checker, for the constants this script must not restate."""
    path = root / KIT_DIR / "check_conformance.py"
    try:
        spec = importlib.util.spec_from_file_location("menq_kit_check_conformance", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as exc:  # whatever a broken kit file raises is a RED line, never a traceback
        raise Refusal(f"cannot load {KIT_DIR}/check_conformance.py: {type(exc).__name__}: {exc}") from exc
    return module


def tracked_under_kit(root: Path) -> list[str]:
    try:
        result = subprocess.run(["git", "ls-files", "-z", "--", KIT_DIR], cwd=root, check=True, capture_output=True)
        paths = [part for part in result.stdout.decode("utf-8").split("\0") if part]
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError) as exc:
        raise Refusal(f"cannot enumerate tracked files with git ls-files -z: {exc}") from exc
    return sorted(path[len(KIT_DIR) + 1:] for path in paths)


def build_manifest(root: Path) -> dict[str, object]:
    checker = load_checker(root)
    tracked = set(tracked_under_kit(root))
    problems: list[str] = []
    for rel in sorted(tracked - set(KIT_FILES) - {MANIFEST_NAME}):
        problems.append(f"file under {KIT_DIR}/ is neither a declared kit file nor the manifest: {KIT_DIR}/{rel}")
    for rel in KIT_FILES:
        if rel not in tracked:
            problems.append(f"declared kit file is not tracked by git: {KIT_DIR}/{rel}")
        elif not (root / KIT_DIR / rel).is_file():
            problems.append(f"declared kit file is missing from the checkout: {KIT_DIR}/{rel}")
    for rel in checker.REQUIRED_KIT_FILES:
        if rel not in KIT_FILES:
            problems.append(f"the checker needs {rel}, which is not a declared kit file")
    if len(set(KIT_FILES)) != len(KIT_FILES):
        problems.append("a kit file is declared twice")
    if problems:
        raise Refusal("; ".join(problems))
    files: dict[str, str] = {}
    for rel in sorted(KIT_FILES):
        try:
            files[rel] = checker.kit_hash((root / KIT_DIR / rel).read_bytes())
        except OSError as exc:
            raise Refusal(f"cannot read kit file {KIT_DIR}/{rel}: {exc.strerror or exc}") from exc
    return {
        "schema_version": checker.KIT_MANIFEST_SCHEMA_VERSION,
        "repository": checker.STANDARD_REPOSITORY,
        "kit_dir": KIT_DIR,
        "hash": checker.HASH_RULE,
        "files": files,
    }


def manifest_bytes(manifest: dict[str, object]) -> bytes:
    return (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def check(root: Path) -> list[str]:
    """RED lines; an empty list means the manifest equals what the files produce."""
    try:
        expected = build_manifest(root)
    except Refusal as refusal:
        return [str(refusal)]
    path = root / KIT_DIR / MANIFEST_NAME
    if not path.is_file():
        return [f"kit manifest is missing: {KIT_DIR}/{MANIFEST_NAME}"]
    if MANIFEST_NAME not in tracked_under_kit(root):
        return [f"kit manifest is not tracked by git: {KIT_DIR}/{MANIFEST_NAME}"]
    try:
        actual = json.loads(path.read_bytes().decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return [f"kit manifest is malformed: {KIT_DIR}/{MANIFEST_NAME}: {exc}"]
    if not isinstance(actual, dict):
        return [f"kit manifest is malformed: {KIT_DIR}/{MANIFEST_NAME}: top level must be an object"]
    errors: list[str] = []
    for key in sorted(set(expected) | set(actual)):
        if key == "files":
            continue
        if expected.get(key) != actual.get(key):
            errors.append(f"kit manifest field {key!r} is {actual.get(key)!r}, expected {expected.get(key)!r}")
    recorded = actual.get("files")
    if not isinstance(recorded, dict):
        return errors + ["kit manifest 'files' must be an object mapping a kit file to its sha256"]
    wanted = expected["files"]
    for rel in sorted(set(wanted) | set(recorded)):
        if rel not in recorded:
            errors.append(f"kit manifest does not list kit file: {rel}")
        elif rel not in wanted:
            errors.append(f"kit manifest lists a file that is not in the kit: {rel}")
        elif recorded[rel] != wanted[rel]:
            errors.append(f"kit manifest hash drift for {rel}: recorded {recorded[rel]}, the file is {wanted[rel]}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="write the manifest from the kit files")
    mode.add_argument("--check", action="store_true", help="exit 1 unless the manifest equals what the files produce")
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (default: this checkout)")
    args = parser.parse_args(argv)
    root = args.root.resolve()

    if args.write:
        try:
            manifest = build_manifest(root)
            (root / KIT_DIR / MANIFEST_NAME).write_bytes(manifest_bytes(manifest))
        except (Refusal, OSError) as refusal:
            print("KIT MANIFEST: RED")
            print(f"- {refusal}")
            return 1
        print(f"KIT MANIFEST: WRITTEN ({len(manifest['files'])} kit files)")
        return 0

    errors = check(root)
    if errors:
        print("KIT MANIFEST: RED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"KIT MANIFEST: GREEN ({len(KIT_FILES)} kit files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
