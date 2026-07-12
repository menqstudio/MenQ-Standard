# MenQ Standard — AI Working Context

> Living continuity document for AI collaborators.  
> AI համագործակիցների կենդանի շարունակականության փաստաթուղթ։

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Working  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-12  
**Canonical repository:** `https://github.com/menqstudio/MenQ-Standard`

## Հայերեն

### Պարտադիր startup workflow

Նոր AI collaborator-ը աշխատանքից առաջ կարդում է՝

1. `README.md`
2. `PROJECT_CONTEXT.md`
3. `COLLABORATION_STYLE.md`
4. `AI_WORKING_CONTEXT.md`
5. `DECISION_INDEX.md`
6. `DECISIONS.md`
7. `CHANGELOG.md`
8. `ROADMAP.md`
9. `foundation/README.md`
10. `foundation/PROJECT_CONTEXT.md`
11. `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`
12. համապատասխան platform/chapter context-ը
13. `NEXT_CHAT_HANDOFF.md`, եթե current է

Repository-ի հասցեն և արդեն documented persistent rules-ը Owner-ից կրկին չեն հարցվում։

### Human–AI սկզբունք

> Մարդը միտք է բերում։  
> AI-ն օգնում է։  
> Մարդը որոշում է։  
> Ստանդարտը պահպանում է։

AI-ն MenQ architect և engineering teammate է։ Final authority-ն և accountability-ն մարդունն են։ AI-ն չի կարող self-approve անել կամ canonical truth-ը ինքնուրույն lock անել։

### Ընթացիկ canonical վիճակ

- Foundation v1 — Locked և GREEN։
- `D-024 — Platforms Architecture v1` — merged և canonical։
- `D-025 — MenQ Design Platform Architecture v1` — `Approved — Implementing`, ոչ `Locked`։
- Working branch — `d-025-design-platform-architecture-v1`։
- Draft PR — `#3`, merge չի արվում մինչև completeness, synchronization, validation և Owner approval։

### Owner-approved Design Platform baseline

Հաստատված workshop baseline-ը պահպանված է `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`-ում և ներառում է՝

- Foundation → Brand Core → Design Platform Core → Product Design Layers սահմանը,
- governed token concerns և orthogonal dimensions,
- canonical token source և generation pipeline,
- primitives,
- behavior-first components,
- reusable patterns,
- themes/modes/product expression separation,
- accessibility,
- Armenian + English canonical localization և on-demand locale packs,
- content architecture,
- governed assets,
- motion architecture,
- package, release, versioning, migration և compatibility architecture։

Theme, state, density, platform, locale, accessibility և motion preference-ը token layers չեն։ Controlled exceptions-ը normal token layer չեն։ Detailed systems-ը առանձին canonical specifications են, իսկ D-025-ը architecture boundary-ն է։

### Հաջորդ հստակ աշխատանք

1. Կտոր 12 — Validation, CI, Conformance և Quality Gates Architecture։
2. Documentation portal, catalog և design-tool integration։
3. Governance, contribution, ownership և change-request lifecycle։
4. Product adoption, maturity model և two-consumer validation plan։
5. Canonical specification index և implementation package plan։
6. D-025 completeness audit, validator design և Draft PR #3 review։
7. Canonical synchronization, GREEN evidence և Owner review։

---

## English

### Required startup workflow

Before work, a new AI collaborator reads the root startup set, the relevant platform/chapter context, and the current `NEXT_CHAT_HANDOFF.md`. Do not ask the Owner again for the repository address or persistent rules already documented in the repository.

### Human–AI principle

> Humans bring ideas.  
> AI assists.  
> Humans decide.  
> Standards preserve.

AI works as the MenQ architect and engineering teammate. Final authority and accountability remain human. AI may not self-approve or independently lock canonical truth.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- `D-024 — Platforms Architecture v1` is merged and canonical.
- `D-025 — MenQ Design Platform Architecture v1` is `Approved — Implementing`, not `Locked`.
- Working branch: `d-025-design-platform-architecture-v1`.
- Draft PR: `#3`; it must remain unmerged until completeness, synchronization, validation, and Owner approval are complete.

### Owner-approved Design Platform baseline

The approved workshop baseline is preserved in `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`. It covers the ecosystem boundary, governed token concerns and orthogonal dimensions, canonical token source and generation pipeline, primitives, behavior-first components, reusable patterns, themes/modes/product expression separation, accessibility, Armenian and English canonical localization plus on-demand locales, content architecture, governed assets, motion, and package/release/versioning/migration/compatibility architecture.

Theme, state, density, platform, locale, accessibility, and motion preference are not token layers. Controlled exceptions are not a normal token layer. Detailed systems belong in separate canonical specifications; D-025 remains the architecture boundary.

### Exact next work

1. Part 12 — Validation, CI, Conformance, and Quality Gates Architecture.
2. Documentation portal, catalog, and design-tool integration.
3. Governance, contribution, ownership, and change-request lifecycle.
4. Product adoption, maturity model, and two-consumer validation plan.
5. Canonical specification index and implementation package plan.
6. D-025 completeness audit, validator design, and Draft PR #3 review.
7. Canonical synchronization, GREEN evidence, and Owner review.

<!-- END: MENQ_STANDARD_AI_WORKING_CONTEXT -->