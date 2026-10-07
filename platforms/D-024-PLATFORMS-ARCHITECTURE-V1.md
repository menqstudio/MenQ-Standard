# D-024 — Platforms Architecture v1 / Platforms ճարտարապետություն v1

**Status / Կարգավիճակ:** Locked / Locked  
**Date / Ամսաթիվ:** 2026-07-12  
**Locked / Lock-ի ամսաթիվ:** 2026-10-07  
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

**HY:** Capability-ն որակավորվում է որպես Platform միայն այն դեպքում, երբ բավարարված են բոլոր պարտադիր չափանիշները՝

**EN:** A capability qualifies as a Platform only when all required criteria are satisfied:

1. **Reusable / Վերօգտագործելի** — useful to more than one product or system. / օգտակար է մեկից ավելի product-ի կամ system-ի համար։
2. **Bounded / Սահմանված** — has an explicit scope and exclusions. / ունի explicit scope և exclusions։
3. **Contracted / Contract-ներով** — exposes stable interfaces, rules, or contracts. / տրամադրում է կայուն interfaces, rules կամ contracts։
4. **Owned / Owner-ով** — has a named human owner. / ունի անվանված human owner։
5. **Versioned / Versioned** — changes are traceable and releasable. / փոփոխությունները traceable և releasable են։
6. **Validated / Ստուգվող** — has tests, conformance checks, or equivalent validation. / ունի tests, conformance checks կամ համարժեք validation։
7. **Foundation-aligned / Foundation-ին համապատասխան** — does not contradict locked Foundation rules. / չի հակասում locked Foundation rules-ին։
8. **Adoptable / Կիրառելի** — has a documented adoption model for products or systems. / ունի products-ի կամ systems-ի համար փաստաթղթավորված adoption model։
9. **Core-pure / Core-ը մաքուր** — product-specific business logic does not live in the platform core. / product-specific business logic-ը չի գտնվում platform core-ում։

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

**HY:**

1. **Platforms-ը թողնել անորոշ։** Մերժված է, քանի որ պահպանում է անորոշությունը և ապագա drift-ը։
2. **Յուրաքանչյուր shared library համարել Platform։** Մերժված է, քանի որ ստեղծում է architecture inflation և թույլ ownership։
3. **Միանգամից ստեղծել բոլոր հնարավոր platform folders-ը։** Մերժված է որպես architecture theatre՝ առանց ապացուցված reusable capability-ի։
4. **Platforms-ը տեղադրել MenQ Studio Products-ի տակ։** Մերժված է, քանի որ Platforms-ը MenQ Standard-ի capability architecture է, իսկ products-ը մնում են MenQ Studio-ի outputs։

**EN:**

1. **Keep Platforms undefined.** Rejected because it preserves ambiguity and future drift.
2. **Treat every shared library as a Platform.** Rejected because it creates architecture inflation and weak ownership.
3. **Create all possible platform folders immediately.** Rejected as architecture theatre without proven reusable capability.
4. **Place Platforms under MenQ Studio Products.** Rejected because Platforms are MenQ Standard capability architecture, while products remain MenQ Studio outputs.

## Why this option / Ինչու այս տարբերակը

**HY:** Այս model-ը reusable capability-ն առանձնացնում է product ownership-ից, պահպանում է Foundation → Platform → Product ուղղությունը և կանխում է product-specific logic-ի ներթափանցումը shared core-ի մեջ։ Այն նաև պահանջում է evidence և formal decision յուրաքանչյուր նոր Platform-ի համար։

**EN:** This model separates reusable capability from product ownership, preserves the Foundation → Platform → Product direction, and prevents product-specific logic from entering shared core. It also requires evidence and a formal decision for each new Platform.

## Expected outcome / Սպասվող արդյունք

**HY:**

- Հետևողական platform boundaries ամբողջ MenQ ecosystem-ում։
- Reusable capabilities՝ առանց product coupling-ի։
- Traceable platform ownership, versioning և validation։
- Ոչ մի speculative platform taxonomy կամ դատարկ architecture։

**EN:**

- Consistent platform boundaries across the MenQ ecosystem.
- Reusable capabilities without product coupling.
- Traceable platform ownership, versioning, and validation.
- No speculative platform taxonomy or empty architecture.

## KPI / Success criteria

**HY:**

1. `platforms/` root package-ը առկա է և անցնում է link/content validation։
2. Յուրաքանչյուր գրանցված Platform ունի human owner, charter, boundary, version status և validation path։
3. Ոչ մի Platform core չի պարունակում product-specific business logic։
4. Նոր Platform proposals-ը օգտագործում են MenQ Decision System-ը։
5. Platform-ը mature համարվելուց առաջ առնվազն երկու products կամ systems պետք է կարողանան այն adopt անել, եթե Owner-ը strategic exception չի հաստատում։

**EN:**

1. `platforms/` root package exists and passes link/content validation.
2. Every registered Platform has a human owner, charter, boundary, version status, and validation path.
3. No Platform core contains product-specific business logic.
4. New Platform proposals use the MenQ Decision System.
5. At least two products or systems can adopt a Platform before it is considered mature, unless the Owner approves a strategic exception.

## Risks / Ռիսկեր

**HY:**

- Վաղաժամ abstraction։
- Platform-ի վերածվելը shared files-ի համար աղբանոցի։
- Ownership-ի անորոշություն։
- Product teams-ի կողմից contracts-ի շրջանցում։
- Ավելորդ documentation՝ առանց աշխատող capability-ի։

**EN:**

- Premature abstraction.
- Platform becoming a dumping ground for shared files.
- Ownership ambiguity.
- Product teams bypassing contracts.
- Excess documentation without working capability.

## Mitigations / Կանխարգելում

**HY:**

- Պարտադիր qualification criteria և registry։
- Formal decision trigger նոր Platforms-ի համար։
- Անվանված human owner։
- Adoption և validation պահանջներ։
- Product-specific logic-ի բացառում։
- Պարբերական architecture review։

**EN:**

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

**HY:**

- Locked վիճակում գտնվող Foundation v1։
- MenQ Decision System v1։
- Documentation Standard v1։
- Canonical Write Integrity Law։
- AI Collaboration Standard v1։

**EN:**

- Locked Foundation v1.
- MenQ Decision System v1.
- Documentation Standard v1.
- Canonical Write Integrity Law.
- AI Collaboration Standard v1.

## Implementation owner / Իրականացման owner

**HY:** MenQ Owner՝ MenQ Architect AI-ի աջակցությամբ։

**EN:** MenQ Owner, assisted by MenQ Architect AI.

## Validation method / Validation մեթոդ

**HY:**

- Պարտադիր ֆայլերի առկայության checks։
- Bilingual semantic parity review։
- Internal links-ի verification։
- Decision registry traceability։
- Platform qualification checklist-ի validation։
- GitHub Actions validation մինչև lock-ը։

**EN:**

- Required file existence checks.
- Bilingual semantic parity review.
- Internal link verification.
- Decision registry traceability.
- Platform qualification checklist validation.
- GitHub Actions validation before lock.

## Review trigger / Վերանայման trigger

**HY:**

Վերանայել, երբ տեղի է ունենում հետևյալներից որևէ մեկը՝

- առաջարկվում է երկրորդ Platform;
- առաջին երկու products-ը adopt են անում Design Platform-ը;
- Platform boundary-ն հակասում է Operating Standards-ին կամ Extensions-ին;
- ownership-ը կամ versioning-ը դառնում է անհստակ;
- Foundation-ի էական փոփոխությունն ազդում է Platforms-ի վրա։

**EN:**

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

**HY:**

- Owner approval-ը MenQ Standard project conversation-ում՝ 2026-07-12-ին։
- Locked Foundation և Decision System canonical documentation։
- Foundation v1 GREEN validation evidence։

**EN:**

- Owner approval in the MenQ Standard project conversation on 2026-07-12.
- Locked Foundation and Decision System canonical documentation.
- Foundation v1 GREEN validation evidence.

## Lock condition / Lock-ի պայման

**HY:** Decision-ը `Locked` է դառնում միայն canonical package-ի implementation-ից, CI validation-ից և post-write synchronization verification-ից հետո։

**EN:** The decision becomes `Locked` only after implementation of the canonical package, CI validation, and post-write synchronization verification.

## Lock record / Lock-ի գրառում

**HY:** Lock-ի երեք պայմանները կատարված են՝ (1) canonical package-ը (`platforms/README.md`, `platforms/PROJECT_CONTEXT.md`, `platforms/PLATFORM_REGISTRY.md`, այս decision-ը) implemented և merged է (`8d949f7`); (2) CI validation-ը GREEN է՝ `Platforms Integrity` run [`#279`](https://github.com/menqstudio/MenQ-Standard/actions/runs/37674248750)՝ `main`-ի վրա; (3) post-write synchronization-ը ստուգված է Foundation, Platforms և Markdown inventory validator-ներով։ Owner-ը՝ Գևորգ Օհանյանը, lock-ը հաստատել է project conversation-ում 2026-10-07-ին։ Հետագա փոփոխությունները պահանջում են governed change control և Owner-ի explicit հաստատում։

**EN:** All three lock conditions are met: (1) the canonical package (`platforms/README.md`, `platforms/PROJECT_CONTEXT.md`, `platforms/PLATFORM_REGISTRY.md`, this decision) is implemented and merged (`8d949f7`); (2) CI validation is GREEN: `Platforms Integrity` run [`#279`](https://github.com/menqstudio/MenQ-Standard/actions/runs/37674248750) on `main`; (3) post-write synchronization is verified by the Foundation, Platforms and Markdown inventory validators. The Owner, Gevorg Ohanyan, approved the lock in the project conversation on 2026-10-07. Further changes require governed change control and explicit Owner approval.

<!-- END: D-024-PLATFORMS-ARCHITECTURE-V1 -->