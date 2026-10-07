# Input

Text input inside a `FormRow`; `Textarea` and `Select` share the style.

## The consumer provides
Native input attributes; `FormRow` label (and `error`) in hy/en/ru.

## Props
- `invalid`: sets `aria-invalid` and the danger border
- `FormRow`: `label`, `error`

## Rules
- `color-page-bg` fill, `color-border-subtle`, `radius-lg`. Focus: 2px `color-focus-ring`.
- Errors say what to fix, in `color-danger-text`.

_Source: BroPS ui.tsx + invalid state._
