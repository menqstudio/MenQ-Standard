export type PatternClassName = "actionGroup" | "section";
export type PatternDirection = "row" | "column";
export type PatternAlignment = "start" | "center" | "end" | "stretch";
export type SectionPatternVariant = "plain" | "surface" | "outlined" | "elevated";
export type ComponentSize = "sm" | "md" | "lg";

export declare const PATTERN_CLASS_NAMES: Readonly<{
  actionGroup: "menq-pattern-action-group";
  section: "menq-pattern-section";
}>;

export declare function patternClass(name: PatternClassName): string;

export interface ActionGroupPatternOptions {
  direction?: PatternDirection;
  align?: PatternAlignment;
  wrap?: boolean;
  labelledBy?: string;
  className?: string;
}

export interface ActionGroupPatternProps {
  readonly className: string;
  readonly role: "group";
  readonly "data-menq-pattern": "action-group";
  readonly "data-direction": PatternDirection;
  readonly "data-align": PatternAlignment;
  readonly "data-wrap": "true" | "false";
  readonly "aria-labelledby"?: string;
}

export declare function actionGroupPatternProps(options?: ActionGroupPatternOptions): Readonly<ActionGroupPatternProps>;

export interface SectionPatternOptions {
  variant?: SectionPatternVariant;
  size?: ComponentSize;
  labelledBy?: string;
  describedBy?: string;
  className?: string;
}

export interface SectionPatternProps {
  readonly className: string;
  readonly "data-menq-pattern": "section";
  readonly "data-variant": SectionPatternVariant;
  readonly "data-size": ComponentSize;
  readonly "data-menq-component"?: "card";
  readonly "aria-labelledby"?: string;
  readonly "aria-describedby"?: string;
}

export declare function sectionPatternProps(options?: SectionPatternOptions): Readonly<SectionPatternProps>;
