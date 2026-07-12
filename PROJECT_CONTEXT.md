# MenQ Standard — Project Context / MenQ Standard — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Canonical repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-13

## Հայերեն

### Canonical source

MenQ Standard-ի միակ canonical source of truth-ը GitHub repository-ն է։ Chat-ը workshop է, ոչ canonical source։ Repository address-ը և documented persistent rules-ը Owner-ից նոր chat-ում կրկին չեն հարցվում։

### Պարտադիր startup workflow

Յուրաքանչյուր նոր AI session մինչև substantive աշխատանք պարտավոր է active branch/ref-ում enumerate և ամբողջությամբ կարդալ repository-ի բոլոր tracked `.md` files-ը՝ ըստ [`foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`](foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md)-ի։ Active PR-ի դեպքում նաև կարդացվում են metadata-ն, changed files-ը, diff-ը, review threads-ը և checks-ը։

### Human–AI և authority

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն MenQ architect և engineering teammate է։ Final authority-ն և accountability-ն մարդունն են։ AI-ն չի կարող self-approve անել, human approval հորինել կամ canonical truth-ը ինքնուրույն lock անել։

### Canonical write integrity

Յուրաքանչյուր write, update, replacement, move կամ delete ենթարկվում է `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`-ին՝ complete read → SHA preserve → write → beginning/end re-read → synchronization verification → GREEN։ Tool success-ը evidence չէ։

### Ընթացիկ canonical վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 Platforms Architecture v1 — merged և canonical։
- D-025 MenQ Design Platform Architecture v1 — PR #3-ով merge է եղել, բայց `Locked` չէ։
- D-026 Canonical Session Read Law — Locked և machine-enforced։
- PR #3 merge commit — `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`։
- Merged implementation head — `9c10c288c16ef319ce4d5aa91000f7b0a46ecf60`։
- Closure branch — `d-025-post-merge-closure`։
- Parts 1–16 architecture, implementation package set, private preview candidate և two-consumer evidence-ը GREEN են։
- Post-merge canonical synchronization և `main` validation evidence-ը closure transaction-ի scope-ն են։
- D-025 lock-ը պահանջում է առանձին explicit Owner decision։

### Հաջորդ աշխատանք

1. Ավարտել `d-025-post-merge-closure` branch-ի canonical synchronization-ը։
2. Ստանալ closure PR-ի GREEN checks։
3. Merge-ից հետո ստանալ GREEN `main` push checks։
4. Final closure record-ը դարձնել GREEN։
5. Owner-ին ներկայացնել առանձին D-025 lock որոշում։

---

## English

### Canonical source

The GitHub repository is the single canonical source of truth for MenQ Standard. Conversation is the workshop, not the canonical source. Do not ask the Owner again for the repository address or documented persistent rules.

### Required startup workflow

Before substantive work, every AI session must enumerate and completely read every tracked `.md` file on the active branch/ref under [`foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`](foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md). For an active PR, metadata, changed files, diff, review threads, and checks must also be read.

### Human–AI and authority

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI may not self-approve, invent human approval, or independently lock canonical truth.

### Canonical write integrity

Every write follows `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`: complete read → preserve SHA → write → re-read beginning and ending → verify synchronization → GREEN. Tool success is not evidence.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- D-024 Platforms Architecture v1 is merged and canonical.
- D-025 MenQ Design Platform Architecture v1 was merged through PR #3 but is not `Locked`.
- D-026 Canonical Session Read Law is Locked and machine-enforced.
- PR #3 merge commit: `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`.
- Merged implementation head: `9c10c288c16ef319ce4d5aa91000f7b0a46ecf60`.
- Closure branch: `d-025-post-merge-closure`.
- Parts 1–16 architecture, the implementation package set, the private preview candidate, and two-consumer evidence are GREEN.
- Post-merge canonical synchronization and `main` validation evidence are the scope of the closure transaction.
- D-025 lock requires a separate explicit Owner decision.

### Next work

1. Complete canonical synchronization on `d-025-post-merge-closure`.
2. Obtain GREEN closure PR checks.
3. After merge, obtain GREEN `main` push checks.
4. Mark the final closure record GREEN.
5. Present a separate D-025 lock decision to the Owner.

<!-- END: MENQ_STANDARD_PROJECT_CONTEXT -->
