# CR-0012 — Design Platform records brought to the present / Design Platform-ի գրառումների համաժամեցում իրական վիճակի հետ

```json
{
  "id": "CR-0012",
  "title": {"hy": "Design Platform-ի գրառումների համաժամեցում իրական վիճակի հետ", "en": "Design Platform records brought to the present"},
  "class": "contract-extension",
  "status": "proposed",
  "proposer": "AI collaborator (Claude), from the 2026-10-09 review of the Design Platform records",
  "proposerOwnerId": null,
  "approvals": [],
  "affectedAssets": [
    "menq.design.spec.brand-core.v1",
    "menq.design.spec.primitives.v1",
    "menq.design.spec.components.v1",
    "menq.design.spec.patterns.v1",
    "menq.design.spec.locales.v1",
    "menq.design.spec.governance.v1",
    "menq.design.spec.adoption.v1",
    "menq.design.spec.brand-expression.v1"
  ],
  "decision": "D-025",
  "risk": "R1",
  "consumerEvidencePlan": "No product consumer is affected: no token, component, bundle, asset, build script or validator changes. The consumers of these records are the validators and the next session. Evidence: the eight repository gates run GREEN on the working tree, and the pull-request gate passes with 'Change-Request: CR-0012'. Nothing outside this repository is promised.",
  "migrationPlan": "None. Two optional metadata fields are added to change-request records (mergeEvidence, closureBlockedBy) and two top-level fields to d-025-readiness-record.json (snapshotNotice, current); no existing field of any record is changed or removed.",
  "rollback": "Revert the implementing pull request. Records return to their earlier text; no consumer holds a pinned copy of anything this change touches.",
  "evidencePlan": "generate_markdown_inventory.py --check, validate_foundation.py, validate_platforms.py, check_session_read_budget.py, validate_governance.py, validate_brand_expression.py and validate_phase_a.py GREEN; the governance pull-request gate GREEN with 'Change-Request: CR-0012'; every merge hash recorded in CR-0004…CR-0011 exists in the repository (git cat-file).",
  "targetRelease": "none (records only)",
  "pullRequests": [],
  "closure": null
}
```

## Հայերեն

### Խնդիր

2026-10-09-ի վերանայումը ցույց տվեց, որ Design Platform-ի գրառումները չեն համընկնում repository-ի իրական վիճակի հետ.

1. `CR-0004`…`CR-0011`-ը `approved` էին՝ `"pullRequests": []` և `"closure": null`, մինչդեռ նրանց աշխատանքը merge է եղել (PR #20…#28)։
2. `CHANGELOG.md`-ը 2026-10-07-ի D-027 գրառումից հետո ոչինչ չուներ, ներառյալ փոխված գույնի արժեքը (`CR-0006`), փոխարինված լոգոն (`CR-0005`) և `FormRow`-ի փոխված contract-ը (`CR-0007`)։
3. `NEXT_CHAT_HANDOFF.md`-ը պատրաստված էր 2026-07-13-ին և ասում էր, որ D-025-ի բաց action չկա։
4. `ROADMAP.md`-ը և `PROJECT_CONTEXT.md`-ը consumer-ների M3/M4 validation-ը ցույց էին տալիս որպես ավարտված և GREEN՝ ուղղումից հետո։ `brand-expression/PROJECT_CONTEXT.md`-ը գրում էր 124 token և 24 կոմպոնենտ. չափվածը 132 և 35 է։
5. D-025 որոշման ֆայլը ուղղման ծանուցում չուներ, թեև lock, closure և final-audit գրառումները ունեին։
6. `d-025-readiness-record.json`-ի top-level դաշտերը հակասում էին նույն ֆայլի `evidenceCorrections` բաժնին։
7. Status պիտակները տարբեր ֆայլերում տարբեր են։
8. `components/Cover/`-ը README չուներ և ոչ մի տեղ չէր հիշատակվում։

### Ցանկալի արդյունք

Գրառումները ասում են այն, ինչ repository-ն իրականում պահում է. ինչն է Locked, ինչն է Draft, ինչն է բաց։ Change request-ը փակված է միայն այնտեղ, որտեղ նրա evidence-ը երևում է repository-ում։ Պատմությունը չի վերագրվում, Locked որոշման տեքստը չի փոխվում, և Owner-ի փոխարեն ոչ մի approval չի գրանցվում։

### Scope և ազդեցություն (accessibility, localization, content, design-tool)

**Փոխվում է.** `CHANGELOG.md`, `NEXT_CHAT_HANDOFF.md`, `ROADMAP.md`, `PROJECT_CONTEXT.md`, `README.md`, `ARCHITECTURE.md`, `CONTRACTS.md`, `brand-expression/PROJECT_CONTEXT.md`, `governance/CHANGE_REQUEST_TEMPLATE.md`, `CR-0004`…`CR-0011`, D-025 որոշման ֆայլը (միայն ծանուցում), `implementation/release/d-025-readiness-record.json` (երկու նոր դաշտ), նոր `brand-expression/components/Cover/README.md`։ `platforms/`-ից դուրս՝ `SESSION_READ_MANIFEST.json`-ի նոր area-ները և վերագեներացված `MARKDOWN_INVENTORY.json`-ը։

**Չի փոխվում.** Token, կոմպոնենտ, bundle, asset, build script, validator, workflow, registry։

**Class-ի ընտրությունը.** `contract-extension`, քանի որ ավելանում է նոր metadata. change request-ի record-ում՝ `mergeEvidence` և `closureBlockedBy`, readiness record-ում՝ `snapshotNotice` և `current`։ Առանց դրանց աշխատանքը կլիներ `compatible-implementation`։ `editorial` չէ, քանի որ պնդումների իմաստը փոխվում է և JSON ֆայլ է փոխվում։

**Change request-ների բաժանումը.** Փակված՝ `CR-0004` (նրա `evidencePlan`-ը ամբողջությամբ ստուգվում է repository-ում)։ Բաց՝ `CR-0005`…`CR-0011`. ամեն մեկի `closureBlockedBy`-ն անվանում է պակասող evidence-ը։

**Accessibility.** Ոչինչ չի ուղղվում, բայց գրանցվում է բաց թերություն. հիմնական Button-ը (`.btn--primary`) սպիտակ տեքստը (`#ffffff`) դնում է `gradient-brand`-ի վրա (`color-action-primary` → `color-accent`)։ Light theme-ում ազուր ծայրը (`#0369a1`) տալիս է 5.93:1, cyan ծայրը (`#06b6d4`)՝ 2.43:1. 4.5:1-ից ցածր է gradient-ի մոտ 30%-ից հետո։ Dark theme-ում (`#020617` տեքստ)՝ 7.28:1 և 11.16:1։ `components/Button/README.md`-ը չի փոխվել։

**Localization, content, design-tool.** Չեն ազդվում։

**Owner-ին թողնված status-ի հակասությունները** (lifecycle արժեք չի փոխվել).

1. `ARCHITECTURE.md`՝ `Locked (D-025, 2026-07-13)`, իսկ նրանից սնվող registry գրառումը՝ `menq.design.spec.brand-core.v1`՝ `Approved — Implementing`։
2. `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`՝ `Locked baseline`, իսկ նրանից սնվող `tokens.v1`, `foundations.v1`, `assets.v1`, `motion.v1` գրառումները՝ `Approved — Implementing`։
3. `CONTRACTS.md`՝ «մանրամասն specifications-ը սպասման մեջ են», իսկ D-025-ի lock-ի 1-ին պայմանը՝ «ամբողջական canonical specification set-ը առկա է», և չորս registry specification հղվում են այս ֆայլին։
4. Registry-ի top-level `status`-ը `Locked` է, իսկ նրա 16 specification-ից 13-ը՝ `Approved — Implementing` (1-ը `Locked`, 2-ը `Draft`)։
5. Part 12, 13, 15 և 16 փաստաթղթերը՝ `Approved Architecture — Implementing`, մինչդեռ D-025-ը `Locked` է. Part 13-ը backlog-ում է, բայց baseline-ի §11-ը ասում է, որ բոլոր կետերը փակվել են lock-ով։
6. `GOVERNANCE_…_V1.md`-ի վերնագիրը՝ `Approved Architecture — Implementing`, իսկ նրա «Implementation status» բաժինը, `governance/README.md`-ը և registry-ն՝ `Locked`։
7. «Locked և GREEN» (`PROJECT_CONTEXT.md`-ի վերնագիր, readiness record-ի `status`, `D-025_FINAL_POST_LOCK_AUDIT.md`), մինչդեռ evidence-ի ուղղումը ասում է, որ երկու իրական consumer-ի պայմանը ապացուցված չէ։
8. `implementation/release/`-ի երեք փաստաթուղթը՝ `Approved — Implementing`՝ D-025-ի (`Locked`) ներքո։

### Այլընտրանքներ

- Փակել բոլոր ութ change request-ը, քանի որ աշխատանքը merge է եղել՝ մերժվեց. lifecycle-ը պահանջում է, որ evidence-ը կապված լինի, իսկ յոթի evidence-ը repository-ում չկա։
- Readiness record-ի top-level արժեքները փոխել ընթացիկի՝ մերժվեց. `scripts/validate_platforms.py`-ը պահանջում է, որ `status`-ը լինի `Locked and GREEN`, `crossConsumerValidation`-ը՝ `GREEN`, իսկ top-level maturity-ն՝ ուղղման `previousMaturity`-ն, և պատմությունը չպետք է վերագրվի։
- Button-ի README-ն ուղղել, որ գրի 5.9:1՝ մերժվեց. կոմպոնենտը իսկապես խախտում է կանոնը cyan ծայրում, ուստի սա թերություն է, ոչ հնացած տեքստ։
- Status պիտակները միավորել՝ մերժվեց. lifecycle արժեքը Owner-ի որոշումն է։

### Migration և rollback

Migration պետք չէ։ Rollback՝ իրականացնող PR-ի revert։

## English

### Problem

The 2026-10-09 review showed that the Design Platform records do not match what the repository holds:

1. `CR-0004`…`CR-0011` were `approved` with `"pullRequests": []` and `"closure": null`, while their work is merged (PR #20…#28).
2. `CHANGELOG.md` had nothing after the 2026-10-07 D-027 entry, including a changed colour value (`CR-0006`), a replaced logo (`CR-0005`) and a changed `FormRow` contract (`CR-0007`).
3. `NEXT_CHAT_HANDOFF.md` was prepared on 2026-07-13 and said no D-025 action remained open.
4. `ROADMAP.md` and `PROJECT_CONTEXT.md` still showed the consumers' M3/M4 validation as completed and GREEN after the correction. `brand-expression/PROJECT_CONTEXT.md` said 124 tokens and 24 components; the measured numbers are 132 and 35.
5. The D-025 decision file carried no correction notice, although the lock, closure and final-audit records did.
6. The top-level fields of `d-025-readiness-record.json` contradicted the same file's `evidenceCorrections` block.
7. Status labels differ from file to file.
8. `components/Cover/` had no README and was mentioned nowhere.

### Desired outcome

The records say what the repository really holds: what is Locked, what is Draft, what is open. A change request is closed only where its evidence can be seen in the repository. History is not rewritten, the body of a Locked decision is not changed, and no approval is recorded on the Owner's behalf.

### Scope and impact (accessibility, localization, content, design-tool)

**Changed:** `CHANGELOG.md`, `NEXT_CHAT_HANDOFF.md`, `ROADMAP.md`, `PROJECT_CONTEXT.md`, `README.md`, `ARCHITECTURE.md`, `CONTRACTS.md`, `brand-expression/PROJECT_CONTEXT.md`, `governance/CHANGE_REQUEST_TEMPLATE.md`, `CR-0004`…`CR-0011`, the D-025 decision file (a notice only), `implementation/release/d-025-readiness-record.json` (two new fields), and a new `brand-expression/components/Cover/README.md`. Outside `platforms/`: the new areas in `SESSION_READ_MANIFEST.json` and the regenerated `MARKDOWN_INVENTORY.json`.

**Not changed:** any token, component, bundle, asset, build script, validator, workflow or registry.

**Choice of class:** `contract-extension`, because new metadata is added: `mergeEvidence` and `closureBlockedBy` in the change-request record, `snapshotNotice` and `current` in the readiness record. Without them the work would be `compatible-implementation`. It is not `editorial`, because the meaning of statements changes and a JSON file changes.

**The change-request split:** closed — `CR-0004` (its `evidencePlan` can be checked in full in the repository). Open — `CR-0005`…`CR-0011`; the `closureBlockedBy` of each names the missing evidence.

**Accessibility:** nothing is fixed, but an open defect is recorded. The primary Button (`.btn--primary`) puts white text (`#ffffff`) on `gradient-brand` (`color-action-primary` → `color-accent`). In the light theme the azure end (`#0369a1`) gives 5.93:1 and the cyan end (`#06b6d4`) gives 2.43:1; the ratio is below 4.5:1 from about 30% of the way along the gradient. In the dark theme (`#020617` text) the ends give 7.28:1 and 11.16:1. `components/Button/README.md` was not changed.

**Localization, content, design-tool:** not affected.

**Status conflicts left for the Owner** (no lifecycle value was changed):

1. `ARCHITECTURE.md` says `Locked (D-025, 2026-07-13)`, while the registry entry sourced from it, `menq.design.spec.brand-core.v1`, says `Approved — Implementing`.
2. `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md` says `Locked baseline`, while the `tokens.v1`, `foundations.v1`, `assets.v1` and `motion.v1` entries sourced from it say `Approved — Implementing`.
3. `CONTRACTS.md` says "detailed specifications pending", while D-025's lock condition 1 says "Complete canonical specification set exists", and four registry specifications point at this file.
4. The registry's top-level `status` is `Locked`, while 13 of its 16 specifications are `Approved — Implementing` (1 is `Locked`, 2 are `Draft`).
5. The Part 12, 13, 15 and 16 documents say `Approved Architecture — Implementing`, while D-025 is `Locked`; Part 13 is in the backlog, yet §11 of the baseline says every item was closed by the lock.
6. The header of `GOVERNANCE_…_V1.md` says `Approved Architecture — Implementing`, while its own "Implementation status" section, `governance/README.md` and the registry say `Locked`.
7. "Locked and GREEN" (the header of `PROJECT_CONTEXT.md`, the readiness record's `status`, `D-025_FINAL_POST_LOCK_AUDIT.md`), while the evidence correction says the two-real-consumer condition is not evidenced.
8. The three documents in `implementation/release/` say `Approved — Implementing` under D-025 (`Locked`).

### Alternatives

- Closing all eight change requests because the work is merged was rejected: the lifecycle requires the evidence to be linked, and for seven of them the evidence is not in the repository.
- Changing the readiness record's top-level values to the current ones was rejected: `scripts/validate_platforms.py` requires `status` to be `Locked and GREEN`, `crossConsumerValidation` to be `GREEN` and the top-level maturity to equal the correction's `previousMaturity`, and history must not be rewritten.
- Correcting the Button README to say 5.9:1 was rejected: the component really breaks the rule at the cyan end, so this is a defect, not stale text.
- Unifying the status labels was rejected: a lifecycle value is the Owner's decision.

### Migration and rollback

No migration is needed. Rollback: revert the implementing PR.

<!-- END: CR-0012 -->
