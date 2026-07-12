# D-024 — Platforms Architecture v1 / Platforms ճարտարապետություն v1

**Status / Կարգավիճակ:** Approved — Implementing / Հաստատված — իրականացվում է  
**Date / Ամսաթիվ:** 2026-07-12  
**Decision class / Որոշման դաս:** `C4 — Foundation or Ecosystem`  
**Risk level / Ռիսկի մակարդակ:** `R2 — Moderate`  
**Owner / Պատասխանատու:** MenQ Owner  
**Proposer / Առաջարկող:** MenQ Architect AI  
**Reviewer / Վերանայող:** MenQ Owner  
**Approver / Հաստատող:** Gevorg Ohanyan, MenQ Owner  
**Scope / Scope:** MenQ Standard `Platforms` layer

## Problem / Խնդիր

**HY:** MenQ Standard-ի hierarchy-ում `Platforms` layer-ը նշված էր, բայց չուներ canonical սահմանում, boundary, qualification criteria, repository architecture կամ validation model։ Առանց formal architecture-ի reusable capability-ները կարող էին խառնվել products-ի, services-ի, Operating Standards-ի կամ Extensions-ի հետ։

**EN:** The MenQ Standard hierarchy named a `Platforms` layer, but it lacked a canonical definition, boundary, qualification criteria, repository architecture, and validation model. Without a formal architecture, reusable capabilities could be confused with products, services, Operating Standards, or Extensions.

## Decision / Որոշում

**HY:** Platform-ը reusable capability system է, որը Foundation-ի սկզբունքները վերածում է բազմակի MenQ products-ի կամ systems-ի համար կիրառելի architecture-ի, contracts-ի, components-ի, tools-ի և validation controls-ի։ Platform-ը product, service, միայն documentation, միայն component library կամ Operating Standard չէ։

**EN:** A Platform is a reusable capability system that translates Foundation principles into architecture, contracts, components, tools, and validation controls usable by multiple MenQ products or systems. A Platform is not a product, service, documentation-only body, component library alone, or an Operating Standard.

## Canonical relationship / Canonical հարաբերություն

```text
Foundation
    ↓ constrains
Platforms
    ↓ provide reusable capabilities
MenQ Products / Services

Operating Standards
    ↓ govern how work is performed across platforms

Extensions
    ↓ add optional or domain-specific capability
```

## Platform qualification criteria / Platform որակավորման չափանիշներ

A capability qualifies as a Platform only when all required criteria are satisfied:

1. **Reusable / Վերօգտագործելի** — useful to more than one product or system.
2. **Bounded / Սահմանված** — has an explicit scope and exclusions.
3. **Contracted / Contract-ներով** — exposes stable interfaces, rules, or contracts.
4. **Owned / Owner-ով** — has a named human owner.
5. **Versioned / Versioned** — changes are traceable and releasable.
6. **Validated / Ստուգվող** — has tests, conformance checks, or equivalent validation.
7. **Foundation-aligned / Foundation-ին համապատասխան** — does not contradict locked Foundation rules.
8. **Adoptable / Կիրառելի** — has a documented adoption model for products or systems.
9. **Core-pure / Core-ը մաքուր** — product-specific business logic does not live in the platform core.

## Canonical repository architecture / Canonical repository կառուցվածք

```text
platforms/
├── README.md
├── PROJECT_CONTEXT.md
├── PLATFORM_REGISTRY.md
├── D-024-PLATFORMS-ARCHITECTURE-V1.md
│
└── design/
    ├── README.md
    ├── PROJECT_CONTEXT.md
    ├── PLATFORM_CHARTER.md
    ├── ARCHITECTURE.md
    ├── CONTRACTS.md
    ├── ROADMAP.md
    ├── CHANGELOG.md
    ├── decisions/
    ├── specifications/
    ├── packages/
    └── validation/
```

**HY:** Դատարկ platform directories չեն ստեղծվում միայն taxonomy լրացնելու համար։ Նոր Platform-ը բացվում է իրական reusable capability-ի, named owner-ի և formal decision-ի առկայությամբ։

**EN:** Empty platform directories are not created merely to complete a taxonomy. A new Platform is opened only when a real reusable capability, named owner, and formal decision exist.

## First Platform / Առաջին Platform

**HY:** Առաջին formally opened Platform-ը MenQ Design Platform-ն է։ Այս decision-ը բացում է միայն դրա canonical skeleton-ը և governance boundary-ն։ Design Platform-ի մանրամասն architecture-ը, contracts-ը և implementation standards-ը առանձին decisions կամ approved specifications են պահանջում։

**EN:** The first formally opened Platform is the MenQ Design Platform. This decision opens only its canonical skeleton and governance boundary. Detailed Design Platform architecture, contracts, and implementation standards require separate decisions or approved specifications.

## Alternatives considered / Դիտարկված alternatives

1. **Keep Platforms undefined.** Rejected because it preserves ambiguity and future drift.
2. **Treat every shared library as a Platform.** Rejected because it creates architecture inflation and weak ownership.
3. **Create all possible platform folders immediately.** Rejected as architecture theatre without proven reusable capability.
4. **Place Platforms under MenQ Studio Products.** Rejected because Platforms are MenQ Standard capability architecture, while products remain MenQ Studio outputs.

## Why this option / Ինչու այս տարբերակը

**HY:** Այս model-ը reusable capability-ն առանձնացնում է product ownership-ից, պահպանում է Foundation → Platform → Product ուղղությունը և կանխում է product-specific logic-ի ներթափանցումը shared core-ի մեջ։ Այն նաև պահանջում է evidence և formal decision յուրաքանչյուր նոր Platform-ի համար։

**EN:** This model separates reusable capability from product ownership, preserves the Foundation → Platform → Product direction, and prevents product-specific logic from entering shared core. It also requires evidence and a formal decision for each new Platform.

## Expected outcome / Սպասվող արդյունք

- Consistent platform boundaries across the MenQ ecosystem.
- Reusable capabilities without product coupling.
- Traceable platform ownership, versioning, and validation.
- No speculative platform taxonomy or empty architecture.

## KPI / Success criteria

1. `platforms/` root package exists and passes link/content validation.
2. Every registered Platform has a human owner, charter, boundary, version status, and validation path.
3. No Platform core contains product-specific business logic.
4. New Platform proposals use the MenQ Decision System.
5. At least two products or systems can adopt a Platform before it is considered mature, unless the Owner approves a strategic exception.

## Risks / Ռիսկեր

- Premature abstraction.
- Platform becoming a dumping ground for shared files.
- Ownership ambiguity.
- Product teams bypassing contracts.
- Excess documentation without working capability.

## Mitigations / Կանխարգելում

- Mandatory qualification criteria and registry.
- Formal decision trigger for new Platforms.
- Named human owner.
- Adoption and validation requirements.
- Product-specific logic exclusion.
- Periodic architecture review.

## Reversibility / Rollback

**HY:** Structure-ը reversible է մինչև platform contracts-ի լայն adoption-ը։ Rollback-ը կատարվում է decision supersede/retire lifecycle-ով, registry update-ով և affected products-ի migration plan-ով։ Existing history չի ջնջվում։

**EN:** The structure remains reversible until broad adoption of platform contracts. Rollback uses the decision supersede/retire lifecycle, registry updates, and migration plans for affected products. Existing history is never deleted.

## Dependencies / Կախվածություններ

- Locked Foundation v1.
- MenQ Decision System v1.
- Documentation Standard v1.
- Canonical Write Integrity Law.
- AI Collaboration Standard v1.

## Implementation owner / Իրականացման owner

MenQ Owner, assisted by MenQ Architect AI.

## Validation method / Validation մեթոդ

- Required file existence checks.
- Bilingual semantic parity review.
- Internal link verification.
- Decision registry traceability.
- Platform qualification checklist validation.
- GitHub Actions validation before lock.

## Review trigger / Վերանայման trigger

Review when any of the following occurs:

- a second Platform is proposed;
- the first two products adopt the Design Platform;
- a Platform boundary conflicts with Operating Standards or Extensions;
- ownership or versioning becomes unclear;
- a material Foundation change affects Platforms.

## Affected canonical files / Ազդվող canonical files

- `DECISION_INDEX.md`
- `ECOSYSTEM_ARCHITECTURE.md`
- `README.md`
- `PROJECT_CONTEXT.md`
- `AI_WORKING_CONTEXT.md`
- `ROADMAP.md`
- `CHANGELOG.md`
- `NEXT_CHAT_HANDOFF.md`
- `platforms/**`

## Evidence links / Evidence հղումներ

- Owner approval in the MenQ Standard project conversation on 2026-07-12.
- Locked Foundation and Decision System canonical documentation.
- Foundation v1 GREEN validation evidence.

## Lock condition / Lock-ի պայման

**HY:** Decision-ը `Locked` է դառնում միայն canonical package-ի implementation-ից, CI validation-ից և post-write synchronization verification-ից հետո։

**EN:** The decision becomes `Locked` only after implementation of the canonical package, CI validation, and post-write synchronization verification.

<!-- END: D-024-PLATFORMS-ARCHITECTURE-V1 -->