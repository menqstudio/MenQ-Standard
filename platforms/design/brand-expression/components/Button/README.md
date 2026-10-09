# Button

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Pill կոճակ։ Light-ում հիմնականը միագույն ազուր է (`color-action-primary`, `#0369a1`. hover-ի և սեղմման ժամանակ՝ `color-action-primary-hover`, `#075985`)։ Dark-ում և `ContrastSection`-ի ներսում այն բրենդի գրադիենտն է (ազուր → cyan)։ Հիմնականը hover-ի ժամանակ glow ունի, բոլոր տարբերակները 2px բարձրանում են։

**Ինչ է տալիս օգտագործողը.** `children` (բայ՝ hy/en, անհրաժեշտության դեպքում ru locale pack), `onClick` կամ `href`։

**Props**
- `variant` — `primary` · `secondary` · `outline` · `ghost` · `danger`
- `size` — `sm` (40px) · `md` (48px) · `lg` (56px)
- `loading`, `disabled`, `icon`, `href`, `type` — loading-ը անջատում է կոճակը և դնում `aria-busy`

**Կանոններ**
- Մեկ էկրանին մեկ `primary`։
- Հիմնական կոճակի տեքստի կոնտրաստը (չափված է 2026-10-09-ին WCAG 2.1 relative luminance բանաձևով. կանոնը՝ 4.5:1)։ Light-ում սպիտակ `#ffffff`-ը `#0369a1`-ի վրա 5.93:1 է, hover-ի և սեղմման `#075985`-ի վրա՝ 7.56:1։ Dark-ում `#020617`-ը գրադիենտի վրա 7.28:1 է ազուր ծայրում (`#0ea5e9`) և 11.16:1 cyan ծայրում (`#22d3ee`)։ Բոլոր չափերը (`sm`, `md`, `lg`) անցնում են։
- Մինչև `CR-0013`-ը հիմնականը Light-ում էլ գրադիենտ էր. սպիտակ տեքստը ազուր ծայրում 5.93:1 էր, cyan ծայրում (`#06b6d4`)՝ 2.43:1։ Այս ֆայլի նախկին «ազուր ծայրում 4.1:1» տողը համապատասխանում էր `CR-0006`-ից առաջվա գույնին (`#0284c7`) և cyan ծայրի մասին ոչինչ չէր ասում։
- Շրջված տեքստը (`color-content-inverse`) դրվում է միայն `--fill-action-primary`-ի և `--fill-action-primary-hover`-ի վրա, երբեք ուղիղ `--gradient-brand`-ի վրա։ `validate_brand_expression.py`-ը կարդում է stylesheet-ները և RED է, երբ որևէ կանոն տեքստը դնում է գրադիենտի այնպիսի stop-ի վրա, որը 4.5:1-ից ցածր է որևէ theme scope-ում։
- `danger`-ը միայն `ConfirmDialog`-ի հետևում։

_Աղբյուր՝ Webpage src/components/ui/Button.tsx + BroPS։_

---

## English

Pill button. In Light the primary is solid azure (`color-action-primary`, `#0369a1`; hover and pressed: `color-action-primary-hover`, `#075985`). In Dark and inside `ContrastSection` it is the brand gradient (azure → cyan). The primary glows on hover; all variants lift 2px on hover.

**The consumer provides:** `children` (a verb, in hy/en, ru via locale pack when needed), `onClick` or `href`.

**Props**
- `variant` — `primary` · `secondary` · `outline` · `ghost` · `danger`
- `size` — `sm` (40px) · `md` (48px) · `lg` (56px)
- `loading`, `disabled`, `icon`, `href`, `type` — loading disables the button and sets `aria-busy`

**Rules**
- One `primary` per view.
- Contrast of the primary label (measured on 2026-10-09 with the WCAG 2.1 relative-luminance formula; the rule is 4.5:1). In Light, white `#ffffff` on `#0369a1` is 5.93:1, and on the hover and pressed `#075985` it is 7.56:1. In Dark, `#020617` on the gradient is 7.28:1 at the azure end (`#0ea5e9`) and 11.16:1 at the cyan end (`#22d3ee`). Every size (`sm`, `md`, `lg`) passes.
- Until `CR-0013` the primary was the gradient in Light too: white text was 5.93:1 at the azure end and 2.43:1 at the cyan end (`#06b6d4`). The earlier line in this file, "4.1:1 at the azure end", matched the colour from before `CR-0006` (`#0284c7`) and said nothing about the cyan end.
- Inverse text (`color-content-inverse`) goes only on `--fill-action-primary` and `--fill-action-primary-hover`, never directly on `--gradient-brand`. `validate_brand_expression.py` reads the stylesheets and is RED when a rule puts text on a gradient stop that is below 4.5:1 in any theme scope.
- `danger` only behind `ConfirmDialog`.

_Source: Webpage src/components/ui/Button.tsx + BroPS._

<!-- END: MENQ_COMPONENT_BUTTON -->
