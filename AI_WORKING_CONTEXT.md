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

### Remediation և validation վիճակ

- Safe append-only `DECISION_INDEX.md`-ը պահպանում է `D-001–D-023` traceability-ն։
- `DECISIONS.md`-ը historical `D-001–D-021` registry է և չի ենթարկվում մեծ full rewrite-ի։
- Documentation և AI Collaboration bilingual parity addenda-ները առկա են։
- Foundation normative metadata registry-ն, validator-ը և CI workflow-ը առկա են։
- `Foundation Integrity` workflow run `#9`-ը ավարտվել է `success` conclusion-ով։
- Validator output-ը՝ `FOUNDATION VALIDATION: GREEN` և `Validated 7 Foundation chapters and root controls.`
- Foundation v1 release gate-ը GREEN է։

### Հաջորդ քայլ

1. Ստեղծել և verify անել complete Foundation v1 repository ZIP snapshot-ը՝ release README, version/date, manifest և missing-file verification-ով։
2. ZIP-ը պահել որպես GitHub Release asset, ոչ main branch binary file։
3. Հետո բացել Platforms architecture formal Decision System proposal-ը և սպասել Owner approval-ին։

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

### Remediation and validation state

- The safe append-only `DECISION_INDEX.md` preserves `D-001–D-023` traceability.
- `DECISIONS.md` is the historical `D-001–D-021` registry and is not subject to a large full rewrite.
- Documentation and AI Collaboration bilingual parity addenda exist.
- The Foundation normative metadata registry, validator, and CI workflow exist.
- `Foundation Integrity` workflow run `#9` completed with a `success` conclusion.
- Validator output: `FOUNDATION VALIDATION: GREEN` and `Validated 7 Foundation chapters and root controls.`
- The Foundation v1 release gate is GREEN.

### Next step

1. Create and verify the complete Foundation v1 repository ZIP snapshot with a release README, version/date, manifest, and missing-file verification.
2. Store the ZIP as a GitHub Release asset, not as a binary file in the main branch.
3. Then open the formal Decision System proposal for Platforms architecture and await Owner approval.

<!-- END: MENQ_STANDARD_AI_WORKING_CONTEXT -->