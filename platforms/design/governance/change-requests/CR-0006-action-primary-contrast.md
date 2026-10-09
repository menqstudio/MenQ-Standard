# CR-0006 — Primary action contrast (WCAG AA) / Հիմնական գործողության կոնտրաստ (WCAG AA)

```json
{
  "id": "CR-0006",
  "title": {"hy": "Հիմնական գործողության կոնտրաստ (WCAG AA)", "en": "Primary action contrast (WCAG AA)"},
  "class": "compatible-implementation",
  "status": "implementing",
  "proposer": "AI collaborator (Claude), from MenQ Webpage axe evidence",
  "proposerOwnerId": null,
  "approvals": [
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-08", "evidence": "Owner approved fixing the light-theme color-contrast findings in the project conversation"}
  ],
  "affectedAssets": ["menq.design.spec.brand-expression.v1", "menq.design.generated.tokens-css", "menq.design.generated.tokens-vars-css", "menq.design.generated.tokens-json"],
  "decision": "D-027",
  "risk": "R2",
  "consumerEvidencePlan": "MenQ Webpage re-pins tokens.vars.css; its CI axe run must report zero color-contrast findings in the light theme.",
  "migrationPlan": "No API change. Light-theme primary buttons and active states become a deeper azure (#0284c7 → #0369a1, hover #0ea5e9 → #075985). Consumers re-pin the generated file.",
  "rollback": "Revert the implementing PR; consumers keep their pinned copy until they re-pin.",
  "evidencePlan": "Brand generator --check and brand expression validator GREEN; Webpage axe GREEN for color-contrast.",
  "targetRelease": "none (brand expression layer)",
  "pullRequests": [23],
  "mergeEvidence": ["PR #23 merged at 3eb4af2 on 2026-10-08 01:05 +04:00 (2026-10-07 21:05 UTC)"],
  "closure": null,
  "closureBlockedBy": ["evidencePlan and consumerEvidencePlan: nothing in this repository shows that MenQ Webpage re-pinned tokens.vars.css after 3eb4af2, or a Webpage axe run with zero color-contrast findings in the light theme; the only Webpage axe result recorded here (d-025-readiness-record.json, 2026-10-08) is at pin 493a3df, before this change, with 7 serious color-contrast findings", "open defect found on 2026-10-09 (CR-0012): the primary Button renders white text on gradient-brand (color-action-primary to color-accent); in the light theme the cyan end #06b6d4 gives 2.43:1, so the Button does not meet the rule 'white text only on color-action-primary'; validate_brand_expression.py does not check gradient-brand"]
}
```

## Հայերեն

### Խնդիր

Light theme-ում `color-action-primary`-ը (`#0284c7`) սպիտակ տեքստով տալիս է 4.09:1, ինչը WCAG AA-ից ցածր է սովորական տեքստի համար։ MenQ Webpage-ի axe ստուգումը դա գտավ ամեն light էջում (լեզվի switch-ի ակտիվ կոճակ, admin login-ի կոճակ)։

### Ցանկալի արդյունք

Light-ում `color-action-primary` = `#0369a1` (5.9:1), hover = `#075985` (7.5:1)։ Dark theme-ը չի փոխվում։

### Scope և ազդեցություն

Միայն երկու token-ի light արժեք։ Light-ում հիմնական կոճակներն ու ակտիվ վիճակները մի քիչ ավելի մուգ ազուր են դառնում։ Accessibility-ն լավանում է, localization-ը չի ազդվում։

### Այլընտրանքներ

Կոճակների տեքստը մեծացնել 18.66px bold՝ մերժվեց, քանի որ փոքր կոճակները (switch, badge) կմնային սխալ։ Ուղղել միայն Webpage-ում՝ մերժվեց, քանի որ թերությունը բրենդի token-ում է։

### Migration և rollback

API-ն չի փոխվում։ Consumer-ները re-pin են անում generated ֆայլը։ Rollback՝ PR-ի revert։

### Փակման վիճակ (2026-10-09, CR-0012)

Բաց է։ Աշխատանքը merge է եղել (PR #23՝ `3eb4af2`), generator-ի `--check`-ը և `validate_brand_expression.py`-ը GREEN են (2026-10-09)։ Փակմանը խանգարում է. (1) repository-ում չկա ապացույց, որ MenQ Webpage-ը re-pin է արել `tokens.vars.css`-ը `3eb4af2`-ից հետո, կամ որ նրա axe ստուգումը light theme-ում զրո color-contrast գտածո է տվել. այստեղ գրանցված միակ Webpage axe արդյունքը (`d-025-readiness-record.json`, 2026-10-08) `493a3df` pin-ի վրա է՝ այս փոփոխությունից առաջ, 7 serious color-contrast գտածոյով, (2) 2026-10-09-ին գտնված բաց թերություն. հիմնական Button-ը սպիտակ տեքստը դնում է `gradient-brand`-ի վրա (`color-action-primary` → `color-accent`), և light theme-ում cyan ծայրը (`#06b6d4`) տալիս է 2.43:1. validator-ը `gradient-brand`-ը չի ստուգում։

## English

### Problem

In the light theme `color-action-primary` (`#0284c7`) gives 4.09:1 with white text, below WCAG AA for normal text. MenQ Webpage's axe run found it on every light page (active language-switch button, admin login button).

### Desired outcome

Light `color-action-primary` = `#0369a1` (5.9:1), hover = `#075985` (7.5:1). The dark theme does not change.

### Scope and impact

Only the light values of two tokens. Light primary buttons and active states become a slightly deeper azure. Accessibility improves; localization is not affected.

### Alternatives

Enlarging button labels to 18.66px bold was rejected because small controls (switches, badges) would stay wrong. Fixing only inside Webpage was rejected because the defect is in the brand token.

### Migration and rollback

No API change. Consumers re-pin the generated file. Rollback: revert the PR.

### Closure status (2026-10-09, CR-0012)

Open. The work is merged (PR #23 at `3eb4af2`); the generator `--check` and `validate_brand_expression.py` are GREEN (2026-10-09). Closure is blocked by: (1) nothing in the repository shows that MenQ Webpage re-pinned `tokens.vars.css` after `3eb4af2`, or that its axe run reported zero color-contrast findings in the light theme; the only Webpage axe result recorded here (`d-025-readiness-record.json`, 2026-10-08) is at pin `493a3df`, before this change, with 7 serious color-contrast findings; (2) an open defect found on 2026-10-09: the primary Button puts white text on `gradient-brand` (`color-action-primary` → `color-accent`), and in the light theme the cyan end (`#06b6d4`) gives 2.43:1; the validator does not check `gradient-brand`.

<!-- END: CR-0006 -->
