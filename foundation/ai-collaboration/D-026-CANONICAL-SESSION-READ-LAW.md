# D-026 — Canonical Session Read Law / Canonical session-ի ընթերցման օրենք

**Status / Կարգավիճակ:** Locked / Հաստատված  
**Date / Ամսաթիվ:** 2026-07-12  
**Decision class / Որոշման դաս:** `C4 — Foundation or Ecosystem`  
**Risk level / Ռիսկի մակարդակ:** `R2 — Moderate`  
**Owner / Պատասխանատու:** MenQ Owner  
**Approver / Հաստատող:** Gevorg Ohanyan, MenQ Owner  
**Scope / Scope:** Every new MenQ Standard AI session

## Problem / Խնդիր

**HY:** Startup subset-ը, handoff summary-ն կամ previous-session memory-ն բավարար չէին երաշխավորելու, որ նոր AI session-ը տեսել է repository-ի ամբողջ canonical truth-ը։ Սա կարող էր առաջացնել incomplete context, false completion, architecture drift և չկարդացած files-ի նկատմամբ սխալ verdict կամ write։

**EN:** A startup subset, handoff summary, or previous-session memory was insufficient to guarantee that a new AI session had seen the complete canonical truth of the repository. This could cause incomplete context, false completion, architectural drift, and incorrect verdicts or writes against unread files.

## Decision / Որոշում

**HY:** Յուրաքանչյուր նոր MenQ Standard AI session, մինչև որևէ substantive project աշխատանք սկսելը, պարտավոր է active branch/ref-ում enumerate անել և ամբողջությամբ կարդալ repository-ի բոլոր tracked `.md` ֆայլերը։ Եթե inventory-ն incomplete է, որևէ file unreadable/truncated է կամ complete-read evidence չկա, startup gate-ը RED է և աշխատանքը կանգնում է։

**EN:** Before beginning any substantive project work, every new MenQ Standard AI session must enumerate and completely read every tracked `.md` file on the active branch or ref. If the inventory is incomplete, any file is unreadable or truncated, or complete-read evidence is absent, the startup gate is RED and work stops.

## Canonical law / Canonical օրենք

The complete mandatory law is maintained in [`CANONICAL_SESSION_READ_LAW.md`](CANONICAL_SESSION_READ_LAW.md).

## Mandatory rules / Պարտադիր կանոններ

1. Every new session performs the read from zero against the current repository state.
2. Every tracked `.md` file in every directory is included.
3. The active working branch/ref is authoritative for the session read.
4. Active PR metadata, changed files, diff, review threads, and checks are also read when applicable.
5. Partial output, snippets, summaries, search results, prior memory, and tool success are not complete-read evidence.
6. Any missing or truncated read produces RED and blocks substantive work and canonical writes.
7. The law may not be bypassed for token limits, speed, repository size, or tool limitations.
8. Complete reading does not grant write authority or replace human approval.

## Relationship to existing standards / Կապը գործող ստանդարտների հետ

- This decision extends the AI Collaboration context-loading protocol.
- It does not replace the Canonical Write Integrity Law.
- The Session Read Law governs pre-task loading; the Write Integrity Law governs each canonical write.
- Both are mandatory Foundation controls.

## Evidence / Ապացույց

- Owner instruction in the MenQ Standard project conversation on 2026-07-12.
- Repeated context-loading failure in which work began before the complete required documentation set was read.
- Existing AI Collaboration, Documentation, Governance, and Decision System rules.

## Validation / Ստուգում

Validation requires:

1. the law file exists and is complete;
2. this decision is indexed in `DECISION_INDEX.md`;
3. root and Foundation navigation link the law;
4. AI context and handoff documents require the all-Markdown startup gate;
5. bilingual meaning is equal;
6. post-write integrity verification passes.

## Final rule / Վերջնական կանոն

**HY:** Չկարդացած repository-ից սկսված AI աշխատանքը MenQ Standard-ում վավեր աշխատանք չէ։

**EN:** AI work started from an unread repository is not valid work in MenQ Standard.

<!-- END: D-026-CANONICAL-SESSION-READ-LAW -->