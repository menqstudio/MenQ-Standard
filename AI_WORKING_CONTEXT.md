# MenQ Standard — AI Working Context

> Living continuity document for AI collaborators.  
> AI համագործակիցների կենդանի շարունակականության փաստաթուղթ։

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Working  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-12  
**Canonical repository:** `https://github.com/menqstudio/MenQ-Standard`

## Հայերեն

### Պարտադիր startup workflow

Յուրաքանչյուր նոր AI session մինչև որևէ substantive project աշխատանք սկսելը պարտավոր է՝

1. հաստատել canonical repository-ն և active branch/ref-ը,
2. enumerate անել repository-ի բոլոր tracked `.md` ֆայլերը,
3. յուրաքանչյուր `.md` file ամբողջությամբ կարդալ beginning-ից end-of-file կամ ending marker,
4. active PR-ի դեպքում կարդալ metadata-ն, changed files-ը, diff-ը, review threads-ը և checks-ը,
5. unresolved read failure կամ truncation-ի բացակայությունից հետո միայն հայտարարել startup gate-ը GREEN։

Պարտադիր օրենքը՝ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`։ Startup subset-ը, handoff-ը, summary-ն, partial range-ը կամ previous-session memory-ն complete-read evidence չեն։ Repository-ի հասցեն և արդեն documented persistent rules-ը Owner-ից կրկին չեն հարցվում։

### Human–AI սկզբունք

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն MenQ architect և engineering teammate է։ Final authority-ն և accountability-ն մարդունն են։ AI-ն չի կարող self-approve անել կամ canonical truth-ը ինքնուրույն lock անել։

### Ընթացիկ canonical վիճակ

- Foundation v1 — Locked և GREEN։
- `D-024 — Platforms Architecture v1` — merged և canonical։
- `D-025 — MenQ Design Platform Architecture v1` — `Approved — Implementing`, ոչ `Locked`։
- `D-026 — Canonical Session Read Law` — Locked, enforcement infrastructure GREEN։
- Canonical Markdown inventory — 57 tracked files, strict path/size/SHA drift enforcement։
- Working branch — `d-025-design-platform-architecture-v1`։
- Draft PR — `#3`, merge չի արվում մինչև completeness, synchronization, validation և Owner approval։

### Owner-approved Design Platform baseline

Parts 1–11-ը պահպանված են `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`-ում։ Part 12-ը պահպանված է `platforms/design/VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`-ում և սահմանում է յոթ sequential gates, verdict semantics, conformance profiles, exception contract և evidence contract։

Canonical token dependency layers-ը՝ Reference → Semantic → Component → Pattern → Product Extension։ Theme, state, density, platform, locale, accessibility և motion preference-ը token layers չեն։ Controlled exceptions-ը normal token layer չեն։

### Հաջորդ հստակ աշխատանք

1. Part 13 — Documentation portal, component catalog և design-tool integration architecture։
2. Governance, contribution, ownership և change-request lifecycle։
3. Product adoption, maturity model և two-consumer validation plan։
4. Canonical specification index և implementation package plan։
5. D-025 completeness audit, validator implementation և Draft PR #3 review։
6. Canonical synchronization, GREEN evidence և Owner review։

---

## English

### Required startup workflow

Before beginning any substantive project work, every new AI session must:

1. identify the canonical repository and active branch or ref;
2. enumerate every tracked `.md` file in the repository;
3. read each `.md` file completely from beginning to end-of-file or ending marker;
4. when an active PR is involved, read its metadata, changed files, diff, review threads, and checks;
5. declare the startup gate GREEN only after confirming there are no unresolved read failures or truncation.

The mandatory law is `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`. A startup subset, handoff, summary, partial range, or previous-session memory is not complete-read evidence. Do not ask the Owner again for the repository address or persistent rules already documented in the repository.

### Human–AI principle

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI may not self-approve or independently lock canonical truth.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- `D-024 — Platforms Architecture v1` is merged and canonical.
- `D-025 — MenQ Design Platform Architecture v1` is `Approved — Implementing`, not `Locked`.
- `D-026 — Canonical Session Read Law` is Locked and its enforcement infrastructure is GREEN.
- The canonical Markdown inventory contains 57 tracked files with strict path/size/SHA drift enforcement.
- Working branch: `d-025-design-platform-architecture-v1`.
- Draft PR: `#3`; it remains unmerged until completeness, synchronization, validation, and Owner approval are complete.

### Owner-approved Design Platform baseline

Parts 1–11 are preserved in `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`. Part 12 is preserved in `platforms/design/VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md` and defines seven sequential gates, verdict semantics, conformance profiles, the exception contract, and the evidence contract.

Canonical token dependency layers are Reference → Semantic → Component → Pattern → Product Extension. Theme, state, density, platform, locale, accessibility, and motion preference are not token layers. Controlled exceptions are not a normal token layer.

### Exact next work

1. Part 13 — Documentation portal, component catalog, and design-tool integration architecture.
2. Governance, contribution, ownership, and change-request lifecycle.
3. Product adoption, maturity model, and two-consumer validation plan.
4. Canonical specification index and implementation package plan.
5. D-025 completeness audit, validator implementation, and Draft PR #3 review.
6. Canonical synchronization, GREEN evidence, and Owner review.

<!-- END: MENQ_STANDARD_AI_WORKING_CONTEXT -->