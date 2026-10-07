# ChatMessage

Chat message with distinct human, Bro and specialist-agent identities.

## The consumer provides
`role`, `author`, `children`, optional `time`, `scope`, `state`, `stateLabel`, `mine`.

## Props
- `role`: `human` · `bro` · `agent`
- `state`: `running` · `done` · `failed`

## Rules
- Identity by avatar shape + bubble border + name, not colour alone.
- Agent scope (mono) and execution state sit next to the message.

_Source: BroPS chat CSS + MenQ identity layer._
