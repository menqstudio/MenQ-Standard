# MenQ Design Platform Architecture / MenQ Design Platform ճարտարապետություն

**Status / Կարգավիճակ:** Locked (D-025, 2026-07-13) / Locked (D-025, 2026-07-13)  
**Decision / Որոշում:** [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md)  
**Detailed baseline / Մանրամասն հիմք:** [`DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`](DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md)

> **Status note / Status-ի նշում (2026-10-09, `CR-0012`):** Այս ֆայլի վերնագիրը ասում է `Locked (D-025, 2026-07-13)`։ Այս ֆայլից սնվող registry գրառումը՝ `menq.design.spec.brand-core.v1`-ը [`specifications/design-platform-registry.json`](specifications/design-platform-registry.json)-ում և `governance/ownership-registry.json`-ում, ունի `Approved — Implementing` lifecycle, մինչդեռ նույն registry-ի top-level `status`-ը `Locked` է։ Երկու արժեքները չեն համընկնում. որն է ճիշտը՝ որոշում է Owner-ը։ Բացի այդ, ներքևի «Lock gate» բաժինը «առնվազն երկու տարբեր իրական consumer validation»-ը նշում է որպես lock-ի պայման. այդ պայմանի evidence-ը ուղղվել է 2026-10-07-ին և բաց է (տես [`D-025_EVIDENCE_CORRECTION_RECORD.md`](D-025_EVIDENCE_CORRECTION_RECORD.md))։ / This file's header says `Locked (D-025, 2026-07-13)`. The registry entry sourced from this file, `menq.design.spec.brand-core.v1` in [`specifications/design-platform-registry.json`](specifications/design-platform-registry.json) and in `governance/ownership-registry.json`, has the lifecycle `Approved — Implementing`, while the same registry's top-level `status` is `Locked`. The two values disagree; which one is right is the Owner's decision. In addition, the "Lock gate" section below names "validation by at least two distinct real consumers" as a lock condition; the evidence for that condition was corrected on 2026-10-07 and is open (see [`D-025_EVIDENCE_CORRECTION_RECORD.md`](D-025_EVIDENCE_CORRECTION_RECORD.md)).

## Հայերեն

### Համակարգի սահմանը

```text
MenQ Foundation
    ↓
MenQ Brand Core
    ↓
MenQ Design Platform Core
    ↓
Product Design Layers
```

MenQ Design Platform-ը ամբողջ MenQ ecosystem-ի reusable design capability system-ն է։ Shared core-ը product-neutral է։ Product layer-ը կարող է consume, compose, theme և documented extension points-ով extend անել Platform-ը, բայց չի կարող silently mutate, fork կամ product business logic տեղափոխել shared core։

### Architecture planes

1. **Brand Core** — MenQ identity և canonical brand contracts։
2. **Tokens** — governed token architecture, schema, generation և resolution dimensions։
3. **Primitives** — color, typography, spacing, sizing, layout, radius, border, elevation, opacity, iconography, focus, motion և z-index foundations։
4. **Components** — reusable behavior, anatomy, states, variants, accessibility և stable APIs։
5. **Patterns** — reusable interaction/composition contracts՝ առանց product workflow պարտադրելու։
6. **Delivery** — packages, documentation, tooling, adoption, migration, versioning, compatibility և validation։

### Token architecture

Token architecture-ը ունի յոթ governed concern, բայց ոչ յոթ նույնատիպ dependency layer։

1. Reference tokens
2. Semantic tokens
3. Theme mapping
4. Component tokens
5. Pattern tokens
6. Product-extension tokens
7. Controlled exceptions — governed temporary bypass, ոչ սովորական layer

Orthogonal dimensions են state, viewport/container, density, platform, locale/script, accessibility mode, motion preference և product expression։ Canonical source-ը structured JSON է։ CSS, TypeScript և design-tool exports-ը generated outputs են, ոչ source of truth։

### Cross-cutting contracts

Accessibility, Armenian/English semantic parity, on-demand locale packs, content clarity, theming, motion/reduced motion, asset provenance, versioning, migration, compatibility և conformance validation-ը պարտադիր են ամբողջ architecture-ի համար։

### Product expression

Theme-ը semantic mapping է։ Mode-ը capability կամ preference dimension է։ Product identity-ն product-local expression է։ Glass, aurora, HUD, glow, grain և նման visual families-ը optional expression packages կամ product-local layers են, ոչ shared identity law։

### Lock gate

D-025-ը `Locked` է 2026-07-13-ից ([`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md))։ Lock-ի պայմաններն էին՝ canonical specification set, implementation package, առնվազն երկու տարբեր իրական consumer validation, bilingual parity, release/migration evidence, Owner approval և GREEN automation։ Հետագա փոփոխությունները ենթարկվում են change-control-ին և Owner-ի explicit հաստատմանը։

## English

### System boundary

```text
MenQ Foundation
    ↓
MenQ Brand Core
    ↓
MenQ Design Platform Core
    ↓
Product Design Layers
```

The MenQ Design Platform is the reusable design capability system for the entire MenQ ecosystem. The shared core is product-neutral. A product layer may consume, compose, theme, and extend the Platform through documented extension points, but it may not silently mutate or fork the core or move product business logic into it.

### Architecture planes

1. **Brand Core** — MenQ identity and canonical brand contracts.
2. **Tokens** — governed token architecture, schema, generation, and resolution dimensions.
3. **Primitives** — color, typography, spacing, sizing, layout, radius, border, elevation, opacity, iconography, focus, motion, and z-index foundations.
4. **Components** — reusable behavior, anatomy, states, variants, accessibility, and stable APIs.
5. **Patterns** — reusable interaction and composition contracts without imposing product workflows.
6. **Delivery** — packages, documentation, tooling, adoption, migration, versioning, compatibility, and validation.

### Token architecture

The token architecture contains seven governed concerns, but not seven identical dependency layers.

1. Reference tokens
2. Semantic tokens
3. Theme mapping
4. Component tokens
5. Pattern tokens
6. Product-extension tokens
7. Controlled exceptions — a governed temporary bypass, not a normal layer

Orthogonal dimensions are state, viewport/container, density, platform, locale/script, accessibility mode, motion preference, and product expression. The canonical source is structured JSON. CSS, TypeScript, and design-tool exports are generated outputs, not sources of truth.

### Cross-cutting contracts

Accessibility, Armenian/English semantic parity, on-demand locale packs, clear content, theming, motion and reduced motion, asset provenance, versioning, migration, compatibility, and conformance validation are mandatory across the architecture.

### Product expression

A theme maps semantics. A mode represents a capability or preference dimension. Product identity is product-local expression. Glass, aurora, HUD, glow, grain, and similar visual families are optional expression packages or product-local layers, not shared identity laws.

### Lock gate

D-025 has been `Locked` since 2026-07-13 ([`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md)). The lock conditions were the canonical specification set, implementation package, validation by at least two distinct real consumers, bilingual parity, release and migration evidence, Owner approval, and GREEN automation. Further changes follow change control and explicit Owner approval.

<!-- END: MENQ_DESIGN_PLATFORM_ARCHITECTURE -->