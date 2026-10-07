# Icon

**Status / Կարգավիճակ:** Draft (D-027, CR-0009)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

24-grid գծային իկոն (Lucide-ի երկրաչափություն)՝ միասնական չափով և հաստությամբ։

**Ինչ է տալիս օգտագործողը.** SVG path-եր (`children`), `size` (`sm` 16px, `md` 20px, `lg` 24px), ըստ ցանկության `label`։

**Կանոններ**
- Իկոնագրության աղբյուրը Lucide-ն է (ISC լիցենզիա)՝ 24 grid, `--icon-stroke` (2), կլոր ծայրեր։ Ուրիշ իկոնների ընտանիքներ չխառնել։
- Չափերը միայն `--icon-size-sm/md/lg`-ով։ Գույնը՝ `currentColor`, այսինքն ծնողի տեքստի token-ը։
- Դեկորատիվ իկոնը `aria-hidden` է։ Եթե իկոնը միակ իմաստակիրն է (օր.՝ կոճակ առանց տեքստի), տալ `label` կամ կոճակին `aria-label`։
- Իկոնը տեքստի հետ՝ `sm` կամ `md`, կոճակներում՝ `md`, feature-ներում և empty state-երում՝ `lg`։

## English

A 24-grid stroke icon (Lucide geometry) with one size scale and stroke.

**The consumer provides:** SVG paths (`children`), `size` (`sm` 16px, `md` 20px, `lg` 24px), optional `label`.

**Rules**
- The iconography source is Lucide (ISC licence): 24 grid, `--icon-stroke` (2), round caps. Do not mix other icon families.
- Sizes only through `--icon-size-sm/md/lg`. Color is `currentColor`, i.e. the parent's text token.
- A decorative icon is `aria-hidden`. When the icon is the only carrier of meaning (e.g. an icon-only button), give it a `label` or give the button an `aria-label`.
- With text use `sm` or `md`; in buttons `md`; in features and empty states `lg`.

<!-- END: MENQ_COMPONENT_ICON -->
