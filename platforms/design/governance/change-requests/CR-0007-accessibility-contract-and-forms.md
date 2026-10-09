# CR-0007 — Accessibility contract and form components / Մատչելիության պայմանագիր և ձևերի կոմպոնենտներ

```json
{
  "id": "CR-0007",
  "title": {"hy": "Մատչելիության պայմանագիր և ձևերի կոմպոնենտներ", "en": "Accessibility contract and form components"},
  "class": "contract-extension",
  "status": "implementing",
  "proposer": "AI collaborator (Claude), design-system gap review 2026-10-08",
  "proposerOwnerId": null,
  "approvals": [
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-08", "evidence": "Owner approved the gap-review order (step 2: accessibility rule and form components)"}
  ],
  "affectedAssets": ["menq.design.spec.brand-expression.v1", "menq.design.validator.validate-brand-expression"],
  "decision": "D-027",
  "risk": "R1",
  "consumerEvidencePlan": "Components render with zero axe violations in both themes; MenQ Webpage adopts FormRow/Checkbox patterns for its lead form in a later change.",
  "migrationPlan": "FormRow now renders a div with an explicit label (htmlFor) instead of wrapping the control in a label; it requires exactly one child control. Existing props are unchanged.",
  "rollback": "Revert the implementing PR.",
  "evidencePlan": "validate_brand_expression.py GREEN incl. 34 WCAG contrast checks (negative-tested); Chromium render + axe 0 violations, light and dark.",
  "targetRelease": "none (brand expression layer)",
  "pullRequests": [24],
  "mergeEvidence": ["PR #24 merged at cd25a7b on 2026-10-08 01:21 +04:00 (2026-10-07 21:21 UTC)"],
  "closure": null,
  "closureBlockedBy": ["evidencePlan: no Chromium render and no axe result, light or dark, is recorded in this repository", "evidencePlan ('negative-tested'): no test of the 34 contrast checks is in the repository; scripts/ holds tests for the foundation, platforms, inventory and read-budget gates only", "consumerEvidencePlan (required for class contract-extension): no axe result for the components, and nothing shows that MenQ Webpage adopted FormRow or Checkbox"]
}
```

## Հայերեն

### Խնդիր

Մատչելիության կանոնը միայն տեքստով էր գրված, և ոչինչ չէր ստուգում token-ների կոնտրաստը. դրա պատճառով light-ի 4.1:1 զույգը հասավ կայք։ Ձևերի կոմպոնենտներից կային միայն Input-ը և Field-ը. Textarea-ն, Select-ը և FormRow-ը փաստաթուղթ չունեին, Checkbox, Radio և Switch չկային, և error-ը կապված չէր control-ին։

### Ցանկալի արդյունք

Validator-ը ստուգում է 17 տեքստ/ֆոն զույգ երկու թեմայում (≥ 4.5:1)։ `FormRow`-ը կապում է label-ը, hint-ը և error-ը (`aria-describedby`, `aria-invalid`, `role="alert"`)։ Նոր՝ `Checkbox`, `RadioGroup`, `Switch`, փաստաթղթավորված `Textarea`, `Select`, `FormRow`։

### Scope և ազդեցություն

Միայն brand expression շերտը։ Accessibility-ն լավանում է, localization-ը չի ազդվում (label-ները տալիս է օգտագործողը)։

### Այլընտրանքներ

Custom (ոչ native) checkbox/radio՝ մերժվեց, քանի որ native input-ը պահում է ստեղնաշարը, ձևի ուղարկումը և screen reader-ի վարքը։

### Migration և rollback

FormRow-ը հիմա պահանջում է ճիշտ մեկ child control։ Rollback՝ PR-ի revert։

### Փակման վիճակ (2026-10-09, CR-0012)

Բաց է։ Աշխատանքը merge է եղել (PR #24՝ `cd25a7b`), և `validate_brand_expression.py`-ը GREEN է՝ 34 contrast ստուգումով (2026-10-09)։ Փակմանը խանգարում է. (1) repository-ում գրանցված չէ ոչ Chromium render, ոչ axe արդյունք՝ light կամ dark, (2) 34 contrast ստուգման negative test repository-ում չկա, (3) կոմպոնենտների axe արդյունք չկա, և ոչինչ ցույց չի տալիս, որ MenQ Webpage-ը ընդունել է FormRow-ը կամ Checkbox-ը։

## English

### Problem

The accessibility rule existed only as text, and nothing checked token contrast, which is how the light 4.1:1 pair reached the site. The forms set had only Input and Field: Textarea, Select and FormRow were undocumented, Checkbox, Radio and Switch were missing, and the error was not linked to its control.

### Desired outcome

The validator checks 17 text/background pairs in both themes (≥ 4.5:1). `FormRow` links the label, hint and error (`aria-describedby`, `aria-invalid`, `role="alert"`). New: `Checkbox`, `RadioGroup`, `Switch`; documented `Textarea`, `Select`, `FormRow`.

### Scope and impact

Brand expression layer only. Accessibility improves; localization is not affected (the consumer supplies labels).

### Alternatives

Custom (non-native) checkbox/radio was rejected: native inputs keep keyboard, form submission and screen-reader behavior.

### Migration and rollback

FormRow now requires exactly one child control. Rollback: revert the PR.

### Closure status (2026-10-09, CR-0012)

Open. The work is merged (PR #24 at `cd25a7b`) and `validate_brand_expression.py` is GREEN with its 34 contrast checks (2026-10-09). Closure is blocked by: (1) no Chromium render and no axe result, light or dark, is recorded in the repository; (2) no negative test of the 34 contrast checks is in the repository; (3) there is no axe result for the components, and nothing shows that MenQ Webpage adopted FormRow or Checkbox.

<!-- END: CR-0007 -->
