# Textarea

**Status / Կարգավիճակ:** Draft (D-027, CR-0007)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Բազմատող տեքստի դաշտ՝ `Input`-ի ոճով։ Օգտագործվում է `FormRow`-ի մեջ։

**Ինչ է տալիս օգտագործողը.** Native textarea-ի ատրիբուտներ, `invalid`։

**Կանոններ**
- Միշտ `FormRow`-ի մեջ, որ label-ը և error-ը կապված լինեն։
- `invalid`-ը ցույց է տալիս `color-danger-text` եզր և `aria-invalid`։

## English

A multi-line text field styled like `Input`. Used inside `FormRow`.

**The consumer provides:** Native textarea attributes, `invalid`.

**Rules**
- Always inside `FormRow` so the label and error are linked.
- `invalid` shows a `color-danger-text` border and sets `aria-invalid`.

<!-- END: MENQ_COMPONENT_TEXTAREA -->
