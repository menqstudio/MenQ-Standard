# D-025 — MenQ Design Platform Architecture v1 / MenQ Design Platform ճարտարապետություն v1

**Status / Կարգավիճակ:** Approved — Implementing / Հաստատված — իրականացվում է  
**Date / Ամսաթիվ:** 2026-07-12  
**Decision class / Որոշման դաս:** `C4 — Foundation or Ecosystem`  
**Risk level / Ռիսկի մակարդակ:** `R2 — Moderate`  
**Owner / Պատասխանատու:** MenQ Owner  
**Approver / Հաստատող:** Gevorg Ohanyan, MenQ Owner  
**Scope / Scope:** MenQ Design Platform architecture

## Problem / Խնդիր

**HY:** D-024-ը formally բացել էր MenQ Design Platform-ը, բայց detailed planes-ը, dependency direction-ը, token model-ը, product-extension սահմանները, delivery, migration և validation gates-ը canonical չէին։ Առանց այդ սահմանների shared design capability-ն կարող էր վերածվել component dump-ի, brand archive-ի կամ մեկ product-ի UI grammar-ի։

**EN:** D-024 formally opened the MenQ Design Platform, but its detailed planes, dependency direction, token model, product-extension boundaries, delivery, migration, and validation gates were not canonical. Without those boundaries, shared design capability could degrade into a component dump, brand archive, or the UI grammar of one product.

## Decision / Որոշում

**HY:** MenQ Design Platform-ը ամբողջ MenQ ecosystem-ի reusable design capability system-ն է։ Այն ունի վեց architecture plane, product-neutral shared core, controlled product-extension model, versioned delivery և evidence-based validation։ Product identity-ն, business logic-ը և domain workflow-ը shared core չեն մտնում։

**EN:** The MenQ Design Platform is the reusable design capability system for the entire MenQ ecosystem. It has six architecture planes, a product-neutral shared core, a controlled product-extension model, versioned delivery, and evidence-based validation. Product identity, business logic, and domain workflows do not belong in the shared core.

## Architecture planes / Architecture planes

1. **Brand Core** — MenQ meaning, canonical marks, palette direction, typography direction, and identity contracts.
2. **Tokens** — reference, semantic, component, pattern, and product-extension token concerns.
3. **Primitives** — reusable foundations and low-level UI constructs.
4. **Components** — reusable behavior, states, variants, accessibility, and stable APIs.
5. **Patterns** — reusable interaction and composition contracts.
6. **Delivery** — packages, documentation, tooling, adoption, migration, versioning, and validation.

## Dependency direction / Կախվածությունների ուղղություն

```text
Foundation
    ↓ constrains
MenQ Brand Core
    ↓ informs
Design Platform Core
    ↓ delivered through
Packages, documentation, tooling, and validation
    ↓ adopted and extended by
Product Design Layers
```

Dependency direction-ը միակողմանի է։ Product layer-ը կարող է consume, compose, theme և contract-ով extend անել Platform-ը, բայց չի կարող silently mutate կամ fork անել shared core-ը։

## Token architecture / Token architecture

Canonical dependency layers՝

1. **Reference** — raw canonical values.
2. **Semantic** — meaning-based roles.
3. **Component** — component contract mappings.
4. **Pattern** — reusable composition mappings.
5. **Product Extension** — controlled product-local extension.

Theme, state, density, platform, viewport/container, locale/script, accessibility mode, motion preference և product expression-ը orthogonal resolution dimensions են, ոչ token layers։ Controlled exceptions-ը governed temporary bypass mechanism են, ոչ normal dependency layer։

Canonical token source-ը structured JSON է՝ schema, bilingual descriptions, owner, lifecycle և version metadata-ով։ Generated CSS, TypeScript, design-tool exports և manifests-ը source of truth չեն։

## Approved architecture baseline / Հաստատված architecture baseline

Owner-approved baseline-ը պահպանված է [`../DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`](../DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md)-ում և ներառում է՝

- Foundation → Brand Core → Design Platform Core → Product Design Layers boundary;
- canonical token source/build pipeline;
- primitives and design foundations;
- behavior-first components;
- reusable patterns;
- theme, mode, and product-expression separation;
- accessibility as a release condition;
- Armenian and English as equal canonical languages;
- additional on-demand locale packs;
- content architecture and terminology governance;
- governed assets, icons, illustrations, media, and motion;
- packages, SemVer, compatibility, deprecation, migration, rollback, and release evidence.

## Shared core boundary / Shared core սահման

### Included / Ներառված

- Brand contracts and canonical ownership boundaries;
- token architecture, naming, dependency, and generation rules;
- primitives, components, patterns, and accessibility behavior;
- theming, localization, content, motion, and asset contracts;
- package, adoption, compatibility, migration, validation, and documentation systems.

### Excluded / Չներառված

- product-specific identity and business logic;
- domain workflows and one-off page anatomy;
- product-specific visual grammar and campaign visuals;
- optional effects treated as mandatory MenQ identity;
- silent source copies, forks, or private API access.

## Localization rule / Լոկալիզացիայի կանոն

Armenian and English are equal canonical languages with semantic parity. Additional languages are on-demand locale packs. A locale may be declared supported only when its approved scope is complete, including UI strings, pluralization, formatting, direction, font/script mapping, accessibility labels, validation messages, and fallback behavior.

## Component and pattern rule / Component և pattern կանոն

Shared component-ի առաջնային արժեքը behavior contract-ն է՝ anatomy, slots, states, events, keyboard behavior, focus, semantics, accessibility, token surface, stable API և lifecycle։ Pattern-ը reusable interaction/composition contract է, ոչ product workflow։

## Validation and lock gate / Validation և lock gate

D-025 reaches `Locked` only when all are true:

1. Complete canonical specification set exists and is synchronized.
2. At least one versioned implementation package or equivalent delivery exists.
3. At least two distinct real MenQ consumers validate adoption, unless the Owner approves a documented strategic exception.
4. Token, accessibility, localization, visual, interaction, package, migration, and compatibility checks pass in the approved scope.
5. Armenian and English documentation have semantic parity.
6. Release and migration evidence are recorded.
7. Required validators and GitHub Actions are GREEN.
8. The human Owner explicitly approves lock.

## Alternatives rejected / Մերժված alternatives

- component library only;
- one flat token list;
- theme/state/density modeled as token layers;
- controlled exceptions modeled as a normal layer;
- one product as reference architecture;
- mandatory visual-style family;
- copy-paste delivery and silent forks.

## Risks and mitigations / Ռիսկեր և կանխարգելում

Risks՝ premature abstraction, inventory growth without demand, brand/platform confusion, semantic bypass, documentation without implementation, and optional effects becoming mandatory by habit.

Mitigations՝ product-neutral boundaries, real consumer evidence, explicit token dependency rules, separate specifications, versioned packages, migration policy, conformance gates, named human ownership, and Owner approval.

## Affected canonical files / Ազդվող canonical files

- `AI_WORKING_CONTEXT.md`
- `PROJECT_CONTEXT.md`
- `ROADMAP.md`
- `CHANGELOG.md`
- `NEXT_CHAT_HANDOFF.md`
- `DECISION_INDEX.md`
- `platforms/design/PROJECT_CONTEXT.md`
- `platforms/design/ARCHITECTURE.md`
- `platforms/design/CONTRACTS.md`
- `platforms/design/ROADMAP.md`
- `platforms/design/CHANGELOG.md`
- `platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`
- future detailed specifications, packages, validators, and evidence under `platforms/design/`

## Evidence / Ապացույց

- Owner approval in the MenQ Standard project conversation on 2026-07-12.
- D-024 Platforms Architecture v1.
- Owner approval of architecture workshop Parts 1–11.
- Draft PR #3 remains open and unmerged.

## Lock condition / Lock-ի պայման

**HY:** Այս decision-ը approved architecture boundary է, բայց `Locked` չէ մինչև canonical synchronization-ը, implementation package-ը, multi-consumer validation-ը, migration/release evidence-ը, Owner approval-ը և GREEN automation evidence-ը ամբողջական չլինեն։

**EN:** This decision is an approved architecture boundary, but it is not `Locked` until canonical synchronization, the implementation package, multi-consumer validation, migration and release evidence, Owner approval, and GREEN automation evidence are complete.

<!-- END: D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1 -->