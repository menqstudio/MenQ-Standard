import { buttonProps } from "@menq/design-primitives";

export const COMPONENT_CLASS_NAMES = Object.freeze({
  button: "menq-button",
  card: "menq-card",
});

const BUTTON_VARIANTS = new Set(["primary", "secondary", "quiet", "danger"]);
const COMPONENT_SIZES = new Set(["sm", "md", "lg"]);
const CARD_VARIANTS = new Set(["surface", "outlined", "elevated"]);

function enumValue(value, allowed, name) {
  if (!allowed.has(value)) {
    throw new TypeError(`Invalid ${name}: ${String(value)}`);
  }
  return value;
}

function optionalId(value, name) {
  if (value === undefined || value === null) return undefined;
  if (typeof value !== "string" || value.trim() === "") {
    throw new TypeError(`${name} must be a non-empty string when provided`);
  }
  return value;
}

export function componentClass(name) {
  const value = COMPONENT_CLASS_NAMES[name];
  if (!value) throw new TypeError(`Unknown component class: ${String(name)}`);
  return value;
}

export function buttonComponentProps(options = {}) {
  const {
    variant = "primary",
    size = "md",
    loading = false,
    className,
    ...primitiveOptions
  } = options;

  enumValue(variant, BUTTON_VARIANTS, "button variant");
  enumValue(size, COMPONENT_SIZES, "button size");
  if (typeof loading !== "boolean") throw new TypeError("loading must be boolean");
  if (className !== undefined && (typeof className !== "string" || className.trim() === "")) {
    throw new TypeError("className must be a non-empty string when provided");
  }

  const primitive = buttonProps({
    ...primitiveOptions,
    disabled: Boolean(primitiveOptions.disabled || loading),
  });

  const props = {
    ...primitive,
    className: className ? `${COMPONENT_CLASS_NAMES.button} ${className}` : COMPONENT_CLASS_NAMES.button,
    "data-menq-component": "button",
    "data-variant": variant,
    "data-size": size,
  };
  if (loading) props["aria-busy"] = true;
  return Object.freeze(props);
}

export function cardComponentProps(options = {}) {
  const {
    variant = "surface",
    size = "md",
    labelledBy,
    describedBy,
    className,
  } = options;

  enumValue(variant, CARD_VARIANTS, "card variant");
  enumValue(size, COMPONENT_SIZES, "card size");
  if (className !== undefined && (typeof className !== "string" || className.trim() === "")) {
    throw new TypeError("className must be a non-empty string when provided");
  }

  const props = {
    className: className ? `${COMPONENT_CLASS_NAMES.card} ${className}` : COMPONENT_CLASS_NAMES.card,
    "data-menq-component": "card",
    "data-variant": variant,
    "data-size": size,
  };
  const label = optionalId(labelledBy, "labelledBy");
  const description = optionalId(describedBy, "describedBy");
  if (label !== undefined) props["aria-labelledby"] = label;
  if (description !== undefined) props["aria-describedby"] = description;
  return Object.freeze(props);
}
