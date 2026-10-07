# ThemeSwitch

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

System / Light / Dark փոխարկիչ։ Կիրառում է `data-theme`-ը mount-ի ժամանակ և հետևում OS-ի փոփոխություններին։

**Ինչ է տալիս օգտագործողը.** Ըստ ցանկության `onChange(pref)` (պահպանելու համար), `labels`, `value`, `defaultValue`, `apply`։

**Props**
- `apply` — `false`՝ եթե թեման արտաքինից է կիրառվում

**Կանոններ**
- Ընտրությունը պահել ըստ օգտատիրոջ և կիրառել մինչև առաջին նկարումը։

_Աղբյուր՝ MenQ addition։_

---

## English

System / Light / Dark switch. Applies `data-theme` on mount and follows OS changes.

**The consumer provides:** Optional `onChange(pref)` (to persist), `labels`, `value`, `defaultValue`, `apply`.

**Props**
- `apply` — `false` when the theme is applied elsewhere

**Rules**
- Persist per user and apply before first paint.

_Source: MenQ addition._

<!-- END: MENQ_COMPONENT_THEMESWITCH -->
