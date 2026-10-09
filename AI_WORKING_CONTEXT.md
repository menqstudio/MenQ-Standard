# MenQ Standard — AI Working Context

> Living continuity document for AI collaborators.  
> AI համագործակիցների կենդանի շարունակականության փաստաթուղթ։

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Working  
**Last synchronized / Վերջին համաժամեցում:** 2026-10-09  
**Canonical repository:** `https://github.com/menqstudio/MenQ-Standard`

## Հայերեն

### Պարտադիր startup workflow

Յուրաքանչյուր նոր AI session մինչև substantive աշխատանք պարտավոր է active branch/ref-ում ամբողջությամբ կարդալ session-read core-ը՝ `foundation/ai-collaboration/SESSION_READ_MANIFEST.json`-ի `core` ցանկը, որևէ directory-ում աշխատելուց առաջ՝ նաև այդ directory-ի area-ի ֆայլերը, իսկ active PR-ի դեպքում՝ metadata, changed files, diff, review threads և checks։ Պարտադիր օրենքը՝ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md` (`D-026`, `D-028`)։

### Human–AI սկզբունք

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն MenQ architect և engineering teammate է։ Final authority-ն և accountability-ն մարդունն են։ AI-ն չի self-approve անում և canonical truth չի lock անում։

### Ընթացիկ canonical վիճակ

Ընթացիկ վիճակի միակ ամբողջական ցանկը [`README.md`](README.md)-ի `Status` բաժինն է․ այս ֆայլը այն չի կրկնում։

### Locked invariants

- Shared core-ը product-neutral է։
- Canonical dependency model-ը՝ Reference → Semantic → Component → Pattern → Product Extension։
- Theme, state, density, platform, locale, accessibility և motion preference-ը orthogonal dimensions են։
- Controlled exceptions-ը governed bypass են, ոչ normal layer։
- Generated portal/catalog/design-tool views-ը source of truth չեն։
- Armenian և English canonical languages են։
- D-025 փոփոխությունը պահանջում է governed change control և explicit Owner approval։

### Բաց հարցեր և հաջորդ քայլ

2026-10-07 zero-trust audit-ի remediation-ի 1–6 փուլերը [`CHANGELOG.md`](CHANGELOG.md)-ում գրանցված են ավարտված․ այս ֆայլը մինչև 2026-10-09 ասում էր, որ remediation-ը շարունակվում է։ Բաց հարցերի միակ ցանկը և հաջորդ session-ի առաջին քայլը [`NEXT_CHAT_HANDOFF.md`](NEXT_CHAT_HANDOFF.md)-ում են։

---

## English

### Required startup workflow

Before substantive work, every AI session must read in full, on the active branch/ref, the session-read core, which is the `core` list of `foundation/ai-collaboration/SESSION_READ_MANIFEST.json`; before working in a directory, also the files of that directory's area; and, for an active PR, metadata, changed files, diff, review threads, and checks. The mandatory law is `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md` (`D-026`, `D-028`).

### Human–AI principle

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI does not self-approve or lock canonical truth.

### Current canonical state

The one complete list of the current state is the `Status` section of [`README.md`](README.md); this file does not restate it.

### Locked invariants

- The shared core is product-neutral.
- Canonical dependency model: Reference → Semantic → Component → Pattern → Product Extension.
- Theme, state, density, platform, locale, accessibility, and motion preference are orthogonal dimensions.
- Controlled exceptions are governed bypasses, not a normal layer.
- Generated portal, catalog, and design-tool views are not sources of truth.
- Armenian and English are canonical languages.
- Changes to D-025 require governed change control and explicit Owner approval.

### Open matters and next step

Remediation phases 1–6 of the 2026-10-07 zero-trust audit are recorded complete in [`CHANGELOG.md`](CHANGELOG.md); until 2026-10-09 this file said that remediation continues. The one list of open matters and the first step of the next session are in [`NEXT_CHAT_HANDOFF.md`](NEXT_CHAT_HANDOFF.md).

<!-- END: MENQ_STANDARD_AI_WORKING_CONTEXT -->