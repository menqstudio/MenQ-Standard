# Button

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Pill կոճակ։ Հիմնականը բրենդի գրադիենտն է (ազուր → cyan), hover-ի ժամանակ glow-ով, բոլոր տարբերակները 2px բարձրանում են։

**Ինչ է տալիս օգտագործողը.** `children` (բայ՝ hy/en, անհրաժեշտության դեպքում ru locale pack), `onClick` կամ `href`։

**Props**
- `variant` — `primary` · `secondary` · `outline` · `ghost` · `danger`
- `size` — `sm` (40px) · `md` (48px) · `lg` (56px)
- `loading`, `disabled`, `icon`, `href`, `type` — loading-ը անջատում է կոճակը և դնում `aria-busy`

**Կանոններ**
- Մեկ էկրանին մեկ `primary`։
- Light-ում gradient-ի վրա սպիտակ տեքստը ազուր ծայրում 4.1:1 է․ primary label-ները պահել 16px semibold (`md`/`lg`)։
- `danger`-ը միայն `ConfirmDialog`-ի հետևում։

_Աղբյուր՝ Webpage src/components/ui/Button.tsx + BroPS։_

---

## English

Pill button. The primary is the brand gradient (azure → cyan) with a glow on hover; all variants lift 2px on hover.

**The consumer provides:** `children` (a verb, in hy/en, ru via locale pack when needed), `onClick` or `href`.

**Props**
- `variant` — `primary` · `secondary` · `outline` · `ghost` · `danger`
- `size` — `sm` (40px) · `md` (48px) · `lg` (56px)
- `loading`, `disabled`, `icon`, `href`, `type` — loading disables the button and sets `aria-busy`

**Rules**
- One `primary` per view.
- White on the gradient is 4.1:1 at the azure end in Light; keep primary labels 16px semibold (`md`/`lg`).
- `danger` only behind `ConfirmDialog`.

_Source: Webpage src/components/ui/Button.tsx + BroPS._

<!-- END: MENQ_COMPONENT_BUTTON -->
