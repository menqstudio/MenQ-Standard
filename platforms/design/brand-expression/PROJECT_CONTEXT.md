# MenQ Brand Expression — Project Context / Նախագծի կոնտեքստ

**Last synchronized / Վերջին համաժամացում:** 2026-10-09 (`CR-0012`)  
**Decision / Որոշում:** `D-027` — Approved — Implementing  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

**Ներկա վիճակ.** Բրենդային շերտը բերվել է D-027-ի ներքո։ Canonical token source-ը (`source/brand-tokens.source.json`, 132 թոքեն՝ չափված 2026-10-09-ին) ունի `menq.design.token.*` ID-ներ, հայերեն/անգլերեն նկարագրություններ, owner և lifecycle։ `tokens.css`-ը, `tokens.vars.css`-ը և `tokens.json`-ը գեներացվում են և ստուգվում են CI-ում։ Core կոմպոնենտները (35՝ bundle-ի header-ում, չափված 2026-10-09-ին) product-neutral են. `components/Cover/`-ը կոմպոնենտ չէ, այլ preview քարտ։ Բրոյի կոմպոնենտները (5) և avatar-ը տեղափոխված են `product-extensions/bro/`։ 2026-10-07-ից հետո շերտը փոխվել է `CR-0003`…`CR-0010`-ով (տես [`../CHANGELOG.md`](../CHANGELOG.md))։

**Ծագում.** Գույները և ոճը վերցված են `menqstudio/Webpage`-ի token-ներից, հավելվածի կոմպոնենտները՝ `menqstudio/BroPS`-ից, լրացումները նշված են։

**Սահմաններ.** Այս շերտը D-025-ի canonical token source-ը (`implementation/packages/design-tokens/source/tokens.json`) չի փոխում։ Երկու համակարգերի mapping-ը D-027-ի բաց կետ է։

**Validation.** `platforms/design/validation/validate_brand_expression.py`։

**Հաջորդ քայլեր.** (1) D-025 token source-ի հետ mapping-ի որոշում, (2) MenQ Webpage-ը որպես առաջին իրական consumer. գրանցված է միայն `tokens.vars.css`-ի առաջին pin-ը (`493a3df`), (3) ru locale pack-ի ձևակերպում, (4) lifecycle-ը Draft-ից Approved՝ consumer evidence-ից հետո, (5) `CR-0005`…`CR-0010`-ի պակասող evidence-ը, (6) հիմնական Button-ի և Բրոյի avatar-ի թերությունը (սպիտակ տեքստը light theme-ում gradient-ի cyan ծայրում 2.43:1 էր) ուղղված է `CR-0013`-ով. Owner-ը merge է արել նրա pull request #35-ը 2026-10-09-ին։

## English

**Current state.** The brand layer is brought in under D-027. The canonical token source (`source/brand-tokens.source.json`, 132 tokens, measured on 2026-10-09) has `menq.design.token.*` IDs, Armenian/English descriptions, owner and lifecycle. `tokens.css`, `tokens.vars.css` and `tokens.json` are generated and checked in CI. The core components (35 in the bundle header, measured on 2026-10-09) are product-neutral; `components/Cover/` is not a component but a preview card. Bro's components (5) and avatar moved to `product-extensions/bro/`. Since 2026-10-07 the layer has changed through `CR-0003`…`CR-0010` (see [`../CHANGELOG.md`](../CHANGELOG.md)).

**Origin.** Colours and style come from the `menqstudio/Webpage` tokens, app components from `menqstudio/BroPS`; additions are marked.

**Boundaries.** This layer does not change the D-025 canonical token source (`implementation/packages/design-tokens/source/tokens.json`). Mapping the two systems is an open D-027 item.

**Validation.** `platforms/design/validation/validate_brand_expression.py`.

**Next steps.** (1) Decide the mapping with the D-025 token source, (2) MenQ Webpage as the first real consumer: only its first pin of `tokens.vars.css` (`493a3df`) is recorded, (3) formalise the ru locale pack, (4) move lifecycle from Draft to Approved after consumer evidence, (5) the missing evidence for `CR-0005`…`CR-0010`, (6) the defect of the primary Button and the Bro avatar (white text was 2.43:1 at the cyan end of the gradient in the light theme) is fixed by `CR-0013`; the Owner merged its pull request #35 on 2026-10-09.

<!-- END: MENQ_BRAND_EXPRESSION_PROJECT_CONTEXT -->
