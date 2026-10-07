# CR-0009 — Iconography, Accordion, Nav and Tooltip / Իկոնագրություն, Accordion, Nav և Tooltip

```json
{
  "id": "CR-0009",
  "title": {"hy": "Իկոնագրություն, Accordion, Nav և Tooltip", "en": "Iconography, Accordion, Nav and Tooltip"},
  "class": "contract-extension",
  "status": "approved",
  "proposer": "AI collaborator (Claude), design-system gap review 2026-10-08",
  "proposerOwnerId": null,
  "approvals": [
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-08", "evidence": "Owner approved the gap-review order (step 4: iconography rule and Accordion/Nav/Tooltip)"}
  ],
  "affectedAssets": ["menq.design.spec.brand-expression.v1", "menq.design.generated.tokens-css", "menq.design.generated.tokens-vars-css", "menq.design.generated.tokens-json"],
  "decision": "D-027",
  "risk": "R1",
  "consumerEvidencePlan": "Rendered with interaction tests and axe in both themes; MenQ Webpage can replace its FAQ and header navigation with Accordion and Nav in a later change.",
  "migrationPlan": "Additive: four tokens (icon-size-sm/md/lg, icon-stroke) and four components. Button now forwards aria-* and data-* attributes.",
  "rollback": "Revert the implementing PR.",
  "evidencePlan": "Brand expression validator GREEN; Chromium test: accordion aria-expanded toggles, tooltip opens on focus with aria-describedby and closes on Escape; axe 0 violations light and dark.",
  "targetRelease": "none (brand expression layer)",
  "pullRequests": [],
  "closure": null
}
```

## Հայերեն

### Խնդիր

Իկոնների համար կանոն չկար (Webpage-ը օգտագործում է Lucide, բայց չափերն ու հաստությունը ֆիքսված չէին), իսկ Accordion (FAQ), Nav և Tooltip կոմպոնենտներ չկային։

### Ցանկալի արդյունք

Իկոնագրության կանոն՝ Lucide, 24 grid, `--icon-stroke`, `--icon-size-sm/md/lg` token-ներ և `Icon` կոմպոնենտ։ `Accordion`՝ WAI-ARIA disclosure, `Nav`՝ landmark `aria-current`-ով, `Tooltip`՝ focus-ով, Escape-ով և `aria-describedby`-ով։

### Scope և ազդեցություն

Միայն brand expression շերտը։ Accessibility-ն լավանում է, localization-ը չի ազդվում։

### Այլընտրանքներ

Native `details`/`summary` Accordion-ի համար՝ մերժվեց, քանի որ heading-ի կառուցվածքն ու մի բացված բաժնի ռեժիմը ավելի վատ են վերահսկվում։

### Migration և rollback

Միայն ավելացումներ։ Rollback՝ PR-ի revert։

## English

### Problem

There was no icon rule (Webpage uses Lucide, but size and stroke were not fixed), and there were no Accordion (FAQ), Nav or Tooltip components.

### Desired outcome

An iconography rule: Lucide, 24 grid, `--icon-stroke`, `--icon-size-sm/md/lg` tokens and an `Icon` component. `Accordion` with the WAI-ARIA disclosure pattern, `Nav` as a landmark with `aria-current`, `Tooltip` with focus, Escape and `aria-describedby`.

### Scope and impact

Brand expression layer only. Accessibility improves; localization is not affected.

### Alternatives

Native `details`/`summary` for Accordion was rejected: heading structure and single-open mode are harder to control.

### Migration and rollback

Additions only. Rollback: revert the PR.

<!-- END: CR-0009 -->
