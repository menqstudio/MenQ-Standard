# Platforms — Project Context / Platforms — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Active / Գործող  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** MenQ Owner  
**Last synchronized / Վերջին համաժամեցում:** 2026-07-12

## Հայերեն

### Նպատակ

`Platforms`-ը MenQ Standard-ի reusable capability layer-ն է։ Այն Foundation-ի պարտադիր սկզբունքները դարձնում է shared architecture, contracts, components, tools և validation controls, որոնք կարող են կիրառվել մեկից ավելի MenQ product-ի կամ system-ի կողմից։

### Canonical սահման

- Platform-ը MenQ Studio product կամ service չէ։
- Platform core-ը product-specific business logic չի պահում։
- Operating Standards-ը սահմանում է՝ ինչպես է աշխատանքը կատարվում Platforms-ի շուրջ։
- Extensions-ը ավելացնում է optional կամ domain-specific capability։
- Նոր Platform-ը բացվում է միայն formal decision-ով և named human owner-ով։

### Ընթացիկ վիճակ

- `D-024` Owner-ի կողմից approved է և implementation/validation փուլում է։
- Առաջին formally opened Platform-ը `Design Platform`-ն է։
- Design Platform-ի մանրամասն architecture-ը դեռ locked չէ և առանձին review/approval է պահանջում։

### Startup workflow

Platforms-ի հետ աշխատանքից առաջ կարդալ root startup set-ը, `platforms/README.md`, `platforms/D-024-PLATFORMS-ARCHITECTURE-V1.md`, `platforms/PLATFORM_REGISTRY.md` և համապատասխան Platform-ի context-ը։

---

## English

### Purpose

`Platforms` is the reusable capability layer of MenQ Standard. It turns mandatory Foundation principles into shared architecture, contracts, components, tools, and validation controls that can be adopted by more than one MenQ product or system.

### Canonical boundary

- A Platform is not a MenQ Studio product or service.
- Platform core does not contain product-specific business logic.
- Operating Standards define how work is performed around Platforms.
- Extensions add optional or domain-specific capability.
- A new Platform is opened only through a formal decision and a named human owner.

### Current state

- `D-024` is Owner-approved and in implementation/validation.
- The first formally opened Platform is the `Design Platform`.
- Detailed Design Platform architecture is not yet locked and requires separate review and approval.

### Startup workflow

Before Platform work, read the root startup set, `platforms/README.md`, `platforms/D-024-PLATFORMS-ARCHITECTURE-V1.md`, `platforms/PLATFORM_REGISTRY.md`, and the context of the relevant Platform.

<!-- END: PLATFORMS_PROJECT_CONTEXT -->