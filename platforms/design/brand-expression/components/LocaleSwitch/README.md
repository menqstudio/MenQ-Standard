# LocaleSwitch

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

ՀԱՅ / EN / РУС փոխարկիչ։ Կանոնական լեզուներն են հայերենը և անգլերենը, ռուսերենը locale pack է։

**Ինչ է տալիս օգտագործողը.** `onChange(locale)`, ըստ ցանկության `value`, `defaultValue` (`hy`), `label`։

**Props**
- `value` — `hy` · `en` · `ru`

**Կանոններ**
- Փոխարկումը app-ը չի վերաբեռնում և պահպանում է էկրանի վիճակը։
- РУС-ը ցույց տալ միայն այն արտադրանքում, որը ru locale pack ունի։

_Աղբյուր՝ MenQ addition։_

---

## English

ՀԱՅ / EN / РУС switch. Canonical languages are Armenian and English; Russian is a locale pack.

**The consumer provides:** `onChange(locale)`; optional `value`, `defaultValue` (`hy`), `label`.

**Props**
- `value` — `hy` · `en` · `ru`

**Rules**
- Switching never reloads the app and keeps screen state.
- Show РУС only in products that ship the ru locale pack.

_Source: MenQ addition._

<!-- END: MENQ_COMPONENT_LOCALESWITCH -->
