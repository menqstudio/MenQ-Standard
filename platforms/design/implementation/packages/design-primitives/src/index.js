export const PRIMITIVE_CLASS_NAMES = Object.freeze({
  visuallyHidden: "menq-visually-hidden",
  buttonReset: "menq-button-reset",
});

const BUTTON_TYPES = new Set(["button", "submit", "reset"]);
const ARIA_CURRENT_VALUES = new Set(["page", "step", "location", "date", "time", true, false]);

function optionalId(value, name) {
  if (value === undefined || value === null