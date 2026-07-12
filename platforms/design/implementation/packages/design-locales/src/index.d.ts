export interface BilingualMessage { hy: string; en: string }
export interface CanonicalContentInput { id: string; message: BilingualMessage }
export interface CanonicalContent extends CanonicalContentInput { readonly placeholders: readonly string[] }
export interface LocalePack { readonly ids: readonly string[]; resolve(id: string, locale?: string): string }
export const CANONICAL_LOCALES: readonly ("hy" | "en")[];
export const CONTENT_ID_PATTERN: RegExp;
export function defineCanonicalContent(input: CanonicalContentInput): CanonicalContent;
export function createLocalePack(records: CanonicalContentInput[], extraPacks?: Record<string, Record<string, string>>): LocalePack;
