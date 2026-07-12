export const CANONICAL_LANGUAGES = Object.freeze(["hy", "en"]);

export const TOKEN_LAYERS = Object.freeze([
  "Reference",
  "Semantic",
  "Component",
  "Pattern",
  "Product Extension",
]);

export const TOKEN_TYPES = Object.freeze([
  "color",
  "dimension",
  "number",
  "duration",
  "cubic-bezier",
  "font-family",
  "font-weight",
  "line-height",
  "shadow",
  "string",
]);

export const TOKEN_ID_PATTERN = /^menq\.design\.token\.(reference|semantic|component|pattern|product-extension)\.[a-z0-9.-]+$/;
export const TOKEN_SOURCE