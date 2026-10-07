# Badge

Pill label. Brand tones from the site (neutral, accent, glass) and status tones for apps (info, success, warning, danger — with a dot).

## The consumer provides
`children` (one or two words) and `tone`.

## Props
- `tone`: `neutral` · `accent` · `glass` · `info` · `success` · `warning` · `danger`; `dot` forces a dot

## Rules
- Status text uses the `-text` tokens, so every tone passes 4.5:1 in both themes.
- Status badges always carry a dot and a word — never color alone.

_Source: Webpage src/components/ui/Badge.tsx + status tones._
