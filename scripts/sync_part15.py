#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"Missing expected block in {path}: {old[:100]!r}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


def prepend_after_heading(path: str, heading: str, marker: str, section: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if marker in text:
        return
    if not text.startswith(heading):
        raise SystemExit(f"Unexpected heading in {path}")
    p.write_text(heading + section + text[len(heading):], encoding="utf-8")

# Design Platform context
replace(
    "platforms/design/PROJECT_CONTEXT.md",
    "- Part 14 governance/contribution/ownership/change-request architecture-ը canonical է։\n",
    "- Part 14 governance/contribution/ownership/change-request architecture-ը canonical է։\n- Part 15 product adoption/maturity/two-consumer validation architecture-ը canonical է։\n",
)
replace(
    "platforms/design/PROJECT_CONTEXT.md",
    "1. Part 15 — Product Adoption, Maturity Model և Two-Consumer Validation Plan։\n2. Canonical specification index և implementation package plan։\n3. D-025 completeness audit, validator design և Draft PR #3 review։\n4. Canonical synchronization, GREEN evidence և Owner review։",
    "1. Part 16 — Canonical Specification Index and Implementation Package Plan։\n2. D-025 completeness audit, validator design և Draft PR #3 review։\n3. Canonical synchronization, GREEN evidence և Owner review։",
)
replace(
    "platforms/design/PROJECT_CONTEXT.md",
    "- Part 14 governance, contribution, ownership, and change-request lifecycle architecture is canonical.\n",
    "- Part 14 governance, contribution, ownership, and change-request lifecycle architecture is canonical.\n- Part 15 product adoption, maturity, and two-consumer validation architecture is canonical.\n",
)
replace(
    "platforms/design/PROJECT_CONTEXT.md",
    "1. Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.\n2. Canonical specification index and implementation package plan.\n3. D-025 completeness audit, validator design, and Draft PR #3 review.\n4. Canonical synchronization, GREEN evidence, and Owner review.",
    "1. Part 16 — Canonical Specification Index and Implementation Package Plan.\n2. D-025 completeness audit, validator design, and Draft PR #3 review.\n3. Canonical synchronization, GREEN evidence, and Owner review.",
)

# Design roadmap
replace(
    "platforms/design/ROADMAP.md",
    "- [x] Part 14 — Governance, Contribution, Ownership, and Change-Request Lifecycle.\n",
    "- [x] Part 14 — Governance, Contribution, Ownership, and Change-Request Lifecycle.\n- [x] Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.\n",
)
replace(
    "platforms/design/ROADMAP.md",
    "1. Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.\n2. Canonical specification index and implementation package plan.\n3. D-025 completeness audit, validator design, and Draft PR #3 review.",
    "1. Part 16 — Canonical Specification Index and Implementation Package Plan.\n2. D-025 completeness audit, validator design, and Draft PR #3 review.",
)

# Design handoff
replace(
    "platforms/design/NEXT_CHAT_HANDOFF.md",
    "4. Part 14-ը պահպանված է `GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md`-ում։\n",
    "4. Part 14-ը պահպանված է `GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md`-ում։\n5. Part 15-ը պահպանված է `PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`-ում։\n",
)
replace(
    "platforms/design/NEXT_CHAT_HANDOFF.md",
    "## Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan",
    "## Part 16 — Canonical Specification Index and Implementation Package Plan",
)
replace(
    "platforms/design/NEXT_CHAT_HANDOFF.md",
    "15. Product adoption, maturity model և two-consumer validation plan։\n16. Canonical specification index և implementation package plan։",
    "16. Canonical specification index և implementation package plan։",
)
replace(
    "platforms/design/NEXT_CHAT_HANDOFF.md",
    "- Part 14: `GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md`.\n",
    "- Part 14: `GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md`.\n- Part 15: `PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`.\n",
)
replace(
    "platforms/design/NEXT_CHAT_HANDOFF.md",
    "**Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.**",
    "**Part 16 — Canonical Specification Index and Implementation Package Plan.**",
)

# Root continuity
for path in ["PROJECT_CONTEXT.md", "AI_WORKING_CONTEXT.md", "NEXT_CHAT_HANDOFF.md"]:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    text = text.replace(
        "Part 14 governance/contribution/ownership/change-request architecture-ը canonical է։",
        "Part 14 governance/contribution/ownership/change-request architecture-ը canonical է։ Part 15 product adoption/maturity/two-consumer validation architecture-ը նույնպես canonical է։",
    )
    text = text.replace(
        "Part 14 governance, contribution, ownership, and change-request lifecycle architecture is canonical.",
        "Part 14 governance, contribution, ownership, and change-request lifecycle architecture is canonical. Part 15 product adoption, maturity, and two-consumer validation architecture is also canonical.",
    )
    text = text.replace(
        "Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan",
        "Part 16 — Canonical Specification Index and Implementation Package Plan",
    )
    text = text.replace(
        "Product adoption, maturity model և two-consumer validation plan։\n2. Canonical specification index և implementation package plan։",
        "Canonical specification index և implementation package plan։",
    )
    text = text.replace(
        "Product adoption, maturity model, and two-consumer validation plan.\n2. Canonical specification index and implementation package plan.",
        "Canonical specification index and implementation package plan.",
    )
    p.write_text(text, encoding="utf-8")

replace(
    "ROADMAP.md",
    "- [x] Part 14 — Governance, Contribution, Ownership, and Change-Request Lifecycle\n",
    "- [x] Part 14 — Governance, Contribution, Ownership, and Change-Request Lifecycle\n- [x] Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan\n",
)
replace(
    "ROADMAP.md",
    "1. Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.\n2. Canonical specification index and implementation package plan.\n3. D-025 completeness audit, validator design, and Draft PR #3 review.\n4. GREEN evidence and Owner review.",
    "1. Part 16 — Canonical Specification Index and Implementation Package Plan.\n2. D-025 completeness audit, validator design, and Draft PR #3 review.\n3. GREEN evidence and Owner review.",
)

# Changelogs
section_design = """## 2026-07-12 — Part 15 product adoption and two-consumer validation architecture

### Հայերեն

- Ավելացվել է `PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`։
- Սահմանվել են M0–M5 adoption maturity levels-ը, evidence-backed downgrade rule-ը և consumer record contract-ը։
- Երկու consumers-ը պետք է տարբերվեն առնվազն երեք meaningful dimensions-ով։
- Demo-ն, duplicated shell-ը, նույն app-ի երկու page-ը կամ branding variant-ը երկու consumer չեն համարվում։
- Lock gate-ը պահանջում է երկու distinct M3 consumers, առնվազն մեկ M4 operational consumer և explicit Owner approval։
- Continuation point-ը տեղափոխվել է Part 16 — Canonical Specification Index and Implementation Package Plan։

### English

- Added `PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`.
- Defined M0–M5 adoption maturity levels, evidence-backed downgrade rules, and the consumer record contract.
- Required two consumers to differ across at least three meaningful dimensions.
- A demo, duplicated shell, two pages of one app, or branding variants do not count as two consumers.
- The lock gate requires two distinct M3 consumers, at least one M4 operational consumer, and explicit Owner approval.
- Advanced the continuation point to Part 16 — Canonical Specification Index and Implementation Package Plan.

"""
prepend_after_heading(
    "platforms/design/CHANGELOG.md",
    "# MenQ Design Platform — Changelog / MenQ Design Platform — Փոփոխությունների պատմություն\n\n",
    "## 2026-07-12 — Part 15 product adoption and two-consumer validation architecture",
    section_design,
)

section_root = """## 2026-07-12 — Design Platform Part 15 adoption architecture

### Հայերեն

- Ավելացվել է product adoption, maturity model և two-consumer validation architecture v1-ը։
- Adoption-ը սահմանվել է որպես governed contract consumption և operational evidence, ոչ package install։
- Սահմանվել են M0–M5 maturity levels-ը և երկու genuinely distinct consumers-ի validation rule-ը։
- Continuation point-ը տեղափոխվել է Part 16 — Canonical Specification Index and Implementation Package Plan։
- D-025-ը մնում է `Approved — Implementing`, Draft PR #3-ը՝ open, Draft և unmerged։

### English

- Added Product Adoption, Maturity Model, and Two-Consumer Validation Architecture v1.
- Defined adoption as governed contract consumption and operational evidence, not package installation.
- Defined M0–M5 maturity levels and the validation rule for two genuinely distinct consumers.
- Advanced the continuation point to Part 16 — Canonical Specification Index and Implementation Package Plan.
- D-025 remains `Approved — Implementing`; Draft PR #3 remains open, Draft, and unmerged.

"""
prepend_after_heading(
    "CHANGELOG.md",
    "# MenQ Standard — Changelog\n\n",
    "## 2026-07-12 — Design Platform Part 15 adoption architecture",
    section_root,
)
