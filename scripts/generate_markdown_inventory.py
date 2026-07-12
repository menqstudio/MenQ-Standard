#!/usr/bin/env python3
"""Generate or verify the tracked Markdown inventory for MenQ Standard."""

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


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def tracked_markdown() -> list[str]:
    output = git("ls-files", "--", "*.md", "*.MD")
    return sorted({line.strip() for line in output.splitlines() if line.strip()})


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest() -> dict[str, object]:
    paths = tracked_markdown()
    files: list[dict[str, object]] = []
    for rel in paths:
        path = ROOT / rel
        if not path.is_file():
            raise RuntimeError(f"tracked Markdown file missing from checkout: {rel}")
        files.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha256(path)})
    return {
        "schema_version": SCHEMA_VERSION,
        "repository": "menqstudio/MenQ-Standard",
        "source": "git ls-files -- *.md *.MD",
        "file_count": len(files),
        "files": files,
    }


def serialized(data: dict[str, object]) -> str:
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"), sort_keys=False)


def report_drift(actual_text: str, expected_data: dict[str, object]) -> None:
    try:
        actual_data = json.loads(actual_text)
    except json.JSONDecodeError as exc:
        print(f"- manifest JSON is invalid: {exc}")
        return
    actual_files = {entry.get("path"): entry for entry in actual_data.get("files", [])}
    expected_files = {entry.get("path"): entry for entry in expected_data.get("files", [])}
    for path in sorted(set(actual_files) | set(expected_files)):
        actual_entry = actual_files.get(path)
        expected_entry = expected_files.get(path)
        if actual_entry != expected_entry:
            print(f"- {path}: actual={actual_entry} expected={expected_entry}")
    for key in ("schema_version", "repository", "source", "file_count"):
        if actual_data.get(key) != expected_data.get(key):
            print(f"- {key}: actual={actual_data.get(key)!r} expected={expected_data.get(key)!r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write the canonical manifest")
    parser.add_argument("--check", action="store_true", help="verify the canonical manifest")
    args = parser.parse_args()
    if args.write == args.check:
        parser.error("choose exactly one of --write or --check")

    expected_data = build_manifest()
    expected = serialized(expected_data)
    if args.write:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(expected, encoding="utf-8")
        print(f"MARKDOWN INVENTORY: WRITTEN ({expected_data['file_count']} files)")
        return 0

    if not MANIFEST.is_file():
        print(f"MARKDOWN INVENTORY: RED - missing {MANIFEST.relative_to(ROOT)}")
        return 1
    actual = MANIFEST.read_text(encoding="utf-8")
    if actual != expected:
        print("MARKDOWN INVENTORY: RED - manifest is stale or inconsistent")
        report_drift(actual, expected_data)
        return 1

    manifest = json.loads(actual)
    listed = [entry["path"] for entry in manifest.get("files", [])]
    if listed != tracked_markdown():
        print("MARKDOWN INVENTORY: RED - path list does not match tracked Markdown files")
        return 1
    print(f"MARKDOWN INVENTORY: GREEN ({manifest['file_count']} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
