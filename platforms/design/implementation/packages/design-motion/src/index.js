import { assertCanonicalTokenId } from "@menq/design-contracts";

export const MOTION_INTENTS = Object.freeze(["enter", "exit", "change", "feedback", "ambient"]);
export const MOTION_PROPERTIES = Object.freeze(["opacity", "transform", "filter", "clip-path", "color", "background-color", "box-shadow"]);
export const REDUCED_MOTION_STRATEGIES = Object.freeze(["disable", "simplify", "preserve"]);
export const MOTION_RECIPE_ID_PATTERN = /^menq\.design\.motion\.(enter|exit|change|feedback|ambient)\.[a-z0-9.-]+$/;

const INTENTS = new Set(MOTION_INTENTS);
const PROPERTIES = new Set(MOTION_PROPERTIES);
const STRATEGIES = new Set(REDUCED_MOTION_STRATEGIES);

function requiredString(value, name) {
  if (typeof value !== "string" || value.trim() === "") throw new TypeError(`${name} must be a non-empty string`);
  return value;
}

export function defineMotionRecipe(input) {
  if (input === null || typeof input !== "object" || Array.isArray(input)) throw new TypeError("motion recipe must be an object");
  const id = requiredString(input.id, "id");
  const intent = requiredString(input.intent, "intent");
  if (!MOTION_RECIPE_ID_PATTERN.test(id)) throw new TypeError(`Invalid motion recipe ID: ${id}`);
  if (!INTENTS.has(intent) || !id.startsWith(`menq.design.motion.${intent}.`)) throw new TypeError("motion intent must match the recipe ID");
  const properties = input.properties;
  if (!Array.isArray(properties) || properties.length === 0) throw new TypeError("properties must be a non-empty array");
  const uniqueProperties = [...new Set(properties.map((value) => requiredString(value, "property")))];
  for (const property of uniqueProperties) if (!PROPERTIES.has(property)) throw new TypeError(`Unsupported motion property: ${property}`);
  const durationToken = requiredString(input.durationToken, "durationToken");
  const easingToken = requiredString(input.easingToken, "easingToken");
  assertCanonicalTokenId(durationToken);
  assertCanonicalTokenId(easingToken);
  const reducedMotion = input.reducedMotion ?? "simplify";
  if (!STRATEGIES.has(reducedMotion)) throw new TypeError(`Invalid reduced-motion strategy: ${reducedMotion}`);
  if (intent === "ambient" && reducedMotion === "preserve") throw new TypeError("ambient motion may not be preserved under reduced motion");
  return Object.freeze({ id, intent, properties: Object.freeze(uniqueProperties), durationToken, easingToken, reducedMotion });
}

export function resolveMotionRecipe(recipe, prefersReducedMotion = false) {
  if (typeof prefersReducedMotion !== "boolean") throw new TypeError("prefersReducedMotion must be boolean");
  const value = defineMotionRecipe(recipe);
  if (!prefersReducedMotion || value.reducedMotion === "preserve") return value;
  if (value.reducedMotion === "disable") return Object.freeze({ ...value, disabled: true, properties: Object.freeze([]) });
  return Object.freeze({ ...value, reduced: true, properties: Object.freeze(value.properties.filter((property) => property === "opacity" || property === "color" || property === "background-color")) });
}
