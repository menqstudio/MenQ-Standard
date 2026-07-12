# MenQ Standard — AI Working Context

> Living continuity document for AI collaborators.  
> AI համագործակիցների կենդանի շարունակականության փաստաթուղթ։

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Working  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-12  
**Canonical repository:** `https://github.com/menqstudio/MenQ-Standard`

---

## Հայերեն

### Նպատակ

Այս ֆայլը պահպանում է MenQ Standard-ի ընթացիկ աշխատանքային կոնտեքստը։ Այն չի փոխարինում canonical chapter-ներին և չի ստեղծում նոր truth։ Այն միայն ամփոփում է repository-ում արդեն հաստատված փաստերը և հաջորդ քայլը։

### Պարտադիր startup workflow

MenQ Standard-ի հետ աշխատանքից առաջ կարդալ՝

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `DECISIONS.md`
4. `CHANGELOG.md`
5. `ROADMAP.md`
6. `foundation/README.md`
7. `foundation/PROJECT_CONTEXT.md`
8. համապատասխան թեմատիկ chapter-ը

Repository-ի հասցեն կամ արդեն փաստաթղթավորված մշտական կանոնները Owner-ից կրկին չեն հարցվում։

### Human–AI սկզբունք

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն աշխատում է որպես MenQ architect և engineering teammate։ Վերջնական authority-ն և accountability-ն մարդունն են։ AI-ն չի կարող իրեն approval տալ կամ ինքնուրույն canonical truth lock անել։

### MenQ ecosystem

```text
MenQ Ecosystem
├── MenQ Studio
│   ├── Company
│   ├── Services
│   └── Products
│
└── MenQ Standard
    ├── Foundation
    ├── Platforms
    ├── Operating Standards
    └── Extensions
```

MenQ Studio-ն ընկերությունն է։ MenQ Standard-ը ecosystem-ի operating standard-ն է։ Services-ը և Products-ը պատկանում են MenQ Studio-ին։

### Foundation-ի locked կառուցվածք

```text
Foundation
├── Philosophy
├── Principles
├── Terminology
├── Governance
├── Decision System
├── Documentation
└── AI Collaboration
```

### Ընթացիկ canonical վիճակ

- Philosophy — Locked
- Principles — Locked (`D-017`)
- Terminology — Locked v1, Living Standard (`D-018`)
- Governance — Locked v1 (`D-019`)
- Decision System — Locked v1 (`D-020`)
- Documentation Standard — Locked v1 (`D-021`)
- AI Collaboration — Pending; հաջորդ կառուցվող chapter-ը

### Locked operational rules

- GitHub repository-ն single canonical source of truth-ն է։
- Chat-ը workshop է, ոչ canonical source։
- Approved ecosystem-level գաղափարները պարտադիր փաստաթղթավորվում են։
- Foundation-level final approval authority-ն Owner-ինն է։
- AI-ն չի կարող self-approve անել։
- Authority-ն explicit, scoped, least-necessary, traceable և revocable է։
- Formal decisions-ը օգտագործում են `C0–C4` classes և `R0–R4` risk levels։
- Decision gates-ը գնահատվում են `GREEN`, `YELLOW`, `RED` արդյունքներով։
- Locked decision-ի material change-ը history չի rewrite անում։
- Հայերեն և անգլերեն տարբերակները հավասար authoritative են։
- Canonical write-ից հետո պարտադիր է re-read և integrity verification։
- Multi-file deliverable-ը տրվում է ամբողջական package-ով և հնարավորության դեպքում ZIP-ով։ ZIP-ը snapshot է, ոչ canonical source։

### Documentation file roles

- `README.md` — human entry point
- `PROJECT_CONTEXT.md` — stable AI context
- `AI_WORKING_CONTEXT.md` — living continuity summary
- `DECISIONS.md` — locked decision registry
- `CHANGELOG.md` — historical change record
- `ROADMAP.md` — future direction, ոչ locked commitment

### Ընթացիկ աշխատանք

Documentation transaction-ը ավարտված և synchronized է։ Ստեղծված կամ թարմացված են՝

- `foundation/documentation/README.md`
- `DECISIONS.md`՝ `D-021`
- `CHANGELOG.md`
- `foundation/README.md`
- `ROADMAP.md`
- `foundation/PROJECT_CONTEXT.md`
- `README.md`
- այս `AI_WORKING_CONTEXT.md`

### Հաջորդ քայլ

Կառուցել `Foundation → AI Collaboration v1` chapter-ը։ Դրանից հետո կատարել Foundation-wide consistency, bilingual parity, link և integrity audit։

### Continuity rule

Եթե այս ֆայլը stale կամ կիսատ է, այն չի օգտագործվում որպես truth։ Նախ կարդացվում են canonical chapter-ները և decisions-ը, ապա summary-ն վերականգնվում է միայն հաստատված repository facts-ից։

---

## English

### Purpose

This file preserves the current working context of MenQ Standard. It does not replace canonical chapters and does not create new truth. It only summarizes facts already approved in the repository and the next step.

### Required startup workflow

Before working on MenQ Standard, read:

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `DECISIONS.md`
4. `CHANGELOG.md`
5. `ROADMAP.md`
6. `foundation/README.md`
7. `foundation/PROJECT_CONTEXT.md`
8. the relevant topic-specific chapter

Do not ask the Owner again for the repository address or persistent rules already documented in the repository.

### Human–AI principle

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI may not approve itself or independently lock canonical truth.

### MenQ ecosystem

```text
MenQ Ecosystem
├── MenQ Studio
│   ├── Company
│   ├── Services
│   └── Products
│
└── MenQ Standard
    ├── Foundation
    ├── Platforms
    ├── Operating Standards
    └── Extensions
```

MenQ Studio is the company. MenQ Standard is the operating standard of the ecosystem. Services and Products belong to MenQ Studio.

### Locked Foundation structure

```text
Foundation
├── Philosophy
├── Principles
├── Terminology
├── Governance
├── Decision System
├── Documentation
└── AI Collaboration
```

### Current canonical state

- Philosophy — Locked
- Principles — Locked (`D-017`)
- Terminology — Locked v1, Living Standard (`D-018`)
- Governance — Locked v1 (`D-019`)
- Decision System — Locked v1 (`D-020`)
- Documentation Standard — Locked v1 (`D-021`)
- AI Collaboration — Pending; the next chapter to build

### Locked operational rules

- The GitHub repository is the single canonical source of truth.
- Conversation is the workshop, not the canonical source.
- Approved ecosystem-level ideas must be documented.
- Final Foundation-level approval authority belongs to the Owner.
- AI cannot self-approve.
- Authority is explicit, scoped, least-necessary, traceable, and revocable.
- Formal decisions use `C0–C4` classes and `R0–R4` risk levels.
- Decision gates use `GREEN`, `YELLOW`, and `RED` outcomes.
- Material changes to locked decisions do not rewrite history.
- Armenian and English versions are equally authoritative.
- Every canonical write requires re-reading and integrity verification.
- Multi-file deliverables are provided as complete packages and preferably as ZIP files. A ZIP is a snapshot, not the canonical source.

### Documentation file roles

- `README.md` — human entry point
- `PROJECT_CONTEXT.md` — stable AI context
- `AI_WORKING_CONTEXT.md` — living continuity summary
- `DECISIONS.md` — locked decision registry
- `CHANGELOG.md` — historical change record
- `ROADMAP.md` — future direction, not a locked commitment

### Current work

The documentation transaction is complete and synchronized. The following were created or updated:

- `foundation/documentation/README.md`
- `DECISIONS.md` with `D-021`
- `CHANGELOG.md`
- `foundation/README.md`
- `ROADMAP.md`
- `foundation/PROJECT_CONTEXT.md`
- `README.md`
- this `AI_WORKING_CONTEXT.md`

### Next step

Build the `Foundation → AI Collaboration v1` chapter. Then perform a Foundation-wide consistency, bilingual parity, link, and integrity audit.

### Continuity rule

If this file is stale or truncated, do not use it as truth. Read the canonical chapters and decisions first, then restore the summary only from approved repository facts.
