#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def update(path: str, transforms):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    for old, new in transforms:
        if old in text:
            text = text.replace(old, new)
    p.write_text(text, encoding="utf-8")


def prepend(path: str, heading: str, marker: str, section: str):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if marker in text:
        return
    if not text.startswith(heading):
        raise SystemExit(f"Unexpected heading in {path}")
    p.write_text(heading + section + text[len(heading):], encoding="utf-8")

# Design Platform state
update("platforms/design/PROJECT_CONTEXT.md", [
    ("- Part 15 product adoption/maturity/two-consumer validation architecture-ը canonical է։\n", "- Part 15 product adoption/maturity/two-consumer validation architecture-ը canonical է։\n- Part 16 canonical specification index/implementation package plan-ը canonical է։\n"),
    ("- Part 15 product adoption, maturity, and two-consumer validation architecture is canonical.\n", "- Part 15 product adoption, maturity, and two-consumer validation architecture is canonical.\n- Part 16 canonical specification index and implementation package plan is canonical.\n"),
    ("1. Part 16 — Canonical Specification Index and Implementation Package Plan։\n2. D-025 completeness audit, validator design և Draft PR #3 review։\n3. Canonical synchronization, GREEN evidence և Owner review։", "1. D-025 completeness audit and architecture gap analysis։\n2. Design Platform validator and CI implementation։\n3. Draft PR #3 review, canonical synchronization, GREEN evidence and Owner review։"),
    ("1. Part 16 — Canonical Specification Index and Implementation Package Plan.\n2. D-025 completeness audit, validator design, and Draft PR #3 review.\n3. Canonical synchronization, GREEN evidence, and Owner review.", "1. D-025 completeness audit and architecture gap analysis.\n2. Design Platform validator and CI implementation.\n3. Draft PR #3 review, canonical synchronization, GREEN evidence, and Owner review."),
])

update("platforms/design/ROADMAP.md", [
    ("- [x] Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.\n", "- [x] Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.\n- [x] Part 16 — Canonical Specification Index and Implementation Package Plan.\n"),
    ("1. Part 16 — Canonical Specification Index and Implementation Package Plan.\n2. D-025 completeness audit, validator design, and Draft PR #3 review.", "1. D-025 completeness audit and architecture gap analysis.\n2. Design Platform validator and CI implementation.\n3. Draft PR #3 review and Owner review."),
])

update("platforms/design/NEXT_CHAT_HANDOFF.md", [
    ("5. Part 15-ը պահպանված է `PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`-ում։\n", "5. Part 15-ը պահպանված է `PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`-ում։\n6. Part 16-ը պահպանված է `CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md`-ում։\n"),
    ("- Part 15: `PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`.\n", "- Part 15: `PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`.\n- Part 16: `CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md`.\n"),
    ("## Part 16 — Canonical Specification Index and Implementation Package Plan", "## D-025 Completeness Audit, Validator Design, and Draft PR Review"),
    ("**Part 16 — Canonical Specification Index and Implementation Package Plan.**", "**D-025 Completeness Audit, Validator Design, and Draft PR Review.**"),
])

# Root continuity
for path in ["PROJECT_CONTEXT.md", "AI_WORKING_CONTEXT.md", "NEXT_CHAT_HANDOFF.md"]:
    update(path, [
        ("Part 15 product adoption/maturity/two-consumer validation architecture-ը նույնպես canonical է։", "Part 15 product adoption/maturity/two-consumer validation architecture-ը և Part 16 specification index/package plan-ը canonical են։"),
        ("Part 15 product adoption, maturity, and two-consumer validation architecture is also canonical.", "Part 15 product adoption/maturity/two-consumer validation architecture and Part 16 specification index/package plan are canonical."),
        ("Part 16 — Canonical Specification Index and Implementation Package Plan", "D-025 Completeness Audit, Validator Design, and Draft PR Review"),
    ])

update("ROADMAP.md", [
    ("- [x] Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan\n", "- [x] Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan\n- [x] Part 16 — Canonical Specification Index and Implementation Package Plan\n"),
    ("1. Part 16 — Canonical Specification Index and Implementation Package Plan.\n2. D-025 completeness audit, validator design, and Draft PR #3 review.\n3. GREEN evidence and Owner review.", "1. D-025 completeness audit and architecture gap analysis.\n2. Design Platform validator and CI implementation.\n3. Draft PR #3 review, GREEN evidence, and Owner review."),
])

section_design = """## 2026-07-12 — Part 16 specification index and implementation package plan

### Հայերեն

- Ավելացվել է `CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md`։
- Սահմանվել են canonical IDs, ownership, dependency graph, package/API mapping և release input contract-ը։
- Սահմանվել է package topology-ը՝ contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales և validation։
- Սահմանվել են deterministic build graph-ը, public API contract-ը, release channels-ը և release manifest-ը։
- Continuation point-ը տեղափոխվել է D-025 completeness audit, validator design և Draft PR review։

### English

- Added `CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md`.
- Defined canonical IDs, ownership, dependency graph, package/API mapping, and release-input contracts.
- Defined package topology for contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales, and validation.
- Defined the deterministic build graph, public API contract, release channels, and release manifest.
- Advanced the continuation point to the D-025 completeness audit, validator design, and Draft PR review.

"""
prepend("platforms/design/CHANGELOG.md", "# MenQ Design Platform — Changelog / MenQ Design Platform — Փոփոխությունների պատմություն\n\n", "## 2026-07-12 — Part 16 specification index and implementation package plan", section_design)

section_root = """## 2026-07-12 — Design Platform Part 16 package architecture

### Հայերեն

- Ավելացվել է canonical specification index և implementation package plan v1-ը։
- Սահմանվել են package boundaries, dependency direction, deterministic build graph, public API և release manifest contracts-ը։
- Continuation point-ը տեղափոխվել է D-025 completeness audit, validator design և Draft PR review։
- D-025-ը մնում է `Approved — Implementing`, Draft PR #3-ը՝ open, Draft և unmerged։

### English

- Added Canonical Specification Index and Implementation Package Plan v1.
- Defined package boundaries, dependency direction, deterministic build graph, public API, and release-manifest contracts.
- Advanced the continuation point to the D-025 completeness audit, validator design, and Draft PR review.
- D-025 remains `Approved — Implementing`; Draft PR #3 remains open, Draft, and unmerged.

"""
prepend("CHANGELOG.md", "# MenQ Standard — Changelog\n\n", "## 2026-07-12 — Design Platform Part 16 package architecture", section_root)
