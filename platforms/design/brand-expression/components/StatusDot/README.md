# StatusDot

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Կենդանի վիճակի նշան՝ գործակալների, աշխատանքների, մարդկանց համար։

**Ինչ է տալիս օգտագործողը.** `status`, `label` (թարգմանված)։

**Props**
- `status` — `online` · `busy` · `offline` · `error`

**Կանոններ**
- Գույները՝ `color-status-*`։ `busy`-ը պուլսավորում է, reduced motion-ի դեպքում՝ ոչ։
- Label-ը միշտ ցույց տալ։

_Աղբյուր՝ MenQ addition։_

---

## English

Live state indicator for agents, runs and people.

**The consumer provides:** `status`, `label` (translated).

**Props**
- `status` — `online` · `busy` · `offline` · `error`

**Rules**
- Colours: `color-status-*`. `busy` pulses; reduced motion stops it.
- Always show the label.

_Source: MenQ addition._

<!-- END: MENQ_COMPONENT_STATUSDOT -->
