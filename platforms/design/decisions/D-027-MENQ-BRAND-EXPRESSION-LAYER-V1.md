# D-027 — MenQ Brand Expression Layer v1 / MenQ բրենդային արտահայտման շերտ v1

**Decision ID:** `D-027`  
**Status / Կարգավիճակ:** Approved — Implementing / Հաստատված — իրականացվում է  
**Date / Ամսաթիվ:** 2026-10-07  
**Decision class / Որոշման դաս:** `C2 — Platform`  
**Risk level / Ռիսկի մակարդակ:** `R2 — Moderate`  
**Owner / Պատասխանատու:** MenQ Owner  
**Proposer / Առաջարկող:** AI collaborator (Claude), after the 2026-10-07 zero-trust audit  
**Reviewer / Վերանայող:** MenQ Owner  
**Approver / Հաստատող:** Gevorg Ohanyan, MenQ Owner — approved in the project conversation on 2026-10-07 («համաձայն եմ»)  
**Scope / Scope:** `platforms/design/brand-expression/`, `platforms/design/product-extensions/`  
**Supersedes / Փոխարինում է:** — (regularises the ungoverned PR #7 package `platforms/design/menq-design-system/`)  
**Superseded by / Փոխարինված է:** —

## Problem / Խնդիր

**HY:** 2026-10-07-ին PR #7-ով `platforms/design/menq-design-system/` փաթեթը մտավ `main`՝ առանց decision-ի, change request-ի, registry entry-ի և bilingual փաստաթղթերի։ Այն ուներ առանձին token համակարգ՝ առանց `menq.design.token.*` ID-ների, ռուսերենը հայտարարում էր հավասար canonical լեզու, canonical copy-ն նշում էր claude.ai artifact-ը, իսկ Բրոյի ինքնությունը և գործակալային կոմպոնենտները դնում էր shared core-ում։ Ոչ մի validator այն չէր ստուգում։

**EN:** On 2026-10-07, PR #7 merged `platforms/design/menq-design-system/` into `main` without a decision, change request, registry entry or bilingual documentation. It carried a separate token system without `menq.design.token.*` IDs, declared Russian an equal canonical language, named a claude.ai artifact as the canonical copy, and placed Bro's identity and agent components in the shared core. No validator checked it.

## Context / Կոնտեքստ

**HY:** D-025-ը (Locked) սահմանում է Design Platform-ի plane-երը, token layer-ները, product boundary-ն և hy/en canonical լեզուները։ MenQ-ի իրական բրենդային արտահայտումը (ազուր/cyan slate-ի վրա, BrandMark) ապրում է `menqstudio/Webpage`-ում, իսկ D-025 token source-ը պարունակում է միայն 8 չեզոք թոքեն։

**EN:** D-025 (Locked) defines the Design Platform planes, token layers, the product boundary and hy/en canonical languages. MenQ's real brand expression (azure/cyan on slate, BrandMark) lives in `menqstudio/Webpage`, while the D-025 token source holds only 8 neutral tokens.

## Decision / Որոշում

**HY:**

1. Փաթեթը վերանվանվում է `platforms/design/brand-expression/` և դառնում է D-025-ի **consumer** բրենդային շերտ (Brand Core plane), ոչ թե D-025 token source-ի փոխարինող։
2. Միակ canonical աղբյուրը `brand-expression/source/brand-tokens.source.json`-ն է՝ `menq.design.token.*` ID-ներով, շերտով, hy/en նկարագրությամբ, owner-ով, lifecycle-ով և light/dark mode-երով։ `tokens.css`-ը և `tokens.json`-ը գեներացվում են և non-canonical են։
3. Shared core-ում մնում են միայն product-neutral կոմպոնենտները։ Բրոյի ինքնությունը, avatar-ը և գործակալային կոմպոնենտները տեղափոխվում են `platforms/design/product-extensions/bro/`։
4. Հայերենը և անգլերենը մնում են միակ canonical լեզուները։ Ռուսերենը locale pack է այն արտադրանքների համար, որոնց պետք է։
5. Canonical աղբյուրը repository-ն է։ Ցանկացած design tool (ներառյալ claude.ai Design System artifact) mirror է։
6. Brand assets-ը (լոգոներ, ֆոնտեր, avatar) ունեն asset record՝ owner, provenance, license, lifecycle, sha256։
7. `validate_brand_expression.py`-ը և առանձին CI workflow-ը ստուգում են schema-ն, generated drift-ը, `var()` resolution-ը, կոմպոնենտների ամբողջականությունը, bilingual README-ները և asset record-ները։

**EN:**

1. The package is renamed `platforms/design/brand-expression/` and becomes a brand layer that **consumes** D-025 (Brand Core plane), not a replacement for the D-025 token source.
2. The only canonical source is `brand-expression/source/brand-tokens.source.json`, with `menq.design.token.*` IDs, layer, hy/en descriptions, owner, lifecycle and light/dark modes. `tokens.css` and `tokens.json` are generated and non-canonical.
3. Only product-neutral components stay in the shared core. Bro's identity, avatar and agent components move to `platforms/design/product-extensions/bro/`.
4. Armenian and English remain the only canonical languages. Russian is a locale pack for products that need it.
5. The repository is the canonical source. Any design tool (including the claude.ai Design System artifact) is a mirror.
6. Brand assets (logos, fonts, avatar) carry asset records: owner, provenance, license, lifecycle, sha256.
7. `validate_brand_expression.py` and a dedicated CI workflow check the schema, generated drift, `var()` resolution, component completeness, bilingual READMEs and asset records.

## Alternatives considered / Դիտարկված այլընտրանքներ

**HY:** (a) Փաթեթը հեռացնել governed tree-ից կամ նշել non-canonical — մերժվեց, քանի որ բրենդը իրական պահանջ է և պետք է պահվի canonical repository-ում։ (b) Բրենդային թոքենները միանգամից գրել D-025 canonical token source-ի մեջ — հետաձգվեց, քանի որ դա կփոխեր Locked D-025 package topology-ն և release evidence-ը առանց consumer evidence-ի։ (c) Ամեն ինչ թողնել shared core-ում — մերժվեց D-025 product boundary-ի պատճառով։

**EN:** (a) Remove the package from the governed tree or mark it non-canonical — rejected, because the brand is a real need and belongs in the canonical repository. (b) Write the brand tokens straight into the D-025 canonical token source — deferred, because it would change the Locked D-025 package topology and release evidence without consumer evidence. (c) Keep everything in the shared core — rejected because of the D-025 product boundary.

## Expected outcome and KPI / Ակնկալվող արդյունք և KPI

**HY:** Բրենդային շերտը governed է, bilingual է, մեքենայորեն ստուգվում է, և առնվազն մեկ իրական consumer (MenQ Webpage) այն օգտագործում է։ KPI՝ `validate_brand_expression.py` GREEN ամեն PR-ում, 0 չսահմանված `var()`, 0 generated drift։

**EN:** The brand layer is governed, bilingual and machine-validated, and at least one real consumer (MenQ Webpage) adopts it. KPI: `validate_brand_expression.py` GREEN on every PR, zero unresolved `var()`, zero generated drift.

## Risks and mitigations / Ռիսկեր և մեղմացում

**HY:** Երկու token համակարգ (D-025 և D-027) կարող են շեղվել → mapping-ը D-027-ի բաց կետ է և պետք է որոշվի նախքան Locked։ Product extension-ները կարող են հետ սողոսկել core → validator-ը արգելում է `bro`/agent կոմպոնենտները core bundle-ում։ Ռուսերենը կարող է կիսատ մնալ → locale pack-ը արտադրանքում պետք է լինի ամբողջական։

**EN:** Two token systems (D-025 and D-027) may drift → the mapping is an open D-027 item that must be decided before Locked. Product extensions may creep back into the core → the validator rejects Bro/agent components in the core bundle. Russian may be partial → where a product ships the ru locale pack, it must be complete.

## Reversibility / Հետշրջելիություն

**HY:** Լիովին հետշրջելի է․ փոփոխությունները ֆայլային են և մեկ PR-ում։ Rollback՝ PR-ի revert։

**EN:** Fully reversible: the changes are file-level and contained in one PR. Rollback: revert the PR.

## Dependencies / Կախվածություններ

`D-025`, `D-026`, Documentation Standard, Decision System.

## Implementation owner and validation / Իրականացում և ստուգում

**HY:** Իրականացնող՝ AI collaborator, Owner-ի հաստատմամբ։ Validation՝ `platforms/design/validation/validate_brand_expression.py`, `.github/workflows/design-brand-expression.yml`, Markdown inventory, Platforms և Foundation validators։

**EN:** Implementation: AI collaborator with Owner approval. Validation: `platforms/design/validation/validate_brand_expression.py`, `.github/workflows/design-brand-expression.yml`, Markdown inventory, Platforms and Foundation validators.

## Review trigger / Վերանայման trigger

**HY:** Առաջին իրական consumer-ի ինտեգրում, D-025 token source-ի հետ mapping-ի որոշում կամ ru locale pack-ի ձևակերպում։

**EN:** The first real consumer integration, the mapping decision with the D-025 token source, or formalising the ru locale pack.

## Affected canonical files / Ազդված canonical ֆայլեր

- `platforms/design/brand-expression/**`
- `platforms/design/product-extensions/**`
- `platforms/design/specifications/design-platform-registry.json`
- `platforms/design/validation/validate_brand_expression.py`
- `.github/workflows/design-brand-expression.yml`
- `DECISION_INDEX.md`, `CHANGELOG.md`, `platforms/design/CHANGELOG.md`, `platforms/design/README.md`

## Evidence / Ապացույց

- Zero-trust audit of `menqstudio/MenQ-Standard` on 2026-10-07 (findings on PR #7).
- Owner approval in the project conversation on 2026-10-07.
- Source repositories: `menqstudio/Webpage@d985a57` (tokens, BrandMark), `menqstudio/BroPS@05754bd` (app components).

<!-- END: D-027-MENQ-BRAND-EXPRESSION-LAYER-V1 -->
