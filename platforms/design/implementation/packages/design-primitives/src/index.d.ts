export declare const PRIMITIVE_CLASS_NAMES: Readonly<{
  visuallyHidden: "menq-visually-hidden";
  buttonReset: "menq-button-reset";
}>;

export type PrimitiveClassName = keyof typeof PRIMITIVE_CLASS_NAMES;
export type AriaCurrent = "page" | "step" | "location" | "date" | "time" | boolean;

export declare function primitiveClass(name: PrimitiveClassName): string;

export interface ButtonOptions {
  type?: "button" | "submit" | "reset";
  disabled?: boolean;
  pressed?: boolean;
  controlsId?: string;
  expanded?: boolean;
}

export declare function buttonProps(options?: ButtonOptions): Readonly<Record<string, string | boolean>>;

export interface LinkOptions {
  href: string;
  current?: AriaCurrent;
  external?: boolean;
}

export declare function linkProps(options: LinkOptions): Readonly<Record<string, string | boolean>>;

export interface DisclosureOptions {
  expanded?: boolean;
  contentId: string;
  triggerId: string;
}

export interface DisclosureProps {
  trigger: Readonly<Record<string, string | boolean>>;
  content: Readonly<Record<string, string | boolean>>;
}

export declare function disclosureProps(options: DisclosureOptions): Readonly<DisclosureProps>;
