# MenQ Design Platform — Project Context / MenQ Design Platform — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Merged — post-merge closure in progress / Merged — post-merge closure-ը ընթացքի մեջ է  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** MenQ Owner  
**Parent architecture:** [`../D-024-PLATFORMS-ARCHITECTURE-V1.md`](../D-024-PLATFORMS-ARCHITECTURE-V1.md)  
**Current decision:** [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md)

## Հայերեն

### Նպատակ

MenQ Design Platform-ը ամբողջ MenQ ecosystem-ի reusable, product-neutral design capability system-ն է՝ contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales, validation, delivery և adoption boundaries-ով։ Product-specific identity, business logic և domain workflow shared core չեն մտնում։

### Ընթացիկ canonical վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 — merged և canonical։
- D-025 — PR #3-ով merge է եղել, բայց `Locked` չէ։
- D-026 — Locked և machine-enforced։
- PR #3 merge commit — `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`։
- Merged implementation head — `9c10c288c16ef319ce4d5aa91000f7b0a46ecf60`։
- Closure branch — `d-025-post-merge-closure`։
- Parts 1–16 architecture set-ը canonical է։
- Canonical registry, schemas, ownership, dependency graph և 10 package boundaries-ը implemented են։
- Private preview release candidate-ը `0.1.0-next.0` է։
- Deterministic build, checksums, public API, compatibility, migration և rollback evidence-ը GREEN են։
- `MenQ Design Catalog` consumer-ը M3/GREEN է։
- `MenQ Release Evidence Console` consumer-ը M4 operational/GREEN է։
- Cross-consumer validation և quality/adoption evidence-ը GREEN են։
- Post-merge canonical synchronization և `main` automation evidence-ը դեռ closure gate են։

### Evidence

- Readiness record՝ `implementation/release/d-025-readiness-record.json`։
- Merge evidence՝ [`D-025_POST_MERGE_CLOSURE_RECORD.md`](D-025_POST_MERGE_CLOSURE_RECORD.md)։
- Audit՝ `D-025_COMPLETENESS_AUDIT.md`։
- PR review՝ `D-025_DRAFT_PR_REVIEW_RECORD.md`։

### Authority boundary և հաջորդ քայլ

Merge-ը lock authorization չէ։ Closure PR-ի checks-ը և դրանից հետո `main` push checks-ը պետք է GREEN լինեն։ Միայն դրանից հետո Owner-ին ներկայացվում է առանձին D-025 lock որոշում։

---

## English

### Purpose

The MenQ Design Platform is the reusable, product-neutral design capability system for the MenQ ecosystem, with governed boundaries for contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales, validation, delivery, and adoption. Product identity, business logic, and domain workflows do not enter the shared core.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- D-024 is merged and canonical.
- D-025 was merged through PR #3 but is not `Locked`.
- D-026 is Locked and machine-enforced.
- PR #3 merge commit: `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`.
- Merged implementation head: `9c10c288c16ef319ce4d5aa91000f7b0a46ecf60`.
- Closure branch: `d-025-post-merge-closure`.
- The Parts 1–16 architecture set is canonical.
- The canonical registry, schemas, ownership, dependency graph, and ten package boundaries are implemented.
- The private preview release candidate is `0.1.0-next.0`.
- Deterministic build, checksums, public API, compatibility, migration, and rollback evidence are GREEN.
- The `MenQ Design Catalog` consumer is M3/GREEN.
- The `MenQ Release Evidence Console` consumer is M4 operational/GREEN.
- Cross-consumer validation and quality/adoption evidence are GREEN.
- Post-merge canonical synchronization and `main` automation evidence remain closure gates.

### Evidence

- Readiness record: `implementation/release/d-025-readiness-record.json`.
- Merge evidence: [`D-025_POST_MERGE_CLOSURE_RECORD.md`](D-025_POST_MERGE_CLOSURE_RECORD.md).
- Audit: `D-025_COMPLETENESS_AUDIT.md`.
- PR review: `D-025_DRAFT_PR_REVIEW_RECORD.md`.

### Authority boundary and next step

Merge is not lock authorization. Closure PR checks and subsequent `main` push checks must be GREEN. Only then is a separate D-025 lock decision presented to the Owner.

<!-- END: MENQ_DESIGN_PLATFORM_PROJECT_CONTEXT -->
