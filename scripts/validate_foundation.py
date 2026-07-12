#!/usr/bin/env python3
"""Validate MenQ Foundation documentation structure and integrity markers."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

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
}


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


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
        for decision_id in ("D-022", "D-023"):
            if decision_id not in text:
                errors.append(f"decision index missing {decision_id}")

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

    if errors:
        print("FOUNDATION VALIDATION: RED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("FOUNDATION VALIDATION: GREEN")
    print(f"Validated {len(CHAPTERS)} Foundation chapters and root controls.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
