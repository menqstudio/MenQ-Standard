# MenQ Design Platform — Next Chat Handoff / MenQ Design Platform — Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-07-12  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Working branch:** `d-025-design-platform-architecture-v1`  
**Draft PR:** `https://github.com/menqstudio/MenQ-Standard/pull/3`

## Հայերեն

### Պարտադիր մեկնարկ

Նոր chat-ում ոչ մի հայտնի բան կրկին չհարցնել։ Մինչև substantive աշխատանք՝ active branch/ref-ում enumerate և ամբողջությամբ կարդալ բոլոր tracked Markdown files-ը, ստուգել canonical manifest-ի path/size/SHA evidence-ը և կարդալ Draft PR #3 metadata, changed files, diff, review threads և checks-ը։

### Ընթացիկ վիճակ

- Foundation v1 — GREEN և Locked։
- D-024 Platforms Architecture v1 — merged և canonical։
- D-025 MenQ Design Platform Architecture v1 — `Approved — Implementing`, ոչ `Locked`։
- D-026 Canonical Session Read Law — Locked, enforcement infrastructure GREEN։
- Canonical Markdown inventory — 57 tracked files strict drift enforcement-ով։
- Draft PR #3 բաց է, Draft է և unmerged։
- Design Platform-ը product-neutral shared capability է։ Product-specific identity, business logic և domain workflows shared core չեն մտնում։

### Ավարտված architecture scope

- Parts 1–11՝ `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`։
- Part 12՝ `VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`։
- Part 12-ը սահմանում է յոթ sequential gates՝ Source Integrity, Build Integrity, Contract Conformance, Visual and Interaction Quality, Consumer Conformance, Package and Compatibility, Release Evidence։
- GREEN/YELLOW/RED verdict semantics-ը, conformance profiles-ը, exception contract-ը և evidence contract-ը canonical են։

### Կարևոր architecture rules

- Dependency layers՝ Reference → Semantic → Component → Pattern → Product Extension։
- Theme, state, density, platform, locale/script, accessibility և motion preference-ը resolution dimensions են, ոչ token layers։
- Controlled exceptions-ը governed bypass են, ոչ normal layer։
- Armenian և English canonical languages են՝ semantic equality-ով։
- Accessibility-ը release condition է։
- Generated outputs-ը source of truth չեն։
- Tool success-ը GREEN evidence չէ։

### Շարունակելու ճշգրիտ կետը

Հաջորդ chat-ը անմիջապես սկսում է՝

## Part 13 — Documentation Portal, Component Catalog, and Design-Tool Integration Architecture

Հետո հերթով՝

1. Governance, contribution, ownership և change-request lifecycle։
2. Product adoption, maturity model և two-consumer validation plan։
3. Canonical specification index և implementation package plan։
4. D-025 completeness audit, validator implementation և Draft PR #3 review։
5. Canonical synchronization, GREEN evidence և Owner review։

### Արգելված գործողություններ

- PR #3-ը չmerge անել և ready-for-review չդարձնել առանց Owner instruction-ի։
- D-025-ը `Locked` չանվանել։
- Product-specific identity կամ business logic shared core չմտցնել։
- Controlled exception-ը normal layer չդարձնել։
- Complete-read evidence չունենալով չասել, որ repository-ն ամբողջությամբ կարդացվել է։

---

## English

### Mandatory startup

Do not ask again for known context. Before substantive work, enumerate and completely read every tracked Markdown file on the active branch/ref, verify canonical manifest path/size/SHA evidence, and read Draft PR #3 metadata, changed files, diff, review threads, and checks.

### Current state

- Foundation v1 is GREEN and Locked.
- D-024 Platforms Architecture v1 is merged and canonical.
- D-025 is `Approved — Implementing`, not `Locked`.
- D-026 Canonical Session Read Law is Locked and its enforcement infrastructure is GREEN.
- The canonical Markdown inventory contains 57 tracked files with strict drift enforcement.
- Draft PR #3 is open, Draft, and unmerged.
- The Platform is product-neutral. Product identity, business logic, and domain workflows do not enter shared core.

### Completed architecture scope

- Parts 1–11: `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`.
- Part 12: `VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`.
- Part 12 defines seven sequential gates: Source Integrity, Build Integrity, Contract Conformance, Visual and Interaction Quality, Consumer Conformance, Package and Compatibility, and Release Evidence.
- GREEN/YELLOW/RED verdict semantics, conformance profiles, the exception contract, and the evidence contract are canonical.

### Exact continuation point

Start immediately with:

**Part 13 — Documentation Portal, Component Catalog, and Design-Tool Integration Architecture**

Then continue with governance/contribution, product adoption and two-consumer validation, the canonical specification index and implementation package plan, the D-025 completeness audit and validator implementation, final synchronization, GREEN evidence, and Owner review.

### Prohibited actions

Do not merge or mark PR #3 ready, call D-025 Locked, move product identity or business logic into shared core, treat controlled exceptions as a normal layer, or claim a complete repository read without complete-read evidence.

<!-- END: MENQ_DESIGN_PLATFORM_NEXT_CHAT_HANDOFF -->