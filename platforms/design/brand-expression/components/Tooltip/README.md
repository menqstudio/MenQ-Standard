# Tooltip

**Status / Կարգավիճակ:** Draft (D-027, CR-0009)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Լրացուցիչ կարճ տեքստ hover-ի և ստեղնաշարի focus-ի դեպքում։

**Ինչ է տալիս օգտագործողը.** `content`, ճիշտ մեկ focus ստացող trigger (`children`), `placement`, `delay`։

**Կանոններ**
- Tooltip-ը երբեք չի կրում հիմնական տեղեկություն և չի պարունակում հղումներ կամ կոճակներ։
- Բացվում է focus-ի դեպքում էլ, փակվում է Escape-ով, կապված է trigger-ին `aria-describedby`-ով։

## English

Short supplementary text on hover and keyboard focus.

**The consumer provides:** `content`, exactly one focusable trigger (`children`), `placement`, `delay`.

**Rules**
- A tooltip never carries essential information and never contains links or buttons.
- It also opens on focus, closes with Escape, and is linked to the trigger with `aria-describedby`.

<!-- END: MENQ_COMPONENT_TOOLTIP -->
