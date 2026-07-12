# Foundation — Project Context / Foundation — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Informative  
**Canonical scope / Canonical scope:** `foundation/`  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-12

## Հայերեն

### Նպատակ

`Foundation`-ը MenQ Standard-ի կայուն և պարտադիր հիմքն է։ Այն սահմանում է Philosophy-ն, Principles-ը, Terminology-ն, Governance-ը, Decision System-ը, Documentation-ը և AI Collaboration-ը։ Platforms-ը, Operating Standards-ը և Extensions-ը պետք է բխեն Foundation-ից և չհակասեն դրան։

### Canonical կառուցվածք

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

- `philosophy/README.md` — Locked
- `principles/README.md` — Locked
- `terminology/README.md` — Locked v1, Living Standard
- `governance/README.md` — Locked v1
- `decision-system/README.md` — Locked v1
- `documentation/README.md` — Locked v1
- `ai-collaboration/README.md` — Pending

### Authority

- Foundation-level final approval authority՝ MenQ Owner։
- AI-ն կարող է ուսումնասիրել, draft անել, challenge անել և documentation maintain անել, բայց չի կարող իրեն final approval տալ կամ Foundation truth-ը ինքնուրույն lock անել։
- Foundation-ի material փոփոխությունը պահանջում է MenQ Decision System-ի formal lifecycle և Owner approval։

### Startup workflow

Foundation-ի հետ աշխատանքից առաջ պարտադիր կարդացվում են՝

1. repository root `README.md`,
2. root `PROJECT_CONTEXT.md`,
3. `DECISIONS.md`,
4. `CHANGELOG.md`,
5. `foundation/README.md`,
6. այս `PROJECT_CONTEXT.md`-ը,
7. համապատասխան Foundation chapter-ը։

### Սահմաններ

- Foundation-ը չի պարունակում product-specific implementation details։
- Foundation term-ը կամ rule-ը product layer-ում չի վերասահմանվում։
- Նոր Foundation chapter կամ hierarchy change չի կատարվում առանց Owner approval-ի։
- Canonical history-ն չի ջնջվում կամ լուռ վերագրվում։
- Հայերեն և անգլերեն տարբերակները պահպանում են semantic equality։

### Հաջորդ քայլ

Կառուցել և հաստատել `AI Collaboration v1`, հետո կատարել Foundation-wide integrity և consistency review։

---

## English

### Purpose

`Foundation` is the stable and mandatory base of MenQ Standard. It defines Philosophy, Principles, Terminology, Governance, the Decision System, Documentation, and AI Collaboration. Platforms, Operating Standards, and Extensions must derive from Foundation and must not contradict it.

### Canonical structure

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

- `philosophy/README.md` — Locked
- `principles/README.md` — Locked
- `terminology/README.md` — Locked v1, Living Standard
- `governance/README.md` — Locked v1
- `decision-system/README.md` — Locked v1
- `documentation/README.md` — Locked v1
- `ai-collaboration/README.md` — Pending

### Authority

- Final approval authority for Foundation-level changes belongs to the MenQ Owner.
- AI may explore, draft, challenge, and maintain documentation, but it may not grant itself final approval or independently lock Foundation truth.
- A material Foundation change requires the formal MenQ Decision System lifecycle and Owner approval.

### Startup workflow

Before working on Foundation, read:

1. the repository root `README.md`,
2. the root `PROJECT_CONTEXT.md`,
3. `DECISIONS.md`,
4. `CHANGELOG.md`,
5. `foundation/README.md`,
6. this `PROJECT_CONTEXT.md`,
7. the relevant Foundation chapter.

### Boundaries

- Foundation does not contain product-specific implementation details.
- A Foundation term or rule is not redefined in a product layer.
- No new Foundation chapter or hierarchy change is made without Owner approval.
- Canonical history is not deleted or silently rewritten.
- Armenian and English versions maintain semantic equality.

### Next step

Build and approve `AI Collaboration v1`, then perform a Foundation-wide integrity and consistency review.
