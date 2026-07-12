# MenQ Design Platform — Project Context / MenQ Design Platform — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Active architecture implementation / Գործող architecture implementation  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** MenQ Owner  
**Parent architecture:** [`../D-024-PLATFORMS-ARCHITECTURE-V1.md`](../D-024-PLATFORMS-ARCHITECTURE-V1.md)  
**Current decision:** [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md)  
**Approved baseline:** [`DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`](DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md)

## Հայերեն

### Նպատակ

MenQ Design Platform-ը ամբողջ MenQ ecosystem-ի reusable design capability system-ն է։ Այն ապահովում է shared architecture, contracts, tokens, primitives, components, patterns, assets, tooling, delivery, adoption և validation՝ առանց product-specific identity, business logic կամ domain workflow shared core տեղափոխելու։

### Ընթացիկ վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 Platforms Architecture v1 — merged և canonical։
- D-025 — `Approved — Implementing`, ոչ `Locked`։
- Working branch — `d-025-design-platform-architecture-v1`։
- Draft PR — `#3`, merge չի արվում մինչև completeness, synchronization, validation և Owner approval։
- Parts 1–11 baseline-ը պահպանված է `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`-ում։
- Part 12 validation/CI/conformance/quality-gates architecture-ը canonical է։
- Part 13 documentation portal/component catalog/design-tool integration architecture-ը canonical է։
- Part 14 governance/contribution/ownership/change-request lifecycle architecture-ը canonical է։

### Հաստատված համակարգի սահման

```text
MenQ Foundation
    ↓
MenQ Brand Core
    ↓
MenQ Design Platform Core
    ↓
Product Design Layers
```

Product layer-ը կարող է consume, compose, theme և contract-ով extend անել Platform-ը, բայց չի կարող silently mutate կամ fork անել shared core-ը։

### Canonical dependency model

Reference → Semantic → Component → Pattern → Product Extension։ Theme, state, density, platform, viewport/container, locale/script, accessibility և motion preference-ը orthogonal resolution dimensions են, ոչ token layers։ Controlled exceptions-ը governed temporary bypass են, ոչ normal dependency layer։

### Հաստատված architecture scope

Architecture scope-ը ներառում է token source/build pipeline, primitives, behavior-first components, reusable patterns, themes/modes/product expression separation, accessibility, Armenian + English canonical localization, on-demand locale packs, content, governed assets, motion, package/release/versioning/migration/compatibility, յոթ sequential validation gates, conformance/evidence/exception contracts, documentation portal, behavior-first catalog, governed design-tool mapping, authority model, ownership registry, contribution classes և change-request lifecycle։

### Պարտադիր կանոններ

- Human Owner-ը final authority-ն է։
- Shared core-ը product-neutral է։
- Armenian և English canonical languages են՝ semantic equality-ով։
- Accessibility-ը release condition է։
- Generated outputs-ը source of truth չեն։
- Portal, catalog և design-tool libraries-ը նույն canonical repository source-ի governed views են։
- Unowned canonical asset-ը RED governance defect է։
- High-risk կամ breaking change-ի self-approval-ը արգելված է։
- Merge-ը առանձին authority action է, ոչ GREEN CI-ի ավտոմատ հետևանք։
- Raw source copy/fork-ը standard adoption model չէ։
- Detailed systems-ը առանձին canonical specifications են, D-025-ը architecture boundary-ն է։
- Յուրաքանչյուր write ենթարկվում է Canonical Write Integrity Law-ին։

### Հաջորդ հստակ աշխատանք

1. Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan։
2. Canonical specification index և implementation package plan։
3. D-025 completeness audit, validator design և Draft PR #3 review։
4. Canonical synchronization, GREEN evidence և Owner review։

---

## English

### Purpose

The MenQ Design Platform is the reusable design capability system for the entire MenQ ecosystem. It provides shared architecture, contracts, tokens, primitives, components, patterns, assets, tooling, delivery, adoption, and validation without moving product-specific identity, business logic, or domain workflows into the shared core.

### Current state

- Foundation v1 is Locked and GREEN.
- D-024 Platforms Architecture v1 is merged and canonical.
- D-025 is `Approved — Implementing`, not `Locked`.
- Working branch: `d-025-design-platform-architecture-v1`.
- Draft PR: `#3`; it remains unmerged until completeness, synchronization, validation, and Owner approval are complete.
- Parts 1–11 are preserved in `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`.
- Part 12 validation, CI, conformance, and quality-gates architecture is canonical.
- Part 13 documentation portal, component catalog, and design-tool integration architecture is canonical.
- Part 14 governance, contribution, ownership, and change-request lifecycle architecture is canonical.

### Approved system boundary

```text
MenQ Foundation
    ↓
MenQ Brand Core
    ↓
MenQ Design Platform Core
    ↓
Product Design Layers
```

A product layer may consume, compose, theme, and contractually extend the Platform, but may not silently mutate or fork the shared core.

### Canonical dependency model

Reference → Semantic → Component → Pattern → Product Extension. Theme, state, density, platform, viewport/container, locale/script, accessibility, and motion preference are orthogonal resolution dimensions, not token layers. Controlled exceptions are governed temporary bypasses, not a normal dependency layer.

### Approved architecture scope

The architecture covers the token source/build pipeline, primitives, behavior-first components, reusable patterns, theme/mode/product-expression separation, accessibility, Armenian and English canonical localization, on-demand locale packs, content, governed assets, motion, package/release/versioning/migration/compatibility, seven sequential validation gates, conformance/evidence/exception contracts, a documentation portal, behavior-first catalog, governed design-tool mappings, the authority model, ownership registry, contribution classes, and change-request lifecycle.

### Mandatory rules

- The human Owner holds final authority.
- The shared core is product-neutral.
- Armenian and English are canonical languages with semantic equality.
- Accessibility is a release condition.
- Generated outputs are not sources of truth.
- Portal, catalog, and design-tool libraries are governed views of the same repository source.
- An unowned canonical asset is a RED governance defect.
- Self-approval is forbidden for high-risk or breaking changes.
- Merge is a separate authority action, not an automatic consequence of green CI.
- Raw source copying and forking are not the standard adoption model.
- Detailed systems belong in separate canonical specifications; D-025 remains the architecture boundary.
- Every write follows the Canonical Write Integrity Law.

### Exact next work

1. Part 15 — Product Adoption, Maturity Model, and Two-Consumer Validation Plan.
2. Canonical specification index and implementation package plan.
3. D-025 completeness audit, validator design, and Draft PR #3 review.
4. Canonical synchronization, GREEN evidence, and Owner review.

<!-- END: MENQ_DESIGN_PLATFORM_PROJECT_CONTEXT -->