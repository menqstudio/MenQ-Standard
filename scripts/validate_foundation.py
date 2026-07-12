#!/usr/bin/env python3
"""Validate MenQ Foundation documentation and D-026 session-read integrity."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY_REL = "foundation/ai-collaboration/MARKDOWN_INVENTORY.json"
INVENTORY = ROOT / INVENTORY_REL

CHAPTERS = (
    "philosophy",
    "principles",
    "terminology",
    "governance",
    "decision-system",
    "documentation",
    "ai-collaboration",
)

REQUIRED_ROOT = (
    "README.md",
    "PROJECT_CONTEXT.md",
    "AI_WORKING_CONTEXT.md",
    "DECISIONS.md",
    "DECISION_INDEX.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "COLLABORATION_STYLE.md",
)

REQUIRED_FOUNDATION = (
    "foundation/README.md",
    "foundation/PROJECT_CONTEXT.md",
    "foundation/FOUNDATION_NORMATIVE_METADATA_REGISTRY.md",
    "foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md",
    "foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md",
    "foundation/ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md",
    INVENTORY_REL,
)

EXPECTED_MARKERS = {
    "README.md": "<!-- END: MENQ_STANDARD_ROOT_README -->",
    "PROJECT_CONTEXT.md": "<!-- END: MENQ_STANDARD_PROJECT_CONTEXT -->",
    "DECISION_INDEX.md": "<!-- END: MENQ_DECISION_INDEX -->",
    "ROADMAP.md": "<!-- END: MENQ_STANDARD_ROADMAP -->",
    "COLLABORATION_STYLE.md": "<!-- END: MENQ_COLLABORATION_STYLE -->",
    "foundation/README.md": "<!-- END: FOUNDATION_README_V1 -->",
    "foundation/PROJECT_CONTEXT.md": "<!-- END: FOUNDATION_PROJECT_CONTEXT -->",
    "foundation/FOUNDATION_NORMATIVE_METADATA_REGISTRY.md": "<!-- END: FOUNDATION_NORMATIVE_METADATA_REGISTRY -->",
    "foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md": "<!-- END: CANONICAL_WRITE_INTEGRITY_LAW_V1 -->",
    "foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md": "<!-- END: CANONICAL_SESSION_READ_LAW_V1 -->",
    "foundation/ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md": "<!-- END: D-026-CANONICAL-SESSION-READ-LAW -->",
}

D026_REQUIRED_REFERENCES = {
    "README.md": (
        "CANONICAL_SESSION_READ_LAW.md",
        "D-026-CANONICAL-SESSION-READ-LAW.md",
    ),
    "PROJECT_CONTEXT.md": ("CANONICAL_SESSION_READ_LAW.md",),
    "AI_WORKING_CONTEXT.md": ("D-026",),
    "NEXT_CHAT_HANDOFF.md": (
        "CANONICAL_SESSION_READ_LAW.md",
        "D-026",
    ),
    "DECISION_INDEX.md": ("D-026",),
    "foundation/README.md": (
        "CANONICAL_SESSION_READ_LAW.md",
        "D-026-CANONICAL-SESSION-READ-LAW.md",
    ),
    "foundation/ai-collaboration/PROJECT_CONTEXT.md": ("D-026",),
}


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tracked_markdown_files(errors: list[str]) -> list[str]:
    try:
        result = subprocess.run(
            ["git", "ls-files", "*.md"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        errors.append(f"cannot enumerate tracked Markdown files: {exc}")
        return []

    paths = sorted(line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip())
    if not paths:
        errors.append("tracked Markdown inventory is empty")
    if len(paths) != len(set(paths)):
        errors.append("tracked Markdown inventory contains duplicate paths")
    return paths


def validate_inventory(errors: list[str]) -> int:
    if not INVENTORY.is_file():
        errors.append(f"missing canonical Markdown inventory: {INVENTORY_REL}")
        return 0

    try:
        data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid canonical Markdown inventory: {exc}")
        return 0

    entries = data.get("files")
    declared_count = data.get("file_count")
    if not isinstance(entries, list):
        errors.append("Markdown inventory 'files' must be a list")
        return 0
    if declared_count != len(entries):
        errors.append(
            f"Markdown inventory count mismatch: declared {declared_count}, actual {len(entries)}"
        )

    actual_paths = tracked_markdown_files(errors)
    manifest_paths = [entry.get("path") for entry in entries if isinstance(entry, dict)]

    if len(manifest_paths) != len(entries):
        errors.append("Markdown inventory contains non-object entries")
    if manifest_paths != sorted(manifest_paths):
        errors.append("Markdown inventory paths are not sorted")
    if len(manifest_paths) != len(set(manifest_paths)):
        errors.append("Markdown inventory contains duplicate paths")
    if manifest_paths != actual_paths:
        missing = sorted(set(actual_paths) - set(manifest_paths))
        stale = sorted(set(manifest_paths) - set(actual_paths))
        if missing:
            errors.append(f"Markdown inventory missing tracked files: {', '.join(missing)}")
        if stale:
            errors.append(f"Markdown inventory contains untracked files: {', '.join(stale)}")
        if not missing and not stale:
            errors.append("Markdown inventory path ordering differs from git ls-files")

    by_path = {
        entry.get("path"): entry
        for entry in entries
        if isinstance(entry, dict) and isinstance(entry.get("path"), str)
    }

    for rel in actual_paths:
        path = ROOT / rel
        entry = by_path.get(rel)
        if entry is None:
            continue
        if not path.is_file():
            errors.append(f"inventory path is not a file: {rel}")
            continue

        actual_size = path.stat().st_size
        actual_sha = sha256_file(path)
        if entry.get("bytes") != actual_size:
            errors.append(
                f"Markdown inventory size drift for {rel}: expected {entry.get('bytes')}, actual {actual_size}"
            )
        if entry.get("sha256") != actual_sha:
            errors.append(f"Markdown inventory SHA-256 drift for {rel}")

    return len(actual_paths)


def main() -> int:
    errors: list[str] = []

    for rel in (*REQUIRED_ROOT, *REQUIRED_FOUNDATION):
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"missing required file: {rel}")

    for chapter in CHAPTERS:
        for name in ("README.md", "PROJECT_CONTEXT.md"):
            rel = f"foundation/{chapter}/{name}"
            if not (ROOT / rel).is_file():
                errors.append(f"missing chapter file: {rel}")

    for rel, marker in EXPECTED_MARKERS.items():
        path = ROOT / rel
        if path.is_file() and marker not in read_text(rel):
            errors.append(f"missing ending marker in {rel}: {marker}")

    decision_index = ROOT / "DECISION_INDEX.md"
    if decision_index.is_file():
        text = read_text("DECISION_INDEX.md")
        for decision_id in ("D-022", "D-023", "D-026"):
            if decision_id not in text:
                errors.append(f"decision index missing {decision_id}")

    for rel, references in D026_REQUIRED_REFERENCES.items():
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"missing D-026 synchronization file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for reference in references:
            if reference not in text:
                errors.append(f"{rel} missing D-026 reference: {reference}")

    foundation_context = ROOT / "foundation/PROJECT_CONTEXT.md"
    if foundation_context.is_file():
        text = read_text("foundation/PROJECT_CONTEXT.md")
        if re.search(r"AI Collaboration.*Pending", text, flags=re.IGNORECASE):
            errors.append("foundation context still marks AI Collaboration Pending")

    for rel in (
        "foundation/documentation/BILINGUAL_PARITY_ADDENDUM.md",
        "foundation/ai-collaboration/BILINGUAL_PARITY_ADDENDUM.md",
    ):
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"missing bilingual parity control: {rel}")
        else:
            text = path.read_text(encoding="utf-8")
            if "## Հայերեն" not in text or "## English" not in text:
                errors.append(f"bilingual sections missing in {rel}")

    markdown_count = validate_inventory(errors)

    if errors:
        print("FOUNDATION VALIDATION: RED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("FOUNDATION VALIDATION: GREEN")
    print(
        f"Validated {len(CHAPTERS)} Foundation chapters, root controls, "
        f"D-026 synchronization, and {markdown_count} tracked Markdown files."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
