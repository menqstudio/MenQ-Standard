# CR-0006 — Primary action contrast (WCAG AA) / Հիմնական գործողության կոնտրաստ (WCAG AA)

```json
{
  "id": "CR-0006",
  "title": {"hy": "Հիմնական գործողության կոնտրաստ (WCAG AA)", "en": "Primary action contrast (WCAG AA)"},
  "class": "compatible-implementation",
  "status": "approved",
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
  "pullRequests": [],
  "closure": null
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

<!-- END: CR-0006 -->
