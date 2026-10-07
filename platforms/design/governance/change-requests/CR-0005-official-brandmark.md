# CR-0005 — Official BrandMark from the MenQ logo / Պաշտոնական BrandMark՝ MenQ լոգոյից

```json
{
  "id": "CR-0005",
  "title": {"hy": "Պաշտոնական BrandMark՝ MenQ լոգոյից", "en": "Official BrandMark from the MenQ logo"},
  "class": "contract-extension",
  "status": "approved",
  "proposer": "MenQ Owner report, implemented by the AI collaborator (Claude)",
  "proposerOwnerId": null,
  "approvals": [
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-08", "evidence": "Owner in the project conversation: the BrandMark is wrong, the brand mark is the logo he supplied"}
  ],
  "affectedAssets": ["menq.design.spec.brand-expression.v1", "menq.design.extension.bro"],
  "decision": "D-027",
  "risk": "R2",
  "consumerEvidencePlan": "MenQ Webpage replaces its BrandMark with the same mark in a follow-up PR with CI runtime evidence; the claude.ai Design System mirror is updated.",
  "migrationPlan": "BrandMark props are unchanged (compact, admin, tag); the visual changes from the azure pill to the official mark. SVG file names are kept, so references keep working.",
  "rollback": "Revert the implementing PR.",
  "evidencePlan": "Brand expression validator GREEN (asset sha256, bundle syntax, components, var resolution); rendered comparison against the official logo.",
  "targetRelease": "none (brand expression layer)",
  "pullRequests": [],
  "closure": null
}
```

## Հայերեն

### Խնդիր

`BrandMark` կոմպոնենտը և `menq-wordmark-*`/`menq-q-mark-*` SVG-ները ցույց էին տալիս Inter տառատեսակով «Men» և ազուր pill-ի մեջ power նշան։ Owner-ը հաստատեց, որ դա սխալ է. MenQ-ի մարկը իր տրամադրած լոգոն է՝ կլորացված «Men» և neon power-ring Q։

### Ցանկալի արդյունք

Պաշտոնական լոգոյից պատրաստված վեկտոր մարկ՝ «Men»-ը trace արված, Q-ն կառուցված լոգոյի չափված երկրաչափությամբ (կենտրոն, շառավիղ 199.5, ներքևի բացվածք ≈63°, ուղղահայաց գիծ)։ Նույն մարկը `BrandMark`-ում (inline SVG) և չորս SVG ֆայլերում։ Ավելացվեց նաև Բրոյի avatar-ի 1024×1024 master-ը։

### Scope և ազդեցություն

BrandMark-ի props-ը չեն փոխվում, տեսքը փոխվում է։ Accessibility՝ `role="img"` և `aria-label` պահպանված են։ Localization չի ազդվում։

### Այլընտրանքներ

PNG լոգոն օգտագործել ամենուր՝ մերժվեց, քանի որ փոքր չափերում և բաց ֆոնին պետք է վեկտոր և theme-ին հարմարվող «Men»։

### Migration և rollback

Ֆայլերի անունները պահպանված են։ Rollback՝ PR-ի revert։

## English

### Problem

The `BrandMark` component and the `menq-wordmark-*`/`menq-q-mark-*` SVGs showed an Inter "Men" with a power symbol inside an azure pill. The Owner confirmed this is wrong: the MenQ mark is the logo he supplied, a rounded "Men" with the neon power-ring Q.

### Desired outcome

A vector mark made from the official logo: "Men" traced, the Q constructed to the logo's measured geometry (centre, radius 199.5, bottom gap ≈63°, vertical stem). The same mark in `BrandMark` (inline SVG) and in the four SVG files. The 1024×1024 master of Bro's avatar is added too.

### Scope and impact

BrandMark props do not change; its look does. Accessibility: `role="img"` and `aria-label` are kept. Localization is not affected.

### Alternatives

Using the PNG logo everywhere was rejected: small sizes and light grounds need a vector and a theme-aware "Men".

### Migration and rollback

File names are kept. Rollback: revert the PR.

<!-- END: CR-0005 -->
