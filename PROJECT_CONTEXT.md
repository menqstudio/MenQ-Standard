# MenQ Standard — Project Context / MenQ Standard — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Canonical repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-12

## Հայերեն

### Canonical source

MenQ Standard-ի միակ canonical source of truth-ը GitHub repository-ն է։ Chat-ը workshop է, ոչ canonical source։ Repository address-ը և documented persistent rules-ը Owner-ից նոր chat-ում կրկին չեն հարցվում։

### Պարտադիր startup workflow

Յուրաքանչյուր նոր AI session մինչև substantive աշխատանք active branch/ref-ում enumerate և ամբողջությամբ կարդում է բոլոր tracked `.md` files-ը՝ ըստ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`-ի։ Canonical manifest-ը enforce է անում path/size/SHA drift-ը։ Active PR-ի դեպքում նաև կարդացվում են metadata-ն, changed files-ը, diff-ը, review threads-ը և checks-ը։

### Human–AI և authority

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն MenQ architect և engineering teammate է։ Final authority-ն և accountability-ն մարդունն են։ AI-ն չի կարող self-approve անել, human approval հորինել կամ canonical truth-ը ինքնուրույն lock անել։

### Canonical write integrity

Յուրաքանչյուր write ենթարկվում է `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`-ին՝ complete read → SHA preserve → write → beginning/end re-read → synchronization verification → GREEN։ Tool success-ը evidence չէ։

### Decision registry

- `DECISIONS.md` պահպանում է historical `D-001–D-021` registry-ն և մեծ full replacement չի ստանում։
- `DECISION_INDEX.md` active append-only registry է։
- Dedicated decisions-ը պահպանում են `D-022+` records-ը։

### Ընթացիկ canonical վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 Platforms Architecture v1 — merged և canonical։
- D-025 MenQ Design Platform Architecture v1 — `Approved — Implementing`, ոչ `Locked`։
- D-026 Canonical Session Read Law — Locked, enforcement infrastructure GREEN։
- Canonical Markdown inventory — 57 tracked files strict path/size/SHA drift enforcement-ով։
- Working branch — `d-025-design-platform-architecture-v1`։
- Draft PR — `#3`, merge չի արվում մինչև architecture completeness, canonical synchronization, validator evidence, երկու իրական consumer validation և Owner approval։
- Parts 1–11 baseline-ը պահպանված է `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`-ում։
- Part 12 validation architecture-ը պահպանված է `platforms/design/VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`-ում։

### Հաջորդ աշխատանք

Ուղիղ շարունակել Design Platform Part 13-ից՝ Documentation Portal, Component Catalog և Design-Tool Integration Architecture, հետո governance/contribution, adoption/two-consumer validation, specification index, implementation package, completeness audit, validator implementation և Owner review։

---

## English

### Canonical source

The GitHub repository is the single canonical source of truth for MenQ Standard. Conversation is the workshop, not the canonical source. Do not ask the Owner again for the repository address or documented persistent rules.

### Required startup workflow

Before substantive work, every new AI session enumerates and completely reads all tracked `.md` files on the active branch/ref under `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`. The canonical manifest enforces path/size/SHA drift. When an active PR is involved, its metadata, changed files, diff, review threads, and checks must also be read.

### Human–AI and authority

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI may not self-approve, invent human approval, or independently lock canonical truth.

### Canonical write integrity

Every write follows `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`: complete read → preserve SHA → write → re-read beginning and ending → verify synchronization → GREEN. Tool success is not evidence.

### Decision registry

- `DECISIONS.md` preserves the historical `D-001–D-021` registry and is not subject to large full replacement.
- `DECISION_INDEX.md` is the active append-only registry.
- Dedicated decisions preserve `D-022+` records.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- D-024 Platforms Architecture v1 is merged and canonical.
- D-025 MenQ Design Platform Architecture v1 is `Approved — Implementing`, not `Locked`.
- D-026 Canonical Session Read Law is Locked and its enforcement infrastructure is GREEN.
- The canonical Markdown inventory contains 57 tracked files with strict path/size/SHA drift enforcement.
- Working branch: `d-025-design-platform-architecture-v1`.
- Draft PR: `#3`; it remains unmerged until architecture completeness, canonical synchronization, validator evidence, two real consumer validations, and Owner approval.
- Parts 1–11 are preserved in `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`.
- Part 12 validation architecture is preserved in `platforms/design/VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`.

### Next work

Continue directly with Design Platform Part 13: Documentation Portal, Component Catalog, and Design-Tool Integration Architecture, followed by governance/contribution, adoption and two-consumer validation, specification indexing, implementation packaging, completeness audit, validator implementation, and Owner review.

<!-- END: MENQ_STANDARD_PROJECT_CONTEXT -->