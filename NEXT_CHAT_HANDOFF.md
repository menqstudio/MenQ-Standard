# MenQ Standard — Next Chat Handoff / Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-07-12  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Working branch:** `d-025-design-platform-architecture-v1`  
**Draft PR:** `https://github.com/menqstudio/MenQ-Standard/pull/3`

## Հայերեն

### Պարտադիր հրահանգ

Նոր chat-ում repository-ի հասցեն, Owner-ի անունը, project-ի նպատակը, communication style-ը կամ continuation point-ը կրկին չհարցնել։ Մինչ substantive աշխատանք՝ active branch/ref-ում enumerate և ամբողջությամբ կարդալ բոլոր tracked `.md` files-ը՝ ըստ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`-ի։ Active PR-ի դեպքում կարդալ metadata, changed files, diff, review threads և checks։

### Ընթացիկ վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 — merged և canonical։
- D-025 — `Approved — Implementing`, ոչ `Locked`։
- D-026 — Locked և machine-enforced։
- Draft PR #3 — open, Draft, unmerged։
- Parts 1–11 baseline-ը canonical է։
- Part 12 validation/CI/conformance/quality-gates architecture-ը canonical է։
- Part 13 documentation portal/component catalog/design-tool integration architecture-ը canonical է։
- Part 14 governance/contribution/ownership/change-request lifecycle architecture-ը canonical է։

### Architecture invariants

- Canonical dependency model՝ Reference → Semantic → Component → Pattern → Product Extension։
- Theme/state/density/platform/locale/accessibility/motion preference-ը orthogonal dimensions են։
- Controlled exceptions-ը governed bypass են։
- Shared core-ը product-neutral է։
- Portal, catalog և design-tool integration-ը նույն repository source-ի governed views են, ոչ parallel truth systems։
- Unowned canonical asset-ը RED defect է։
- High-risk կամ breaking change-ի self-approval-ը արգելված է։
- Merge-ը առանձին authority action է, ոչ GREEN CI-ի ավտոմատ հետևանք։
- Armenian և English canonical languages են։

### Հստակ continuation point

Ուղիղ սկսել՝

## Part 16 — Canonical Specification Index and Implementation Package Plan

Հետո՝ canonical specification index, implementation package plan, completeness audit, validator design, GREEN evidence և Owner review։ Merge և lock-ը առանձին explicit decisions են։

### Արգելված գործողություններ

- PR #3-ը չmerge անել և ready-for-review չդարձնել առանց Owner instruction-ի։
- D-025-ը `Locked` չանվանել։
- Product-specific identity, business logic կամ workflows shared core չմտցնել։
- Generated docs/catalog/design-tool outputs-ը canonical source չհամարել։
- High-risk կամ breaking change-ը self-approve չանել։
- GREEN CI-ն merge approval չհամարել։
- Tool success-ը GREEN evidence չհամարել։

---

## English

### Mandatory instruction

Do not ask again for the repository address, Owner identity, project purpose, communication style, or continuation point. Before substantive work, enumerate and completely read all tracked `.md` files on the active branch/ref under `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`. For the active PR, read metadata, changed files, diff, review threads, and checks.

### Current state

- Foundation v1 is Locked and GREEN.
- D-024 is merged and canonical.
- D-025 is `Approved — Implementing`, not `Locked`.
- D-026 is Locked and machine-enforced.
- Draft PR #3 is open, Draft, and unmerged.
- Parts 1–11 baseline, Part 12 validation architecture, Part 13 documentation/catalog/design-tool architecture, and Part 14 governance/contribution/change-lifecycle architecture are canonical.

### Exact continuation point

Start immediately with:

**Part 16 — Canonical Specification Index and Implementation Package Plan.**

Then continue with the canonical specification index, implementation package planning, completeness audit, validator design, GREEN evidence, and Owner review. Merge and lock remain separate explicit decisions.

<!-- END: MENQ_STANDARD_NEXT_CHAT_HANDOFF -->