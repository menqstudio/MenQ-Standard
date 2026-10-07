# AgentCard

Specialist agent: identity, status, scope, current task, progress.

## The consumer provides
`name`, `role`, `status`, optional `statusLabel`, `scope[]`, `task`, `progress`.

## Props
- `status`: `online` · `busy` · `offline` · `error`; `progress` 0–100

## Rules
- Scope is always visible. Progress bar uses `color-action-primary`.

_Source: MenQ addition (standard family: agent card)._
