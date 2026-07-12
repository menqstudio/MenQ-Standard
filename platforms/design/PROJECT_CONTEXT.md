# MenQ Design Platform — Project Context / MenQ Design Platform — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Active skeleton / Գործող skeleton  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** MenQ Owner  
**Parent architecture:** [`../D-024-PLATFORMS-ARCHITECTURE-V1.md`](../D-024-PLATFORMS-ARCHITECTURE-V1.md)

## Հայերեն

### Նպատակ

MenQ Design Platform-ը կառուցում է reusable design capability՝ MenQ products-ի և systems-ի համար։ Այն պետք է ապահովի shared foundations, contracts, primitives, components, assets, tooling, adoption guidance և validation՝ առանց product-specific identity-ն կամ logic-ը shared core-ի մեջ տեղափոխելու։

### Ընթացիկ վիճակ

Platform-ը formally opened է `D-024`-ով, բայց detailed architecture-ը դեռ locked չէ։ Այս փուլում միայն canonical skeleton-ը, boundary-ն և հաջորդ աշխատանքների տեղերն են սահմանված։

### Պարտադիր կանոններ

- Foundation-ը սահմանափակում և ուղղորդում է Platform-ը։
- Human Owner-ը final authority-ն է։
- Shared core-ը product-specific business logic չի պարունակում։
- Detailed contracts-ը և implementation standards-ը approval-ից առաջ canonical mandatory ուժ չունեն։
- Յուրաքանչյուր write ենթարկվում է Canonical Write Integrity Law-ին։

### Հաջորդ աշխատանք

1. Ուսումնասիրել Design Platform scope-ը և consumers-ը։
2. Առաջարկել architecture planes և dependency direction։
3. Սահմանել token, component, asset և tooling contracts-ը։
4. Սահմանել adoption, conformance և versioning model-ը։
5. Validate անել առնվազն երկու իրական product/system use case-ով։

## English

### Purpose

MenQ Design Platform builds reusable design capability for MenQ products and systems. It must provide shared foundations, contracts, primitives, components, assets, tooling, adoption guidance, and validation without moving product-specific identity or logic into the shared core.

### Current state

The Platform is formally opened by `D-024`, but its detailed architecture is not yet locked. At this stage, only the canonical skeleton, boundary, and locations for future work are defined.

### Mandatory rules

- Foundation constrains and guides the Platform.
- The human Owner holds final authority.
- The shared core contains no product-specific business logic.
- Detailed contracts and implementation standards have no mandatory canonical authority before approval.
- Every write follows the Canonical Write Integrity Law.

### Next work

1. Explore Design Platform scope and consumers.
2. Propose architecture planes and dependency direction.
3. Define token, component, asset, and tooling contracts.
4. Define adoption, conformance, and versioning models.
5. Validate with at least two real product or system use cases.

<!-- END: MENQ_DESIGN_PLATFORM_PROJECT_CONTEXT -->