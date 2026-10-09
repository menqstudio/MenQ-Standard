#!/usr/bin/env python3
"""Generate or verify the tracked Markdown inventory for MenQ Standard.

``--check`` never answers with a traceback: a missing, malformed or surprising input is a RED line
that names the reason.  ``scripts/test_generate_markdown_inventory.py`` breaks each subject once.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "foundation/ai-collaboration/MARKDOWN_INVENTORY.json"
SCHEMA_VERSION = 1
# One rule, shared with scripts/validate_foundation.py: a tracked path whose name ends in ".md" in
# any letter case.  The two scripts disagreed about "NOTE.MD" until 2026-10-09, and no inventory
# could satisfy both.
SOURCE = "git ls-files -z (paths ending in .md, any letter case)"
HEADER_KEYS = ("schema_version", "repository", "source", "file_count")


class Refusal(Exception):
    """A condition the inventory cannot be built or verified under; printed as a RED line."""


def tracked_markdown() -> list[str]:
    """Tracked Markdown paths from ``git ls-files -z``, so a space or a non-ASCII name is one path."""
    try:
        result = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True)
        paths = [part for part in result.stdout.decode("utf-8").split("\0") if part]
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError) as exc:
        raise Refusal(f"cannot enumerate tracked files with git ls-files -z: {exc}") from exc
    return sorted({path for path in paths if path.lower().endswith(".md")})


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest() -> dict[str, object]:
    files: list[dict[str, object]] = []
    for rel in tracked_markdown():
        path = ROOT / rel
        if not path.is_file():
            raise Refusal(f"tracked Markdown file is missing from the checkout: {rel}")
        try:
            files.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha256(path)})
        except OSError as exc:
            raise Refusal(f"cannot read tracked Markdown file {rel}: {exc.strerror or exc}") from exc
    return {
        "schema_version": SCHEMA_VERSION,
        "repository": "menqstudio/MenQ-Standard",
        "source": SOURCE,
        "file_count": len(files),
        "files": files,
    }


def serialized(data: dict[str, object]) -> str:
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"), sort_keys=False)


def check(expected_data: dict[str, object]) -> list[str]:
    """Compare the committed manifest with the tree.  Returns RED lines; empty means GREEN."""
    if not MANIFEST.is_file():
        return [f"missing {MANIFEST.relative_to(ROOT).as_posix()}"]
    try:
        actual_text = MANIFEST.read_bytes().decode("utf-8")
        actual = json.loads(actual_text)
    except (OSError, ValueError) as exc:
        return [f"manifest is not valid UTF-8 JSON: {exc}"]
    if not isinstance(actual, dict) or not isinstance(actual.get("files"), list):
        return ["manifest must be a JSON object with a 'files' list"]

    problems: list[str] = []
    entries = actual["files"]
    listed = [entry.get("path") for entry in entries if isinstance(entry, dict) and isinstance(entry.get("path"), str)]
    if len(listed) != len(entries):
        problems.append("manifest contains entries without a path")
    expected_files = {entry["path"]: entry for entry in expected_data["files"]}
    tracked = list(expected_files)
    if listed != tracked:
        problems.append("path list does not match tracked Markdown files")
        for path in sorted(set(tracked) - set(listed)):
            problems.append(f"  not in the manifest: {path}")
        for path in sorted(set(listed) - set(tracked)):
            problems.append(f"  not a tracked Markdown file: {path}")
        if set(listed) == set(tracked):
            problems.append("  same paths, different order or a duplicate")
    for entry in entries:
        if isinstance(entry, dict) and entry.get("path") in expected_files and entry != expected_files[entry["path"]]:
            problems.append(f"stale entry for {entry['path']}: manifest={entry} tree={expected_files[entry['path']]}")
    for key in HEADER_KEYS:
        if actual.get(key) != expected_data[key]:
            problems.append(f"{key}: manifest={actual.get(key)!r} expected={expected_data[key]!r}")
    if not problems and actual_text != serialized(expected_data):
        problems.append("manifest is not in the generator's canonical serialisation; run --write")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write the canonical manifest")
    parser.add_argument("--check", action="store_true", help="verify the canonical manifest")
    args = parser.parse_args()
    if args.write == args.check:
        parser.error("choose exactly one of --write or --check")

    try:
        expected_data = build_manifest()
        if args.write:
            MANIFEST.parent.mkdir(parents=True, exist_ok=True)
            MANIFEST.write_bytes(serialized(expected_data).encode("utf-8"))
            print(f"MARKDOWN INVENTORY: WRITTEN ({expected_data['file_count']} files)")
            return 0
        problems = check(expected_data)
    except Refusal as exc:
        print(f"MARKDOWN INVENTORY: RED - {exc}")
        return 1
    except Exception as exc:  # the gate answers RED, never with a traceback
        print(f"MARKDOWN INVENTORY: RED - internal error: {type(exc).__name__}: {exc}")
        return 1

    if problems:
        print(f"MARKDOWN INVENTORY: RED - {problems[0]}")
        for problem in problems[1:]:
            print(f"- {problem.strip()}")
        return 1
    print(f"MARKDOWN INVENTORY: GREEN ({expected_data['file_count']} files)")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    sys.exit(main())
