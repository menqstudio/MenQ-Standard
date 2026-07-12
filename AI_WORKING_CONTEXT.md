# MenQ Standard — AI Working Context

> Living continuity document for AI collaborators.  
> AI համագործակիցների կենդանի շարունակականության փաստաթուղթ։

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Working  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-12  
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
- D-025 — `Approved — Implementing`, ոչ `Locked`։
- D-026 — Locked և machine-enforced։
- Working branch — `d-025-design-platform-architecture-v1`։
- Draft PR #3 — open, Draft, unmerged։
- Parts 1–11 baseline, Part 12 validation architecture, Part 13 documentation/catalog/design-tool architecture և Part 14 governance/contribution/change-lifecycle architecture canonical են։

### Architecture invariants

- Shared core-ը product-neutral է։
- Canonical dependency model-ը՝ Reference → Semantic → Component → Pattern → Product Extension։
- Theme, state, density, platform, locale, accessibility և motion preference-ը orthogonal dimensions են։
- Controlled exceptions-ը governed bypass են, ոչ normal layer։
- Portal, catalog և design-tool integration-ը generated/governed views են, ոչ source of truth։
- Unowned canonical asset-ը RED governance defect է։
- High-risk կամ breaking change-ի self-approval-ը արգելված է։
- Merge-ը առանձին authority action է, ոչ GREEN CI-ի ավտոմատ հետևանք։
- Armenian և English canonical languages են։

### Հաջորդ հստակ աշխատանք

1. Part 16 — Canonical Specification Index and Implementation Package Plan։
2. Canonical specification index և implementation package plan։
3. D-025 completeness audit, validator design և PR #3 review։
4. GREEN evidence և Owner review։

---

## English

### Required startup workflow

Before substantive work, every AI session must enumerate and completely read all tracked `.md` files on the active branch/ref and, for the active PR, read metadata, changed files, diff, review threads, and checks. The mandatory law is `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`.

### Human–AI principle

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI does not self-approve or lock canonical truth.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- D-024 is merged and canonical.
- D-025 is `Approved — Implementing`, not `Locked`.
- D-026 is Locked and machine-enforced.
- Working branch: `d-025-design-platform-architecture-v1`.
- Draft PR #3 is open, Draft, and unmerged.
- Parts 1–11 baseline, Part 12 validation architecture, Part 13 documentation/catalog/design-tool architecture, and Part 14 governance/contribution/change-lifecycle architecture are canonical.

### Architecture invariants

- Shared core is product-neutral.
- Canonical dependency model: Reference → Semantic → Component → Pattern → Product Extension.
- Theme, state, density, platform, locale, accessibility, and motion preference are orthogonal dimensions.
- Controlled exceptions are governed bypasses, not a normal layer.
- The portal, catalog, and design-tool integration are generated/governed views, not sources of truth.
- An unowned canonical asset is a RED governance defect.
- Self-approval is prohibited for high-risk or breaking changes.
- Merge is a separate authority action, not an automatic consequence of green CI.
- Armenian and English are canonical languages.

### Exact next work

1. Part 16 — Canonical Specification Index and Implementation Package Plan.
2. Canonical specification index and implementation package plan.
3. D-025 completeness audit, validator design, and PR #3 review.
4. GREEN evidence and Owner review.

<!-- END: MENQ_STANDARD_AI_WORKING_CONTEXT -->