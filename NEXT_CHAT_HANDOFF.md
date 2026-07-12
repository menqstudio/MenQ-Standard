# MenQ Standard — Next Chat Handoff / Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-07-13  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Working branch:** `d-025-post-merge-closure`

## Հայերեն

### Պարտադիր մեկնարկ

Մինչև substantive աշխատանք՝ active branch/ref-ում enumerate և ամբողջությամբ կարդալ repository-ի բոլոր tracked `.md` files-ը՝ ըստ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`-ի։ Active PR-ի դեպքում կարդալ metadata, changed files, diff, review threads և checks։

### Ընթացիկ վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 — merged և canonical։
- D-025 — PR #3-ով merge է եղել, բայց `Locked` չէ։
- D-026 — Locked և machine-enforced։
- PR #3 merge commit — `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`։
- Merged implementation head — `9c10c288c16ef319ce4d5aa91000f7b0a46ecf60`։
- Closure branch — `d-025-post-merge-closure`։
- Architecture, implementation և consumer evidence — GREEN։
- Canonical synchronization և post-merge automation evidence — IN PROGRESS։
- Overall closure verdict — YELLOW։

### Շարունակելու ճշգրիտ կետը

1. Ավարտել stale current-state documentation synchronization-ը։
2. Regenerate անել canonical Markdown inventory-ն։
3. Ստանալ closure PR-ի բոլոր պարտադիր GREEN checks-ը։
4. Merge անել closure PR-ը միայն explicit Owner approval-ով։
5. Ստանալ GREEN `main` push workflow evidence։
6. Finalize անել `platforms/design/D-025_POST_MERGE_CLOSURE_RECORD.md`-ը։
7. Առանձին ներկայացնել D-025 lock որոշումը Owner-ին։

### Արգելված գործողություններ

- D-025-ը `Locked` չանվանել մինչև առանձին explicit Owner decision։
- YELLOW closure-ը GREEN չներկայացնել։
- Generated artifacts-ը canonical source չհամարել։

---

## English

### Mandatory startup

Before substantive work, enumerate and completely read every tracked `.md` file on the active branch/ref under `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`. For an active PR, read metadata, changed files, diff, review threads, and checks.

### Current state

- Foundation v1 is Locked and GREEN.
- D-024 is merged and canonical.
- D-025 was merged through PR #3 but is not `Locked`.
- D-026 is Locked and machine-enforced.
- PR #3 merge commit: `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`.
- Merged implementation head: `9c10c288c16ef319ce4d5aa91000f7b0a46ecf60`.
- Closure branch: `d-025-post-merge-closure`.
- Architecture, implementation, and consumer evidence are GREEN.
- Canonical synchronization and post-merge automation evidence are IN PROGRESS.
- Overall closure verdict is YELLOW.

### Exact continuation point

1. Complete stale current-state documentation synchronization.
2. Regenerate the canonical Markdown inventory.
3. Obtain all required GREEN closure PR checks.
4. Merge the closure PR only with explicit Owner approval.
5. Obtain GREEN `main` push workflow evidence.
6. Finalize `platforms/design/D-025_POST_MERGE_CLOSURE_RECORD.md`.
7. Present a separate D-025 lock decision to the Owner.

### Prohibited actions

- Do not describe D-025 as `Locked` without a separate explicit Owner decision.
- Do not represent YELLOW closure as GREEN.
- Do not treat generated artifacts as canonical source.

<!-- END: MENQ_STANDARD_NEXT_CHAT_HANDOFF -->
