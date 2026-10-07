# Input

**Status / Կարգավիճակ:** Draft (D-027)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Տեքստի դաշտ `FormRow`-ի մեջ։ `Textarea`-ն և `Select`-ը նույն ոճն ունեն։

**Ինչ է տալիս օգտագործողը.** Native input-ի ատրիբուտներ, `FormRow`-ի label և `error`։

**Props**
- `invalid` — դնում է `aria-invalid` և սխալի եզրագիծ
- `FormRow` — `label`, `error`

**Կանոններ**
- Ֆոնը՝ `color-surface-primary`, եզրը՝ `color-border-subtle`, `radius-lg`։ Focus՝ `color-focus-ring`։
- Սխալը ասում է՝ ինչ ուղղել, `color-danger-text`-ով։

_Աղբյուր՝ BroPS src/components/ui.tsx։_

---

## English

Text input inside a `FormRow`; `Textarea` and `Select` share the style.

**The consumer provides:** Native input attributes; a `FormRow` label and `error`.

**Props**
- `invalid` — sets `aria-invalid` and the danger border
- `FormRow` — `label`, `error`

**Rules**
- `color-surface-primary` fill, `color-border-subtle`, `radius-lg`. Focus uses `color-focus-ring`.
- Errors say what to fix, in `color-danger-text`.

_Source: BroPS src/components/ui.tsx._

<!-- END: MENQ_COMPONENT_INPUT -->
