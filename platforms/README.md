# Platforms / Platform-ներ

**Status / Կարգավիճակ:** Active architecture — D-024 implementing / Գործող architecture — D-024 իրականացվում է  
**Owner / Պատասխանատու:** MenQ Owner

## Purpose / Նպատակ

**HY:** Platforms layer-ը MenQ Standard-ի reusable capability architecture-ն է։ Այն Foundation-ի սկզբունքները վերածում է բազմակի MenQ products-ի և systems-ի համար կիրառելի architecture-ի, contracts-ի, components-ի, tools-ի և validation controls-ի։

**EN:** The Platforms layer is the reusable capability architecture of MenQ Standard. It translates Foundation principles into architecture, contracts, components, tools, and validation controls usable by multiple MenQ products and systems.

## Boundary / Սահման

A Platform is not:

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

Operating Standards govern how work is performed across Platforms. Extensions add optional or domain-specific capability.

## Qualification rule / Որակավորման կանոն

A capability may enter the Platform registry only when it is reusable, bounded, contracted, human-owned, versioned, validated, Foundation-aligned, adoptable, and free of product-specific business logic in its core.

## Registry / Registry

See [`PLATFORM_REGISTRY.md`](PLATFORM_REGISTRY.md).

## Decisions / Որոշումներ

- [`D-024 — Platforms Architecture v1`](D-024-PLATFORMS-ARCHITECTURE-V1.md)

## Active Platforms / Գործող Platform-ներ

- [`Design Platform`](design/README.md) — formally opened; detailed architecture pending separate approval.

## Creation rule / Ստեղծման կանոն

**HY:** Դատարկ Platform folders չեն ստեղծվում taxonomy լրացնելու համար։ Նոր Platform-ը պահանջում է իրական reusable capability, named human owner և formal MenQ Decision System approval։

**EN:** Empty Platform folders are not created to complete a taxonomy. A new Platform requires a real reusable capability, a named human owner, and formal approval through the MenQ Decision System.

<!-- END: PLATFORMS_ROOT_README -->