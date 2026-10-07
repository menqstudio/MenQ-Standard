# ThemeSwitch

System / Light / Dark segmented switch. Sets `data-theme` on the root.

## The consumer provides
Optional `onChange(pref)` to persist, `labels`, `value`, `defaultValue` (`system`).

## Rules
- `system` follows `prefers-color-scheme`; the rendered theme is always Light or Dark.
- Persist per user; apply before first paint to avoid a flash.

_MenQ addition (standard: runtime Dark/Light switcher; Webpage semantic.css)._
