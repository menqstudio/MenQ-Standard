# MenQ Design Platform / MenQ դիզայնի հարթակ

**Status / Կարգավիճակ:** Active — Architecture Locked (D-025) / Գործող — architecture-ը Locked է (D-025)  
**Platform owner / Հարթակի պատասխանատու:** MenQ Owner  
**Platform class / Հարթակի դաս:** Reusable ecosystem capability

## Հայերեն

MenQ Design Platform-ը MenQ ecosystem-ի reusable design capability system-ն է։ Այն պետք է Foundation-ի principles-ը վերածի shared design architecture-ի, contracts-ի, tokens-ի, components-ի, assets-ի, tooling-ի և validation controls-ի, որոնք կարող են կիրառվել մեկից ավելի MenQ product-ում կամ system-ում։

**Ինչն է Locked, ինչը՝ ոչ (2026-10-09, `CR-0012`).** Մինչև 2026-10-09-ը այստեղ գրված էր, որ «այս skeleton-ը չի lock անում մանրամասն design architecture, token model, component API կամ implementation stack»։ Դա ճիշտ էր D-024-ի skeleton-ի համար և այլևս ճիշտ չէ. D-025-ը design architecture-ը, ներառյալ token architecture-ը, `Locked` է դարձրել 2026-07-13-ին, իսկ Part 14 governance-ի implementation-ը `Locked` է 2026-10-07-ից։ Locked չեն՝ D-027 brand expression շերտը և նրա կոմպոնենտները (Draft), տասը implementation package-ը (Preview) և repository-ի առաջին էջի ստանդարտը (Draft)։ D-025-ի երկու իրական consumer-ի evidence-ը ուղղվել է 2026-10-07-ին և բաց է։ Բաց կետերը՝ [`NEXT_CHAT_HANDOFF.md`](NEXT_CHAT_HANDOFF.md)-ում։

### Boundary

Design Platform-ը չի պարունակում product-specific screens, business logic կամ մեկ product-ի visual decisions-ը որպես shared core։ Product-specific design-ը ապրում է product layer-ում և կարող է օգտագործել Platform contracts-ը։

### Canonical files

- [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) — ընթացիկ վիճակ
- [`NEXT_CHAT_HANDOFF.md`](NEXT_CHAT_HANDOFF.md) — բաց կետեր և շարունակության կետ
- [`PLATFORM_CHARTER.md`](PLATFORM_CHARTER.md)
- [`ARCHITECTURE.md`](ARCHITECTURE.md)
- [`CONTRACTS.md`](CONTRACTS.md)
- [`ROADMAP.md`](ROADMAP.md)
- [`CHANGELOG.md`](CHANGELOG.md)
- [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md) — D-025 որոշումը (Locked)
- [`DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`](DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md) — Parts 1–11 baseline
- [`VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`](VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md) — Part 12
- [`DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1.md`](DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1.md) — Part 13 (backlog)
- [`GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md`](GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md) — Part 14
- [`PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`](PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md) — Part 15
- [`CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md`](CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md) — Part 16
- [`D-025_LOCK_RECORD.md`](D-025_LOCK_RECORD.md), [`D-025_POST_MERGE_CLOSURE_RECORD.md`](D-025_POST_MERGE_CLOSURE_RECORD.md), [`D-025_FINAL_POST_LOCK_AUDIT.md`](D-025_FINAL_POST_LOCK_AUDIT.md), [`D-025_EVIDENCE_CORRECTION_RECORD.md`](D-025_EVIDENCE_CORRECTION_RECORD.md) — lock-ի, closure-ի, audit-ի և evidence-ի ուղղման գրառումներ
- [`D-025_COMPLETENESS_AUDIT.md`](D-025_COMPLETENESS_AUDIT.md), [`D-025_DRAFT_PR_REVIEW_RECORD.md`](D-025_DRAFT_PR_REVIEW_RECORD.md) — lock-ից առաջ պատմական snapshot-ներ
- [`governance/`](governance/README.md) — Part 14-ի իրականացում՝ ownership, approval matrix, change request-ներ
- [`specifications/design-platform-registry.json`](specifications/design-platform-registry.json) — canonical registry
- [`implementation/`](implementation/) — տասը package, երկու pilot consumer, release գրառումներ
- [`validation/`](validation/) — validator-ներ
- [`decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md`](decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md) — բրենդային արտահայտման շերտ
- [`brand-expression/`](brand-expression/) — MenQ բրենդային թոքեններ, լոգոներ, core կոմպոնենտներ
- [`product-extensions/`](product-extensions/) — արտադրանքային ընդլայնումներ (Բրո)
- [`repository-front/`](repository-front/README.md) — repository-ի առաջին էջի ստանդարտ v1 (Draft, `CR-0011`)

## English

MenQ Design Platform is the reusable design capability system of the MenQ ecosystem. It must translate Foundation principles into shared design architecture, contracts, tokens, components, assets, tooling, and validation controls that can be adopted by more than one MenQ product or system.

**What is Locked and what is not (2026-10-09, `CR-0012`).** Until 2026-10-09 this file said that "this skeleton does not lock detailed design architecture, the token model, component APIs, or an implementation stack". That was true of the D-024 skeleton and is no longer true: D-025 locked the design architecture, including the token architecture, on 2026-07-13, and the Part 14 governance implementation has been `Locked` since 2026-10-07. Not locked: the D-027 brand expression layer and its components (Draft), the ten implementation packages (Preview) and the repository front page standard (Draft). D-025's two-real-consumer evidence was corrected on 2026-10-07 and is open. Open items are in [`NEXT_CHAT_HANDOFF.md`](NEXT_CHAT_HANDOFF.md).

### Boundary

The Design Platform does not place product-specific screens, business logic, or one product's visual decisions into the shared core. Product-specific design lives in the product layer and may adopt Platform contracts.

### Canonical files

- [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) — current state
- [`NEXT_CHAT_HANDOFF.md`](NEXT_CHAT_HANDOFF.md) — open items and the continuation point
- [`PLATFORM_CHARTER.md`](PLATFORM_CHARTER.md)
- [`ARCHITECTURE.md`](ARCHITECTURE.md)
- [`CONTRACTS.md`](CONTRACTS.md)
- [`ROADMAP.md`](ROADMAP.md)
- [`CHANGELOG.md`](CHANGELOG.md)
- [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md) — the D-025 decision (Locked)
- [`DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`](DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md) — Parts 1–11 baseline
- [`VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`](VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md) — Part 12
- [`DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1.md`](DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1.md) — Part 13 (backlog)
- [`GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md`](GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md) — Part 14
- [`PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`](PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md) — Part 15
- [`CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md`](CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md) — Part 16
- [`D-025_LOCK_RECORD.md`](D-025_LOCK_RECORD.md), [`D-025_POST_MERGE_CLOSURE_RECORD.md`](D-025_POST_MERGE_CLOSURE_RECORD.md), [`D-025_FINAL_POST_LOCK_AUDIT.md`](D-025_FINAL_POST_LOCK_AUDIT.md), [`D-025_EVIDENCE_CORRECTION_RECORD.md`](D-025_EVIDENCE_CORRECTION_RECORD.md) — lock, closure, audit and evidence-correction records
- [`D-025_COMPLETENESS_AUDIT.md`](D-025_COMPLETENESS_AUDIT.md), [`D-025_DRAFT_PR_REVIEW_RECORD.md`](D-025_DRAFT_PR_REVIEW_RECORD.md) — historical snapshots from before the lock
- [`governance/`](governance/README.md) — the Part 14 implementation: ownership, approval matrix, change requests
- [`specifications/design-platform-registry.json`](specifications/design-platform-registry.json) — canonical registry
- [`implementation/`](implementation/) — ten packages, two pilot consumers, release records
- [`validation/`](validation/) — validators
- [`decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md`](decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md) — brand expression layer
- [`brand-expression/`](brand-expression/) — MenQ brand tokens, logos, core components
- [`product-extensions/`](product-extensions/) — product extensions (Bro)
- [`repository-front/`](repository-front/README.md) — repository front page standard v1 (Draft, `CR-0011`)

<!-- END: MENQ_DESIGN_PLATFORM_README -->