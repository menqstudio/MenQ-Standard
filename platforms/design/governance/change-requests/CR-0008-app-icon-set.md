# CR-0008 — App icon and favicon set / App icon-ների և favicon-ի հավաքածու

```json
{
  "id": "CR-0008",
  "title": {"hy": "App icon-ների և favicon-ի հավաքածու", "en": "App icon and favicon set"},
  "class": "compatible-implementation",
  "status": "implementing",
  "proposer": "AI collaborator (Claude), design-system gap review 2026-10-08",
  "proposerOwnerId": null,
  "approvals": [
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-08", "evidence": "Owner approved the gap-review order (step 3: favicon / app icon set)"}
  ],
  "affectedAssets": ["menq.design.spec.brand-expression.v1"],
  "decision": "D-027",
  "risk": "R1",
  "consumerEvidencePlan": "MenQ Webpage serves the set (favicon.ico, icon.svg, apple-icon, manifest) and its CI verifies the files are reachable.",
  "migrationPlan": "None: additive assets.",
  "rollback": "Revert the implementing PR.",
  "evidencePlan": "Asset records with SHA-256 checked by validate_brand_expression.py; rendered preview at 16–512 px.",
  "targetRelease": "none (brand expression layer)",
  "pullRequests": [25],
  "mergeEvidence": ["PR #25 merged at e48d230 on 2026-10-08 01:26 +04:00 (2026-10-07 21:26 UTC)"],
  "closure": null,
  "closureBlockedBy": ["evidencePlan: no rendered preview at 16-512 px is recorded in this repository (the icon files exist at 16/32/48, 180, 192 and 512 px and their asset records verify)", "consumerEvidencePlan: nothing in this repository shows that MenQ Webpage serves the set or that its CI checks the files are reachable"]
}
```

## Հայերեն

### Խնդիր

Չկար favicon և app icon՝ պաշտոնական Q մարկից. Webpage-ը օգտագործում էր Next.js-ի default favicon-ը։

### Ցանկալի արդյունք

`assets/Icons/`՝ SVG master, maskable master, `favicon.ico` (16/32/48), Apple touch icon 180, PWA 192/512 և maskable 512, asset record-ներով։

### Scope և ազդեցություն

Միայն նոր asset-ներ։ Token-ները և կոմպոնենտները չեն փոխվում։

### Այլընտրանքներ

Թափանցիկ ֆոնով Q՝ մերժվեց, քանի որ 16px-ում և բաց tab-երում cyan գծերը վատ են երևում։

### Migration և rollback

Migration պետք չէ։ Rollback՝ PR-ի revert։

### Փակման վիճակ (2026-10-09, CR-0012)

Բաց է։ Աշխատանքը merge է եղել (PR #25՝ `e48d230`). asset record-ների SHA-256-ը համընկնում է, `validate_brand_expression.py`-ը GREEN է (2026-10-09)։ Փակմանը խանգարում է. (1) 16–512 px rendered preview-ի գրառում repository-ում չկա (icon ֆայլերը կան 16/32/48, 180, 192 և 512 px չափերով), (2) ոչինչ ցույց չի տալիս, որ MenQ Webpage-ը մատուցում է հավաքածուն, կամ որ նրա CI-ը ստուգում է ֆայլերի հասանելիությունը։

## English

### Problem

There was no favicon or app icon made from the official Q mark; Webpage served the Next.js default favicon.

### Desired outcome

`assets/Icons/`: SVG master, maskable master, `favicon.ico` (16/32/48), Apple touch icon 180, PWA 192/512 and maskable 512, with asset records.

### Scope and impact

New assets only. Tokens and components do not change.

### Alternatives

A Q on a transparent background was rejected: at 16 px and on light tabs the cyan strokes read poorly.

### Migration and rollback

No migration is needed. Rollback: revert the PR.

### Closure status (2026-10-09, CR-0012)

Open. The work is merged (PR #25 at `e48d230`); the asset-record SHA-256 values match and `validate_brand_expression.py` is GREEN (2026-10-09). Closure is blocked by: (1) no rendered preview at 16–512 px is recorded in the repository (the icon files exist at 16/32/48, 180, 192 and 512 px); (2) nothing shows that MenQ Webpage serves the set or that its CI checks the files are reachable.

<!-- END: CR-0008 -->
