# MenQ Brand Expression / MenQ բրենդային արտահայտում

**Status / Կարգավիճակ:** Draft — implementing under `D-027` / Draft՝ `D-027`-ի ներքո իրականացվում է  
**Decision / Որոշում:** [`D-027`](../decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md)  
**Owner / Պատասխանատու:** MenQ Owner  
**Registry spec / Registry spec:** `menq.design.spec.brand-expression.v1`

## Հայերեն

### Ինչ է սա

MenQ-ի բրենդային արտահայտման շերտն է՝ ազուր և cyan գույներ slate ֆոնի վրա, տառատեսակ, տարածություններ, կլորացումներ, ստվերներ, շարժում, լոգո և product-neutral կոմպոնենտներ։ Այն D-025 Design Platform-ի consumer-ն է և չի փոխարինում նրա canonical token source-ին։ Կոնկրետ արտադրանքի (օրինակ՝ Բրո) տարրերը գտնվում են [`../product-extensions/`](../product-extensions/)-ում։

### Աղբյուրներ և գեներացված ֆայլեր

- `source/brand-tokens.source.json` — **միակ canonical աղբյուրը**։ Ամեն թոքեն ունի `menq.design.token.*` ID, շերտ, տեսակ, հայերեն և անգլերեն նկարագրություն, պատասխանատու և lifecycle։ Schema՝ `source/brand-token-source.schema.json`։
- `tokens.css` և `tokens.json` — **գեներացված** են `scripts/build_brand_tokens.py`-ով։ Ձեռքով չխմբագրել։ `tokens.json`-ը design-tool mirror է։
- `tokens.vars.css` — **գեներացված**, միայն CSS custom property-ներ (առանց type-style class-երի և `@font-face`-ի)։ Սա է արտադրանքների (օր.՝ MenQ Webpage) համար consumption artifact-ը, որպեսզի class-երը չբախվեն արտադրանքի սեփական class-երի հետ։
- `components/bundle.js`, `components/bundle.css`, `components/index.d.ts` — core կոմպոնենտներ (`window.MenQ`)։
- `assets/ASSET_RECORDS.json` — լոգոների և ֆոնտերի owner, provenance, license, sha256։

### Միացում

```html
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="components/bundle.css">
<script src="https://cdn.jsdelivr.net/npm/react@18.3.1/umd/react.production.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/react-dom@18.3.1/umd/react-dom.production.min.js"></script>
<script src="components/bundle.js"></script>
```

Dark թեմայի համար `<html>`-ին դնել `data-theme="dark"` կամ օգտագործել `ThemeSwitch`։

### Լեզուներ

- Հայերենը (`hy`) և անգլերենը (`en`) հավասար canonical լեզուներ են (D-025)։
- Ռուսերենը (`ru`) **locale pack** է՝ այն արտադրանքների համար, որոնք դրա կարիքն ունեն (օրինակ՝ MenQ Webpage, BroPS)։ Այդ արտադրանքում այն պետք է լինի ամբողջական։
- Թվերը և գումարները ձևաչափել `Intl`-ով ակտիվ locale-ի համար, `֏`-ը թվից հետո։
- Ձայնը՝ կարճ, արդյունքի վրա կենտրոնացած, հանգիստ։ Կոճակները բայեր են։ Սխալները ասում են՝ ինչ ուղղել։ UI տեքստում emoji չկա։

### Գույն

- Կոմպոնենտներում պրիմիտիվներ (`neutral-*`, `blue-*`, `cyan-*`…) չօգտագործել, միայն semantic `color-*` թոքեններ։
- Մակերեսներ՝ `color-page-bg` → `color-surface-primary` → `color-surface-secondary` → `color-surface-elevated`։
- Տեքստ՝ `color-content-primary`, `color-content-secondary`, `color-content-muted`, `color-content-inverse`։
- Ազուրը որպես տեքստ՝ `color-action-primary-strong`։ Cyan-ը որպես տեքստ՝ `color-accent-text`։ `color-accent`-ը light-ում տեքստ չէ։
- Վիճակների տեքստը միշտ `-text` թոքեններով է (`color-success-text`, `color-warning-text`, `color-danger-text`), և ամեն վիճակ ունի բառ կամ իկոն։
- Հարաբերական լցոններ՝ `color-hover` → `color-selected` → `color-pressed`։ Focus՝ `color-focus-ring`։ Scrim՝ `color-overlay`։

### Թեմաներ

- Light-ը և Dark-ը պարտադիր են և հավասար։ `ThemeSwitch`-ը տալիս է System, Light, Dark։
- `ContrastSection`-ը մուգ navy բաժին է երկու թեմայում էլ․ tokens.css-ը նրա ներսում dark արժեքներ է կիրառում։

### Տառատեսակ

- `sans` և `display`՝ Inter, Inter Cyrillic, Noto Sans Armenian, `mono`՝ JetBrains Mono։ Variable ֆոնտերը `fonts/`-ում են (OFL-1.1)։
- Մարքեթինգ՝ `hero`, `h1`, `h2`։ Հավելված՝ `h3`, `title`, `body-sm`, `caption`, `overline`, `code`, `stat`։

### Տարածություն, կլորացում, շերտեր, շարժում

- Միայն `space-*` քայլեր։ Քարտ՝ `space-6`, լռելյայն gap՝ `space-4`։
- Կոճակներ և badge-եր՝ pill (`radius-button`, `radius-pill`), քարտեր՝ `radius-card`, դաշտեր՝ `radius-lg`։
- Շերտեր՝ `z-raised` < `z-header` < `z-drawer` < `z-palette` < `z-modal` < `z-toast`։
- Շարժում՝ տես «Շարժում և վիդեո» բաժինը։

### Շարժում և վիդեո

**Սկզբունքներ.** Շարժումը բացատրում է՝ ինչ փոխվեց, որտեղից եկավ, ինչ է հիմա ակտիվ։ Այն երբեք չի դանդաղեցնում գործողությունը և չի կրում միակ իմաստը։ `prefers-reduced-motion: reduce`-ի դեպքում մուտքի և լոգոյի անիմացիաներն անջատվում են, բովանդակությունը ցույց է տրվում անմիջապես։

**Ժամանակներ.**
- `duration-fast` (150ms)՝ hover, focus, toggle։ `duration-base` (240ms)՝ dropdown, tooltip, drawer, modal։ `duration-slow` (420ms)՝ տարրի կամ քարտի մուտք։ `duration-section` (700ms)՝ ամբողջ բաժնի փոխանցում։
- Easing՝ `ease-standard` վիճակի փոփոխության համար, `ease-out` մուտքի համար, `ease-in-out` տեղաշարժի համար։ Linear՝ միայն progress-ի և spinner-ի համար։

**Անվանված pattern-ներ** (`Reveal` կոմպոնենտ, մեկ անգամ, երբ տարրը մտնում է էկրան).
- `fade`՝ միայն opacity։ `rise`՝ opacity + `motion-distance-md` վերև (քարտեր, բաժիններ)։ `rise-sm`՝ `motion-distance-sm` (փոքր տարրեր)։ `scale`՝ 0.96 → 1 (մեդիա, նկարներ)։
- Stagger՝ `index` × `motion-stagger` (60ms), առավելագույնը 8 քայլ։
- Hero-ի վերնագիրը, LCP տարրը և կարևոր CTA-ն `Reveal`-ով չթաքցնել։

**Լոգոյի power-on.** `BrandMark powerOn`՝ «Men»-ը հայտնվում է, Q-ի օղակը գծվում է, գիծը վառվում է, glow-ը միանում է (`duration-power-on`, 1.2վ)։ Միայն hero-ում, splash-ում կամ loading-ում, մեկ անգամ session-ում։ Header-ում և կրկնվող տեղերում՝ ոչ։

**Վիդեո.**
- Autoplay՝ միայն `muted` + `playsinline` + `poster`, առանց ձայնի։ 5 վայրկյանից երկար շարժման համար պարտադիր է տեսանելի pause կոճակ (WCAG 2.2.2)։ Reduced motion-ի դեպքում autoplay չկա, ցույց է տրվում poster-ը։
- Վայրկյանում 3-ից ավել բռնկում չի թույլատրվում (WCAG 2.3.1)։ Խոսքով վիդեոն ունի ենթագրեր (հայերեն, անգլերեն) և transcript։
- Ֆորմատ՝ MP4 (H.264) + WebM, hero loop ≤ 3 MB, ≤ 1080p։ Գույնը՝ brand ֆոն (slate/ink) + ազուր/cyan շեշտեր, առանց այլ ապրանքանիշերի։

**Shader-ներ.** Core շերտի մաս չեն։ Թույլատրվում են միայն որպես առանձին optional expression package՝ static fallback-ով, reduced motion-ի դեպքում անջատված, էկրանից դուրս՝ կանգնեցված։ Նման package ստեղծելու համար անհրաժեշտ է նոր CR։

### Լոգո

- React-ում՝ `BrandMark`։ Այլ տեղերում՝ `assets/Logos/`-ի ֆայլերը (կանոնները՝ նրա README-ում)։

### Իկոնագրություն

- Մեկ ընտանիք՝ Lucide (ISC), 24 grid, `--icon-stroke` (2), կլոր ծայրեր։ Չափերը՝ `--icon-size-sm` (16px), `--icon-size-md` (20px), `--icon-size-lg` (24px)։ Գույնը՝ `currentColor`։ React-ում՝ `Icon` կոմպոնենտը։ App icon-ները և favicon-ը՝ `assets/Icons/`։

### Մատչելիություն

- Տեքստ՝ 4.5:1, իկոններ և control-ների եզրեր՝ 3:1, երկու թեմայում։ Ամբողջական ստեղնաշարային կառավարում, տեսանելի focus (`color-focus-ring`)։
- `validate_brand_expression.py`-ը մեքենայորեն ստուգում է 17 տեքստ/ֆոն զույգ երկու թեմայում (34 ստուգում, ≥ 4.5:1)։ Token-ի փոփոխությունը, որը խախտում է զույգը, RED է։
- Accent գույնը որպես տեքստ՝ միայն `color-accent-text`, ազուրը որպես տեքստ՝ `color-action-primary-strong`։ Սպիտակ տեքստ՝ միայն `color-action-primary`-ի վրա (5.9:1, CR-0006)։
- Ձևեր՝ `FormRow`-ը կապում է label-ը, hint-ը և error-ը control-ին (`aria-describedby`, `aria-invalid`), error-ը `role="alert"` է։ Checkbox/Radio/Switch-ը native են կամ `role="switch"`։

---

## English

### What this is

MenQ's brand expression layer: azure and cyan on slate, type, spacing, radii, shadows, motion, logo and product-neutral components. It is a consumer of the D-025 Design Platform and does not replace its canonical token source. Product-specific parts (for example Bro) live in [`../product-extensions/`](../product-extensions/).

### Sources and generated files

- `source/brand-tokens.source.json` — **the only canonical source**. Every token has a `menq.design.token.*` ID, layer, type, Armenian and English description, owner and lifecycle. Schema: `source/brand-token-source.schema.json`.
- `tokens.css` and `tokens.json` — **generated** by `scripts/build_brand_tokens.py`. Never edit by hand. `tokens.json` is a design-tool mirror.
- `tokens.vars.css` — **generated**, CSS custom properties only (no type-style classes, no `@font-face`). This is the consumption artifact for products (e.g. MenQ Webpage), so its classes cannot collide with a product's own classes.
- `components/bundle.js`, `components/bundle.css`, `components/index.d.ts` — core components (`window.MenQ`).
- `assets/ASSET_RECORDS.json` — owner, provenance, license and sha256 for logos and fonts.

### Consuming

```html
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="components/bundle.css">
<script src="https://cdn.jsdelivr.net/npm/react@18.3.1/umd/react.production.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/react-dom@18.3.1/umd/react-dom.production.min.js"></script>
<script src="components/bundle.js"></script>
```

Set `data-theme="dark"` on `<html>` for Dark, or use `ThemeSwitch`.

### Languages

- Armenian (`hy`) and English (`en`) are equal canonical languages (D-025).
- Russian (`ru`) is a **locale pack** for products that need it (for example MenQ Webpage, BroPS). Where shipped, it must be complete.
- Format numbers and money with `Intl` for the active locale; `֏` follows the number.
- Voice: short, outcome-first, calm. Buttons are verbs. Errors say what to fix. No emoji in UI copy.

### Colour

- Never use primitives (`neutral-*`, `blue-*`, `cyan-*`…) in components; use the semantic `color-*` tokens.
- Surfaces: `color-page-bg` → `color-surface-primary` → `color-surface-secondary` → `color-surface-elevated`.
- Text: `color-content-primary`, `color-content-secondary`, `color-content-muted`, `color-content-inverse`.
- Azure as text: `color-action-primary-strong`. Cyan as text: `color-accent-text`. `color-accent` is never text in Light.
- State text always uses the `-text` tokens (`color-success-text`, `color-warning-text`, `color-danger-text`), and every state carries a word or icon.
- Interaction fills: `color-hover` → `color-selected` → `color-pressed`. Focus: `color-focus-ring`. Scrims: `color-overlay`.

### Themes

- Light and Dark are mandatory and equal. `ThemeSwitch` offers System, Light, Dark.
- `ContrastSection` is a dark navy section in both themes; tokens.css applies the dark values inside it.

### Typography

- `sans` and `display`: Inter, Inter Cyrillic, Noto Sans Armenian; `mono`: JetBrains Mono. Variable fonts in `fonts/` (OFL-1.1).
- Marketing: `hero`, `h1`, `h2`. App: `h3`, `title`, `body-sm`, `caption`, `overline`, `code`, `stat`.

### Spacing, radius, layers, motion

- `space-*` steps only. Cards `space-6`; default gap `space-4`.
- Buttons and badges are pills (`radius-button`, `radius-pill`); cards `radius-card`; inputs `radius-lg`.
- Layers: `z-raised` < `z-header` < `z-drawer` < `z-palette` < `z-modal` < `z-toast`.
- Motion: see "Motion and video".

### Motion and video

**Principles.** Motion explains what changed, where it came from and what is active now. It never slows an action down and never carries the only meaning. Under `prefers-reduced-motion: reduce`, entrance and logo animations are switched off and content is shown at once.

**Timing.**
- `duration-fast` (150ms): hover, focus, toggles. `duration-base` (240ms): dropdowns, tooltips, drawers, modals. `duration-slow` (420ms): an element or card entering. `duration-section` (700ms): a whole-section transition.
- Easing: `ease-standard` for state changes, `ease-out` for entrances, `ease-in-out` for movement. Linear only for progress and spinners.

**Named patterns** (the `Reveal` component, played once when the element enters the viewport).
- `fade`: opacity only. `rise`: opacity plus `motion-distance-md` upward (cards, sections). `rise-sm`: `motion-distance-sm` (small elements). `scale`: 0.96 → 1 (media, images).
- Stagger: `index` × `motion-stagger` (60ms), at most 8 steps.
- Never hide the hero heading, the LCP element or a primary CTA behind `Reveal`.

**Logo power-on.** `BrandMark powerOn`: "Men" fades in, the Q ring draws, the stem lights, then the glow comes on (`duration-power-on`, 1.2s). Only in a hero, splash or loading state, once per session. Never in the header or in repeated places.

**Video.**
- Autoplay only with `muted` + `playsinline` + `poster`, never with sound. Motion longer than 5 seconds needs a visible pause control (WCAG 2.2.2). Under reduced motion there is no autoplay; the poster is shown.
- No more than 3 flashes per second (WCAG 2.3.1). Video with speech has captions (Armenian, English) and a transcript.
- Format: MP4 (H.264) + WebM, hero loop ≤ 3 MB, ≤ 1080p. Colour: brand grounds (slate/ink) with azure/cyan accents, no other brands.

**Shaders.** Not part of the core layer. Allowed only as a separate optional expression package with a static fallback, switched off under reduced motion and paused off-screen. Creating such a package requires a new CR.

### Logo

- In React use `BrandMark`. Elsewhere use the files in `assets/Logos/` (rules in its README).

### Iconography

- One family: Lucide (ISC), 24 grid, `--icon-stroke` (2), round caps. Sizes: `--icon-size-sm` (16px), `--icon-size-md` (20px), `--icon-size-lg` (24px). Color is `currentColor`. In React use the `Icon` component. App icons and the favicon live in `assets/Icons/`.

### Accessibility

- Text 4.5:1, icons and control borders 3:1, in both themes. Full keyboard operation with a visible focus (`color-focus-ring`).
- `validate_brand_expression.py` machine-checks 17 text/background pairs in both themes (34 checks, ≥ 4.5:1). A token change that breaks a pair is RED.
- Accent as text uses only `color-accent-text`; azure as text uses `color-action-primary-strong`. White text only on `color-action-primary` (5.9:1, CR-0006).
- Forms: `FormRow` links the label, hint and error to its control (`aria-describedby`, `aria-invalid`); the error has `role="alert"`. Checkbox/Radio are native inputs; Switch uses `role="switch"`.

<!-- END: MENQ_BRAND_EXPRESSION_README -->
