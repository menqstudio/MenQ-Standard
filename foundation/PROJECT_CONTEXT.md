# Foundation — Project Context / Foundation — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Informative  
**Canonical scope / Canonical scope:** `foundation/`  
**Owner / Պատասխանատու:** MenQ Owner  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-12

## Հայերեն

### Նպատակ

`Foundation`-ը MenQ Standard-ի կայուն և պարտադիր հիմքն է։ Այն սահմանում է Philosophy-ն, Principles-ը, Terminology-ն, Governance-ը, Decision System-ը, Documentation-ը և AI Collaboration-ը։ Platforms-ը, Operating Standards-ը և Extensions-ը պետք է բխեն Foundation-ից և չհակասեն դրան։

### Canonical կառուցվածք և վիճակ

- `philosophy/README.md` — Locked v1
- `principles/README.md` — Locked v1
- `terminology/README.md` — Locked v1, Living Standard
- `governance/README.md` — Locked v1
- `decision-system/README.md` — Locked v1
- `documentation/README.md` — Locked v1
- `ai-collaboration/README.md` — Locked v1

Յուրաքանչյուր major chapter ունի `README.md` և `PROJECT_CONTEXT.md`։ Legacy metadata gaps-ը լրացվում են [`FOUNDATION_NORMATIVE_METADATA_REGISTRY.md`](FOUNDATION_NORMATIVE_METADATA_REGISTRY.md)-ով։ Documentation և AI Collaboration mixed-language legacy sections-ի semantic parity-ն լրացվում է իրենց `BILINGUAL_PARITY_ADDENDUM.md` files-ով։

### Authority

- Foundation-level final approval authority-ն MenQ Owner-ինն է։
- AI-ն կարող է ուսումնասիրել, draft, challenge, execute և verify անել միայն իր explicit scope-ի ներսում։
- AI-ն չի կարող self-approve անել կամ Foundation truth-ը ինքնուրույն lock անել։
- Material Foundation change-ը պահանջում է Decision System lifecycle և Owner approval։

### Startup workflow

Foundation-ի հետ աշխատանքից առաջ կարդալ՝ root `README.md`, `PROJECT_CONTEXT.md`, `DECISION_INDEX.md`, `DECISIONS.md`, `CHANGELOG.md`, `ROADMAP.md`, `foundation/README.md`, այս file-ը, Canonical Write Integrity Law-ը և համապատասխան chapter-ը։

### Integrity և decisions

- `DECISIONS.md` պահպանում է historical `D-001–D-021` registry-ն։
- `DECISION_INDEX.md`-ը active append-only registry է և կապում է dedicated `D-022`, `D-023` records-ը։
- Canonical writes-ը ենթարկվում են `documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`-ին։
- Integrity validator-ը պահվում է `scripts/validate_foundation.py`-ում և գործարկվում է CI workflow-ով։
- `Foundation Integrity` workflow run `#9`-ը ավարտվել է `success` conclusion-ով։
- Validator output-ը՝ `FOUNDATION VALIDATION: GREEN` և `Validated 7 Foundation chapters and root controls.`
- Foundation v1 release gate-ը GREEN է։

### Հաջորդ քայլ

Ստեղծել և verify անել Foundation v1 complete repository ZIP snapshot-ը՝ release README, version/date, SHA-256 manifest և missing-file verification-ով։ ZIP-ը հրապարակվում է GitHub Release asset-ով և չի պահվում main branch-ում որպես binary։ Դրանից հետո Platforms architecture-ը բացվում է միայն formal Decision System proposal-ով և Owner approval-ով։

---

## English

### Purpose

`Foundation` is the stable and mandatory base of MenQ Standard. It defines Philosophy, Principles, Terminology, Governance, the Decision System, Documentation, and AI Collaboration. Platforms, Operating Standards, and Extensions must derive from Foundation and must not contradict it.

### Canonical structure and state

- `philosophy/README.md` — Locked v1
- `principles/README.md` — Locked v1
- `terminology/README.md` — Locked v1, Living Standard
- `governance/README.md` — Locked v1
- `decision-system/README.md` — Locked v1
- `documentation/README.md` — Locked v1
- `ai-collaboration/README.md` — Locked v1

Every major chapter contains `README.md` and `PROJECT_CONTEXT.md`. Legacy metadata gaps are supplied by [`FOUNDATION_NORMATIVE_METADATA_REGISTRY.md`](FOUNDATION_NORMATIVE_METADATA_REGISTRY.md). Semantic parity for mixed-language legacy sections in Documentation and AI Collaboration is supplied by their `BILINGUAL_PARITY_ADDENDUM.md` files.

### Authority

- Final Foundation-level approval authority belongs to the MenQ Owner.
- AI may explore, draft, challenge, execute, and verify only within explicit scope.
- AI may not self-approve or independently lock Foundation truth.
- A material Foundation change requires the Decision System lifecycle and Owner approval.

### Startup workflow

Before Foundation work, read the root `README.md`, `PROJECT_CONTEXT.md`, `DECISION_INDEX.md`, `DECISIONS.md`, `CHANGELOG.md`, `ROADMAP.md`, `foundation/README.md`, this file, the Canonical Write Integrity Law, and the relevant chapter.

### Integrity and decisions

- `DECISIONS.md` preserves the historical `D-001–D-021` registry.
- `DECISION_INDEX.md` is the active append-only registry and links dedicated `D-022` and `D-023` records.
- Canonical writes follow `documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`.
- The integrity validator is stored in `scripts/validate_foundation.py` and runs through CI.
- `Foundation Integrity` workflow run `#9` completed with a `success` conclusion.
- Validator output: `FOUNDATION VALIDATION: GREEN` and `Validated 7 Foundation chapters and root controls.`
- The Foundation v1 release gate is GREEN.

### Next step

Create and verify the complete Foundation v1 repository ZIP snapshot with a release README, version/date, SHA-256 manifest, and missing-file verification. Publish the ZIP as a GitHub Release asset and do not store it as a binary in the main branch. After that, open Platforms architecture only through a formal Decision System proposal and Owner approval.

<!-- END: FOUNDATION_PROJECT_CONTEXT -->