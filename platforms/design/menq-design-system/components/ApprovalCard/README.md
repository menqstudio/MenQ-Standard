# ApprovalCard

Human approval gate for an agent action.

## The consumer provides
`title`, `risk`, optional `description`, `requestedBy`, labels, `onApprove`, `onReject`.

## Props
- `risk`: `low` · `medium` · `high`

## Rules
- Approval requirements are never hidden or animated away.
- High risk: danger border; reject stays as easy as approve.

_Source: MenQ addition (standard family: approval card)._
