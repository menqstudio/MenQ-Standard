# Platforms / Platform-ներ

**Status / Կարգավիճակ:** Active architecture — D-024 implementing / Գործող architecture — D-024 իրականացվում է  
**Owner / Պատասխանատու:** MenQ Owner

## Purpose / Նպատակ

**HY:** Platforms layer-ը MenQ Standard-ի reusable capability architecture-ն է։ Այն Foundation-ի սկզբունքները վերածում է բազմակի MenQ products-ի և systems-ի համար կիրառելի architecture-ի, contracts-ի, components-ի, tools-ի և validation controls-ի։

**EN:** The Platforms layer is the reusable capability architecture of MenQ Standard. It translates Foundation principles into architecture, contracts, components, tools, and validation controls usable by multiple MenQ products and systems.

## Boundary / Սահման

**HY:** Platform-ը չէ՝

- MenQ Studio product;
- service offering;
- միայն documentation;
- միայն component library;
- Operating Standard;
- product-specific business-logic container։

**EN:** A Platform is not:

- a MenQ Studio product;
- a service offering;
- documentation alone;
- a component library alone;
- an Operating Standard;
- a product-specific business-logic container.

## Canonical direction / Canonical ուղղություն

```text
Foundation
    ↓ constrains
Platforms
    ↓ provide reusable capabilities
MenQ Products / Services
```

**HY:** Operating Standards-ը կարգավորում են, թե ինչպես է աշխատանքը կատարվում Platforms-ի միջով։ Extensions-ը ավելացնում են optional կամ domain-specific capability։

**EN:** Operating Standards govern how work is performed across Platforms. Extensions add optional or domain-specific capability.

## Qualification rule / Որակավորման կանոն

**HY:** Capability-ն կարող է մտնել Platform registry միայն այն դեպքում, երբ այն reusable է, bounded, contracted, human-owned, versioned, validated, Foundation-aligned, adoptable է և իր core-ում զերծ է product-specific business logic-ից։

**EN:** A capability may enter the Platform registry only when it is reusable, bounded, contracted, human-owned, versioned, validated, Foundation-aligned, adoptable, and free of product-specific business logic in its core.

## Registry / Registry

**HY:** Տե՛ս [`PLATFORM_REGISTRY.md`](PLATFORM_REGISTRY.md)-ը։

**EN:** See [`PLATFORM_REGISTRY.md`](PLATFORM_REGISTRY.md).

## Decisions / Որոշումներ

- [`D-024 — Platforms Architecture v1`](D-024-PLATFORMS-ARCHITECTURE-V1.md)

## Active Platforms / Գործող Platform-ներ

- [`Design Platform`](design/README.md) — architecture Locked under D-025; brand expression layer under D-027. / architecture-ը Locked է D-025-ով, brand expression layer-ը՝ D-027-ով։

## Creation rule / Ստեղծման կանոն

**HY:** Դատարկ Platform folders չեն ստեղծվում taxonomy լրացնելու համար։ Նոր Platform-ը պահանջում է իրական reusable capability, named human owner և formal MenQ Decision System approval։

**EN:** Empty Platform folders are not created to complete a taxonomy. A new Platform requires a real reusable capability, a named human owner, and formal approval through the MenQ Decision System.

<!-- END: PLATFORMS_ROOT_README -->