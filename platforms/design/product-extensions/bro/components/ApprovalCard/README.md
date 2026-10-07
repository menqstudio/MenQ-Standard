# ApprovalCard

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Մարդու հաստատում՝ գործակալի գործողությունից առաջ։

**Ինչ է տալիս օգտագործողը.** `title`, `risk`, ըստ ցանկության `description`, `requestedBy`, label-ներ, `onApprove`, `onReject`։

**Props**
- `risk` — `low` · `medium` · `high`

**Կանոններ**
- Հաստատման պահանջը երբեք չի թաքցվում։ Մերժելը նույնքան հեշտ է, որքան հաստատելը։

_Աղբյուր՝ MenQ addition (Bro)։_

---

## English

Human approval gate for an agent action.

**The consumer provides:** `title`, `risk`, optional `description`, `requestedBy`, labels, `onApprove`, `onReject`.

**Props**
- `risk` — `low` · `medium` · `high`

**Rules**
- Approval requirements are never hidden. Rejecting is as easy as approving.

_Source: MenQ addition (Bro)._

<!-- END: MENQ_COMPONENT_APPROVALCARD -->
