# LocaleSwitch

HY / EN / RU segmented switch. The three languages are equal.

## The consumer provides
`onChange(locale)`; optional `value`, `defaultValue` (`hy`), `label`.

## Rules
- Switching never reloads the app, keeps navigation, drawers, filters and unsaved form values, and persists per user.
- Order is always ՀԱՅ · EN · РУС. Each button has its language's own name as `title`.

_MenQ addition (standard: runtime HY/EN/RU switcher)._
