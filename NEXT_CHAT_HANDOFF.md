# MenQ Standard — Next Chat Handoff / Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-07-13  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Canonical ref:** `main`

## Հայերեն

### Պարտադիր մեկնարկ

Մինչև substantive աշխատանք՝ active branch/ref-ում enumerate և ամբողջությամբ կարդալ repository-ի բոլոր tracked `.md` files-ը՝ ըստ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`-ի։ Active PR-ի դեպքում կարդալ metadata, changed files, diff, review threads և checks։

### Ընթացիկ վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 — merged և canonical։
- D-025 — Locked և GREEN։
- D-026 — Locked և machine-enforced։
- D-025 implementation merge — `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`։
- D-025 closure merge — `9a833339b1d707d6cd8a792e031dd8ca2857d556`։
- D-025 lock merge — `261f85e5b20d726a0ab1f05da84a4dc45a248873`։
- Validated lock head — `8ba2e987ff6dab2c25fda18744c7376953d0108f`։
- Architecture, implementation, consumer, closure և lock evidence — GREEN։
- Final post-lock audit record — `platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md`։
- D-025 transaction-ը փակված է։

### Շարունակելու ճշգրիտ կետը

1. Ընտրել MenQ Standard-ի հաջորդ ecosystem priority-ն։
2. Բացել առանձին decision transaction։
3. D-025-ը փոխել միայն governed change request, impact analysis, compatibility/migration evidence, validators և explicit Owner approval ճանապարհով։

### Արգելված գործողություններ

- D-025-ի locked boundary-ն silently չփոխել։
- Historical evidence-ը չջնջել կամ վերագրել։
- Generated artifacts-ը canonical source չհամարել։

---

## English

### Mandatory startup

Before substantive work, enumerate and completely read every tracked `.md` file on the active branch/ref under `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`. For an active PR, read metadata, changed files, diff, review threads, and checks.

### Current state

- Foundation v1 is Locked and GREEN.
- D-024 is merged and canonical.
- D-025 is Locked and GREEN.
- D-026 is Locked and machine-enforced.
- D-025 implementation merge: `2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc`.
- D-025 closure merge: `9a833339b1d707d6cd8a792e031dd8ca2857d556`.
- D-025 lock merge: `261f85e5b20d726a0ab1f05da84a4dc45a248873`.
- Validated lock head: `8ba2e987ff6dab2c25fda18744c7376953d0108f`.
- Architecture, implementation, consumer, closure, and lock evidence are GREEN.
- Final post-lock audit record: `platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md`.
- The D-025 transaction is closed.

### Exact continuation point

1. Select the next MenQ Standard ecosystem priority.
2. Open a separate decision transaction.
3. Change D-025 only through a governed change request, impact analysis, compatibility and migration evidence, validators, and explicit Owner approval.

### Prohibited actions

- Do not silently change the D-025 locked boundary.
- Do not delete or rewrite historical evidence.
- Do not treat generated artifacts as canonical source.

<!-- END: MENQ_STANDARD_NEXT_CHAT_HANDOFF -->