# MenQ Standard — Project Context / MenQ Standard — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Canonical repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-13

## Հայերեն

### Canonical source

MenQ Standard-ի միակ canonical source of truth-ը GitHub repository-ն է։ Chat-ը workshop է, ոչ canonical source։

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
- D-025 MenQ Design Platform Architecture v1 — Locked և GREEN։
- D-026 Canonical Session Read Law — Locked և machine-enforced։
- D-025 implementation merge — `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`։
- D-025 closure merge — `9a833339b1d707d6cd8a792e031dd8ca2857d556`։
- D-025 lock merge — `261f85e5b20d726a0ab1f05da84a4dc45a248873`։
- Validated lock head — `8ba2e987ff6dab2c25fda18744c7376953d0108f`։
- Parts 1–16 architecture, implementation packages, private preview candidate և two-consumer evidence-ը GREEN են։
- Explicit Owner lock approval — 2026-07-13։
- Final post-lock audit — [`platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md`](platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md)։

### Հաջորդ աշխատանք

1. D-025 transaction-ը փակված է․ բաց implementation, closure կամ lock action չկա։
2. Հետագա Design Platform փոփոխությունները կառավարել locked change-control կանոններով։
3. Owner-ը ընտրում է MenQ Standard-ի հաջորդ ecosystem priority-ն՝ առանձին decision transaction-ով։

---

## English

### Canonical source

The GitHub repository is the single canonical source of truth for MenQ Standard. Conversation is the workshop, not the canonical source.

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
- D-025 MenQ Design Platform Architecture v1 is Locked and GREEN.
- D-026 Canonical Session Read Law is Locked and machine-enforced.
- D-025 implementation merge: `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`.
- D-025 closure merge: `9a833339b1d707d6cd8a792e031dd8ca2857d556`.
- D-025 lock merge: `261f85e5b20d726a0ab1f05da84a4dc45a248873`.
- Validated lock head: `8ba2e987ff6dab2c25fda18744c7376953d0108f`.
- Parts 1–16 architecture, implementation packages, the private preview candidate, and two-consumer evidence are GREEN.
- Explicit Owner lock approval: 2026-07-13.
- Final post-lock audit: [`platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md`](platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md).

### Next work

1. The D-025 transaction is closed; no implementation, closure, or lock action remains open.
2. Govern future Design Platform changes under locked change-control rules.
3. The Owner selects the next MenQ Standard ecosystem priority through a separate decision transaction.

<!-- END: MENQ_STANDARD_PROJECT_CONTEXT -->