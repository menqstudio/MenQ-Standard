# D-029 — Consumer Adoption Layer / Consumer-ների ընդունման շերտ

**Decision ID:** `D-029`  
**Status / Կարգավիճակ:** Proposed — not approved. The approval is the Owner's merge of the pull request that carries this record, and nothing else / Proposed — հաստատված չէ. Հաստատումը Owner-ի կողմից այս record-ը պարունակող pull request-ի merge-ն է, և ուրիշ ոչինչ  
**Date / Ամսաթիվ:** 2026-10-09  
**Decision class / Որոշման դաս:** `C4 — Foundation or Ecosystem`  
**Risk level / Ռիսկի մակարդակ:** `R2 — Moderate`  
**Owner / Պատասխանատու:** MenQ Owner  
**Proposer / Առաջարկող:** AI collaborator (Claude), on a task from the Owner's orchestrating session on 2026-10-09  
**Reviewer / Վերանայող:** MenQ Owner, on the pull request. Reviewer and Approver are the same person; the overlap is disclosed under Governance §3.7  
**Approver / Հաստատող:** MenQ Owner — not yet. No approval is claimed by this text  
**Scope / Scope:** MenQ Standard, and every MenQ product repository that follows it  
**Supersedes / Փոխարինում է:** nothing. It supplies the adoption mechanism that `D-028` left to “a separate, later decision”; the text of `D-028` is unchanged apart from a dated pointer  
**Superseded by / Փոխարինված է:** —

## Problem / Խնդիր

**HY:** MenQ Standard-ը կանոններ է սահմանում product repository-ների համար, և `D-028`-ը նրանցից պահանջում է session-read manifest, byte budget և CI gate։ Բայց `main`-ի `f664ec3` commit-ում product repository-ն դա ընդունելու ոչ մի ճանապարհ չունի։ Չկա ստանդարտի տարբերակ․ `VERSION` ֆայլ չկա, իսկ երկու tag-ը (`foundation-v1.0.0`, `design-platform-v0.1.0-next.0`) ցույց են տալիս 2026-10-07-ի նույն `3793b3c` commit-ը, այսինքն `D-028`-ից առաջ։ Չկա ֆայլ, որով repository-ն ասի, թե որ տարբերակին է հետևում։ Չկա conformance ստուգում, որը repository-ն կարող է գործարկել․ `scripts/validate_foundation.py`-ը և `scripts/validate_platforms.py`-ը կարդում են այս repository-ի սեփական ուղիները, իսկ `scripts/check_session_read_budget.py`-ը ուներ `--root` և `--manifest` պարամետրեր, բայց նրա default-ը այս repository-ի manifest-ն էր, և այն ոչ մի տեղ չէր տարածվում։ Ինը workflow-ից ոչ մեկը `workflow_call` չունի։ Եվ ստանդարտի փոփոխությունը որևէ repository-ի հասնելու ճանապարհ չունի։ `D-028`-ը դա ինքն է ասում՝ «adoption մեխանիզմ դեռ գոյություն չունի»։ Առանց այդ շերտի ստանդարտի ամեն կանոն consumer-ի համար պահանջ է առանց ստուգման։

**EN:** MenQ Standard sets rules for product repositories, and `D-028` requires of them a session-read manifest, a byte budget and a CI gate. Yet at `main` commit `f664ec3` a product repository has no way to adopt any of it. There is no version of the standard: no `VERSION` file exists, and the two tags (`foundation-v1.0.0`, `design-platform-v0.1.0-next.0`) both point at commit `3793b3c` of 2026-10-07, which is before `D-028`. There is no file in which a repository says which version it follows. There is no conformance check a repository can run: `scripts/validate_foundation.py` and `scripts/validate_platforms.py` read this repository's own paths, and `scripts/check_session_read_budget.py` did have `--root` and `--manifest` parameters, but its default was this repository's manifest and it was distributed nowhere. None of the nine workflows has `workflow_call`. And a change to the standard has no way to reach any repository. `D-028` says so itself: “no adoption mechanism for consumer repositories exists yet”. Without that layer every rule of the standard is, for a consumer, a requirement without a check.

## Context / Կոնտեքստ

**HY:** Այս record-ը կազմողին փոխանցվել են Owner-ի հետևյալ որոշումները և նպատակը, բոլորը project conversation-ից, որը canonical source չէ․ (1) նպատակը՝ ամեն repository գնում է MenQ Standard, պարբերաբար ստուգում, թե ինչ է ավելացել կամ փոխվել, և թարմացվում է այնտեղից, (2) update-ը consumer-ում գալիս է որպես pull request և երբեք ավտոմատ merge չի արվում, (3) բոլոր repository-ների համար մեկ read-budget սահման՝ 350,000 բայթ (սա գրված է `D-028`-ում և gate-ի կոդում), (4) MenQ Standard-ը public է։ Կազմողին հաղորդվել է նաև, որ 2026-10-09-ին երեք անկախ reviewer նույն բացը գտել են, և որ `menqstudio`-ի տակ մոտ ինը product repository կա, որոնցից յոթը private են։ Այս վերջին երկուսը այս repository-ից չեն ստուգվել։ Այս record-ի տեքստը, kit-ի կազմը, pin-ի ձևաչափը և առաջին տարբերակի թիվը կազմել է AI-ն․ Owner-ը դրանք չի հաստատել, մինչև pull request-ը merge չանի։

**EN:** The drafter of this record was given the following decisions and goal of the Owner, all from the project conversation, which is not a canonical source: (1) the goal, that every repository goes to MenQ Standard, checks periodically what was added or changed, and updates itself from there; (2) an update arrives in a consumer as a pull request and is never merged automatically; (3) one read-budget ceiling for every repository, 350,000 bytes (this one is written in `D-028` and in the gate's code); (4) MenQ Standard is public. The drafter was also told that three independent reviewers found the same gap on 2026-10-09, and that about nine product repositories exist under `menqstudio`, seven of them private. Those last two statements were not checked from this repository. The text of this record, the composition of the kit, the format of the pin and the first version number were drafted by AI; the Owner has not approved them until the Owner merges the pull request.

## Decision / Որոշում

**HY:**

1. **Տարբերակ։** Ստանդարտն ունի մեկ տարբերակ՝ repository-ի root-ի `VERSION` ֆայլում, `MAJOR.MINOR.PATCH` ձևով։ Առաջին թիվը `2.0.0` է (տես «Ինչու այս տարբերակը»)։ `CHANGELOG.md`-ի վերնագիրը անվանում է ամեն տարբերակ՝ «MenQ Standard v…» ձևով։
2. **Consumer kit։** `consumer/` directory-ն պարունակում է այն ֆայլերը, որոնք product repository-ն պատճենում է անփոփոխ՝ session-read budget gate-ը, `sync_facts.py`-ը իր թեստերով և ձեռնարկով, conformance checker-ը, երկու workflow template, `CONSUMER_CONTRACT.md` և `ADOPTION.md`։ `consumer/KIT_MANIFEST.json`-ը թվարկում է kit-ի ամեն ֆայլ իր sha256-ով։ Kit-ի ֆայլի hash-ը նրա բայթերի sha256-ն է CRLF-ը LF դարձնելուց հետո։
3. **Մեկ իրականացում։** Budget gate-ի միակ իրականացումը `consumer/check_session_read_budget.py`-ն է․ `scripts/check_session_read_budget.py`-ը այն բեռնում է և տալիս է միայն այս repository-ի երկու default-ը։ Consumer-ի համար manifest-ի պայմանական ուղին root-ի `SESSION_READ_MANIFEST.json`-ն է, և այն պարամետր է։
4. **Pin։** Ստանդարտին հետևող repository-ն իր root-ում պահում է `.menq-standard.json`՝ ստանդարտի repository-ն, տարբերակը, այն ամբողջական commit-ը, որից վերցվել է kit-ը, kit-ի directory-ն, manifest-ի ուղին, kit-ի ամեն ֆայլի sha256-ը և ամեն render արված workflow-ի hash-ն ու commit-ը։
5. **Conformance։** Repository-ն հետևում է ստանդարտին, երբ `check_conformance.py check`-ը նրա վրա GREEN է։ Թե ինչ է դա պարտադրում՝ գրված է [`consumer/CONSUMER_CONTRACT.md`](../../consumer/CONSUMER_CONTRACT.md)-ում՝ երեք ցանկով (MUST, MUST NOT, ADVISORY), և MUST-ի ամեն կետ անվանում է իր ստուգումը։ `D-028`-ի consumer պահանջը այնտեղ MUST 4-ն է։
6. **Reusable workflow։** `.github/workflows/consumer-conformance.yml`-ը (`on: workflow_call`) checkout է անում կանչող repository-ն և ստանդարտը, ստանդարտը տեղափոխում է pin-ի նշած commit-ին միայն եթե այն `main`-ի վրա է, և գործարկում է checker-ի՝ ստանդարտում գտնվող պատճենը։ Repository-ն այն կանչում է ամբողջական commit SHA-ով։
7. **Update։** Update-ը repository-ին հասնում է միայն pull request-ով։ Kit-ի `menq-standard-update.yml` template-ը, որը repository-ն պատճենում է իր մեջ, ժամանակացույցով և ձեռքով fetch է անում ստանդարտը, համեմատում pin-ի հետ, և եթե pin-ը հետ է մնացել՝ թարմացնում է kit-ը և pin-ը ու բացում pull request՝ ստանդարտի changelog-ի համապատասխան հատվածով։ Այն երբեք merge կամ approve չի անում։ Ստանդարտը ոչ մի repository-ում write իրավունք չունի և չի ստանում։
8. **Gate-եր այս repository-ում։** `scripts/generate_kit_manifest.py --check`-ը RED է, երբ manifest-ը տարբերվում է ֆայլերից։ `scripts/check_standard_version.py`-ը RED է, երբ `consumer/`-ի կամ reusable workflow-ի ֆայլ փոխվել է base-ի նկատմամբ, իսկ `VERSION`-ը չի աճել։ `scripts/check_consumer_templates.py`-ը template-ները պահում է pinned SHA-ի, pipe-to-shell-ի արգելքի և «երբեք merge» կանոնների մեջ։ Բոլորը և նրանց թեստերը հայտարարված են `scripts/validate_foundation.py`-ի `REQUIRED_WORKFLOW_RUNS`-ում։
9. **Authority։** `CONSUMER_CONTRACT.md`-ի MUST կամ MUST NOT ցանկի փոփոխությունը ecosystem-wide պարտադիր կանոնի փոփոխություն է և պահանջում է Owner-ի հաստատում (`G4`)՝ pull request-ի merge-ով։ Kit-ի ցանկացած փոփոխություն կրում է ավելի բարձր տարբերակ։

**EN:**

1. **A version.** The standard has one version, in the file `VERSION` at the repository root, in the form `MAJOR.MINOR.PATCH`. The first number is `2.0.0` (see “Why this option”). A heading of `CHANGELOG.md` names every version, in the form “MenQ Standard v…”.
2. **A consumer kit.** The directory `consumer/` holds the files a product repository copies unchanged: the session-read budget gate, `sync_facts.py` with its tests and its manual, the conformance checker, two workflow templates, `CONSUMER_CONTRACT.md` and `ADOPTION.md`. `consumer/KIT_MANIFEST.json` lists every kit file with its sha256. The hash of a kit file is the sha256 of its bytes after CRLF is folded to LF.
3. **One implementation.** The only implementation of the budget gate is `consumer/check_session_read_budget.py`; `scripts/check_session_read_budget.py` loads it and supplies only this repository's two defaults. For a consumer the conventional manifest path is `SESSION_READ_MANIFEST.json` at the root, and it is a parameter.
4. **A pin.** A repository that follows the standard keeps `.menq-standard.json` at its root: the standard's repository, the version, the full commit the kit was taken from, the kit directory, the manifest path, the sha256 of every kit file, and the hash and commit of every rendered workflow.
5. **Conformance.** A repository follows the standard when `check_conformance.py check` is GREEN on it. What that enforces is written in [`consumer/CONSUMER_CONTRACT.md`](../../consumer/CONSUMER_CONTRACT.md) as three lists (MUST, MUST NOT, ADVISORY), and every MUST item names its check. The consumer requirement of `D-028` is MUST 4 there.
6. **A reusable workflow.** `.github/workflows/consumer-conformance.yml` (`on: workflow_call`) checks out the calling repository and the standard, moves the standard to the commit the pin names only when that commit is on `main`, and runs the standard's copy of the checker. A repository calls it at a full commit SHA.
7. **Updates.** An update reaches a repository only as a pull request. The kit's `menq-standard-update.yml` template, which a repository copies into itself, fetches the standard on a schedule and on demand, compares it with the pin, and when the pin is behind updates the kit and the pin and opens a pull request carrying the matching section of the standard's changelog. It never merges and never approves. The standard holds no write access to any repository and is given none.
8. **Gates in this repository.** `scripts/generate_kit_manifest.py --check` is RED when the manifest differs from the files. `scripts/check_standard_version.py` is RED when a file of `consumer/` or the reusable workflow changed against the base and `VERSION` did not increase. `scripts/check_consumer_templates.py` holds the templates to the pinned-SHA rule, the ban on piping a download into a shell, and the “never merges” rule. All of them and their tests are declared in `REQUIRED_WORKFLOW_RUNS` of `scripts/validate_foundation.py`.
9. **Authority.** A change to the MUST or MUST NOT list of `CONSUMER_CONTRACT.md` is a change to an ecosystem-wide mandatory rule and requires Owner approval (`G4`) through the merge of a pull request. Any change to the kit carries a higher version.

## What the mechanism proves and does not prove / Ինչ է ապացուցում մեխանիզմը և ինչ չի ապացուցում

**HY:** Checker-ը, գործարկված առանց ստանդարտի (`--standard` չկա), ապացուցում է միայն ներքին համաձայնությունը՝ pin-ը ճիշտ ձևի է, ֆայլերը ունեն pin-ում գրված hash-երը, budget gate-ը GREEN է։ Այդ ռեժիմում repository-ն կարող է kit-ի ֆայլը փոխել և pin-ում գրել նոր hash-ը, և արդյունքը կմնա GREEN․ output-ը ամեն գործարկման ժամանակ ասում է, որ ստանդարտի հետ համեմատությունը չի կատարվել։ Միայն `--standard`-ով, այսինքն reusable workflow-ում, ապացուցվում է, որ pin-ի commit-ը ստանդարտի `main`-ի վրա է, և որ տարբերակը և hash-երը ստանդարտինն են։ Ոչ մի ծրագիր չի ապացուցում, որ repository-ն ընդհանրապես ընդունել է ստանդարտը, որ նրա Actions-ը միացված է, որ conformance run-ը պարտադիր status check է, կամ որ update pull request-ը որևէ մեկը կարդացել է։ Reusable workflow-ը և update template-ը GitHub-ում երբեք չեն գործարկվել․ ստուգվել են միայն local, ժամանակավոր repository-ներում, որտեղ GitHub-ը փոխարինված էր local clone-ով և `gh`-ի փոխարինիչով։ Ուստի ճիշտ ձևակերպումն է՝ «մեխանիզմը կա և local փորձարկված է», ոչ թե «consumer-ները ստուգվում են CI-ում»։

**EN:** The checker, run without the standard (no `--standard`), proves internal consistency only: the pin is well-formed, the files have the hashes the pin records, the budget gate is GREEN. In that mode a repository can change a kit file and write the new hash into its pin, and the result stays GREEN; the output says on every run that the comparison with the standard did not happen. Only with `--standard`, that is, in the reusable workflow, is it proved that the pin's commit is on the standard's `main` and that the version and the hashes are the standard's own. No program proves that a repository adopted the standard at all, that its Actions is enabled, that the conformance run is a required status check, or that anybody read an update pull request. The reusable workflow and the update template have never run on GitHub: they were exercised only locally, in temporary repositories, with GitHub replaced by a local clone and a stand-in for `gh`. The correct statement is therefore “the mechanism exists and was exercised locally”, not “consumers are checked in CI”.

## Alternatives considered / Դիտարկված այլընտրանքներ

**HY:**

- (ա) **Git submodule** — մերժվեց։ Submodule-ը իսկապես pin է անում commit, և Dependabot-ը կարող է submodule-ի համար pull request բացել․ դրանք նրա ուժեղ կողմերն են։ Բայց այն repository-ի մեջ բերում է ամբողջ ստանդարտը (311 tracked ֆայլ, մոտ 4.96 MB `f664ec3`-ում), ոչ թե ինը ֆայլ․ առանց `--recurse-submodules`-ի clone-ում գործիքները բացակայում են, և gate-ը չի գործարկվում․ submodule-ի ֆայլերը repository-ի tracked ֆայլեր չեն, ուստի budget gate-ի orphan ստուգումը դրանք չի տեսնում․ submodule-ի update pull request-ը ցույց է տալիս միայն փոխված SHA, ոչ թե ինչ է փոխվել։
- (բ) **Հրապարակված package** (PyPI, npm կամ GitHub Packages) — մերժվեց։ Այն պահանջում է registry, release գործընթաց և publish credentials, որոնք այսօր չկան, և release-ը Owner-ի authority-ն է։ Repository-ին CI-ում և AI session-ի մեկնարկին պետք կլիներ ցանց և installer։ Package-ը չի բերում workflow ֆայլերը և Markdown կանոնները։ Kit-ը ինը ֆայլ է առանց dependency-ների․ package-ը դրա համար ավելորդ բարդություն է (Principles․ Complexity Must Earn Its Place)։
- (գ) **Ստանդարտը commit է push անում consumer-ների մեջ** — մերժվեց։ Դա պահանջում է, որ public repository-ն պահի write credential բոլոր product repository-ների համար, ներառյալ private-ները։ Դա հակասում է այս repository-ի սեփական workflow policy-ին (`contents: read`), Governance §3.3-ին (նվազագույն անհրաժեշտ authority) և Owner-ի որոշմանը, որ update-ը գալիս է pull request-ով։
- (դ) **Պատճեն առանց pin-ի** — մերժվեց։ Սա այսօրվա փաստացի վիճակն է։ Առանց pin-ի հնարավոր չէ ասել, թե որ տարբերակն է պատճենված, հնարավոր չէ հայտնաբերել local խմբագրումը, և հնարավոր չէ իմանալ, որ պատճենը հնացել է։ Պատճենը, որը ոչ ոք չի կարող ստուգել, fork է։
- (ե) **Միայն reusable workflow, առանց local պատճենի** — մերժվեց որպես միակ մեխանիզմ։ Այդ դեպքում ոչինչ չի գործարկվում առանց ցանցի և առանց GitHub-ի, և AI session-ը չի կարող gate-ը գործարկել push-ից առաջ։ Նրա ուժեղ կողմը պահպանված է․ CI-ի վճիռը տալիս է ստանդարտի պատճենը։
- (զ) **Consumer-ը կանչում է ստանդարտի `main`-ը առանց SHA-ի** — մերժվեց։ Չամրացված `uses`-ը RED է այս repository-ի policy-ով, և ստանդարտի մեկ փոփոխությունը միանգամից կկարմրեցներ բոլոր repository-ները առանց նրանց կողմից որևէ փոփոխության։

**EN:**

- (a) **A git submodule** — rejected. A submodule does pin a commit, and Dependabot can open pull requests for a submodule; those are its strengths. But it brings the whole standard into the repository (311 tracked files, about 4.96 MB at `f664ec3`) rather than nine files; in a clone made without `--recurse-submodules` the tools are absent and the gate does not run; the files of a submodule are not tracked files of the repository, so the orphan check of the budget gate does not see them; and a submodule update pull request shows only a changed SHA, not what changed.
- (b) **A published package** (PyPI, npm or GitHub Packages) — rejected. It needs a registry, a release process and publishing credentials, none of which exist today, and release is the Owner's authority. A repository would need the network and an installer in CI and at the start of an AI session. A package does not deliver workflow files or the Markdown rules. The kit is nine files with no dependencies; a package is complexity that has not earned its place (Principles: Complexity Must Earn Its Place).
- (c) **The standard pushing commits into consumers** — rejected. It requires a public repository to hold a write credential for every product repository, the private ones included. That contradicts this repository's own workflow policy (`contents: read`), Governance §3.3 (least necessary authority) and the Owner's decision that an update arrives as a pull request.
- (d) **A copy with no pin** — rejected. This is the de-facto state today. Without a pin nobody can say which version was copied, a local edit cannot be detected, and nobody can know that the copy went stale. A copy nobody can verify is a fork.
- (e) **A reusable workflow only, with no local copy** — rejected as the only mechanism. Nothing would run without the network and without GitHub, and an AI session could not run the gate before pushing. Its strength is kept: the verdict in CI is given by the standard's copy.
- (f) **A consumer calling the standard's `main` with no SHA** — rejected. An unpinned `uses` is RED under this repository's policy, and one change to the standard would turn every repository RED at once without any change on their side.

## Why this option / Ինչու այս տարբերակը

**HY:** Պատճեն և pin՝ միասին, միակ տարբերակն է, որտեղ gate-ը աշխատում է առանց ցանցի (AI session-ը այն գործարկում է local), և միաժամանակ ամեն պատճեն ստուգելի է ստանդարտի դեմ։ Ընդունված trade-off-ը՝ kit-ի ֆայլերը կրկնվում են ամեն repository-ում, և update-ը պահանջում է մարդու merge ամեն repository-ում։ Երկրորդը Owner-ի որոշումն է, ոչ թե թերություն։

Առաջին տարբերակի թիվը `2.0.0` է երեք պատճառով։ (1) `foundation-v1.0.0` tag-ը արդեն կա և ցույց է տալիս `D-028`-ից առաջվա commit․ եթե ստանդարտի տարբերակը նույնպես `1.0.0` լիներ, երկու տարբեր բան նույն թիվը կկրեին։ (2) `foundation-v1.0.0`-ից հետո `D-028`-ը մասամբ փոխարինեց Locked `D-026` օրենքը և consumer-ների համար ավելացրեց նոր պարտադիր պահանջ․ semantic versioning-ով դա անհամատեղելի փոփոխություն է, այսինքն MAJOR։ (3) `0.x`-ը կնշանակեր «դեռ ոչինչ կայուն չէ», մինչդեռ Foundation v1-ը Locked է։ Թիվը կազմողի դատողությունն է․ այլ թիվ ընտրելը Owner-ինն է, և այն փոխվում է `VERSION`-ի մեկ տողով և changelog-ի մեկ վերնագրով։

**EN:** A copy together with a pin is the only option in which the gate works without the network (an AI session runs it locally) and every copy is, at the same time, verifiable against the standard. The accepted trade-off: the kit files are duplicated in every repository, and an update needs a person's merge in every repository. The second is the Owner's decision, not a defect.

The first version number is `2.0.0` for three reasons. (1) The tag `foundation-v1.0.0` already exists and points at a commit from before `D-028`; were the standard's version `1.0.0` as well, two different things would carry one number. (2) Since `foundation-v1.0.0`, `D-028` superseded the Locked `D-026` law in part and added a new mandatory requirement for consumers; under semantic versioning that is an incompatible change, hence MAJOR. (3) `0.x` would say “nothing is stable yet”, while Foundation v1 is Locked. The number is the drafter's judgement; choosing another is the Owner's, and it changes with one line of `VERSION` and one changelog heading.

## Assumptions / Ենթադրություններ

**HY:**

- GitHub-ը թույլ է տալիս private repository-ին կանչել public repository-ի reusable workflow, և `actions/checkout`-ը private repository-ի token-ով կարող է checkout անել public MenQ Standard-ը։ Այստեղ չի ստուգվել։ Validation՝ առաջին private repository-ի առաջին run-ը․ owner՝ MenQ Owner․ ձախողման հետևանք՝ reusable workflow-ը ստանդարտը վերցնում է `git clone`-ով, ինչպես update template-ը։
- Actions token-ը չի կարող push անել `.github/workflows/`-ի փոփոխություն, և նրա բացած pull request-ը չի գործարկում repository-ի workflow-ները։ Դիզայնը հենվում է երկուսի վրա․ եթե առաջինը սխալ է, update-ը կարող էր նաև workflow-ները նորացնել․ եթե երկրորդը սխալ է, pull request-ի վրա conformance run կերևա ինքնաբերաբար։ Այստեղ չեն ստուգվել։ Validation՝ առաջին update pull request-ը իրական repository-ում։
- Product repository-ները ունեն Python 3 և git իրենց CI-ում և developer մեքենաներում։ Kit-ը այստեղ գործարկվել է միայն Python 3.13-ով․ CI-ն հայտարարում է 3.12։

**EN:**

- GitHub lets a private repository call a reusable workflow of a public repository, and `actions/checkout` running with a private repository's token can check out the public MenQ Standard. Not checked here. Validation: the first run in the first private repository; owner: MenQ Owner; consequence of failure: the reusable workflow fetches the standard with `git clone`, as the update template does.
- An Actions token cannot push a change under `.github/workflows/`, and a pull request it opens does not start the repository's workflows. The design leans on both: were the first false, an update could refresh the workflows too; were the second false, a conformance run would appear on the pull request by itself. Not checked here. Validation: the first update pull request in a real repository.
- Product repositories have Python 3 and git in their CI and on developer machines. The kit was run here with Python 3.13 only; CI declares 3.12.

## Expected outcome and KPI / Ակնկալվող արդյունք և KPI

**HY:** Product repository-ն կարող է մեկ հրամանով ընդունել ստանդարտը, local և CI-ում ստուգել իր համապատասխանությունը, և ստանդարտի փոփոխությունը նրան հասնում է pull request-ով։ Baseline՝ 0 repository pin-ով, քանի որ pin-ի ձևաչափ չկար։ KPI՝ pin ունեցող և GREEN conformance run ունեցող product repository-ների թիվը, և pin-ի հետ մնալու տևողությունը։ Target և ժամկետ՝ չեն սահմանվել․ դրանք Owner-ինն են։ Ազնիվ սահմանափակում՝ այս KPI-ն այսօր ոչ մի ծրագիր չի չափում․ ստանդարտը consumer-ների ցանկ չունի և private repository-ները չի տեսնում, ուստի թիվը կարող է հաշվել միայն մարդը կամ org-ի մակարդակի գործիքը, որը այս որոշման մաս չէ։

**EN:** A product repository can adopt the standard with one command, check its conformance locally and in CI, and a change to the standard reaches it as a pull request. Baseline: 0 repositories with a pin, because no pin format existed. KPI: the number of product repositories that hold a pin and have a GREEN conformance run, and how long a pin stays behind. Target and deadline: not set; they are the Owner's. An honest limit: no program measures this KPI today. The standard has no list of consumers and cannot see private repositories, so the number can be counted only by a person or by an organisation-level tool that is not part of this decision.

## Risks and mitigations / Ռիսկեր և մեղմացում

**HY:**

- Reusable workflow-ը և update template-ը GitHub-ում չեն գործարկվել → նրանց քայլերը գործարկվել են որպես shell ժամանակավոր repository-ներում, և template-ների policy-ն պահում է gate-ը․ GitHub-ի վարքը մնում է չստուգված, մինչև առաջին իրական ընդունումը։
- Առանց `--standard`-ի checker-ը կարելի է խաբել կեղծված pin-ով → output-ը դա ասում է ամեն անգամ, և CI-ի վճիռը տալիս է ստանդարտի պատճենը՝ `--standard`-ով։
- Reusable workflow-ի առաջին քայլը գործարկում է ստանդարտի `main`-ի checker-ը, որպեսզի կարդա pin-ը → `main`-ում merge արված թերությունը կարող է միանգամից կոտրել բոլոր repository-ների CI-ն։ Մեղմացում՝ `pin-commit` և `check` հրամանների տողերը հայտարարված interface են և ունեն թեստեր․ ռիսկը չի վերանում։
- Render արված workflow-ները մնում են այն SHA-ի վրա, որով render են արվել → `status`-ը անվանում է այն workflow-ը, որի template-ը փոխվել է, և update pull request-ը դա ցույց է տալիս․ նորից render անում է մարդը։
- Kit-ին ավելացված նոր Markdown ֆայլը RED է դարձնում update pull request-ը, մինչև repository-ն այն չավելացնի իր session-read manifest-ին → դա ճիշտ վարք է (ֆայլը, որը ոչ ոքի չի ասվում կարդալ, RED է), և `ADOPTION.md`-ը դա նկարագրում է։
- Repository-ն կարող է պարզապես չընդունել ստանդարտը կամ ջնջել workflow-ը → ոչ մի ծրագիր դա չի տեսնում․ consumer-ների ցանկ չկա։ Բաց հարց Owner-ի համար։
- `sync_facts.py`-ը այժմ երկու տեղում է՝ OS repository-ում և kit-ում → kit-ի պատճենը բայթ առ բայթ նույնն է (sha256 `d4fed638…`)․ թե որն է canonical աղբյուրը՝ բաց հարց է Owner-ի համար։
- Hash-ը LF-ի բերված բայթերի վրա է, ուստի միայն տողավերջերը փոխող խմբագրումը չի հայտնաբերվում → ընդունված է, որպեսզի autocrlf-ով checkout-ը չփոփոխված ֆայլը խմբագրված չցույց տա։
- Թե տարբերակի որ մասն է աճում՝ գրված կանոն է, ոչ թե ստուգում → gate-ը ստուգում է միայն, որ kit-ի փոփոխությունը աճեցնում է տարբերակը։

**EN:**

- The reusable workflow and the update template have not run on GitHub → their steps were run as shell in temporary repositories, and a gate holds the templates to the policy; GitHub's behaviour stays unchecked until the first real adoption.
- Without `--standard` the checker can be deceived by a forged pin → the output says so every time, and the verdict in CI is given by the standard's copy, with `--standard`.
- The first step of the reusable workflow runs the checker of the standard's `main` in order to read the pin → a defect merged into `main` can break the CI of every repository at once. Mitigation: the command lines `pin-commit` and `check` are a declared interface and have tests; the risk is not removed.
- Rendered workflows stay at the SHA they were rendered with → `status` names a workflow whose template changed and the update pull request shows it; a person re-renders.
- A new Markdown file added to the kit turns an update pull request RED until the repository adds it to its session-read manifest → that is correct behaviour (a file nobody is told to read is RED), and `ADOPTION.md` describes it.
- A repository can simply not adopt the standard, or delete the workflow → no program sees that; there is no list of consumers. An open question for the Owner.
- `sync_facts.py` now lives in two places, the OS repository and the kit → the kit's copy is byte-for-byte the same (sha256 `d4fed638…`); which one is the canonical source is an open question for the Owner.
- The hash is over LF-normalised bytes, so an edit that changes only line endings is not detected → accepted, so that a checkout with autocrlf does not show an unmodified file as edited.
- Which part of the version increases is a written rule, not a check → the gate checks only that a change to the kit increases the version.

## Reversibility / Հետշրջելիություն

**HY:** Լիովին հետշրջելի է։ Այս repository-ում՝ pull request-ի revert-ը հեռացնում է `consumer/`-ը, `VERSION`-ը, reusable workflow-ը և երեք script-ը, և `scripts/check_session_read_budget.py`-ը նորից դառնում է իրականացումը։ Product repository-ում՝ մեկ commit, որը ջնջում է pin-ը, kit-ի directory-ն և երկու workflow-ը։ Դրսում ոչինչ չի ստեղծվում՝ ոչ package, ոչ token, ոչ tag, ոչ release։ Ոչ մի repository դեռ չի ընդունել այս շերտը, ուստի rollback-ը ոչ մեկի վրա չի ազդում։

**EN:** Fully reversible. In this repository: reverting the pull request removes `consumer/`, `VERSION`, the reusable workflow and the three scripts, and `scripts/check_session_read_budget.py` becomes the implementation again. In a product repository: one commit that deletes the pin, the kit directory and the two workflows. Nothing is created outside: no package, no token, no tag, no release. No repository has adopted this layer yet, so a rollback affects nobody.

## What this decision does not do / Ինչ այս որոշումը չի անում

**HY:**

- Չի սահմանում ժամկետ, մինչև երբ repository-ն պետք է ընդունի ստանդարտը․ `D-028`-ը մեխանիզմը և ժամկետը թողել էր հետագա որոշման, և սա տալիս է միայն մեխանիզմը։
- Չի ստեղծում consumer-ների ցանկ և չի ստուգում, թե որ repository-ներն են ընդունել ստանդարտը։
- Ոչ մի repository չի ընդունում․ ոչ մի product repository չի փոխվել։
- Չի ստեղծում tag կամ release․ դրանք Owner-ինն են։ `VERSION` ֆայլը tag չէ։
- Չի տարածում Design Platform-ի package-ները․ `D-025`-ի consumption-ը առանձին է։
- Չի ստուգում, որ session-ը որևէ բան կարդացել է, և չի սահմանափակում area-ները․ երկուսն էլ մնում են ինչպես `D-028`-ում։
- Չի կարգավորում `sync_facts`-ը այս repository-ում․ `config/doc-facts.json` այստեղ չկա։

**EN:**

- It sets no deadline by which a repository must adopt the standard: `D-028` left the mechanism and the deadline to a later decision, and this supplies the mechanism only.
- It creates no list of consumers and does not check which repositories adopted the standard.
- It adopts nothing anywhere: no product repository was changed.
- It creates no tag and no release; those are the Owner's. The `VERSION` file is not a tag.
- It does not distribute the packages of the Design Platform; consumption under `D-025` is separate.
- It does not check that a session read anything and does not bound areas; both stay as in `D-028`.
- It does not configure `sync_facts` in this repository: there is no `config/doc-facts.json` here.

## Dependencies / Կախվածություններ

`D-019` (Governance), `D-020` (Decision System), `D-022` (Canonical Write Integrity Law), `D-023` (AI Collaboration Standard), `D-028` (Bounded Session Read Law).

## Implementation owner and validation / Իրականացում և ստուգում

**HY:** Իրականացնող՝ AI collaborator-ը կազմում է draft-ը, MenQ Owner-ը merge է անում։ Validation՝ `scripts/test_check_conformance.py`, `scripts/test_generate_kit_manifest.py`, `scripts/test_check_standard_version.py`, `scripts/test_check_consumer_templates.py`, `consumer/test_sync_facts.py`, `scripts/test_check_session_read_budget.py`-ի 60 նախկին թեստը անփոփոխ և յոթ նորը, և `scripts/test_validate_foundation.py`-ը։ Ամեն ստուգման համար կա թեստ, որը ժամանակավոր git repository-ում կոտրում է հենց այդ բանը․ fixture-ները գրված են բայթերով, և hash կամ բայթ հաշվող ամեն ինչի համար կա CRLF fixture։ Նոր ստուգումներից յուրաքանչյուրը մեկ անգամ թուլացվել է՝ համոզվելու համար, որ թեստ է կարմրում․ արդյունքը, ներառյալ գոյատևած mutant-ները, հաղորդվում է reviewer-ին draft-ի հետ և այս record-ում գրանցված չէ։ Ամբողջ ճանապարհը՝ ընդունում, վեց RED դեպք, update և նոր pin, կատարվել է local՝ ժամանակավոր repository-ում։

**EN:** Implementation: the AI collaborator drafts and the MenQ Owner merges. Validation: `scripts/test_check_conformance.py`, `scripts/test_generate_kit_manifest.py`, `scripts/test_check_standard_version.py`, `scripts/test_check_consumer_templates.py`, `consumer/test_sync_facts.py`, the 60 earlier tests of `scripts/test_check_session_read_budget.py` unchanged plus seven new ones, and `scripts/test_validate_foundation.py`. For every check there is a test that breaks exactly that thing in a temporary git repository; the fixtures are written as bytes, and everything that hashes or counts bytes has a CRLF fixture. Each new check was weakened once to confirm that a test goes red; the result, surviving mutants included, is reported to the reviewer with the draft and is not recorded in this file. The whole path, adoption, six RED cases, an update and the new pin, was performed locally in a temporary repository.

## Review trigger / Վերանայման trigger

**HY:** Առաջին product repository-ն ընդունում է շերտը․ reusable workflow-ի կամ update workflow-ի առաջին run-ը GitHub-ում․ վերևի ենթադրություններից որևէ մեկը սխալ է դուրս գալիս․ Owner-ը սահմանում է ժամկետ կամ consumer-ների ցանկ․ kit-ը պահանջում է pin-ի նոր ձևաչափ։

**EN:** The first product repository adopts the layer; the first run of the reusable workflow or of the update workflow on GitHub; one of the assumptions above proves false; the Owner sets a deadline or a list of consumers; the kit needs a new pin format.

## Affected canonical files / Ազդված canonical ֆայլեր

- `foundation/ai-collaboration/D-029-CONSUMER-ADOPTION-LAYER.md`
- `foundation/ai-collaboration/D-028-BOUNDED-SESSION-READ-LAW.md` (a dated pointer only)
- `foundation/ai-collaboration/SESSION_READ_MANIFEST.json`, `foundation/ai-collaboration/MARKDOWN_INVENTORY.json`
- `foundation/PROJECT_CONTEXT.md`
- `VERSION`, `DECISION_INDEX.md`, `CHANGELOG.md`, `NEXT_CHAT_HANDOFF.md`
- `consumer/` (the kit, `KIT_MANIFEST.json`)
- `scripts/check_session_read_budget.py`, `scripts/generate_kit_manifest.py`, `scripts/check_standard_version.py`, `scripts/check_consumer_templates.py`, `scripts/validate_foundation.py`, and the tests beside them
- `.github/workflows/consumer-conformance.yml`, `.github/workflows/markdown-inventory-bootstrap.yml`

## Evidence / Ապացույց

**HY:**

- Չափումներ `f664ec3` head-ում, 2026-10-09-ին․ `git ls-tree -r --name-only f664ec3`-ը չունի `VERSION` և չունի pin ֆայլ․ `.github/workflows/`-ում ինը ֆայլ կա, և `git grep workflow_call f664ec3 -- .github/workflows`-ը ոչինչ չի գտնում․ `git tag`-ը տալիս է երկու tag, երկուսն էլ `3793b3c`-ի վրա։
- `scripts/check_session_read_budget.py`-ի 28–29 տողերը `f664ec3`-ում՝ `DEFAULT_ROOT = Path(__file__).resolve().parents[1]` և `MANIFEST_REL = "foundation/ai-collaboration/SESSION_READ_MANIFEST.json"`։
- `sync_facts.py`-ի և `test_sync_facts.py`-ի sha256-ները kit-ում հավասար են OS repository-ի `tools/`-ի ֆայլերին (`d4fed638…`, `9baea6c2…`)՝ չափված այս մեքենայում։
- Local փորձարկումը և թեստերի ու mutant-ների արդյունքները հաղորդվում են reviewer-ին draft-ի հետ։
- Owner-ի որոշումները և նպատակը՝ project conversation-ից։ Conversation-ը canonical source չէ, և այս տեքստի հաստատումը pull request-ի merge-ն է։

**EN:**

- Measurements at head `f664ec3` on 2026-10-09: `git ls-tree -r --name-only f664ec3` has no `VERSION` and no pin file; `.github/workflows/` holds nine files and `git grep workflow_call f664ec3 -- .github/workflows` finds nothing; `git tag` gives two tags, both at `3793b3c`.
- Lines 28–29 of `scripts/check_session_read_budget.py` at `f664ec3`: `DEFAULT_ROOT = Path(__file__).resolve().parents[1]` and `MANIFEST_REL = "foundation/ai-collaboration/SESSION_READ_MANIFEST.json"`.
- The sha256 of `sync_facts.py` and of `test_sync_facts.py` in the kit equal those of the files in `tools/` of the OS repository (`d4fed638…`, `9baea6c2…`), measured on this machine.
- The local exercise and the results of the tests and of the mutants are reported to the reviewer with the draft.
- The Owner's decisions and goal, from the project conversation. Conversation is not the canonical source, and the approval of this text is the merge of the pull request.

<!-- END: D-029-CONSUMER-ADOPTION-LAYER -->
