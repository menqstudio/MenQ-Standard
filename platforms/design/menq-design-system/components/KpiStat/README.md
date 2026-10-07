# KpiStat

KPI tile with ~800ms count-up and a delta.

## The consumer provides
`label`, `value`, optional `unit`, `delta`, `deltaLabel`, `locale`.

## Props
- `value` number, `unit`, `delta` (%), `deltaLabel`, `locale` (default hy-AM)

## Rules
- Count-up 800ms ease-out; instant under reduced motion. Tabular numbers.
- Delta arrow + sign + colour (`color-success-text` / `-danger-text`).

_Source: MenQ addition (standard: KPI count-up ≈800ms)._
