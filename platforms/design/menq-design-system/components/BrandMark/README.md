# BrandMark

The MenQ logo: "Men" set in the display face, the Q drawn as a power symbol in an azure pill.

## The consumer provides
Nothing. Optional `compact`, `admin` (adds the ADMIN tag), `tag` (custom tag text).

## Props
- `compact`: smaller size for dense headers
- `admin`: shows the uppercase tag after the mark

## Rules
- The Q pill is always `color-action-primary` with `color-content-inverse` symbol and `shadow-glow`. Never recolor it, never separate "Men" from the Q.
- Clear space around the mark: at least the Q's diameter. Minimum width: 96px.
- Outside React (email, PDF, favicon) use the SVGs in the Logos asset group: `menq-wordmark-light.svg` on light grounds, `menq-wordmark-dark.svg` on dark, `menq-q-mark-*` when space is square.

_Source: Webpage src/components/brand/BrandMark.tsx._
