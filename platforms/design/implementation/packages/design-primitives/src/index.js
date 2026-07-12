export const PRIMITIVE_CLASS_NAMES = Object.freeze({
  visuallyHidden: "menq-visually-hidden",
  buttonReset: "menq-button-reset",
});

const BUTTON_TYPES = new Set(["button", "submit", "reset"]);
const ARIA_CURRENT_VALUES = new Set(["page", "step", "location", "date", "time", true, false]);

function optionalId(value, name) {
  if (value === undefined || value === null) return undefined;
  if (typeof value !== "string" || value.trim() === "") {
    throw new TypeError(`${name} must be a non-empty string when provided`);
  }
  return value;
}

export function primitiveClass(name) {
  const value = PRIMITIVE_CLASS_NAMES[name];
  if (!value) throw new TypeError(`Unknown primitive class: ${String(name)}`);
  return value;
}

export function buttonProps(options = {}) {
  const { type = "button", disabled = false, pressed, controlsId, expanded } = options;
  if (!BUTTON_TYPES.has(type)) throw new TypeError(`Invalid button type: ${String(type)}`);
  if (typeof disabled !== "boolean") throw new TypeError("disabled must be boolean");
  if (pressed !== undefined && typeof pressed !== "boolean") throw new TypeError("pressed must be boolean when provided");
  if (expanded !== undefined && typeof expanded !== "boolean") throw new TypeError("expanded must be boolean when provided");

  const props = { type, disabled };
  if (pressed !== undefined) props["aria-pressed"] = pressed;
  if (expanded !== undefined) props["aria-expanded"] = expanded;
  const controls = optionalId(controlsId, "controlsId");
  if (controls !== undefined) props["aria-controls"] = controls;
  return Object.freeze(props);
}

export function linkProps(options = {}) {
  const { href, current, external = false } = options;
  if (typeof href !== "string" || href.trim() === "") throw new TypeError("href must be a non-empty string");
  if (current !== undefined && !ARIA_CURRENT_VALUES.has(current)) {
    throw new TypeError(`Invalid aria-current value: ${String(current)}`);
  }
  if (typeof external !== "boolean") throw new TypeError("external must be boolean");

  const props = { href };
  if (current !== undefined) props["aria-current"] = current;
  if (external) {
    props.target = "_blank";
    props.rel = "noopener noreferrer";
  }
  return Object.freeze(props);
}

export function disclosureProps(options = {}) {
  const { expanded = false, contentId, triggerId } = options;
  if (typeof expanded !== "boolean") throw new TypeError("expanded must be boolean");
  const content = optionalId(contentId, "contentId");
  const trigger = optionalId(triggerId, "triggerId");
  if (!content || !trigger) throw new TypeError("contentId and triggerId are required");

  return Object.freeze({
    trigger: Object.freeze({
      id: trigger,
      type: "button",
      "aria-expanded": expanded,
      "aria-controls": content,
    }),
    content: Object.freeze({
      id: content,
      role: "region",
      "aria-labelledby": trigger,
      hidden: !expanded,
    }),
  });
}
