# MenQ Standard — Changelog

## 2026-10-09 — D-025 readiness record: the snapshot and the current state separated; CR-0012 approval recorded

### Հայերեն

- D-025 readiness record-ը (`platforms/design/implementation/release/d-025-readiness-record.json`) անցավ `schemaVersion` 2-ի։ 2026-07-13-ի lock-ի պահին գրանցված յոթ դաշտը (`status`, `evidenceSnapshot`, `consumers`, `crossConsumerValidation`, `qualityAndAdoptionEvidence`, `finalAudit`, `remainingAction`) նույն արժեքներով տեղափոխվեց մեկ դաշտի՝ `snapshot2026-07-13`-ի տակ։ `current`-ը ընթացիկ վիճակի միակ բլոկն է։ `snapshotNotice`-ը հանվեց։ `evidenceCorrections`-ը չի փոխվել։
- `scripts/validate_platforms.py`-ը այլևս չի պահանջում հուլիսի արժեքները վերին մակարդակում։ Այն պահանջում է, որ snapshot-ը լինի, ամբողջական լինի և չփոխվի (content hash), և որ նրա maturity-ն հավասար լինի վերջին ուղղման `previousMaturity`-ին։ `current`-ի ամեն դաշտ պետք է հավասար լինի վերջին ուղղմանը։ `current`-ը, որը պնդում է GREEN, `met`, `evidenced` կամ M3 և բարձր առանց ուղղման հիմքի, RED է։ Snapshot-ի և `current`-ի դաշտերի խառնումը RED է՝ անունով։ `KNOWN INCONSISTENCY` տողը այլևս չի տպվում, և վերջին տողերը կարդացվում են `current`-ից։
- Validator-ից հանվեցին երեք պարտադիր արտահայտությունները, որոնք `platforms/design/ROADMAP.md`-ին ստիպում էին մեջբերել ուղղվածը։ Roadmap-ի տեքստը չի փոխվել։
- `scripts/test_validate_platforms.py`․ 112 թեստ։ Նոր կամ փոխված յուրաքանչյուր կանոն մեկ անգամ թուլացվեց՝ 42 mutant, բոլորի դեպքում առնվազն մեկ թեստ կարմրեց։
- `CR-0012`-ի status-ը դարձավ `implementing`, և գրանցվեց մեկ approval, որի evidence-ը Owner-ի կողմից pull request #33-ի merge-ն է (merge commit `391ff55`, 2026-10-09)։ Change request-ը փակված չէ․ այս փոփոխությունը այն ավարտում է և հաստատված է միայն իր pull request-ի merge-ով։ Այս գրառումը հաստատում չի հայտարարում։
- `DECISIONS.md`-ում `D-009`-ի տակի 2026-10-09-ի նշման վերջին նախադասությունը այժմ գրում է փաստը՝ Owner-ը merge է արել pull request #32-ը (merge commit `b24de94`)։ Նշման մնացած մասը չի փոխվել։ `NEXT_CHAT_HANDOFF.md`-ի 5-րդ կետը թարմացվեց։
- Սահմաններ․ ստուգումները կատարվել են local clone-ում առանց ցանցի, ուստի GitHub-ից ոչինչ չի կարդացվել, և այս փոփոխությունը GitHub Actions-ում դեռ չի գործարկվել։ `ECOSYSTEM_ARCHITECTURE.md`-ը և `NEXT_CHAT_HANDOFF.md`-ի 7-րդ կետը դեռ ասում են, որ `D-009`-ի նշումը հաստատում չունի․ դրանք չեն փոխվել։

### English

- The D-025 readiness record (`platforms/design/implementation/release/d-025-readiness-record.json`) moved to `schemaVersion` 2. The seven fields recorded at the 2026-07-13 lock (`status`, `evidenceSnapshot`, `consumers`, `crossConsumerValidation`, `qualityAndAdoptionEvidence`, `finalAudit`, `remainingAction`) moved, with the same values, under one field, `snapshot2026-07-13`. `current` is the one block for the current state. `snapshotNotice` was removed. `evidenceCorrections` is unchanged.
- `scripts/validate_platforms.py` no longer requires the July values at the top level. It requires the snapshot to exist, to be complete and to be unchanged (a content hash), and its maturity to equal the latest correction's `previousMaturity`. Every field of `current` must equal the latest correction. A `current` that claims GREEN, `met`, `evidenced` or M3 and above without the correction's support is RED. Mixing the fields of the snapshot and of `current` is RED by name. The `KNOWN INCONSISTENCY` line is no longer printed, and the last lines are read from `current`.
- The three required phrases that made `platforms/design/ROADMAP.md` quote what was corrected were removed from the validator. The roadmap's text was not changed.
- `scripts/test_validate_platforms.py`: 112 tests. Every new or changed rule was weakened once: 42 mutants, and for each at least one test went red.
- The status of `CR-0012` became `implementing`, and one approval was recorded whose evidence is the Owner's merge of pull request #33 (merge commit `391ff55`, 2026-10-09). The change request is not closed: this change completes it and is approved only by the merge of its own pull request. This entry claims no approval.
- In `DECISIONS.md` the last sentence of the 2026-10-09 note under `D-009` now states the fact: the Owner merged pull request #32 (merge commit `b24de94`). The rest of the note is unchanged. Item 5 of `NEXT_CHAT_HANDOFF.md` was updated.
- Limits: the checks were made in a local clone without network access, so nothing was read from GitHub, and this change has not yet run in GitHub Actions. `ECOSYSTEM_ARCHITECTURE.md` and item 7 of `NEXT_CHAT_HANDOFF.md` still say that the note under `D-009` has no approval; they were not changed.

## 2026-10-09 — Root and Foundation status statements synchronized

### Հայերեն

- 2026-10-09-ի review-ի ութ կետից յուրաքանչյուրը նախ ստուգվեց ֆայլերում, հետո ուղղվեց։ Փոխվել են միայն պնդումներ․ ոչ մի պատմական գրառում չի ջնջվել, ոչ մի tag չի փոխվել, և այս գրառումը հաստատում չի հայտարարում։ Owner-ի հաստատումը այս փոփոխությունների pull request-ի merge-ն է։
- Ընթացիկ վիճակի ցանկը այժմ մեկ տեղում է՝ `README.md`-ի `Status` բաժնում։ `PROJECT_CONTEXT.md`-ը, `AI_WORKING_CONTEXT.md`-ը և `NEXT_CHAT_HANDOFF.md`-ը այն այլևս չեն կրկնում և հղվում են այնտեղ։ Ցանկին ավելացվեց `D-027`-ի տողը, որը մյուս երեք ֆայլերում կար, իսկ այստեղ՝ ոչ։ Session-read core-ը 107,581 բայթից դարձավ 103,847։
- `README.md`-ի «MenQ Design Platform status» պարբերությունը, `PROJECT_CONTEXT.md`-ի «two-consumer evidence-ը GREEN է» տողը և `ROADMAP.md`-ի «Երկու distinct consumer՝ M3 և M4» ավարտված կետը դեռ պնդում էին այն maturity evidence-ը, որը 2026-10-07-ի գրառումը հետ էր վերցրել։ Այժմ բոլորը ասում են՝ repo-ի ներսի երկու consumer-ը M2 pilot են, իրական consumer-ի պարտավորությունը բաց է։ `ROADMAP.md`-ի կետը պահպանում է նախկին ձևակերպումը և ուղղման ամսաթիվը։
- `AI_WORKING_CONTEXT.md`-ը և `ROADMAP.md`-ը ասում էին, որ audit-ի remediation-ը «շարունակվում է (workflow security, bilingual completion, Owner-ի որոշումներ)», մինչդեռ այս changelog-ը 4-րդ, 5-րդ և 6-րդ փուլերը գրանցում է ավարտված։ Երկուսն էլ ուղղվեցին։
- `NEXT_CHAT_HANDOFF.md`-ը վերագրվեց 2026-10-09-ի դրությամբ՝ ինչն է ճիշտ հիմա, յոթ բաց հարց և առաջին քայլը։
- «Last synchronized» ամսաթիվը 2026-10-09 է այն ֆայլերում, որոնք ամբողջությամբ ստուգվեցին՝ `PROJECT_CONTEXT.md`, `AI_WORKING_CONTEXT.md`, `ROADMAP.md`, `ECOSYSTEM_ARCHITECTURE.md`, `foundation/README.md`, `foundation/PROJECT_CONTEXT.md`, `foundation/ai-collaboration/PROJECT_CONTEXT.md`, `release/FOUNDATION_V1_RELEASE_README.md`։ Governance, Documentation և Decision System chapter context-ները ստացան այդ տողը առաջին անգամ։ Philosophy, Principles և Terminology context-ները չեն ստուգվել և մնում են 2026-07-12։
- `foundation/README.md`-ի `Current gate` բաժինը այլևս չի նշում 2026-07-ի workflow run `#9`-ը որպես ընթացիկ evidence, այլ մեջբերում է validator-ի 2026-10-09-ի local output-ը։ `foundation/PROJECT_CONTEXT.md`-ը այլևս չի մեջբերում տող, որը validator-ը չի տպում։
- `DECISIONS.md`-ում `D-009`-ի տակ ավելացվեց 2026-10-09-ի երկլեզու նշում՝ քայլերի հերթականությունը և «GitHub գնում է միայն հաստատված…» նախադասությունը մասամբ փոխարինված են `D-020`-ով։ `D-009`-ի տեքստը և status-ը չեն փոխվել։ Նույն հղումը ավելացվեց `ECOSYSTEM_ARCHITECTURE.md`-ին, որը կրկնում է այդ workflow-ը։
- `ECOSYSTEM_ARCHITECTURE.md`-ը ստացավ metadata header՝ Owner, canonical path, related decisions, last synchronized։ `Status`, `Version`, `Document class` և `Review trigger` դաշտերը չեն լրացվել, քանի որ դրանք որոշող գրառում չկա։
- `release/FOUNDATION_V1_RELEASE_README.md`-ը այժմ գրում է ստուգված փաստերը՝ `foundation-v1.0.0` tag-ը ցույց է տալիս նույն `3793b3c` commit-ը (2026-10-07), ինչ `design-platform-v0.1.0-next.0`-ը, և snapshot-ը ամբողջ repository-ն է։
- `DECISION_INDEX.md`-ի `D-028` տողի հայերեն կեսը գրում էր `Proposed`, անգլերենը՝ `Approved`․ հայերենը ուղղվեց։
- Սահմաններ․ ստուգումները կատարվել են local clone-ում առանց ցանցի, ուստի ոչ մի GitHub Actions run, Release էջ կամ asset չի կարդացվել։ `platforms/`, `scripts/` և `.github/` directory-ներում ոչինչ չի փոխվել։ `MARKDOWN_INVENTORY.json`-ը վերագեներացվեց։

### English

- Each of the eight items of the review of 2026-10-09 was checked in the files first and corrected after. Only statements changed: no historical record was deleted, no tag was changed, and this entry claims no approval. The Owner's approval is the merge of the pull request that carries these changes.
- The list of the current state now lives in one place, the `Status` section of `README.md`. `PROJECT_CONTEXT.md`, `AI_WORKING_CONTEXT.md` and `NEXT_CHAT_HANDOFF.md` no longer restate it and point there. The list gained the `D-027` line, which the other three files had and this one lacked. The session-read core went from 107,581 bytes to 103,847.
- The “MenQ Design Platform status” paragraph of `README.md`, the line “two-consumer evidence is GREEN” of `PROJECT_CONTEXT.md` and the completed item “Two distinct consumers: M3 and M4” of `ROADMAP.md` still asserted the maturity evidence that the entry of 2026-10-07 had withdrawn. All now say that the two in-repo consumers are M2 pilots and that the real-consumer obligation is open. The `ROADMAP.md` item keeps the earlier wording and the date of the correction.
- `AI_WORKING_CONTEXT.md` and `ROADMAP.md` said that remediation of the audit “continues (workflow security, bilingual completion, Owner decisions)”, while this changelog records phases 4, 5 and 6 as complete. Both were corrected.
- `NEXT_CHAT_HANDOFF.md` was rewritten as of 2026-10-09: what is true now, seven open matters, and the first step.
- The “Last synchronized” date is 2026-10-09 in the files that were verified in full: `PROJECT_CONTEXT.md`, `AI_WORKING_CONTEXT.md`, `ROADMAP.md`, `ECOSYSTEM_ARCHITECTURE.md`, `foundation/README.md`, `foundation/PROJECT_CONTEXT.md`, `foundation/ai-collaboration/PROJECT_CONTEXT.md`, `release/FOUNDATION_V1_RELEASE_README.md`. The Governance, Documentation and Decision System chapter contexts received that line for the first time. The Philosophy, Principles and Terminology contexts were not verified and stay at 2026-07-12.
- The `Current gate` section of `foundation/README.md` no longer names workflow run `#9` of July 2026 as the current evidence; it quotes the validator's local output of 2026-10-09. `foundation/PROJECT_CONTEXT.md` no longer quotes a line the validator does not print.
- In `DECISIONS.md` a bilingual note dated 2026-10-09 was added under `D-009`: the order of the steps and the sentence “Only approved architecture and decisions enter GitHub” are superseded in part by `D-020`. The text and the status of `D-009` are unchanged. The same pointer was added to `ECOSYSTEM_ARCHITECTURE.md`, which repeats that workflow.
- `ECOSYSTEM_ARCHITECTURE.md` received a metadata header: Owner, canonical path, related decisions, last synchronized. The fields `Status`, `Version`, `Document class` and `Review trigger` were not filled in, because no record determines them.
- `release/FOUNDATION_V1_RELEASE_README.md` now states the checked facts: the tag `foundation-v1.0.0` points at the same commit `3793b3c` (2026-10-07) as `design-platform-v0.1.0-next.0`, and the snapshot is the whole repository.
- The Armenian half of the `D-028` line of `DECISION_INDEX.md` read `Proposed` while the English half read `Approved`; the Armenian was corrected.
- Limits: the checks were made in a local clone without network access, so no GitHub Actions run, Release page or asset was read. Nothing was changed in the `platforms/`, `scripts/` or `.github/` directories. `MARKDOWN_INVENTORY.json` was regenerated.

## 2026-10-09 — Validators check content, and the validators are tested

### Հայերեն

- 2026-10-09-ի անկախ մեխանիկական review-ն validator-ների ստուգվող օբյեկտները մեկ առ մեկ փչացրեց repository-ի ժամանակավոր պատճենում և գրանցեց, թե որ ստուգումները մնացին GREEN։ Եզրակացությունը՝ validator-ները ստուգում էին, որ բաները գոյություն ունեն, ոչ թե ինչ են պարունակում, և validator-ներին ոչինչ չէր ստուգում։ Review-ի 18 կետից յուրաքանչյուրը նախ վերարտադրվեց, հետո ուղղվեց։
- `scripts/validate_foundation.py`․ պարտադիր փաստաթուղթը պետք է ունենա level-1 վերնագիր, `Status` metadata տող, հայերեն և անգլերեն բաժին, առնվազն 600 բայթ body, 50 հայերեն և 300 լատինական տառ, և END marker-ը պետք է լինի ֆայլի վերջում։ Սահմանները դրված են այսօրվա ամենափոքր պարտադիր փաստաթղթի չափերից (952 բայթ, 66 հայերեն տառ, 527 լատինական տառ) ցածր։ Երեք փաստաթուղթ՝ `README.md`, `CHANGELOG.md` և `ECOSYSTEM_ARCHITECTURE.md`, `Status` տող չունեն և անունով ազատված են միայն այդ կանոնից։
- Workflow-ները այլևս բառերով չեն համեմատվում, այլ parse են արվում։ CI-ն YAML գրադարան չի տեղադրում, ուստի validator-ն ունի workflow-ների օգտագործած YAML ենթաբազմության խիստ parser և RED է տալիս այն ամենի վրա, ինչ չի կարող parse անել։ Կանոնը՝ վերին մակարդակի `permissions`-ը ճիշտ `contents: read` է, `contents: write` կարող են ունենալ միայն `publish-release.yml`-ի երկու հրապարակող job-երը, ամեն `uses` ամրացված է 40 նիշանոց SHA-ով, `pull_request_target`-ը, `continue-on-error`-ը, `|| true`-ն և ներբեռնածի pipe-ը shell-ին արգելված են, `pnpm install`-ը պետք է ունենա `--frozen-lockfile`, և հայտարարված ինը workflow-ից յուրաքանչյուրը պետք է գոյություն ունենա և առանց պայմանի գործարկի իր validator-ը։
- Links․ ստուգվում են վերնագրով, reference-style և HTML (`src`, `href`, `srcset`) հղումները և anchor-ները, և հղման թիրախը պետք է լինի tracked ֆայլ։ Երկլեզվություն․ label-ից հետո պետք է լինի տեքստ, և language block-ից դուրս գտնվող բաժինը չի կարող լինել միայն անգլերեն։ Decision index․ ցանկացած համարով decision ֆայլ պետք է նշված լինի index-ում։
- Path-երը թվարկվում են `git ls-files -z`-ով, ուստի բացատ կամ հայերեն տառեր պարունակող անունը այլևս traceback չի տալիս, և `.MD` վերջածանցը նույն կերպ է հաշվվում generator-ում և validator-ում։ Inventory-ի `source` դաշտը փոխվեց, և `MARKDOWN_INVENTORY.json`-ը վերագեներացվեց։ Երեք script-ից ոչ մեկը այլևս traceback-ով չի պատասխանում․ անսպասելի input-ը RED տող է։
- `scripts/validate_platforms.py`․ readiness record-ը `{}` կամ դատարկ list լինելու դեպքում RED է։ Permanent release-ի URL-ը, tag-ը, asset-ը, digest-ը և source commit-ը պետք է համաձայն լինեն միմյանց, release version-ին և `D-025_EVIDENCE_CORRECTION_RECORD.md`-ին։ `realConsumerObligation.status`-ը `met` կարող է լինել միայն երկու տարբեր անվանված իրական consumer-ի և յուրաքանչյուրի թվագրված evidence-ի դեպքում։ `PLATFORM_REGISTRY.md`-ը պետք է ունենա տող յուրաքանչյուր platform directory-ի համար։ Վերջին տողերը այլևս անպայման տպվող literal-ներ չեն, այլ կարդացվում են record-ից։
- Չուղղված անհամապատասխանություն․ readiness record-ի վերին մակարդակի `consumers[].maturity`-ն ցույց է տալիս M3 և M4, իսկ նույն ֆայլի evidence correction-ը՝ M2 և M2։ Record-ը չի խմբագրվել։ Validator-ը վերին մակարդակի արժեքը պահում է correction-ի `previousMaturity`-ին հավասար և ամեն գործարկման ժամանակ տպում է `KNOWN INCONSISTENCY` տող։ Record-ը ուղղելը Owner-ի որոշում է։
- Ավելացվեցին `scripts/test_validate_foundation.py`, `scripts/test_validate_platforms.py` և `scripts/test_generate_markdown_inventory.py` թեստերը․ յուրաքանչյուր ստուգում ունի թեստ, որը ժամանակավոր git repository-ում փչացնում է հենց իր օբյեկտը և պահանջում է RED՝ կոնկրետ հաղորդագրությամբ։ Թեստերը ավելացվեցին `Markdown Inventory Integrity` workflow-ին։
- Սահմաններ․ release tag-ի գոյությունը GitHub-ում offline չի ստուգվում, միայն հայերեն գրված բաժինը չի հայտնաբերվում, և shell-ի վերլուծությունը ծածկում է թվարկված ձևերը, ոչ թե ամեն հնարավորը։ Այս գրառումը հաստատում չի հայտարարում, և այս փոփոխությունը GitHub Actions-ում դեռ չի գործարկվել։

### English

- The independent mechanical review of 2026-10-09 broke the subjects of the validators one at a time in a temporary copy of the repository and recorded which checks stayed GREEN. Its conclusion: the validators checked that things exist, not what they contain, and nothing checked the validators. Each of the review's 18 items was reproduced first and fixed after.
- `scripts/validate_foundation.py`: a required document must have a level-1 title, a `Status` metadata line, an Armenian and an English section, at least 600 body bytes, 50 Armenian and 300 Latin letters, and its END marker must be at the end of the file. The floors sit below the smallest required document of today (952 bytes, 66 Armenian letters, 527 Latin letters). Three documents, `README.md`, `CHANGELOG.md` and `ECOSYSTEM_ARCHITECTURE.md`, carry no `Status` line and are exempt by name from that one rule only.
- Workflows are no longer matched by words; they are parsed. CI installs no YAML library, so the validator carries a strict parser for the YAML subset the workflows use and is RED on anything it cannot parse. The rule: top-level `permissions` is exactly `contents: read`, only the two publishing jobs of `publish-release.yml` may hold `contents: write`, every `uses` is pinned to a 40-character SHA, `pull_request_target`, `continue-on-error`, `|| true` and piping a download into a shell are refused, `pnpm install` must carry `--frozen-lockfile`, and each of the nine declared workflows must exist and run its validator unconditionally.
- Links: titled, reference-style and HTML (`src`, `href`, `srcset`) links and anchors are checked, and a link target must be a tracked file. Bilingual parity: a label must be followed by text, and a section outside a language block may not be English-only. Decision index: a decision file of any number must be named in the index.
- Paths are enumerated with `git ls-files -z`, so a name with a space or Armenian letters no longer gives a traceback, and the `.MD` suffix is counted the same way by the generator and the validator. The inventory's `source` field changed, and `MARKDOWN_INVENTORY.json` was regenerated. None of the three scripts answers with a traceback any more; a surprising input is a RED line.
- `scripts/validate_platforms.py`: a readiness record that is `{}` or an empty list is RED. The permanent release's URL, tag, asset, digest and source commit must agree with each other, with the release version and with `D-025_EVIDENCE_CORRECTION_RECORD.md`. `realConsumerObligation.status` may be `met` only with two distinct named real consumers that each have dated evidence. `PLATFORM_REGISTRY.md` must have a row for every platform directory. The last lines are no longer literals printed unconditionally; they are read from the record.
- An inconsistency left unfixed: the top-level `consumers[].maturity` of the readiness record shows M3 and M4, while the evidence correction in the same file shows M2 and M2. The record was not edited. The validator holds the top-level value equal to the correction's `previousMaturity` and prints a `KNOWN INCONSISTENCY` line on every run. Correcting the record is an Owner decision.
- Added the tests `scripts/test_validate_foundation.py`, `scripts/test_validate_platforms.py` and `scripts/test_generate_markdown_inventory.py`: every check has a test that breaks exactly its subject in a temporary git repository and requires RED with the specific message. The tests were added to the `Markdown Inventory Integrity` workflow.
- Limits: the existence of the release tag on GitHub is not checked offline, a section written only in Armenian is not detected, and the shell analysis covers the listed forms rather than every possible one. This entry claims no approval, and this change has not yet run in GitHub Actions.
## 2026-10-09 — D-028 approved

### Հայերեն

- Owner-ը 2026-10-09-ին `menqstudio` հաշվից merge արեց pull request #29-ը (merge commit `ed91149`)․ դա `D-028`-ի հաստատումն է։ `D-028`-ի status-ը դարձավ `Approved`, ոչ `Locked`։ `CANONICAL_SESSION_READ_LAW.md` v2-ը ուժի մեջ է։
- Այն փաստաթղթերը, որոնք `D-028`-ը անվանում էին առաջարկված, այժմ նշում են հաստատումը և pull request-ի համարը։ Ներքևի «D-028 proposed» գրառումը մնում է անփոփոխ՝ որպես այն, ինչ ճիշտ էր գրելու պահին։

### English

- On 2026-10-09 the Owner merged pull request #29 from the `menqstudio` account (merge commit `ed91149`); that is the approval of `D-028`. The status of `D-028` became `Approved`, not `Locked`. `CANONICAL_SESSION_READ_LAW.md` v2 is in force.
- The documents that called `D-028` proposed now state the approval and the pull request number. The “D-028 proposed” entry below stays unchanged, as what was true when it was written.

## 2026-10-09 — D-028 proposed: bounded session read

### Հայերեն

- Ավելացվեց `D-028` Bounded Session Read Law-ը՝ status-ը `Proposed`։ Հաստատումը Owner-ի կողմից նրա pull request-ի merge-ն է․ այս գրառումը հաստատում չի հայտարարում։ D-028-ը մասամբ փոխարինում է `D-026`-ը․ «բոլոր tracked `.md` ֆայլերը» (133 ֆայլ, 684,725 բայթ `c61608a`-ում, առանց վերին սահմանի) պահանջի փոխարեն պարտադիր ընթերցումը դառնում է սահմանափակ core՝ 120,000 բայթից ոչ ավելի, իսկ մնացածը կարդացվում է ըստ directory-ի area-ի։
- Ավելացվեց `foundation/ai-collaboration/SESSION_READ_MANIFEST.json`՝ core-ի 10 ֆայլ (107,705 բայթ այս draft-ում) per-file սահմաններով և 65 area։
- Ավելացվեց `scripts/check_session_read_budget.py` gate-ը և նրա թեստերը․ gate-ը RED է, երբ manifest-ը բացակայում կամ անվավեր է, core ֆայլը բացակայում է կամ գերազանցում է իր սահմանը, core-ի ընդհանուր չափը կամ per-file սահմանների գումարը գերազանցում է budget-ը, path-ը կրկնվում է, area-ն նշում է գոյություն չունեցող directory կամ ֆայլ, կամ tracked Markdown ֆայլը հասանելի չէ ո՛չ core-ից, ո՛չ որևէ area-ից։ Բայթերը հաշվվում են CRLF-ը LF դարձնելուց հետո։ Gate-ը ավելացվեց `Markdown Inventory Integrity` workflow-ին։
- `CANONICAL_SESSION_READ_LAW.md`-ը դարձավ v2՝ core և area կանոնով։ Այն հստակ ասում է, որ receipt-ը ապացուցում է core-ի փոխանցումը տվյալ content hash-ով, բայց ոչ հասկանալը, և որ ոչ մի ծրագիր չի ստուգում session-ի ընթերցումը։ Հեռացվեցին §2, §3, §5, §6 և §10 բաժինների կրկնվող կրճատ անգլերեն պարբերությունները, որոնք կրկնում էին հին կանոնը։
- `README.md`, `PROJECT_CONTEXT.md`, `AI_WORKING_CONTEXT.md`, `NEXT_CHAT_HANDOFF.md`, `foundation/README.md`, `foundation/PROJECT_CONTEXT.md`, `foundation/ai-collaboration/PROJECT_CONTEXT.md`, `platforms/design/PROJECT_CONTEXT.md` և `platforms/design/NEXT_CHAT_HANDOFF.md` փաստաթղթերում հին կանոնի կրկնությունը և D-026-ի մասին «machine-enforced» պնդումը փոխարինվեցին նրանով, ինչ իրականում ստուգվում է։
- Բոլոր MenQ repository-ների համար մեկ ընդհանուր առավելագույն սահման՝ 350,000 բայթ, gate-ի կոդում․ MenQ Standard-ը իր manifest-ում հայտարարում է 120,000։
- `MARKDOWN_INVENTORY.json`-ը և նրա drift check-ը մնում են։ Consumer repository-ների համար նույն կանոնը պահանջվում է D-028-ով, բայց adoption մեխանիզմ դեռ չկա․ դա հետագա որոշում է։

### English

- Added `D-028` Bounded Session Read Law with status `Proposed`. The approval is the Owner's merge of its pull request; this entry claims no approval. D-028 supersedes `D-026` in part: instead of “every tracked `.md` file” (133 files and 684,725 bytes at `c61608a`, with no upper bound), the mandatory read becomes a bounded core of at most 120,000 bytes, and everything else is read by the area of a directory.
- Added `foundation/ai-collaboration/SESSION_READ_MANIFEST.json`: 10 core files (107,705 bytes in this draft) with per-file ceilings, and 65 areas.
- Added the `scripts/check_session_read_budget.py` gate and its tests. The gate is RED when the manifest is missing or malformed, a core file is absent or exceeds its ceiling, the core total or the sum of the per-file ceilings exceeds the budget, a path is listed twice, an area names a directory or file that does not exist, or a tracked Markdown file is reachable from neither the core nor any area. Bytes are counted after CRLF is folded to LF. The gate was added to the `Markdown Inventory Integrity` workflow.
- `CANONICAL_SESSION_READ_LAW.md` became v2 with the core and area rule. It states plainly that a receipt proves delivery of the core at a given content hash but not comprehension, and that no program checks a session's read. Removed the duplicate condensed English paragraphs of §2, §3, §5, §6 and §10, which restated the old rule.
- In `README.md`, `PROJECT_CONTEXT.md`, `AI_WORKING_CONTEXT.md`, `NEXT_CHAT_HANDOFF.md`, `foundation/README.md`, `foundation/PROJECT_CONTEXT.md`, `foundation/ai-collaboration/PROJECT_CONTEXT.md`, `platforms/design/PROJECT_CONTEXT.md` and `platforms/design/NEXT_CHAT_HANDOFF.md`, the restatement of the old rule and the “machine-enforced” claim about D-026 were replaced with what is actually checked.
- One universal maximum for every MenQ repository, 350,000 bytes, in the gate's code; MenQ Standard declares 120,000 in its manifest.
- `MARKDOWN_INVENTORY.json` and its drift check remain. D-028 requires the same rule of consumer repositories, but no adoption mechanism exists yet; that is a later decision.

## 2026-10-08 — CR-0011: repository front page standard v1

### Հայերեն

- Repo-ի առաջին էջի ստանդարտ՝ շապիկի նկարներ (light, dark, հեռախոս) և README-ի առաջին բլոկ («Start here» և չորս տողանոց ամփոփում HY/EN)։ Generator՝ `platforms/design/repository-front/make_front.py`։ Կիրառված է MenQ Studio-ի բոլոր repo-ներում և Scout client նախագծում։

### English

- Repository front page standard: cover pictures (light, dark, phone) and a README front block (Start here and a four-row summary in HY/EN). Generator: `platforms/design/repository-front/make_front.py`. Applied to every MenQ Studio repository and to the Scout client project.

## 2026-10-08 — CR-0010: motion, logo power-on, video and shader rules

### Հայերեն

- Շարժման կանոններ՝ սկզբունքներ, ժամանակներ, easing, անվանված pattern-ներ (`fade`, `rise`, `rise-sm`, `scale`) և նոր `Reveal` կոմպոնենտ։
- `BrandMark powerOn`՝ լոգոյի power-on անիմացիա։ Նոր token-ներ՝ `duration-power-on`, `motion-stagger`, `motion-distance-sm/md`։ Reduced motion-ի դեպքում ամեն անիմացիա անջատված է։
- Վիդեոյի կանոններ (autoplay, pause, ենթագրեր, ֆորմատ) և shader-ների սահման (միայն optional package, նոր CR-ով)։
- `tokens.json` mirror-ը հիմա ներառում է `motion` խումբը և `icon-stroke`-ը, որոնք նախկինում բաց էին թողնված։

### English

- Motion rules: principles, timing, easing, named patterns (`fade`, `rise`, `rise-sm`, `scale`) and a new `Reveal` component.
- `BrandMark powerOn`: the logo power-on animation. New tokens: `duration-power-on`, `motion-stagger`, `motion-distance-sm/md`. Every animation is switched off under reduced motion.
- Video rules (autoplay, pause, captions, format) and the shader boundary (optional package only, through a new CR).
- The `tokens.json` mirror now includes the `motion` group and `icon-stroke`, which were previously left out.

## 2026-10-08 — CR-0009: iconography, Accordion, Nav, Tooltip

### Հայերեն

- Իկոնագրության կանոն՝ Lucide, 24 grid, նոր token-ներ `--icon-size-sm/md/lg` և `--icon-stroke`, `Icon` կոմպոնենտ։
- Նոր `Accordion` (WAI-ARIA disclosure), `Nav` (`aria-current`), `Tooltip` (focus, Escape, `aria-describedby`)։ `Button`-ը փոխանցում է `aria-*`/`data-*` ատրիբուտները։ axe՝ 0 violation երկու թեմայում։

### English

- Iconography rule: Lucide, 24 grid, new tokens `--icon-size-sm/md/lg` and `--icon-stroke`, and an `Icon` component.
- New `Accordion` (WAI-ARIA disclosure), `Nav` (`aria-current`) and `Tooltip` (focus, Escape, `aria-describedby`). `Button` forwards `aria-*`/`data-*` attributes. axe: 0 violations in both themes.

## 2026-10-08 — CR-0008: app icon and favicon set

### Հայերեն

- Ավելացվեց `brand-expression/assets/Icons/`՝ favicon (ICO + SVG), Apple touch icon, PWA և maskable icon-ներ՝ պաշտոնական Q մարկից, asset record-ներով։

### English

- Added `brand-expression/assets/Icons/`: favicon (ICO + SVG), Apple touch icon, PWA and maskable icons made from the official Q mark, with asset records.

## 2026-10-08 — CR-0007: accessibility contract and form components

### Հայերեն

- `validate_brand_expression.py`-ը ստուգում է 17 տեքստ/ֆոն զույգ երկու թեմայում (34 ստուգում, ≥ 4.5:1, WCAG AA)։
- Ավելացվեցին `Checkbox`, `RadioGroup`, `Switch`, փաստաթղթավորվեցին `Textarea`, `Select`, `FormRow`։ `FormRow`-ը կապում է label-ը, hint-ը և error-ը control-ին։ Control-ների եզրերը 3:1 են։ axe՝ 0 violation երկու թեմայում։

### English

- `validate_brand_expression.py` checks 17 text/background pairs in both themes (34 checks, ≥ 4.5:1, WCAG AA).
- Added `Checkbox`, `RadioGroup`, `Switch`; documented `Textarea`, `Select`, `FormRow`. `FormRow` links the label, hint and error to its control. Control borders reach 3:1. axe: 0 violations in both themes.

## 2026-10-08 — CR-0006: primary action contrast

### Հայերեն

- Light theme-ում `color-action-primary`-ը դարձավ `#0369a1` (սպիտակ տեքստով 5.9:1), hover-ը՝ `#075985`, որ հիմնական կոճակները ցանկացած չափի դեպքում անցնեն WCAG AA-ն։ Dark theme-ը չի փոխվել։

### English

- In the light theme `color-action-primary` is now `#0369a1` (5.9:1 with white text) and its hover `#075985`, so primary buttons pass WCAG AA at any size. The dark theme is unchanged.

## 2026-10-08 — CR-0005: official BrandMark

### Հայերեն

- `BrandMark`-ը և `menq-wordmark-*`/`menq-q-mark-*` SVG-ները փոխարինվեցին պաշտոնական լոգոյից պատրաստված վեկտոր մարկով (կլորացված «Men» + neon power-ring Q)։ Նախկին Inter «Men» + ազուր pill տարբերակը սխալ էր։
- Ավելացվեց Բրոյի avatar-ի 1024×1024 master-ը։

### English

- `BrandMark` and the `menq-wordmark-*`/`menq-q-mark-*` SVGs are replaced by a vector mark made from the official logo (rounded "Men" + neon power-ring Q). The earlier Inter "Men" + azure pill version was wrong.
- Added the 1024×1024 master of Bro's avatar.

## 2026-10-08 — CR-0004: neon logo high-resolution master

### Հայերեն

- Ավելացվեց պաշտոնական neon լոգոյի բարձր լուծաչափի master-ը՝ `brand-expression/assets/Logos/menq-logo-neon-hires.png` (1913×720, թափանցիկ ֆոն), asset record-ով և SHA-256-ով։

### English

- Added the high-resolution master of the official neon logo, `brand-expression/assets/Logos/menq-logo-neon-hires.png` (1913×720, transparent), with an asset record and SHA-256.

## 2026-10-07 — CR-0003: brand custom-properties artifact

### Հայերեն

- Brand generator-ը արտադրում է նաև `tokens.vars.css`՝ միայն custom property-ներ, առանց class-երի և `@font-face`-ի, որպեսզի արտադրանքները (առաջինը՝ MenQ Webpage) կարողանան pinned copy օգտագործել առանց class-ների բախման։

### English

- The brand generator also emits `tokens.vars.css`: custom properties only, without classes or `@font-face`, so products (first MenQ Webpage) can use a pinned copy without class collisions.

## 2026-10-07 — Part 14 governance implementation Locked

### Հայերեն

- Owner-ը Part 14-ի implementation-ը հաստատեց `Locked`։ `CR-0002`-ը փակված է, registry-ում `menq.design.spec.governance.v1`-ը `Locked` է։

### English

- The Owner approved the Part 14 implementation as `Locked`. `CR-0002` is closed, and `menq.design.spec.governance.v1` is `Locked` in the registry.

## 2026-10-07 — Audit phase 6c: Part 14 governance implementation

### Հայերեն

- Part 14-ը իրականացվեց `platforms/design/governance/`-ում՝ ownership registry (48 canonical asset), approval matrix (5 class), change-request template և առաջին record-ները (`CR-0001` փակված, `CR-0002` հաստատված)։
- `validate_governance.py`-ը և `design-governance.yml`-ը ստուգում են ownership coverage-ը, approval matrix-ը, self-approval-ի արգելքը և պահանջում են `Change-Request: CR-NNNN` կամ `Change-Class: editorial` Design Platform-ի ֆայլեր փոխող ամեն PR-ում։ Ավելացվեց PR template։
- Part 13-ը backlog-ում է Owner-ի որոշմամբ։

### English

- Implemented Part 14 in `platforms/design/governance/`: ownership registry (48 canonical assets), approval matrix (5 classes), change-request template and the first records (`CR-0001` closed, `CR-0002` approved).
- `validate_governance.py` and `design-governance.yml` check ownership coverage, the approval matrix and the self-approval ban, and require `Change-Request: CR-NNNN` or `Change-Class: editorial` on every PR that changes Design Platform files. Added a PR template.
- Part 13 is in the backlog by Owner decision.

## 2026-10-07 — Audit phase 6a: D-024 lock, releases and D-025 evidence correction

### Հայերեն

- D-024 Platforms Architecture v1-ը `Locked` է Owner-ի հաստատմամբ. lock-ի երեք պայմանները գրանցված են decision-ում։
- Հրապարակվեցին մշտական GitHub Release-ներ՝ `foundation-v1.0.0` (Foundation v1 ZIP + `SHA256SUMS.txt`) և `design-platform-v0.1.0-next.0` (preview bundle)։
- D-025 evidence-ը ուղղվեց՝ առանց պատմությունը վերագրելու. ժամկետանց workflow artifact-ը փոխարինվեց մշտական release-ով, իսկ repo-ի ներսի երկու consumer-ը վերագնահատվեց M2 pilot (M3/M4-ը self-attested էր)։ D-025-ը մնում է Locked, իրական consumer-ի պարտավորությունը (MenQ Webpage) բաց է։
- Consumer build-երը և `validate_consumers.py`-ը այլևս չեն հայտարարում M3/M4 կամ production equivalence։ Platforms validator-ը պահանջում է evidence correction-ը, մշտական release-ի digest-ը և M2-ից ոչ բարձր grade։

### English

- D-024 Platforms Architecture v1 is `Locked` with Owner approval; the three lock conditions are recorded in the decision.
- Published permanent GitHub Releases: `foundation-v1.0.0` (Foundation v1 ZIP + `SHA256SUMS.txt`) and `design-platform-v0.1.0-next.0` (preview bundle).
- Corrected D-025 evidence without rewriting history: the expired workflow artifact is replaced by the permanent release, and the two in-repo consumers are re-graded to M2 pilots (M3/M4 was self-attested). D-025 remains Locked; the real-consumer obligation (MenQ Webpage) is open.
- Consumer builds and `validate_consumers.py` no longer claim M3/M4 or production equivalence. The Platforms validator requires the evidence correction, the permanent release digest and a grade no higher than M2.

## 2026-10-07 — Audit phase 6b: permanent release publishing

### Հայերեն

- Ավելացվեց `publish-release.yml` workflow-ը. `foundation-v*` և `design-platform-v*` tag-երը `main`-ի վրա կառուցում և հրապարակում են GitHub Release՝ մշտական asset-ով և SHA-256-ով։ Սա փոխարինում է 30/90 օրում ջնջվող workflow artifact-ները որպես release evidence։

### English

- Added the `publish-release.yml` workflow: `foundation-v*` and `design-platform-v*` tags on `main` build and publish a GitHub Release with a permanent asset and SHA-256. This replaces 30/90-day workflow artifacts as release evidence.

## 2026-10-07 — Audit phase 5: bilingual completion (R-05 reopened and closed)

### Հայերեն

- Documentation, AI Collaboration, Governance և Decision System chapter-ների, Canonical Write Integrity և Canonical Session Read օրենքների, D-024-ի, D-025-ի, D-026-ի, D-027-ի, audit/validation գրառումների, root README/ROADMAP/DECISION_INDEX-ի և Platforms փաստաթղթերի միալեզու բաժինները ստացան լիարժեք հայերեն կամ անգլերեն համարժեք։
- Գոյություն ունեցող տեքստը չի ջնջվել կամ վերաձևակերպվել. ավելացվել են միայն թարգմանություններ և `**HY:**`/`**EN:**` label-ներ։ D-025-ում (Locked) փոփոխությունը միայն parity-ի ավելացում է, իմաստը չի փոխվել։
- Օրենքների այն բաժիններում, որտեղ անգլերենը միայն կրճատ ամփոփում էր, ավելացվեց ամբողջական անգլերեն ցանկ։
- R-05-ը վերաբացվեց և փակվեց (`foundation/FOUNDATION_V1_REAUDIT.md`)։ Foundation validator-ը ստուգում է `**HY:**`/`**EN:**` label parity-ն բոլոր tracked Markdown-ների յուրաքանչյուր բաժնում։

### English

- Single-language sections received complete Armenian or English counterparts in the Documentation, AI Collaboration, Governance and Decision System chapters, the Canonical Write Integrity and Canonical Session Read laws, D-024, D-025, D-026, D-027, the audit/validation records, the root README/ROADMAP/DECISION_INDEX and the Platforms documents.
- No existing text was deleted or reworded; only translations and `**HY:**`/`**EN:**` labels were added. In D-025 (Locked) the change is parity-only and does not alter meaning.
- Where the laws' English was only a condensed summary, a complete English list was added.
- R-05 reopened and closed (`foundation/FOUNDATION_V1_REAUDIT.md`). The Foundation validator checks `**HY:**`/`**EN:**` label parity in every section of all tracked Markdown.

## 2026-10-07 — Audit phase 4: workflow security

### Հայերեն

- Բոլոր 7 workflow-ները ունեն top-level `permissions: contents: read`։
- Բոլոր third-party action-ները pin են արված ամբողջական commit SHA-ով (major tag-ը մեկնաբանությունում)։
- Design Platform workspace-ը ունի `pnpm-lock.yaml`, CI-ը տեղադրում է `--frozen-lockfile`-ով։
- Ավելացվեցին `.gitignore` և `.gitattributes` (LF line ending-ներ, binary ֆայլեր, generated lockfile)։
- Foundation validator-ը RED է տալիս, եթե workflow-ը չունի `permissions`, action-ը pin չէ SHA-ով կամ օգտագործվում է `--no-frozen-lockfile`։ Foundation Integrity-ն գործարկվում է ցանկացած workflow-ի փոփոխության դեպքում։

### English

- All 7 workflows declare top-level `permissions: contents: read`.
- Every third-party action is pinned to a full commit SHA (major tag kept as a comment).
- The Design Platform workspace has a `pnpm-lock.yaml`; CI installs with `--frozen-lockfile`.
- Added `.gitignore` and `.gitattributes` (LF line endings, binary files, generated lockfile).
- The Foundation validator goes RED when a workflow lacks `permissions`, an action is not SHA-pinned, or `--no-frozen-lockfile` is used. Foundation Integrity runs on any workflow change.

## 2026-10-07 — Audit phase 3: status synchronization

### Հայերեն

- D-025-ի `Locked` կարգավիճակը համաժամեցվեց Design Platform-ի architecture, baseline, README, Platforms registry և context ֆայլերում։ Registry-ի `status`-ը այժմ `Locked` է, և Phase A validator-ը պահանջում է, որ այն համընկնի D-025 record-ի կարգավիճակի հետ։
- `ECOSYSTEM_ARCHITECTURE.md`-ում Standard Mission-ը ցույց է տրվում որպես Locked (`D-011`), ֆայլը հղված է root README-ից։
- Ավելացվեցին END marker-ներ `DECISIONS.md`, `ECOSYSTEM_ARCHITECTURE.md` և Foundation chapter-ների փաստաթղթերում։ Foundation validator-ը դրանք պահանջում է, պահանջում է `D-027`-ը ինդեքսում և RED է տալիս, եթե marker-ով կառավարվող ֆայլը բացակայում է։
- D-027-ը և audit-ի վիճակը ավելացվեցին `PROJECT_CONTEXT.md`, `AI_WORKING_CONTEXT.md`, `NEXT_CHAT_HANDOFF.md`, `ROADMAP.md`-ում։ Հեռացվեց հնացած «D-026 validator-ը դեռ պետք է» տեքստը։
- Lock-ից առաջ գրված D-025 audit/review գրառումները նշվեցին որպես historical snapshot, Foundation remediation changelog-ը՝ որպես փոխարինված validation evidence-ով։

### English

- Synchronized D-025's `Locked` status across the Design Platform architecture, baseline, README, Platforms registry and context files. The registry `status` is now `Locked`, and the Phase A validator requires it to mirror the D-025 record status.
- `ECOSYSTEM_ARCHITECTURE.md` shows the Standard Mission as Locked (`D-011`) and is linked from the root README.
- Added END markers to `DECISIONS.md`, `ECOSYSTEM_ARCHITECTURE.md` and the Foundation chapter documents. The Foundation validator requires them, requires `D-027` in the index, and goes RED when a marker-governed file is missing.
- Added D-027 and the audit state to `PROJECT_CONTEXT.md`, `AI_WORKING_CONTEXT.md`, `NEXT_CHAT_HANDOFF.md` and `ROADMAP.md`. Removed the stale "D-026 validator still needed" text.
- Marked the pre-lock D-025 audit and review records as historical snapshots, and the Foundation remediation changelog as superseded by validation evidence.

## 2026-10-07 — Audit phase 2: validator hardening

### Հայերեն

- Foundation validator-ը ստուգում է բոլոր tracked Markdown-ների relative հղումները և որ ամեն `D-0xx` decision ֆայլ գրանցված է `DECISION_INDEX.md`-ում։ Ուղղվեց D-023-ի կոտրված հղումը։
- Platforms validator-ը `platforms/**/*.md`-ի բոլոր ֆայլերից պահանջում է հայերեն և անգլերեն բաժին և END marker։ Ավելացվեցին բացակայող END marker-ները release փաստաթղթերում։
- Phase A validator-ը կիրառում է registry-ի և token source-ի JSON Schema-ները և հայտնաբերում է չգրանցված package-ները։ Registry schema-ն ընդունում է `$schema`։
- Token build-ը արգելում է CSS custom property-ի բախումները, foundations build-ը ստուգում է `var(--x, fallback)`-ը և բոլոր package-ների CSS-ը։
- Public API validator-ը ստուգում է `index.js`/`index.d.ts` export parity-ն և դատարկ baseline-ը։ Baseline-ը սառեցված է `0.1.0-next.0` preview-ի վրա։
- Workflow-ների path filter-ները ծածկում են validator-ներն ու build script-երը։

### English

- The Foundation validator checks every relative link in tracked Markdown and that every `D-0xx` decision file is registered in `DECISION_INDEX.md`. Fixed the broken D-023 link.
- The Platforms validator requires Armenian and English sections and an END marker in every `platforms/**/*.md` file. Added the missing END markers to the release documents.
- The Phase A validator enforces the registry and token-source JSON Schemas and detects unregistered packages. The registry schema accepts `$schema`.
- The token build rejects CSS custom-property collisions; the foundations build checks `var(--x, fallback)` and every package's CSS.
- The public API validator checks `index.js`/`index.d.ts` export parity and an empty baseline. The baseline is frozen at the `0.1.0-next.0` preview.
- Workflow path filters cover the validators and build scripts.

## 2026-10-07 — D-027 MenQ Brand Expression Layer v1

### Հայերեն

- PR #7-ով առանց governance մտած `platforms/design/menq-design-system/` փաթեթը բերվեց D-027-ի ներքո և վերանվանվեց `platforms/design/brand-expression/`։
- Ավելացվեց canonical brand token source (`menq.design.token.*` ID-ներ, hy/en նկարագրություններ, owner, lifecycle, light/dark mode-եր) և generator՝ drift ստուգումով։
- Բրոյի ինքնությունը և 5 գործակալային կոմպոնենտ տեղափոխվեցին `platforms/design/product-extensions/bro/`։
- Ռուսերենը սահմանվեց որպես locale pack, canonical աղբյուրը՝ repository-ն։
- Ավելացվեցին asset records, bilingual փաստաթղթեր, `validate_brand_expression.py` և `design-brand-expression.yml` workflow։

### English

- Brought the ungoverned PR #7 package `platforms/design/menq-design-system/` under D-027 and renamed it `platforms/design/brand-expression/`.
- Added a canonical brand token source (`menq.design.token.*` IDs, hy/en descriptions, owner, lifecycle, light/dark modes) and a generator with a drift check.
- Moved Bro's identity and five agent components to `platforms/design/product-extensions/bro/`.
- Defined Russian as a locale pack and the repository as the canonical source.
- Added asset records, bilingual documentation, `validate_brand_expression.py` and the `design-brand-expression.yml` workflow.

## 2026-07-12 — Design Platform Part 16 package architecture

### Հայերեն

- Ավելացվել է canonical specification index և implementation package plan v1-ը։
- Սահմանվել են package boundaries, dependency direction, deterministic build graph, public API և release manifest contracts-ը։
- Continuation point-ը տեղափոխվել է D-025 completeness audit, validator design և Draft PR review։
- D-025-ը մնում է `Approved — Implementing`, Draft PR #3-ը՝ open, Draft և unmerged։

### English

- Added Canonical Specification Index and Implementation Package Plan v1.
- Defined package boundaries, dependency direction, deterministic build graph, public API, and release-manifest contracts.
- Advanced the continuation point to the D-025 completeness audit, validator design, and Draft PR review.
- D-025 remains `Approved — Implementing`; Draft PR #3 remains open, Draft, and unmerged.

## 2026-07-12 — Design Platform Part 15 adoption architecture

### Հայերեն

- Ավելացվել է product adoption, maturity model և two-consumer validation architecture v1-ը։
- Adoption-ը սահմանվել է որպես governed contract consumption և operational evidence, ոչ package install։
- Continuation point-ը տեղափոխվել է Part 16 — Canonical Specification Index and Implementation Package Plan։
- D-025-ը մնում է `Approved — Implementing`, Draft PR #3-ը՝ open, Draft և unmerged։

### English

- Added Product Adoption, Maturity Model, and Two-Consumer Validation Architecture v1.
- Defined adoption as governed contract consumption and operational evidence, not package installation.
- Advanced the continuation point to Part 16 — Canonical Specification Index and Implementation Package Plan.
- D-025 remains `Approved — Implementing`; Draft PR #3 remains open, Draft, and unmerged.

## 2026-07-12 — Design Platform Part 14 governance architecture

### Հայերեն

- Ավելացվել է governance, contribution, ownership և change-request lifecycle architecture v1-ը։
- Սահմանվել են authority model-ը, ownership registry-ն, contribution classes-ը, approval matrix-ը և lifecycle-ը։
- Unowned canonical asset-ը սահմանվել է որպես RED governance defect։
- High-risk կամ breaking change-ի self-approval-ը արգելվել է։
- Merge-ը սահմանվել է որպես առանձին authority action, ոչ GREEN CI-ի ավտոմատ հետևանք։
- Continuation point-ը տեղափոխվել է Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan։
- D-025-ը մնում է `Approved — Implementing`, Draft PR #3-ը մնում է open, Draft և unmerged։

### English

- Added Governance, Contribution, Ownership, and Change-Request Lifecycle Architecture v1.
- Defined the authority model, ownership registry, contribution classes, approval matrix, and lifecycle.
- Defined an unowned canonical asset as a RED governance defect.
- Prohibited self-approval for high-risk or breaking changes.
- Defined merge as a separate authority action, not an automatic consequence of green CI.
- Advanced the continuation point to Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.
- D-025 remains `Approved — Implementing`; Draft PR #3 remains open, Draft, and unmerged.

## 2026-07-12 — D-026 enforcement and Design Platform Part 12

### Հայերեն

- D-026 Canonical Session Read Law-ը դարձել է enforceable՝ canonical Markdown inventory, path/size/SHA drift validation և strict GitHub Actions gate-ով։
- Ավելացվել է D-026 final GREEN validation record-ը՝ իրական workflow evidence-ով և truncation incident transparency-ով։
- Ավելացվել է Design Platform Part 12 validation, CI, conformance և quality-gates architecture-ը։
- Սահմանվել են յոթ sequential gates, GREEN/YELLOW/RED verdict semantics-ը, conformance profiles-ը, exception contract-ը և evidence contract-ը։
- Root և Design Platform contexts, roadmaps, changelogs և handoffs-ը տեղափոխվել են Part 13 continuation point-ի վրա։
- D-025-ը մնում է `Approved — Implementing`, Draft PR #3-ը մնում է open, Draft և unmerged։

### English

- Made D-026 Canonical Session Read Law enforceable through a canonical Markdown inventory, path/size/SHA drift validation, and a strict GitHub Actions gate.
- Added the final GREEN D-026 validation record with real workflow evidence and transparent recording of the truncation incident.
- Added Design Platform Part 12 validation, CI, conformance, and quality-gates architecture.
- Defined seven sequential gates, GREEN/YELLOW/RED verdict semantics, conformance profiles, the exception contract, and the evidence contract.
- Advanced root and Design Platform contexts, roadmaps, changelogs, and handoffs to the Part 13 continuation point.
- D-025 remains `Approved — Implementing`; Draft PR #3 remains open, Draft, and unmerged.

## 2026-07-12 — D-025 Design Platform architecture baseline synchronization

### Հայերեն

- D-025 MenQ Design Platform Architecture v1-ը synchronized է Owner-approved workshop Parts 1–11 baseline-ի հետ։
- Canonical token dependency model-ը սահմանվել է որպես Reference → Semantic → Component → Pattern → Product Extension։
- Theme, state, density, platform, viewport/container, locale/script, accessibility, motion preference և product expression-ը սահմանվել են որպես orthogonal dimensions։
- Controlled exceptions-ը սահմանվել են որպես governed temporary bypass, ոչ normal token layer։
- Armenian և English լեզուները հաստատվել են որպես հավասար canonical languages, additional languages-ը՝ on-demand locale packs։
- Թարմացվել են D-025 decision-ը, root և Design Platform contexts-ը, roadmaps-ը, changelog-ները, architecture/contracts-ը, AI working context-ը, handoff-ները և Draft PR #3 description-ը։
- Ավելացվել է `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`։
- D-025-ը մնում է `Approved — Implementing`, Draft PR #3-ը մնում է open, Draft և unmerged։

### English

- Synchronized D-025 MenQ Design Platform Architecture v1 with the Owner-approved workshop Parts 1–11 baseline.
- Defined the canonical token dependency model as Reference → Semantic → Component → Pattern → Product Extension.
- Defined theme, state, density, platform, viewport/container, locale/script, accessibility, motion preference, and product expression as orthogonal dimensions.
- Defined controlled exceptions as governed temporary bypasses, not a normal token layer.
- Confirmed Armenian and English as equal canonical languages and additional languages as on-demand locale packs.
- Updated the D-025 decision, root and Design Platform contexts, roadmaps, changelogs, architecture/contracts, AI working context, handoffs, and Draft PR #3 description.
- Added `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`.
- D-025 remains `Approved — Implementing`; Draft PR #3 remains open, Draft, and unmerged.

## 2026-07-12 — Foundation v1 validation and packaging

### Հայերեն

- `Foundation Integrity` workflow run `#9`-ը ավարտվել է `success` conclusion-ով։
- Validator-ը վերադարձրել է `FOUNDATION VALIDATION: GREEN` և հաստատել է յոթ Foundation chapter-ներն ու root controls-ը։
- `foundation/FOUNDATION_V1_VALIDATION_RUN.md` final validation record-ը թարմացվել է GREEN evidence-ով։
- Root README-ը, project contexts-ը, AI working context-ը, Foundation index-ը և Roadmap-ը synchronized են GREEN release gate-ի հետ։
- Ավելացվել է `release/FOUNDATION_V1_RELEASE_README.md`։
- Ավելացվել է `.github/workflows/foundation-v1-package.yml`՝ validated ZIP snapshot, SHA-256 manifest և missing-file verification ստեղծելու համար։
- Foundation v1 ZIP-ը սահմանվել է որպես GitHub Release asset, ոչ main branch binary file։
- Հաջորդ architecture աշխատանքը Platforms formal Decision System proposal-ն է՝ Owner approval-ով։

### English

- `Foundation Integrity` workflow run `#9` completed with a `success` conclusion.
- The validator returned `FOUNDATION VALIDATION: GREEN` and confirmed seven Foundation chapters and root controls.
- The final validation record in `foundation/FOUNDATION_V1_VALIDATION_RUN.md` was updated with GREEN evidence.
- The root README, project contexts, AI working context, Foundation index, and Roadmap were synchronized with the GREEN release gate.
- Added `release/FOUNDATION_V1_RELEASE_README.md`.
- Added `.github/workflows/foundation-v1-package.yml` to create the validated ZIP snapshot, SHA-256 manifest, and missing-file verification.
- The Foundation v1 ZIP is defined as a GitHub Release asset, not a binary file in the main branch.
- The next architecture work is a formal Decision System proposal for Platforms with Owner approval.

## 2026-07-12

### Հայերեն

- Ավելացվել է `PROJECT_CONTEXT.md`։
- Ֆիքսվել է MenQ Standard-ի canonical repository-ն։
- Ֆիքսվել է նոր chat-երում repository-ի հասցեն կրկին չհարցնելու կանոնը։
- Ֆիքսվել է ընկերական, հանգիստ և ուղիղ համագործակցության տոնը։
- Ֆիքսվել է ամբողջական փաթեթների և հնարավորության դեպքում ZIP deliverable-ի նախընտրությունը։
- Ավելացվել է `DECISIONS.md`՝ locked որոշումների համար։
- Ավելացվել է `ECOSYSTEM_ARCHITECTURE.md`։
- Lock է արվել MenQ Standard-ի core hierarchy-ն։
- Lock է արվել Foundation և Philosophy hierarchy-ները։
- Ավելացվել է `foundation/README.md`։
- Ավելացվել է `foundation/philosophy/README.md`։
- Հստակ բաժանվել են MenQ Studio-ի company vision/mission-ը և MenQ Standard-ի standard vision/mission-ը։
- MenQ Studio-ի company mission-ը գրանցվել է canonical ձևով։
- Lock է արվել MenQ Standard-ի mission-ը։
- Lock են արվել MenQ Standard-ի Core Beliefs-ը։
- Lock է արվել MenQ Standard-ի Human–AI Philosophy-ն։
- Lock է արվել MenQ Standard-ի Design Philosophy-ն։
- Ավելացվել և lock է արվել `foundation/philosophy/ENGINEERING_PHILOSOPHY.md` ամբողջական bilingual chapter-ը։
- Engineering Philosophy-ն գրանցվել է `D-015` որոշմամբ։
- Վերականգնվել է կիսատ `AI_WORKING_CONTEXT.md` continuity փաստաթուղթը՝ միայն canonical փաստերից։
- Ավելացվել և lock է արվել `foundation/philosophy/PRODUCT_PHILOSOPHY.md` ամբողջական bilingual chapter-ը։
- Product Philosophy-ն գրանցվել է `D-016` որոշմամբ։
- Philosophy chapter-ի ամբողջ բովանդակությունը ստացել է `Locked` կարգավիճակ։
- Ավելացվել և lock է արվել `foundation/principles/README.md`՝ 16 bilingual MenQ Principles-ով։
- Ավելացվել է `Measurable Outcomes` principle-ը՝ baseline, KPI, target, owner և measurement cadence պարտադիր կառուցվածքով։
- MenQ Principles-ը գրանցվել է `D-017` որոշմամբ և կապվել Foundation index-ին։
- Ավելացվել և lock է արվել `foundation/terminology/README.md`՝ որպես Terminology v1.0 living glossary։
- Terminology v1-ի evolution rule-ը սահմանում է traceable, bilingual և history-preserving թարմացումներ։
- Terminology v1-ը գրանցվել է `D-018` որոշմամբ։
- Ավելացվել և lock է արվել `foundation/governance/README.md`՝ որպես Governance v1.0։
- Governance v1-ը գրանցվել է `D-019` որոշմամբ և կապվել Foundation index-ին։
- Վերականգնվել է պատահաբար կիսատ դարձած `CHANGELOG.md` canonical history-ն Git history-ից։
- Ավելացվել և lock է արվել `foundation/decision-system/README.md`՝ որպես Decision System v1.0։
- Decision System v1-ը գրանցվել է `D-020` որոշմամբ և կապվել Foundation index-ին։
- Decision System-ը lock է արել `C0–C4` decision classes-ը, `R0–R4` risk levels-ը, lifecycle-ը, seven gates-ը, `GREEN/YELLOW/RED` outcomes-ը և history-preserving change rule-ը։
- Ավելացվել և lock է արվել `foundation/documentation/README.md`՝ որպես Documentation Standard v1.0։
- Documentation Standard v1-ը գրանցվել է `D-021` որոշմամբ և կապվել Foundation index-ին։
- Lock են արվել core documentation file roles-ը, bilingual equality-ն, single-source rule-ը, safe replacement-ը և post-write integrity verification-ը։
- Ավելացվել է root `ROADMAP.md`։
- Ավելացվել է `foundation/PROJECT_CONTEXT.md`։
- Նախկինում կիսատ դարձած `AI_WORKING_CONTEXT.md`-ը ամբողջությամբ վերականգնվել և synchronized է ընթացիկ canonical վիճակի հետ։
- Canonical documentation write-երի համար պարտադիր է դարձել post-write re-read և beginning/end integrity verification-ը։
- Ավելացվել և lock է արվել `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md` օրենքը։
- Canonical Write Integrity Law-ը գրանցվել է dedicated `D-022` record-ով։
- Վերականգնվել է նախորդ write-ով վնասված root `README.md`-ը և ավելացվել canonical navigation-ը։
- Ավելացվել և lock է արվել `foundation/ai-collaboration/README.md`՝ որպես AI Collaboration Standard v1.0։
- Ավելացվել է `foundation/ai-collaboration/PROJECT_CONTEXT.md`։
- AI Collaboration Standard v1-ը գրանցվել է dedicated `D-023` record-ով։
- Foundation-ի բոլոր յոթ chapter-ները կառուցվել և lock են արվել։
- Foundation-ի հաջորդ քայլը սահմանվել է որպես ամբողջական consistency, bilingual parity, link և documentation integrity audit։

### English

- Added `PROJECT_CONTEXT.md`.
- Recorded the canonical MenQ Standard repository.
- Recorded the rule not to request the repository address again in new chats.
- Recorded the friendly, calm, and direct collaboration tone.
- Recorded the preference for complete packages and ZIP deliverables when possible.
- Added `DECISIONS.md` for locked decisions.
- Added `ECOSYSTEM_ARCHITECTURE.md`.
- Locked the MenQ Standard core hierarchy.
- Locked the Foundation and Philosophy hierarchies.
- Added `foundation/README.md`.
- Added `foundation/philosophy/README.md`.
- Clearly separated MenQ Studio company vision/mission from MenQ Standard standard vision/mission.
- Recorded the MenQ Studio company mission canonically.
- Locked the MenQ Standard mission.
- Locked the MenQ Standard Core Beliefs.
- Locked the MenQ Standard Human–AI Philosophy.
- Locked the MenQ Standard Design Philosophy.
- Added and locked the complete bilingual `foundation/philosophy/ENGINEERING_PHILOSOPHY.md` chapter.
- Recorded Engineering Philosophy as decision `D-015`.
- Repaired the truncated `AI_WORKING_CONTEXT.md` continuity document using only canonical facts.
- Added and locked the complete bilingual `foundation/philosophy/PRODUCT_PHILOSOPHY.md` chapter.
- Recorded Product Philosophy as decision `D-016`.
- Set the complete Philosophy chapter content status to `Locked`.
- Added and locked `foundation/principles/README.md` with 16 bilingual MenQ Principles.
- Added the `Measurable Outcomes` principle with mandatory baseline, KPI, target, owner, and measurement cadence.
- Recorded MenQ Principles as decision `D-017` and linked the chapter from the Foundation index.
- Added and locked `foundation/terminology/README.md` as the Terminology v1.0 living glossary.
- Defined the Terminology v1 evolution rule for traceable, bilingual, history-preserving updates.
- Recorded Terminology v1 as decision `D-018`.
- Added and locked `foundation/governance/README.md` as Governance v1.0.
- Recorded Governance v1 as decision `D-019` and linked it from the Foundation index.
- Restored the accidentally truncated `CHANGELOG.md` canonical history from Git history.
- Added and locked `foundation/decision-system/README.md` as Decision System v1.0.
- Recorded Decision System v1 as decision `D-020` and linked it from the Foundation index.
- Locked the `C0–C4` decision classes, `R0–R4` risk levels, lifecycle, seven gates, `GREEN/YELLOW/RED` outcomes, and history-preserving change rule.
- Added and locked `foundation/documentation/README.md` as Documentation Standard v1.0.
- Recorded Documentation Standard v1 as decision `D-021` and linked it from the Foundation index.
- Locked the core documentation file roles, bilingual equality, the single-source rule, safe replacement, and post-write integrity verification.
- Added the root `ROADMAP.md`.
- Added `foundation/PROJECT_CONTEXT.md`.
- Fully restored the previously truncated `AI_WORKING_CONTEXT.md` and synchronized it with the current canonical state.
- Made post-write re-reading and beginning/end integrity verification mandatory for canonical documentation writes.
- Added and locked the `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md` law.
- Recorded the Canonical Write Integrity Law in a dedicated `D-022` record.
- Restored the root `README.md` damaged by a previous write and added canonical navigation.
- Added and locked `foundation/ai-collaboration/README.md` as AI Collaboration Standard v1.0.
- Added `foundation/ai-collaboration/PROJECT_CONTEXT.md`.
- Recorded AI Collaboration Standard v1 in a dedicated `D-023` record.
- Built and locked all seven Foundation chapters.
- Set the next Foundation step as a complete consistency, bilingual parity, link, and documentation integrity audit.

<!-- END: MENQ_STANDARD_CHANGELOG -->