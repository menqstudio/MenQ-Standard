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
export const TOKEN_SOURCE_SCHEMA_ID = "menq.design.schema.token-source.v1";

export function isCanonicalTokenId(value) {
  return typeof value === "string" && TOKEN_ID_PATTERN.test(value);
}

export function assertCanonicalTokenId(value) {
  if (!isCanonicalTokenId(value)) {
    throw new TypeError(`Invalid canonical token ID: ${String(value)}`);
  }
}

export function assertBilingualDescription(value) {
  if (
    value === null ||
    typeof value !== "object" ||
    typeof value.hy !== "string" ||
    value.hy.trim() === "" ||
    typeof value.en !== "string" ||
    value.en.trim() === ""
  ) {
    throw new TypeError("A bilingual description requires non-empty hy and en values.");
  }
}
