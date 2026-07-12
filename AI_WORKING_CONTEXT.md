# MenQ Standard — AI Working Context

> Living continuity document for AI collaborators.  
> AI համագործակիցների կենդանի շարունակականության փաստաթուղթ։

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Working  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-12  
**Canonical repository:** `https://github.com/menqstudio/MenQ-Standard`

## Հայերեն

### Պարտադիր startup workflow

Նոր AI collaborator-ը աշխատանքից առաջ կարդում է՝

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `COLLABORATION_STYLE.md`
4. `DECISION_INDEX.md`
5. `DECISIONS.md`
6. `CHANGELOG.md`
7. `ROADMAP.md`
8. `foundation/README.md`
9. `foundation/PROJECT_CONTEXT.md`
10. `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`
11. համապատասխան chapter-ը
12. `NEXT_CHAT_HANDOFF.md`, եթե այն առկա է և ընթացիկ է

Repository-ի հասցեն և արդեն documented persistent rules-ը Owner-ից կրկին չեն հարցվում։

### Human–AI սկզբունք

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն աշխատում է որպես MenQ architect և engineering teammate։ Final authority-ն և accountability-ն մարդունն են։ AI-ն չի կարող self-approve անել կամ canonical truth-ը ինքնուրույն lock անել։

### Ընթացիկ canonical վիճակ

- Philosophy — Locked v1
- Principles — Locked v1 (`D-017`)
- Terminology — Locked v1, Living Standard (`D-018`)
- Governance — Locked v1 (`D-019`)
- Decision System — Locked v1 (`D-020`)
- Documentation Standard — Locked v1 (`D-021`)
- Canonical Write Integrity Law — Locked (`D-022`)
- AI Collaboration — Locked v1 (`D-023`)

Բոլոր յոթ Foundation chapter-ները ունեն `README.md` և `PROJECT_CONTEXT.md`։

### Remediation վիճակ

- Ստեղծվել է safe append-only `DECISION_INDEX.md`՝ `D-001–D-023` traceability-ի համար։
- `DECISIONS.md` պահպանվել է որպես historical `D-001–D-021` registry և այլևս չի պահանջում վտանգավոր full rewrite։
- Ստեղծվել են Documentation և AI Collaboration bilingual parity addenda-ները։
- Ստեղծվել է `foundation/FOUNDATION_NORMATIVE_METADATA_REGISTRY.md`։
- Ստեղծվել է `scripts/validate_foundation.py` validator-ը։
- Ստեղծվել է `.github/workflows/foundation-integrity.yml` CI workflow-ը։
- Ստեղծվել է `COLLABORATION_STYLE.md`, որը սահմանում է Գևորգի հետ բոլոր AI collaborators-ի միատեսակ communication mood-ը։

### Integrity status

Manual repository verification-ը հաստատել է required files-ի գոյությունը և critical ending markers-ը այն files-ում, որոնք այս transaction-ով ստեղծվել կամ թարմացվել են։ GitHub Actions CI run/status-ը դեռ evidence չի վերադարձրել և պետք է ստուգվի հաջորդ session-ում։ Մինչ CI GREEN evidence-ը Foundation release ZIP-ը չի ներկայացվում որպես validated release artifact։

### Հաջորդ քայլ

1. Կարդալ `NEXT_CHAT_HANDOFF.md`։
2. Ստուգել Foundation Integrity workflow run-ը կամ local clone-ում գործարկել `python scripts/validate_foundation.py`։
3. Եթե validator-ը RED է՝ ուղղել միայն reported defects-ը և կրկին verify անել։
4. Եթե GREEN է՝ ստեղծել Foundation v1 complete repository ZIP snapshot և հետո բացել Platforms architecture formal decision-ը։

---

## English

### Required startup workflow

Before work, a new AI collaborator reads:

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `COLLABORATION_STYLE.md`
4. `DECISION_INDEX.md`
5. `DECISIONS.md`
6. `CHANGELOG.md`
7. `ROADMAP.md`
8. `foundation/README.md`
9. `foundation/PROJECT_CONTEXT.md`
10. `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`
11. the relevant chapter
12. `NEXT_CHAT_HANDOFF.md` when present and current

Do not ask the Owner again for the repository address or persistent rules already documented in the repository.

### Human–AI principle

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI may not self-approve or independently lock canonical truth.

### Current canonical state

- Philosophy — Locked v1
- Principles — Locked v1 (`D-017`)
- Terminology — Locked v1, Living Standard (`D-018`)
- Governance — Locked v1 (`D-019`)
- Decision System — Locked v1 (`D-020`)
- Documentation Standard — Locked v1 (`D-021`)
- Canonical Write Integrity Law — Locked (`D-022`)
- AI Collaboration — Locked v1 (`D-023`)

All seven Foundation chapters contain `README.md` and `PROJECT_CONTEXT.md`.

### Remediation state

- A safe append-only `DECISION_INDEX.md` provides traceability for `D-001–D-023`.
- `DECISIONS.md` is preserved as the historical `D-001–D-021` registry and no longer requires unsafe full rewrites.
- Documentation and AI Collaboration bilingual parity addenda exist.
- `foundation/FOUNDATION_NORMATIVE_METADATA_REGISTRY.md` exists.
- `scripts/validate_foundation.py` exists.
- `.github/workflows/foundation-integrity.yml` exists.
- `COLLABORATION_STYLE.md` defines a consistent communication mood for all AI collaborators working with Gevorg.

### Integrity status

Manual repository verification confirms the required files and critical ending markers for files created or updated in this transaction. GitHub Actions has not yet returned CI run/status evidence and must be checked in the next session. Until CI GREEN evidence exists, the Foundation release ZIP must not be represented as a validated release artifact.

### Next step

1. Read `NEXT_CHAT_HANDOFF.md`.
2. Check the Foundation Integrity workflow run or run `python scripts/validate_foundation.py` in a local clone.
3. If the validator is RED, fix only the reported defects and verify again.
4. If GREEN, create the complete Foundation v1 repository ZIP snapshot and then open the formal Platforms architecture decision.

<!-- END: MENQ_STANDARD_AI_WORKING_CONTEXT -->