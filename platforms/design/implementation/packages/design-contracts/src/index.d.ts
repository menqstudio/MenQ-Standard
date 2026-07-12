export type CanonicalLanguage = "hy" | "en";
export type TokenLayer = "Reference" | "Semantic" | "Component" | "Pattern" | "Product Extension";
export type TokenType =
  | "color"
  | "dimension"
  | "number"
  | "duration"
  | "cubic-bezier"
  | "font-family"
  | "font-weight"
  | "line-height"
  | "shadow"
  | "string";

export interface BilingualDescription {
  hy: string;
  en: string;
}

export interface CanonicalTokenRecord {
  id: string;
  layer: TokenLayer;
  type: TokenType;
  description: BilingualDescription;
  ownerId: string;
  lifecycle: "Draft" | "Approved — Implementing" | "Locked" | "Deprecated";
  value?: string | number;
  reference?: string;
}

export interface TokenSourceDocument {
  schemaVersion: 1;
  sourceId: string;
  decision: "D-025";
  status: "Approved — Implementing";
  canonicalLanguages: readonly ["hy", "en"];
  generatedOutputsAreCanonical: false;
  tokens: CanonicalTokenRecord[];
}

export const CANONICAL_LANGUAGES: readonly ["hy", "en"];
export const TOKEN_LAYERS: readonly TokenLayer[];
export const TOKEN_TYPES: readonly TokenType[];
export const TOKEN_ID_PATTERN: RegExp;
export const TOKEN_SOURCE_SCHEMA_ID: "menq.design.schema.token-source.v1";

export function isCanonicalTokenId(value: unknown): value is string;
export function assertCanonicalTokenId(value: unknown): asserts value is string;
export function assertBilingualDescription(value: unknown): asserts value is BilingualDescription;
