# Card

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Premium քարտ՝ `radius-card`, `space-6` padding, 1px `color-border-subtle` և վերևում բարակ գիծ։

**Ինչ է տալիս օգտագործողը.** `children`, ըստ ցանկության `variant`, `interactive`, `className`, `style`։

**Props**
- `variant` — `solid` · `elevated` · `outline` · `glass` · `brand` · `premium`
- `interactive` — hover-ի ժամանակ բարձրանում է 4px, `shadow-hover`

**Կանոններ**
- `interactive` միայն սեղմվող քարտերի համար։
- Քարտը քարտի մեջ չդնել։ `ContrastSection`-ում՝ `premium`։

_Աղբյուր՝ Webpage src/components/ui/Card.tsx։_

---

## English

Premium card: `radius-card`, `space-6` padding, 1px `color-border-subtle` and a hairline top rule.

**The consumer provides:** `children`; optional `variant`, `interactive`, `className`, `style`.

**Props**
- `variant` — `solid` · `elevated` · `outline` · `glass` · `brand` · `premium`
- `interactive` — lifts 4px with `shadow-hover` on hover

**Rules**
- Only clickable cards are `interactive`.
- Never nest cards. Inside a `ContrastSection` use `premium`.

_Source: Webpage src/components/ui/Card.tsx._

<!-- END: MENQ_COMPONENT_CARD -->
