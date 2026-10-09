# Change Request Template / Change request-ի ձևանմուշ

**Status / Կարգավիճակ:** Active / Գործող  
**Owner / Պատասխանատու:** MenQ Owner  
**Part / Մաս:** Part 14 — Governance, Contribution, Ownership and Change-Request Lifecycle

## Հայերեն

Պատճենել այս ֆայլը `change-requests/CR-NNNN-<slug>.md` անունով, լրացնել `json` metadata block-ը և երկու լեզվով բաժինները։ `validate_governance.py`-ը ստուգում է metadata-ն, approval matrix-ը և ownership-ը։ PR-ի նկարագրության մեջ գրել `Change-Request: CR-NNNN`։ Խմբագրական (միայն Markdown) փոփոխության դեպքում CR պետք չէ՝ գրել `Change-Class: editorial`։

Metadata դաշտեր՝ `class` (`editorial`, `compatible-implementation`, `contract-extension`, `breaking`, `emergency`), `status` (`proposed`, `approved`, `implementing`, `closed`, `rejected`, `withdrawn`), `affectedAssets` (ID-ներ `ownership-registry.json`-ից), `approvals` (owner ID, անուն, ամսաթիվ, ապացույց), `decision` (`breaking`-ի համար պարտադիր), `consumerEvidencePlan`, `migrationPlan`, `rollback`, `evidencePlan`, `pullRequests`, `closure`։

Ըստ ցանկության դաշտեր (ավելացվել են `CR-0012`-ով, validator-ը դրանք չի պահանջում)՝ `mergeEvidence` (merge եղած pull request-ները՝ commit-ով և ամսաթվով) և `closureBlockedBy` (ինչ evidence է պակասում, երբ աշխատանքը merge է եղել, բայց change request-ը դեռ չի կարող փակվել. այդ դեպքում `closure`-ը մնում է `null`)։ Owner-ի հաստատմանը սպասող change request-ի `status`-ը `proposed` է, իսկ `approvals`-ը՝ դատարկ ցանկ. approval-ը գրանցվում է միայն այն բանից հետո, երբ Owner-ը այն տվել է։

## English

Copy this file to `change-requests/CR-NNNN-<slug>.md`, fill in the `json` metadata block and both language sections. `validate_governance.py` checks the metadata, the approval matrix and ownership. Put `Change-Request: CR-NNNN` in the PR description. An editorial (Markdown-only) change needs no CR; write `Change-Class: editorial` instead.

Metadata fields: `class` (`editorial`, `compatible-implementation`, `contract-extension`, `breaking`, `emergency`), `status` (`proposed`, `approved`, `implementing`, `closed`, `rejected`, `withdrawn`), `affectedAssets` (IDs from `ownership-registry.json`), `approvals` (owner ID, name, date, evidence), `decision` (required for `breaking`), `consumerEvidencePlan`, `migrationPlan`, `rollback`, `evidencePlan`, `pullRequests`, `closure`.

Optional fields (added by `CR-0012`; the validator does not require them): `mergeEvidence` (the merged pull requests, with commit and date) and `closureBlockedBy` (the evidence still missing when the work is merged but the change request cannot close yet; `closure` then stays `null`). A change request awaiting the Owner's approval has `status` `proposed` and an empty `approvals` list; an approval is recorded only after the Owner has given it.

## Template / Ձևանմուշ

````text
# CR-NNNN — <English title> / <Հայերեն վերնագիր>

```json
{
  "id": "CR-NNNN",
  "title": {"hy": "", "en": ""},
  "class": "compatible-implementation",
  "status": "proposed",
  "proposer": "",
  "proposerOwnerId": null,
  "approvals": [],
  "affectedAssets": [],
  "decision": null,
  "risk": "R1",
  "consumerEvidencePlan": "",
  "migrationPlan": "",
  "rollback": "",
  "evidencePlan": "",
  "targetRelease": "",
  "pullRequests": [],
  "closure": null
}
```

## Հայերեն

### Խնդիր
### Ցանկալի արդյունք
### Scope և ազդեցություն (accessibility, localization, content, design-tool)
### Այլընտրանքներ
### Migration և rollback

## English

### Problem
### Desired outcome
### Scope and impact (accessibility, localization, content, design-tool)
### Alternatives
### Migration and rollback

<!-- END: CR-NNNN -->
````

<!-- END: DESIGN_CHANGE_REQUEST_TEMPLATE -->
