# MenQ Design Platform — Project Context / MenQ Design Platform — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** D-025 Locked and GREEN / D-025 Locked և GREEN  
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
- D-025 — Locked և machine-enforced։
- D-026 — Locked և machine-enforced։
- PR #3 implementation merge commit — `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`։
- PR #4 closure merge commit — `9a833339b1d707d6cd8a792e031dd8ca2857d556`։
- Validated closure head — `b16e0211bb29355df43257847fce818765a4a747`։
- Parts 1–16 architecture set-ը canonical է։
- Canonical registry, schemas, ownership, dependency graph և 10 package boundaries-ը implemented են։
- Private preview release candidate-ը `0.1.0-next.0` է։
- Deterministic build, checksums, public API, compatibility, migration և rollback evidence-ը GREEN են։
- `MenQ Design Catalog` consumer-ը M3/GREEN է։
- `MenQ Release Evidence Console` consumer-ը M4 operational/GREEN է։
- Cross-consumer validation և quality/adoption evidence-ը GREEN են։
- D-025 is Locked։

### Evidence

- Readiness record՝ `implementation/release/d-025-readiness-record.json`։
- Post-merge closure record՝ [`D-025_POST_MERGE_CLOSURE_RECORD.md`](D-025_POST_MERGE_CLOSURE_RECORD.md)։
- Lock record՝ [`D-025_LOCK_RECORD.md`](D-025_LOCK_RECORD.md)։
- Audit՝ `D-025_COMPLETENESS_AUDIT.md`։
- PR review՝ `D-025_DRAFT_PR_REVIEW_RECORD.md`։

### Locked change boundary

D-025-ի հետագա փոփոխությունները պահանջում են governed change request, impact analysis, compatibility/migration evidence, validators և explicit Owner approval։ Lock-ը չի արգելում զարգացումը․ այն արգելում է silent drift-ը։

---

## English

### Purpose

The MenQ Design Platform is the reusable, product-neutral design capability system for the MenQ ecosystem, with governed boundaries for contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales, validation, delivery, and adoption. Product identity, business logic, and domain workflows do not enter the shared core.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- D-024 is merged and canonical.
- D-025 is Locked and machine-enforced.
- D-026 is Locked and machine-enforced.
- PR #3 implementation merge commit: `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`.
- PR #4 closure merge commit: `9a833339b1d707d6cd8a792e031dd8ca2857d556`.
- Validated closure head: `b16e0211bb29355df43257847fce818765a4a747`.
- The Parts 1–16 architecture set is canonical.
- The canonical registry, schemas, ownership, dependency graph, and ten package boundaries are implemented.
- The private preview release candidate is `0.1.0-next.0`.
- Deterministic build, checksums, public API, compatibility, migration, and rollback evidence are GREEN.
- The `MenQ Design Catalog` consumer is M3/GREEN.
- The `MenQ Release Evidence Console` consumer is M4 operational/GREEN.
- Cross-consumer validation and quality/adoption evidence are GREEN.
- D-025 is Locked.

### Evidence

- Readiness record: `implementation/release/d-025-readiness-record.json`.
- Post-merge closure record: [`D-025_POST_MERGE_CLOSURE_RECORD.md`](D-025_POST_MERGE_CLOSURE_RECORD.md).
- Lock record: [`D-025_LOCK_RECORD.md`](D-025_LOCK_RECORD.md).
- Audit: `D-025_COMPLETENESS_AUDIT.md`.
- PR review: `D-025_DRAFT_PR_REVIEW_RECORD.md`.

### Locked change boundary

Future D-025 changes require a governed change request, impact analysis, compatibility and migration evidence, validators, and explicit Owner approval. Lock does not prevent evolution; it prevents silent drift.

<!-- END: MENQ_DESIGN_PLATFORM_PROJECT_CONTEXT -->