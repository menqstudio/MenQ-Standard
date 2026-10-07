# CR-0001 — D-025 evidence correction / D-025 ապացույցի ուղղում

```json
{
  "id": "CR-0001",
  "title": {"hy": "D-025 ապացույցի ուղղում", "en": "D-025 evidence correction"},
  "class": "compatible-implementation",
  "status": "closed",
  "proposer": "AI collaborator (Claude), 2026-10-07 zero-trust audit",
  "proposerOwnerId": null,
  "approvals": [
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-07", "evidence": "Owner decision in the project conversation: correct the evidence and make it permanent"}
  ],
  "affectedAssets": [
    "menq.design.consumer.catalog",
    "menq.design.consumer.release-console",
    "menq.design.validator.validate-consumers",
    "menq.design.workflow.design-platform-preview-release",
    "menq.design.spec.adoption.v1"
  ],
  "decision": "D-025",
  "risk": "R2",
  "consumerEvidencePlan": "MenQ Webpage becomes the first real consumer with independent evidence; the Owner selects the second.",
  "migrationPlan": "None: no public package API changes.",
  "rollback": "Revert PR #15; the readiness record keeps its historical fields.",
  "evidencePlan": "Platforms validator requires the evidence correction; preview-release pipeline GREEN with M2 pilots; permanent release design-platform-v0.1.0-next.0.",
  "targetRelease": "design-platform-v0.1.0-next.0",
  "pullRequests": [15],
  "closure": {"date": "2026-10-07", "evidence": ["PR #15 merged at 7da80a9", "CI GREEN: Platforms Integrity, Phase A, Preview Release, Foundation, Markdown Inventory", "Permanent release design-platform-v0.1.0-next.0"]}
}
```

## Հայերեն

### Խնդիր

D-025-ի lock evidence-ը հղվում էր ժամկետանց workflow artifact-ի, իսկ repo-ի ներսի երկու consumer-ի M3/M4 grade-ը self-attested էր։

### Ցանկալի արդյունք

Մշտական release evidence, ազնիվ consumer grade (M2) և իրական consumer-ի բաց պարտավորություն՝ առանց պատմությունը վերագրելու։

### Scope և ազդեցություն

Consumer build-եր, `validate_consumers.py`, readiness record, Platforms validator։ Public package API-ն, accessibility-ն և localization-ը չեն փոխվում։

### Այլընտրանքներ

Միայն գրանցել իրականությունը՝ մերժվեց, քանի որ evidence-ը կմնար ժամկետանց։ Թողնել ինչպես կա՝ մերժվեց։

### Migration և rollback

Migration պետք չէ։ Rollback՝ PR #15-ի revert։

## English

### Problem

D-025's lock evidence pointed to an expired workflow artifact, and the M3/M4 grades of the two in-repo consumers were self-attested.

### Desired outcome

Permanent release evidence, an honest consumer grade (M2) and an open real-consumer obligation, without rewriting history.

### Scope and impact

Consumer builds, `validate_consumers.py`, the readiness record and the Platforms validator. The public package API, accessibility and localization do not change.

### Alternatives

Only recording the facts was rejected because the evidence would stay expired. Leaving it as it is was rejected.

### Migration and rollback

No migration is needed. Rollback: revert PR #15.

<!-- END: CR-0001 -->
