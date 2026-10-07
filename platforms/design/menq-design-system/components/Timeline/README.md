# Timeline

Execution timeline for agent runs and processes.

## The consumer provides
`items` [{title, meta?, detail?, state}].

## Props
- `state`: `done` · `running` · `waiting` · `failed` · `pending`

## Rules
- Execution state is always visible; motion never hides it.

_Source: MenQ addition (standard family: timeline)._
