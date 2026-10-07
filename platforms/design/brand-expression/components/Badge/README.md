# Badge

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Pill պիտակ՝ բրենդի (neutral, accent, glass) և կարգավիճակի (info, success, warning, danger) տոներով։

**Ինչ է տալիս օգտագործողը.** `children` (մեկ-երկու բառ) և `tone`։

**Props**
- `tone` — `neutral` · `accent` · `glass` · `info` · `success` · `warning` · `danger`
- `dot` — կետ է ավելացնում

**Կանոններ**
- Կարգավիճակի տեքստը `-text` թոքեններով է՝ երկու թեմայում 4.5:1 և ավելի։
- Կարգավիճակի badge-ը միշտ կետ + բառ է, ոչ միայն գույն։

_Աղբյուր՝ Webpage src/components/ui/Badge.tsx։_

---

## English

Pill label with brand tones (neutral, accent, glass) and status tones (info, success, warning, danger).

**The consumer provides:** `children` (one or two words) and `tone`.

**Props**
- `tone` — `neutral` · `accent` · `glass` · `info` · `success` · `warning` · `danger`
- `dot` — forces a dot

**Rules**
- Status text uses the `-text` tokens, so every tone passes 4.5:1 in both themes.
- Status badges always carry a dot and a word, never colour alone.

_Source: Webpage src/components/ui/Badge.tsx._

<!-- END: MENQ_COMPONENT_BADGE -->
