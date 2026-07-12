# MenQ Design Platform — Changelog / MenQ Design Platform — Փոփոխությունների պատմություն

## 2026-07-12 — Part 15 product adoption and two-consumer validation architecture

### Հայերեն

- Ավելացվել է `PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`։
- Սահմանվել են M0–M5 maturity levels-ը և երկու genuinely distinct consumers-ի validation rule-ը։
- Continuation point-ը տեղափոխվել է Part 16 — Canonical Specification Index and Implementation Package Plan։

### English

- Added `PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md`.
- Defined M0–M5 maturity levels and the validation rule for two genuinely distinct consumers.
- Advanced the continuation point to Part 16 — Canonical Specification Index and Implementation Package Plan.

## 2026-07-12 — Part 14 governance and change lifecycle architecture

### Հայերեն

- Ավելացվել է `GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md`։
- Սահմանվել են authority model-ը, ownership registry-ն, contribution classes-ը, review/approval matrix-ը և change-request lifecycle-ը։
- Unowned canonical asset-ը սահմանվել է որպես RED governance defect։
- High-risk կամ breaking change-ի self-approval-ը արգելվել է։
- Merge-ը սահմանվել է որպես առանձին authority action, ոչ GREEN CI-ի ավտոմատ հետևանք։
- Emergency path-ը պահպանում է retrospective record, validation, synchronization և unresolved-risk ownership-ը։
- Continuation point-ը տեղափոխվել է Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan։

### English

- Added `GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md`.
- Defined the authority model, ownership registry, contribution classes, review and approval matrix, and change-request lifecycle.
- Defined an unowned canonical asset as a RED governance defect.
- Prohibited self-approval for high-risk or breaking changes.
- Defined merge as a separate authority action rather than an automatic consequence of green CI.
- Preserved retrospective recording, validation, synchronization, and unresolved-risk ownership in the emergency path.
- Advanced the continuation point to Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.

## 2026-07-12 — Part 13 documentation, catalog, and design-tool integration architecture

### Հայերեն

- Ավելացվել է `DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1.md`։
- Documentation portal-ը, component catalog-ը և design-tool integration-ը սահմանվել են որպես նույն canonical repository source-ից կառուցվող governed views, ոչ առանձին truth sources։
- Սահմանվել են bilingual navigation/parity, version/compatibility visibility, behavior-first catalog entries, public-API-only examples, stable canonical IDs, token/component mapping parity և cross-surface drift detection։
- Սահմանվել է synchronization pipeline-ը՝ repository source → schema validation → package generation → documentation extraction → catalog build → design-tool validation → parity report → release evidence։
- Part 13-ը architecture-level complete է, բայց implementation-ը Locked չէ մինչև prototype, mapping proof, validator automation, consumer use և explicit Owner approval։
- Continuation point-ը տեղափոխվել է Part 14 — Governance, Contribution, Ownership, and Change-Request Lifecycle։

### English

- Added `DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1.md`.
- Defined the documentation portal, component catalog, and design-tool integration as governed views generated from the same canonical repository source, not independent sources of truth.
- Defined bilingual navigation/parity, version and compatibility visibility, behavior-first catalog entries, public-API-only examples, stable canonical IDs, token/component mapping parity, and cross-surface drift detection.
- Defined the synchronization pipeline from repository source through schema validation, package generation, documentation extraction, catalog build, design-tool validation, parity reporting, and release evidence.
- Part 13 is architecture-complete, but implementation is not Locked until prototype, mapping proof, validator automation, consumer use, and explicit Owner approval are complete.
- Advanced the continuation point to Part 14 — Governance, Contribution, Ownership, and Change-Request Lifecycle.

## 2026-07-12 — Part 12 validation architecture

### Հայերեն

- Ավելացվել է `VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`։
- Սահմանվել են յոթ sequential gates, GREEN/YELLOW/RED verdict semantics-ը, conformance profiles-ը, exception contract-ը և evidence contract-ը։
- D-025-ը մնում է `Approved — Implementing`, PR #3-ը մնում է Draft և unmerged։

### English

- Added `VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`.
- Defined seven sequential gates, GREEN/YELLOW/RED verdict semantics, conformance profiles, the exception contract, and the evidence contract.
- D-025 remains `Approved — Implementing`; PR #3 remains Draft and unmerged.

## 2026-07-12 — D-025 architecture baseline synchronization

### Հայերեն

- D-025-ը synchronized է Owner-approved Parts 1–11 baseline-ի հետ։
- Four-layer wording-ը փոխարինվել է canonical dependency model-ով՝ Reference → Semantic → Component → Pattern → Product Extension։
- Theme, state, density, platform, viewport/container, locale/script, accessibility, motion preference և product expression-ը սահմանվել են որպես orthogonal dimensions։
- Controlled exceptions-ը սահմանվել են որպես governed temporary bypass, ոչ normal token layer։
- Ավելացվել է canonical token source/build pipeline-ը։
- Հաստատվել են behavior-first component, reusable pattern, theming, accessibility, localization, content, asset, motion, package, release, versioning, migration և compatibility architecture-ները։
- Armenian և English լեզուները հաստատվել են որպես հավասար canonical languages։ Additional languages-ը սահմանվել են որպես on-demand locale packs։
- Ավելացվել են `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md` և Design Platform-specific `NEXT_CHAT_HANDOFF.md`։
- D-025-ը մնում է `Approved — Implementing`, PR #3-ը մնում է Draft և unmerged։

### English

- Synchronized D-025 with the Owner-approved Parts 1–11 baseline.
- Replaced the four-layer wording with the canonical dependency model: Reference → Semantic → Component → Pattern → Product Extension.
- Defined theme, state, density, platform, viewport/container, locale/script, accessibility, motion preference, and product expression as orthogonal dimensions.
- Defined controlled exceptions as governed temporary bypasses, not a normal token layer.
- Added the canonical token source and build pipeline.
- Approved behavior-first component, reusable pattern, theming, accessibility, localization, content, asset, motion, package, release, versioning, migration, and compatibility architecture.
- Confirmed Armenian and English as equal canonical languages and additional languages as on-demand locale packs.
- D-025 remains `Approved — Implementing`; PR #3 remains Draft and unmerged.

## 2026-07-12 — Initial D-025 architecture implementation

### Հայերեն

- Ավելացվել է `D-025 — MenQ Design Platform Architecture v1` decision-ը։
- Սահմանվել է վեց architecture plane՝ Brand Core, Tokens, Primitives, Components, Patterns և Delivery։
- Սահմանվել է product-neutral shared core boundary-ը և controlled product extension direction-ը։
- Architecture review-ից հանվել են logo presentation-ը և project-specific references-ը։

### English

- Added the `D-025 — MenQ Design Platform Architecture v1` decision.
- Defined six architecture planes: Brand Core, Tokens, Primitives, Components, Patterns, and Delivery.
- Defined the product-neutral shared-core boundary and controlled product-extension direction.
- Removed logo presentation and project-specific references from the architecture review.

<!-- END: MENQ_DESIGN_PLATFORM_CHANGELOG -->