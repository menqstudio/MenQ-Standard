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
- Draft PR — `#3`, open, Draft և unmerged։
- Parts 1–11 baseline-ը canonical է։
- Parts 12–16 canonical architecture specifications-ը complete են։
- `D-025_COMPLETENESS_AUDIT.md` և `D-025_DRAFT_PR_REVIEW_RECORD.md` canonical են։
- Architecture verdict-ը GREEN է։
- Implementation/lock readiness-ը YELLOW է՝ իրական package և consumer evidence-ի բացակայության պատճառով։
- `scripts/validate_platforms.py`-ը D-025-aware conformance validator է։

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

Architecture scope-ը ներառում է token source/build pipeline, primitives, behavior-first components, reusable patterns, themes/modes/product expression separation, accessibility, Armenian + English canonical localization, content, governed assets, motion, package/release/versioning/migration/compatibility, validation/conformance/evidence/exception contracts, documentation portal, component catalog, design-tool mapping, governance, ownership, change-request lifecycle, adoption maturity, two-consumer validation և canonical specification/package plan։

### Պարտադիր կանոններ

- Human Owner-ը final authority-ն է։
- Shared core-ը product-neutral է։
- Armenian և English canonical languages են՝ semantic equality-ով։
- Accessibility-ը release condition է։
- Generated outputs-ը source of truth չեն։
- Unowned canonical asset-ը RED governance defect է։
- High-risk կամ breaking change-ի self-approval-ը արգելված է։
- Merge-ը առանձին authority action է, ոչ GREEN CI-ի ավտոմատ հետևանք։
- Raw source copy/fork-ը standard adoption model չէ։
- Յուրաքանչյուր write ենթարկվում է Canonical Write Integrity Law-ին։

### Հաջորդ հստակ աշխատանք

1. Implementation Phase A — canonical specification registry, schemas, ownership, dependency graph և package skeleton։
2. Ընտրել երկու distinct real consumer candidates և սահմանել bounded pilot scopes։
3. Պահպանել Architecture GREEN / Implementation YELLOW verdict-ը մինչև իրական implementation և consumer evidence։

---

## English

### Purpose

The MenQ Design Platform is the reusable design capability system for the entire MenQ ecosystem. It provides shared architecture, contracts, tokens, primitives, components, patterns, assets, tooling, delivery, adoption, and validation without moving product-specific identity, business logic, or domain workflows into the shared core.

### Current state

- Foundation v1 is Locked and GREEN.
- D-024 Platforms Architecture v1 is merged and canonical.
- D-025 is `Approved — Implementing`, not `Locked`.
- Working branch: `d-025-design-platform-architecture-v1`.
- Draft PR #3 is open, Draft, and unmerged.
- The Parts 1–11 baseline is canonical.
- Parts 12–16 canonical architecture specifications are complete.
- `D-025_COMPLETENESS_AUDIT.md` and `D-025_DRAFT_PR_REVIEW_RECORD.md` are canonical.
- The architecture verdict is GREEN.
- Implementation and lock readiness remain YELLOW because real package and consumer evidence do not yet exist.
- `scripts/validate_platforms.py` is a D-025-aware conformance validator.

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

Reference → Semantic → Component → Pattern → Product Extension. Theme, state, density, platform, viewport/container, locale/script, accessibility, and motion preference are orthogonal dimensions, not token layers. Controlled exceptions are governed temporary bypasses, not a normal dependency layer.

### Approved architecture scope

The architecture covers token source/build, primitives, behavior-first components, reusable patterns, theme/mode/product expression, accessibility, Armenian and English canonical localization, content, governed assets, motion, package/release/versioning/migration/compatibility, validation and evidence contracts, documentation and catalog surfaces, design-tool mappings, governance, ownership, change-request lifecycle, adoption maturity, two-consumer validation, and the canonical specification/package plan.

### Mandatory rules

- The human Owner holds final authority.
- The shared core is product-neutral.
- Armenian and English are canonical languages with semantic equality.
- Accessibility is a release condition.
- Generated outputs are not sources of truth.
- An unowned canonical asset is a RED governance defect.
- Self-approval is forbidden for high-risk or breaking changes.
- Merge is a separate authority action, not an automatic consequence of green CI.
- Raw source copying and forking are not the standard adoption model.
- Every write follows the Canonical Write Integrity Law.

### Exact next work

1. Implementation Phase A — canonical specification registry, schemas, ownership, dependency graph, and package skeleton.
2. Select two distinct real consumer candidates and define bounded pilot scopes.
3. Preserve Architecture GREEN / Implementation YELLOW until real implementation and consumer evidence exist.

<!-- END: MENQ_DESIGN_PLATFORM_PROJECT_CONTEXT -->
