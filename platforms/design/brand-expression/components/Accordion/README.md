# Accordion

**Status / Կարգավիճակ:** Draft (D-027, CR-0009)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Բացվող-փակվող բաժիններ (FAQ)՝ WAI-ARIA disclosure pattern-ով։

**Ինչ է տալիս օգտագործողը.** `items` (`id`, `title`, `content`), `multiple`, `defaultOpen`/`open`, `onChange`, `headingLevel`։

**Կանոններ**
- Վերնագիրը իսկական heading է (`headingLevel`, լռությամբ h3), կոճակը ունի `aria-expanded` և `aria-controls`։
- Կարևոր տեղեկությունը չթաքցնել accordion-ի մեջ. այն լրացուցիչ մանրամասների համար է։

## English

Expandable sections (FAQ) using the WAI-ARIA disclosure pattern.

**The consumer provides:** `items` (`id`, `title`, `content`), `multiple`, `defaultOpen`/`open`, `onChange`, `headingLevel`.

**Rules**
- The title is a real heading (`headingLevel`, h3 by default); the button has `aria-expanded` and `aria-controls`.
- Do not hide essential information in an accordion; it is for supporting detail.

<!-- END: MENQ_COMPONENT_ACCORDION -->
