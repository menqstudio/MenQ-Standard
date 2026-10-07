# Card

Premium card: `radius-card` (24px), `space-6` padding, 1px `color-border-subtle`, and a hairline top rule fading through `color-border-strong`.

## The consumer provides
`children`; optional `variant`, `interactive`, `className`, `style`.

## Props
- `variant`: `solid` (default) · `elevated` (`shadow-card`) · `outline` · `glass` · `brand` (soft brand gradient) · `premium` (panel gradient + `shadow-premium`)
- `interactive`: lifts 4px with `shadow-hover` on hover

## Rules
- Only clickable cards are `interactive`.
- Never nest cards. Inside a `ContrastSection` use `premium`.

_Source: Webpage src/components/ui/Card.tsx + design-v2.css._
