# MenQ Design Platform — Next Chat Handoff / MenQ Design Platform — Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-10-09 (`CR-0012`. ուժի մեջ է merge-ից հետո / in effect when merged)  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Canonical ref:** `main`

## Հայերեն

### Պարտադիր մեկնարկ

Մինչև substantive աշխատանք՝ active branch/ref-ում ամբողջությամբ կարդալ session-read core-ը՝ `foundation/ai-collaboration/SESSION_READ_MANIFEST.json`-ի `core` ցանկը, իսկ որևէ directory-ում աշխատելուց առաջ՝ նաև այդ directory-ի area-ի ֆայլերը՝ ըստ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`-ի։ Active PR-ի դեպքում կարդալ metadata, changed files, diff, review threads և checks։

### Ընթացիկ վիճակ

**Locked**

- D-025 architecture-ը `Locked` է 2026-07-13-ից՝ Owner-ի որոշմամբ։ Implementation merge — `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`, closure merge — `9a833339b1d707d6cd8a792e031dd8ca2857d556`, lock merge — `261f85e5b20d726a0ab1f05da84a4dc45a248873`, validated lock head — `8ba2e987ff6dab2c25fda18744c7376953d0108f`։
- Part 14 governance-ի implementation-ը `Locked` է 2026-10-07-ից ([`governance/`](governance/README.md))։

**Ուղղված**

- D-025-ի evidence-ը ուղղվել է 2026-10-07-ին ([`D-025_EVIDENCE_CORRECTION_RECORD.md`](D-025_EVIDENCE_CORRECTION_RECORD.md)). repository-ի ներսի երկու consumer-ը M2 pilot են, M3/M4-ը ապացուցված չէ, workflow artifact-ը ժամկետանց է, մշտական release-ը `design-platform-v0.1.0-next.0`-ն է։
- 2026-07-13-ի «two-consumer evidence — GREEN» պնդումը այլևս ուժի մեջ չէ։ D-025 որոշման ֆայլը, lock, closure և final-audit գրառումները կրում են ուղղման ծանուցում։
- `implementation/release/d-025-readiness-record.json`-ի top-level դաշտերը 2026-07-13-ի snapshot են. ընթացիկ վիճակը նրա `current` և `evidenceCorrections` դաշտերում է։

**Draft և իրականացման փուլում**

- D-027 brand expression շերտը. որոշումը `Approved — Implementing` է, շերտի և Bro extension-ի lifecycle-ը՝ Draft։ Չափված է 2026-10-09-ին՝ 132 token, 35 core կոմպոնենտ bundle-ում, 5 Bro կոմպոնենտ։
- Repository-ի առաջին էջի ստանդարտ v1-ը Draft է (`CR-0011`)։
- Տասը package-ը Preview են. private preview candidate-ը `0.1.0-next.0`-ն է։

**Change request-ներ**

- Փակված՝ `CR-0001`, `CR-0002`, `CR-0003`, `CR-0004`։
- Բաց՝ `CR-0005`…`CR-0011`. աշխատանքը merge է եղել, բայց ամեն մեկի `closureBlockedBy`-ում անվանված evidence-ը չկա։
- Առաջարկված՝ `CR-0012` (այս համաժամեցումը). սպասում է Owner-ի հաստատմանը։

### Շարունակելու ճշգրիտ կետը

1. **Իրական consumer-ի պարտավորությունը բաց է։** Առաջինը MenQ Webpage-ն է, երկրորդը ընտրում է Owner-ը։ Գրանցված ընթացքը՝ Webpage-ը pin է արել `tokens.vars.css`-ը և «M1-candidate» է. բարձրացումը Owner-ի որոշում է։ Չլուծված հարց. `tokens.vars.css`-ը D-027 շերտի ֆայլ է, ոչ D-025 package, ուստի Owner-ը պետք է որոշի՝ դա հաշվվո՞ւմ է որպես D-025 adoption։
2. **D-025 ↔ D-027 token mapping-ը որոշված չէ։** D-027-ը պահանջում է այն որոշել նախքան Locked դառնալը։
3. **`CR-0005`…`CR-0011`-ի evidence-ը հավաքել** (Webpage-ի re-pin և axe արդյունքներ, Chromium test-երի գրառումներ, մյուս repository-ների front page PR-ները), հետո փակել։
4. **Բաց accessibility թերություն.** հիմնական Button-ը light theme-ում սպիտակ տեքստը դնում է gradient-ի վրա, որի cyan ծայրում կոնտրաստը 2.43:1 է (պահանջը՝ 4.5:1)։ Ուղղումը պահանջում է նոր change request։
5. **Status պիտակների հակասությունները** թվարկված են `CR-0012`-ում. դրանք լուծում է միայն Owner-ը։
6. `ru` locale pack-ի ձևակերպումը (D-027-ի review trigger)։
7. Backlog (տես [`ROADMAP.md`](ROADMAP.md))՝ Part 13 (portal, catalog, design-tool), M5 evidence, codemod-ներ, լրացուցիչ locale pack-եր։
8. Ամեն ոչ խմբագրական փոփոխություն անցնում է change request-ով. pull request-ի նկարագրության մեջ գրել `Change-Request: CR-NNNN`։

### Արգելված գործողություններ

- Locked boundary-ն silently չփոխել։
- Historical evidence-ը չջնջել կամ վերագրել։
- Owner-ի approval-ը նրա փոխարեն չլրացնել։
- Change request-ը չփակել evidence-ով, որը repository-ից չի երևում։

---

## English

### Mandatory startup

Before substantive work, read in full, on the active branch/ref, the session-read core, which is the `core` list of `foundation/ai-collaboration/SESSION_READ_MANIFEST.json`, and, before working in a directory, the files of that directory's area, under `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`. For an active PR, read metadata, changed files, diff, review threads, and checks.

### Current state

**Locked**

- The D-025 architecture has been `Locked` since 2026-07-13 by Owner decision. Implementation merge: `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`; closure merge: `9a833339b1d707d6cd8a792e031dd8ca2857d556`; lock merge: `261f85e5b20d726a0ab1f05da84a4dc45a248873`; validated lock head: `8ba2e987ff6dab2c25fda18744c7376953d0108f`.
- The Part 14 governance implementation has been `Locked` since 2026-10-07 ([`governance/`](governance/README.md)).

**Corrected**

- D-025's evidence was corrected on 2026-10-07 ([`D-025_EVIDENCE_CORRECTION_RECORD.md`](D-025_EVIDENCE_CORRECTION_RECORD.md)): the two in-repository consumers are M2 pilots, M3/M4 is not evidenced, the workflow artifact has expired, and the permanent release is `design-platform-v0.1.0-next.0`.
- The 2026-07-13 claim "two-consumer evidence is GREEN" is no longer in force. The D-025 decision file and the lock, closure and final-audit records carry a correction notice.
- The top-level fields of `implementation/release/d-025-readiness-record.json` are a 2026-07-13 snapshot; the current state is in its `current` and `evidenceCorrections` fields.

**Draft and implementing**

- The D-027 brand expression layer: the decision is `Approved — Implementing`; the lifecycle of the layer and of the Bro extension is Draft. Measured on 2026-10-09: 132 tokens, 35 core components in the bundle, 5 Bro components.
- Repository front page standard v1 is Draft (`CR-0011`).
- The ten packages are Preview; the private preview candidate is `0.1.0-next.0`.

**Change requests**

- Closed: `CR-0001`, `CR-0002`, `CR-0003`, `CR-0004`.
- Open: `CR-0005`…`CR-0011`. Their work is merged, but the evidence each names in `closureBlockedBy` does not exist yet.
- Proposed: `CR-0012` (this synchronisation), awaiting the Owner's approval.

### Exact continuation point

1. **The real-consumer obligation is open.** MenQ Webpage is the first; the Owner selects the second. Recorded progress: Webpage pinned `tokens.vars.css` and is an "M1-candidate"; promotion is an Owner decision. Unresolved question: `tokens.vars.css` is a file of the D-027 layer, not a D-025 package, so the Owner has to decide whether that counts as D-025 adoption.
2. **The D-025 ↔ D-027 token mapping is not decided.** D-027 requires it to be decided before it can be Locked.
3. **Collect the evidence for `CR-0005`…`CR-0011`** (Webpage re-pin and axe results, records of the Chromium tests, the front-page pull requests in the other repositories), then close them.
4. **Open accessibility defect:** in the light theme the primary Button puts white text on a gradient whose cyan end gives 2.43:1 (the rule is 4.5:1). Fixing it needs a new change request.
5. **The status-label conflicts** are listed in `CR-0012`; only the Owner can settle them.
6. Formalising the `ru` locale pack (a D-027 review trigger).
7. Backlog (see [`ROADMAP.md`](ROADMAP.md)): Part 13 (portal, catalog, design-tool), M5 evidence, codemods, additional locale packs.
8. Every non-editorial change goes through a change request; put `Change-Request: CR-NNNN` in the pull-request description.

### Prohibited actions

- Do not silently change the locked boundary.
- Do not delete or rewrite historical evidence.
- Do not fill in the Owner's approval on his behalf.
- Do not close a change request on evidence that cannot be seen in the repository.

<!-- END: MENQ_DESIGN_PLATFORM_NEXT_CHAT_HANDOFF -->