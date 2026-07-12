export type MotionIntent = "enter" | "exit" | "change" | "feedback" | "ambient";
export type MotionProperty = "opacity" | "transform" | "filter" | "clip-path" | "color" | "background-color" | "box-shadow";
export type ReducedMotionStrategy = "disable" | "simplify" | "preserve";

export interface MotionRecipeInput {
  id: string;
  intent: MotionIntent;
  properties: MotionProperty[];
  durationToken: string;
  easingToken: string;
  reducedMotion?: ReducedMotionStrategy;
}

export interface MotionRecipe {
  readonly id: string;
  readonly intent: MotionIntent;
  readonly properties: readonly MotionProperty[];
  readonly durationToken: string;
  readonly easingToken: string;
  readonly reducedMotion: ReducedMotionStrategy;
  readonly disabled?: boolean;
  readonly reduced?: boolean;
}

export const MOTION_INTENTS: readonly MotionIntent[];
export const MOTION_PROPERTIES: readonly MotionProperty[];
export const REDUCED_MOTION_STRATEGIES: readonly ReducedMotionStrategy[];
export const MOTION_RECIPE_ID_PATTERN: RegExp;
export function defineMotionRecipe(input: MotionRecipeInput): MotionRecipe;
export function resolveMotionRecipe(recipe: MotionRecipeInput, prefersReducedMotion?: boolean): MotionRecipe;
