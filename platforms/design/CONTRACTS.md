# MenQ Design Platform Contracts / MenQ Design Platform contract-ներ

**Status / Կարգավիճակ:** Approved architecture scope — detailed specifications pending / Հաստատված architecture scope — մանրամասն specifications-ը սպասման մեջ են  
**Decision / Որոշում:** [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md)

## Հայերեն

Այս file-ը սահմանում է D-025-ով հաստատված contract families-ը։ Մանրամասն API-ները, token names-ը, component inventories-ը և package schemas-ը առանձին approved specifications են պահանջում։

### Contract families

1. **Brand contracts** — canonical marks, identity usage, palette roles և typography direction։
2. **Token contracts** — primitive, semantic, component և product-extension layering, naming և dependency rules։
3. **Primitive contracts** — surface, text, icon, focus, layout, spacing, radius, elevation և motion roles։
4. **Component contracts** — states, variants, keyboard behavior, focus, semantics, accessibility և stable APIs։
5. **Pattern contracts** — reusable interaction/composition rules՝ առանց universal page anatomy պարտադրելու։
6. **Asset contracts** — source ownership, formats, metadata, versioning և deprecation։
7. **Theming contracts** — dark/light/system mapping և semantic indirection։
8. **Localization contracts** — Armenian/English semantic parity, text expansion և locale-safe presentation։
9. **Motion contracts** — purposeful motion, shared timing/easing և reduced-motion fallback։
10. **Delivery contracts** — versioned packages, documentation, manifests և release evidence։
11. **Adoption contracts** — install, map, extend, validate և upgrade workflow։
12. **Compatibility contracts** — SemVer կամ equivalent versioning, migration և deprecation windows։
13. **Conformance contracts** — automated և human validation gates։

### Boundary rule

Որևէ product-specific business logic, domain workflow, one-off layout կամ product visual grammar shared contract չէ։ Product extension-ը թույլատրվում է միայն documented extension points-ով և չի կարող silently փոխել shared core-ը։

### Change rule

Contract change-ը պետք է լինի versioned, traceable, impact-reviewed և համապատասխան changelog/migration evidence-ով։ Breaking change-ը չի մտնում release առանց Owner-approved compatibility decision-ի։

## English

This file defines the contract families approved by D-025. Detailed APIs, token names, component inventories, and package schemas require separate approved specifications.

### Contract families

1. **Brand contracts** — canonical marks, identity usage, palette roles, and typography direction.
2. **Token contracts** — primitive, semantic, component, and product-extension layering, naming, and dependency rules.
3. **Primitive contracts** — surface, text, icon, focus, layout, spacing, radius, elevation, and motion roles.
4. **Component contracts** — states, variants, keyboard behavior, focus, semantics, accessibility, and stable APIs.
5. **Pattern contracts** — reusable interaction and composition rules without imposing a universal page anatomy.
6. **Asset contracts** — source ownership, formats, metadata, versioning, and deprecation.
7. **Theming contracts** — dark, light, and system mapping through semantic indirection.
8. **Localization contracts** — Armenian and English semantic parity, text expansion, and locale-safe presentation.
9. **Motion contracts** — purposeful motion, shared timing and easing, and reduced-motion fallback.
10. **Delivery contracts** — versioned packages, documentation, manifests, and release evidence.
11. **Adoption contracts** — install, map, extend, validate, and upgrade workflow.
12. **Compatibility contracts** — SemVer or equivalent versioning, migration, and deprecation windows.
13. **Conformance contracts** — automated and human validation gates.

### Boundary rule

No product-specific business logic, domain workflow, one-off layout, or product visual grammar is a shared contract. Product extension is allowed only through documented extension points and may not silently mutate the shared core.

### Change rule

A contract change must be versioned, traceable, impact-reviewed, and supported by changelog and migration evidence. A breaking change does not enter a release without an Owner-approved compatibility decision.

<!-- END: MENQ_DESIGN_PLATFORM_CONTRACTS -->