# CR-0003 — Brand custom-properties consumption artifact / Brand custom property-ների consumption artifact

```json
{
  "id": "CR-0003",
  "title": {"hy": "Brand custom property-ների consumption artifact", "en": "Brand custom-properties consumption artifact"},
  "class": "compatible-implementation",
  "status": "closed",
  "proposer": "AI collaborator (Claude), MenQ Webpage adoption",
  "proposerOwnerId": null,
  "approvals": [
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-07", "evidence": "Owner instruction in the project conversation: make MenQ Webpage the real D-025 consumer"}
  ],
  "affectedAssets": [
    "menq.design.build.brand-tokens",
    "menq.design.generated.tokens-vars-css",
    "menq.design.spec.brand-expression.v1"
  ],
  "decision": "D-027",
  "risk": "R1",
  "consumerEvidencePlan": "MenQ Webpage vendors tokens.vars.css pinned by commit and SHA-256 and proves token parity and runtime rendering in its own CI.",
  "migrationPlan": "None: additive output; tokens.css is unchanged.",
  "rollback": "Revert the implementing PR; consumers keep their pinned copy.",
  "evidencePlan": "build_brand_tokens.py --check covers the new output; brand expression and governance validators GREEN.",
  "targetRelease": "none (brand expression layer)",
  "pullRequests": [18, 19],
  "closure": {"date": "2026-10-08", "evidence": ["PR #18 merged at 493a3df with all CI checks GREEN", "menqstudio/webpage PR #2 vendors tokens.vars.css pinned to 493a3df (SHA-256 1e377a93…f3d7)", "Webpage CI run 37680568760 GREEN: token parity 1632/1632 in 8 contexts; runtime evidence 14 page×theme checks; axe 0 critical"]}
}
```

## Հայերեն

### Խնդիր

`tokens.css`-ը պարունակում է նաև type-style class-եր (`.hero`, `.h1`, `.body`…) և `@font-face`։ MenQ Webpage-ը օգտագործում է `hero` class-ը, ուստի ամբողջ ֆայլը import անելը կփոխեր կայքի տեսքը, իսկ font-երի relative ճանապարհները կկոտրվեին։

### Ցանկալի արդյունք

Generator-ը արտադրում է նաև `tokens.vars.css`՝ նույն custom property-ները, նույն theme selector-ներով, առանց class-երի և font-երի։

### Scope և ազդեցություն

Միայն նոր generated ֆայլ և generator-ի փոփոխություն։ `tokens.css`-ը, token source-ը, accessibility-ն և localization-ը չեն փոխվում։

### Այլընտրանքներ

Webpage-ում ձեռքով կտրել ֆայլը՝ մերժվեց, քանի որ pinned SHA-ն upstream-ի հետ չէր համընկնի։ Հեռացնել class-երը `tokens.css`-ից՝ մերժվեց, քանի որ self-hosted էջերը դրանք օգտագործում են։

### Migration և rollback

Migration պետք չէ։ Rollback՝ PR-ի revert։

## English

### Problem

`tokens.css` also carries type-style classes (`.hero`, `.h1`, `.body`…) and `@font-face`. MenQ Webpage uses a `hero` class, so importing the whole file would change the site, and the relative font paths would break.

### Desired outcome

The generator also emits `tokens.vars.css`: the same custom properties under the same theme selectors, without classes or fonts.

### Scope and impact

Only a new generated file and a generator change. `tokens.css`, the token source, accessibility and localization do not change.

### Alternatives

Trimming the file by hand inside Webpage was rejected because the pinned SHA would no longer match upstream. Removing the classes from `tokens.css` was rejected because self-hosted pages use them.

### Migration and rollback

No migration is needed. Rollback: revert the PR.

<!-- END: CR-0003 -->
