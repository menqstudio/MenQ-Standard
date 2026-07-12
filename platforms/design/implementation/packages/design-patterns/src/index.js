import { cardComponentProps } from "@menq/design-components";

export const PATTERN_CLASS_NAMES = Object.freeze({
  actionGroup: "menq-pattern-action-group",
  section: "menq-pattern-section",
});

const ALIGNMENTS = new Set(["start", "center", "end", "stretch"]);
const DIRECTIONS = new Set(["row", "column"]);
const SECTION_VARIANTS = new Set(["plain", "surface", "outlined", "elevated"]);
const COMPONENT_SIZES = new Set(["sm", "md", "lg"]);

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

export function patternClass(name) {
  const value = PATTERN_CLASS_NAMES[name];
  if (!value) throw new TypeError(`Unknown pattern class: ${String(name)}`);
  return value;
}

export function actionGroupPatternProps(options = {}) {
  const {
    direction = "row",
    align = "end",
    wrap = true,
    labelledBy,
    className,
  } = options;

  enumValue(direction, DIRECTIONS, "action-group direction");
  enumValue(align, ALIGNMENTS, "action-group alignment");
  if (typeof wrap !== "boolean") throw new TypeError("wrap must be boolean");
  if (className !== undefined && (typeof className !== "string" || className.trim() === "")) {
    throw new TypeError("className must be a non-empty string when provided");
  }

  const props = {
    className: className ? `${PATTERN_CLASS_NAMES.actionGroup} ${className}` : PATTERN_CLASS_NAMES.actionGroup,
    role: "group",
    "data-menq-pattern": "action-group",
    "data-direction": direction,
    "data-align": align,
    "data-wrap": wrap ? "true" : "false",
  };
  const label = optionalId(labelledBy, "labelledBy");
  if (label !== undefined) props["aria-labelledby"] = label;
  return Object.freeze(props);
}

export function sectionPatternProps(options = {}) {
  const {
    variant = "plain",
    size = "md",
    labelledBy,
    describedBy,
    className,
  } = options;

  enumValue(variant, SECTION_VARIANTS, "section variant");
  enumValue(size, COMPONENT_SIZES, "section size");
  if (className !== undefined && (typeof className !== "string" || className.trim() === "")) {
    throw new TypeError("className must be a non-empty string when provided");
  }
  const baseClass = className ? `${PATTERN_CLASS_NAMES.section} ${className}` : PATTERN_CLASS_NAMES.section;

  if (variant === "plain") {
    const props = {
      className: baseClass,
      "data-menq-pattern": "section",
      "data-variant": "plain",
      "data-size": size,
    };
    const label = optionalId(labelledBy, "labelledBy");
    const description = optionalId(describedBy, "describedBy");
    if (label !== undefined) props["aria-labelledby"] = label;
    if (description !== undefined) props["aria-describedby"] = description;
    return Object.freeze(props);
  }

  const card = cardComponentProps({
    variant,
    size,
    labelledBy,
    describedBy,
    className: baseClass,
  });

  return Object.freeze({
    ...card,
    "data-menq-pattern": "section",
  });
}
