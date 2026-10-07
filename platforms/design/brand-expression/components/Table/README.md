# Table

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Տվյալների աղյուսակ՝ վերնագրով, hover տողերով և cell renderer-ներով։

**Ինչ է տալիս օգտագործողը.** `columns`, `rows`, ըստ ցանկության `caption`։

**Props**
- `columns` — [{key,label,align?,render?}]

**Կանոններ**
- Թվերը աջ հավասարեցված։ Նեղ էկրանին հորիզոնական scroll։ Դատարկ `rows`-ը չի կոտրում։

_Աղբյուր՝ MenQ addition։_

---

## English

Data table with header, hover rows and cell renderers.

**The consumer provides:** `columns`, `rows`, optional `caption`.

**Props**
- `columns` — [{key,label,align?,render?}]

**Rules**
- Numbers align right. Scrolls horizontally on narrow screens. Missing `rows` renders empty.

_Source: MenQ addition._

<!-- END: MENQ_COMPONENT_TABLE -->
