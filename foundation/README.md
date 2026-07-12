# Foundation / Հիմք

**Status / Կարգավիճակ:** Locked v1 — Remediated, validation pending / Հաստատված v1 — ուղղումները կիրառված են, validation-ը սպասվում է  
**Owner / Պատասխանատու:** MenQ Owner

See [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) for stable context, [`FOUNDATION_V1_INTEGRITY_AUDIT.md`](FOUNDATION_V1_INTEGRITY_AUDIT.md) for the original RED audit, and [`FOUNDATION_V1_REAUDIT.md`](FOUNDATION_V1_REAUDIT.md) for the current YELLOW re-audit.

## Chapters / Chapter-ներ

- [`Philosophy`](philosophy/README.md) — Locked v1; [`context`](philosophy/PROJECT_CONTEXT.md)
- [`Principles`](principles/README.md) — Locked v1; [`context`](principles/PROJECT_CONTEXT.md)
- [`Terminology`](terminology/README.md) — Locked v1, Living Standard; [`context`](terminology/PROJECT_CONTEXT.md)
- [`Governance`](governance/README.md) — Locked v1; [`context`](governance/PROJECT_CONTEXT.md)
- [`Decision System`](decision-system/README.md) — Locked v1; [`context`](decision-system/PROJECT_CONTEXT.md)
- [`Documentation`](documentation/README.md) — Locked v1; [`context`](documentation/PROJECT_CONTEXT.md)
- [`AI Collaboration`](ai-collaboration/README.md) — Locked v1; [`context`](ai-collaboration/PROJECT_CONTEXT.md)

## Supporting controls / Աջակցող controls

- [`FOUNDATION_NORMATIVE_METADATA_REGISTRY.md`](FOUNDATION_NORMATIVE_METADATA_REGISTRY.md) — normalized legacy metadata
- [`documentation/BILINGUAL_PARITY_ADDENDUM.md`](documentation/BILINGUAL_PARITY_ADDENDUM.md) — Documentation parity control
- [`ai-collaboration/BILINGUAL_PARITY_ADDENDUM.md`](ai-collaboration/BILINGUAL_PARITY_ADDENDUM.md) — AI Collaboration parity control
- [`documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`](documentation/CANONICAL_WRITE_INTEGRITY_LAW.md) — mandatory safe-write law
- [`../DECISION_INDEX.md`](../DECISION_INDEX.md) — active append-only decision registry
- [`../scripts/validate_foundation.py`](../scripts/validate_foundation.py) — integrity validator
- [`../.github/workflows/foundation-integrity.yml`](../.github/workflows/foundation-integrity.yml) — CI enforcement

## Boundary / Սահման

**HY:** Foundation-ը product-specific implementation details չի պարունակում։ Platforms-ը, Operating Standards-ը և Extensions-ը պետք է բխեն Foundation-ից և չհակասեն դրան։

**EN:** Foundation does not contain product-specific implementation details. Platforms, Operating Standards, and Extensions must derive from Foundation and must not contradict it.

## Current gate / Ընթացիկ gate

**HY:** Repository-side remediation-ը կիրառված է։ Release gate-ը YELLOW է մինչև validator-ի իրական GREEN execution evidence-ը։

**EN:** Repository-side remediation has been applied. The release gate remains YELLOW until real GREEN validator execution evidence exists.

## Next / Հաջորդը

1. Run `python scripts/validate_foundation.py` locally or verify the Foundation Integrity workflow.
2. On GREEN, create the complete Foundation v1 ZIP snapshot.
3. Then open the formal Platforms architecture decision.

<!-- END: FOUNDATION_README_V1 -->