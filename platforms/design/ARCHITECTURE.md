# MenQ Design Platform Architecture / MenQ Design Platform ճարտարապետություն

**Status / Կարգավիճակ:** Exploring / Ուսումնասիրվում է

## Հայերեն

Detailed architecture-ը դեռ approved կամ locked չէ։ Այս file-ը պահում է ապագա approved architecture-ը և մինչև formal decision-ը mandatory implementation contract չէ։

Ուսումնասիրվող areas՝ foundations, tokens, primitives, components, patterns, assets, tooling, documentation, validation, distribution և product adoption boundaries։

Պարտադիր dependency direction-ը՝

```text
Foundation → Design Platform → Product design layers
```

Product-specific layer-ը կարող է extend անել Platform-ը, բայց չի կարող silently փոխել shared contracts-ը։

## English

Detailed architecture is not yet approved or locked. This file is reserved for future approved architecture and is not a mandatory implementation contract before a formal decision.

Areas to explore include foundations, tokens, primitives, components, patterns, assets, tooling, documentation, validation, distribution, and product adoption boundaries.

Mandatory dependency direction:

```text
Foundation → Design Platform → Product design layers
```

A product-specific layer may extend the Platform but may not silently change shared contracts.

<!-- END: MENQ_DESIGN_PLATFORM_ARCHITECTURE -->