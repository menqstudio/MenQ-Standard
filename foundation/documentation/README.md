# MenQ Documentation Standard / MenQ փաստաթղթավորման ստանդարտ

**Status / Կարգավիճակ:** Locked v1 / Հաստատված v1  
**Version / Տարբերակ:** 1.0  
**Owner / Պատասխանատու:** MenQ Owner  
**Document class / Փաստաթղթի դաս:** Normative  
**Canonical path / Canonical ուղի:** `foundation/documentation/README.md`  
**Related decision / Կապված որոշում:** `D-021`

## Core Rule / Հիմնական կանոն

> **HY:** Չփաստաթղթավորված կարևոր գիտելիքը չի համարվում պահպանված։ Canonical documentation-ը MenQ ecosystem-ի operational memory-ն է։  
> **EN:** Important knowledge that is not documented is not considered preserved. Canonical documentation is the operational memory of the MenQ ecosystem.

---

## 1. Purpose / Նպատակ

**HY:** MenQ Documentation Standard-ը սահմանում է՝ որտեղ է պահպանվում canonical truth-ը, ինչ դեր ունի յուրաքանչյուր հիմնական փաստաթուղթ, ինչպես են փաստաթղթերը կառուցվում և անվանվում, ինչպես է պահպանվում Armenian–English semantic equality-ն, ինչպես են փոփոխությունները versioned և traceable դառնում, ինչպես են կանխվում stale, duplicated, missing կամ truncated փաստաթղթերը, և ինչպես են մարդիկ ու AI համակարգերը անվտանգ օգտագործում documentation-ը։

**EN:** MenQ Documentation Standard defines where canonical truth is preserved, the role of each primary document, how documents are structured and named, how Armenian–English semantic equality is maintained, how changes become versioned and traceable, how stale, duplicated, missing, or truncated documentation is prevented, and how humans and AI systems safely use documentation.

---

## 2. Boundary / Սահման

- **Governance** → ով ունի documentation approve անելու authority / who has authority to approve documentation.
- **Decision System** → ինչպես է բովանդակությունը approved decision դառնում / how content becomes an approved decision.
- **Documentation** → որտեղ, ինչ ձևով և ինչ integrity controls-ով է այն պահպանվում / where and how it is preserved, including integrity controls.
- **AI Collaboration** → ինչպես է AI-ն կարդում, ստեղծում, թարմացնում և ստուգում documentation-ը / how AI reads, creates, updates, and validates documentation.
- **Operating Standards** → domain-specific documentation workflows և templates / domain-specific documentation workflows and templates.

---

## 3. Documentation Principles / Փաստաթղթավորման սկզբունքներ

### 3.1 Canonical Before Convenient / Canonical-ը՝ հարմարից առաջ

**HY:** Chat-ը, AI memory-ն, local copy-ն, exported ZIP-ը կամ presentation-ը չեն փոխարինում canonical repository-ին։  
**EN:** Conversations, AI memory, local copies, exported ZIP packages, and presentations do not replace the canonical repository.

### 3.2 One Truth, Many Views / Մեկ ճշմարտություն, բազմաթիվ ներկայացումներ

**HY:** Նույն authoritative բովանդակությունը չի պահպանվում մի քանի անկախ տեղերում։ Այլ փաստաթղթերը link կամ summary են տալիս և նշում canonical source-ը։  
**EN:** The same authoritative content is not maintained independently in multiple locations. Other documents link to or summarize it while identifying the canonical source.

### 3.3 Documentation Is Part of the System / Documentation-ը համակարգի մաս է

**HY:** Documentation-ը optional explanation չէ։ Այն architecture-ի, product-ի, process-ի և governance-ի պարտադիր բաղադրիչ է։  
**EN:** Documentation is not optional explanation. It is a required component of architecture, products, processes, and governance.

### 3.4 Human and AI Readability / Մարդու և AI-ի ընթեռնելիություն

**HY:** Documentation-ը պետք է միաժամանակ հասկանալի լինի մարդկանց և machine-assisted readers-ի համար՝ հստակ headings-ով, stable terminology-ով, explicit status-ներով և predictable structure-ով։  
**EN:** Documentation must be understandable to both humans and machine-assisted readers through clear headings, stable terminology, explicit statuses, and predictable structure.

### 3.5 Bilingual Equality / Երկլեզու հավասարություն

**HY:** Հայերեն և անգլերեն canonical տարբերակները հավասար authoritative են և փոխանցում են նույն ամբողջական իմաստը։  
**EN:** Armenian and English canonical versions are equally authoritative and carry the same complete meaning.

### 3.6 History Is Preserved / Պատմությունը պահպանվում է

**HY:** Material փոփոխությունը չի վերագրում անցյալը։ Հին որոշումները, versions-ը և պատճառները պահպանվում են traceable ձևով։  
**EN:** Material changes do not rewrite the past. Previous decisions, versions, and rationales remain traceable.

### 3.7 Documentation Changes With Reality / Documentation-ը փոխվում է իրականության հետ

**HY:** Երբ system-ը, rule-ը կամ architecture-ը փոխվում է, համապատասխան documentation-ը փոխվում է նույն approved change-ի մասով։  
**EN:** When a system, rule, or architecture changes, the corresponding documentation changes as part of the same approved change.

### 3.8 Stale Documentation Is a Defect / Հնացած documentation-ը defect է

**HY:** Սխալ կամ հնացած փաստաթուղթը ավելի վտանգավոր է, քան բացահայտ բացակայող փաստաթուղթը, որովհետև այն ստեղծում է կեղծ վստահություն։  
**EN:** Incorrect or stale documentation is more dangerous than visibly missing documentation because it creates false confidence.

---

## 4. Canonical Repository Rule / Canonical repository-ի կանոն

**HY:** Յուրաքանչյուր MenQ project, product, platform, standard կամ governed domain պետք է ունենա մեկ հայտարարված canonical repository կամ canonical documentation location։ Պետք է հնարավոր լինի պարզել canonical repository-ն, default branch-ը, document owner-ը, ակտիվ version-ը, applicable decisions-ը և archive location-ը։

**EN:** Every MenQ project, product, platform, standard, or governed domain must have one declared canonical repository or canonical documentation location. It must be possible to determine the canonical repository, default branch, document owner, active version, applicable decisions, and archive location.

---

## 5. Documentation Architecture / Փաստաթղթավորման architecture

```text
Canonical Repository
├── README.md
├── PROJECT_CONTEXT.md
├── AI_WORKING_CONTEXT.md
├── DECISIONS.md
├── CHANGELOG.md
├── ROADMAP.md
│
├── <major-area>/
│   ├── README.md
│   ├── PROJECT_CONTEXT.md
│   └── topic-specific documents
│
└── archive/
```

**HY:** Այս կառուցվածքը baseline է։ Project-specific շերտերը կարող են ավելացնել անհրաժեշտ փաստաթղթեր, բայց չեն փոխում core file roles-ը։  
**EN:** This structure is the baseline. Project-specific layers may add necessary documents but do not redefine the core file roles.

---

## 6. Core File Roles / Հիմնական ֆայլերի դերերը

### 6.1 `README.md` — Human Entry Point / Մարդու մուտքի կետ

**HY:** `README.md`-ը մարդկանց համար առաջին ընթեռնելի entry point-ն է։ Այն բացատրում է՝ ինչ է system-ը կամ folder-ը, ինչ նպատակ ունի, ինչ վիճակում է, ինչպես է կառուցված, որտեղ են հիմնական փաստաթղթերը և ինչից սկսել։  
**EN:** `README.md` is the first human-readable entry point. It explains what the system or folder is, its purpose, current status, structure, where the primary documents are, and where to begin.

### 6.2 `PROJECT_CONTEXT.md` — Stable AI Context / Կայուն AI կոնտեքստ

**HY:** `PROJECT_CONTEXT.md`-ը պահպանում է AI collaborators-ի համար կայուն, երկարաժամկետ context-ը՝ canonical source, mission և scope, architecture boundaries, մշտական working rules, Owner preferences, required startup workflow և prohibited assumptions։ Այն չի օգտագործվում արագ փոփոխվող task status-ի համար։

**EN:** `PROJECT_CONTEXT.md` preserves stable, long-term context for AI collaborators: the canonical source, mission and scope, architecture boundaries, persistent working rules, Owner preferences, the required startup workflow, and prohibited assumptions. It is not used for rapidly changing task status.

### 6.3 `AI_WORKING_CONTEXT.md` — Living Continuity / Կենդանի շարունակականություն

**HY:** `AI_WORKING_CONTEXT.md`-ը պահպանում է ընթացիկ աշխատանքային վիճակը, վերջին synchronized status-ը, բաց հարցերը և հաջորդ քայլը։ Այն չի փոխարինում canonical chapter-ներին, չի ստեղծում նոր truth, summary է canonical փաստերից, պետք է պարբերաբար synchronize արվի և stale լինելու դեպքում հստակ նշվի։

**EN:** `AI_WORKING_CONTEXT.md` preserves the current working state, last synchronized status, open matters, and the next step. It does not replace canonical chapters, does not create new truth, summarizes canonical facts, must be synchronized regularly, and must be explicitly marked when stale.

### 6.4 `DECISIONS.md` — Locked Decision Registry / Հաստատված որոշումների գրանցամատյան

**HY:** `DECISIONS.md`-ը պահպանում է approved և locked decisions-ը՝ unique ID-ով, date-ով, status-ով, rationale-ով և canonical links-ով։ Այն չի օգտագործվում որպես brainstorm կամ task list։  
**EN:** `DECISIONS.md` preserves approved and locked decisions with a unique ID, date, status, rationale, and canonical links. It is not used as a brainstorm or task list.

### 6.5 `CHANGELOG.md` — Historical Change Record / Փոփոխությունների պատմություն

**HY:** `CHANGELOG.md`-ը chronological history է՝ ինչ է ավելացվել, փոխվել, fixed, deprecated, superseded կամ removed։ Այն բացատրում է ինչ է փոխվել, ոչ ամբողջ decision rationale-ը։  
**EN:** `CHANGELOG.md` is the chronological history of what was added, changed, fixed, deprecated, superseded, or removed. It explains what changed, not the complete decision rationale.

### 6.6 `ROADMAP.md` — Future Direction / Ապագա ուղղություն

**HY:** `ROADMAP.md`-ը պահպանում է planned, proposed և future work-ը։ Roadmap item-ը commitment կամ locked decision չէ, մինչև Decision System-ով չի հաստատվել։  
**EN:** `ROADMAP.md` preserves planned, proposed, and future work. A roadmap item is not a commitment or locked decision until approved through the Decision System.

---

## 7. Folder Documentation Rule / Folder documentation-ի կանոն

**HY:** Յուրաքանչյուր independent project և յուրաքանչյուր governed major folder պարտադիր ունի `README.md` և `PROJECT_CONTEXT.md`։ Երկարաժամկետ կամ ակտիվ աշխատանքի դեպքում կիրառվում են նաև `DECISIONS.md`, `CHANGELOG.md`, `ROADMAP.md` և `AI_WORKING_CONTEXT.md`։ Low-level source-code folders-ը առանձին documentation set չեն պահանջում, եթե դրանք governed knowledge boundary չեն։

**EN:** Every independent project and every governed major folder must contain `README.md` and `PROJECT_CONTEXT.md`. Long-lived or actively governed work also uses `DECISIONS.md`, `CHANGELOG.md`, `ROADMAP.md`, and `AI_WORKING_CONTEXT.md`. Low-level source-code folders do not require a separate documentation set unless they form a governed knowledge boundary.

---

## 8. Document Classes / Փաստաթղթերի դասեր

- **Normative:** սահմանում է պարտադիր rule, standard, architecture կամ decision / defines a mandatory rule, standard, architecture, or decision.
- **Informative:** բացատրում է normative content-ը, բայց չի ստեղծում նոր rule / explains normative content without creating a new rule.
- **Working:** draft, exploration, notes կամ ընթացիկ context է / contains drafts, exploration, notes, or current working context.
- **Generated:** automation-ից ստացված output է՝ source և regeneration rule-ով / output produced by automation with a declared source and regeneration rule.
- **Archived:** այլևս active authority չունի և պահպանվում է history-ի համար / no longer carries active authority and is preserved for history.

Document-ը պետք է պարզ ցույց տա իր class-ը, երբ ambiguity հնարավոր է։ A document must state its class when ambiguity is possible.

---

## 9. Required Document Metadata / Պարտադիր metadata

Normative և long-lived documents-ը պետք է հնարավորության դեպքում ներառեն՝

```text
Title:
Status:
Version:
Owner:
Scope:
Document class:
Canonical path:
Last updated:
Related decisions:
Supersedes:
Superseded by:
Review trigger or cadence:
```

**HY:** Metadata-ն պետք է լինի փաստացի և թարմ։ Դատարկ կամ կեղծ metadata-ն չի ավելացվում միայն template-ը լրացնելու համար։  
**EN:** Metadata must be factual and current. Empty or invented metadata is not added merely to satisfy a template.

---

## 10. Naming and Path Rules / Անվանման և path-ի կանոններ

1. Root governance files-ը օգտագործում են stable uppercase names՝ `README.md`, `DECISIONS.md`, `CHANGELOG.md`։
2. Directory names-ը օգտագործում են predictable lowercase kebab-case, եթե locked convention-ը այլ բան չի սահմանում։
3. File name-ը նկարագրում է բովանդակությունը, ոչ ժամանակավոր task-ը։
4. Անորոշ անուններ՝ `final.md`, `new.md`, `latest2.md`, `stuff.md`, չեն օգտագործվում canonical documentation-ում։
5. Stable path-ը գերադասելի է հաճախակի rename-ից։
6. Rename-ի դեպքում links-ը և references-ը թարմացվում են նույն change-ում։

---

## 11. Bilingual Documentation Rule / Երկլեզու documentation-ի կանոն

1. Հայերեն և անգլերեն բաժինները հավասար authoritative են։
2. Երկու լեզուներում պարտադիր է նույն scope-ը, rules-ը, exceptions-ը և examples-ի իմաստը։
3. Մեկ լեզվով միայն summary, իսկ մյուսով ամբողջ rule չի թույլատրվում։
4. Literal translation-ը պարտադիր չէ, semantic equality-ն պարտադիր է։
5. Technical term-ը կարող է մնալ անգլերեն, երբ forced translation-ը կորցնում է precision-ը։
6. Material update-ը complete չէ, մինչև երկու լեզուներն էլ synchronized չեն։
7. Language mismatch-ը documentation defect է։

---

## 12. Single Source and Duplication Rule / Միակ աղբյուրի և duplication-ի կանոն

**HY:** Normative rule-ը մեկ canonical location ունի։ Այլ փաստաթղթերում թույլատրվում է link, կարճ summary, կիրառման օրինակ կամ product-specific specialization։ Չի թույլատրվում ամբողջ rule-ը copy-paste անել և անկախ թարմացնել, ստեղծել նույն authority ունեցող երկրորդ տարբերակ կամ summary-ն ներկայացնել որպես complete canonical rule։

**EN:** A normative rule has one canonical location. Other documents may contain a link, short summary, application example, or product-specific specialization. They may not copy the complete rule and maintain it independently, create a second version with equal authority, or present a summary as the complete canonical rule.

---

## 13. Documentation Change Classes / Documentation փոփոխությունների դասեր

### Editorial Change / Խմբագրական փոփոխություն

Typo, grammar, formatting, broken link կամ wording clarification without semantic change։ Formal decision պարտադիր չէ, բայց change-ը traceable է։

### Material Change / Իմաստային փոփոխություն

Rule-ի իմաստի, scope-ի, requirement-ի, authority-ի, status-ի, terminology-ի, architecture-ի կամ process-ի փոփոխություն։ Material change-ը պահանջում է Decision System-ի համապատասխան lifecycle։

---

## 14. Update Transaction Rule / Միասնական update-ի կանոն

**HY:** Approved փոփոխությունը պետք է հնարավորինս մեկ complete documentation transaction-ով թարմացնի՝ canonical chapter-ը, related `DECISIONS.md` entry-ն, `CHANGELOG.md`-ը, parent index կամ `README.md`-ը, `PROJECT_CONTEXT.md` կամ `AI_WORKING_CONTEXT.md`-ը երբ context-ը փոխվել է, և related links ու status-ները։ Partial synchronization-ը documentation debt է։

**EN:** An approved change should update, as one complete documentation transaction whenever practical, the canonical chapter, related `DECISIONS.md` entry, `CHANGELOG.md`, parent index or `README.md`, `PROJECT_CONTEXT.md` or `AI_WORKING_CONTEXT.md` when context changed, and related links and statuses. Partial synchronization creates documentation debt.

---

## 15. Integrity Protection / Integrity-ի պաշտպանություն

Յուրաքանչյուր canonical write-ից հետո պարտադիր է verify անել՝

1. file-ը բացվում է,
2. title-ը և status-ը պահպանված են,
3. expected beginning և ending sections-ը գոյություն ունեն,
4. content-ը պատահաբար truncated չէ,
5. Armenian և English բաժինները ամբողջական են,
6. links-ը ճիշտ են,
7. parent index-ը համապատասխանում է,
8. SHA կամ version-ը փոփոխվել է սպասված ձևով,
9. unrelated canonical information չի կորել։

**EN:** After every canonical write, verify that the file can be read; title and status remain present; expected beginning and ending sections exist; content was not accidentally truncated; Armenian and English sections are complete; links are correct; the parent index is synchronized; the SHA or version changed as expected; and unrelated canonical information was not lost.

> **HY:** Write success-ը evidence չէ։ Re-read և integrity verification են evidence-ը։  
> **EN:** A successful write response is not evidence. Re-reading and integrity verification are the evidence.

---

## 16. Safe Replacement Rule / Անվտանգ ամբողջական փոխարինման կանոն

**HY:** Երբ tool-ը file-ը ամբողջությամբ replace է անում, սկզբում կարդացվում է ամբողջ ընթացիկ canonical content-ը, պահպանվում է current file identifier կամ SHA-ն, նոր content-ը կառուցվում է ամբողջական ձևով, write-ից հետո file-ը կրկին կարդացվում է, իսկ truncation կամ data loss-ի դեպքում history-ից վերականգնվում է նախորդ canonical version-ը։

**EN:** When a tool replaces an entire file, the complete current canonical content is read first, the current file identifier or SHA is preserved, replacement content is constructed in full, the file is re-read after the write, and if truncation or data loss occurs, the previous canonical version is restored from history.

---

## 17. No Silent Deletion / Լուռ ջնջման արգելք

**HY:** Canonical information-ը չի ջնջվում միայն այն պատճառով, որ այլևս ակտիվ չէ։ Այն supersede, deprecate, retire կամ archive է արվում։ Permanent deletion-ը պահանջում է explicit authority և պահպանման անհրաժեշտության գնահատում։

**EN:** Canonical information is not deleted merely because it is no longer active. It is superseded, deprecated, retired, or archived. Permanent deletion requires explicit authority and an assessment of preservation needs.

---

## 18. Link and Reference Rules / Link-երի և reference-ների կանոններ

1. Relative repository links-ը նախընտրելի են internal files-ի համար։
2. Link text-ը նկարագրում է destination-ը։
3. Canonical document-ը չի հղվում միայն chat message-ով։
4. External source-ի դեպքում պահպանվում են title, source և access date, երբ նյութը կարող է փոխվել։
5. Broken link-ը defect է։
6. Renamed document-ը պետք է ունենա updated inbound references։
7. Orphan normative document-ը՝ առանց parent index link-ի, documentation defect է։

---

## 19. Evidence and Source Rule / Ապացույցի և աղբյուրի կանոն

**HY:** Factual կամ current claim-ը պետք է ունենա համապատասխան source, երբ այն արտաքին է, փոփոխական է, վիճելի է, high-risk է կամ decision-ի հիմք է։ AI-generated text-ը ինքնուրույն source կամ evidence չէ։ Documentation-ը պետք է տարբերակի fact, decision, assumption, proposal, interpretation և example։

**EN:** A factual or current claim must have an appropriate source when it is external, changeable, disputed, high-risk, or a basis for a decision. AI-generated text is not independently a source or evidence. Documentation must distinguish fact, decision, assumption, proposal, interpretation, and example.

---

## 20. Generated Documentation / Գեներացված documentation

Generated document-ը պետք է նշի source data-ն, generator-ը կամ process-ը, generated date-ը, manual edit-ի թույլատրելիությունը, regeneration command կամ workflow-ը, և canonical է, թե derived artifact։

**HY:** Generated output-ը canonical չի դառնում միայն այն պատճառով, որ automation-ն է այն ստեղծել։  
**EN:** Generated output does not become canonical merely because automation produced it.

---

## 21. Package and ZIP Rule / Փաթեթի և ZIP-ի կանոն

**HY:** Երբ deliverable-ը բաղկացած է մի քանի կապված ֆայլերից, այն տրվում է որպես ամբողջական package և հնարավորության դեպքում ZIP։ Package-ը պետք է պարունակի ամբողջական file set-ը, root `README.md`, version կամ snapshot date, մեծ package-ի դեպքում file manifest և missing dependency-ների բացակայության ստուգում։ ZIP-ը delivery snapshot է, ոչ canonical source։ Canonical repository-ն պահպանում է active truth-ը։

**EN:** When a deliverable contains multiple related files, it is delivered as one complete package and preferably as a ZIP. The package must contain the complete file set, a root `README.md`, a version or snapshot date, a file manifest when the package is large, and verification that no required dependencies are missing. A ZIP is a delivery snapshot, not the canonical source. The canonical repository preserves the active truth.

---

## 22. Documentation Ownership / Documentation ownership

**HY:** Յուրաքանչյուր normative կամ long-lived document պետք է ունենա պատասխանատու owner կամ steward։ Owner-ը պատասխանատու է correctness-ի, synchronization-ի, review-ի, deprecation-ի, archive-ի և unresolved conflict-ի escalation-ի համար։ AI-ն կարող է maintain և review անել documentation-ը, բայց human accountability-ն չի վերանում։

**EN:** Every normative or long-lived document must have a responsible owner or steward. The owner is accountable for correctness, synchronization, review, deprecation, archiving, and escalation of unresolved conflicts. AI may maintain and review documentation, but human accountability remains.

---

## 23. Review Triggers / Վերանայման triggers

Document-ը review է պահանջում, երբ related decision, implementation կամ terminology է փոխվում, contradiction է հայտնաբերվում, broken link կամ missing section կա, bilingual mismatch կա, Owner կամ steward-ը փոխվում է, review cadence-ը հասնում է, կամ incident-ը ցույց է տալիս, որ documentation-ը սխալ կամ անբավարար էր։

---

## 24. Documentation Quality Gates / Documentation quality gates

1. **Purpose Gate:** նպատակը և audience-ը հստակ են / purpose and audience are clear.
2. **Canonical Location Gate:** canonical path-ը և owner-ը հստակ են / canonical path and owner are clear.
3. **Structural Completeness Gate:** required sections և metadata առկա են / required sections and metadata exist.
4. **Semantic Accuracy Gate:** բովանդակությունը համապատասխանում է approved truth-ին / content matches approved truth.
5. **Bilingual Equality Gate:** երկու լեզուներն հավասար ամբողջական են / both languages are equally complete.
6. **Traceability Gate:** decisions, sources և changes traceable են / decisions, sources, and changes are traceable.
7. **Integrity Gate:** file-ը ամբողջական, readable, non-truncated է և links-ը աշխատում են / the file is complete, readable, non-truncated, and links work.
8. **Synchronization Gate:** indexes, changelog և context files synchronized են / indexes, changelog, and context files are synchronized.

Required gate-ի `RED` վիճակում document-ը չի ստանում `Locked` status։ A document does not receive `Locked` status while a required gate is `RED`.

---

## 25. Documentation KPIs / Documentation KPI-ներ

Documentation system-ը կարող է չափվել՝ missing required documents, stale document rate, broken internal links, bilingual mismatch count, undocumented locked decisions, documentation update lag, orphan normative documents, expired review dates, duplicate canonical rules, integrity կամ truncation incidents, AI sessions started from stale context և changes that updated implementation but not documentation։ KPI-ն պետք է չափի trust և continuity, ոչ միայն document count-ը։

---

## 26. Minimum Project Documentation Set / Նվազագույն project documentation set

Յուրաքանչյուր active MenQ project-ի minimum set-ը՝

```text
README.md
PROJECT_CONTEXT.md
DECISIONS.md
CHANGELOG.md
ROADMAP.md
```

AI-driven շարունակական աշխատանքի դեպքում ավելացվում է՝

```text
AI_WORKING_CONTEXT.md
```

Յուրաքանչյուր major governed area ունի իր՝

```text
README.md
PROJECT_CONTEXT.md
```

---

## 27. Documentation Completion Rule / Documentation completion-ի կանոն

**HY:** Փաստաթուղթը complete չէ, մինչև բովանդակությունը approved scope-ին համապատասխանում է, երկու լեզուներն ամբողջական են, related decisions-ը linked են, parent index-ը synchronized է, changelog entry-ն գրանցված է և post-write integrity verification-ը անցել է։

**EN:** A document is not complete until its content matches the approved scope, both languages are complete, related decisions are linked, the parent index is synchronized, the changelog entry is recorded, and post-write integrity verification has passed.

---

## 28. Final Documentation Rule / Վերջնական կանոն

> **HY:** Chat-ը ստեղծում է գաղափար։ Decision-ը հաստատում է ուղղությունը։ Documentation-ը պահպանում է ճշմարտությունը։ Verification-ը ապացուցում է, որ այն չի կորել։  
> **EN:** Conversation creates the idea. A decision approves the direction. Documentation preserves the truth. Verification proves that it was not lost.
