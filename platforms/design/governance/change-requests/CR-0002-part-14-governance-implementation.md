# CR-0002 — Part 14 governance implementation / Part 14 governance-ի իրականացում

```json
{
  "id": "CR-0002",
  "title": {"hy": "Part 14 governance-ի իրականացում", "en": "Part 14 governance implementation"},
  "class": "contract-extension",
  "status": "approved",
  "proposer": "AI collaborator (Claude), 2026-10-07 zero-trust audit",
  "proposerOwnerId": null,
  "approvals": [
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-07", "evidence": "Owner decision in the project conversation: build Part 14 now, Part 13 to backlog"}
  ],
  "affectedAssets": [
    "menq.design.spec.governance.v1",
    "menq.design.validator.validate-governance",
    "menq.design.workflow.design-governance"
  ],
  "decision": "D-025",
  "risk": "R1",
  "consumerEvidencePlan": "Real lifecycle evidence: CR-0001 and CR-0002 run through the lifecycle and the PR gate on their own pull requests.",
  "migrationPlan": "None: governance tooling only.",
  "rollback": "Revert the implementing PR; no package or token changes.",
  "evidencePlan": "Design Governance workflow GREEN; negative tests for unowned assets, missing approvals, self-approval and an unlinked PR.",
  "targetRelease": "none (governance tooling)",
  "pullRequests": [],
  "closure": null
}
```

## Հայերեն

### Խնդիր

Part 14-ը architecture-level ավարտված էր, բայց ownership registry, change-request template, approval matrix-ի enforcement և contribution automation չկար։

### Ցանկալի արդյունք

Ամեն canonical asset ունի owner, ամեն ոչ խմբագրական փոփոխություն ունի change request, approval matrix-ը մեքենայորեն ստուգվում է, իսկ PR-ը առանց CR-ի չի անցնում։

### Scope և ազդեցություն

`platforms/design/governance/`, `validate_governance.py`, `design-governance.yml`։ Package-ները, token-ները, accessibility-ն և localization-ը չեն փոխվում։

### Այլընտրանքներ

Երկու մասն էլ (13 և 14) կառուցել միասին՝ հետաձգվեց Owner-ի որոշմամբ։ Թողնել backlog-ում՝ մերժվեց։

### Migration և rollback

Migration պետք չէ։ Rollback՝ իրականացնող PR-ի revert։

## English

### Problem

Part 14 was complete at the architecture level, but there was no ownership registry, change-request template, approval-matrix enforcement or contribution automation.

### Desired outcome

Every canonical asset has an owner, every non-editorial change has a change request, the approval matrix is machine-checked, and a PR without a CR does not pass.

### Scope and impact

`platforms/design/governance/`, `validate_governance.py`, `design-governance.yml`. Packages, tokens, accessibility and localization do not change.

### Alternatives

Building Parts 13 and 14 together was deferred by Owner decision. Leaving both in the backlog was rejected.

### Migration and rollback

No migration is needed. Rollback: revert the implementing PR.

<!-- END: CR-0002 -->
