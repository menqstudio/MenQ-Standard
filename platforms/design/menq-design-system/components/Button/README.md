# Button

Pill button: the primary is the brand gradient (azure → cyan) with a glow on hover; all variants lift 2px on hover.

## The consumer provides
`children` (verb label in hy/en/ru), `onClick` or `href` (renders a link).

## Props
- `variant`: `primary` (default) · `secondary` · `outline` · `ghost` · `danger`
- `size`: `sm` (40px) · `md` (48px) · `lg` (56px); `small` = `size: 'sm'`
- `loading`, `disabled`, `icon`, `href`, `type`, `title`

## Rules
- One `primary` per view. Hero CTAs use `lg`; app toolbars use `sm`.
- Radius `radius-button` (pill). Heights `button-height-*`.
- Primary label is `color-content-inverse` on the gradient — 4.1:1 at the azure end in Light. Keep primary labels at 16px semibold (`md`/`lg`); in Light avoid `sm` primary for long text.
- `danger` only behind `ConfirmDialog`.

_Source: Webpage src/components/ui/Button.tsx + BroPS danger/loading._
