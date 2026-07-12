#!/usr/bin/env python3
from pathlib import Path

path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
heading = "# MenQ Standard — Changelog\n\n"
marker = "## 2026-07-12 — Design Platform Part 14 governance architecture"

if marker not in text:
    if not text.startswith(heading):
        raise SystemExit("Unexpected CHANGELOG.md heading")
    section = """## 2026-07-12 — Design Platform Part 14 governance architecture

### Հայերեն

- Ավելացվել է governance, contribution, ownership և change-request lifecycle architecture v1-ը։
- Սահմանվել են authority model-ը, ownership registry-ն, contribution classes-ը, approval matrix-ը և lifecycle-ը։
- Unowned canonical asset-ը սահմանվել է որպես RED governance defect։
- High-risk կամ breaking change-ի self-approval-ը արգելվել է։
- Merge-ը սահմանվել է որպես առանձին authority action, ոչ GREEN CI-ի ավտոմատ հետևանք։
- Continuation point-ը տեղափոխվել է Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan։
- D-025-ը մնում է `Approved — Implementing`, Draft PR #3-ը մնում է open, Draft և unmerged։

### English

- Added Governance, Contribution, Ownership, and Change-Request Lifecycle Architecture v1.
- Defined the authority model, ownership registry, contribution classes, approval matrix, and lifecycle.
- Defined an unowned canonical asset as a RED governance defect.
- Prohibited self-approval for high-risk or breaking changes.
- Defined merge as a separate authority action, not an automatic consequence of green CI.
- Advanced the continuation point to Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.
- D-025 remains `Approved — Implementing`; Draft PR #3 remains open, Draft, and unmerged.

"""
    path.write_text(heading + section + text[len(heading):], encoding="utf-8")
