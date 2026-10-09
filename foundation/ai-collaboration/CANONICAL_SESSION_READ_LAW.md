# Canonical Session Read Law / Canonical session-ի ընթերցման օրենք

**Status / Կարգավիճակ:** v2 — proposed under `D-028`; in force from the Owner's merge of the D-028 pull request. v1 (Locked, `D-026`) is superseded in part. / v2 — առաջարկված `D-028`-ով. ուժի մեջ է մտնում, երբ Owner-ը merge է անում D-028-ի pull request-ը։ v1-ը (Locked, `D-026`) մասամբ փոխարինված է։  
**Version / Տարբերակ:** 2.0  
**Owner / Պատասխանատու:** MenQ Owner  
**Document class / Փաստաթղթի դաս:** Normative  
**Canonical path / Canonical ուղի:** `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`  
**Related decisions / Կապված որոշումներ:** `D-023`, `D-026`, `D-028`

## 1. Law / Օրենք

**HY:** Յուրաքանչյուր նոր MenQ Standard AI session պարտավոր է, մինչև որևէ project աշխատանք, analysis, proposal, write, edit, review, validation կամ verdict սկսելը, ամբողջությամբ կարդալ session-read CORE-ի բոլոր ֆայլերը՝ [`SESSION_READ_MANIFEST.json`](SESSION_READ_MANIFEST.json)-ի `core` ցանկը, նրա հերթականությամբ։ Որևէ directory-ում աշխատելուց առաջ session-ը ամբողջությամբ կարդում է նաև այն ֆայլերը, որոնք manifest-ը նշում է այդ directory-ի AREA-ի համար։ Core կամ area ֆայլի փոխարեն handoff, summary, search snippet, partial range կամ chat memory կարդալը բավարար չէ։ Core-ը սահմանափակ է․ gate-ը այն պահում է ընդհանուր 120,000 բայթի սահմանում, ուստի token կամ context limit-ը չի կարող այն չկարդալու պատճառ լինել։

**EN:** Every new MenQ Standard AI session must, before beginning any project work, analysis, proposal, write, edit, review, validation, or verdict, read in full every file of the session-read CORE: the `core` list of [`SESSION_READ_MANIFEST.json`](SESSION_READ_MANIFEST.json), in its order. Before working in a directory, the session also reads in full the files the manifest lists for that directory's AREA. Reading a handoff, summary, search snippet, partial range, or chat memory in place of a core or area file is insufficient. The core is bounded: a gate holds it to 120,000 bytes in total, so a token or context limit cannot be a reason not to read it.

## 2. Scope / Կիրառման սահման

**HY:** Այս օրենքը կիրառվում է՝

1. MenQ Standard-ի յուրաքանչյուր նոր chat կամ AI session-ի նկատմամբ,
2. ցանկացած AI collaborator, agent, orchestrator կամ specialist agent-ի նկատմամբ, որը MenQ Standard canonical repository-ի վրա աշխատում է,
3. core-ի նկատմամբ՝ manifest-ի `core` ցանկի յուրաքանչյուր ֆայլ, active branch/ref-ում, միշտ և առաջին substantive պատասխանից առաջ,
4. area-ի նկատմամբ՝ այն ֆայլերը, որոնք manifest-ի `areas`-ը նշում է աշխատանքի դիպած directory-ի համար, այդ directory-ում առաջին փոփոխությունից կամ verdict-ից առաջ։ Path-ի area-ն manifest-ում նշված ամենամոտ directory-ն է՝ հենց այդ path-ի directory-ն կամ նրանից վեր․ եթե ավելի մոտ directory նշված չէ, գործում է root area-ն՝ `.`։ Մի քանի directory-ի դիպչող աշխատանքը կարդում է դրանցից յուրաքանչյուրի area-ն,
5. core-ից և session-ի area-ներից դուրս գտնվող ցանկացած tracked ֆայլի նկատմամբ՝ այն պահից, երբ session-ը հենվում է դրա վրա, մեջբերում է, գնահատում կամ փոխում է այն․ այդ ֆայլը նախ կարդացվում է ամբողջությամբ։

**EN:** This law applies:

1. to every new MenQ Standard chat or AI session,
2. to any AI collaborator, agent, orchestrator, or specialist agent working on the MenQ Standard canonical repository,
3. to the core: every file in the manifest's `core` list, on the active branch/ref, always and before the first substantive response,
4. to the area: the files the manifest's `areas` lists for the directory the work touches, before the first change or verdict in that directory. The area of a path is the nearest directory listed in the manifest, at that path's own directory or above it; when no nearer directory is listed, the root area `.` applies. Work that touches several directories reads the area of each,
5. to any tracked file outside the core and outside the session's areas, from the moment the session relies on it, cites it, judges it, or changes it: that file is first read in full.

## 3. Mandatory Startup Gate / Պարտադիր startup gate

**HY:** Նոր session-ը project աշխատանքի չի անցնում, մինչև բոլոր քայլերը GREEN չեն՝

1. հաստատել canonical repository-ն և active branch/ref-ը,
2. կարդալ manifest-ը և որոշել core-ը և task-ի area-ները,
3. core-ի յուրաքանչյուր ֆայլ ամբողջությամբ կարդալ manifest-ի հերթականությամբ՝ beginning-ից ending marker կամ end-of-file,
4. truncation, unreadable content, inaccessible file կամ failed fetch հայտնաբերել,
5. retry կամ alternate safe read method օգտագործել մինչև complete read,
6. կարդալ active PR metadata, changed files, diff, review threads և checks, երբ աշխատանքը կապված է active PR-ի հետ,
7. որևէ directory-ում աշխատելուց առաջ ամբողջությամբ կարդալ նրա area-ի ֆայլերը,
8. միայն core-ի իրական complete read-ից հետո հայտարարել startup gate-ը GREEN։

**EN:** A new session does not proceed to project work until all steps are GREEN:

1. confirm the canonical repository and the active branch/ref,
2. read the manifest and determine the core and the areas of the task,
3. read each core file completely in the manifest's order, from the beginning to the ending marker or end-of-file,
4. detect truncation, unreadable content, an inaccessible file, or a failed fetch,
5. use a retry or an alternate safe read method until the read is complete,
6. read the active PR metadata, changed files, diff, review threads, and checks when the work is tied to an active PR,
7. before working in a directory, read the files of its area completely,
8. declare the startup gate GREEN only after a real complete read of the core.

## 4. Evidence Rule / Ապացույցի կանոն

**HY:** «Կարդացի», «context-ը գիտեմ», tool success-ը, file search result-ը կամ partial output-ը complete-read evidence չեն։ Evidence-ը active ref-ի manifest-ն է, core-ի և կարդացված area-ի յուրաքանչյուր ֆայլի complete-read result-ը, unresolved read failure-ների բացակայությունը և active branch/ref-ի traceability-ն։ `scripts/check_session_read_budget.py --receipt`-ը տպում է մեկ SHA-256 digest core-ի ֆայլերի բովանդակության վրա՝ manifest-ի հերթականությամբ։ Receipt-ը, որը գրանցել է core-ը session-ին փոխանցած գործիքը, ապացուցում է, թե core-ի որ բովանդակությունն է փոխանցվել և ինչ content hash-ով։ Այն չի ապացուցում և չի կարող ապացուցել, որ session-ը հասկացել է կարդացածը։ Digest-ը, որը session-ը ինքն է հաշվել, ապացուցում է միայն, որ session-ը կարողացել է գործարկել հրամանը։ Այս repository-ում ոչ մի ծրագիր չի ստուգում, որ session-ը որևէ բան կարդացել է․ gate-ը ստուգում է միայն manifest-ը, բայթերի սահմանը և receipt-ի հաշվարկը։

**EN:** Statements such as “I read it,” prior familiarity, tool success, file-search results, or partial output are not complete-read evidence. Evidence consists of the manifest at the active ref, a complete-read result for every core file and every area file read, absence of unresolved read failures, and traceability to the active branch or ref. `scripts/check_session_read_budget.py --receipt` prints one SHA-256 digest over the content of the core files in the manifest's order. A receipt recorded by the tool that delivered the core to the session proves which core content was delivered and at which content hash. It does not and cannot prove that the session understood what it read. A digest the session computed for itself proves only that the session was able to run the command. No program in this repository checks that a session read anything: the gate checks only the manifest, the byte ceiling, and the receipt arithmetic.

## 5. RED Stop Rule / RED կանգառի կանոն

**HY:** Եթե core-ի որևէ ֆայլ կամ աշխատանքի դիպած area-ի որևէ ֆայլ ամբողջությամբ չի կարդացվել, inaccessible է, truncated է, կամ manifest-ը բացակայում է կամ անվավեր է՝

1. startup gate-ը RED է,
2. AI-ն չի կարող ասել, որ core-ը կամ area-ն կարդացել է, և չի կարող ասել, որ ամբողջ repository-ն կարդացել է, եթե չի կարդացել,
3. substantive project work-ը կանգնում է,
4. canonical write, decision proposal, architecture verdict կամ validation չի կատարվում,
5. AI-ն բացահայտ հայտնում է կոնկրետ չկարդացված կամ չստուգված files-ը,
6. աշխատանքը շարունակվում է միայն missing read-ը complete դարձնելուց հետո։

**EN:** If any core file or any file of an area the work touches has not been read completely, is inaccessible, is truncated, or the manifest is missing or invalid:

1. the startup gate is RED,
2. the AI may not say that it has read the core or the area, and may not say that it has read the entire repository when it has not,
3. substantive project work stops,
4. no canonical write, decision proposal, architecture verdict, or validation is performed,
5. the AI explicitly discloses the specific unread or unverified files,
6. work continues only after the missing read has been made complete.

## 6. No Shortcut Rule / Կարճ ճանապարհի արգելք

**HY:** Core-ի ընթերցումը չի շրջանցվում՝

- token կամ context limit-ով,
- ժամանակ խնայելու պատճառաբանությամբ,
- նախկին session memory-ով,
- handoff summary-ով,
- «relevant files only» մոտեցմամբ,
- file count-ի մեծությամբ,
- tool limitation-ով,
- Owner-ի հայտնի instruction-ները հիշելու պատճառաբանությամբ։

Area-ի ֆայլը նույնպես չի փոխարինվում summary-ով կամ հիշողությամբ։ Եթե core-ը չափազանց մեծացել է, լուծումը manifest-ը որոշմամբ փոխելն է, ոչ թե ֆայլ բաց թողնելը։

**EN:** The core read may not be bypassed:

- because of a token or context limit,
- on the grounds of saving time,
- through previous session memory,
- through a handoff summary,
- through a "relevant files only" approach,
- because of the size of the file count,
- because of a tool limitation,
- on the grounds of remembering the Owner's known instructions.

An area file is likewise not replaced by a summary or by memory. When the core has grown too large, the remedy is to change the manifest through a decision, never to skip a file.

## 7. Session Isolation Rule / Session isolation-ի կանոն

**HY:** Նախորդ session-ի core կամ area read-ը չի փոխանցվում որպես ընթացիկ session-ի evidence։ Յուրաքանչյուր նոր session իր startup gate-ը կատարում է զրոյից՝ canonical repository-ի ընթացիկ state-ի նկատմամբ։

**EN:** A core or area read performed in a previous session does not transfer as evidence to the current session. Every new session performs its own startup gate from zero against the current state of the canonical repository.

## 8. Branch and Change Awareness / Branch և փոփոխությունների awareness

AI-ն պարտավոր է կարդալ այն branch/ref-ը, որի վրա իրական աշխատանքը կատարվում է։ Default branch-ի read-ը չի փոխարինում working branch-ի read-ին։ Active PR-ի դեպքում PR diff-ը լրացնում է, բայց չի փոխարինում core-ի և area-ի read-ին։

The AI must read the branch or ref on which the real work is being performed. Reading the default branch does not replace reading the working branch. For an active PR, the PR diff supplements but does not replace the core and area read.

## 9. Delegation Rule / Delegation-ի կանոն

Orchestrator-ը չի կարող read-ի պարտականությունը փոխանցել specialist agent-ին և առանց evidence-ի GREEN համարել։ Եթե read-ը բաժանվում է agents-ի միջև, պարտադիր են manifest-ը, exact ownership per file, complete results, failure disclosure և final synthesis։ Agent chain-ը complete-read evidence չի դառնում ինքնաբերաբար։

An orchestrator may not delegate the read obligation and declare GREEN without evidence. If reading is distributed across agents, the process requires the manifest, exact ownership per file, complete results, disclosed failures, and final synthesis. An agent chain does not automatically become complete-read evidence.

## 10. Relationship to Other Laws / Կապը այլ օրենքների հետ

**HY:**

- Այս օրենքը գործում է մինչև task execution-ը։
- `CANONICAL_WRITE_INTEGRITY_LAW.md`-ը գործում է յուրաքանչյուր canonical write-ի ժամանակ և պահանջում է փոփոխվող ֆայլի ամբողջական ընթերցում՝ անկախ նրանից, core-ում է այն, area-ում, թե դրանցից դուրս։
- Երկու օրենքներն էլ պարտադիր են և չեն փոխարինում միմյանց։
- Core-ի կամ area-ի complete read-ը write permission կամ human approval չի ստեղծում։
- `MARKDOWN_INVENTORY.json`-ը և նրա drift check-ը մնում են․ դրանք ցույց են տալիս, թե ինչ Markdown կա repository-ում, ոչ թե ինչ է կարդացվել։

**EN:**

- This law operates before task execution.
- `CANONICAL_WRITE_INTEGRITY_LAW.md` operates during every canonical write and requires a complete read of the file being changed, whether it is in the core, in an area, or outside both.
- Both laws are mandatory and do not replace each other.
- A complete read of the core or of an area does not create write permission or human approval.
- `MARKDOWN_INVENTORY.json` and its drift check remain: they show what Markdown the repository holds, not what was read.

## 11. Completion Sequence / Ավարտի sequence

```text
IDENTIFY CANONICAL REPOSITORY AND ACTIVE REF
→ READ SESSION_READ_MANIFEST.json
→ READ EVERY CORE FILE COMPLETELY, IN ORDER
→ VERIFY NO TRUNCATION OR ACCESS FAILURE
→ READ ACTIVE PR EVIDENCE WHEN APPLICABLE
→ RECORD COMPLETE-READ EVIDENCE
→ STARTUP GATE GREEN
→ READ THE AREA OF EACH DIRECTORY BEFORE WORKING IN IT
→ BEGIN PROJECT WORK
```

## 12. Final Rule / Վերջնական կանոն

> **HY:** Առանց core-ի ամբողջական ընթերցման սկսված AI աշխատանքը MenQ Standard-ում վավեր աշխատանք չէ։  
> **EN:** AI work started without a complete read of the core is not valid work in MenQ Standard.

<!-- END: CANONICAL_SESSION_READ_LAW_V1 -->
