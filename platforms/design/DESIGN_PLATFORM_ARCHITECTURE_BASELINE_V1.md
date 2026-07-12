# MenQ Design Platform Architecture Baseline v1 / MenQ Design Platform ճարտարապետական հիմք v1

**Status / Կարգավիճակ:** Owner-approved workshop baseline — canonical specification work continues / Owner-ի հաստատած workshop baseline — canonical specification աշխատանքը շարունակվում է  
**Decision / Որոշում:** [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md)  
**Date / Ամսաթիվ:** 2026-07-12

## Հայերեն

### 1. Համակարգի սահմանը

MenQ Design Platform-ը ամբողջ MenQ ecosystem-ի reusable design capability system-ն է։ Հիմնական շղթան է՝

```text
MenQ Foundation
    ↓
MenQ Brand Core
    ↓
MenQ Design Platform Core
    ↓
Product Design Layers
```

- Foundation-ը սահմանում է authority, bilingual parity, accessibility, documentation և validation օրենքները։
- Brand Core-ը սահմանում է MenQ identity-ն և canonical brand assets-ը։
- Design Platform Core-ը սահմանում է shared design infrastructure-ը։
- Product Design Layer-ը կարող է consume, compose, theme և contract-ով extend անել Platform-ը, բայց չի կարող silently mutate կամ fork անել shared core-ը։

### 2. Token architecture

Հաստատված token architecture-ը ունի յոթ governed concern, բայց ոչ յոթ միանման dependency layer։

1. **Reference tokens** — raw design values։
2. **Semantic tokens** — meaning-based roles։
3. **Theme mapping** — semantic role-երի light/dark/high-contrast mapping։
4. **Component tokens** — component contract mappings։
5. **Pattern tokens** — reusable composition mappings։
6. **Product-extension tokens** — controlled product-local extension։
7. **Controlled exceptions** — ժամանակավոր governed bypass mechanism, ոչ սովորական token layer։

Orthogonal dimensions՝ state, viewport/container, density, platform, locale/script, accessibility mode, motion preference և product expression։

Canonical source-ը structured JSON է՝ schema, bilingual descriptions, owner, lifecycle և version metadata-ով։ Generated CSS/TypeScript/design-tool outputs-ը source of truth չեն։ Pipeline-ը կատարում է schema, naming, dependency, cycle, parity, accessibility և stale-output checks։

### 3. Primitives

Primitive architecture-ը ներառում է color, typography, spacing, sizing, layout/grid, radius, border, elevation, opacity, iconography, focus, motion և z-index foundations։ Raw values-ը hardcode չեն արվում consumer code-ում։

### 4. Components

Shared component-ի առաջնային արժեքը behavior contract-ն է՝ anatomy, slots, states, variants, events, keyboard behavior, focus, semantics, accessibility, token surface, stable API և lifecycle։ Native semantics-ը նախընտրելի է։ Product-ը կարող է compose կամ wrap անել documented extension points-ով, բայց չի կարող հասնել private DOM/API կամ հեռացնել accessibility behavior-ը։

### 5. Patterns

Pattern-ը մի քանի primitives/components-ի reusable interaction/composition contract է, ոչ product workflow։ Հաստատված families-ը ներառում են forms, navigation, feedback, data display, search/filter, selection, overlays, onboarding, status/progress և optional application-shell patterns։ Pattern-ը պարտադիր հաշվի է առնում loading, empty, error, partial, stale, offline, permission-limited և responsive states։

### 6. Themes, modes և product expression

Theme-ը semantic mapping է։ Mode-ը capability/preference dimension է։ Product identity-ն product-local expression է։ Optional glass, aurora, HUD, glow, grain և նման families-ը կարող են լինել versioned expression packages, բայց shared identity law չեն։

Accessibility modes-ը combinatorial theme names չեն ստեղծում։ Light/dark, contrast, motion, transparency, density, platform և locale independently resolve են։

### 7. Accessibility, localization և content

Accessibility-ը release condition է՝ keyboard, focus, semantics, screen reader, contrast, zoom/reflow, reduced motion, touch targets և recovery paths։ Target-ը WCAG 2.2 AA-equivalent baseline է, բայց checklist compliance-ը բավարար չէ։

Canonical languages-ը Armenian + English են՝ semantic equality-ով։ Additional languages-ը on-demand locale packs են։ Supported հայտարարված locale-ը իր approved scope-ում կիսատ չի կարող լինել։ Technical fallback chain-ը՝ requested locale → product default → English fallback։

Content-ը interface contract է։ Shared bilingual terminology registry, action naming, error, loading/status և locale-aware formatting rules են պահանջվում։

### 8. Assets և motion

Assets-ը governed resources են՝ owner, purpose, source, provenance/license, lifecycle, formats, accessibility role և variants metadata-ով։ Brand assets-ը Brand Core-ի, shared icons/pipeline-ը Platform-ի, product imagery/characters-ը Product Layer-ի ownership-ն են։

Motion-ը բացատրում է state change-ը և տալիս feedback։ Full/reduced/no-nonessential-motion behavior-ը documented է։ Animation-ը state source չէ, interrupt/reverse/cancel-safe է և performance budget ունի։

### 9. Packages, versioning և release

Հաստատված package direction-ը՝ Tokens → Primitives → Components → Patterns → Product Design Layer → Product Application։ Platform-ը product package չի import անում։ Public API-ն explicit export map է։

Packages-ը SemVer կամ approved equivalent policy են օգտագործում։ Breaking change-ը ներառում է API, token, visual, behavior, accessibility, runtime, locale կամ package incompatibility։ Deprecation-ը replacement, migration window և earliest removal version ունի։ Stable release-ը evidence-backed transaction է՝ compatibility manifest, tests, accessibility, localization, visual regression, consumer validation, migration և Owner approval-ով։

### 10. Lock gate

D-025-ը դեռ `Approved — Implementing` է։ Այն `Locked` է դառնում միայն ամբողջ canonical specification set-ից, implementation package-ից, առնվազն երկու տարբեր real consumer validation-ից, bilingual parity-ից, migration/release evidence-ից, Owner approval-ից և GREEN automation-ից հետո։

### 11. Հաջորդ կտորները

Շարունակել նույն architecture workshop-ը հետևյալ հերթով՝

1. Validation, CI, conformance և quality gates։
2. Documentation portal, catalog և design-tool integration։
3. Governance, contribution, ownership և change-request lifecycle։
4. Product adoption, maturity model և two-consumer validation plan։
5. Canonical specification index և implementation package plan։
6. D-025 completeness audit, validator և Draft PR review։

---

## English

### 1. System boundary

The MenQ Design Platform is the reusable design capability system for the entire MenQ ecosystem. The governing chain is:

```text
MenQ Foundation
    ↓
MenQ Brand Core
    ↓
MenQ Design Platform Core
    ↓
Product Design Layers
```

- Foundation defines authority, bilingual parity, accessibility, documentation, and validation laws.
- Brand Core defines MenQ identity and canonical brand assets.
- Design Platform Core defines shared design infrastructure.
- A Product Design Layer may consume, compose, theme, and contractually extend the Platform, but may not silently mutate or fork the shared core.

### 2. Token architecture

The approved token architecture contains seven governed concerns, but not seven identical dependency layers.

1. **Reference tokens** — raw design values.
2. **Semantic tokens** — meaning-based roles.
3. **Theme mapping** — light, dark, and high-contrast mapping of semantic roles.
4. **Component tokens** — component contract mappings.
5. **Pattern tokens** — reusable composition mappings.
6. **Product-extension tokens** — controlled product-local extension.
7. **Controlled exceptions** — a temporary governed bypass mechanism, not a normal token layer.

Orthogonal dimensions are state, viewport/container, density, platform, locale/script, accessibility mode, motion preference, and product expression.

The canonical source is structured JSON with schema, bilingual descriptions, ownership, lifecycle, and version metadata. Generated CSS, TypeScript, and design-tool outputs are not sources of truth. The pipeline performs schema, naming, dependency, cycle, parity, accessibility, and stale-output checks.

### 3. Primitives

Primitive architecture covers color, typography, spacing, sizing, layout/grid, radius, border, elevation, opacity, iconography, focus, motion, and z-index foundations. Raw values are not hardcoded in consumer code.

### 4. Components

The primary value of a shared component is its behavior contract: anatomy, slots, states, variants, events, keyboard behavior, focus, semantics, accessibility, token surface, stable API, and lifecycle. Native semantics are preferred. A product may compose or wrap documented extension points but may not access private DOM/API or remove accessibility behavior.

### 5. Patterns

A pattern is a reusable interaction/composition contract built from primitives and components, not a product workflow. Approved families include forms, navigation, feedback, data display, search/filter, selection, overlays, onboarding, status/progress, and optional application-shell patterns. Patterns must account for loading, empty, error, partial, stale, offline, permission-limited, and responsive states.

### 6. Themes, modes, and product expression

A theme maps semantics. A mode represents a capability or preference dimension. Product identity is product-local expression. Optional glass, aurora, HUD, glow, grain, and similar families may exist as versioned expression packages but are not shared identity laws.

Accessibility modes do not create combinatorial theme names. Light/dark, contrast, motion, transparency, density, platform, and locale resolve independently.

### 7. Accessibility, localization, and content

Accessibility is a release condition covering keyboard, focus, semantics, screen readers, contrast, zoom/reflow, reduced motion, touch targets, and recovery paths. The target is a WCAG 2.2 AA-equivalent baseline, but checklist compliance alone is insufficient.

Armenian and English are equal canonical languages. Additional languages are on-demand locale packs. A locale declared supported may not be partial within its approved scope. The technical fallback chain is requested locale → product default → English fallback.

Content is part of the interface contract. Shared bilingual terminology, action naming, error, loading/status, and locale-aware formatting rules are required.

### 8. Assets and motion

Assets are governed resources with owner, purpose, source, provenance/license, lifecycle, format, accessibility role, and variant metadata. Brand assets belong to Brand Core; shared icons and the technical pipeline belong to the Platform; product imagery and characters belong to Product Layers.

Motion explains state change and provides feedback. Full, reduced, and no-nonessential-motion behavior is documented. Animation is not the state source, is safe to interrupt/reverse/cancel, and operates within a performance budget.

### 9. Packages, versioning, and release

The approved package direction is Tokens → Primitives → Components → Patterns → Product Design Layer → Product Application. The Platform never imports a product package. Public APIs are explicit export maps.

Packages use SemVer or an approved equivalent policy. Breaking change includes API, token, visual, behavior, accessibility, runtime, locale, or package incompatibility. Deprecation includes a replacement, migration window, and earliest removal version. A stable release is an evidence-backed transaction with a compatibility manifest, tests, accessibility, localization, visual regression, consumer validation, migration, and Owner approval.

### 10. Lock gate

D-025 remains `Approved — Implementing`. It becomes `Locked` only after the full canonical specification set, an implementation package, validation by at least two distinct real consumers, bilingual parity, migration/release evidence, Owner approval, and GREEN automation.

### 11. Next sections

Continue the architecture workshop in this order:

1. Validation, CI, conformance, and quality gates.
2. Documentation portal, catalog, and design-tool integration.
3. Governance, contribution, ownership, and change-request lifecycle.
4. Product adoption, maturity model, and two-consumer validation plan.
5. Canonical specification index and implementation package plan.
6. D-025 completeness audit, validator, and Draft PR review.

<!-- END: MENQ_DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1 -->