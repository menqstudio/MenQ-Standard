# MenQ Standard — AI Working Context

> Living continuity document for AI collaborators.  
> AI համագործակիցների կենդանի շարունակականության փաստաթուղթ։

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Working  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-13  
**Canonical repository:** `https://github.com/menqstudio/MenQ-Standard`

## Հայերեն

### Պարտադիր startup workflow

Յուրաքանչյուր նոր AI session մինչև substantive աշխատանք պարտավոր է active branch/ref-ում ամբողջությամբ կարդալ session-read core-ը՝ `foundation/ai-collaboration/SESSION_READ_MANIFEST.json`-ի `core` ցանկը, որևէ directory-ում աշխատելուց առաջ՝ նաև այդ directory-ի area-ի ֆայլերը, իսկ active PR-ի դեպքում՝ metadata, changed files, diff, review threads և checks։ Պարտադիր օրենքը՝ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`։

### Human–AI սկզբունք

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն MenQ architect և engineering teammate է։ Final authority-ն և accountability-ն մարդունն են։ AI-ն չի self-approve անում և canonical truth չի lock անում։

### Ընթացիկ canonical վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 — Locked (2026-10-07)։
- Foundation v1.0.0 — հրապարակված՝ `foundation-v1.0.0` GitHub Release։
- D-025 evidence — ուղղված. consumer-ները M2 pilot են, իրական consumer-ի պարտավորությունը բաց է։
- D-025 — Locked և GREEN։
- D-026 — Locked. մասամբ փոխարինված է D-028-ով։ CI-ը ստուգում է Markdown inventory-ն, ոչ թե session-ի ընթերցումը։
- D-028 — Proposed (առաջարկված. հաստատումը Owner-ի կողմից նրա pull request-ի merge-ն է)։ Gate-ը core-ը պահում է 120,000 բայթի սահմանում։
- D-027 — Approved — Implementing (brand expression layer + Bro product extension)։
- D-025 implementation merge — `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`։
- D-025 closure merge — `9a833339b1d707d6cd8a792e031dd8ca2857d556`։
- D-025 lock merge — `261f85e5b20d726a0ab1f05da84a4dc45a248873`։
- Final audit — `platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md`։
- D-025 transaction-ը փակված է։

### Locked invariants

- Shared core-ը product-neutral է։
- Canonical dependency model-ը՝ Reference → Semantic → Component → Pattern → Product Extension։
- Theme, state, density, platform, locale, accessibility և motion preference-ը orthogonal dimensions են։
- Controlled exceptions-ը governed bypass են, ոչ normal layer։
- Generated portal/catalog/design-tool views-ը source of truth չեն։
- Armenian և English canonical languages են։
- D-025 փոփոխությունը պահանջում է governed change control և explicit Owner approval։

### Հաջորդ հստակ աշխատանք

2026-10-07 zero-trust audit-ի remediation-ը շարունակվում է փուլերով (workflow security, bilingual completion, Owner-ի որոշումներ)։ D-027-ը Locked դառնալու համար պետք է D-025 mapping-ը և առաջին իրական consumer-ը։ Դրանից հետո Owner-ը ընտրում է հաջորդ ecosystem priority-ն։

---

## English

### Required startup workflow

Before substantive work, every AI session must read in full, on the active branch/ref, the session-read core, which is the `core` list of `foundation/ai-collaboration/SESSION_READ_MANIFEST.json`; before working in a directory, also the files of that directory's area; and, for an active PR, metadata, changed files, diff, review threads, and checks. The mandatory law is `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`.

### Human–AI principle

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI does not self-approve or lock canonical truth.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- D-024 is Locked (2026-10-07).
- Foundation v1.0.0 is published as the `foundation-v1.0.0` GitHub Release.
- D-025 evidence is corrected: the consumers are M2 pilots and the real-consumer obligation is open.
- D-025 is Locked and GREEN.
- D-026 is Locked and superseded in part by D-028. CI checks the Markdown inventory, not a session's read.
- D-028 is Proposed (proposed; the Owner's merge of its pull request is the approval). The gate holds the core to 120,000 bytes.
- D-027 is Approved — Implementing (brand expression layer + Bro product extension).
- D-025 implementation merge: `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`.
- D-025 closure merge: `9a833339b1d707d6cd8a792e031dd8ca2857d556`.
- D-025 lock merge: `261f85e5b20d726a0ab1f05da84a4dc45a248873`.
- Final audit: `platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md`.
- The D-025 transaction is closed.

### Locked invariants

- The shared core is product-neutral.
- Canonical dependency model: Reference → Semantic → Component → Pattern → Product Extension.
- Theme, state, density, platform, locale, accessibility, and motion preference are orthogonal dimensions.
- Controlled exceptions are governed bypasses, not a normal layer.
- Generated portal, catalog, and design-tool views are not sources of truth.
- Armenian and English are canonical languages.
- Changes to D-025 require governed change control and explicit Owner approval.

### Exact next work

Remediation of the 2026-10-07 zero-trust audit continues in phases (workflow security, bilingual completion, Owner decisions). D-027 needs the D-025 mapping and its first real consumer before it can lock. After that, the Owner selects the next ecosystem priority.

<!-- END: MENQ_STANDARD_AI_WORKING_CONTEXT -->