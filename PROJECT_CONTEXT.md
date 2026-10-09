# MenQ Standard — Project Context / MenQ Standard — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Canonical repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Last synchronized / Վերջին համաժամեցում:** 2026-10-09

## Հայերեն

### Canonical source

MenQ Standard-ի միակ canonical source of truth-ը GitHub repository-ն է։ Chat-ը workshop է, ոչ canonical source։

### Պարտադիր startup workflow

Յուրաքանչյուր նոր AI session մինչև substantive աշխատանք պարտավոր է active branch/ref-ում ամբողջությամբ կարդալ session-read core-ը՝ [`foundation/ai-collaboration/SESSION_READ_MANIFEST.json`](foundation/ai-collaboration/SESSION_READ_MANIFEST.json)-ի `core` ցանկը, իսկ որևէ directory-ում աշխատելուց առաջ՝ նաև այդ directory-ի area-ի ֆայլերը՝ ըստ [`foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`](foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md)-ի։ Active PR-ի դեպքում նաև կարդացվում են metadata-ն, changed files-ը, diff-ը, review threads-ը և checks-ը։

### Human–AI և authority

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն MenQ architect և engineering teammate է։ Final authority-ն և accountability-ն մարդունն են։ AI-ն չի կարող self-approve անել, human approval հորինել կամ canonical truth-ը ինքնուրույն lock անել։

### Canonical write integrity

Յուրաքանչյուր write, update, replacement, move կամ delete ենթարկվում է `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`-ին՝ complete read → SHA preserve → write → beginning/end re-read → synchronization verification → GREEN։ Tool success-ը evidence չէ։

### Ընթացիկ canonical վիճակ

Ընթացիկ վիճակի միակ ամբողջական ցանկը [`README.md`](README.md)-ի `Status` բաժինն է։ Այս ֆայլը այն չի կրկնում․ Documentation Standard §6.2-ի համաձայն `PROJECT_CONTEXT.md`-ը կայուն context է, ոչ թե արագ փոփոխվող status։ Որոշումները գտնվում են [`DECISION_INDEX.md`](DECISION_INDEX.md)-ից, փոփոխությունների պատմությունը՝ [`CHANGELOG.md`](CHANGELOG.md)-ում։

### Հաջորդ աշխատանք

1. Բաց հարցերը և հաջորդ session-ի առաջին քայլը [`NEXT_CHAT_HANDOFF.md`](NEXT_CHAT_HANDOFF.md)-ում են։
2. Locked որոշումը (օրինակ՝ D-025) փոխվում է միայն governed change control-ով և Owner-ի explicit հաստատմամբ։
3. MenQ Standard-ի հաջորդ ecosystem priority-ն ընտրում է Owner-ը՝ առանձին decision transaction-ով։

---

## English

### Canonical source

The GitHub repository is the single canonical source of truth for MenQ Standard. Conversation is the workshop, not the canonical source.

### Required startup workflow

Before substantive work, every AI session must read in full, on the active branch/ref, the session-read core, which is the `core` list of [`foundation/ai-collaboration/SESSION_READ_MANIFEST.json`](foundation/ai-collaboration/SESSION_READ_MANIFEST.json), and, before working in a directory, the files of that directory's area, under [`foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`](foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md). For an active PR, metadata, changed files, diff, review threads, and checks must also be read.

### Human–AI and authority

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI may not self-approve, invent human approval, or independently lock canonical truth.

### Canonical write integrity

Every write follows `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`: complete read → preserve SHA → write → re-read beginning and ending → verify synchronization → GREEN. Tool success is not evidence.

### Current canonical state

The one complete list of the current state is the `Status` section of [`README.md`](README.md). This file does not restate it: under Documentation Standard §6.2, `PROJECT_CONTEXT.md` is stable context, not rapidly changing status. Decisions are found from [`DECISION_INDEX.md`](DECISION_INDEX.md), and the history of changes is in [`CHANGELOG.md`](CHANGELOG.md).

### Next work

1. Open matters and the first step of the next session are in [`NEXT_CHAT_HANDOFF.md`](NEXT_CHAT_HANDOFF.md).
2. A Locked decision (for example D-025) changes only through governed change control and explicit Owner approval.
3. The Owner selects the next MenQ Standard ecosystem priority through a separate decision transaction.

<!-- END: MENQ_STANDARD_PROJECT_CONTEXT -->