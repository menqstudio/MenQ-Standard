# Modal

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Երկխոսություն մուգ շերտի վրա՝ focus trap-ով, Escape-ով և focus-ի վերադարձով։

**Ինչ է տալիս օգտագործողը.** `title`, `onClose`, `children`; `inline`՝ միայն փաստաթղթերի համար, առանց scrim-ի և trap-ի։

**Props**
- `title`, `onClose`, `inline`

**Կանոններ**
- `color-surface-elevated`, `radius-card`, `shadow-lg`, scrim՝ `color-overlay`, z՝ `z-modal`։

_Աղբյուր՝ BroPS src/components/ui.tsx։_

---

## English

Dialog on a scrim with a focus trap, Escape to close and focus restore.

**The consumer provides:** `title`, `onClose`, `children`; `inline` renders without scrim or trap (docs only).

**Props**
- `title`, `onClose`, `inline`

**Rules**
- `color-surface-elevated`, `radius-card`, `shadow-lg`, scrim `color-overlay`, z `z-modal`.

_Source: BroPS src/components/ui.tsx._

<!-- END: MENQ_COMPONENT_MODAL -->
