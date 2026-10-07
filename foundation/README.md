# Foundation / Հիմք

**Status / Կարգավիճակ:** Locked v1 — Validated GREEN / Հաստատված v1 — ստուգված GREEN  
**Owner / Պատասխանատու:** MenQ Owner

**HY:** Տե՛ս [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md)-ը՝ կայուն context-ի համար, [`FOUNDATION_V1_INTEGRITY_AUDIT.md`](FOUNDATION_V1_INTEGRITY_AUDIT.md)-ը՝ սկզբնական RED audit-ի համար, [`FOUNDATION_V1_REAUDIT.md`](FOUNDATION_V1_REAUDIT.md)-ը՝ YELLOW remediation re-audit-ի համար, և [`FOUNDATION_V1_VALIDATION_RUN.md`](FOUNDATION_V1_VALIDATION_RUN.md)-ը՝ վերջնական GREEN execution evidence-ի համար։

**EN:** See [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) for stable context, [`FOUNDATION_V1_INTEGRITY_AUDIT.md`](FOUNDATION_V1_INTEGRITY_AUDIT.md) for the original RED audit, [`FOUNDATION_V1_REAUDIT.md`](FOUNDATION_V1_REAUDIT.md) for the YELLOW remediation re-audit, and [`FOUNDATION_V1_VALIDATION_RUN.md`](FOUNDATION_V1_VALIDATION_RUN.md) for final GREEN execution evidence.

## Chapters / Chapter-ներ

- [`Philosophy`](philosophy/README.md) — Locked v1; [`context`](philosophy/PROJECT_CONTEXT.md) / Հաստատված v1
- [`Principles`](principles/README.md) — Locked v1; [`context`](principles/PROJECT_CONTEXT.md) / Հաստատված v1
- [`Terminology`](terminology/README.md) — Locked v1, Living Standard; [`context`](terminology/PROJECT_CONTEXT.md) / Հաստատված v1, Living Standard
- [`Governance`](governance/README.md) — Locked v1; [`context`](governance/PROJECT_CONTEXT.md) / Հաստատված v1
- [`Decision System`](decision-system/README.md) — Locked v1; [`context`](decision-system/PROJECT_CONTEXT.md) / Հաստատված v1
- [`Documentation`](documentation/README.md) — Locked v1; [`context`](documentation/PROJECT_CONTEXT.md) / Հաստատված v1
- [`AI Collaboration`](ai-collaboration/README.md) — Locked v1; [`context`](ai-collaboration/PROJECT_CONTEXT.md) / Հաստատված v1

## Supporting controls / Աջակցող controls

- [`FOUNDATION_NORMATIVE_METADATA_REGISTRY.md`](FOUNDATION_NORMATIVE_METADATA_REGISTRY.md) — normalized legacy metadata / normalized legacy metadata
- [`documentation/BILINGUAL_PARITY_ADDENDUM.md`](documentation/BILINGUAL_PARITY_ADDENDUM.md) — Documentation parity control / Documentation-ի parity control
- [`ai-collaboration/BILINGUAL_PARITY_ADDENDUM.md`](ai-collaboration/BILINGUAL_PARITY_ADDENDUM.md) — AI Collaboration parity control / AI Collaboration-ի parity control
- [`documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`](documentation/CANONICAL_WRITE_INTEGRITY_LAW.md) — mandatory safe-write law / պարտադիր safe-write law
- [`ai-collaboration/CANONICAL_SESSION_READ_LAW.md`](ai-collaboration/CANONICAL_SESSION_READ_LAW.md) — mandatory all-Markdown session startup law / պարտադիր all-Markdown session startup law
- [`ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md`](ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md) — dedicated locked decision / dedicated locked decision
- [`../DECISION_INDEX.md`](../DECISION_INDEX.md) — active append-only decision registry / գործող append-only decision registry
- [`../scripts/validate_foundation.py`](../scripts/validate_foundation.py) — integrity validator / integrity validator
- [`../.github/workflows/foundation-integrity.yml`](../.github/workflows/foundation-integrity.yml) — CI enforcement / CI enforcement
- [`../.github/workflows/foundation-v1-package.yml`](../.github/workflows/foundation-v1-package.yml) — validated snapshot packaging / ստուգված snapshot-ի packaging
- [`../release/FOUNDATION_V1_RELEASE_README.md`](../release/FOUNDATION_V1_RELEASE_README.md) — release snapshot description / release snapshot-ի նկարագրություն

## Boundary / Սահման

**HY:** Foundation-ը product-specific implementation details չի պարունակում։ Platforms-ը, Operating Standards-ը և Extensions-ը պետք է բխեն Foundation-ից և չհակասեն դրան։

**EN:** Foundation does not contain product-specific implementation details. Platforms, Operating Standards, and Extensions must derive from Foundation and must not contradict it.

## Current gate / Ընթացիկ gate

**HY:** `Foundation Integrity` workflow run `#9`-ը ավարտվել է `success` conclusion-ով։ Validator-ը վերադարձրել է `FOUNDATION VALIDATION: GREEN` և հաստատել է յոթ Foundation chapter-ներն ու root controls-ը։ Foundation v1 release gate-ը GREEN է։ `D-026`-ով ավելացվել է նոր session-ի պարտադիր all-Markdown read gate-ը, և Foundation validator-ը մեքենայորեն ստուգում է D-026-ի հղումներն ու startup reference-ները։

**EN:** `Foundation Integrity` workflow run `#9` completed with a `success` conclusion. The validator returned `FOUNDATION VALIDATION: GREEN` and confirmed seven Foundation chapters and root controls. The Foundation v1 release gate is GREEN. `D-026` adds the mandatory all-Markdown read gate for every new session; the Foundation validator machine-checks the D-026 links and startup references.

## Next / Հաջորդը

1. Foundation v1.0.0-ը հրապարակված է՝ [`foundation-v1.0.0`](https://github.com/menqstudio/MenQ-Standard/releases/tag/foundation-v1.0.0) (ZIP + `SHA256SUMS.txt`)։ / Foundation v1.0.0 is published: [`foundation-v1.0.0`](https://github.com/menqstudio/MenQ-Standard/releases/tag/foundation-v1.0.0) (ZIP + `SHA256SUMS.txt`).
2. Հետագա release-ները՝ `.github/workflows/publish-release.yml`-ով։ / Later releases go through `.github/workflows/publish-release.yml`.

<!-- END: FOUNDATION_README_V1 -->