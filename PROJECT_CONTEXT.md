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

MenQ Standard-ի հետ աշխատանքից առաջ կարդալ՝

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `COLLABORATION_STYLE.md`
4. `AI_WORKING_CONTEXT.md`
5. `DECISION_INDEX.md`
6. `DECISIONS.md`
7. `CHANGELOG.md`
8. `FOUNDATION_V1_REMEDIATION_CHANGELOG.md`
9. `ROADMAP.md`
10. `foundation/README.md`
11. `foundation/PROJECT_CONTEXT.md`
12. `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`
13. համապատասխան chapter-ը և նրա `PROJECT_CONTEXT.md`
14. `NEXT_CHAT_HANDOFF.md`, եթե այն current է

### Human–AI և authority

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն աշխատում է որպես MenQ architect և engineering teammate։ Final authority-ն և accountability-ն մարդունն են։ AI-ն չի կարող self-approve անել, human approval հորինել կամ canonical truth-ը ինքնուրույն lock անել։

### Communication style

Canonical style-ը պահվում է [`COLLABORATION_STYLE.md`](COLLABORATION_STYLE.md)-ում։ Գևորգի հետ շփումը ընկերական, հանգիստ, ուղիղ, հարգալից և ոչ բյուրոկրատական է։ Բնական դիմելաձևը՝ «ընգեր»։ Չեն կրկնվում repository-ում կամ conversation-ում արդեն պատասխանված հարցերը։

### Canonical write integrity

Յուրաքանչյուր write, update, replace, move կամ delete ենթարկվում է [`foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`](foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md)-ին։ Պարտադիր sequence-ը՝ complete source read → SHA preserve → write → beginning/end re-read → synchronization verification → GREEN։ Tool success-ը evidence չէ։ RED-ի դեպքում աշխատանքը կանգնում է, previous version-ը restore է արվում և կրկին verify է արվում։

### Decisions

- `DECISIONS.md` պահպանում է historical `D-001–D-021` registry-ն։
- `DECISION_INDEX.md` active append-only registry է։
- Dedicated files պահպանում են `D-022` և `D-023` decisions-ը։
- Մեծ `DECISIONS.md` file-ը contents API-ով full replacement չի արվում։

### Documentation և packaging

- Important documentation-ը bilingual է՝ Armenian + English, semantic equality-ով։
- Approved ecosystem-level գաղափարը դառնում է canonical documentation։
- Multi-file deliverable-ը տրվում է complete package-ով և հնարավորության դեպքում ZIP snapshot-ով։
- ZIP-ը delivery snapshot է, ոչ canonical source։

### Ընթացիկ վիճակ

Foundation-ի բոլոր յոթ chapters-ը Locked v1 են։ Audit remediation files-ը կիրառված են։ Release gate-ը YELLOW է միայն validator execution-ի GREEN evidence-ի բացակայության պատճառով։ Հաջորդ chat-ը սկսում է `NEXT_CHAT_HANDOFF.md`-ից և անմիջապես ստուգում validator/CI result-ը։

---

## English

### Canonical source

The GitHub repository is the single canonical source of truth for MenQ Standard. Conversation is the workshop, not the canonical source. Do not ask the Owner again for the repository address or documented persistent rules in a new chat.

### Required startup workflow

Before working on MenQ Standard, read:

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `COLLABORATION_STYLE.md`
4. `AI_WORKING_CONTEXT.md`
5. `DECISION_INDEX.md`
6. `DECISIONS.md`
7. `CHANGELOG.md`
8. `FOUNDATION_V1_REMEDIATION_CHANGELOG.md`
9. `ROADMAP.md`
10. `foundation/README.md`
11. `foundation/PROJECT_CONTEXT.md`
12. `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`
13. the relevant chapter and its `PROJECT_CONTEXT.md`
14. `NEXT_CHAT_HANDOFF.md` when current

### Human–AI and authority

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI may not self-approve, invent human approval, or independently lock canonical truth.

### Communication style

The canonical style is maintained in [`COLLABORATION_STYLE.md`](COLLABORATION_STYLE.md). Communication with Gevorg is friendly, calm, direct, respectful, and non-bureaucratic. In Armenian, the natural form of address is “ընգեր”. Questions already answered in the repository or conversation are not repeated.

### Canonical write integrity

Every write, update, replacement, move, or deletion follows [`foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`](foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md). The mandatory sequence is: read the complete source → preserve SHA → write → re-read beginning and ending → verify synchronization → GREEN. Tool success is not evidence. On RED, work stops, the previous version is restored, and verification is repeated.

### Decisions

- `DECISIONS.md` preserves the historical `D-001–D-021` registry.
- `DECISION_INDEX.md` is the active append-only registry.
- Dedicated files preserve decisions `D-022` and `D-023`.
- The large `DECISIONS.md` file is not replaced through a full contents-API rewrite.

### Documentation and packaging

- Important documentation is bilingual Armenian + English with semantic equality.
- Approved ecosystem-level ideas become canonical documentation.
- Multi-file deliverables are delivered as complete packages and preferably as ZIP snapshots.
- A ZIP is a delivery snapshot, not the canonical source.

### Current state

All seven Foundation chapters are Locked v1. Audit remediation files have been applied. The release gate remains YELLOW only because GREEN validator execution evidence is not yet available. The next chat starts from `NEXT_CHAT_HANDOFF.md` and immediately checks the validator or CI result.

<!-- END: MENQ_STANDARD_PROJECT_CONTEXT -->