# AI Collaboration — Project Context / AI համագործակցություն — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Informative  
**Canonical scope / Canonical scope:** `foundation/ai-collaboration/`  
**Last synchronized / Վերջին համաժամեցում:** 2026-10-09

## Հայերեն

### Նպատակ

Այս context-ը օգնում է մարդկանց և AI collaborators-ին ճիշտ կիրառել [`README.md`](README.md)-ում locked AI Collaboration Standard v1-ը և [`CANONICAL_SESSION_READ_LAW.md`](CANONICAL_SESSION_READ_LAW.md)-ը։ Այն չի ստեղծում նոր authority կամ rule և չի փոխարինում canonical chapter-ին կամ law-ին։

### Պարտադիր session startup

Յուրաքանչյուր նոր MenQ Standard AI session մինչև substantive աշխատանք սկսելը պարտավոր է active branch/ref-ում ամբողջությամբ կարդալ session-read core-ը՝ [`SESSION_READ_MANIFEST.json`](SESSION_READ_MANIFEST.json)-ի `core` ցանկը, իսկ որևէ directory-ում աշխատելուց առաջ՝ նաև այդ directory-ի area-ի ֆայլերը։ Handoff-ը, summary-ն, partial range-ը կամ previous-session memory-ն core կամ area ֆայլի complete-read evidence չեն։ Եթե core-ի կամ area-ի որևէ file unreadable, inaccessible կամ truncated է, startup gate-ը RED է և աշխատանքը կանգնում է։

### Պարտադիր հիմքեր

AI Collaboration-ի հետ աշխատանքից առաջ core-ը և այս folder-ի area-ն կարդալուց հետո հատուկ հաստատել նաև՝

1. repository root `README.md`,
2. root `PROJECT_CONTEXT.md`,
3. `DECISION_INDEX.md` և historical `DECISIONS.md`,
4. `CHANGELOG.md`,
5. `foundation/README.md`,
6. `foundation/PROJECT_CONTEXT.md`,
7. `foundation/governance/README.md`,
8. `foundation/decision-system/README.md`,
9. `foundation/documentation/README.md`,
10. `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`,
11. այս folder-ի `README.md`,
12. `CANONICAL_SESSION_READ_LAW.md`,
13. `D-026-CANONICAL-SESSION-READ-LAW.md`,
14. `D-028-BOUNDED-SESSION-READ-LAW.md` և `SESSION_READ_MANIFEST.json`։

### Locked առանցք

- Human final authority և accountability։
- AI authority՝ միայն `G0–G2`։
- No self-approval և no invented approval։
- Ամեն նոր session-ում session-read core-ի complete read, իսկ աշխատանքի directory-ի համար՝ նրա area-ի complete read։
- Canonical context before session memory։
- Minimum necessary context և memory isolation։
- Explicit task contract, scope, risk, validation և handoff։
- Tool success-ը verification evidence չէ։
- Failure-ը բացահայտվում, contained և corrected է։
- Agent chain-ը human approval չի դառնում։
- Approved reusable learning-ը փաստաթղթավորվում է։

### Ընթացիկ վիճակ

- `README.md` — Locked v1։
- Related decisions — `D-023`, `D-026`, `D-028`։
- `CANONICAL_SESSION_READ_LAW.md` — v2՝ ըստ D-028-ի (հաստատված. Owner-ը merge է արել pull request #29-ը 2026-10-09-ին)։ v1-ը Locked էր D-026-ով։
- Foundation-ի բոլոր յոթ chapter-ները կառուցված են։
- Մեքենայորեն ստուգվում են Markdown inventory-ի drift-ը (Foundation validator) և session-read manifest-ն ու core-ի 120,000 բայթի սահմանը (`scripts/check_session_read_budget.py`)։ Ոչ մի ծրագիր չի ստուգում, որ session-ը որևէ բան կարդացել է։

---

## English

### Purpose

This context helps humans and AI collaborators correctly apply the locked AI Collaboration Standard v1 in [`README.md`](README.md) and the [`CANONICAL_SESSION_READ_LAW.md`](CANONICAL_SESSION_READ_LAW.md). It creates no new authority or rule and does not replace the canonical chapter or law.

### Mandatory session startup

Before substantive work begins, every new MenQ Standard AI session must read in full, on the active branch or ref, the session-read core, which is the `core` list of [`SESSION_READ_MANIFEST.json`](SESSION_READ_MANIFEST.json), and, before working in a directory, the files of that directory's area. A handoff, summary, partial range, or previous-session memory is not complete-read evidence for a core or area file. If any core or area file is unreadable, inaccessible, or truncated, the startup gate is RED and work stops.

### Required foundation

After reading the core and this folder's area, specifically confirm:

1. the repository root `README.md`,
2. root `PROJECT_CONTEXT.md`,
3. `DECISION_INDEX.md` and historical `DECISIONS.md`,
4. `CHANGELOG.md`,
5. `foundation/README.md`,
6. `foundation/PROJECT_CONTEXT.md`,
7. `foundation/governance/README.md`,
8. `foundation/decision-system/README.md`,
9. `foundation/documentation/README.md`,
10. `foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md`,
11. this folder's `README.md`,
12. `CANONICAL_SESSION_READ_LAW.md`,
13. `D-026-CANONICAL-SESSION-READ-LAW.md`,
14. `D-028-BOUNDED-SESSION-READ-LAW.md` and `SESSION_READ_MANIFEST.json`.

### Locked backbone

- Final human authority and accountability.
- AI authority limited to `G0–G2`.
- No self-approval and no invented approval.
- Complete reading of the session-read core in every new session and, for the directory being worked in, of its area.
- Canonical context before session memory.
- Minimum necessary context and memory isolation.
- Explicit task contract, scope, risk, validation, and handoff.
- Tool success is not verification evidence.
- Failures are disclosed, contained, and corrected.
- An agent chain does not become human approval.
- Approved reusable learning is documented.

### Current state

- `README.md` — Locked v1.
- Related decisions — `D-023`, `D-026`, `D-028`.
- `CANONICAL_SESSION_READ_LAW.md` — v2 under D-028 (approved; the Owner merged pull request #29 on 2026-10-09). v1 was Locked under D-026.
- All seven Foundation chapters are built.
- Machine-checked: Markdown inventory drift (Foundation validator), and the session-read manifest and the 120,000-byte core ceiling (`scripts/check_session_read_budget.py`). No program checks that a session read anything.

<!-- END: AI_COLLABORATION_PROJECT_CONTEXT -->