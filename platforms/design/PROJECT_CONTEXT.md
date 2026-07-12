# MenQ Design Platform — Project Context / MenQ Design Platform — Նախագծի կոնտեքստ

**Status / Կարգավիճակ:** Technical and adoption readiness GREEN — Owner authority pending / Տեխնիկական և որդեգրման պատրաստականություն GREEN — Owner լիազորումը սպասման մեջ  
**Document class / Փաստաթղթի դաս:** Informative  
**Owner / Պատասխանատու:** MenQ Owner  
**Parent architecture:** [`../D-024-PLATFORMS-ARCHITECTURE-V1.md`](../D-024-PLATFORMS-ARCHITECTURE-V1.md)  
**Current decision:** [`decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md`](decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md)

## Հայերեն

### Նպատակ

MenQ Design Platform-ը ամբողջ MenQ ecosystem-ի reusable, product-neutral design capability system-ն է՝ contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales, validation, delivery և adoption boundaries-ով։ Product-specific identity, business logic և domain workflow shared core չեն մտնում։

### Ընթացիկ canonical վիճակ

- Foundation v1 — Locked և GREEN։
- D-024 — merged և canonical։
- D-025 — `Approved — Implementing`, ոչ `Locked`։
- D-026 — Locked և machine-enforced։
- Working branch — `d-025-design-platform-architecture-v1`։
- PR #3 — open, Draft և unmerged։
- Parts 1–11 baseline և Parts 12–16 architecture set-ը canonical են։
- Canonical registry, schemas, ownership, dependency graph և 10 package boundaries-ը implemented են։
- Private preview release candidate-ը `0.1.0-next.0` է։
- Deterministic build, checksums, public API diff, compatibility, migration և rollback evidence-ը GREEN են։
- `MenQ Design Catalog` consumer-ը M3/GREEN է։
- `MenQ Release Evidence Console` consumer-ը M4 operational/GREEN է։
- Cross-consumer validation և quality/adoption evidence-ը GREEN են։
- Owner authority pending է ready-for-review, merge և lock գործողությունների համար։

### Canonical dependency model

Reference → Semantic → Component → Pattern → Product Extension։ Theme, state, density, platform, viewport/container, locale/script, accessibility և motion preference-ը orthogonal resolution dimensions են։ Controlled exceptions-ը governed temporary bypass են։

### Evidence

- Readiness record՝ `implementation/release/d-025-readiness-record.json`։
- Release workflow՝ `Design Platform Preview Release Integrity`, run `#12`, conclusion `success`։
- Artifact՝ `8265108086`, digest `sha256:54c736ed590ae521b24c0b0d58878ed72539a66f4edcdf5c1489996f176a8764`։
- Audit՝ `D-025_COMPLETENESS_AUDIT.md`։
- PR review՝ `D-025_DRAFT_PR_REVIEW_RECORD.md`։

### Authority boundary և հաջորդ քայլ

GREEN CI-ն merge կամ lock authorization չէ։ Հաջորդ գործողությունը MenQ Owner-ի explicit որոշումն է՝ նախ ready-for-review/merge, ապա merge-ից և post-merge validation-ից հետո առանձին lock որոշում։ Մինչ այդ D-025-ը մնում է `Approved — Implementing`։

---

## English

### Purpose

The MenQ Design Platform is the reusable, product-neutral design capability system for the MenQ ecosystem, with governed boundaries for contracts, tokens, foundations, primitives, components, patterns, assets, motion, locales, validation, delivery, and adoption. Product identity, business logic, and domain workflows do not enter the shared core.

### Current canonical state

- Foundation v1 is Locked and GREEN.
- D-024 is merged and canonical.
- D-025 is `Approved — Implementing`, not `Locked`.
- D-026 is Locked and machine-enforced.
- Working branch: `d-025-design-platform-architecture-v1`.
- PR #3 is open, Draft, and unmerged.
- The Parts 1–11 baseline and Parts 12–16 architecture set are canonical.
- The canonical registry, schemas, ownership, dependency graph, and ten package boundaries are implemented.
- The private preview release candidate is `0.1.0-next.0`.
- Deterministic build, checksums, public API diff, compatibility, migration, and rollback evidence are GREEN.
- The `MenQ Design Catalog` consumer is M3/GREEN.
- The `MenQ Release Evidence Console` consumer is M4 operational/GREEN.
- Cross-consumer validation and quality/adoption evidence are GREEN.
- Owner authority pending applies to ready-for-review, merge, and lock actions.

### Canonical dependency model

Reference → Semantic → Component → Pattern → Product Extension. Theme, state, density, platform, viewport/container, locale/script, accessibility, and motion preference are orthogonal resolution dimensions. Controlled exceptions are governed temporary bypasses.

### Evidence

- Readiness record: `implementation/release/d-025-readiness-record.json`.
- Release workflow: `Design Platform Preview Release Integrity`, run `#12`, conclusion `success`.
- Artifact: `8265108086`, digest `sha256:54c736ed590ae521b24c0b0d58878ed72539a66f4edcdf5c1489996f176a8764`.
- Audit: `D-025_COMPLETENESS_AUDIT.md`.
- PR review: `D-025_DRAFT_PR_REVIEW_RECORD.md`.

### Authority boundary and next step

GREEN CI is not merge or lock authorization. The next action is an explicit MenQ Owner decision for ready-for-review and merge, followed after merge and post-merge validation by a separate lock decision. Until then, D-025 remains `Approved — Implementing`.

<!-- END: MENQ_DESIGN_PLATFORM_PROJECT_CONTEXT -->
