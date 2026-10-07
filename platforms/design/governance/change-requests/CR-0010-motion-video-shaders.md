# CR-0010 — Motion, logo power-on, video and shader rules / Շարժում, լոգոյի power-on, վիդեոյի և shader-ների կանոններ

```json
{
  "id": "CR-0010",
  "title": {"hy": "Շարժում, լոգոյի power-on, վիդեոյի և shader-ների կանոններ", "en": "Motion, logo power-on, video and shader rules"},
  "class": "contract-extension",
  "status": "approved",
  "proposer": "AI collaborator (Claude), design-system gap review 2026-10-08",
  "proposerOwnerId": null,
  "approvals": [
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-08", "evidence": "Owner approved the gap-review order (step 5: motion, video guidelines, shaders as optional only)"}
  ],
  "affectedAssets": ["menq.design.spec.brand-expression.v1", "menq.design.generated.tokens-css", "menq.design.generated.tokens-vars-css", "menq.design.generated.tokens-json"],
  "decision": "D-027",
  "risk": "R1",
  "consumerEvidencePlan": "Rendered in Chromium with normal and reduced motion; MenQ Webpage can adopt Reveal and the hero power-on in a later change.",
  "migrationPlan": "Additive: four tokens, one component, a BrandMark prop and documentation. The tokens.json mirror gains a motion group and icon-stroke; existing groups keep their entries.",
  "rollback": "Revert the implementing PR.",
  "evidencePlan": "Brand expression validator GREEN; Chromium test: Reveal reaches opacity 1 after entering the viewport, power-on ends with the ring fully drawn, reduced motion shows final state with no animation; axe 0 violations light and dark.",
  "targetRelease": "none (brand expression layer)",
  "pullRequests": [],
  "closure": null
}
```

## Հայերեն

### Խնդիր

Շարժման համար կային միայն ժամանակի token-ներ և մեկ տող կանոն։ Անվանված pattern-ներ, լոգոյի անիմացիա, վիդեոյի կանոններ և shader-ների սահման չկային։ `tokens.json` mirror-ը բաց էր թողնում շարժման token-ները և `icon-stroke`-ը։

### Ցանկալի արդյունք

Շարժման սկզբունքներ և ժամանակների աղյուսակ, `Reveal` կոմպոնենտ, `BrandMark powerOn`, վիդեոյի կանոններ (WCAG 2.2.2, 2.3.1), shader-ներ՝ միայն optional package։ Mirror-ը ամբողջական է։

### Scope և ազդեցություն

Միայն brand expression շերտը։ Reduced motion-ը պարտադիր է, localization-ը չի ազդվում։

### Այլընտրանքներ

Motion գրադարան (Framer Motion և այլն)՝ մերժվեց. CSS keyframe-ները և token-ները բավարար են և կախվածություն չեն ավելացնում։

### Migration և rollback

Միայն ավելացումներ։ Rollback՝ PR-ի revert։

## English

### Problem

Motion had only duration tokens and a one-line rule. There were no named patterns, no logo animation, no video rules and no shader boundary. The `tokens.json` mirror left out the motion tokens and `icon-stroke`.

### Desired outcome

Motion principles and a timing table, a `Reveal` component, `BrandMark powerOn`, video rules (WCAG 2.2.2, 2.3.1), and shaders only as an optional package. The mirror is complete.

### Scope and impact

Brand expression layer only. Reduced motion is mandatory; localization is not affected.

### Alternatives

A motion library (Framer Motion or similar) was rejected: CSS keyframes and tokens are enough and add no dependency.

### Migration and rollback

Additions only. Rollback: revert the PR.

<!-- END: CR-0010 -->
