# Foundation / Հիմք

**Status / Կարգավիճակ:** Locked v1 — Validated GREEN / Հաստատված v1 — ստուգված GREEN  
**Owner / Պատասխանատու:** MenQ Owner  
**Last synchronized / Վերջին համաժամեցում:** 2026-10-09

**HY:** Տե՛ս [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md)-ը՝ կայուն context-ի համար, [`FOUNDATION_V1_INTEGRITY_AUDIT.md`](FOUNDATION_V1_INTEGRITY_AUDIT.md)-ը՝ սկզբնական RED audit-ի համար, [`FOUNDATION_V1_REAUDIT.md`](FOUNDATION_V1_REAUDIT.md)-ը՝ YELLOW remediation re-audit-ի համար, և [`FOUNDATION_V1_VALIDATION_RUN.md`](FOUNDATION_V1_VALIDATION_RUN.md)-ը՝ 2026-07-12-ի GREEN execution evidence-ի համար։ Ընթացիկ gate-ը՝ ներքևում։

**EN:** See [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) for stable context, [`FOUNDATION_V1_INTEGRITY_AUDIT.md`](FOUNDATION_V1_INTEGRITY_AUDIT.md) for the original RED audit, [`FOUNDATION_V1_REAUDIT.md`](FOUNDATION_V1_REAUDIT.md) for the YELLOW remediation re-audit, and [`FOUNDATION_V1_VALIDATION_RUN.md`](FOUNDATION_V1_VALIDATION_RUN.md) for the GREEN execution evidence of 2026-07-12. The current gate is below.

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
- [`ai-collaboration/CANONICAL_SESSION_READ_LAW.md`](ai-collaboration/CANONICAL_SESSION_READ_LAW.md) — mandatory session startup law: bounded core plus area read / պարտադիր session startup law՝ սահմանափակ core և area-ի ընթերցում
- [`ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md`](ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md) — dedicated locked decision, superseded in part by D-028 / dedicated locked decision, մասամբ փոխարինված D-028-ով
- [`ai-collaboration/D-028-BOUNDED-SESSION-READ-LAW.md`](ai-collaboration/D-028-BOUNDED-SESSION-READ-LAW.md) — bounded session read decision (approved; the Owner merged pull request #29 on 2026-10-09) / սահմանափակ session read-ի որոշում (հաստատված. Owner-ը merge է արել pull request #29-ը 2026-10-09-ին)
- [`ai-collaboration/SESSION_READ_MANIFEST.json`](ai-collaboration/SESSION_READ_MANIFEST.json) — session-read core and areas / session-read core և area-ներ
- [`../scripts/check_session_read_budget.py`](../scripts/check_session_read_budget.py) — session-read budget gate / session-read budget-ի gate
- [`../DECISION_INDEX.md`](../DECISION_INDEX.md) — active append-only decision registry / գործող append-only decision registry
- [`../scripts/validate_foundation.py`](../scripts/validate_foundation.py) — integrity validator / integrity validator
- [`../.github/workflows/foundation-integrity.yml`](../.github/workflows/foundation-integrity.yml) — CI enforcement / CI enforcement
- [`../.github/workflows/foundation-v1-package.yml`](../.github/workflows/foundation-v1-package.yml) — validated snapshot packaging / ստուգված snapshot-ի packaging
- [`../release/FOUNDATION_V1_RELEASE_README.md`](../release/FOUNDATION_V1_RELEASE_README.md) — release snapshot description / release snapshot-ի նկարագրություն

## Boundary / Սահման

**HY:** Foundation-ը product-specific implementation details չի պարունակում։ Platforms-ը, Operating Standards-ը և Extensions-ը պետք է բխեն Foundation-ից և չհակասեն դրան։

**EN:** Foundation does not contain product-specific implementation details. Platforms, Operating Standards, and Extensions must derive from Foundation and must not contradict it.

## Current gate / Ընթացիկ gate

**HY:** 2026-10-09-ին `python3 scripts/validate_foundation.py`-ը, գործարկված local clone-ում `main`-ի `7b5d0ca` commit-ի վրա հիմնված working tree-ում, տպել է `FOUNDATION VALIDATION: GREEN` և `Validated 7 Foundation chapters, root controls, D-026 synchronization, 9 workflows, and 134 tracked Markdown files.`։ Սա local գործարկում է, ոչ թե CI run․ այս պարբերության համար ոչ մի workflow run չի կարդացվել։ 2026-07-12-ի workflow run `#9`-ը, որը այս պարբերությունը մինչև 2026-10-09 նշում էր որպես ընթացիկ evidence, մնում է պատմական գրառում [`FOUNDATION_V1_VALIDATION_RUN.md`](FOUNDATION_V1_VALIDATION_RUN.md)-ում։ `D-026`-ով ավելացվել էր նոր session-ի պարտադիր all-Markdown read gate-ը․ `D-028`-ը (հաստատված. Owner-ը merge է արել pull request #29-ը 2026-10-09-ին) այն փոխարինում է սահմանափակ core-ի և area-ի ընթերցմամբ։ Foundation validator-ը մեքենայորեն ստուգում է D-026-ի հղումներն ու startup reference-ները, իսկ `scripts/check_session_read_budget.py`-ը՝ session-read manifest-ը և core-ի բայթերի սահմանը։ Ոչ մեկը չի ստուգում, որ session-ը որևէ բան կարդացել է։

**EN:** On 2026-10-09 `python3 scripts/validate_foundation.py`, run in a local clone on a working tree based on `main` commit `7b5d0ca`, printed `FOUNDATION VALIDATION: GREEN` and `Validated 7 Foundation chapters, root controls, D-026 synchronization, 9 workflows, and 134 tracked Markdown files.` This is a local run, not a CI run; no workflow run was read for this paragraph. Workflow run `#9` of 2026-07-12, which this paragraph named as the current evidence until 2026-10-09, remains the historical record in [`FOUNDATION_V1_VALIDATION_RUN.md`](FOUNDATION_V1_VALIDATION_RUN.md). `D-026` added the mandatory all-Markdown read gate for every new session; `D-028` (approved; the Owner merged pull request #29 on 2026-10-09) replaces it with the bounded core and area read. The Foundation validator machine-checks the D-026 links and startup references, and `scripts/check_session_read_budget.py` checks the session-read manifest and the core byte ceiling. Neither checks that a session read anything.

## Next / Հաջորդը

1. Foundation v1.0.0-ը հրապարակված է՝ [`foundation-v1.0.0`](https://github.com/menqstudio/MenQ-Standard/releases/tag/foundation-v1.0.0) (ZIP + `SHA256SUMS.txt`)։ / Foundation v1.0.0 is published: [`foundation-v1.0.0`](https://github.com/menqstudio/MenQ-Standard/releases/tag/foundation-v1.0.0) (ZIP + `SHA256SUMS.txt`).
2. Հետագա release-ները՝ `.github/workflows/publish-release.yml`-ով։ / Later releases go through `.github/workflows/publish-release.yml`.

<!-- END: FOUNDATION_README_V1 -->