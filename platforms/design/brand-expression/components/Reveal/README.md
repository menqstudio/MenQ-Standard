# Reveal

**Status / Կարգավիճակ:** Draft (D-027, CR-0010)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Անվանված մուտքի անիմացիա (`fade`, `rise`, `rise-sm`, `scale`), որը մեկ անգամ է խաղում, երբ տարրը մտնում է էկրան։

**Ինչ է տալիս օգտագործողը.** `children`, `pattern` (լռությամբ `rise`), `index` (stagger, մինչև 8), `as`։

**Կանոններ**
- Reduced motion-ի կամ IntersectionObserver չլինելու դեպքում բովանդակությունը ցույց է տրվում անմիջապես, առանց անիմացիայի։
- Hero-ի վերնագիրը, LCP տարրը և հիմնական CTA-ն `Reveal`-ի մեջ չդնել։ Մեկ բաժնում՝ մեկ pattern։

## English

A named entrance animation (`fade`, `rise`, `rise-sm`, `scale`) that plays once when the element enters the viewport.

**The consumer provides:** `children`, `pattern` (default `rise`), `index` (stagger, up to 8), `as`.

**Rules**
- Under reduced motion, or without IntersectionObserver, content is shown at once without animation.
- Never wrap the hero heading, the LCP element or the primary CTA in `Reveal`. One pattern per section.

<!-- END: MENQ_COMPONENT_REVEAL -->
