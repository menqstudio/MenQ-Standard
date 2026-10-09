# MenQ Design Platform — Project Context / MenQ Design Platform — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Locked and GREEN / Locked և GREEN  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** MenQ Owner  
**Parent architecture:** [`../D-024-PLATFORMS-ARCHITECTURE-V1.md`](../D-024-PLATFORMS-ARCHITECTURE-V1.md)  
**Current decisions / Գործող որոշումներ:** [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md), [`decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md`](decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md)  
**Last synchronized / Վերջին համաժամեցում:** 2026-10-09 (`CR-0012`)

> **Status note / Status-ի նշում (2026-10-09):** Վերևի «Locked և GREEN»-ը 2026-07-13-ի lock-ի պիտակն է։ `Locked`-ը ուժի մեջ է։ «GREEN»-ը այլևս չի ծածկում երկու իրական consumer-ի պայմանը. այն ուղղվել է 2026-10-07-ին և բաց է։ Պիտակը փոխելը Owner-ի որոշում է (տես `CR-0012`)։ / The "Locked and GREEN" above is the label of the 2026-07-13 lock. `Locked` is in force. "GREEN" no longer covers the two-real-consumer condition, which was corrected on 2026-10-07 and is open. Changing the label is the Owner's decision (see `CR-0012`).

## Հայերեն

### Նպատակ

MenQ Design Platform-ը ամբողջ MenQ ecosystem-ի reusable, product-neutral design capability system-ն է՝ contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales, validation, delivery և adoption boundaries-ով։ Product-specific identity, business logic և domain workflow shared core չեն մտնում։

### Ընթացիկ canonical վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 — Locked (2026-10-07)։
- D-025 — `Locked` (2026-07-13, Owner-ի որոշմամբ)։ Lock-ի հետ գրանցված GREEN-ը այլևս չի ծածկում երկու իրական consumer-ի պայմանը (տես ներքևի կետերը)։
- D-026 — Locked. մասամբ փոխարինված է D-028-ով (հաստատված. Owner-ը merge է արել pull request #29-ը 2026-10-09-ին)։ CI-ը ստուգում է Markdown inventory-ն և session-read core-ի բայթերի սահմանը, ոչ թե session-ի ընթերցումը։
- Parts 1–16 architecture set-ը canonical է։
- Canonical registry, schemas, ownership, dependency graph և 10 package boundaries-ը implemented են։
- Private preview candidate-ը `0.1.0-next.0` է։
- Deterministic build, checksums, public API, compatibility, migration և rollback evidence-ը GREEN են։
- `MenQ Design Catalog` և `MenQ Release Evidence Console` consumer-ները repository-ի ներսի reference pilot-ներ են՝ վերագնահատված M2 (2026-10-07), քանի որ նրանց M3/M4 verdict-ը self-attested էր։ Տես [`D-025_EVIDENCE_CORRECTION_RECORD.md`](D-025_EVIDENCE_CORRECTION_RECORD.md)։
- Մշտական preview release՝ [`design-platform-v0.1.0-next.0`](https://github.com/menqstudio/MenQ-Standard/releases/tag/design-platform-v0.1.0-next.0)։
- Cross-consumer validation-ը և quality/adoption evidence-ը 2026-07-13-ին գրանցվել են GREEN՝ repository-ի ներսի երկու pilot-ի հիման վրա։ 2026-10-07-ի ուղղումից հետո դա երկու իրական consumer-ի evidence չէ. պարտավորությունը բաց է։ Readiness record-ի top-level դաշտերը դեռ ցույց են տալիս 2026-07-13-ի արժեքները. ընթացիկ վիճակը նրա `current` դաշտում է։
- Part 14 governance-ի implementation-ը `Locked` է 2026-10-07-ից ([`governance/`](governance/README.md))։ Change request-ներ՝ փակված `CR-0001`…`CR-0004`, բաց `CR-0005`…`CR-0011` (աշխատանքը merge է եղել, evidence-ը պակասում է), առաջարկված `CR-0012`։
- D-027 brand expression շերտը ([`brand-expression/`](brand-expression/README.md)). որոշումը `Approved — Implementing` է, շերտի lifecycle-ը՝ Draft։ Չափված է 2026-10-09-ին՝ 132 token (`source/brand-tokens.source.json`), 35 core կոմպոնենտ bundle-ում, 5 Bro կոմպոնենտ ([`product-extensions/bro/`](product-extensions/bro/README.md))։
- Repository-ի առաջին էջի ստանդարտ v1-ը ([`repository-front/`](repository-front/README.md)) Draft է (`CR-0011`)։

### Merge և lock evidence

- Implementation merge՝ `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`։
- Closure merge՝ `9a833339b1d707d6cd8a792e031dd8ca2857d556`։
- Lock merge՝ `261f85e5b20d726a0ab1f05da84a4dc45a248873`։
- Validated lock head՝ `8ba2e987ff6dab2c25fda18744c7376953d0108f`։
- Explicit Owner lock approval՝ 2026-07-13։
- Final audit՝ [`D-025_FINAL_POST_LOCK_AUDIT.md`](D-025_FINAL_POST_LOCK_AUDIT.md)։

### Authority boundary և հաջորդ քայլ

D-025 transaction-ը փակված է (PR #3, #4, #5)։ Բաց են՝ (1) իրական consumer-ի պարտավորությունը. առաջինը MenQ Webpage-ն է, երկրորդը ընտրում է Owner-ը, (2) D-025 ↔ D-027 token mapping-ի որոշումը, (3) `CR-0005`…`CR-0011`-ի evidence-ը, (4) հիմնական Button-ի կոնտրաստի թերությունը, (5) status պիտակների հակասությունները։ Մանրամասները՝ [`NEXT_CHAT_HANDOFF.md`](NEXT_CHAT_HANDOFF.md) և [`ROADMAP.md`](ROADMAP.md)։ Architecture-ի հետագա փոփոխությունը պահանջում է governed change request, impact analysis, compatibility/migration evidence, validators և explicit Owner approval։

---

## English

### Purpose

The MenQ Design Platform is the reusable, product-neutral design capability system for the MenQ ecosystem, with governed boundaries for contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales, validation, delivery, and adoption. Product identity, business logic, and domain workflows do not enter the shared core.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- D-024 is Locked (2026-10-07).
- D-025 is `Locked` (2026-07-13, by Owner decision). The GREEN recorded with the lock no longer covers the two-real-consumer condition (see the bullets below).
- D-026 is Locked and superseded in part by D-028 (approved; the Owner merged pull request #29 on 2026-10-09). CI checks the Markdown inventory and the session-read core byte ceiling, not a session's read.
- The Parts 1–16 architecture set is canonical.
- The canonical registry, schemas, ownership, dependency graph, and ten package boundaries are implemented.
- The private preview candidate is `0.1.0-next.0`.
- Deterministic build, checksums, public API, compatibility, migration, and rollback evidence are GREEN.
- The `MenQ Design Catalog` and `MenQ Release Evidence Console` consumers are in-repository reference pilots, re-graded to M2 on 2026-10-07 because their M3/M4 verdicts were self-attested. See [`D-025_EVIDENCE_CORRECTION_RECORD.md`](D-025_EVIDENCE_CORRECTION_RECORD.md).
- Permanent preview release: [`design-platform-v0.1.0-next.0`](https://github.com/menqstudio/MenQ-Standard/releases/tag/design-platform-v0.1.0-next.0).
- Cross-consumer validation and quality/adoption evidence were recorded GREEN on 2026-07-13, on the basis of the two in-repository pilots. After the 2026-10-07 correction that is not evidence of two real consumers; the obligation is open. The readiness record's top-level fields still show the 2026-07-13 values; the current state is in its `current` field.
- The Part 14 governance implementation has been `Locked` since 2026-10-07 ([`governance/`](governance/README.md)). Change requests: `CR-0001`…`CR-0004` closed, `CR-0005`…`CR-0011` open (work merged, evidence missing), `CR-0012` proposed.
- The D-027 brand expression layer ([`brand-expression/`](brand-expression/README.md)): the decision is `Approved — Implementing`; the layer's lifecycle is Draft. Measured on 2026-10-09: 132 tokens (`source/brand-tokens.source.json`), 35 core components in the bundle, 5 Bro components ([`product-extensions/bro/`](product-extensions/bro/README.md)).
- Repository front page standard v1 ([`repository-front/`](repository-front/README.md)) is Draft (`CR-0011`).

### Merge and lock evidence

- Implementation merge: `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`.
- Closure merge: `9a833339b1d707d6cd8a792e031dd8ca2857d556`.
- Lock merge: `261f85e5b20d726a0ab1f05da84a4dc45a248873`.
- Validated lock head: `8ba2e987ff6dab2c25fda18744c7376953d0108f`.
- Explicit Owner lock approval: 2026-07-13.
- Final audit: [`D-025_FINAL_POST_LOCK_AUDIT.md`](D-025_FINAL_POST_LOCK_AUDIT.md).

### Authority boundary and next step

The D-025 transaction is closed (PR #3, #4, #5). Open: (1) the real-consumer obligation — MenQ Webpage is the first, the Owner selects the second; (2) the D-025 ↔ D-027 token-mapping decision; (3) the evidence for `CR-0005`…`CR-0011`; (4) the primary Button contrast defect; (5) the status-label conflicts. Details: [`NEXT_CHAT_HANDOFF.md`](NEXT_CHAT_HANDOFF.md) and [`ROADMAP.md`](ROADMAP.md). Future architecture changes require a governed change request, impact analysis, compatibility and migration evidence, validators, and explicit Owner approval.

<!-- END: MENQ_DESIGN_PLATFORM_PROJECT_CONTEXT -->