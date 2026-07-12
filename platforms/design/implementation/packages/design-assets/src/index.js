import { CANONICAL_LANGUAGES, assertBilingualDescription } from "@menq/design-contracts";

export const ASSET_KINDS = Object.freeze([
  "icon",
  "illustration",
  "image",
  "logo",
  "media",
]);

export const ASSET_ID_PATTERN = /^menq\.design\.asset\.(icon|illustration|image|logo|media)\.[a-z0-9.-]+$/;
export const ASSET_INTEGRITY_PATTERN = /^sha256-[a-f0-9]{64}$/;

const ASSET_KIND_SET = new Set(ASSET_KINDS);
const LANGUAGE_SET = new Set(CANONICAL_LANGUAGES);

function requiredString(value, name) {
  if (typeof value !== "string" || value.trim() === "") {
    throw new TypeError(`${name} must be a non-empty string`);
  }
  return value;
}

function cloneBilingual(value, name) {
  assertBilingualDescription(value);
  return Object.freeze({ hy: value.hy, en: value.en });
}

export function isCanonicalAssetId(value) {
  return typeof value === "string" && ASSET_ID_PATTERN.test(value);
}

export function defineAssetRecord(input) {
  if (input === null || typeof input !== "object" || Array.isArray(input)) {
    throw new TypeError("asset record must be an object");
  }

  const id = requiredString(input.id, "id");
  if (!isCanonicalAssetId(id)) {
    throw new TypeError(`Invalid canonical asset ID: ${id}`);
  }

  const kind = requiredString(input.kind, "kind");
  if (!ASSET_KIND_SET.has(kind)) {
    throw new TypeError(`Invalid asset kind: ${kind}`);
  }
  if (!id.startsWith(`menq.design.asset.${kind}.`)) {
    throw new TypeError(`Asset ID kind does not match record kind: ${id}`);
  }

  const decorative = input.decorative ?? false;
  if (typeof decorative !== "boolean") {
    throw new TypeError("decorative must be boolean");
  }
  if (decorative && input.alt !== undefined) {
    throw new TypeError("decorative assets must not define alt text");
  }
  if (!decorative && input.alt === undefined) {
    throw new TypeError("non-decorative assets require bilingual alt text");
  }

  const integrity = input.integrity;
  if (integrity !== undefined && !ASSET_INTEGRITY_PATTERN.test(integrity)) {
    throw new TypeError("integrity must use sha256- followed by 64 lowercase hexadecimal characters");
  }

  const record = {
    id,
    kind,
    source: requiredString(input.source, "source"),
    description: cloneBilingual(input.description, "description"),
    decorative,
    provenance: Object.freeze({
      owner: requiredString(input.provenance?.owner, "provenance.owner"),
      origin: requiredString(input.provenance?.origin, "provenance.origin"),
      license: requiredString(input.provenance?.license, "provenance.license"),
    }),
  };

  if (!decorative) record.alt = cloneBilingual(input.alt, "alt");
  if (integrity !== undefined) record.integrity = integrity;

  return Object.freeze(record);
}

export function createAssetRegistry(records) {
  if (!Array.isArray(records)) {
    throw new TypeError("records must be an array");
  }

  const entries = new Map();
  for (const input of records) {
    const record = defineAssetRecord(input);
    if (entries.has(record.id)) {
      throw new TypeError(`Duplicate asset ID: ${record.id}`);
    }
    entries.set(record.id, record);
  }

  const ids = Object.freeze([...entries.keys()].sort());

  return Object.freeze({
    ids,
    get(id) {
      const record = entries.get(id);
      if (!record) throw new TypeError(`Unknown asset ID: ${String(id)}`);
      return record;
    },
    resolve(id, locale = "en") {
      if (!LANGUAGE_SET.has(locale)) {
        throw new TypeError(`Unsupported canonical locale: ${String(locale)}`);
      }
      const record = entries.get(id);
      if (!record) throw new TypeError(`Unknown asset ID: ${String(id)}`);
      return Object.freeze({
        id: record.id,
        kind: record.kind,
        source: record.source,
        description: record.description[locale],
        alt: record.decorative ? "" : record.alt[locale],
        decorative: record.decorative,
        provenance: record.provenance,
        ...(record.integrity ? { integrity: record.integrity } : {}),
      });
    },
  });
}
