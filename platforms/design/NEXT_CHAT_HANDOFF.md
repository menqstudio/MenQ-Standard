# MenQ Design Platform — Next Chat Handoff / MenQ Design Platform — Հաջորդ chat-ի handoff

**Status / Կարգավիճակ:** Current / Ընթացիկ  
**Prepared / Պատրաստվել է:** 2026-07-12  
**Owner / Պատասխանատու:** Gevorg Ohanyan  
**Repository:** `https://github.com/menqstudio/MenQ-Standard`  
**Working branch:** `d-025-design-platform-architecture-v1`  
**Draft PR:** `https://github.com/menqstudio/MenQ-Standard/pull/3`

## Հայերեն

### Պարտադիր մեկնարկ

Մինչև substantive աշխատանք՝ active branch/ref-ում enumerate և ամբողջությամբ կարդալ repository-ի բոլոր tracked `.md` files-ը՝ ըստ `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`-ի։ Active PR-ի դեպքում կարդալ metadata, changed files, diff, review threads և checks։ Startup subset-ը, այս handoff-ը կամ previous memory-ն complete-read evidence չեն։

### Ընթացիկ վիճակ

- Foundation v1 — GREEN և Locked։
- D-024 Platforms Architecture v1 — merged և canonical։
- D-025 MenQ Design Platform Architecture v1 — `Approved — Implementing`, ոչ `Locked`։
- D-026 Canonical Session Read Law — Locked և machine-enforced։
- Draft PR #3 — open, Draft, unmerged։
- Shared core-ը product-neutral է։ Product identity, business logic և domain workflows shared core չեն մտնում։

### Canonical architecture state

1. Parts 1–11 baseline — `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`։
2. Part 12 — `VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`։
3. Part 13 — `DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1.md`։
4. Part 14 — `GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md`։
5. Canonical dependency model՝ Reference → Semantic → Component → Pattern → Product Extension։
6. Theme, state, density, platform, locale, accessibility և motion preference-ը orthogonal dimensions են, ոչ token layers։
7. Portal, catalog և design-tool integration-ը նույն canonical source-ի governed views են։
8. Unowned canonical asset-ը RED defect է։ High-risk/breaking change-ի self-approval-ը արգելված է։
9. Merge-ը առանձին authority action է, ոչ GREEN CI-ի ավտոմատ հետևանք։

### Շարունակելու ճշգրիտ կետը

Հաջորդ աշխատանքը՝

## Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan

Այնուհետև՝

16. Canonical specification index և implementation package plan։
17. D-025 completeness audit, validator design և Draft PR #3 review։
18. Canonical synchronization և GREEN evidence։
19. Owner review։ Merge և lock-ը առանձին explicit decisions են։

### Արգելված գործողություններ

- PR #3-ը չmerge անել և ready-for-review չդարձնել առանց Owner instruction-ի։
- D-025-ը `Locked` չանվանել։
- Product-specific identity, logic կամ workflows shared core չմտցնել։
- Generated docs/catalog/design-tool library-ը canonical source չհամարել։
- High-risk կամ breaking change-ը self-approve չանել։
- GREEN CI-ն merge approval չհամարել։
- Tool success-ը GREEN evidence չհամարել։

---

## English

### Mandatory startup

Before substantive work, enumerate and completely read every tracked `.md` file on the active branch/ref under `foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md`. For the active PR, read metadata, changed files, diff, review threads, and checks. This handoff or previous memory is not complete-read evidence.

### Current state

- Foundation v1 is GREEN and Locked.
- D-024 Platforms Architecture v1 is merged and canonical.
- D-025 is `Approved — Implementing`, not `Locked`.
- D-026 is Locked and machine-enforced.
- Draft PR #3 is open, Draft, and unmerged.
- Shared core is product-neutral.

### Canonical architecture state

- Parts 1–11: `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`.
- Part 12: `VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`.
- Part 13: `DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1.md`.
- Part 14: `GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md`.
- Canonical dependency model: Reference → Semantic → Component → Pattern → Product Extension.
- The portal, catalog, and design-tool integration are governed views of the same source.
- An unowned canonical asset is a RED defect. Self-approval is prohibited for high-risk and breaking changes.
- Merge is a separate authority action, not an automatic consequence of green CI.

### Exact continuation point

Start immediately with:

**Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.**

Then continue with the canonical specification index and implementation package plan, completeness audit, validator design, synchronization, GREEN evidence, and Owner review. Merge and lock remain separate explicit decisions.

<!-- END: MENQ_DESIGN_PLATFORM_NEXT_CHAT_HANDOFF -->