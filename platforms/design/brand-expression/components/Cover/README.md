# Cover

**Status / Կարգավիճակ:** Draft (D-027) — not a component / կոմպոնենտ չէ  
**Owner / Պատասխանատու:** MenQ Owner  
**Written / Գրվել է:** 2026-10-09 (`CR-0012`), from the contents of `preview.html` only / միայն `preview.html`-ի բովանդակությունից

## Հայերեն

Սա կոմպոնենտ չէ։ Թղթապանակում կա միայն `preview.html`՝ 960×300 px ստատիկ քարտ։ Այն սկսվում է `@dsCard height=300` նշիչով, որն ունեն նաև կոմպոնենտների preview-ները։

**Ինչ է նկարում.** Մեկ SVG և մեկ տեքստային բլոկ, բոլորը brand token-ներով.
- մուգ navy ուղղանկյուն, որը դուրս է գալիս վերևի և աջ եզրերից, ներսում՝ 48px քայլով բարակ ուղղահայաց գծեր,
- բաց cyan երանգի քառակուսի (`color-accent-soft`) և cyan pill (`color-accent`),
- ազուր շրջան (`color-action-primary`), որի մեջ power նշան է՝ `color-content-inverse` գծերով,
- «MenQ» վերնագիր (120px) և մեկ տող՝ «AI-գործակալներ և ավտոմատացում՝ հայերեն, English, русский.»։

**Ինչ չէ.** `Cover`-ը չկա `bundle.js`-ի header-ում, `bundle.css`-ում և `index.d.ts`-ում. այն ոչինչ չի export անում և prop-եր չունի։ `validate_brand_expression.py`-ը այս թղթապանակը անունով ազատում է «bundle-ի header-ում չկա» ստուգումից, բայց ստուգում է նրա `var()`-երի resolution-ը։

**Ինչի համար է.** Ֆայլը չի ասում, և մինչև 2026-10-09-ը ոչ մի փաստաթուղթ այն չէր հիշատակում։ Նշանակությունը այստեղ չի ենթադրվում։

**Հայտնի անհամապատասխանություններ**
- Քարտը նկարում է `CR-0005`-ով փոխարինված նշանը (ազուր շրջան power նշանով), ոչ թե պաշտոնական մարկը։
- Միակ տողը հայերեն է և անգլերեն համարժեք չունի. այն ռուսերենը նշում է հայերենի և անգլերենի կողքին, մինչդեռ ռուսերենը locale pack է։
- Այն ուղղակի օգտագործում է պրիմիտիվներ (`--neutral-950`, `--neutral-800`, `--blue-600`), ինչը շերտի գույնի կանոնը արգելում է կոմպոնենտներում։

## English

This is not a component. The folder holds only `preview.html`, a static 960×300 px card. It starts with the `@dsCard height=300` marker that the component previews also carry.

**What it draws.** One SVG and one text block, all through brand tokens:
- a dark navy slab that bleeds off the top and right edges, with hairline vertical lines at a 48px pitch inside it,
- a soft cyan tinted square (`color-accent-soft`) and a cyan pill (`color-accent`),
- an azure disc (`color-action-primary`) carrying a power symbol drawn in `color-content-inverse` strokes,
- the heading "MenQ" (120px) and one line: «AI-գործակալներ և ավտոմատացում՝ հայերեն, English, русский.» ("AI agents and automation: Armenian, English, Russian.").

**What it is not.** `Cover` is not in the `bundle.js` header, in `bundle.css` or in `index.d.ts`; it exports nothing and has no props. `validate_brand_expression.py` exempts this folder by name from its "not listed in its bundle header" check, but does check that its `var()` references resolve.

**What it is for.** The file does not say, and until 2026-10-09 no document mentioned it. Its purpose is not guessed here.

**Known mismatches**
- The card draws the mark that `CR-0005` replaced (an azure disc with a power symbol), not the official mark.
- Its only line is in Armenian with no English counterpart, and it names Russian beside Armenian and English, while Russian is a locale pack.
- It uses primitives directly (`--neutral-950`, `--neutral-800`, `--blue-600`), which the layer's colour rule forbids in components.

<!-- END: MENQ_COMPONENT_COVER -->
