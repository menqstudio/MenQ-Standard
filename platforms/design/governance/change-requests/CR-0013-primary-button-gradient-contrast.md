# CR-0013 — Inverse text taken off the brand gradient in Light / Շրջված տեքստը Light-ում հանվում է բրենդի gradient-ի վրայից

```json
{
  "id": "CR-0013",
  "title": {"hy": "Շրջված տեքստը Light-ում հանվում է բրենդի gradient-ի վրայից (հիմնական Button, Բրոյի avatar)", "en": "Inverse text taken off the brand gradient in Light (primary Button, Bro avatar)"},
  "class": "breaking",
  "status": "proposed",
  "proposer": "AI collaborator (Claude). In the project conversation on 2026-10-09 the Owner delegated the choice of fix to the AI collaborator (\"you decide the button\"); that delegation is not an approval of this change",
  "proposerOwnerId": null,
  "approvals": [],
  "affectedAssets": [
    "menq.design.spec.brand-expression.v1",
    "menq.design.extension.bro",
    "menq.design.validator.validate-brand-expression",
    "menq.design.validator.test-validate-brand-expression"
  ],
  "decision": "D-027",
  "risk": "R2",
  "consumerEvidencePlan": "Consumer inventory on 2026-10-09: no consumer of components/bundle.css or of the Bro bro.css is recorded in this repository. MenQ Webpage is recorded as pinning tokens.vars.css only (d-025-readiness-record.json, 2026-10-08: 'tokens.vars.css @ 493a3df'); this change does not touch tokens.vars.css, tokens.css or tokens.json, so Webpage is not affected. The Bro extension records no real consumer. The claude.ai Design System mirror cannot be seen from this repository. Evidence to collect before closure: (1) the Design Brand Expression Integrity workflow GREEN on the pull request, and the workflow step that runs test_validate_brand_expression.py (added in this change to design-brand-expression.yml) GREEN in GitHub Actions; (2) an axe run of the Button and ChatMessage previews in Light and Dark with zero color-contrast findings; (3) when a product first loads bundle.css, that product's own axe result.",
  "migrationPlan": "No API, prop, class name, token name or token value changes. A consumer that copied or pinned bundle.css before this change keeps the gradient primary Button in Light (2.43:1 at the cyan end) until it takes bundle.css again; no token file has to be re-pinned. bro.css from this change used with an older bundle.css falls back to solid color-action-primary in every theme, because the older bundle does not define --fill-action-primary. There is no deprecation window: the old Light rendering fails the layer's own 4.5:1 rule and is not kept as an option. A product that wants the gradient under inverse text gets it inside [data-theme=\"dark\"] or .section-contrast, where it passes at both ends.",
  "rollback": "Revert the implementing pull request. The gradient returns to the Light primary Button and Bro avatar, and validate_brand_expression.py returns to the 34 token-pair checks only. A consumer that already took the new bundle.css pins the previous commit.",
  "evidencePlan": "validate_brand_expression.py GREEN on the changed tree and RED on the old .btn--primary and .mq-avatar--bro rules, naming the selector, the theme scope, the stop and the ratio; platforms/design/validation/test_validate_brand_expression.py (44 tests) GREEN, with each new check mutated once and every mutant caught (49 mutants, 0 survivors, local run of 2026-10-09); build_brand_tokens.py --check GREEN (no token changed); validate_governance.py, validate_phase_a.py, scripts/validate_foundation.py, scripts/validate_platforms.py, scripts/check_session_read_budget.py and the Markdown inventory check GREEN; the governance pull-request gate GREEN with 'Change-Request: CR-0013'. Not yet evidenced on 2026-10-09: any GitHub Actions run of this change, a screenshot, an axe result. The workflow step is added in this change: design-brand-expression.yml runs the new test file and REQUIRED_WORKFLOW_RUNS of scripts/validate_foundation.py declares it.",
  "targetRelease": "none (brand expression layer)",
  "pullRequests": [],
  "closure": null
}
```

## Հայերեն

### Խնդիր

`components/bundle.css`-ում `.btn--primary`-ն ուներ `background: var(--gradient-brand)` և `color: var(--color-content-inverse)`, իսկ `--gradient-brand`-ը `color-action-primary` → `color-accent` gradient է։ Light theme-ում դա սպիտակ `#ffffff` տեքստ է `#0369a1` → `#06b6d4` gradient-ի վրա. կոնտրաստը ազուր ծայրում 5.93:1 է, cyan ծայրում՝ 2.43:1։ Շերտի կանոնը 4.5:1 է և «սպիտակ տեքստ՝ միայն `color-action-primary`-ի վրա» (`CR-0006`)։ Նույն ձևն ուներ Բրոյի `bro.css`-ի `.mq-avatar--bro` կանոնը։ Dark theme-ում `#020617` տեքստը `#0ea5e9` → `#22d3ee`-ի վրա 7.28:1 և 11.16:1 է և անցնում է։

`validate_brand_expression.py`-ը ստուգում էր 17 token զույգ երկու թեմայում, և դրանցից ոչ մեկը gradient չէր, ուստի validator-ը GREEN էր։ Թերությունը գրանցվել էր `CR-0006`-ի `closureBlockedBy`-ում և `CR-0012`-ում. այս change request-ը այն ուղղում է։

Չափումները կրկնվել են 2026-10-09-ին token source-ի արժեքներից՝ WCAG 2.1 relative luminance բանաձևով։

### Ցանկալի արդյունք

1. Light-ում շրջված տեքստ կրող մակերեսը միագույն `color-action-primary` է (5.93:1), hover-ի և սեղմման ժամանակ՝ `color-action-primary-hover` (7.56:1)։ Dark-ում և `.section-contrast`-ի ներսում gradient-ը մնում է, քանի որ երկու ծայրում էլ անցնում է։
2. Ոչ մի token-ի արժեք չի փոխվում։ `bundle.css`-ի derived բլոկում ավելանում է երկու custom property՝ `--fill-action-primary` և `--fill-action-primary-hover`. դրանք միայն `var()` հղումներ են token-ներին, ինչպես `--gradient-brand`-ը, ուստի գույնի արժեքների միակ աղբյուրը մնում է `source/brand-tokens.source.json`-ը։ `--gradient-brand`-ը չի վերասահմանվում, քանի որ այն օգտագործվում է նաև առանց տեքստի (progress-ի լցոն, timeline-ի նշիչ)։
3. Validator-ն ինքն է գտնում այս դասի թերությունը. կարդում է `bundle.css`-ը և `bro.css`-ը, և ամեն կանոնի համար, որը տեքստի գույնի տակ ֆոն է ներկում, լուծում է ֆոնը token source-ով երեք scope-ում (Light, Dark, `.section-contrast`) և պահանջում 4.5:1՝ gradient-ի ամեն գունային stop-ում։ Չլուծվող stop-ը RED է, ոչ թե բաց թողնված։ 17 զույգը մնում է։

### Scope և ազդեցություն (accessibility, localization, content, design-tool)

**Փոխված CSS կանոններ.** `bundle.css`՝ `.btn--primary` (ֆոնը՝ `var(--fill-action-primary)`), `.btn--primary:hover` (ավելացավ `background: var(--fill-action-primary-hover)`), նոր `.btn--primary:active` կանոն և derived բլոկի երկու նոր property՝ dark scope-երի override-ով։ `bro.css`՝ `.mq-avatar--bro` (ֆոնը՝ `var(--fill-action-primary, var(--color-action-primary))`)։

**Աշխատանքի ընթացքում գտնված և ուղղված երկրորդ թերություն.** `.btn:active { background: var(--color-pressed) }` կանոնը ավելի specific էր, քան `.btn--primary`-ը, ուստի սեղմված հիմնական կոճակը շրջված տեքստը դնում էր կիսաթափանց `color-pressed`-ի վրա. էջի ֆոնի վրա դա 1.23:1 է Light-ում և 1.41:1 Dark-ում։ Նոր `.btn--primary:active` կանոնը սեղմված վիճակին տալիս է hover-ի ֆոնը։

**Class-ի ընտրությունը՝ `breaking`.** `bundle.css` օգտագործող consumer-ը Light-ում տեսնում է այլ հիմնական կոճակ՝ gradient-ի փոխարեն միագույն ազուր։ Baseline-ի §9-ը ասում է՝ «Breaking change-ը ներառում է API, token, visual, behavior, accessibility, runtime, locale կամ package incompatibility», իսկ Part 14-ի §4-ը breaking է համարում «public contract, behavior, package, migration կամ consumer impact փոխող change»-ը։ Փոփոխությունը տեսանելի է և փոխում է այն, ինչ `Button/README.md`-ը խոստանում էր («հիմնականը բրենդի գրադիենտն է»), ուստի ընտրված է ավելի խիստ class-ը։ `emergency`-ն («accessibility blocker») դիտարկվեց և մերժվեց. ոչինչ չի արագացվում, և Owner-ի merge-ը սովորական ճանապարհն է։ Նախադեպը միանշանակ չէ. `CR-0006`-ը, որը նույնպես տեսանելի գույն փոխեց, դասակարգված է `compatible-implementation`։ `decision` դաշտում գրված է `D-027`-ը՝ շերտի կառավարող որոշումը. այս փոփոխության համար առանձին որոշում գրված չէ, և դրա անհրաժեշտությունը Owner-ի հարցն է։

**Ով է ազդվում.** MenQ Webpage-ը՝ ոչ. readiness record-ը գրանցում է, որ այն pin է արել միայն `tokens.vars.css`-ը, որը չի փոխվում։ Ազդվում է միայն այն consumer-ը, որը բեռնում է `components/bundle.css`-ը կամ Բրոյի `bro.css`-ը. այդպիսի consumer repository-ում գրանցված չէ։

**Accessibility.** Հիմնական Button-ը և Բրոյի սկզբնատառով avatar-ը Light-ում 2.43:1-ից դառնում են 5.93:1։ Նկարով Բրոյի avatar-ի 2px օղակը Light-ում նույնպես դառնում է միագույն։

**Չուղղված, գրանցված.** `card--brand`-ը տեքստի տակ դնում է `gradient-brand-soft`-ը։ Քարտի սեփական տեքստը (`color-content-primary`) Light-ում 15.43:1 և 18.39:1 է, բայց նրա ներսում դրված `color-content-muted` տեքստը (օրինակ՝ `field-label`-ը `Card/preview.html`-ում) Light-ում 3.64:1 է ազուր ծայրում և 4.34:1 cyan ծայրում։ Դա այլ կանոն է (muted տեքստ երանգավորված մակերեսի վրա), validator-ը այն չի տեսնում, և այս change request-ը այն չի ուղղում։

**Localization, content, design-tool.** Չեն ազդվում։ `components/index.d.ts`-ը և `bundle.js`-ը չեն փոխվել։

### Այլընտրանքներ

- Light-ում gradient-ի cyan ծայրը մգացնել (`color-accent`-ի արժեքը փոխել)՝ մերժվեց. token-ի արժեքի փոփոխությունը կազդեր `tokens.vars.css`-ի վրա, այսինքն՝ MenQ Webpage-ի, և cyan accent-ի վրա ամենուր։
- `--gradient-brand`-ը Light-ում վերասահմանել որպես միագույն՝ մերժվեց. gradient-ը օգտագործվում է նաև առանց տեքստի (`mq-metric-fill`, `mq-progress`, timeline-ի նշիչ), և դրանք կկորցնեին իրենց տեսքը առանց պատճառի։
- Light-ում տեքստը դարձնել մուգ (`#020617`) gradient-ի վրա՝ մերժվեց. չափվածը 3.40:1 է ազուր ծայրում և 8.31:1 cyan ծայրում, այսինքն՝ թերությունը միայն կտեղափոխվեր մյուս ծայրը։
- Validator-ի 17 զույգի ցանկին ավելացնել ևս մեկ զույգ (`color-content-inverse` / `color-accent`)՝ մերժվեց որպես միակ միջոց. ցանկը չի կարող անվանել այն զույգը, որի մասին ոչ ոք չի մտածել, իսկ stylesheet-ը կարդացող ստուգումը գտնում է նաև հաջորդը։

### Migration և rollback

API, prop, class և token չեն փոխվում։ Հին `bundle.css` pin արած consumer-ը պահում է հին տեսքը (Light-ում 2.43:1), մինչև նորից վերցնի `bundle.css`-ը. token ֆայլը re-pin անել պետք չէ։ Նոր `bro.css`-ը հին `bundle.css`-ի հետ avatar-ին տալիս է միագույն `color-action-primary` բոլոր թեմաներում (fallback)։ Deprecation window չկա. հին Light տեսքը խախտում է շերտի կանոնը։ Rollback՝ իրականացնող PR-ի revert։

## English

### Problem

In `components/bundle.css`, `.btn--primary` had `background: var(--gradient-brand)` and `color: var(--color-content-inverse)`, and `--gradient-brand` is a gradient from `color-action-primary` to `color-accent`. In the light theme that is white `#ffffff` text on a gradient from `#0369a1` to `#06b6d4`: the contrast is 5.93:1 at the azure end and 2.43:1 at the cyan end. The layer's rule is 4.5:1 and "white text only on `color-action-primary`" (`CR-0006`). The `.mq-avatar--bro` rule of Bro's `bro.css` had the same shape. In the dark theme `#020617` text on `#0ea5e9` → `#22d3ee` is 7.28:1 and 11.16:1, and passes.

`validate_brand_expression.py` checked 17 token pairs in both themes, and none of them was the gradient, so the validator was GREEN. The defect was recorded in the `closureBlockedBy` of `CR-0006` and in `CR-0012`; this change request fixes it.

The measurements were repeated on 2026-10-09 from the values of the token source, with the WCAG 2.1 relative-luminance formula.

### Desired outcome

1. In Light, a surface that carries inverse text is solid `color-action-primary` (5.93:1), and `color-action-primary-hover` on hover and while pressed (7.56:1). In Dark and inside `.section-contrast` the gradient stays, because it passes at both ends.
2. No token value changes. The derived block of `bundle.css` gains two custom properties, `--fill-action-primary` and `--fill-action-primary-hover`; like `--gradient-brand` they are only `var()` references to tokens, so `source/brand-tokens.source.json` stays the only source of colour values. `--gradient-brand` itself is not redefined, because it is also used where there is no text (a progress fill, the timeline marker).
3. The validator finds this class of defect by itself: it reads `bundle.css` and `bro.css`, and for every rule that paints a background under a text colour it resolves the background through the token source in three scopes (Light, Dark, `.section-contrast`) and requires 4.5:1 at every colour stop of a gradient. A stop it cannot resolve is RED, not skipped. The 17 pairs stay.

### Scope and impact (accessibility, localization, content, design-tool)

**CSS rules changed.** `bundle.css`: `.btn--primary` (its background is `var(--fill-action-primary)`), `.btn--primary:hover` (gained `background: var(--fill-action-primary-hover)`), a new `.btn--primary:active` rule, and the two new properties of the derived block with their override for the dark scopes. `bro.css`: `.mq-avatar--bro` (its background is `var(--fill-action-primary, var(--color-action-primary))`).

**A second defect found and fixed during this work.** The rule `.btn:active { background: var(--color-pressed) }` was more specific than `.btn--primary`, so a pressed primary button put inverse text on the translucent `color-pressed`: over the page background that is 1.23:1 in Light and 1.41:1 in Dark. The new `.btn--primary:active` rule gives the pressed state the hover fill.

**Choice of class: `breaking`.** A consumer of `bundle.css` sees a different primary button in Light: solid azure instead of the gradient. §9 of the baseline says "Breaking change includes API, token, visual, behavior, accessibility, runtime, locale, or package incompatibility", and §4 of Part 14 calls breaking "a change to a public contract, behavior, package, migration, or consumer expectation". The change is visible and changes what `Button/README.md` promised ("the primary is the brand gradient"), so the stricter class is chosen. `emergency` ("accessibility-blocking") was considered and rejected: nothing is being expedited, and the Owner's merge is the ordinary path. The precedent is not uniform: `CR-0006`, which also changed a visible colour, is classed `compatible-implementation`. The `decision` field names `D-027`, the decision that governs the layer; no separate decision was written for this change, and whether one is needed is a question for the Owner.

**Who is affected.** Not MenQ Webpage: the readiness record shows that it pinned only `tokens.vars.css`, which does not change. Only a consumer that loads `components/bundle.css` or Bro's `bro.css` is affected; no such consumer is recorded in the repository.

**Accessibility.** The primary Button and Bro's initial avatar go from 2.43:1 to 5.93:1 in Light. The 2px ring of Bro's image avatar becomes solid in Light as well.

**Recorded, not fixed.** `card--brand` puts `gradient-brand-soft` under text. The card's own text (`color-content-primary`) is 15.43:1 and 18.39:1 in Light, but `color-content-muted` text placed inside it (for example the `field-label` in `Card/preview.html`) is 3.64:1 at the azure end and 4.34:1 at the cyan end in Light. That is a different rule (muted text on a tinted surface), the validator cannot see it, and this change request does not fix it.

**Localization, content, design-tool.** Not affected. `components/index.d.ts` and `bundle.js` did not change.

### Alternatives

- Darkening the cyan end of the gradient in Light (changing the value of `color-accent`) was rejected: a token value change would reach `tokens.vars.css`, and so MenQ Webpage, and the cyan accent everywhere.
- Redefining `--gradient-brand` as a solid colour in Light was rejected: the gradient is also used without text (`mq-metric-fill`, `mq-progress`, the timeline marker), and those would lose their look for no reason.
- Making the text dark (`#020617`) on the gradient in Light was rejected: measured, it is 3.40:1 at the azure end and 8.31:1 at the cyan end, so the failure would only move to the other end.
- Adding one more pair (`color-content-inverse` / `color-accent`) to the validator's list of 17 was rejected as the only measure: a list cannot name a pair nobody thought of, while a check that reads the stylesheet also finds the next one.

### Migration and rollback

No API, prop, class or token changes. A consumer that pinned the old `bundle.css` keeps the old look (2.43:1 in Light) until it takes `bundle.css` again; no token file needs re-pinning. The new `bro.css` with an old `bundle.css` gives the avatar solid `color-action-primary` in every theme (the fallback). There is no deprecation window: the old Light look breaks the layer's rule. Rollback: revert the implementing PR.

<!-- END: CR-0013 -->
