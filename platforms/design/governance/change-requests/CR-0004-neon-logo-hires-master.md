# CR-0004 — Neon logo high-resolution master / Neon լոգոյի բարձր լուծաչափի master

```json
{
  "id": "CR-0004",
  "title": {"hy": "Neon լոգոյի բարձր լուծաչափի master", "en": "Neon logo high-resolution master"},
  "class": "compatible-implementation",
  "status": "approved",
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
  "pullRequests": [],
  "closure": null
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

<!-- END: CR-0004 -->
