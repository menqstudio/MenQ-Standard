export const VERDICTS = Object.freeze(["GREEN", "YELLOW", "RED"]);
export const CONFORMANCE_PROFILES = Object.freeze(["core-author", "product-consumer", "documentation-consumer", "design-tool"]);
const VERDICT_SET = new Set(VERDICTS);
const PROFILE_SET = new Set(CONFORMANCE_PROFILES);

function requiredString(value, name) {
  if (typeof value !== "string" || value.trim() === "") throw new TypeError(`${name} must be a non-empty string`);
  return value;
}

export function validateBilingualParity(value) {
  const errors = [];
  if (!value || typeof value !== "object" || Array.isArray(value)) return Object.freeze(["value must be an object"]);
  if (typeof value.hy !== "string" || value.hy.trim() === "") errors.push("missing Armenian value");
  if (typeof value.en !== "string" || value.en.trim() === "") errors.push("missing English value");
  return Object.freeze(errors);
}

export function validateDesignToolMapping(mapping) {
  const errors = [];
  if (!mapping || typeof mapping !== "object" || Array.isArray(mapping)) return Object.freeze(["mapping must be an object"]);
  for (const field of ["canonicalId", "sourcePath", "packageName", "version"]) {
    if (typeof mapping[field] !== "string" || mapping[field].trim() === "") errors.push(`missing ${field}`);
  }
  return Object.freeze(errors);
}

export function extractDocumentationEntry(input) {
  if (!input || typeof input !== "object" || Array.isArray(input)) throw new TypeError("documentation entry must be an object");
  const bilingualErrors = validateBilingualParity(input.title);
  if (bilingualErrors.length) throw new TypeError(bilingualErrors.join(", "));
  return Object.freeze({
    id: requiredString(input.id, "id"),
    title: Object.freeze({ hy: input.title.hy, en: input.title.en }),
    packageName: requiredString(input.packageName, "packageName"),
    publicApi: Object.freeze([...(input.publicApi ?? [])]),
    sourcePath: requiredString(input.sourcePath, "sourcePath"),
  });
}

export function createConformanceResult(input) {
  if (!input || typeof input !== "object" || Array.isArray(input)) throw new TypeError("conformance result must be an object");
  const verdict = requiredString(input.verdict, "verdict");
  const profile = requiredString(input.profile, "profile");
  if (!VERDICT_SET.has(verdict)) throw new TypeError(`Invalid verdict: ${verdict}`);
  if (!PROFILE_SET.has(profile)) throw new TypeError(`Invalid profile: ${profile}`);
  const checks = Array.isArray(input.checks) ? input.checks.map((check) => Object.freeze({ id: requiredString(check.id, "check.id"), passed: Boolean(check.passed) })) : [];
  if (verdict === "GREEN" && checks.some((check) => !check.passed)) throw new TypeError("GREEN result may not contain failed checks");
  return Object.freeze({ profile, verdict, commitSha: requiredString(input.commitSha, "commitSha"), checks: Object.freeze(checks), exceptions: Object.freeze([...(input.exceptions ?? [])]) });
}
