# D-025 — MenQ Design Platform Architecture v1 / MenQ Design Platform ճարտարապետություն v1

**Status / Կարգավիճակ:** Approved — Implementing / Հաստատված — իրականացվում է  
**Date / Ամսաթիվ:** 2026-07-12  
**Decision class / Որոշման դաս:** `C4 — Foundation or Ecosystem`  
**Risk level / Ռիսկի մակարդակ:** `R2 — Moderate`  
**Owner / Պատասխանատու:** MenQ Owner  
**Proposer / Առաջարկող:** MenQ Architect AI  
**Reviewer / Վերանայող:** MenQ Owner  
**Approver / Հաստատող:** Gevorg Ohanyan, MenQ Owner  
**Scope / Scope:** MenQ Design Platform architecture

## Problem / Խնդիր

**HY:** MenQ Design Platform-ը formally բացված էր `D-024`-ով, բայց detailed architecture-ը, planes-ը, dependency direction-ը, token model-ը, adoption model-ը և validation gates-ը դեռ canonical կերպով սահմանված չէին։ Առանց այդ սահմանների shared design capability-ն կարող էր վերածվել component dump-ի, brand archive-ի կամ մեկ product-ի design grammar-ի։

**EN:** The MenQ Design Platform was formally opened by `D-024`, but its detailed architecture, planes, dependency direction, token model, adoption model, and validation gates were not yet canonically defined. Without those boundaries, shared design capability could degrade into a component dump, a brand archive, or the design grammar of one product.

## Decision / Որոշում

**HY:** MenQ Design Platform-ը կառուցվում է որպես reusable design capability system ամբողջ MenQ ecosystem-ի համար։ Այն ունի վեց architecture plane, չորս token layer, product-neutral shared core, controlled product extension model, versioned delivery և evidence-based validation։ Որևէ product-ի identity-ն, business logic-ը կամ domain-specific UI grammar-ը shared core-ի մաս չէ։

**EN:** The MenQ Design Platform is built as a reusable design capability system for the entire MenQ ecosystem. It has six architecture planes, four token layers, a product-neutral shared core, a controlled product extension model, versioned delivery, and evidence-based validation. No product identity, business logic, or domain-specific UI grammar belongs in the shared core.

## Architecture planes / Architecture planes

1. **Brand Core / Brand Core** — MenQ meaning, canonical marks, core palette, typography direction, and identity contracts.
2. **Tokens / Token-ներ** — primitive, semantic, component, and product-extension token layers.
3. **Primitives / Primitive-ներ** — surfaces, text, icons, focus, layout, spacing, radius, elevation, and motion primitives.
4. **Components / Component-ներ** — reusable UI behavior, states, variants, accessibility, and stable APIs.
5. **Patterns / Pattern-ներ** — reusable interaction and composition patterns such as forms, navigation, feedback, and data display.
6. **Delivery / Delivery** — packages, documentation, tooling, adoption, migration, versioning, and validation.

## Dependency direction / Կախվածությունների ուղղություն

```text
Foundation
    ↓ constrains
MenQ Brand Core
    ↓ informs
Design Platform Tokens
    ↓ compose
Primitives
    ↓ compose
Components
    ↓ compose
Patterns
    ↓ delivered through
Packages, documentation, tooling, and validation
    ↓ adopted and extended by
MenQ product design layers
```

**HY:** Dependency direction-ը միակողմանի է։ Product layer-ը կարող է consume և contract-ով extend անել Platform-ը, բայց չի կարող silently փոխել shared contracts-ը կամ raw source copy/fork-ը դարձնել ստանդարտ adoption model։

**EN:** Dependency direction is one-way. A product layer may consume and contractually extend the Platform, but it may not silently change shared contracts or make raw source copying and forking the standard adoption model.

## Four-layer token model / Չորսաշերտ token model

1. **Primitive tokens** — raw values such as color ramps, spacing, type sizes, radii, and durations.
2. **Semantic tokens** — meaning-based roles such as action, surface, text, border, status, and focus.
3. **Component tokens** — component contract mappings such as button, input, modal, table, or navigation roles.
4. **Product-extension tokens** — approved product customization that depends on semantic and component contracts without mutating them silently.

## Shared core boundary / Shared core սահման

### Included / Ներառված

- MenQ brand contracts;
- token architecture and naming rules;
- primitives and accessible component behavior;
- theming, localization, motion, and asset contracts;
- versioned packages, adoption guidance, migration, and validation.

### Excluded / Չներառված

- product-specific business logic;
- domain workflows;
- one-off page anatomy;
- product-specific visual grammar;
- campaign visuals;
- optional effects treated as mandatory MenQ identity.

## Optional visual expression / Optional visual expression

**HY:** Aurora, HUD, glass, glow, grain, mesh և նման visual families-ը կարող են գոյություն ունենալ որպես optional, versioned expression packages կամ product-local layers։ Դրանք MenQ shared core-ի պարտադիր identity չեն։

**EN:** Aurora, HUD, glass, glow, grain, mesh, and similar visual families may exist as optional, versioned expression packages or product-local layers. They are not mandatory MenQ shared-core identity.

## Component contract / Component contract

**HY:** Shared component-ի առաջնային արժեքը behavior-ն է՝ states, keyboard operation, focus, semantics, accessibility, API stability և compatibility։ Appearance-ը կառուցվում է tokens-ով և թույլատրված extension-ներով։ Card-ը, dashboard-ը կամ որևէ մեկ layout pattern universal page law չեն։

**EN:** The primary value of a shared component is behavior: states, keyboard operation, focus, semantics, accessibility, API stability, and compatibility. Appearance is built through tokens and permitted extensions. Cards, dashboards, or any single layout pattern are not universal page laws.

## Cross-cutting contracts / Համատարած contract-ներ

The following are mandatory across all planes:

- accessibility;
- Armenian and English semantic parity;
- theming;
- purposeful motion and reduced-motion support;
- canonical asset metadata and ownership;
- versioning, compatibility, deprecation, and migration;
- conformance validation.

## Adoption model / Կիրառման model

1. Install or consume a versioned package or canonical asset.
2. Map product themes to semantic contracts.
3. Extend through approved product-extension tokens and product-local patterns.
4. Run automated and human conformance checks.
5. Upgrade through compatibility policy and migration guidance.

## Validation and lock gate / Validation և lock gate

D-025 reaches `Locked` only when all of the following are true:

1. At least two distinct real MenQ products or systems validate adoption, unless the Owner approves a documented strategic exception.
2. Token conformance is demonstrated in the validated scope.
3. Accessibility checks cover keyboard, focus, contrast, semantics, and reduced motion.
4. Armenian and English documentation have semantic parity.
5. Versioned package or equivalent delivery integrity is demonstrated with changelog and migration evidence.
6. Architecture and validation evidence receive explicit human Owner approval.
7. Repository validators and required GitHub Actions checks are GREEN.

## Alternatives considered / Դիտարկված alternatives

1. **Component library only.** Rejected because a Platform also requires contracts, assets, tooling, adoption, migration, and validation.
2. **Single flat token list.** Rejected because it couples raw values, meaning, components, and product customization.
3. **One product as the reference architecture.** Rejected because the Platform must remain ecosystem-level and product-neutral.
4. **Mandatory visual style family.** Rejected because optional expression must not become universal identity law.
5. **Copy-paste delivery.** Rejected because it creates silent forks and untraceable drift.

## Risks / Ռիսկեր

- premature abstraction;
- excessive component inventory before real demand;
- brand and platform boundaries becoming mixed;
- product teams bypassing semantic contracts;
- architecture documentation without working packages;
- optional visual effects becoming mandatory by habit.

## Mitigations / Կանխարգելում

- product-neutral core boundary;
- evidence from multiple consumers;
- layered tokens;
- versioned packages and migration policy;
- conformance checks;
- named human ownership;
- separate controlled specifications for detailed tokens and components.

## Expected outcome / Սպասվող արդյունք

- one reusable design capability architecture for the MenQ ecosystem;
- consistent contracts without forcing identical product expression;
- clean separation between shared core and product layers;
- traceable adoption, versioning, migration, and validation;
- no product-specific logic or identity inside the shared core.

## Implementation owner / Իրականացման owner

MenQ Owner, assisted by MenQ Architect AI.

## Affected canonical files / Ազդվող canonical files

- `DECISION_INDEX.md`
- `README.md`
- `PROJECT_CONTEXT.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `platforms/design/PROJECT_CONTEXT.md`
- `platforms/design/ARCHITECTURE.md`
- `platforms/design/CONTRACTS.md`
- `platforms/design/ROADMAP.md`
- `platforms/design/CHANGELOG.md`
- future specifications, packages, and validation records under `platforms/design/`

## Evidence / Ապացույց

- Owner approval in the MenQ Standard project conversation on 2026-07-12.
- D-024 Platforms Architecture v1.
- MenQ Design Platform visual architecture review approved after removing product-specific references and logo presentation from the architecture review.

## Lock condition / Lock-ի պայման

**HY:** Այս decision-ը approved architecture boundary է, բայց `Locked` չի համարվում մինչև canonical synchronization-ը, implementation package-ը, multi-consumer validation-ը, Owner approval-ը և GREEN automation evidence-ը։

**EN:** This decision is an approved architecture boundary, but it is not `Locked` until canonical synchronization, the implementation package, multi-consumer validation, Owner approval, and GREEN automation evidence are complete.

<!-- END: D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1 -->