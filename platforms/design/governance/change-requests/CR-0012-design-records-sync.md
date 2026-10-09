# CR-0012 — Design Platform records brought to the present / Design Platform-ի գրառումների համաժամեցում իրական վիճակի հետ

```json
{
  "id": "CR-0012",
  "title": {"hy": "Design Platform-ի գրառումների համաժամեցում իրական վիճակի հետ", "en": "Design Platform records brought to the present"},
  "class": "contract-extension",
  "status": "closed",
  "proposer": "AI collaborator (Claude), from the 2026-10-09 review of the Design Platform records",
  "proposerOwnerId": null,
  "approvals": [
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-09", "evidence": "The Owner merged pull request #33 from the menqstudio account: merge commit 391ff55486321dde38b9d392b07cefa5258f6802, commit date 2026-10-09T04:54:56Z; GitHub reports the merge at 2026-10-09T04:54:57Z by `menqstudio` (read from the pull request with `gh pr view 33` on 2026-10-09). This approval covers what pull request #33 contained; the completing pull request is approved only by its own merge."},
    {"ownerId": "owner.menq", "name": "Gevorg Ohanyan", "date": "2026-10-09", "evidence": "The Owner merged the completing pull request #34 from the menqstudio account: merge commit ab229005fe27d89e25577821aef0f0115eb28443; GitHub reports the merge at 2026-10-09T05:18:48Z by `menqstudio` (read with `gh pr view 34` on 2026-10-09). This approval covers what pull request #34 contains."}
  ],
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
  "consumerEvidencePlan": "No product consumer is affected: no token, component, bundle, asset, build script or validator changes. The consumers of these records are the validators and the next session. Evidence: the eight repository gates run GREEN on the working tree, and the pull-request gate passes with 'Change-Request: CR-0012'. Nothing outside this repository is promised. Completion pull request (2026-10-09): scripts/validate_platforms.py and scripts/test_validate_platforms.py change; they are outside platforms/design/ and are not assets of the ownership registry, and still no product consumer is affected.",
  "migrationPlan": "Pull request #33: none. Two optional metadata fields are added to change-request records (mergeEvidence, closureBlockedBy) and two top-level fields to d-025-readiness-record.json (snapshotNotice, current); no existing field of any record is changed or removed. Completion pull request (2026-10-09): d-025-readiness-record.json moves to schemaVersion 2. The seven top-level fields recorded on 2026-07-13 (status, evidenceSnapshot, consumers, crossConsumerValidation, qualityAndAdoptionEvidence, finalAudit, remainingAction) move, values unchanged, under 'snapshot2026-07-13'; 'snapshotNotice' is removed; 'current' stays as the one current block; 'evidenceCorrections' is untouched. A reader of the old top-level keys reads 'snapshot2026-07-13' for history and 'current' for the state in force. The only program in this repository that reads the record, scripts/validate_platforms.py, changes in the same pull request.",
  "rollback": "Revert the implementing pull request (the completion pull request reverts on its own: the record layout, the validator rules and their tests go back together). Records return to their earlier text; no consumer holds a pinned copy of anything this change touches.",
  "evidencePlan": "generate_markdown_inventory.py --check, validate_foundation.py, validate_platforms.py, check_session_read_budget.py, validate_governance.py, validate_brand_expression.py and validate_phase_a.py GREEN; the governance pull-request gate GREEN with 'Change-Request: CR-0012'; every merge hash recorded in CR-0004…CR-0011 exists in the repository (git cat-file). Completion pull request (2026-10-09): scripts/test_validate_platforms.py GREEN with one test per new or changed validator rule plus green controls on the real record; every new or changed rule weakened once to confirm that a test fails; validate_platforms.py GREEN on the working tree with no KNOWN INCONSISTENCY line; the seven snapshot values compared equal to the top-level values at 391ff55.",
  "targetRelease": "none (records only)",
  "pullRequests": [33, 34],
  "mergeEvidence": ["PR #33 merged at 391ff55 on 2026-10-09 08:54 +04:00 (2026-10-09 04:54 UTC)", "PR #34 merged at ab22900 on 2026-10-09 09:18 +04:00 (2026-10-09 05:18 UTC)"],
  "closure": {"date": "2026-10-09", "evidence": ["PR #33 merged at 391ff55 with all 9 GitHub Actions checks passed", "PR #34 merged at ab22900 with all 8 GitHub Actions checks passed, including scripts/test_validate_platforms.py (112 tests) in the Markdown Inventory workflow", "scripts/validate_platforms.py on main at ab22900 prints PLATFORMS VALIDATION: GREEN with the maturity in force (M2, M2), the obligation open and no KNOWN INCONSISTENCY line", "No consumer evidence was promised: the change touches records and one validator only"]}
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

### Լրացում՝ հաստատում և ավարտման pull request (2026-10-09)

**Հաստատում.** Owner-ը 2026-10-09-ին `menqstudio` հաշվից merge է արել pull request #33-ը (merge commit `391ff55`). դա այս change request-ի հաստատումն է, և այն գրանցված է `approvals`-ում՝ որպես evidence նշելով հենց այդ merge-ը։ Status-ը `implementing` է, ոչ `closed`. աշխատանքը ավարտվում է երկրորդ pull request-ով, որը հաստատված չէ, մինչև Owner-ը այն merge չանի։

**Ինչ է անում ավարտման pull request-ը.**

1. `d-025-readiness-record.json`-ը անցնում է `schemaVersion` 2-ի։ 2026-07-13-ին գրանցված յոթ դաշտը (`status`, `evidenceSnapshot`, `consumers`, `crossConsumerValidation`, `qualityAndAdoptionEvidence`, `finalAudit`, `remainingAction`) նույն արժեքներով տեղափոխվում է մեկ դաշտի՝ `snapshot2026-07-13`-ի տակ։ `current`-ը մնում է ընթացիկ վիճակի միակ բլոկը։ `snapshotNotice`-ը հանվում է, քանի որ այն ասում էր, որ snapshot-ը top-level դաշտերն են, իսկ դա այլևս ճիշտ չէ։ `evidenceCorrections`-ը չի փոխվում։
2. `scripts/validate_platforms.py`-ը այլևս չի պահանջում հուլիսի արժեքները top-level-ում։ Այն պահանջում է, որ snapshot-ը լինի, ամբողջական լինի և չփոխվի (content hash), և որ նրա maturity-ն հավասար լինի վերջին ուղղման `previousMaturity`-ին։ `current`-ի ամեն դաշտ պետք է հավասար լինի վերջին ուղղմանը։ `current`-ը, որը պնդում է GREEN, `met`, `evidenced` կամ M3 և բարձր առանց ուղղման հիմքի, RED է։ Snapshot-ի դաշտը top-level-ում կամ `current`-ի ներսում, կամ `current`-ի դաշտը snapshot-ի ներսում՝ անունով RED է։ `KNOWN INCONSISTENCY` տողը այլևս չի տպվում։
3. Validator-ից հանվում են երեք պարտադիր արտահայտությունները, որոնք `ROADMAP.md`-ին ստիպում էին մեջբերել ուղղվածը։ `ROADMAP.md`-ի տեքստը չի փոխվել։
4. `NEXT_CHAT_HANDOFF.md`-ում և `PROJECT_CONTEXT.md`-ում թարմացվում են record-ը նկարագրող նախադասությունները և `CR-0012`-ի status-ը։

**Այս record-ի որ պնդումներն է փոխարինում.** «Չի փոխվում. … validator»՝ ճիշտ էր pull request #33-ի համար. ավարտման pull request-ը փոխում է `scripts/validate_platforms.py`-ը և նրա թեստերը։ «Readiness record-ի top-level արժեքները փոխել ընթացիկի՝ մերժվեց»՝ մերժման պատճառը validator-ի կանոնն էր. կանոնը փոխվել է, իսկ պատմությունը չի վերագրվում, քանի որ հուլիսի արժեքները անփոփոխ մնում են `snapshot2026-07-13`-ի տակ։ Status-ի հակասությունների 7-րդ կետից record-ի `status`-ի մասը այլևս հակասություն չէ. «Locked and GREEN»-ը record-ում նշված է որպես 2026-07-13-ի արժեք։ Նույն կետի մյուս երկու մասը (`PROJECT_CONTEXT.md`-ի վերնագիրը և `D-025_FINAL_POST_LOCK_AUDIT.md`-ը) մնում է Owner-ին։

**Ինչ է պակասում փակման համար.** Ավարտման pull request-ի merge-ը Owner-ի կողմից։ `closure`-ը մնում է `null`։

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

### Completion: the approval and the completing pull request (2026-10-09)

**Approval.** On 2026-10-09 the Owner merged pull request #33 from the `menqstudio` account (merge commit `391ff55`); that is the approval of this change request, and it is recorded in `approvals` with that merge as its evidence. The status is `implementing`, not `closed`: the work is completed by a second pull request, which is not approved until the Owner merges it.

**What the completing pull request does.**

1. `d-025-readiness-record.json` moves to `schemaVersion` 2. The seven fields recorded on 2026-07-13 (`status`, `evidenceSnapshot`, `consumers`, `crossConsumerValidation`, `qualityAndAdoptionEvidence`, `finalAudit`, `remainingAction`) move, with the same values, under one field, `snapshot2026-07-13`. `current` stays as the one block for the current state. `snapshotNotice` is removed, because it said the snapshot is the top-level fields, and that is no longer true. `evidenceCorrections` does not change.
2. `scripts/validate_platforms.py` no longer requires the July values at the top level. It requires the snapshot to exist, to be complete and to be unchanged (a content hash), and its maturity to equal the latest correction's `previousMaturity`. Every field of `current` must equal the latest correction. A `current` that claims GREEN, `met`, `evidenced` or M3 and above without the correction's support is RED. A snapshot field at the top level or inside `current`, or a field of `current` inside the snapshot, is RED by name. The `KNOWN INCONSISTENCY` line is no longer printed.
3. The three required phrases that made `ROADMAP.md` quote what was corrected are removed from the validator. The text of `ROADMAP.md` was not changed.
4. In `NEXT_CHAT_HANDOFF.md` and `PROJECT_CONTEXT.md` the sentences that describe the record and the status of `CR-0012` are updated.

**Which statements of this record it supersedes.** "Not changed: … validator" was true of pull request #33; the completing pull request changes `scripts/validate_platforms.py` and its tests. "Changing the readiness record's top-level values to the current ones was rejected": the reason for the rejection was the validator's rule; the rule has changed, and history is not rewritten, because the July values stay unchanged under `snapshot2026-07-13`. Of status conflict 7, the part about the record's `status` is no longer a conflict: the record marks "Locked and GREEN" as a 2026-07-13 value. The other two parts of that item (the header of `PROJECT_CONTEXT.md` and `D-025_FINAL_POST_LOCK_AUDIT.md`) stay with the Owner.

**What closure still lacks.** The Owner's merge of the completing pull request. `closure` stays `null`.

<!-- END: CR-0012 -->
