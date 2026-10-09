# CR-0004 — Neon logo high-resolution master / Neon լոգոյի բարձր լուծաչափի master

```json
{
  "id": "CR-0004",
  "title": {"hy": "Neon լոգոյի բարձր լուծաչափի master", "en": "Neon logo high-resolution master"},
  "class": "compatible-implementation",
  "status": "closed",
  "proposer": "MenQ Owner request, implemented by the AI collaborator (Claude)",
  "proposerOwnerId": null,
  "approvals": [
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-08", "evidence": "Owner supplied the logo in the project conversation and asked to add it to the design system"}
  ],
  "affectedAssets": ["menq.design.spec.brand-expression.v1"],
  "decision": "D-027",
  "risk": "R1",
  "consumerEvidencePlan": "Asset record with SHA-256 checked by validate_brand_expression.py; mirrored into the claude.ai Design System artifact.",
  "migrationPlan": "None: additive asset; menq-logo-neon.png stays.",
  "rollback": "Revert the implementing PR.",
  "evidencePlan": "Brand expression validator GREEN (asset record, sha256, bilingual description).",
  "targetRelease": "none (brand expression layer)",
  "pullRequests": [20],
  "mergeEvidence": ["PR #20 merged at dbf410e on 2026-10-08 00:36 +04:00 (2026-10-07 20:36 UTC)"],
  "closure": {"date": "2026-10-09", "evidence": ["PR #20 merged at dbf410e", "Asset record menq.design.asset.brand.menq-logo-neon-hires in brand-expression/assets/ASSET_RECORDS.json: sha256 matches the file, hy/en description, 1913x720 (re-measured on 2026-10-09)", "validate_brand_expression.py GREEN, run locally on 2026-10-09 on the CR-0012 working tree (base 7b5d0ca)", "platforms/design/CHANGELOG.md entry added by CR-0012", "NOT VERIFIED: the claude.ai Design System mirror named in consumerEvidencePlan cannot be seen from this repository; class compatible-implementation does not require consumer evidence (approval-matrix.json)", "Closure proposed by the AI collaborator in CR-0012; it takes effect when the Owner merges that pull request"]}
}
```

## Հայերեն

### Խնդիր

Պաշտոնական neon լոգոն repository-ում կար միայն փոքր չափով (746×240)։ Մեծ մակերեսների և տպագրության համար պետք է բարձր լուծաչափի master։

### Ցանկալի արդյունք

`assets/Logos/menq-logo-neon-hires.png` (1913×720, թափանցիկ ֆոն)՝ asset record-ով, SHA-256-ով և օգտագործման կանոններով։

### Scope և ազդեցություն

Միայն նոր asset։ Token-ները, կոմպոնենտները, accessibility-ն և localization-ը չեն փոխվում։

### Այլընտրանքներ

Փոխարինել գոյություն ունեցող ֆայլը՝ մերժվեց, որ պատմությունը և գոյություն ունեցող հղումները պահպանվեն։

### Migration և rollback

Migration պետք չէ։ Rollback՝ PR-ի revert։

### Փակման վիճակ (2026-10-09, CR-0012)

Փակված է CR-0012-ով (ուժի մեջ է մտնում, երբ Owner-ը merge անի այդ pull request-ը)։ PR #20-ը merge է եղել `dbf410e`-ով։ `evidencePlan`-ը կատարված է և ստուգվում է repository-ում. asset record-ը, SHA-256-ը և երկլեզու նկարագրությունը կան, `validate_brand_expression.py`-ը GREEN է (գործարկվել է 2026-10-09-ին)։ Չի ստուգվել՝ claude.ai Design System mirror-ը, քանի որ այն repository-ից չի երևում. այս class-ի համար consumer evidence-ը պարտադիր չէ։

## English

### Problem

The repository held the official neon logo only at a small size (746×240). Large surfaces and print need a high-resolution master.

### Desired outcome

`assets/Logos/menq-logo-neon-hires.png` (1913×720, transparent) with an asset record, SHA-256 and usage rules.

### Scope and impact

Only a new asset. Tokens, components, accessibility and localization do not change.

### Alternatives

Replacing the existing file was rejected to preserve history and existing references.

### Migration and rollback

No migration is needed. Rollback: revert the PR.

### Closure status (2026-10-09, CR-0012)

Closed by CR-0012 (in effect when the Owner merges that pull request). PR #20 merged at `dbf410e`. The `evidencePlan` is met and can be checked in the repository: the asset record, SHA-256 and bilingual description exist, and `validate_brand_expression.py` is GREEN (run on 2026-10-09). Not verified: the claude.ai Design System mirror, which cannot be seen from the repository; consumer evidence is not required for this class.

<!-- END: CR-0004 -->
