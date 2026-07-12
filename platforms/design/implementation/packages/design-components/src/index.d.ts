export type ComponentSize = "sm" | "md" | "lg";
export type ButtonVariant = "primary" | "secondary" | "quiet" | "danger";
export type CardVariant = "surface" | "outlined" | "elevated";

export declare const COMPONENT_CLASS_NAMES: Readonly<{
  button: "menq-button";
  card: "menq-card";
}>;

export interface ButtonComponentOptions {
  variant?: ButtonVariant;
  size?: ComponentSize;
  loading?: boolean;
  className?: string;
  type?: "button" | "submit" | "reset";
  disabled?: boolean;
  pressed?: boolean;
  controlsId?: string;
  expanded?: boolean;
}

export interface ButtonComponentProps {
  type: "button" | "submit" | "reset";
  disabled: boolean;
  className: string;
  "data-menq-component": "button";
  "data-variant": ButtonVariant;
  "data-size": ComponentSize;
  "aria-pressed"?: boolean;
  "aria-expanded"?: boolean;
  "aria-controls"?: string;
  "aria-busy"?: true;
}

export interface CardComponentOptions {
  variant?: CardVariant;
  size?: ComponentSize;
  labelledBy?: string;
  describedBy?: string;
  className?: string;
}

export interface CardComponentProps {
  className: string;
  "data-menq-component": "card";
  "data-variant": CardVariant;
  "data-size": ComponentSize;
  "aria-labelledby"?: string;
  "aria-describedby"?: string;
}

export declare function componentClass(name: keyof typeof COMPONENT_CLASS_NAMES): string;
export declare function buttonComponentProps(options?: ButtonComponentOptions): Readonly<ButtonComponentProps>;
export declare function cardComponentProps(options?: CardComponentOptions): Readonly<CardComponentProps>;
