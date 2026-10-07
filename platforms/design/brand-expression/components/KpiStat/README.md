# KpiStat

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

KPI քարտ՝ ~800ms թվի աճով և delta-ով։

**Ինչ է տալիս օգտագործողը.** `label`, `value`, ըստ ցանկության `unit`, `delta`, `deltaLabel`, `locale`, `variant`։

**Props**
- `locale` — լռելյայն `hy-AM`

**Կանոններ**
- Reduced motion-ի դեպքում թիվը միանգամից է։ Tabular թվեր։
- Delta՝ սլաք + նշան + գույն (`color-success-text` / `color-danger-text`)։

_Աղբյուր՝ MenQ addition։_

---

## English

KPI tile with an ~800ms count-up and a delta.

**The consumer provides:** `label`, `value`, optional `unit`, `delta`, `deltaLabel`, `locale`, `variant`.

**Props**
- `locale` — default `hy-AM`

**Rules**
- Instant under reduced motion. Tabular figures.
- Delta: arrow + sign + colour (`color-success-text` / `color-danger-text`).

_Source: MenQ addition._

<!-- END: MENQ_COMPONENT_KPISTAT -->
