export type Verdict = "GREEN" | "YELLOW" | "RED";
export type ConformanceProfile = "core-author" | "product-consumer" | "documentation-consumer" | "design-tool";
export interface CheckResult { id: string; passed: boolean }
export interface ConformanceResultInput { profile: ConformanceProfile; verdict: Verdict; commitSha: string; checks?: CheckResult[]; exceptions?: string[] }
export interface DocumentationEntryInput { id: string; title: { hy: string; en: string }; packageName: string; publicApi?: string[]; sourcePath: string }
export const VERDICTS: readonly Verdict[];
export const CONFORMANCE_PROFILES: readonly ConformanceProfile[];
export function validateBilingualParity(value: unknown): readonly string[];
export function validateDesignToolMapping(mapping: unknown): readonly string[];
export function extractDocumentationEntry(input: DocumentationEntryInput): Readonly<DocumentationEntryInput>;
export function createConformanceResult(input: ConformanceResultInput): Readonly<ConformanceResultInput>;
