# ChatMessage

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Չատի հաղորդագրություն՝ մարդ, Բրո և մասնագետ գործակալ։

**Ինչ է տալիս օգտագործողը.** `role`, `author`, `children`, ըստ ցանկության `time`, `scope`, `state`, `stateLabel`, `mine`, `avatarSrc`։

**Props**
- `role` — `human` · `bro` · `agent`
- `MenQ.Bro.avatarSrc` — Բրոյի նկարը (assets/bro-avatar.png)

**Կանոններ**
- Ինքնությունը՝ avatar-ի ձև + եզրագիծ + անուն, ոչ միայն գույն։
- Scope-ը և կատարման վիճակը հաղորդագրության կողքին են։

_Աղբյուր՝ BroPS chat CSS + MenQ։_

---

## English

Chat message for human, Bro and specialist-agent voices.

**The consumer provides:** `role`, `author`, `children`, optional `time`, `scope`, `state`, `stateLabel`, `mine`, `avatarSrc`.

**Props**
- `role` — `human` · `bro` · `agent`
- `MenQ.Bro.avatarSrc` — Bro's image (assets/bro-avatar.png)

**Rules**
- Identity by avatar shape + border + name, not colour alone.
- Scope and execution state sit next to the message.

_Source: BroPS chat CSS + MenQ._

<!-- END: MENQ_COMPONENT_CHATMESSAGE -->
