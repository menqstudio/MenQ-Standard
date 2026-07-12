# MenQ Design Platform — Changelog / MenQ Design Platform — Փոփոխությունների պատմություն

## 2026-07-12 — Part 12 validation architecture and D-026 enforcement synchronization

### Հայերեն

- Ավելացվել է `VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`։
- Սահմանվել են յոթ sequential gates՝ Source Integrity, Build Integrity, Contract Conformance, Visual and Interaction Quality, Consumer Conformance, Package and Compatibility, Release Evidence։
- Սահմանվել են GREEN/YELLOW/RED verdict semantics-ը, conformance profiles-ը, exception contract-ը և evidence contract-ը։
- D-026 session-read infrastructure-ը դարձվել է enforceable՝ canonical Markdown inventory, path/size/SHA drift checks և strict GitHub Actions gate-ով։
- Root և Design Platform contexts/roadmaps/handoffs-ը տեղափոխվել են Part 13 continuation point-ի վրա։
- D-025-ը շարունակում է մնալ `Approved — Implementing`, PR #3-ը՝ Draft և unmerged։

### English

- Added `VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md`.
- Defined seven sequential gates: Source Integrity, Build Integrity, Contract Conformance, Visual and Interaction Quality, Consumer Conformance, Package and Compatibility, and Release Evidence.
- Defined GREEN/YELLOW/RED verdict semantics, conformance profiles, the exception contract, and the evidence contract.
- Made D-026 session-read infrastructure enforceable through a canonical Markdown inventory, path/size/SHA drift checks, and a strict GitHub Actions gate.
- Advanced root and Design Platform contexts, roadmaps, and handoffs to the Part 13 continuation point.
- D-025 remains `Approved — Implementing`; PR #3 remains Draft and unmerged.

## 2026-07-12 — D-025 architecture baseline synchronization

### Հայերեն

- D-025-ը synchronized է Owner-approved Parts 1–11 baseline-ի հետ։
- Four-layer wording-ը փոխարինվել է canonical dependency model-ով՝ Reference → Semantic → Component → Pattern → Product Extension։
- Theme, state, density, platform, viewport/container, locale/script, accessibility, motion preference և product expression-ը սահմանվել են որպես orthogonal dimensions։
- Controlled exceptions-ը սահմանվել են որպես governed temporary bypass, ոչ normal token layer։
- Ավելացվել է canonical token source/build pipeline-ը։
- Հաստատվել են behavior-first component, reusable pattern, theming, accessibility, localization, content, asset, motion, package, release, versioning, migration և compatibility architecture-ները։
- Armenian և English լեզուները հաստատվել են որպես հավասար canonical languages։ Additional languages-ը սահմանվել են որպես on-demand locale packs։
- Ավելացվել են `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md` և Design Platform-specific `NEXT_CHAT_HANDOFF.md`։
- D-025-ը մնում է `Approved — Implementing`, PR #3-ը մնում է Draft և unmerged։

### English

- Synchronized D-025 with the Owner-approved Parts 1–11 baseline.
- Replaced the four-layer wording with the canonical dependency model: Reference → Semantic → Component → Pattern → Product Extension.
- Defined theme, state, density, platform, viewport/container, locale/script, accessibility, motion preference, and product expression as orthogonal dimensions.
- Defined controlled exceptions as governed temporary bypasses, not a normal token layer.
- Added the canonical token source and build pipeline.
- Approved behavior-first component, reusable pattern, theming, accessibility, localization, content, asset, motion, package, release, versioning, migration, and compatibility architecture.
- Confirmed Armenian and English as equal canonical languages and additional languages as on-demand locale packs.
- Added `DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md` and the Design Platform-specific `NEXT_CHAT_HANDOFF.md`.
- D-025 remains `Approved — Implementing`; PR #3 remains Draft and unmerged.

## 2026-07-12 — Initial D-025 architecture implementation

### Հայերեն

- Ավելացվել է `D-025 — MenQ Design Platform Architecture v1` decision-ը։
- Սահմանվել է վեց architecture plane՝ Brand Core, Tokens, Primitives, Components, Patterns և Delivery։
- Սահմանվել է product-neutral shared core boundary-ը և controlled product extension direction-ը։
- Architecture review-ից հանվել են logo presentation-ը և project-specific references-ը։

### English

- Added the `D-025 — MenQ Design Platform Architecture v1` decision.
- Defined six architecture planes: Brand Core, Tokens, Primitives, Components, Patterns, and Delivery.
- Defined the product-neutral shared-core boundary and controlled product-extension direction.
- Removed logo presentation and project-specific references from the architecture review.

<!-- END: MENQ_DESIGN_PLATFORM_CHANGELOG -->