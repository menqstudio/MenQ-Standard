import { CANONICAL_LANGUAGES, assertBilingualDescription } from "@menq/design-contracts";

export const CANONICAL_LOCALES = Object.freeze([...CANONICAL_LANGUAGES]);
export const CONTENT_ID_PATTERN = /^menq\.design\.content\.[a-z0-9.-]+$/;
const CANONICAL_SET = new Set(CANONICAL_LOCALES);
const PLACEHOLDER_PATTERN = /\{([A-Za-z][A-Za-z0-9_]*)\}/g;

function placeholders(value) {
  return [...value.matchAll(PLACEHOLDER_PATTERN)].map((match) => match[1]).sort();
}

export function defineCanonicalContent(input) {
  if (!input || typeof input !== "object" || Array.isArray(input)) throw new TypeError("content record must be an object");
  if (typeof input.id !== "string" || !CONTENT_ID_PATTERN.test(input.id)) throw new TypeError(`Invalid content ID: ${String(input.id)}`);
  assertBilingualDescription(input.message);
  const hy = placeholders(input.message.hy);
  const en = placeholders(input.message.en);
  if (JSON.stringify(hy) !== JSON.stringify(en)) throw new TypeError(`Placeholder parity mismatch for ${input.id}`);
  return Object.freeze({ id: input.id, message: Object.freeze({ hy: input.message.hy, en: input.message.en }), placeholders: Object.freeze(hy) });
}

export function createLocalePack(records, extraPacks = {}) {
  if (!Array.isArray(records)) throw new TypeError("records must be an array");
  const entries = new Map(records.map((record) => {
    const value = defineCanonicalContent(record);
    return [value.id, value];
  }));
  if (entries.size !== records.length) throw new TypeError("Duplicate content ID");
  const extras = new Map();
  for (const [locale, messages] of Object.entries(extraPacks)) {
    if (CANONICAL_SET.has(locale) || !messages || typeof messages !== "object" || Array.isArray(messages)) throw new TypeError(`Invalid on-demand locale pack: ${locale}`);
    for (const id of entries.keys()) if (typeof messages[id] !== "string" || messages[id].trim() === "") throw new TypeError(`Incomplete locale ${locale}: ${id}`);
    extras.set(locale, Object.freeze({ ...messages }));
  }
  return Object.freeze({
    ids: Object.freeze([...entries.keys()].sort()),
    resolve(id, locale = "en") {
      const record = entries.get(id);
      if (!record) throw new TypeError(`Unknown content ID: ${String(id)}`);
      if (CANONICAL_SET.has(locale)) return record.message[locale];
      const pack = extras.get(locale);
      if (!pack) throw new TypeError(`Unsupported locale: ${String(locale)}`);
      return pack[id];
    },
  });
}
