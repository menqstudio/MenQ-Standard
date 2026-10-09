# CR-0005 — Official BrandMark from the MenQ logo / Պաշտոնական BrandMark՝ MenQ լոգոյից

```json
{
  "id": "CR-0005",
  "title": {"hy": "Պաշտոնական BrandMark՝ MenQ լոգոյից", "en": "Official BrandMark from the MenQ logo"},
  "class": "contract-extension",
  "status": "implementing",
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
  "pullRequests": [21, 22],
  "mergeEvidence": ["PR #21 merged at 51728c9 on 2026-10-08 00:48 +04:00 (2026-10-07 20:48 UTC)", "PR #22 (Q-mark viewBox fix) merged at c98e5d5 on 2026-10-08 00:52 +04:00 (2026-10-07 20:52 UTC)"],
  "closure": null,
  "closureBlockedBy": ["consumerEvidencePlan (required for class contract-extension): nothing in this repository shows that MenQ Webpage replaced its BrandMark in a follow-up pull request with CI runtime evidence", "consumerEvidencePlan: the claude.ai Design System mirror update cannot be seen from this repository", "evidencePlan: no record of the rendered comparison against the official logo is in the repository", "synchronization: brand-expression/components/Cover/preview.html still draws the replaced mark (an azure disc with a power symbol)"]
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

### Փակման վիճակ (2026-10-09, CR-0012)

Բաց է։ Աշխատանքը merge է եղել (PR #21՝ `51728c9`, PR #22՝ `c98e5d5`), և `validate_brand_expression.py`-ը GREEN է (2026-10-09)։ Փակմանը խանգարում է. (1) repository-ում չկա ապացույց, որ MenQ Webpage-ը փոխել է իր BrandMark-ը հաջորդ PR-ով՝ CI runtime evidence-ով, (2) claude.ai Design System mirror-ի թարմացումը repository-ից չի երևում, (3) պաշտոնական լոգոյի հետ rendered համեմատության գրառում չկա, (4) `components/Cover/preview.html`-ը դեռ նկարում է փոխարինված նշանը (ազուր շրջան power նշանով)։

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

### Closure status (2026-10-09, CR-0012)

Open. The work is merged (PR #21 at `51728c9`, PR #22 at `c98e5d5`) and `validate_brand_expression.py` is GREEN (2026-10-09). Closure is blocked by: (1) nothing in the repository shows that MenQ Webpage replaced its BrandMark in a follow-up pull request with CI runtime evidence; (2) the claude.ai Design System mirror update cannot be seen from the repository; (3) there is no record of the rendered comparison against the official logo; (4) `components/Cover/preview.html` still draws the replaced mark (an azure disc with a power symbol).

<!-- END: CR-0005 -->
