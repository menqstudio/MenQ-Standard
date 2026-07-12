# MenQ Standard — Next Chat Handoff / Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-07-12  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Working branch:** `d-025-design-platform-architecture-v1`  
**Draft PR:** `https://github.com/menqstudio/MenQ-Standard/pull/3`

## Հայերեն

### Պարտադիր startup gate

Նոր session-ը մինչև substantive աշխատանք՝

1. active branch/ref-ում enumerate է անում բոլոր tracked `.md` files-ը,
2. յուրաքանչյուր file ամբողջությամբ կարդում է,
3. canonical manifest-ի path/size/SHA evidence-ը ստուգում է,
4. PR #3 metadata, changed files, diff, review threads և checks-ը կարդում է,
5. միայն unresolved failure-ի բացակայությունից հետո startup gate-ը GREEN է հայտարարում։

Պարտադիր օրենքը՝ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`։ Repository address-ը, Owner-ը, project purpose-ը, communication style-ը կամ continuation point-ը նորից չհարցնել։

### Ընթացիկ canonical վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 Platforms Architecture v1 — merged և canonical։
- D-025 MenQ Design Platform Architecture v1 — `Approved — Implementing`, ոչ `Locked`։
- D-026 Canonical Session Read Law — Locked, enforcement infrastructure GREEN։
- Canonical Markdown inventory — 57 tracked Markdown files strict path/size/SHA drift enforcement-ով։
- Draft PR #3 — open, Draft, unmerged։
- PR-ը չի merge կամ ready-for-review արվում առանց explicit Owner instruction-ի։

### Ավարտված architecture scope

- Parts 1–11՝ `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`։
- Part 12՝ `platforms/design/VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`։
- Part 12-ը սահմանում է յոթ sequential gates, GREEN/YELLOW/RED semantics, conformance profiles, exception contract և evidence contract։

### Canonical architecture rules

- Dependency layers՝ Reference → Semantic → Component → Pattern → Product Extension։
- Theme, state, density, platform, locale/script, accessibility և motion preference-ը token layers չեն։
- Controlled exceptions-ը normal layer չեն։
- Shared core-ը product-neutral է։
- Armenian և English canonical languages են՝ semantic equality-ով։
- Tool success-ը GREEN evidence չէ։

### Հստակ continuation point

Ուղիղ սկսել՝

**Part 13 — Documentation Portal, Component Catalog, and Design-Tool Integration Architecture**

Հետո հերթով՝

1. Governance, contribution, ownership և change-request lifecycle։
2. Product adoption, maturity model և two-consumer validation plan։
3. Canonical specification index և implementation package plan։
4. D-025 completeness audit, validator implementation և Draft PR #3 review։
5. Canonical synchronization, GREEN evidence և Owner review։

### Արգելված գործողություններ

- PR #3-ը չmerge անել և ready-for-review չդարձնել առանց Owner instruction-ի։
- D-025-ը `Locked` չանվանել։
- Product-specific identity, business logic կամ workflow shared core չմտցնել։
- `DECISIONS.md` historical registry-ն մեծ full rewrite չանել։
- Complete-read evidence չունենալով չասել, որ repository-ն ամբողջությամբ կարդացվել է։

---

## English

### Mandatory startup gate

Before substantive work, a new session must enumerate and completely read every tracked Markdown file on the active branch/ref, verify canonical manifest path/size/SHA evidence, and read PR #3 metadata, changed files, diff, review threads, and checks. It may declare GREEN only when no unresolved failure remains.

The mandatory law is `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`. Do not ask again for the repository address, Owner, project purpose, communication style, or continuation point.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- D-024 Platforms Architecture v1 is merged and canonical.
- D-025 MenQ Design Platform Architecture v1 is `Approved — Implementing`, not `Locked`.
- D-026 Canonical Session Read Law is Locked and its enforcement infrastructure is GREEN.
- The canonical Markdown inventory contains 57 tracked files with strict path/size/SHA drift enforcement.
- Draft PR #3 is open, Draft, and unmerged.
- The PR must not be merged or marked ready without explicit Owner instruction.

### Completed architecture scope

- Parts 1–11: `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`.
- Part 12: `platforms/design/VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`.
- Part 12 defines seven sequential gates, GREEN/YELLOW/RED semantics, conformance profiles, the exception contract, and the evidence contract.

### Exact continuation point

Start directly with:

**Part 13 — Documentation Portal, Component Catalog, and Design-Tool Integration Architecture**

Then continue with governance/contribution, product adoption and two-consumer validation, the canonical specification index and package plan, the D-025 completeness audit and validator implementation, final synchronization, GREEN evidence, and Owner review.

### Prohibited actions

Do not merge or mark PR #3 ready, call D-025 Locked, move product-specific identity or business logic into shared core, rewrite the historical `DECISIONS.md` registry, or claim a complete repository read without complete-read evidence.

<!-- END: MENQ_STANDARD_NEXT_CHAT_HANDOFF -->