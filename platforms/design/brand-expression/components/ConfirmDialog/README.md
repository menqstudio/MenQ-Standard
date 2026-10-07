# ConfirmDialog

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Երկրորդ քայլ՝ անդառնալի գործողությունից առաջ։

**Ինչ է տալիս օգտագործողը.** `title`, `message`, label-ներ, `onConfirm`, `onCancel`։

**Props**
- `title`, `message`, `confirmLabel`, `cancelLabel`

**Կանոններ**
- Ghost չեղարկում՝ ձախ, danger հաստատում՝ աջ։

_Աղբյուր՝ BroPS src/components/ui.tsx։_

---

## English

Second step before anything destructive.

**The consumer provides:** `title`, `message`, labels, `onConfirm`, `onCancel`.

**Props**
- `title`, `message`, `confirmLabel`, `cancelLabel`

**Rules**
- Ghost cancel on the left, danger confirm on the right.

_Source: BroPS src/components/ui.tsx._

<!-- END: MENQ_COMPONENT_CONFIRMDIALOG -->
