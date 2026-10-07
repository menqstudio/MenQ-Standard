# MenQ Design System

**Source of the brand:** `menqstudio/Webpage` tokens (azure + cyan on slate), extended with BroPS app components and MenQ additions. Canonical live copy: the MenQ Design System artifact on claude.ai.

## Consuming

```html
<link rel="stylesheet" href="platforms/design/menq-design-system/tokens.css">
<link rel="stylesheet" href="platforms/design/menq-design-system/components/bundle.css">
<script src="https://cdn.jsdelivr.net/npm/react@18.3.1/umd/react.production.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/react-dom@18.3.1/umd/react-dom.production.min.js"></script>
<script src="platforms/design/menq-design-system/components/bundle.js"></script>
<!-- window.MenQ.Button, window.MenQ.BrandMark, … -->
```

- `tokens.json` — the single source of every value. `tokens.css` is generated from it; never edit `tokens.css` by hand.
- `components/<Name>/README.md` — what each component needs; `components/<Name>/preview.html` — a live example.
- `components/index.d.ts` — props as types. `fonts/` — variable fonts (OFL, licenses beside them). `assets/Logos/` — logo files and Bro's avatar.
- Set `data-theme="dark"` on `<html>` for Dark.

## Usage rules

MenQ is one brand across the website, admin and AI products (BroPS and every product UI). Product UIs inherit this system; they may extend it, never replace or contradict it.

## Direction

- Premium, warm, modern AI business with restrained futuristic expression. Calm, intelligent, human — never a generic admin template, never heavy or toy-like.
- Hierarchy comes from layout, spacing, type, borders, depth and motion — not color alone.
- The brand is **azure + cyan on slate**: `color-action-primary` (azure) for the one primary action and active states, `color-accent` (cyan) for glows, gradients and highlights, slate neutrals for everything else.
- Signature moves: pill buttons with the brand gradient, premium cards with a hairline top rule, glass surfaces, and dark navy contrast sections.

## Logo

- **Official mark:** `menq-logo-neon.png` — white "Men" with a glowing cyan power-ring Q. Dark grounds only (`neutral-950`, contrast sections, app headers); never on white.
- On light grounds, or where the neon PNG can't render, use `BrandMark` / the wordmark SVGs.
- **Bro:** `bro-avatar.png` is Bro's face. Use it wherever Bro speaks — greetings, drafts, chat — in a round frame with a 2px brand-gradient ring and `shadow-glow`. Never for humans or specialist agents.
- Use `BrandMark` in React; elsewhere the SVGs in the Logos group (`menq-wordmark-light.svg` on light grounds, `menq-wordmark-dark.svg` on dark; `menq-q-mark-*` for square slots like favicons and avatars).
- "Men" in the display face + the Q drawn as a power symbol inside an azure pill. Never recolor the pill, never split "Men" from the Q, never set "MenQ" in plain text where the mark fits.
- Clear space: at least the Q's diameter on every side. Minimum width 96px.

## Content and language

- Armenian (`hy`), English (`en`) and Russian (`ru`) are equal, first-class languages. Every string — navigation, buttons, states, errors, accessibility labels, dates, numbers, plurals — exists in all three at full quality.
- Language switches at runtime (`LocaleSwitch`), keeps navigation, drawers, filters and unsaved form values, and persists per user. Fall back to English only for a genuinely missing key.
- All three are left-to-right; components tolerate text expansion without clipping.
- Format numbers and money with `Intl` for the active locale; the dram sign `֏` follows the number.
- Voice: short, outcome-first, confident, calm. Buttons are verbs ("Ամրագրել զանգ · Book a call"). Errors say what to fix. No emoji in UI copy.

## Color

- Never use a primitive (`neutral-*`, `blue-*`, `cyan-*`, …) in a component. Use the semantic `color-*` tokens.
- Surfaces: `color-page-bg` → `color-surface-primary` (cards, inputs) → `color-surface-secondary` (wells, table headers, segmented tracks) → `color-surface-elevated` (modals, drawer, toasts). `color-surface-muted` for tracks and chips.
- Text: `color-content-primary`; `color-content-secondary` for descriptions; `color-content-muted` for labels and meta; `color-content-inverse` on azure and inverse surfaces.
- Borders: `color-border-subtle` by default; `color-border-strong` on hover, for premium top rules and on contrast panels.
- Azure as text (links, active labels): `color-action-primary-strong`. Cyan as text: `color-accent-text`. `color-accent` itself is never text in Light.
- States: fills and dots use `color-success`, `color-warning`, `color-danger`, `color-info`; **text always uses** `color-success-text`, `color-warning-text`, `color-danger-text`, `color-action-primary-strong`. Every state also carries a word or icon.
- Interaction fills: `color-hover` → `color-selected` → `color-pressed`. Focus: `color-focus-ring`. Scrims: `color-overlay`.
- Agents: `color-chat-human-bg`, `color-chat-bro-bg` + `color-chat-bro-accent`, `color-chat-agent-bg` + `color-chat-agent-accent`. Status dots: `color-status-online`, `-busy`, `-offline`, `-error`.
- Charts: series in order `color-chart-1` … `color-chart-6`; label series directly.

## Themes

- Light and Dark are mandatory and feature-complete; `ThemeSwitch` offers System, Light, Dark and sets `data-theme` on the root. Apply the saved choice before first paint.
- `ContrastSection` is a dark navy scope in both themes for results, proof and AI sections; it re-declares the color tokens, so components inside need nothing special. Use `Card variant="premium"` inside it.

## Typography

- One stack for all three scripts: `sans` and `display` = Inter, Inter Cyrillic, Noto Sans Armenian. `mono` = JetBrains Mono. All variable fonts, shipped in `fonts/`.
- Marketing: `hero` (60px), `h1` (48px), `h2` (36px) — tight leading 1.1, tracking −0.02em, balanced wrapping. Lead paragraphs `body-lg` in `color-content-secondary`.
- App: `h3` page titles, `title` for panels, modals, drawers; `body-sm` for UI text and tables; `caption` for meta; `overline` (uppercase, 0.12em) for kickers and field labels; `code` for scopes, IDs, shortcuts; `stat` for KPI numbers with tabular figures.

## Spacing, radius, elevation, layers

- Spacing steps only (`space-1` … `space-32`). Card padding `space-6`; default gap `space-4`; rows `space-3`. Page gutter `space-6`. Section padding `space-16` / `space-20` / `space-24` / `space-32`.
- Widths: `container-narrow` (text), `container-default`, `container-wide` (dashboards). Header height `size-header-height`.
- Radii: buttons, badges, nav and segmented controls are pills (`radius-button`, `radius-pill`); cards and modals `radius-card` (24px); hero panels `radius-3xl`; inputs and wells `radius-lg`; bubbles `radius-xl`; focus and kbd `radius-sm`.
- Shadows: `shadow-sm` inputs and secondary buttons; `shadow-card` cards; `shadow-premium` premium panels; `shadow-lg` modals, drawer, glass; `shadow-glow` brand highlights; `shadow-hover` interactive card hover.
- Layers: `z-raised` < `z-header` < `z-drawer` < `z-palette` < `z-modal` < `z-toast`.

## Motion

- Durations 150 / 240 / 420 / 700ms (`--duration-fast`, `--duration-base`, `--duration-slow`, `--duration-section`); easing `--ease-standard` by default, `--ease-out` for entrances.
- Hover lift: buttons 2px, interactive cards 4px. KPI count-up ≈800ms. Section reveals ≤700ms.
- Motion communicates state, never decoration, and never hides execution state or approval requirements. Reduced motion: everything becomes immediate.

## Agent identity

- Human: round avatar, neutral bubble. Bro: round avatar in the brand gradient with glow, azure-bordered bubble. Specialist agent: rounded-square avatar on the cyan wash, cyan-bordered bubble, scope tag in `code`.
- Status, scope and execution state sit next to the message (`ChatMessage`, `AgentCard`, `Timeline`). Anything needing a human decision is an `ApprovalCard` — never hidden or animated away.

## Accessibility

- 4.5:1 for text, 3:1 for icons, borders and focus, in both themes. Focus: 2px `color-focus-ring`, 2px offset.
- Known source pair: white on the azure→cyan primary gradient is 4.1:1 at its azure end and lower toward cyan in Light. Keep primary labels at 16px semibold (`md`/`lg`) and short.
- Full keyboard: Tabs move with arrow keys; Modal and Drawer close on Escape; CommandComposer sends on Enter.

## Components

- Load React 18, then `components/bundle.css` and `components/bundle.js`; everything is on `window.MenQ`. Each component's README lists what the consumer supplies.
- From Webpage: BrandMark, Button, Card, Badge, SectionHeading, MetricBar, ContrastSection.
- From BroPS (restyled): Panel, PageHeader, Avatar, Field, Input, Textarea, Select, FormRow, EmptyState, Skeleton, Toast, Modal, ConfirmDialog.
- Intentional additions (families the standard lists without code): StatusDot, Tabs, LocaleSwitch, ThemeSwitch, Drawer, KpiStat, Table, Timeline, ChatMessage, AgentCard, ApprovalCard, CommandComposer.

## Done means

- Verified in all six combinations: HY, RU, EN × Light, Dark — full translations, correct theming, no clipping, working switches, full accessibility.

## Not synced

- Not yet built: header and mobile drawer, FAQ disclosure, footer, board, room list, task and decision cards, file row, charts, command palette, app shell.
- Icon set: the site uses lucide icons; no icon files are carried here.
