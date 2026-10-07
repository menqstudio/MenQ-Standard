# Timeline

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Գործակալի աշխատանքի ընթացքի ժամանակագրություն։

**Ինչ է տալիս օգտագործողը.** `items` [{title, meta?, detail?, state}]։

**Props**
- `state` — `done` · `running` · `waiting` · `failed` · `pending`

**Կանոններ**
- Կատարման վիճակը միշտ տեսանելի է, շարժումը այն չի թաքցնում։

_Աղբյուր՝ MenQ addition (Bro)։_

---

## English

Execution timeline for agent runs.

**The consumer provides:** `items` [{title, meta?, detail?, state}].

**Props**
- `state` — `done` · `running` · `waiting` · `failed` · `pending`

**Rules**
- Execution state is always visible; motion never hides it.

_Source: MenQ addition (Bro)._

<!-- END: MENQ_COMPONENT_TIMELINE -->
