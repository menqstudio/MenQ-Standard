# MenQ Design Platform — Project Context / MenQ Design Platform — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Active architecture implementation / Գործող architecture implementation  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** MenQ Owner  
**Parent architecture:** [`../D-024-PLATFORMS-ARCHITECTURE-V1.md`](../D-024-PLATFORMS-ARCHITECTURE-V1.md)  
**Current decision:** [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md)  
**Approved baseline:** [`DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`](DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md)  
**Validation architecture:** [`VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`](VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md)

## Հայերեն

### Նպատակ

MenQ Design Platform-ը ամբողջ MenQ ecosystem-ի reusable design capability system-ն է։ Այն ապահովում է shared architecture, contracts, tokens, primitives, components, patterns, assets, tooling, delivery, adoption և validation՝ առանց product-specific identity, business logic կամ domain workflow shared core տեղափոխելու։

### Ընթացիկ վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 Platforms Architecture v1 — merged և canonical։
- D-025 — `Approved — Implementing`, ոչ `Locked`։
- D-026 session-read enforcement infrastructure — GREEN։
- Working branch — `d-025-design-platform-architecture-v1`։
- Draft PR — `#3`, merge չի արվում մինչև completeness, synchronization, validation, երկու իրական consumer evidence և Owner approval։
- Owner-approved Parts 1–11-ը պահպանված են `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`-ում։
- Part 12 validation/CI/conformance/quality-gates architecture-ը canonical և architecture-complete է։

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

### Token architecture correction

Canonical dependency layers-ը՝ Reference → Semantic → Component → Pattern → Product Extension։ Theme, state, density, platform, viewport/container, locale/script, accessibility և motion preference-ը orthogonal resolution dimensions են, ոչ token layers։ Controlled exceptions-ը governed temporary bypass են, ոչ normal dependency layer։

### Հաստատված baseline scope

Baseline-ը ներառում է token source/build pipeline, primitives, behavior-first components, reusable patterns, themes/modes/product expression separation, accessibility, Armenian + English canonical localization, on-demand locale packs, content architecture, governed assets, motion architecture և package/release/versioning/migration/compatibility architecture։

### Part 12 validation architecture

Part 12-ը սահմանում է յոթ sequential gates՝ Source Integrity, Build Integrity, Contract Conformance, Visual and Interaction Quality, Consumer Conformance, Package and Compatibility, Release Evidence։ GREEN/YELLOW/RED verdict semantics-ը, exception contract-ը, conformance profiles-ը և evidence contract-ը canonical են։

### Պարտադիր կանոններ

- Human Owner-ը final authority-ն է։
- Shared core-ը product-neutral է։
- Armenian և English canonical languages են՝ semantic equality-ով։
- Additional languages-ը on-demand locale packs են։
- Accessibility-ը release condition է։
- Generated outputs-ը source of truth չեն։
- Raw source copy/fork-ը standard adoption model չէ։
- Detailed systems-ը առանձին canonical specifications են, D-025-ը architecture boundary-ն է։
- Tool success-ը GREEN evidence չէ։
- Յուրաքանչյուր write ենթարկվում է Canonical Write Integrity Law-ին։

### Հաջորդ հստակ աշխատանք

1. Documentation portal, component catalog և design-tool integration architecture։
2. Governance, contribution, ownership և change-request lifecycle։
3. Product adoption, maturity model և two-consumer validation plan։
4. Canonical specification index և implementation package plan։
5. D-025 completeness audit, validator implementation և Draft PR #3 review։
6. Canonical synchronization, GREEN evidence և Owner review։

---

## English

### Purpose

The MenQ Design Platform is the reusable design capability system for the entire MenQ ecosystem. It provides shared architecture, contracts, tokens, primitives, components, patterns, assets, tooling, delivery, adoption, and validation without moving product-specific identity, business logic, or domain workflows into the shared core.

### Current state

- Foundation v1 is Locked and GREEN.
- D-024 Platforms Architecture v1 is merged and canonical.
- D-025 is `Approved — Implementing`, not `Locked`.
- D-026 session-read enforcement infrastructure is GREEN.
- Working branch: `d-025-design-platform-architecture-v1`.
- Draft PR: `#3`; it remains unmerged until completeness, synchronization, validation, two real consumer evidence sets, and Owner approval are complete.
- Owner-approved Parts 1–11 are preserved in `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`.
- Part 12 validation/CI/conformance/quality-gates architecture is canonical and architecture-complete.

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

### Token architecture correction

Canonical dependency layers are Reference → Semantic → Component → Pattern → Product Extension. Theme, state, density, platform, viewport/container, locale/script, accessibility, and motion preference are orthogonal resolution dimensions, not token layers. Controlled exceptions are governed temporary bypasses, not a normal dependency layer.

### Approved baseline scope

The baseline covers the token source/build pipeline, primitives, behavior-first components, reusable patterns, themes/modes/product expression separation, accessibility, Armenian and English canonical localization, on-demand locale packs, content architecture, governed assets, motion architecture, and package/release/versioning/migration/compatibility architecture.

### Part 12 validation architecture

Part 12 defines seven sequential gates: Source Integrity, Build Integrity, Contract Conformance, Visual and Interaction Quality, Consumer Conformance, Package and Compatibility, and Release Evidence. GREEN/YELLOW/RED verdict semantics, the exception contract, conformance profiles, and the evidence contract are canonical.

### Mandatory rules

- The human Owner holds final authority.
- The shared core is product-neutral.
- Armenian and English are canonical languages with semantic equality.
- Additional languages are on-demand locale packs.
- Accessibility is a release condition.
- Generated outputs are not sources of truth.
- Raw source copying and forking are not the standard adoption model.
- Detailed systems belong in separate canonical specifications; D-025 remains the architecture boundary.
- Tool success is not GREEN evidence.
- Every write follows the Canonical Write Integrity Law.

### Exact next work

1. Documentation portal, component catalog, and design-tool integration architecture.
2. Governance, contribution, ownership, and change-request lifecycle.
3. Product adoption, maturity model, and two-consumer validation plan.
4. Canonical specification index and implementation package plan.
5. D-025 completeness audit, validator implementation, and Draft PR #3 review.
6. Canonical synchronization, GREEN evidence, and Owner review.

<!-- END: MENQ_DESIGN_PLATFORM_PROJECT_CONTEXT -->