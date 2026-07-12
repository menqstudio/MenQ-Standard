# MenQ Standard — Next Chat Handoff / Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-07-12  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Working branch:** `d-025-design-platform-architecture-v1`  
**Draft PR:** `https://github.com/menqstudio/MenQ-Standard/pull/3`

## Հայերեն

### Պարտադիր մեկնարկ

Մինչև substantive աշխատանք՝ active branch/ref-ում enumerate և ամբողջությամբ կարդալ repository-ի բոլոր tracked `.md` files-ը՝ ըստ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`-ի։ Active PR-ի դեպքում կարդալ metadata, changed files, diff, review threads և checks։ Repository-ի հասցեն, Owner-ի անունը, project-ի նպատակը, communication style-ը կամ continuation point-ը կրկին չհարցնել։

### Ընթացիկ վիճակ

- Foundation v1 — Locked, բայց current branch integrity gate-ը RED է մինչև truncation remediation-ի CI GREEN evidence-ը։
- D-024 — merged և canonical։
- D-025 — `Approved — Implementing`, ոչ `Locked`։
- D-026 — Locked և machine-enforced։
- Draft PR #3 — open, Draft և unmerged։
- Parts 1–16 architecture set-ը canonical է։
- `D-025_COMPLETENESS_AUDIT.md` և `D-025_DRAFT_PR_REVIEW_RECORD.md` canonical են։
- Architecture verdict-ը GREEN է։
- Implementation/lock readiness-ը YELLOW է։
- Root `NEXT_CHAT_HANDOFF.md` և `foundation/terminology/PROJECT_CONTEXT.md` truncation defects-ը remediation transaction-ի scope-ն են։

### Architecture invariants

- Shared core-ը product-neutral է։
- Canonical dependency model-ը՝ Reference → Semantic → Component → Pattern → Product Extension։
- Generated output-ը source of truth չէ։
- Armenian և English canonical languages են։
- Accessibility-ը release condition է։
- Unowned canonical asset-ը RED governance defect է։
- Merge-ը և lock-ը միայն explicit Owner decisions են։

### Շարունակելու ճշգրիտ կետը

1. Ավարտել confirmed truncation defects-ի remediation-ը։
2. Regenerate անել canonical Markdown inventory-ն։
3. Ստանալ GREEN Foundation, Markdown Inventory, Platforms և Foundation Package workflow evidence։
4. Միայն դրանից հետո շարունակել Implementation Phase A-ն՝ machine-readable specification registry, schemas, canonical IDs, ownership records, dependency graph և package/workspace skeleton։
5. Ընտրել երկու distinct real consumer candidates և bounded pilot scopes՝ առանց fake evidence-ի։

### Արգելված գործողություններ

- PR #3-ը չmerge անել և ready-for-review չդարձնել առանց Owner instruction-ի։
- D-025-ը `Locked` չանվանել։
- RED integrity gate-ը GREEN չներկայացնել։
- Product-specific identity, logic կամ workflows shared core չմտցնել։
- Generated artifacts-ը canonical source չհամարել։
- Fake consumer կամ implementation evidence չստեղծել։

---

## English

### Mandatory startup

Before substantive work, enumerate and completely read every tracked `.md` file on the active branch/ref under `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`. For the active PR, read metadata, changed files, diff, review threads, and checks. Do not ask again for the repository address, Owner identity, project purpose, communication style, or continuation point.

### Current state

- Foundation v1 is Locked, but the current branch integrity gate is RED until truncation remediation has GREEN CI evidence.
- D-024 is merged and canonical.
- D-025 is `Approved — Implementing`, not `Locked`.
- D-026 is Locked and machine-enforced.
- Draft PR #3 is open, Draft, and unmerged.
- The Parts 1–16 architecture set is canonical.
- `D-025_COMPLETENESS_AUDIT.md` and `D-025_DRAFT_PR_REVIEW_RECORD.md` are canonical.
- Architecture is GREEN.
- Implementation and lock readiness remain YELLOW.
- The root `NEXT_CHAT_HANDOFF.md` and `foundation/terminology/PROJECT_CONTEXT.md` truncation defects are the scope of the active remediation transaction.

### Architecture invariants

- Shared core is product-neutral.
- Canonical dependency model: Reference → Semantic → Component → Pattern → Product Extension.
- Generated output is not a source of truth.
- Armenian and English are canonical languages.
- Accessibility is a release condition.
- An unowned canonical asset is a RED governance defect.
- Merge and lock require explicit Owner decisions.

### Exact continuation point

1. Complete remediation of the confirmed truncation defects.
2. Regenerate the canonical Markdown inventory.
3. Obtain GREEN evidence from Foundation, Markdown Inventory, Platforms, and Foundation Package workflows.
4. Only then continue Implementation Phase A with the machine-readable specification registry, schemas, canonical IDs, ownership records, dependency graph, and package/workspace skeleton.
5. Select two distinct real consumer candidates and bounded pilot scopes without fabricating evidence.

### Prohibited actions

- Do not merge PR #3 or mark it ready for review without Owner instruction.
- Do not describe D-025 as Locked.
- Do not represent a RED integrity gate as GREEN.
- Do not move product-specific identity, logic, or workflows into shared core.
- Do not treat generated artifacts as canonical source.
- Do not fabricate consumer or implementation evidence.

<!-- END: MENQ_STANDARD_NEXT_CHAT_HANDOFF -->
