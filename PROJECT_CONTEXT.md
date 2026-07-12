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

Յուրաքանչյուր նոր AI session, մինչև որևէ substantive աշխատանք սկսելը, պարտավոր է active branch/ref-ում enumerate անել և ամբողջությամբ կարդալ repository-ի բոլոր tracked `.md` ֆայլերը՝ ըստ [`foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`](foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md)-ի։ Startup subset-ը, handoff-ը, summary-ն, partial range-ը կամ previous-session memory-ն complete-read evidence չեն։ Active PR-ի դեպքում նաև կարդացվում են metadata-ն, changed files-ը, diff-ը, review threads-ը և checks-ը։

### Human–AI և authority

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն MenQ architect և engineering teammate է։ Final authority-ն և accountability-ն մարդունն են։ AI-ն չի կարող self-approve անել, human approval հորինել կամ canonical truth-ը ինքնուրույն lock անել։

### Canonical write integrity

Յուրաքանչյուր write, update, replacement, move կամ delete ենթարկվում է `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`-ին՝ complete read → SHA preserve → write → beginning/end re-read → synchronization verification → GREEN։ Tool success-ը evidence չէ։

### Decision registry

- `DECISIONS.md` պահպանում է historical `D-001–D-021` registry-ն և մեծ full replacement չի ստանում։
- `DECISION_INDEX.md` active append-only registry է։
- Dedicated decisions-ը պահպանում են `D-022+` records-ը։

### Ընթացիկ canonical վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 Platforms Architecture v1 — merged և canonical։
- D-025 MenQ Design Platform Architecture v1 — `Approved — Implementing`, ոչ `Locked`։
- D-026 Canonical Session Read Law — Locked և machine-enforced։
- Working branch — `d-025-design-platform-architecture-v1`։
- Draft PR — `#3`, merge չի արվում մինչև architecture completeness, canonical synchronization, validator evidence, real consumer validation և Owner approval։
- Parts 1–11 baseline-ը պահպանված է `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`-ում։
- Part 12 validation/CI/conformance/quality-gates architecture-ը canonical է։
- Part 13 documentation portal/component catalog/design-tool integration architecture-ը canonical է։
- Part 14 governance/contribution/ownership/change-request lifecycle architecture-ը canonical է։
- Unowned canonical asset-ը RED governance defect է։ High-risk կամ breaking change-ի self-approval-ը արգելված է։
- Merge-ը առանձին authority action է, ոչ GREEN CI-ի ավտոմատ հետևանք։
- Armenian և English canonical languages են։ Additional languages-ը on-demand locale packs են։

### Հաջորդ աշխատանք

Ուղիղ շարունակել Design Platform Part 15-ից՝ Product Adoption, Maturity Model, and Two-Consumer Validation Plan, հետո specification index, implementation package plan, completeness audit, validator և Owner review։

---

## English

### Canonical source

The GitHub repository is the single canonical source of truth for MenQ Standard. Conversation is the workshop, not the canonical source. Do not ask the Owner again for the repository address or documented persistent rules.

### Required startup workflow

Every new AI session must, before beginning substantive work, enumerate and completely read every tracked `.md` file on the active branch or ref in accordance with [`foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`](foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md). A startup subset, handoff, summary, partial range, or previous-session memory is not complete-read evidence. When an active PR is involved, its metadata, changed files, diff, review threads, and checks must also be read.

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
- D-026 Canonical Session Read Law is Locked and machine-enforced.
- Working branch: `d-025-design-platform-architecture-v1`.
- Draft PR: `#3`; it remains unmerged until architecture completeness, canonical synchronization, validator evidence, real consumer validation, and Owner approval.
- Parts 1–11 are preserved in `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`.
- Part 12 validation, CI, conformance, and quality-gates architecture is canonical.
- Part 13 documentation portal, component catalog, and design-tool integration architecture is canonical.
- Part 14 governance, contribution, ownership, and change-request lifecycle architecture is canonical.
- An unowned canonical asset is a RED governance defect. Self-approval is prohibited for high-risk or breaking changes.
- Merge is a separate authority action, not an automatic consequence of green CI.
- Armenian and English are canonical languages. Additional languages are on-demand locale packs.

### Next work

Continue directly with Design Platform Part 15: Product Adoption, Maturity Model, and Two-Consumer Validation Plan, followed by the specification index, implementation package plan, completeness audit, validator work, and Owner review.

<!-- END: MENQ_STANDARD_PROJECT_CONTEXT -->