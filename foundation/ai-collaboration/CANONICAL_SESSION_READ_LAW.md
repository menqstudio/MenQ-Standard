# Canonical Session Read Law / Canonical session-ի ընթերցման օրենք

**Status / Կարգավիճակ:** Locked v1 / Հաստատված v1  
**Version / Տարբերակ:** 1.0  
**Owner / Պատասխանատու:** MenQ Owner  
**Document class / Փաստաթղթի դաս:** Normative  
**Canonical path / Canonical ուղի:** `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`  
**Related decisions / Կապված որոշումներ:** `D-023`, `D-026`

## 1. Law / Օրենք

**HY:** Յուրաքանչյուր նոր MenQ Standard AI session պարտավոր է, մինչև որևէ project աշխատանք, analysis, proposal, write, edit, review, validation կամ verdict սկսելը, ամբողջ canonical repository-ի բոլոր `.md` ֆայլերը ամբողջությամբ կարդալ և հաստատել, որ ընթերցումը complete է։ Միայն startup subset, handoff, summary, search snippet, partial range կամ chat memory կարդալը բավարար չէ։

**EN:** Every new MenQ Standard AI session must, before beginning any project work, analysis, proposal, write, edit, review, validation, or verdict, read every `.md` file in the complete canonical repository in full and confirm that the read is complete. Reading only a startup subset, handoff, summary, search snippet, partial range, or chat memory is insufficient.

## 2. Scope / Կիրառման սահման

Այս օրենքը կիրառվում է՝

1. MenQ Standard-ի յուրաքանչյուր նոր chat կամ AI session-ի նկատմամբ,
2. ցանկացած AI collaborator, agent, orchestrator կամ specialist agent-ի նկատմամբ, որը MenQ Standard canonical repository-ի վրա աշխատում է,
3. repository-ի բոլոր tracked `.md` ֆայլերի նկատմամբ՝ բոլոր directories-ում և active branch/ref-ում,
4. նոր session-ից հետո առաջին substantive պատասխանից առաջ։

This law applies to every new MenQ Standard chat or AI session, every AI collaborator, agent, orchestrator, or specialist working with the canonical repository, every tracked `.md` file in all directories on the active branch or ref, and before the first substantive response after session start.

## 3. Mandatory Startup Gate / Պարտադիր startup gate

Նոր session-ը project աշխատանքի չի անցնում, մինչև բոլոր քայլերը GREEN չեն՝

1. հաստատել canonical repository-ն և active branch/ref-ը,
2. enumerate անել repository-ի բոլոր tracked `.md` ֆայլերը,
3. յուրաքանչյուր `.md` file ամբողջությամբ կարդալ՝ beginning-ից ending marker կամ end-of-file,
4. truncation, unreadable content, inaccessible file կամ failed fetch հայտնաբերել,
5. retry կամ alternate safe read method օգտագործել մինչև complete read,
6. կարդալ active PR metadata, changed files, diff, review threads և checks, երբ աշխատանքը կապված է active PR-ի հետ,
7. միայն իրական complete read-ից հետո հայտարարել startup gate-ը GREEN։

A new session may not proceed to project work until it has identified the canonical repository and active branch or ref, enumerated all tracked `.md` files, read each file completely from beginning to ending marker or end-of-file, detected truncation or access failures, retried through a safe alternative method when needed, read active PR metadata and evidence when relevant, and established a real GREEN startup gate.

## 4. Evidence Rule / Ապացույցի կանոն

**HY:** «Կարդացի», «context-ը գիտեմ», tool success-ը, file search result-ը կամ partial output-ը complete-read evidence չեն։ Evidence-ը file inventory-ն է, յուրաքանչյուր file-ի complete-read result-ը, unresolved read failure-ների բացակայությունը և active branch/ref-ի traceability-ն։

**EN:** Statements such as “I read it,” prior familiarity, tool success, file-search results, or partial output are not complete-read evidence. Evidence consists of the file inventory, a complete-read result for every file, absence of unresolved read failures, and traceability to the active branch or ref.

## 5. RED Stop Rule / RED կանգառի կանոն

Եթե որևէ `.md` file ամբողջությամբ չի կարդացվել, inaccessible է, truncated է կամ inventory-ն ամբողջական չէ՝

1. startup gate-ը RED է,
2. AI-ն չի կարող ասել, որ ամբողջ repository-ն կարդացել է,
3. substantive project work-ը կանգնում է,
4. canonical write, decision proposal, architecture verdict կամ validation չի կատարվում,
5. AI-ն բացահայտ հայտնում է կոնկրետ չկարդացված կամ չստուգված files-ը,
6. աշխատանքը շարունակվում է միայն missing read-ը complete դարձնելուց հետո։

If any `.md` file has not been read completely, is inaccessible, is truncated, or the inventory is incomplete, the startup gate is RED; the AI may not claim the repository was fully read; substantive work stops; no canonical write, decision proposal, architecture verdict, or validation proceeds; the exact unread or unverified files are disclosed; and work resumes only after the missing reads are completed.

## 6. No Shortcut Rule / Կարճ ճանապարհի արգելք

Այս օրենքը չի շրջանցվում՝

- token կամ context limit-ով,
- ժամանակ խնայելու պատճառաբանությամբ,
- նախկին session memory-ով,
- handoff summary-ով,
- «relevant files only» մոտեցմամբ,
- file count-ի մեծությամբ,
- tool limitation-ով,
- Owner-ի հայտնի instruction-ները հիշելու պատճառաբանությամբ։

This law may not be bypassed because of token or context limits, speed, prior session memory, a handoff summary, a relevant-files-only approach, repository size, tool limitations, or remembered Owner instructions.

## 7. Session Isolation Rule / Session isolation-ի կանոն

**HY:** Նախորդ session-ի complete read-ը չի փոխանցվում որպես ընթացիկ session-ի evidence։ Յուրաքանչյուր նոր session իր startup gate-ը կատարում է զրոյից՝ canonical repository-ի ընթացիկ state-ի նկատմամբ։

**EN:** A complete read performed in a previous session does not transfer as evidence to the current session. Every new session performs its own startup gate from zero against the current state of the canonical repository.

## 8. Branch and Change Awareness / Branch և փոփոխությունների awareness

AI-ն պարտավոր է կարդալ այն branch/ref-ը, որի վրա իրական աշխատանքը կատարվում է։ Default branch-ի read-ը չի փոխարինում working branch-ի read-ին։ Active PR-ի դեպքում PR diff-ը լրացնում է, բայց չի փոխարինում full repository read-ին։

The AI must read the branch or ref on which the real work is being performed. Reading the default branch does not replace reading the working branch. For an active PR, the PR diff supplements but does not replace the full repository read.

## 9. Delegation Rule / Delegation-ի կանոն

Orchestrator-ը չի կարող complete-read պարտականությունը փոխանցել specialist agent-ին և առանց evidence-ի GREEN համարել։ Եթե read-ը բաժանվում է agents-ի միջև, պարտադիր են complete inventory, exact ownership per file, complete results, failure disclosure և final synthesis։ Agent chain-ը complete-read evidence չի դառնում ինքնաբերաբար։

An orchestrator may not delegate the read obligation and declare GREEN without evidence. If reading is distributed across agents, the process requires a complete inventory, exact ownership per file, complete results, disclosed failures, and final synthesis. An agent chain does not automatically become complete-read evidence.

## 10. Relationship to Other Laws / Կապը այլ օրենքների հետ

- Այս օրենքը գործում է մինչև task execution-ը։
- `CANONICAL_WRITE_INTEGRITY_LAW.md`-ը գործում է յուրաքանչյուր canonical write-ի ժամանակ։
- Երկու օրենքներն էլ պարտադիր են և չեն փոխարինում միմյանց։
- Complete repository read-ը write permission կամ human approval չի ստեղծում։

This law governs pre-task session loading. `CANONICAL_WRITE_INTEGRITY_LAW.md` governs every canonical write. Both are mandatory and neither replaces the other. A complete repository read does not create write authority or human approval.

## 11. Completion Sequence / Ավարտի sequence

```text
IDENTIFY CANONICAL REPOSITORY AND ACTIVE REF
→ ENUMERATE ALL TRACKED .MD FILES
→ READ EVERY .MD FILE COMPLETELY
→ VERIFY NO TRUNCATION OR ACCESS FAILURE
→ READ ACTIVE PR EVIDENCE WHEN APPLICABLE
→ RECORD COMPLETE-READ EVIDENCE
→ STARTUP GATE GREEN
→ BEGIN PROJECT WORK
```

## 12. Final Rule / Վերջնական կանոն

> **HY:** Չկարդացած repository-ից սկսված AI աշխատանքը MenQ Standard-ում վավեր աշխատանք չէ։  
> **EN:** AI work started from an unread repository is not valid work in MenQ Standard.

<!-- END: CANONICAL_SESSION_READ_LAW_V1 -->
