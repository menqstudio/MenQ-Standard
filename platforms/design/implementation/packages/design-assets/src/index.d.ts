export type CanonicalLanguage = "hy" | "en";
export type AssetKind = "icon" | "illustration" | "image" | "logo" | "media";

export interface BilingualText {
  hy: string;
  en: string;
}

export interface AssetProvenance {
  owner: string;
  origin: string;
  license: string;
}

export interface AssetRecordInput {
  id: string;
  kind: AssetKind;
  source: string;
  description: BilingualText;
  decorative?: boolean;
  alt?: BilingualText;
  provenance: AssetProvenance;
  integrity?: string;
}

export interface AssetRecord {
  readonly id: string;
  readonly kind: AssetKind;
  readonly source: string;
  readonly description: Readonly<BilingualText>;
  readonly decorative: boolean;
  readonly alt?: Readonly<BilingualText>;
  readonly provenance: Readonly<AssetProvenance>;
  readonly integrity?: string;
}

export interface ResolvedAsset {
  readonly id: string;
  readonly kind: AssetKind;
  readonly source: string;
  readonly description: string;
  readonly alt: string;
  readonly decorative: boolean;
  readonly provenance: Readonly<AssetProvenance>;
  readonly integrity?: string;
}

export interface AssetRegistry {
  readonly ids: readonly string[];
  get(id: string): AssetRecord;
  resolve(id: string, locale?: CanonicalLanguage): ResolvedAsset;
}

export declare const ASSET_KINDS: readonly AssetKind[];
export declare const ASSET_ID_PATTERN: RegExp;
export declare const ASSET_INTEGRITY_PATTERN: RegExp;
export declare function isCanonicalAssetId(value: unknown): value is string;
export declare function defineAssetRecord(input: AssetRecordInput): AssetRecord;
export declare function createAssetRegistry(records: AssetRecordInput[]): AssetRegistry;
