# MenQ Design Platform — Project Context / MenQ Design Platform — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Locked and GREEN / Locked և GREEN  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** MenQ Owner  
**Parent architecture:** [`../D-024-PLATFORMS-ARCHITECTURE-V1.md`](../D-024-PLATFORMS-ARCHITECTURE-V1.md)  
**Current decision:** [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md)

## Հայերեն

### Նպատակ

MenQ Design Platform-ը ամբողջ MenQ ecosystem-ի reusable, product-neutral design capability system-ն է՝ contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales, validation, delivery և adoption boundaries-ով։ Product-specific identity, business logic և domain workflow shared core չեն մտնում։

### Ընթացիկ canonical վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 — Locked (2026-10-07)։
- D-025 — Locked և GREEN։
- D-026 — Locked և machine-enforced։
- Parts 1–16 architecture set-ը canonical է։
- Canonical registry, schemas, ownership, dependency graph և 10 package boundaries-ը implemented են։
- Private preview candidate-ը `0.1.0-next.0` է։
- Deterministic build, checksums, public API, compatibility, migration և rollback evidence-ը GREEN են։
- `MenQ Design Catalog` և `MenQ Release Evidence Console` consumer-ները repository-ի ներսի reference pilot-ներ են՝ վերագնահատված M2 (2026-10-07), քանի որ նրանց M3/M4 verdict-ը self-attested էր։ Տես [`D-025_EVIDENCE_CORRECTION_RECORD.md`](D-025_EVIDENCE_CORRECTION_RECORD.md)։
- Մշտական preview release՝ [`design-platform-v0.1.0-next.0`](https://github.com/menqstudio/MenQ-Standard/releases/tag/design-platform-v0.1.0-next.0)։
- Cross-consumer validation և quality/adoption evidence-ը GREEN են։

### Merge և lock evidence

- Implementation merge՝ `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`։
- Closure merge՝ `9a833339b1d707d6cd8a792e031dd8ca2857d556`։
- Lock merge՝ `261f85e5b20d726a0ab1f05da84a4dc45a248873`։
- Validated lock head՝ `8ba2e987ff6dab2c25fda18744c7376953d0108f`։
- Explicit Owner lock approval՝ 2026-07-13։
- Final audit՝ [`D-025_FINAL_POST_LOCK_AUDIT.md`](D-025_FINAL_POST_LOCK_AUDIT.md)։

### Authority boundary և հաջորդ քայլ

D-025 transaction-ը փակված է։ Բաց պարտավորություն՝ առաջին իրական consumer-ը MenQ Webpage-ն է, երկրորդը ընտրում է Owner-ը։ Architecture-ի հետագա փոփոխությունը պահանջում է governed change request, impact analysis, compatibility/migration evidence, validators և explicit Owner approval։

---

## English

### Purpose

The MenQ Design Platform is the reusable, product-neutral design capability system for the MenQ ecosystem, with governed boundaries for contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales, validation, delivery, and adoption. Product identity, business logic, and domain workflows do not enter the shared core.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- D-024 is Locked (2026-10-07).
- D-025 is Locked and GREEN.
- D-026 is Locked and machine-enforced.
- The Parts 1–16 architecture set is canonical.
- The canonical registry, schemas, ownership, dependency graph, and ten package boundaries are implemented.
- The private preview candidate is `0.1.0-next.0`.
- Deterministic build, checksums, public API, compatibility, migration, and rollback evidence are GREEN.
- The `MenQ Design Catalog` and `MenQ Release Evidence Console` consumers are in-repository reference pilots, re-graded to M2 on 2026-10-07 because their M3/M4 verdicts were self-attested. See [`D-025_EVIDENCE_CORRECTION_RECORD.md`](D-025_EVIDENCE_CORRECTION_RECORD.md).
- Permanent preview release: [`design-platform-v0.1.0-next.0`](https://github.com/menqstudio/MenQ-Standard/releases/tag/design-platform-v0.1.0-next.0).
- Cross-consumer validation and quality/adoption evidence are GREEN.

### Merge and lock evidence

- Implementation merge: `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`.
- Closure merge: `9a833339b1d707d6cd8a792e031dd8ca2857d556`.
- Lock merge: `261f85e5b20d726a0ab1f05da84a4dc45a248873`.
- Validated lock head: `8ba2e987ff6dab2c25fda18744c7376953d0108f`.
- Explicit Owner lock approval: 2026-07-13.
- Final audit: [`D-025_FINAL_POST_LOCK_AUDIT.md`](D-025_FINAL_POST_LOCK_AUDIT.md).

### Authority boundary and next step

The D-025 transaction is closed. Open obligation: MenQ Webpage is the first real consumer; the Owner selects the second. Future architecture changes require a governed change request, impact analysis, compatibility and migration evidence, validators, and explicit Owner approval.

<!-- END: MENQ_DESIGN_PLATFORM_PROJECT_CONTEXT -->