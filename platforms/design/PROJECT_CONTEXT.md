# MenQ Design Platform — Project Context / MenQ Design Platform — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Active architecture implementation / Գործող architecture implementation  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** MenQ Owner  
**Parent architecture:** [`../D-024-PLATFORMS-ARCHITECTURE-V1.md`](../D-024-PLATFORMS-ARCHITECTURE-V1.md)  
**Current decision:** [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md)

## Հայերեն

### Նպատակ

MenQ Design Platform-ը կառուցում է reusable design capability՝ MenQ products-ի և systems-ի համար։ Այն ապահովում է shared brand contracts, token architecture, primitives, components, patterns, assets, tooling, adoption guidance և validation՝ առանց որևէ product-specific identity, business logic կամ domain-specific UI grammar shared core-ի մեջ տեղափոխելու։

### Ընթացիկ վիճակ

Platform-ը formally opened է `D-024`-ով։ Detailed architecture boundary-ն approved է `D-025`-ով և գտնվում է implementation փուլում։ `D-025`-ը դեռ `Locked` չէ, քանի դեռ canonical synchronization-ը, implementation package-ը, առնվազն երկու տարբեր իրական consumer validation-ը, Owner approval-ը և GREEN automation evidence-ը ամբողջական չեն։

### Approved architecture

1. Brand Core
2. Tokens
3. Primitives
4. Components
5. Patterns
6. Delivery

Token model-ը չորսաշերտ է՝ primitive, semantic, component և product-extension։ Dependency direction-ը միակողմանի է՝ Foundation-ից դեպի shared Platform, հետո դեպի product design layers։ Product layer-ը կարող է consume և contract-ով extend անել Platform-ը, բայց չի կարող silently փոխել shared contracts-ը։

### Պարտադիր կանոններ

- Foundation-ը սահմանափակում և ուղղորդում է Platform-ը։
- Human Owner-ը final authority-ն է։
- Shared core-ը product-specific identity, business logic կամ domain-specific UI grammar չի պարունակում։
- Logo presentation-ը architecture documentation-ի մաս չէ. canonical brand assets-ը կառավարվում են Brand Core/asset specifications-ով։
- Accessibility, Armenian/English semantic parity, theming, purposeful motion, asset ownership, versioning և conformance validation-ը cross-cutting contracts են։
- Raw source copy/fork-ը standard adoption model չէ։
- Յուրաքանչյուր write ենթարկվում է Canonical Write Integrity Law-ին։

### Հաջորդ աշխատանք

1. Synchronize root և Design Platform canonical documentation-ը `D-025`-ի հետ։
2. Սահմանել detailed token naming և semantic layering specification-ը։
3. Սահմանել primitives և shared component contract-ները։
4. Սահմանել asset, theming, localization, motion և accessibility specifications-ը։
5. Սահմանել package, versioning, migration և conformance validation model-ը։
6. Validate անել առնվազն երկու տարբեր իրական MenQ product/system use case-ով։

## English

### Purpose

MenQ Design Platform builds reusable design capability for MenQ products and systems. It provides shared brand contracts, token architecture, primitives, components, patterns, assets, tooling, adoption guidance, and validation without moving any product-specific identity, business logic, or domain-specific UI grammar into the shared core.

### Current state

The Platform was formally opened by `D-024`. Its detailed architecture boundary is approved by `D-025` and is in implementation. `D-025` is not yet `Locked` until canonical synchronization, the implementation package, validation by at least two distinct real consumers, Owner approval, and GREEN automation evidence are complete.

### Approved architecture

1. Brand Core
2. Tokens
3. Primitives
4. Components
5. Patterns
6. Delivery

The token model has four layers: primitive, semantic, component, and product extension. Dependency direction is one-way from Foundation into the shared Platform and then into product design layers. A product layer may consume and contractually extend the Platform but may not silently change shared contracts.

### Mandatory rules

- Foundation constrains and guides the Platform.
- The human Owner holds final authority.
- The shared core contains no product-specific identity, business logic, or domain-specific UI grammar.
- Logo presentation is not part of architecture documentation; canonical brand assets are governed through Brand Core and asset specifications.
- Accessibility, Armenian/English semantic parity, theming, purposeful motion, asset ownership, versioning, and conformance validation are cross-cutting contracts.
- Raw source copying and forking are not the standard adoption model.
- Every write follows the Canonical Write Integrity Law.

### Next work

1. Synchronize root and Design Platform canonical documentation with `D-025`.
2. Define detailed token naming and semantic layering specifications.
3. Define primitive and shared component contracts.
4. Define asset, theming, localization, motion, and accessibility specifications.
5. Define package, versioning, migration, and conformance validation models.
6. Validate with at least two distinct real MenQ product or system use cases.

<!-- END: MENQ_DESIGN_PLATFORM_PROJECT_CONTEXT -->