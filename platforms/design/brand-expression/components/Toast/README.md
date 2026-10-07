# Toast

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Կարճ հաստատում՝ status շրջանակով և առանձին փակելու կոճակով։

**Ինչ է տալիս օգտագործողը.** `children`, `tone`, ըստ ցանկության `onDismiss`, `dismissLabel`։

**Props**
- `tone` — `success` · `info` · `error`

**Կանոններ**
- `role="status"`, z-index `z-toast`։

_Աղբյուր՝ BroPS src/components/toast.tsx։_

---

## English

Transient confirmation in a status region with a separate dismiss button.

**The consumer provides:** `children`, `tone`, optional `onDismiss`, `dismissLabel`.

**Props**
- `tone` — `success` · `info` · `error`

**Rules**
- `role="status"`, z-index `z-toast`.

_Source: BroPS src/components/toast.tsx._

<!-- END: MENQ_COMPONENT_TOAST -->
