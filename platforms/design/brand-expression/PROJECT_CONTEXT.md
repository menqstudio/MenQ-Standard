# MenQ Brand Expression — Project Context / Նախագծի կոնտեքստ

**Last synchronized / Վերջին համաժամացում:** 2026-10-07  
**Decision / Որոշում:** `D-027` — Approved — Implementing  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

**Ներկա վիճակ.** Բրենդային շերտը բերվել է D-027-ի ներքո։ Canonical token source-ը (`source/brand-tokens.source.json`, 124 թոքեն) ունի `menq.design.token.*` ID-ներ, հայերեն/անգլերեն նկարագրություններ, owner և lifecycle։ `tokens.css`-ը և `tokens.json`-ը գեներացվում են և ստուգվում են CI-ում։ Core կոմպոնենտները (24) product-neutral են, Բրոյի կոմպոնենտները (5) և avatar-ը տեղափոխված են `product-extensions/bro/`։

**Ծագում.** Գույները և ոճը վերցված են `menqstudio/Webpage`-ի token-ներից, հավելվածի կոմպոնենտները՝ `menqstudio/BroPS`-ից, լրացումները նշված են։

**Սահմաններ.** Այս շերտը D-025-ի canonical token source-ը (`implementation/packages/design-tokens/source/tokens.json`) չի փոխում։ Երկու համակարգերի mapping-ը D-027-ի բաց կետ է։

**Validation.** `platforms/design/validation/validate_brand_expression.py`։

**Հաջորդ քայլեր.** (1) D-025 token source-ի հետ mapping-ի որոշում, (2) MenQ Webpage-ը որպես առաջին իրական consumer, (3) ru locale pack-ի ձևակերպում, (4) lifecycle-ը Draft-ից Approved՝ consumer evidence-ից հետո։

## English

**Current state.** The brand layer is brought in under D-027. The canonical token source (`source/brand-tokens.source.json`, 124 tokens) has `menq.design.token.*` IDs, Armenian/English descriptions, owner and lifecycle. `tokens.css` and `tokens.json` are generated and checked in CI. The core components (24) are product-neutral; Bro's components (5) and avatar moved to `product-extensions/bro/`.

**Origin.** Colours and style come from the `menqstudio/Webpage` tokens, app components from `menqstudio/BroPS`; additions are marked.

**Boundaries.** This layer does not change the D-025 canonical token source (`implementation/packages/design-tokens/source/tokens.json`). Mapping the two systems is an open D-027 item.

**Validation.** `platforms/design/validation/validate_brand_expression.py`.

**Next steps.** (1) Decide the mapping with the D-025 token source, (2) MenQ Webpage as the first real consumer, (3) formalise the ru locale pack, (4) move lifecycle from Draft to Approved after consumer evidence.

<!-- END: MENQ_BRAND_EXPRESSION_PROJECT_CONTEXT -->
