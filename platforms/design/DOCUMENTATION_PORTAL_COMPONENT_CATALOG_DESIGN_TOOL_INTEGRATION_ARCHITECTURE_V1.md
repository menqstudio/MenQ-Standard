# Documentation Portal, Component Catalog, and Design-Tool Integration Architecture v1 / Փաստաթղթային պորտալի, բաղադրիչների կատալոգի և դիզայն գործիքի ինտեգրման ճարտարապետություն v1

**Status / Կարգավիճակ:** Approved Architecture — Implementing / Հաստատված ճարտարապետություն — Ներդրման փուլ  
**Decision / Որոշում:** `D-025`  
**Scope / Սահման:** MenQ Design Platform  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

### 1. Նպատակ

Այս architecture-ը սահմանում է, թե MenQ Design Platform-ի canonical contracts-ը ինչպես են դառնում discoverable, testable և synchronized human/AI/design-tool surfaces։ Portal-ը, catalog-ը և design-tool integration-ը երեք առանձին products չեն․ դրանք նույն canonical source-ից կառուցվող երեք governed views են։

### 2. Single-source կանոն

Canonical source-ը repository-ի versioned schemas, specifications, examples և metadata-ն են։ Documentation portal-ը, component catalog-ը, design-tool libraries-ը, code snippets-ը և API references-ը generated consumers են, ոչ source of truth։ Generated surface-ը չի կարող silently override անել repository contract-ը։

### 3. Documentation portal

Portal-ը պետք է տրամադրի՝

- bilingual Armenian/English navigation և semantic parity,
- architecture, contract, token, primitive, component, pattern, asset, motion և release documentation,
- version selector և compatibility visibility,
- status badges՝ Draft, Approved — Implementing, Locked, Deprecated,
- ownership, last validation, package version և migration links,
- searchable terminology և decision traceability,
- runnable examples միայն released կամ explicitly preview-tagged packages-ից։

Portal build-ը fail է անում broken links, missing bilingual pair, stale package reference, unresolved generated drift կամ inaccessible required example-ի դեպքում։

### 4. Component catalog

Catalog-ը behavior-first verification environment է, ոչ միայն visual gallery։ Յուրաքանչյուր entry պարտադիր ունի՝

- anatomy և slots,
- variants, sizes, states և interaction model,
- keyboard/focus/semantics contract,
- accessibility notes և automated results,
- theme, density, platform, locale/script և reduced-motion matrices,
- usage guidance, anti-patterns և migration notes,
- source package/version և canonical specification link։

Catalog stories/examples-ը compile են լինում public APIs-ով։ Private imports, copied internal source կամ product-specific business workflow-ը shared catalog-ում արգելված են։

### 5. Design-tool integration

Design-tool integration-ը source mapping layer է, ոչ parallel design system։ Այն պարտադիր պահպանում է՝

- stable canonical IDs,
- token name/value/type parity,
- component anatomy և variant mapping,
- mode/theme/density/platform separation,
- localization-safe content slots,
- accessibility annotations,
- asset provenance և lifecycle metadata,
- package/spec/version linkage։

Design-tool rename կամ restructuring-ը չի կարող code contract-ը փոխել առանց formal migration և approved decision-ի։ Bidirectional sync-ը թույլատրվում է միայն conflict detection, review և explicit authority rules-ով։

### 6. Synchronization pipeline

```text
Canonical repository source
→ schema validation
→ package generation
→ documentation extraction
→ catalog build
→ design-tool export/import validation
→ cross-surface parity report
→ release evidence
```

Յուրաքանչյուր stage պահպանում է source commit SHA, tool version, generated artifact checksum և verdict։ Cross-surface mismatch-ը RED է, ոչ warning-only։

### 7. Versioning և preview

Stable docs/catalog/design-tool views-ը կապվում են released package version-ին։ `next` կամ preview channel-ը հստակ նշվում է և չի ներկայացվում որպես stable։ Removed կամ deprecated API-ի docs-ը պահվում է migration window-ի ընթացքում։

### 8. Governance

- Platform Maintainer-ը owns portal/catalog pipeline-ը։
- Domain owners-ը owns իրենց specifications և examples-ը։
- Design Tool Maintainer-ը owns mapping/export validation-ը։
- Accessibility owner-ը verifies required matrices-ը։
- MenQ Owner-ը պահում է final architecture և high-risk exception authority-ն։

### 9. Quality gates

Part 13-ը GREEN է միայն երբ՝

1. բոլոր canonical surfaces-ը նույն source/version-ին են հղվում,
2. bilingual parity և link validation-ը pass են,
3. catalog public API-ներով clean build է անում,
4. design-tool mapping drift չկա,
5. accessibility և locale matrices-ը inspectable են,
6. generated output-ը reproducible է,
7. evidence-ը canonical validation record-ում traceable է։

### 10. Lock gate

Part 13-ը architecture-level complete է, բայց implementation-ը Locked չի դառնում մինչև portal/catalog prototype, design-tool mapping proof, validator automation, real consumer use և explicit Owner approval։

---

## English

### 1. Purpose

This architecture defines how canonical MenQ Design Platform contracts become discoverable, testable, and synchronized across human, AI, and design-tool surfaces. The portal, catalog, and design-tool integration are not three independent products; they are three governed views generated from the same canonical source.

### 2. Single-source rule

The canonical source is the repository's versioned schemas, specifications, examples, and metadata. The documentation portal, component catalog, design-tool libraries, code snippets, and API references are generated consumers, not sources of truth. A generated surface may not silently override a repository contract.

### 3. Documentation portal

The portal provides bilingual Armenian/English navigation and semantic parity, architecture and API documentation, version and compatibility visibility, lifecycle status, ownership, validation evidence, migration links, searchable terminology, decision traceability, and examples tied to released or explicitly preview-tagged packages.

The portal build fails on broken links, missing bilingual pairs, stale package references, unresolved generated drift, or inaccessible mandatory examples.

### 4. Component catalog

The catalog is a behavior-first verification environment, not merely a visual gallery. Each entry includes anatomy, slots, variants, sizes, states, interaction behavior, keyboard/focus/semantic contracts, accessibility evidence, theme/density/platform/locale/reduced-motion matrices, usage guidance, anti-patterns, migration notes, and source package/specification links.

Catalog examples compile against public APIs. Private imports, copied internal source, and product-specific business workflows are forbidden in the shared catalog.

### 5. Design-tool integration

Design-tool integration is a source-mapping layer, not a parallel design system. It preserves stable canonical IDs, token parity, component anatomy and variants, orthogonal mode/theme/density/platform dimensions, localization-safe content slots, accessibility annotations, asset provenance, lifecycle metadata, and package/spec/version linkage.

A design-tool rename or restructure may not change a code contract without formal migration and an approved decision. Bidirectional synchronization is allowed only with conflict detection, review, and explicit authority rules.

### 6. Synchronization pipeline

```text
Canonical repository source
→ schema validation
→ package generation
→ documentation extraction
→ catalog build
→ design-tool export/import validation
→ cross-surface parity report
→ release evidence
```

Every stage records the source commit SHA, tool version, artifact checksum, and verdict. A cross-surface mismatch is RED, not warning-only.

### 7. Versioning and preview

Stable portal, catalog, and design-tool views are tied to released package versions. `next` or preview channels are clearly labeled and are not presented as stable. Documentation for removed or deprecated APIs remains available throughout the migration window.

### 8. Governance

The Platform Maintainer owns the portal/catalog pipeline. Domain owners own their specifications and examples. The Design Tool Maintainer owns mapping/export validation. The accessibility owner verifies required matrices. The MenQ Owner retains final architecture and high-risk exception authority.

### 9. Quality gates

Part 13 is GREEN only when all canonical surfaces reference the same source/version, bilingual and link validation pass, the catalog builds against public APIs, design-tool mappings have no drift, accessibility and locale matrices are inspectable, generated output is reproducible, and evidence is traceable in the canonical validation record.

### 10. Lock gate

Part 13 is architecture-complete, but implementation does not become Locked until a portal/catalog prototype, design-tool mapping proof, validator automation, real consumer use, and explicit Owner approval are complete.

<!-- END: DESIGN_PLATFORM_DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1 -->