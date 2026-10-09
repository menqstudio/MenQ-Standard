# D-028 — Bounded Session Read Law / Սահմանափակ session-ի ընթերցման օրենք

**Decision ID:** `D-028`  
**Status / Կարգավիճակ:** Approved — the Owner merged pull request #29 on 2026-10-09 (merge commit `ed91149`); not `Locked` / Approved — Owner-ը merge է արել pull request #29-ը 2026-10-09-ին (merge commit `ed91149`). `Locked` չէ  
**Date / Ամսաթիվ:** 2026-10-09  
**Decision class / Որոշման դաս:** `C4 — Foundation or Ecosystem`  
**Risk level / Ռիսկի մակարդակ:** `R2 — Moderate`  
**Owner / Պատասխանատու:** MenQ Owner  
**Proposer / Առաջարկող:** AI collaborator (Claude), writing down two decisions the Owner made in the project conversation on 2026-10-09  
**Reviewer / Վերանայող:** MenQ Owner, on the pull request. Reviewer and Approver are the same person; the overlap is disclosed under Governance §3.7  
**Approver / Հաստատող:** Gevorg Ohanyan, MenQ Owner — approved by merging pull request #29 from the `menqstudio` account at 2026-10-09T02:45:29Z. The evidence is that merge on GitHub, not a conversation. The body below is unchanged from the text that was merged and still reads as a proposal  
**Scope / Scope:** Every new MenQ Standard AI session; every MenQ product repository that follows the standard (see Consumer requirement)  
**Supersedes / Փոխարինում է:** `D-026` in part (see Supersession)  
**Superseded by / Փոխարինված է:** —

## Problem / Խնդիր

**HY:** D-026-ը (Locked) պահանջում է, որ յուրաքանչյուր AI session մինչև որևէ աշխատանք ամբողջությամբ կարդա repository-ի բոլոր tracked `.md` ֆայլերը, և արգելում է token կամ context limit-ը որպես չկարդալու պատճառ։ `c61608a` head-ում դա 133 Markdown ֆայլ է՝ 684,725 բայթ, առանց վերին սահմանի․ միայն brand-expression-ի 35 component README-ները 38,814 բայթ են, և յուրաքանչյուր նոր component ավելացնում է ևս մեկը։ Owner-ի գնահատմամբ՝ ոչ մի session չի կարող դա կատարել։ Ոչ մի ծրագիր չի ստուգում, որ session-ը որևէ բան կարդացել է․ միակ մեքենայական ստուգումը այն է, որ `MARKDOWN_INVENTORY.json`-ը համապատասխանում է tracked ֆայլերին։ Չնայած դրան՝ հինգ փաստաթուղթ (`README.md`, `PROJECT_CONTEXT.md`, `AI_WORKING_CONTEXT.md`, `NEXT_CHAT_HANDOFF.md`, `platforms/design/PROJECT_CONTEXT.md`) D-026-ը անվանում էր «machine-enforced»։ Կանոնը, որը հնարավոր չէ կատարել և հնարավոր չէ ստուգել, session-ին սովորեցնում է հայտարարել GREEN առանց հիմքի։

**EN:** D-026 (Locked) requires every AI session to read every tracked `.md` file of the repository in full before any work, and forbids a token or context limit as a reason not to. At head `c61608a` that is 133 Markdown files and 684,725 bytes, with no upper bound: the 35 component READMEs of brand-expression alone are 38,814 bytes, and every new component adds one more. In the Owner's assessment, no session can satisfy it. No program checks that a session read anything: the only machine check is that `MARKDOWN_INVENTORY.json` matches the tracked files. Despite that, five documents (`README.md`, `PROJECT_CONTEXT.md`, `AI_WORKING_CONTEXT.md`, `NEXT_CHAT_HANDOFF.md`, `platforms/design/PROJECT_CONTEXT.md`) called D-026 “machine-enforced”. A rule that cannot be satisfied and cannot be checked teaches a session to declare GREEN without grounds.

## Context / Կոնտեքստ

**HY:** Owner-ը 2026-10-09-ին project conversation-ում որոշել է երկու կետ․ (1) պարտադիր ընթերցումը դառնում է սահմանափակ CORE՝ ֆայլերի հերթականությամբ manifest, որը gate-ը պահում է ընդհանուր 120,000 բայթի սահմանում, իսկ մնացածը կարդացվում է ըստ AREA-ի, (2) նույն կանոնը՝ read manifest և gate-ով պահվող byte budget, պահանջվում է standard-ին հետևող յուրաքանչյուր MenQ product repository-ից։ Conversation-ը workshop է, ոչ canonical source։ D-026-ը Locked է, ուստի Decision System §18-ի համաձայն փոփոխությունը մտնում է նոր decision record-ով։ Այս record-ի տեքստը, core-ի կազմը, per-file սահմանները և area-ների ցանկը կազմել է AI-ն․ դրանք Owner-ը չի հաստատել, մինչև pull request-ը merge չանի։

**EN:** On 2026-10-09, in the project conversation, the Owner decided two points: (1) the mandatory read becomes a bounded CORE, an ordered manifest of files that a gate holds to a total of 120,000 bytes, and everything else is read by AREA; (2) the same rule, a read manifest and a byte budget held by a gate, is required of every MenQ product repository that follows the standard. Conversation is the workshop, not the canonical source. D-026 is Locked, so under Decision System §18 the change lands as a new decision record. The text of this record, the composition of the core, the per-file ceilings, and the list of areas were drafted by AI; the Owner has not approved them until the Owner merges the pull request.

## Decision / Որոշում

**HY:**

1. Պարտադիր session read-ը CORE-ն է՝ [`SESSION_READ_MANIFEST.json`](SESSION_READ_MANIFEST.json)-ի `core` ցանկը, նրա հերթականությամբ։ Յուրաքանչյուր նոր session այն կարդում է ամբողջությամբ մինչև որևէ substantive աշխատանք։
2. Core-ի ընդհանուր չափը չի գերազանցում 120,000 բայթը (`total_bytes_max`)։ Յուրաքանչյուր core ֆայլ ունի իր `bytes_max` սահմանը և `why` հիմնավորումը։ Per-file սահմանների գումարը նույնպես չի գերազանցում 120,000-ը, որպեսզի երկու սահմանափակումները չհակասեն իրար։
3. Մնացած ամեն ինչ կարդացվում է ըստ AREA-ի․ manifest-ի `areas`-ը յուրաքանչյուր directory-ի համար նշում է լրացուցիչ ֆայլերը, որոնք session-ը ամբողջությամբ կարդում է այդ directory-ում աշխատելուց առաջ։ Path-ի area-ն manifest-ում նշված ամենամոտ directory-ն է՝ նույն directory-ն կամ նրանից վեր․ եթե ավելի մոտը չկա, գործում է root area-ն՝ `.`։
4. Յուրաքանչյուր tracked Markdown ֆայլ պետք է հասանելի լինի core-ից կամ առնվազն մեկ area-ից։ Ֆայլը, որը ոչ մի session-ի երբևէ չի ասվում կարդալ, RED է։
5. Core-ից և session-ի area-ներից դուրս գտնվող ֆայլը մեկնարկին կարդալ պարտադիր չէ, բայց session-ը, որը հենվում է դրա վրա, մեջբերում, գնահատում կամ փոխում է այն, նախ կարդում է այն ամբողջությամբ։
6. `scripts/check_session_read_budget.py` gate-ը CI-ում RED է տալիս վերը նշված ցանկացած խախտման դեպքում և տպում է core-ի receipt-ը (`--receipt`)։ Բայթերը հաշվվում են CRLF-ը LF դարձնելուց հետո։
7. Բոլոր MenQ repository-ների համար գործում է մեկ ընդհանուր առավելագույն սահման՝ 350,000 բայթ, և այն գրված է gate-ի կոդում։ Յուրաքանչյուր repository իր manifest-ում հայտարարում է իր `total_bytes_max`-ը, որը չի կարող գերազանցել 350,000-ը․ MenQ Standard-ը հայտարարում է 120,000։ Ընդհանուր սահմանը բարձրացնելը պահանջում է նոր որոշում, իսկ repository-ի հայտարարած թիվը փոխելը՝ Owner-ի հաստատում pull request-ի merge-ով։
8. Core-ի կազմը կամ որևէ `bytes_max` փոխելը Foundation-ի փոփոխություն է և պահանջում է Owner-ի հաստատում (`G4`)՝ pull request-ի merge-ով։ Area-ների ցանկին նոր ֆայլ ավելացնելը այն directory-ի սովորական փոփոխության մաս է, որին ֆայլը պատկանում է։
9. [`CANONICAL_SESSION_READ_LAW.md`](CANONICAL_SESSION_READ_LAW.md)-ը դառնում է v2 և կրում է ամբողջական կանոնը։

**EN:**

1. The mandatory session read is the CORE: the `core` list of [`SESSION_READ_MANIFEST.json`](SESSION_READ_MANIFEST.json), in its order. Every new session reads it in full before any substantive work.
2. The total size of the core does not exceed 120,000 bytes (`total_bytes_max`). Every core file has its own `bytes_max` ceiling and a `why` justification. The sum of the per-file ceilings also does not exceed 120,000, so that the two constraints cannot disagree.
3. Everything else is read by AREA: the manifest's `areas` lists, for each directory, the additional files a session reads in full before working in that directory. The area of a path is the nearest directory listed in the manifest, the same directory or one above it; when none is nearer, the root area `.` applies.
4. Every tracked Markdown file must be reachable from the core or from at least one area. A file that no session is ever told to read is RED.
5. A file outside the core and outside the session's areas need not be read at startup, but a session that relies on it, cites it, judges it, or changes it first reads it in full.
6. The `scripts/check_session_read_budget.py` gate goes RED in CI on any of the violations above and prints the receipt of the core (`--receipt`). Bytes are counted after CRLF is folded to LF.
7. One universal maximum applies to every MenQ repository: 350,000 bytes, written in the gate's code. Each repository declares its own `total_bytes_max` in its manifest, which may not exceed 350,000; MenQ Standard declares 120,000. Raising the universal maximum requires a new decision; changing the number a repository declares requires Owner approval through the merge of a pull request.
8. Changing the composition of the core or any `bytes_max` is a Foundation change and requires Owner approval (`G4`) through the merge of a pull request. Adding a new file to the list of areas is part of the ordinary change of the directory the file belongs to.
9. [`CANONICAL_SESSION_READ_LAW.md`](CANONICAL_SESSION_READ_LAW.md) becomes v2 and carries the complete rule.

## What the mechanism proves and does not prove / Ինչ է ապացուցում մեխանիզմը և ինչ չի ապացուցում

**HY:** Gate-ը ապացուցում է, որ manifest-ը վավեր է, core-ի ֆայլերը գոյություն ունեն, core-ը տեղավորվում է սահմանում, և յուրաքանչյուր tracked Markdown ֆայլ հասանելի է core-ից կամ area-ից։ Receipt-ը մեկ SHA-256 digest է core-ի ֆայլերի բովանդակության վրա (path և LF-ի բերված բայթեր)՝ manifest-ի հերթականությամբ։ Receipt-ը, որը գրանցել է core-ը session-ին փոխանցած գործիքը, ապացուցում է, որ core-ի ֆայլերը փոխանցվել են session-ին տվյալ content hash-ով։ Receipt-ը չի ապացուցում և չի կարող ապացուցել, որ session-ը հասկացել է կարդացածը։ Digest-ը, որը session-ը ինքն է հաշվել, ապացուցում է միայն, որ session-ը կարողացել է գործարկել հրամանը։ Area-ի ընթերցումը ոչ մի ծրագիր չի ստուգում։ Այս repository-ում չկա գործիք, որը core-ը փոխանցում է session-ին և գրանցում receipt-ը․ այդ քայլը մնում է session-ը գործարկող միջավայրին։ Ուստի ընթերցման մասին ճիշտ ձևակերպումն է՝ «gate-ը պահում է core-ի չափը և manifest-ի ամբողջականությունը», ոչ թե «ընթերցումը ստուգվում է մեքենայով»։

**EN:** The gate proves that the manifest is valid, that the core files exist, that the core fits its ceiling, and that every tracked Markdown file is reachable from the core or from an area. A receipt is one SHA-256 digest over the content of the core files (path and LF-normalised bytes) in the manifest's order. A receipt recorded by the tool that delivered the core to the session proves that the core files were delivered to the session at the given content hash. A receipt does not and cannot prove that the session understood what it read. A digest the session computed for itself proves only that the session was able to run the command. No program checks the area read. This repository contains no tool that delivers the core to a session and records the receipt; that step is left to the environment that runs the session. The correct statement about the read is therefore “the gate holds the size of the core and the integrity of the manifest”, not “the read is checked by a machine”.

## Consumer requirement / Պահանջ consumer repository-ների համար

**HY:** Standard-ին հետևող յուրաքանչյուր MenQ product repository պարտավոր է ունենալ՝ (ա) session-read manifest՝ հերթականությամբ core ցանկով, (բ) այդ core-ի համար հայտարարված byte budget, (գ) CI-ում գործող gate, որը RED է տալիս, երբ core-ը գերազանցում է budget-ը կամ manifest-ը անվավեր է։ Սա Owner-ի երկրորդ որոշումն է։ Ազնիվ վիճակը՝ consumer repository-ների համար adoption մեխանիզմ դեռ գոյություն չունի։ Չկա consumer-ների ցանկ, որի նկատմամբ այս պահանջը ստուգվի, gate-ը չի տարածվում որպես package, և այս որոշումը կազմելիս ոչ մի այլ repository չի ստուգվել։ Owner-ը 2026-10-09-ին որոշել է, որ բոլորի համար գործում է մեկ թիվ՝ 350,000 բայթ ընդհանուր առավելագույն սահմանը։ Այն վերցված է ecosystem-ի ամենամեծ read set-ից՝ OS repository-ից, որի canonical read-ը այդ օրը 207,623 բայթ էր 350,000 սահմանի տակ, որը OS-ը պահում է 2026-ի օգոստոսից։ Repository-ն հայտարարում է իր budget-ը այդ թվից ոչ ավելի։ OS-ի թվերը վերցված են OS repository-ի սեփական gate-ի output-ից և այս repository-ից չեն ստուգվում։ Adoption մեխանիզմը և ժամկետը առանձին, հետագա որոշման առարկա են։ Մինչ այդ այս բաժինը պահանջ է առանց ստուգման և չպետք է ներկայացվի որպես կատարված։

**EN:** Every MenQ product repository that follows the standard must have: (a) a session-read manifest with an ordered core list, (b) a declared byte budget for that core, (c) a gate running in CI that goes RED when the core exceeds the budget or the manifest is invalid. This is the Owner's second decision. The honest state: no adoption mechanism for consumer repositories exists yet. There is no list of consumers against which this requirement is checked, the gate is not distributed as a package, and no other repository was examined while drafting this decision. On 2026-10-09 the Owner decided that one number applies to all: the universal maximum of 350,000 bytes. It is taken from the largest read set in the ecosystem, the OS repository, whose canonical read was 207,623 bytes that day under a 350,000 ceiling OS has held since August 2026. A repository declares its own budget at or below that number. The OS figures come from the OS repository's own gate output and are not checked from this repository. The adoption mechanism and the deadline are the subject of a separate, later decision. Until then this section is a requirement without a check and must not be represented as fulfilled.

## Alternatives considered / Դիտարկված այլընտրանքներ

**HY:**

- (ա) D-026-ը թողնել անփոփոխ — մերժվեց․ 684,725 բայթը աճում է առանց սահմանի, կանոնը չի ստուգվում, և «կարդացել եմ ամեն ինչ» հայտարարությունը դառնում է սովորական կեղծ GREEN։
- (բ) Ոչինչ չբարձրացնել և չսահմանափակել, հենվել summary-ների և handoff-ի վրա — մերժվեց․ summary-ն հենց այն է, ինչ D-026-ը արգելել էր որպես evidence, այն հնանում է առանց որևէ ստուգման, և session-ը չի կարող տարբերել ամբողջական summary-ն կիսատից։
- (գ) Per-file budget առանց core/area բաժանման — մերժվեց․ յուրաքանչյուր ֆայլի սահմանը չի սահմանափակում ֆայլերի քանակը, ուստի ընդհանուր ընթերցումը դարձյալ աճում է առանց սահմանի (35 component README-ները յուրաքանչյուրը փոքր են, միասին՝ 38,814 բայթ)։
- (դ) Core՝ առանց area-ների և առանց orphan check-ի — մերժվեց․ core-ից դուրս ֆայլերը կդառնային փաստաթղթեր, որոնք ոչ ոքի չի ասվում կարդալ։
- (ե) Manifest-ը ինքը ներառել core-ի մեջ — հետաձգվեց․ manifest-ը 23,000 բայթից մեծ է և հիմնականում area-ների ցանկ է․ այն core-ում դնելը կսպառեր գրեթե ամբողջ headroom-ը։ Session-ը manifest-ը կարդում է core-ը և իր area-ն գտնելու համար, բայց նրա բայթերը budget-ում չեն հաշվվում։

**EN:**

- (a) Keep D-026 as it is — rejected: 684,725 bytes grows without a bound, the rule is not checked, and the statement “I read everything” becomes a routine false GREEN.
- (b) Raise nothing and bound nothing, and rely on summaries and the handoff — rejected: a summary is exactly what D-026 had refused as evidence, it goes stale with no check at all, and a session cannot tell a complete summary from a partial one.
- (c) A per-file budget with no core/area split — rejected: a ceiling on each file does not bound the number of files, so the total read again grows without a bound (the 35 component READMEs are each small and together 38,814 bytes).
- (d) A core with no areas and no orphan check — rejected: files outside the core would become documents nobody is told to read.
- (e) Include the manifest itself in the core — deferred: the manifest is larger than 23,000 bytes and is mostly the list of areas; placing it in the core would consume nearly all of the headroom. A session reads the manifest to find the core and its area, but its bytes are not counted in the budget.

## Why this option / Ինչու այս տարբերակը

**HY:** Սահմանափակ core-ը միակ տարբերակն է, որտեղ «token limit-ը պատճառ չէ» կանոնը կարող է ճիշտ լինել․ կանոնը պահանջում է միայն այն, ինչ հնարավոր է տալ։ Ընդունված trade-off-ը՝ session-ը մեկնարկին այլևս չի տեսնում ամբողջ repository-ն, և core-ից դուրս գտնվող փաստը կարող է բաց մնալ, եթե session-ը սխալ է որոշում իր area-ն։ Դա մեղմվում է area-ի կանոնով, orphan check-ով և «հենվելուց առաջ կարդա» կանոնով, բայց չի վերանում։

**EN:** A bounded core is the only option in which the rule “a token limit is not a reason” can be true: the rule demands only what can be given. The accepted trade-off: a session no longer sees the whole repository at startup, and a fact outside the core can be missed when the session misjudges its area. This is mitigated by the area rule, the orphan check, and the “read before you rely” rule, but it is not removed.

## Assumptions / Ենթադրություններ

**HY:**

- 120,000 բայթ core-ը task-ի և area-ի հետ միասին տեղավորվում է այն մոդելների context-ում, որոնցով MenQ session-ները աշխատում են։ Սա այստեղ չի չափվել։ Validation՝ առաջին session-ները նոր օրենքով․ owner՝ MenQ Owner․ trigger՝ առաջին session-ը, որը չի կարողանում բեռնել core-ը․ ձախողման հետևանք՝ սահմանը իջեցվում է նոր որոշմամբ։
- Ընտրված core-ը բավարար է օրինական աշխատելու համար։ Սա կազմողի դատողությունն է, ոչ թե չափում։ Validation՝ Owner-ի review-ն pull request-ում և առաջին դեպքը, երբ session-ը սխալվում է core-ում չգտնվող կանոնի պատճառով։

**EN:**

- A 120,000-byte core fits, together with the task and an area, in the context of the models MenQ sessions run on. This was not measured here. Validation: the first sessions under the new law; owner: MenQ Owner; trigger: the first session that cannot load the core; consequence of failure: the ceiling is lowered by a new decision.
- The chosen core is sufficient to work lawfully. This is the drafter's judgement, not a measurement. Validation: the Owner's review on the pull request, and the first case in which a session errs because of a rule that is not in the core.

## Expected outcome and KPI / Ակնկալվող արդյունք և KPI

**HY:** Յուրաքանչյուր session կարող է իրականում կատարել մեկնարկային ընթերցումը, և փաստաթղթերը ընթերցման մասին պնդում են միայն այն, ինչ ստուգվում է։ Baseline՝ 684,725 բայթ պարտադիր ընթերցում, առանց սահմանի (`c61608a`)։ KPI և target՝ core-ը ≤ 120,000 բայթ, 0 orphan tracked Markdown ֆայլ, gate-ը GREEN յուրաքանչյուր pull request-ում, 0 փաստաթուղթ, որը ընթերցումը անվանում է մեքենայով ստուգվող։ Owner՝ MenQ Owner։ Չափման հաճախականություն՝ CI-ի յուրաքանչյուր run։ Այս draft-ում չափված core-ը 10 ֆայլ է, 107,705 բայթ, per-file սահմանների գումարը՝ 113,120։

**EN:** Every session can actually perform the startup read, and the documents claim about the read only what is checked. Baseline: 684,725 bytes of mandatory read with no bound (`c61608a`). KPI and target: the core is ≤ 120,000 bytes, 0 orphan tracked Markdown files, the gate is GREEN on every pull request, 0 documents that call the read machine-checked. Owner: MenQ Owner. Measurement cadence: every CI run. The core measured in this draft is 10 files and 107,705 bytes, and the sum of the per-file ceilings is 113,120.

## Risks and mitigations / Ռիսկեր և մեղմացում

**HY:**

- Session-ը բաց է թողնում core-ից դուրս գտնվող կարևոր փաստ → area-ի կանոն, orphan check, «հենվելուց առաջ կարդա» կանոն, և Canonical Write Integrity Law-ը, որը պահանջում է փոփոխվող ֆայլի ամբողջական ընթերցում։
- Area-ները սահման չունեն → ամենամեծ area-ն այս draft-ում `platforms/design`-ն է՝ 23 ֆայլ, 164,171 բայթ, ավելի մեծ, քան ամբողջ core-ը։ `platforms/design/governance/change-requests`-ը աճում է յուրաքանչյուր նոր change request-ի հետ։ Gate-ը տպում է ամենամեծ area-ի չափը, բայց չի սահմանափակում այն։ Area-ների սահմանը բաց հարց է Owner-ի համար։
- Երկու essential փաստաթուղթ չեն տեղավորվում core-ում՝ `foundation/ai-collaboration/README.md` (33,821 բայթ) և `DECISIONS.md` (19,061 բայթ) → դրանք area-ներում են (`foundation/ai-collaboration`, `foundation`, `foundation/decision-system`, `.`)․ AI-ի authority-ի սահմանները core-ում են `foundation/governance/README.md`-ի և `PROJECT_CONTEXT.md`-ի միջոցով, իսկ `D-001–D-021`-ը հասանելի են `DECISION_INDEX.md`-ից։
- Core-ի headroom-ը փոքր է (12,295 բայթ, մոտ 10%) → per-file սահմանները gate-ը RED է դարձնում մինչև ընդհանուր սահմանին հասնելը․ աճի դեպքում պետք է կրճատել կամ տեղափոխել, ոչ թե բարձրացնել սահմանը։
- Receipt-ը կարող է ներկայացվել որպես ընթերցման ապացույց → օրենքի §4-ը և այս record-ը հստակ ասում են, թե ինչ է այն ապացուցում և ինչ՝ ոչ։
- Consumer-ների պահանջը կարող է ներկայացվել որպես կատարված → Consumer requirement բաժինը ասում է, որ մեխանիզմ չկա։

**EN:**

- A session misses an important fact outside the core → the area rule, the orphan check, the “read before you rely” rule, and the Canonical Write Integrity Law, which requires a complete read of the file being changed.
- Areas have no ceiling → the largest area in this draft is `platforms/design`: 23 files, 164,171 bytes, larger than the whole core. `platforms/design/governance/change-requests` grows with every new change request. The gate prints the size of the largest area but does not bound it. A ceiling for areas is an open question for the Owner.
- Two essential documents do not fit in the core, `foundation/ai-collaboration/README.md` (33,821 bytes) and `DECISIONS.md` (19,061 bytes) → they are in areas (`foundation/ai-collaboration`, `foundation`, `foundation/decision-system`, `.`); the limits of AI authority are in the core through `foundation/governance/README.md` and `PROJECT_CONTEXT.md`, and `D-001–D-021` are reachable from `DECISION_INDEX.md`.
- The headroom of the core is small (12,295 bytes, about 10%) → the per-file ceilings turn the gate RED before the total is reached; on growth the answer is to shorten or move, not to raise the ceiling.
- A receipt may be presented as proof of reading → §4 of the law and this record state plainly what it proves and what it does not.
- The consumer requirement may be presented as fulfilled → the Consumer requirement section says that no mechanism exists.

## Reversibility / Հետշրջելիություն

**HY:** Լիովին հետշրջելի է․ փոփոխությունները ֆայլային են և մեկ pull request-ում։ Rollback՝ pull request-ի revert, որը վերադարձնում է D-026-ի v1 օրենքը։ `MARKDOWN_INVENTORY.json`-ը և նրա drift check-ը չեն հեռացվում, ուստի D-026-ի ենթակառուցվածքը rollback-ի ժամանակ մնում է աշխատող։

**EN:** Fully reversible: the changes are file-level and contained in one pull request. Rollback: revert the pull request, which restores the v1 law of D-026. `MARKDOWN_INVENTORY.json` and its drift check are not removed, so the D-026 infrastructure stays working through a rollback.

## Dependencies / Կախվածություններ

`D-020` (Decision System), `D-022` (Canonical Write Integrity Law), `D-023` (AI Collaboration Standard), `D-026` (Canonical Session Read Law), Governance v1 (`D-019`).

## Implementation owner and validation / Իրականացում և ստուգում

**HY:** Իրականացնող՝ AI collaborator-ը կազմում է draft-ը, MenQ Owner-ը merge է անում։ Validation՝ `scripts/check_session_read_budget.py` և նրա թեստերը՝ `scripts/test_check_session_read_budget.py` (յուրաքանչյուր ստուգման համար՝ թեստ, որը կոտրում է հենց այդ բանը ժամանակավոր git repository-ում, գումարած positive control), `Markdown Inventory Integrity` workflow-ը, Markdown inventory-ն, Foundation և Platforms validator-ները։ Gate-ի յուրաքանչյուր ստուգում մեկ անգամ անջատվել է՝ համոզվելու համար, որ առնվազն մեկ թեստ կարմրում է․ արդյունքը հաղորդվում է reviewer-ին draft-ի հետ և այս record-ում գրանցված չէ։

**EN:** Implementation: the AI collaborator drafts and the MenQ Owner merges. Validation: `scripts/check_session_read_budget.py` and its tests in `scripts/test_check_session_read_budget.py` (for every check, a test that breaks exactly that thing in a temporary git repository, plus a positive control), the `Markdown Inventory Integrity` workflow, the Markdown inventory, and the Foundation and Platforms validators. Every check in the gate was disabled once to confirm that at least one test goes red; the result is reported to the reviewer with the draft and is not recorded in this file.

## Review trigger / Վերանայման trigger

**HY:** Core-ը հասնում է 114,000 բայթի (սահմանի 95%-ը)․ session-ը չի կարողանում բեռնել core-ը․ session-ը սխալվում է core-ում չգտնվող կանոնի պատճառով․ առաջին consumer repository-ն ընդունում է պահանջը․ որոշվում է area-ների սահմանը կամ consumer-ների adoption մեխանիզմը։

**EN:** The core reaches 114,000 bytes (95% of the ceiling); a session cannot load the core; a session errs because of a rule that is not in the core; the first consumer repository adopts the requirement; a ceiling for areas or the adoption mechanism for consumers is decided.

## Supersession / Փոխարինում

**HY:** D-028-ը մասամբ փոխարինում է D-026-ը։ Փոխարինվում են՝ D-026-ի `Decision` բաժնի «բոլոր tracked `.md` ֆայլերը» պահանջը, պարտադիր կանոններ 2-ը և 7-ը (7-րդը այժմ արգելում է core-ի ընթերցման շրջանցումը) և `Validation` բաժնի 4-րդ կետը։ Ուժի մեջ են մնում՝ պարտադիր կանոններ 1, 3, 4, 5, 6 և 8-ը՝ core-ի և area-ի նկատմամբ, session isolation-ը, branch awareness-ը, delegation-ի կանոնը, Canonical Write Integrity Law-ի հետ կապը, `MARKDOWN_INVENTORY.json`-ը, `scripts/generate_markdown_inventory.py`-ը և `scripts/validate_foundation.py`-ի drift check-ը։ `D-026_VALIDATION_RECORD.md`-ը մնում է անփոփոխ որպես inventory ենթակառուցվածքի պատմական evidence։ Decision System §7-ը «մասամբ փոխարինված» status չունի, ուստի D-026-ի status-ը մնում է `Locked`՝ մասնակի փոխարինման նշումով և `Superseded by` դաշտով։

**EN:** D-028 supersedes D-026 in part. Superseded: the requirement of D-026's `Decision` section to read “every tracked `.md` file”, mandatory rules 2 and 7 (rule 7 now forbids bypassing the core read), and item 4 of its `Validation` section. Still in force: mandatory rules 1, 3, 4, 5, 6 and 8, applied to the core and the area, session isolation, branch awareness, the delegation rule, the relationship to the Canonical Write Integrity Law, `MARKDOWN_INVENTORY.json`, `scripts/generate_markdown_inventory.py`, and the drift check in `scripts/validate_foundation.py`. `D-026_VALIDATION_RECORD.md` stays unchanged as historical evidence of the inventory infrastructure. Decision System §7 has no “superseded in part” status, so the status of D-026 stays `Locked`, with a note of partial supersession and a `Superseded by` field.

## Affected canonical files / Ազդված canonical ֆայլեր

- `foundation/ai-collaboration/D-028-BOUNDED-SESSION-READ-LAW.md`
- `foundation/ai-collaboration/SESSION_READ_MANIFEST.json`
- `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`
- `foundation/ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md`
- `foundation/ai-collaboration/PROJECT_CONTEXT.md`
- `foundation/ai-collaboration/MARKDOWN_INVENTORY.json`
- `foundation/README.md`, `foundation/PROJECT_CONTEXT.md`
- `README.md`, `PROJECT_CONTEXT.md`, `AI_WORKING_CONTEXT.md`, `NEXT_CHAT_HANDOFF.md`
- `DECISION_INDEX.md`, `CHANGELOG.md`
- `platforms/design/PROJECT_CONTEXT.md`, `platforms/design/NEXT_CHAT_HANDOFF.md`
- `scripts/check_session_read_budget.py`, `scripts/test_check_session_read_budget.py`
- `.github/workflows/markdown-inventory-bootstrap.yml`

## Evidence / Ապացույց

**HY:**

- Չափումներ `c61608a` head-ում, 2026-10-09-ին․ `git ls-files -z '*.md' | tr '\0' '\n' | grep -c .` → 133․ `git ls-files -z '*.md' | xargs -0 cat | wc -c` → 684,725․ նույնը միայն `brand-expression/components/` path-երի համար → 35 ֆայլ, 38,814 բայթ։
- «machine-enforced» բառը `c61608a`-ում D-026-ի մասին՝ `README.md`, `PROJECT_CONTEXT.md`, `AI_WORKING_CONTEXT.md`, `NEXT_CHAT_HANDOFF.md`, `platforms/design/PROJECT_CONTEXT.md` (`grep -rn "machine-enforced"`)։
- `scripts/validate_foundation.py`-ի ընթերցում՝ D-026-ի համար այն ստուգում է inventory-ի path, size և SHA drift-ը և մի քանի փաստաթղթում reference տողերի առկայությունը․ session-ի ընթերցումը ոչինչ չի գրանցում և չի ստուգում։
- Core-ի չափումը այս draft-ում՝ `python3 scripts/check_session_read_budget.py` → 10 ֆայլ, 107,705 բայթ 120,000-ից։
- Owner-ի երկու որոշումները project conversation-ում՝ 2026-10-09-ին։ Conversation-ը canonical source չէ, և այս տեքստի հաստատումը pull request-ի merge-ն է։

**EN:**

- Measurements at head `c61608a` on 2026-10-09: `git ls-files -z '*.md' | tr '\0' '\n' | grep -c .` → 133; `git ls-files -z '*.md' | xargs -0 cat | wc -c` → 684,725; the same restricted to `brand-expression/components/` paths → 35 files, 38,814 bytes.
- The word “machine-enforced” about D-026 at `c61608a`: `README.md`, `PROJECT_CONTEXT.md`, `AI_WORKING_CONTEXT.md`, `NEXT_CHAT_HANDOFF.md`, `platforms/design/PROJECT_CONTEXT.md` (`grep -rn "machine-enforced"`).
- A reading of `scripts/validate_foundation.py`: for D-026 it checks the inventory's path, size and SHA drift and the presence of reference strings in several documents; nothing records or checks a session's read.
- The measurement of the core in this draft: `python3 scripts/check_session_read_budget.py` → 10 files, 107,705 bytes of 120,000.
- The Owner's two decisions in the project conversation on 2026-10-09. Conversation is not the canonical source, and the approval of this text is the merge of the pull request.

<!-- END: D-028-BOUNDED-SESSION-READ-LAW -->
