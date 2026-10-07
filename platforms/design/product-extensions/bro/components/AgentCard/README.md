# AgentCard

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Մասնագետ գործակալ՝ ինքնություն, վիճակ, scope, ընթացիկ գործ, progress։

**Ինչ է տալիս օգտագործողը.** `name`, `role`, `status`, ըստ ցանկության `statusLabel`, `scope[]`, `task`, `progress`, `progressLabel`։

**Props**
- `progress` — 0–100, սահմանափակված

**Կանոններ**
- Scope-ը միշտ տեսանելի է։ Progress bar-ն ունի հասանելի անուն։

_Աղբյուր՝ MenQ addition (Bro)։_

---

## English

Specialist agent: identity, status, scope, current task, progress.

**The consumer provides:** `name`, `role`, `status`, optional `statusLabel`, `scope[]`, `task`, `progress`, `progressLabel`.

**Props**
- `progress` — 0–100, clamped

**Rules**
- Scope is always visible. The progress bar has an accessible name.

_Source: MenQ addition (Bro)._

<!-- END: MENQ_COMPONENT_AGENTCARD -->
