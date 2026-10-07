# Tabs

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Միևնույն բովանդակության տարբեր տեսքերի միջև անցում։

**Ինչ է տալիս օգտագործողը.** `items` [{value,label,count?,id?,controls?}], ըստ ցանկության `value`/`onChange`, `label`։

**Props**
- `items`, `defaultValue`, `value`, `onChange`, `label`

**Կանոններ**
- Սլաքները, Home և End ստեղները տեղափոխում են ընտրությունը և focus-ը (roving tabindex)։
- Ակտիվ tab-ը ընդգծված է `color-action-primary`-ով։

_Աղբյուր՝ MenQ addition։_

---

## English

Switch between views of the same content.

**The consumer provides:** `items` [{value,label,count?,id?,controls?}], optional `value`/`onChange`, `label`.

**Props**
- `items`, `defaultValue`, `value`, `onChange`, `label`

**Rules**
- Arrow keys, Home and End move selection and focus (roving tabindex).
- The active tab is underlined with `color-action-primary`.

_Source: MenQ addition._

<!-- END: MENQ_COMPONENT_TABS -->
