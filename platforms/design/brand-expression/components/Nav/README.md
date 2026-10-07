# Nav

**Status / Կարգավիճակ:** Draft (D-027, CR-0009)  
**Owner / Պատասխանատու:** MenQ Owner

## Հայերեն

Նավիգացիայի landmark՝ ընթացիկ էջը նշված `aria-current`-ով։

**Ինչ է տալիս օգտագործողը.** `label` (պարտադիր, `aria-label`), `items` (`href`, `label`, `current`, `icon`), `orientation`։

**Կանոններ**
- Էջում մի քանի `nav`-ի դեպքում յուրաքանչյուրը տարբեր `label` ունի (օր.՝ «Հիմնական», «Footer»)։
- Ընթացիկ էջը ցույց է տրվում ոչ միայն գույնով, այլև ֆոնով և `aria-current="page"`-ով։ Mobile-ում Nav-ը դրվում է `Drawer`-ի մեջ։

## English

A navigation landmark with the current page marked by `aria-current`.

**The consumer provides:** `label` (required, `aria-label`), `items` (`href`, `label`, `current`, `icon`), `orientation`.

**Rules**
- With several `nav`s on a page, each has a different `label` (e.g. "Main", "Footer").
- The current page is shown by background and `aria-current="page"`, not by color alone. On mobile, put Nav inside a `Drawer`.

<!-- END: MENQ_COMPONENT_NAV -->
