import { assertCanonicalTokenId } from "@menq/design-contracts";

export const MOTION_INTENTS = Object.freeze([
  "enter",
  "exit",
  "change",
  "feedback",
  "ambient",
]);

export const MOTION_PROPERTIES = Object.freeze([
  "opacity",
  "transform",
  "filter",
  "clip-path",
  "color",
  "background-color",
  "box-shadow",
]);

export const REDUCED_MOTION_STRATEGIES = Object.freeze([
  "disable",
  "simplify",
  "pres