# MenQ Ecosystem Architecture

**Owner / Պատասխանատու:** MenQ Owner  
**Canonical path / Canonical ուղի:** `ECOSYSTEM_ARCHITECTURE.md`  
**Related decisions / Կապված որոշումներ:** `D-004`, `D-005`, `D-006`, `D-007`, `D-008`, `D-009`, `D-010`, `D-011` ([`DECISIONS.md`](DECISIONS.md))  
**Last synchronized / Վերջին համաժամեցում:** 2026-10-09

## Հայերեն

### Հիմնական բաժանում

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

## MenQ Studio

MenQ Studio-ն ընկերությունն է։ Այն ստեղծում և առաջարկում է գործնական թվային ու AI լուծումներ մարդկանց և բիզնեսների համար։

### Հիմնական ուղղություններ

- AI լուծումներ
- վեբ կայքեր
- ներքին օգտագործման ծրագրեր
- workflow automation
- SaaS համակարգեր
- պահեստի կառավարման համակարգեր
- ավտոմատացված AI agents

### Company Mission — Locked

> MenQ Studio-ի առաքելությունն է ստեղծել գործնական թվային և AI լուծումներ, որոնք օգնում են մարդկանց ու բիզնեսներին ավտոմատացնել աշխատանքը, կառուցել ավելի արդյունավետ համակարգեր և զարգանալ տեխնոլոգիայի միջոցով։

### Company Vision — Open

MenQ Studio-ի company vision-ը դեռ հաստատված չէ։

## MenQ Standard

MenQ Standard-ը MenQ ecosystem-ի operating standard-ն է։ Այն սահմանում է՝ ինչպես ենք մտածում, որոշում, նախագծում, կառուցում, ստուգում, փաստաթղթավորում և պահպանում համակարգերը։

### Core hierarchy

```text
MenQ Standard
├── Foundation
├── Platforms
├── Operating Standards
└── Extensions
```

### Foundation

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

### Philosophy

```text
Philosophy
├── Vision
├── Mission
├── Core Beliefs
├── Human–AI Philosophy
├── Design Philosophy
├── Engineering Philosophy
└── Product Philosophy
```

### Standard Vision — Locked

> MenQ Standard-ի տեսլականն է դառնալ Human–AI collaboration-ի reference standard։

### Standard Mission — Locked (D-011)

> MenQ Standard-ի առաքելությունն է ստեղծել կիրառելի և զարգացող operating standard, որը մարդկանց ու AI համակարգերին օգնում է միասին մտածել, որոշել, կառուցել և պահպանել որակյալ համակարգեր։

Այն առանձին է MenQ Studio-ի company mission-ից։ Աղբյուր՝ [`DECISIONS.md`](DECISIONS.md) `D-011`։

## Ownership rule

- MenQ Studio-ն ունի company vision և company mission։
- MenQ Standard-ն ունի standard vision և standard mission։
- MenQ Studio-ի Services և Products-ը չեն ապրում MenQ Standard-ի hierarchy-ի մեջ։
- MenQ Standard-ը սահմանում է, թե MenQ ecosystem-ը ինչպես է աշխատում։

## Architecture workflow

```text
Idea
↓
Architecture
↓
Review
↓
Approve
↓
Lock
↓
Documentation
```

Chat-ը workshop-ն է։ GitHub-ը canonical source-ն է։ GitHub գնում է միայն հաստատված architecture-ը և որոշումները։

Այս workflow-ը `D-009`-ի տեքստն է։ Քայլերի հերթականությունը և վերջին նախադասությունը մասամբ փոխարինված են `D-020`-ով․ տես [`DECISIONS.md`](DECISIONS.md)-ում `D-009`-ի տակի 2026-10-09-ի նշումը, որը Owner-ի հաստատում չունի, մինչև Owner-ը merge չանի այն պարունակող pull request-ը։

---

## English

### Primary separation

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

## MenQ Studio

MenQ Studio is the company. It creates and offers practical digital and AI solutions for people and businesses.

### Primary directions

- AI solutions
- websites
- internal-use software
- workflow automation
- SaaS systems
- warehouse management systems
- automated AI agents

### Company Mission — Locked

> MenQ Studio's mission is to create practical digital and AI solutions that help people and businesses automate work, build more efficient systems, and grow through technology.

### Company Vision — Open

MenQ Studio's company vision is not yet approved.

## MenQ Standard

MenQ Standard is the operating standard of the MenQ ecosystem. It defines how we think, decide, design, build, validate, document, and preserve systems.

### Core hierarchy

```text
MenQ Standard
├── Foundation
├── Platforms
├── Operating Standards
└── Extensions
```

### Foundation

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

### Philosophy

```text
Philosophy
├── Vision
├── Mission
├── Core Beliefs
├── Human–AI Philosophy
├── Design Philosophy
├── Engineering Philosophy
└── Product Philosophy
```

### Standard Vision — Locked

> MenQ Standard's vision is to become the reference standard for Human–AI collaboration.

### Standard Mission — Locked (D-011)

> MenQ Standard's mission is to create a practical and evolving operating standard that helps people and AI systems think, decide, build, and preserve quality systems together.

It is separate from the company mission of MenQ Studio. Source: [`DECISIONS.md`](DECISIONS.md) `D-011`.

## Ownership rule

- MenQ Studio has a company vision and company mission.
- MenQ Standard has a standard vision and standard mission.
- MenQ Studio Services and Products do not live inside the MenQ Standard hierarchy.
- MenQ Standard defines how the MenQ ecosystem operates.

## Architecture workflow

```text
Idea
↓
Architecture
↓
Review
↓
Approve
↓
Lock
↓
Documentation
```

Chat is the workshop. GitHub is the canonical source. Only approved architecture and decisions enter GitHub.

This workflow is the text of `D-009`. The order of the steps and the last sentence are superseded in part by `D-020`; see the note of 2026-10-09 under `D-009` in [`DECISIONS.md`](DECISIONS.md), which has no Owner approval until the Owner merges the pull request that contains it.

<!-- END: MENQ_ECOSYSTEM_ARCHITECTURE -->
