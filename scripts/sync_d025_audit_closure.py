#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_required(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise SystemExit(f"Missing expected block in {path}: {old[:120]!r}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


def prepend(path: str, heading: str, marker: str, section: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if marker in text:
        return
    if not text.startswith(heading):
        raise SystemExit(f"Unexpected heading in {path}")
    p.write_text(heading + section + text[len(heading):], encoding="utf-8")


replace_required(
    "platforms/design/ROADMAP.md",
    "- [x] Part 16 — Canonical Specification Index and Implementation Package Plan.\n\n## Current / Ընթացիկ\n\n1. D-025 completeness audit and architecture gap analysis.\n2. Design Platform validator and CI implementation.\n3. Draft PR #3 review and Owner review.",
    "- [x] Part 16 — Canonical Specification Index and Implementation Package Plan.\n- [x] D-025 completeness audit and architecture gap analysis.\n- [x] Design Platform D-025 conformance validator and CI coverage.\n- [x] Draft PR #3 architecture review record.\n\n## Current / Ընթացիկ\n\n1. Implementation Phase A — canonical specification registry, schemas, ownership, dependency graph, and package skeleton.\n2. Select two distinct real consumer candidates and define bounded pilot scopes.\n3. Preserve Architecture GREEN / Implementation YELLOW until real evidence exists.",
)

for path in ["platforms/design/PROJECT_CONTEXT.md", "PROJECT_CONTEXT.md", "AI_WORKING_CONTEXT.md", "NEXT_CHAT_HANDOFF.md", "platforms/design/NEXT_CHAT_HANDOFF.md"]:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    text = text.replace(
        "1. D-025 completeness audit and architecture gap analysis։\n2. Design Platform validator and CI implementation։\n3. Draft PR #3 review, canonical synchronization, GREEN evidence and Owner review։",
        "1. Implementation Phase A — canonical specification registry, schemas, ownership, dependency graph և package skeleton։\n2. Ընտրել երկու distinct real consumer candidates և սահմանել bounded pilot scopes։\n3. Պահպանել Architecture GREEN / Implementation YELLOW verdict-ը մինչև իրական evidence։",
    )
    text = text.replace(
        "1. D-025 completeness audit and architecture gap analysis.\n2. Design Platform validator and CI implementation.\n3. Draft PR #3 review, canonical synchronization, GREEN evidence, and Owner review.",
        "1. Implementation Phase A — canonical specification registry, schemas, ownership, dependency graph, and package skeleton.\n2. Select two distinct real consumer candidates and define bounded pilot scopes.\n3. Preserve Architecture GREEN / Implementation YELLOW until real evidence exists.",
    )
    text = text.replace(
        "D-025 completeness audit, architecture gap analysis, Design Platform validator/CI implementation, and Draft PR review",
        "Implementation Phase A — canonical specification registry, schemas, ownership, dependency graph, and package skeleton",
    )
    text = text.replace(
        "the D-025 completeness audit, architecture gap analysis, Design Platform validator/CI implementation, and Draft PR review",
        "Implementation Phase A — canonical specification registry, schemas, ownership, dependency graph, and package skeleton",
    )
    if "D-025 completeness audit-ը canonical է" not in text and "## Հայերեն" in text:
        anchor = "- Part 16 canonical specification index/implementation package plan-ը canonical է։\n"
        if anchor in text:
            text = text.replace(anchor, anchor + "- D-025 completeness audit-ը և Draft PR review record-ը canonical են։\n", 1)
    if "The D-025 completeness audit and Draft PR review record are canonical" not in text and "## English" in text:
        anchor = "- Part 16 canonical specification index and implementation package plan is canonical.\n"
        if anchor in text:
            text = text.replace(anchor, anchor + "- The D-025 completeness audit and Draft PR review record are canonical.\n", 1)
    p.write_text(text, encoding="utf-8")

replace_required(
    "ROADMAP.md",
    "1. D-025 completeness audit and architecture gap analysis.\n2. Design Platform validator and CI implementation.\n3. Draft PR #3 review, canonical synchronization, GREEN evidence, and Owner review.",
    "1. Implementation Phase A — canonical specification registry, schemas, ownership, dependency graph, and package skeleton.\n2. Select two distinct real consumer candidates and define bounded pilot scopes.\n3. Preserve Architecture GREEN / Implementation YELLOW until real evidence exists.",
)

section_design = """## 2026-07-12 — D-025 completeness audit, validator, and Draft PR review

### Հայերեն

- Architecture completeness-ը գնահատվել է GREEN, implementation/lock readiness-ը՝ YELLOW։
- Ավելացվել են `D-025_COMPLETENESS_AUDIT.md` և `D-025_DRAFT_PR_REVIEW_RECORD.md`։
- `validate_platforms.py`-ը բարձրացվել է D-025 conformance validator-ի մակարդակի։
- PR #3-ը ճիշտ է պահվում open, Draft և unmerged։
- Հաջորդ աշխատանքը Implementation Phase A-ն է։

### English

- Architecture completeness was assessed GREEN; implementation and lock readiness remain YELLOW.
- Added `D-025_COMPLETENESS_AUDIT.md` and `D-025_DRAFT_PR_REVIEW_RECORD.md`.
- Upgraded `validate_platforms.py` into a D-025 conformance validator.
- PR #3 correctly remains open, Draft, and unmerged.
- The next work is Implementation Phase A.

"""
prepend(
    "platforms/design/CHANGELOG.md",
    "# MenQ Design Platform — Changelog / MenQ Design Platform — Փոփոխությունների պատմություն\n\n",
    "## 2026-07-12 — D-025 completeness audit, validator, and Draft PR review",
    section_design,
)

section_root = """## 2026-07-12 — D-025 audit and validator closure

### Հայերեն

- D-025 architecture completeness-ը GREEN է, implementation/lock readiness-ը՝ YELLOW։
- Canonical audit և Draft PR review records-ը ավելացված են։
- Platforms validator-ը այժմ enforce է անում Parts 12–16 architecture set-ը և honest status semantics-ը։
- Հաջորդ աշխատանքը Implementation Phase A-ն է։

### English

- D-025 architecture completeness is GREEN; implementation and lock readiness remain YELLOW.
- Canonical audit and Draft PR review records were added.
- The Platforms validator now enforces the Parts 12–16 architecture set and honest status semantics.
- The next work is Implementation Phase A.

"""
prepend(
    "CHANGELOG.md",
    "# MenQ Standard — Changelog\n\n",
    "## 2026-07-12 — D-025 audit and validator closure",
    section_root,
)
