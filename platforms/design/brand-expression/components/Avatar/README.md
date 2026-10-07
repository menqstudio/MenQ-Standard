# Avatar

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Կլոր avatar՝ սկզբնատառով կամ նկարով։

**Ինչ է տալիս օգտագործողը.** `name`, ըստ ցանկության `src`, `kind`։

**Props**
- `src` — նկարի հասցե, `alt`-ը `name`-ն է
- `kind` — product extension-ների ձևի hook (`mq-avatar--<kind>`)

**Կանոններ**
- Սկզբնատառով avatar-ը `role="img"` է `aria-label`-ով։
- Core-ը ոչ մի արտադրանքի ինքնություն չի սահմանում․ Bro-ի ձևերը `product-extensions/bro`-ում են։

_Աղբյուր՝ BroPS src/components/ui.tsx։_

---

## English

Round avatar with an initial or an image.

**The consumer provides:** `name`; optional `src`, `kind`.

**Props**
- `src` — image URL; `alt` is `name`
- `kind` — shape hook for product extensions (`mq-avatar--<kind>`)

**Rules**
- An initial avatar is `role="img"` with `aria-label`.
- The core defines no product identity; Bro shapes live in `product-extensions/bro`.

_Source: BroPS src/components/ui.tsx._

<!-- END: MENQ_COMPONENT_AVATAR -->
