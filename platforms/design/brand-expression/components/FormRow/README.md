# FormRow

**Status / Կարգավիճակ:** Draft (D-027, CR-0007)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Label + մեկ control + hint + error։ Ինքն է կապում `id`-ն, `aria-describedby`-ն և `aria-invalid`-ը։

**Ինչ է տալիս օգտագործողը.** `label`, ճիշտ մեկ child control, ըստ ցանկության `hint`, `error`, `required`, `id`։

**Կանոններ**
- Error-ը `role="alert"` է և կապված է control-ին `aria-describedby`-ով. գույնը միայն չի կրում իմաստը։
- `required`-ը ավելացնում է `*` (aria-hidden) և native `required`։

## English

Label + one control + hint + error. It wires `id`, `aria-describedby` and `aria-invalid` itself.

**The consumer provides:** `label`, exactly one child control, optional `hint`, `error`, `required`, `id`.

**Rules**
- The error has `role="alert"` and is linked to the control with `aria-describedby`; color never carries the meaning alone.
- `required` adds a `*` (aria-hidden) and native `required`.

<!-- END: MENQ_COMPONENT_FORMROW -->
