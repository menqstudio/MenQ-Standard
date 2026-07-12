# Product Adoption, Maturity Model, and Two-Consumer Validation Plan v1 / Ապրանքի որդեգրման, հասունության մոդելի և երկու սպառողի վավերացման պլան v1

**Status / Կարգավիճակ:** Approved Architecture — Implementing / Հաստատված ճարտարապետություն — Ներդրման փուլ  
**Decision / Որոշում:** `D-025`  
**Scope / Սահման:** MenQ Design Platform  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

### 1. Նպատակ

Այս architecture-ը սահմանում է, թե MenQ Design Platform-ը ինչպես է ընդունվում իրական products-ի կողմից, ինչպես է չափվում adoption maturity-ն և ինչ evidence է պահանջվում առնվազն երկու տարբեր consumer-ի վրա architecture-ը վավերացնելու համար։ Adoption-ը package install չէ․ այն governed contract consumption, operational use, migration readiness և measurable value է։

### 2. Consumer սահմանում

Consumer-ը իրական MenQ product, application, service, internal system կամ governed implementation է, որը՝

- օգտագործում է released կամ explicitly preview-tagged Platform package,
- ունի named Consumer Owner,
- իրական runtime կամ production-like workflow ունի,
- պահպանում է product-local identity և business logic-ը shared core-ից դուրս,
- տալիս է traceable adoption, conformance և migration evidence։

Demo, screenshot-only prototype, copied source fork կամ նույն product-ի երկու theme-ը երկու consumer չեն համարվում։

### 3. Adoption principles

1. **Contract-first:** adoption-ը կատարվում է public APIs, packages և canonical contracts-ով։
2. **No silent fork:** consumer-ը չի copy/mutate անում shared core-ը առանց approved extension կամ exception contract-ի։
3. **Product neutrality:** validation-ը չի դարձնում որևէ consumer Platform-ի canonical reference product։
4. **Evidence over declaration:** «օգտագործում ենք» հայտարարությունը բավարար չէ։
5. **Incremental adoption:** full replacement-ը պարտադիր չէ, եթե bounded adoption scope-ը և debt-ը documented են։
6. **Exit safety:** consumer-ը պետք է կարողանա rollback կամ migrate անել controlled ձևով։

### 4. Adoption lifecycle

```text
Candidate assessment
→ Scope and dependency mapping
→ Owner assignment
→ Integration plan
→ Pilot implementation
→ Conformance validation
→ Consumer acceptance
→ Release or controlled preview
→ Operational observation
→ Maturity review
→ Expand, hold, migrate, or exit
```

Յուրաքանչյուր stage ունի entry criteria, owner, evidence և stop condition։

### 5. Maturity model

#### M0 — Unassessed

Consumer-ը ցանկում է, բայց scope, owner և compatibility չեն գնահատվել։ Սա adoption evidence չէ։

#### M1 — Candidate

Consumer scope-ը, owner-ը, dependencies-ը, risks-ը և expected value-ն documented են։ Integration դեռ չկա։

#### M2 — Pilot

Consumer-ը իրական bounded flow-ում օգտագործում է Platform package կամ preview build։ Public API usage, rollback և known gaps-ը recorded են։

#### M3 — Conformant

Required conformance profile-ը GREEN է։ Accessibility, localization, theme/mode, compatibility և product-extension boundaries-ը verified են։

#### M4 — Operational

Consumer-ը production կամ production-equivalent environment-ում գործարկվում է, ունի monitoring, support owner, release linkage և incident/rollback readiness։

#### M5 — Proven

Consumer-ը առնվազն մեկ meaningful release/migration cycle է անցել, adoption value-ն չափված է, defects/feedback-ը traceable են, և reusable lessons-ը վերադարձվել են Platform governance-ին։

Maturity level-ը ինքնագնահատում չէ։ Այն evidence-backed verdict է և կարող է downgrade լինել drift, unsupported version կամ unresolved exception-ի դեպքում։

### 6. Required consumer record

Յուրաքանչյուր consumer record ներառում է՝

- consumer ID և name,
- Consumer Owner և technical owner,
- product/system purpose,
- adopted package versions,
- adoption scope և excluded scope,
- conformance profile,
- product extensions և exceptions,
- accessibility/localization/content/design-tool impacts,
- integration commit/release references,
- validation results,
- incidents, known gaps և debt,
- rollback/migration plan,
- current maturity level և review date։

### 7. Two-consumer validation rule

D-025-ի architecture-level completeness-ը պահանջում է առնվազն երկու **իրապես տարբեր** consumers։ Նրանք պետք է տարբերվեն առնվազն երեք meaningful dimensions-ով, օրինակ՝

- product purpose կամ domain,
- UI density/interaction complexity,
- runtime/platform,
- localization/content demands,
- accessibility risk,
- data-display կամ workflow patterns,
- release cadence կամ operational constraints։

Նույն codebase-ի երկու branding variant, նույն app-ի երկու page կամ duplicated shell-ը diversity evidence չեն։

### 8. Consumer A և Consumer B validation plan

Յուրաքանչյուր consumer-ի համար պարտադիր է՝

1. named owner և bounded adoption scope,
2. package/version linkage,
3. at least one real end-to-end workflow,
4. public API usage evidence,
5. accessibility և bilingual Armenian/English validation,
6. theme/mode/density/platform matrices ըստ applicable scope-ի,
7. product-extension boundary check,
8. performance և bundle/runtime impact,
9. rollback/migration proof,
10. consumer acceptance record,
11. defects/feedback և Platform response traceability։

Երկու consumers-ի արդյունքները համեմատվում են՝ պարզելու համար, թե shared capability-ն իսկապես reusable է, թե մեկ product-ի accidental abstraction։

### 9. Adoption metrics

Metrics-ը ներառում են՝

- time to first conformant flow,
- public API coverage,
- escaped defects,
- exception count և age,
- migration effort,
- accessibility/localization failures,
- package drift,
- product-local overrides,
- reuse ratio,
- consumer satisfaction,
- release stability և rollback frequency։

Metrics-ը architecture decisions-ի evidence են, ոչ vanity dashboard։

### 10. Failure and stop conditions

Validation-ը RED է, եթե՝

- consumer-ը copied/forked source է օգտագործում որպես primary model,
- shared core-ում product-specific logic է մտցվում,
- owner կամ rollback plan չկա,
- conformance evidence-ը incomplete է,
- երկու consumers-ը meaningful diversity չունեն,
- supported locale/accessibility scope-ը կիսատ է,
- generated output-ը canonical source է ներկայացվում,
- known breaking drift-ը silently accepted է։

### 11. Exit, downgrade և deprecation

Consumer-ը կարող է pause, downgrade, migrate կամ exit անել։ Այդ դեպքում record-ը պահպանում է պատճառը, affected versions-ը, remaining risk-ը, replacement path-ը և closure evidence-ը։ Historical adoption evidence-ը չի ջնջվում։

### 12. Lock gate

Part 15-ը architecture-level complete է, բայց adoption implementation-ը Locked չի դառնում մինչև երկու distinct real consumers-ի առնվազն M3 evidence, առնվազն մեկ consumer-ի M4 operational evidence, cross-consumer findings, remediation records և explicit Owner approval։

---

## English

### 1. Purpose

This architecture defines how real products adopt the MenQ Design Platform, how adoption maturity is measured, and what evidence is required to validate the architecture across at least two distinct consumers. Adoption is not package installation; it is governed contract consumption, operational use, migration readiness, and measurable value.

### 2. Consumer definition

A consumer is a real MenQ product, application, service, internal system, or governed implementation that uses a released or explicitly preview-tagged Platform package, has a named Consumer Owner, runs a real or production-like workflow, keeps product identity and business logic outside shared core, and produces traceable adoption, conformance, and migration evidence.

A demo, screenshot-only prototype, copied-source fork, or two themes of the same product do not count as two consumers.

### 3. Adoption principles

Adoption is contract-first, forbids silent forks, preserves product neutrality, relies on evidence rather than declaration, supports incremental bounded adoption, and requires controlled rollback or migration safety.

### 4. Adoption lifecycle

```text
Candidate assessment
→ Scope and dependency mapping
→ Owner assignment
→ Integration plan
→ Pilot implementation
→ Conformance validation
→ Consumer acceptance
→ Release or controlled preview
→ Operational observation
→ Maturity review
→ Expand, hold, migrate, or exit
```

Every stage has entry criteria, an owner, required evidence, and a stop condition.

### 5. Maturity model

- **M0 — Unassessed:** listed but not evaluated; not adoption evidence.
- **M1 — Candidate:** scope, ownership, dependencies, risk, and expected value are documented.
- **M2 — Pilot:** a real bounded flow uses a Platform package or preview build with public API, rollback, and gap evidence.
- **M3 — Conformant:** the required conformance profile is GREEN, including applicable accessibility, localization, theme/mode, compatibility, and extension-boundary checks.
- **M4 — Operational:** production or production-equivalent use with monitoring, support ownership, release linkage, and incident/rollback readiness.
- **M5 — Proven:** at least one meaningful release or migration cycle has completed, value is measured, defects and feedback are traceable, and reusable lessons return to Platform governance.

Maturity is an evidence-backed verdict, not self-attestation, and may be downgraded for drift, unsupported versions, or unresolved exceptions.

### 6. Required consumer record

Each record identifies the consumer, owners, purpose, package versions, adopted and excluded scope, conformance profile, product extensions, exceptions, cross-cutting impacts, integration references, validation results, incidents, debt, rollback and migration plans, maturity level, and review date.

### 7. Two-consumer validation rule

D-025 architecture completeness requires at least two genuinely distinct consumers differing across at least three meaningful dimensions such as purpose/domain, interaction complexity, runtime/platform, localization demands, accessibility risk, workflow patterns, release cadence, or operational constraints.

Two branding variants, two pages in one application, or duplicated shells do not provide diversity evidence.

### 8. Consumer A and Consumer B validation plan

Each consumer must provide named ownership, bounded scope, package/version linkage, a real end-to-end workflow, public API evidence, Armenian and English validation, applicable theme/mode/density/platform matrices, extension-boundary checks, performance impact, rollback or migration proof, consumer acceptance, and traceable defects and feedback.

The two results are compared to determine whether the shared capability is genuinely reusable rather than an accidental abstraction of one product.

### 9. Adoption metrics

Metrics include time to first conformant flow, public API coverage, escaped defects, exception age, migration effort, accessibility and localization failures, package drift, local overrides, reuse ratio, consumer satisfaction, release stability, and rollback frequency. Metrics serve architecture decisions, not vanity reporting.

### 10. Failure and stop conditions

Validation is RED when copied or forked source is the primary model, product logic enters shared core, ownership or rollback is missing, conformance evidence is incomplete, consumer diversity is insufficient, supported accessibility or locale scope is partial, generated output is treated as canonical, or known breaking drift is silently accepted.

### 11. Exit, downgrade, and deprecation

A consumer may pause, downgrade, migrate, or exit. The record preserves the reason, affected versions, remaining risk, replacement path, and closure evidence. Historical adoption evidence is never deleted.

### 12. Lock gate

Part 15 is architecture-complete, but adoption implementation does not become Locked until two distinct real consumers have at least M3 evidence, at least one consumer has M4 operational evidence, cross-consumer findings and remediation are recorded, and the Owner explicitly approves.

<!-- END: DESIGN_PLATFORM_PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1 -->