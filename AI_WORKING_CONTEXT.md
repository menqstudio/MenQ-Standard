# MenQ Standard — AI Working Context

> Living continuity document for AI collaborators.  
> AI համագործակիցների կենդանի շարունակականության փաստաթուղթ։

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Working  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-12  
**Canonical repository:** `https://github.com/menqstudio/MenQ-Standard`

---

## Հայերեն

### 1. Նպատակ

Այս ֆայլը պահպանում է MenQ Standard-ի ընթացիկ աշխատանքային կոնտեքստը, որպեսզի նոր chat-ը չսկսվի զրոյից։ Այն չի փոխարինում canonical chapter-ներին և չի ստեղծում նոր truth։ Այն միայն ամփոփում է repository-ում արդեն պահպանված փաստերը, բաց հարցերը և հաջորդ քայլը։

### 2. Պարտադիր startup workflow

MenQ Standard-ի հետ աշխատանքից առաջ պարտադիր կարդալ՝

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `DECISIONS.md`
4. `CHANGELOG.md`
5. `ROADMAP.md`
6. `foundation/README.md`
7. `foundation/PROJECT_CONTEXT.md`
8. համապատասխան թեմատիկ chapter-ը

Repository-ի հասցեն կամ արդեն փաստաթղթավորված մշտական կանոնները Owner-ից կրկին չեն հարցվում։

### 3. Մարդ–AI սկզբունք

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն աշխատում է որպես MenQ architect և engineering teammate։ Վերջնական authority-ն և accountability-ն մարդունն են։ AI-ն չի կարող իրեն approval տալ կամ ինքնուրույն canonical truth lock անել։

### 4. MenQ ecosystem-ի բաժանում

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

### 5. Foundation-ի locked կառուցվածք

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

### 6. Ընթացիկ canonical վիճակ

- Philosophy — Locked
- Principles — Locked (`D-017`)
- Terminology — Locked v1, Living Standard (`D-018`)
- Governance — Locked v1 (`D-019`)
- Decision System — Locked v1 (`D-020`)
- Documentation Standard — Locked v1 (`D-021` pending registry synchronization during the current documentation transaction)
- AI Collaboration — Pending; հաջորդ կառուցվող chapter-ը

### 7. Locked Philosophy backbone

- MenQ Standard vision՝ դառնալ Human–AI collaboration-ի reference standard։
- MenQ Standard mission՝ ստեղծել կիրառելի և զարգացող operating standard, որը մարդկանց և AI համակարգերին օգնում է միասին մտածել, որոշել, կառուցել և պահպանել որակյալ համակարգեր։
- Core Beliefs, Human–AI Philosophy, Design Philosophy, Engineering Philosophy և Product Philosophy locked են։

### 8. Locked operational rules

- GitHub repository-ն single canonical source of truth-ն է։
- Chat-ը workshop է, ոչ canonical source։
- Approved ecosystem-level գաղափարները պարտադիր փաստաթղթավորվում են։
- Foundation-level final approval authority-ն Owner-ինն է։
- AI-ն չի կարող self-approve անել։
- Authority-ն explicit, scoped, least-necessary, traceable և revocable է։
- Formal decisions-ը օգտագործում են `C0–C4` classes և `R0–R4` risk levels։
- Decision gates-ը գնահատվում են `GREEN`, `YELLOW`, `RED` արդյունքներով։
- Locked decision-ի material change-ը history չի rewrite անում. ստեղծվում է նոր decision և հինը supersede կամ retire է արվում։
- Հայերեն և անգլերեն տարբերակները հավասար authoritative են։
- Canonical write-ից հետո պարտադիր է re-read և integrity verification։ Write success-ը ինքնուրույն evidence չէ։
- Multi-file deliverable-ը տրվում է ամբողջական package-ով և հնարավորության դեպքում ZIP-ով։ ZIP-ը snapshot է, ոչ canonical source։

### 9. Documentation file roles

- `README.md` — human entry point
- `PROJECT_CONTEXT.md` — stable AI context
- `AI_WORKING_CONTEXT.md` — living continuity summary
- `DECISIONS.md` — locked decision registry
- `CHANGELOG.md` — historical change record
- `ROADMAP.md` — future direction, ոչ locked commitment

### 10. Ընթացիկ աշխատանք

Documentation Standard v1-ը Owner-ի կողմից approved է և canonical chapter-ը ստեղծված է։ Ընթացիկ documentation transaction-ը պետք է ամբողջությամբ synchronize անի՝

1. `foundation/documentation/README.md`
2. `DECISIONS.md`՝ `D-021`
3. `CHANGELOG.md`
4. `foundation/README.md`
5. `ROADMAP.md`
6. `foundation/PROJECT_CONTEXT.md`
7. այս `AI_WORKING_CONTEXT.md`

### 11. Հաջորդ քայլ

Documentation transaction-ի integrity verification-ից հետո կառուցել `Foundation → AI Collaboration v1` chapter-ը։ Դրանից հետո կատարել Foundation-wide consistency, bilingual parity, link և integrity audit։

### 12. Continuity rule

Այս ֆայլը stale կամ կիսատ նկատելու դեպքում այն չի օգտագործվում որպես truth։ Նախ կարդացվում են canonical chapter-ները և decisions-ը, ապա այս summary-ն վերականգնվում է միայն հաստատված repository facts-ից։

---

## English

### 1. Purpose

This file preserves the current working context of MenQ Standard so that a new conversation does not begin from zero. It does not replace canonical chapters and does not create new truth. It only summarizes facts already preserved in the repository, open matters, and the next step.

### 2. Required startup workflow

Before working on MenQ Standard, read:

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `DECISIONS.md`
4. `CHANGELOG.md`
5. `ROADMAP.md`
6. `foundation/README.md`
7. `foundation/PROJECT_CONTEXT.md`
8. the relevant topic-specific chapter

Do not ask the Owner again for the repository address or for persistent rules already documented in the repository.

### 3. Human–AI principle

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI may not approve itself or independently lock canonical truth.

### 4. MenQ ecosystem separation

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

### 5. Locked Foundation structure

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

### 6. Current canonical state

- Philosophy — Locked
- Principles — Locked (`D-017`)
- Terminology — Locked v1, Living Standard (`D-018`)
- Governance — Locked v1 (`D-019`)
- Decision System — Locked v1 (`D-020`)
- Documentation Standard — Locked v1 (`D-021` pending registry synchronization during the current documentation transaction)
- AI Collaboration — Pending; the next chapter to build

### 7. Locked Philosophy backbone

- MenQ Standard vision: become the reference standard for Human–AI collaboration.
- MenQ Standard mission: create a practical and evolving operating standard that helps humans and AI systems think, decide, build, and preserve quality systems together.
- Core Beliefs, Human–AI Philosophy, Design Philosophy, Engineering Philosophy, and Product Philosophy are locked.

### 8. Locked operational rules

- The GitHub repository is the single canonical source of truth.
- Conversation is the workshop, not the canonical source.
- Approved ecosystem-level ideas must be documented.
- Final approval authority for Foundation-level changes belongs to the Owner.
- AI cannot self-approve.
- Authority is explicit, scoped, least-necessary, traceable, and revocable.
- Formal decisions use `C0–C4` classes and `R0–R4` risk levels.
- Decision gates use `GREEN`, `YELLOW`, and `RED` outcomes.
- A material change to a locked decision does not rewrite history; a new decision is created and the old one is superseded or retired.
- Armenian and English versions are equally authoritative.
- Every canonical write requires re-reading and integrity verification. A successful write response is not evidence by itself.
- A multi-file deliverable is provided as a complete package and preferably as a ZIP. A ZIP is a snapshot, not the canonical source.

### 9. Documentation file roles

- `README.md` — human entry point
- `PROJECT_CONTEXT.md` — stable AI context
- `AI_WORKING_CONTEXT.md` — living continuity summary
- `DECISIONS.md` — locked decision registry
- `CHANGELOG.md` — historical change record
- `ROADMAP.md` — future direction, not a locked commitment

### 10. Current work

Documentation Standard v1 has been approved by the Owner and its canonical chapter has been created. The current documentation transaction must fully synchronize:

1. `foundation/documentation/README.md`
2. `DECISIONS.md` with `D-021`
3. `CHANGELOG.md`
4. `foundation/README.md`
5. `ROADMAP.md`
6. `foundation/PROJECT_CONTEXT.md`
7. this `AI_WORKING_CONTEXT.md`

### 11. Next step

After integrity verification of the documentation transaction, build the `Foundation → AI Collaboration v1` chapter. Then perform a Foundation-wide consistency, bilingual parity, link, and integrity audit.

### 12. Continuity rule

If this file is found stale or truncated, it must not be used as truth. Read the canonical chapters and decisions first, then restore this summary only from approved repository facts.
