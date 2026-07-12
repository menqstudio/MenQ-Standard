# MenQ Design Platform Contracts / MenQ Design Platform contract-ներ

**Status / Կարգավիճակ:** Approved architecture scope — detailed specifications pending / Հաստատված architecture scope — մանրամասն specifications-ը սպասման մեջ են  
**Decision / Որոշում:** [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md)  
**Detailed baseline / Մանրամասն հիմք:** [`DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md`](DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md)

## Հայերեն

D-025-ի approved contract families-ը՝

1. Brand Core contracts
2. Token source, schema, naming, dependency, generation և lifecycle contracts
3. Primitive contracts
4. Component behavior և public API contracts
5. Pattern composition contracts
6. Theme, mode, density, platform և product-expression contracts
7. Accessibility contracts
8. Armenian/English canonical parity և on-demand locale-pack contracts
9. Content և terminology contracts
10. Asset, icon, illustration, media և provenance contracts
11. Motion, gesture և interaction-feedback contracts
12. Package, public export և dependency contracts
13. Versioning, compatibility, deprecation և migration contracts
14. Documentation, catalog և design-tool synchronization contracts
15. Adoption և product-extension contracts
16. Validation, CI, conformance և release-evidence contracts
17. Governance, ownership, contribution և exception contracts

### Boundary rule

Product-specific business logic, domain workflow, one-off layout կամ product visual grammar shared contract չէ։ Product extension-ը թույլատրվում է միայն documented extension points-ով և չի կարող silently mutate անել shared core-ը։ Controlled exception-ը ժամանակավոր, owner-ով, reason-ով, review/expiry date-ով և replacement plan-ով governed bypass է, ոչ սովորական styling mechanism։

### Language rule

Հայերենն ու English-ը հավասար canonical լեզուներ են։ Այլ լեզուները on-demand locale packs են։ Supported հայտարարված locale-ը իր approved scope-ում կիսատ չի կարող լինել։

### Change rule

Public contract change-ը versioned, traceable, impact-reviewed և migration/changelog evidence-ով է։ Breaking change-ը չի մտնում stable release առանց Owner-approved compatibility decision-ի և consumer validation-ի։

## English

The D-025 approved contract families are:

1. Brand Core contracts
2. Token source, schema, naming, dependency, generation, and lifecycle contracts
3. Primitive contracts
4. Component behavior and public API contracts
5. Pattern composition contracts
6. Theme, mode, density, platform, and product-expression contracts
7. Accessibility contracts
8. Armenian/English canonical parity and on-demand locale-pack contracts
9. Content and terminology contracts
10. Asset, icon, illustration, media, and provenance contracts
11. Motion, gesture, and interaction-feedback contracts
12. Package, public export, and dependency contracts
13. Versioning, compatibility, deprecation, and migration contracts
14. Documentation, catalog, and design-tool synchronization contracts
15. Adoption and product-extension contracts
16. Validation, CI, conformance, and release-evidence contracts
17. Governance, ownership, contribution, and exception contracts

### Boundary rule

Product-specific business logic, domain workflows, one-off layouts, and product visual grammar are not shared contracts. Product extension is allowed only through documented extension points and may not silently mutate the shared core. A controlled exception is a temporary governed bypass with an owner, reason, review or expiry date, and replacement plan; it is not a normal styling mechanism.

### Language rule

Armenian and English are equal canonical languages. Additional languages are on-demand locale packs. A locale declared supported may not be partial within its approved scope.

### Change rule

A public contract change is versioned, traceable, impact-reviewed, and supported by migration and changelog evidence. A breaking change does not enter a stable release without an Owner-approved compatibility decision and consumer validation.

<!-- END: MENQ_DESIGN_PLATFORM_CONTRACTS -->