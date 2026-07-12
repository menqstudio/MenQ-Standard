# MenQ Standard — AI Working Context

> Living continuity document for AI collaborators.  
> AI համագործակիցների կենդանի շարունակականության փաստաթուղթ։

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Working  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-13  
**Canonical repository:** `https://github.com/menqstudio/MenQ-Standard`

## Հայերեն

### Պարտադիր startup workflow

Յուրաքանչյուր նոր AI session մինչև substantive աշխատանք պարտավոր է active branch/ref-ում enumerate և ամբողջությամբ կարդալ բոլոր tracked `.md` files-ը, իսկ active PR-ի դեպքում՝ metadata, changed files, diff, review threads և checks։ Պարտադիր օրենքը՝ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`։

### Human–AI սկզբունք

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն MenQ architect և engineering teammate է։ Final authority-ն և accountability-ն մարդունն են։ AI-ն չի self-approve անում և canonical truth չի lock անում։

### Ընթացիկ canonical վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 — merged և canonical։
- D-025 — Locked և GREEN։
- D-026 — Locked և machine-enforced։
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

Owner-ը ընտրում է MenQ Standard-ի հաջորդ ecosystem priority-ն և բացում առանձին decision transaction։

---

## English

### Required startup workflow

Before substantive work, every AI session must enumerate and completely read all tracked `.md` files on the active branch/ref and, for an active PR, read metadata, changed files, diff, review threads, and checks. The mandatory law is `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`.

### Human–AI principle

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI does not self-approve or lock canonical truth.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- D-024 is merged and canonical.
- D-025 is Locked and GREEN.
- D-026 is Locked and machine-enforced.
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

The Owner selects the next MenQ Standard ecosystem priority and opens a separate decision transaction.

<!-- END: MENQ_STANDARD_AI_WORKING_CONTEXT -->