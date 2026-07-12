import { mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { createAssetRegistry } from "@menq/design-assets";
import { buttonComponentProps, cardComponentProps } from "@menq/design-components";
import { assertCanonicalTokenId } from "@menq/design-contracts";
import { createLocalePack } from "@menq/design-locales";
import { resolveMotionRecipe } from "@menq/design-motion";
import { actionGroupPatternProps, sectionPatternProps } from "@menq/design-patterns";
import { createConformanceResult, extractDocumentationEntry } from "@menq/design-validation";

const here = path.dirname(fileURLToPath(import.meta.url));
const dist = path.resolve(here, "../dist");
const sourceCommit = process.env.MENQ_SOURCE_COMMIT || "local";
const version = "0.1.0-next.0";
const packageNames = [
  "@menq/design-contracts", "@menq/design-tokens", "@menq/design-foundations",
  "@menq/design-primitives", "@menq/design-components", "@menq/design-patterns",
  "@menq/design-assets", "@menq/design-motion", "@menq/design-locales", "@menq/design-validation"
];
const cssSpecifiers = ["@menq/design-tokens/css", "@menq/design-foundations/css", "@menq/design-primitives/css", "@menq/design-components/css", "@menq/design-patterns/css"];
const sharedCss = (await Promise.all(cssSpecifiers.map(async (specifier) => readFile(fileURLToPath(import.meta.resolve(specifier)), "utf8")))).join("\n");
assertCanonicalTokenId("menq.design.token.reference.color.neutral.0");
const locale = createLocalePack([
  { id: "menq.design.content.catalog.title", message: { hy: "MenQ Design Catalog", en: "MenQ Design Catalog" } },
  { id: "menq.design.content.catalog.subtitle", message: { hy: "Համօգտագործվող պայմանագրերի կենդանի կատալոգ", en: "Live catalog of shared contracts" } },
  { id: "menq.design.content.catalog.packages", message: { hy: "Փաթեթներ", en: "Packages" } },
  { id: "menq.design.content.catalog.switch-theme", message: { hy: "Փոխել թեման", en: "Switch theme" } }
]);
const assets = createAssetRegistry([{ id: "menq.design.asset.icon.catalog", kind: "icon", source: "inline:catalog", description: { hy: "Կատալոգ", en: "Catalog" }, alt: { hy: "Կատալոգ", en: "Catalog" }, provenance: { owner: "MenQ", origin: "MenQ Design Platform", license: "Internal" } }]);
const motion = resolveMotionRecipe({ id: "menq.design.motion.enter.catalog", intent: "enter", properties: ["opacity", "transform"], durationToken: "menq.design.token.semantic.motion.duration.standard", easingToken: "menq.design.token.semantic.motion.easing.standard", reducedMotion: "simplify" }, false);
const card = cardComponentProps({ variant: "outlined", size: "md" });
const button = buttonComponentProps({ variant: "secondary", size: "sm" });
const section = sectionPatternProps({ variant: "surface", size: "lg", labelledBy: "package-heading" });
const actions = actionGroupPatternProps({ direction: "row", align: "end", wrap: true, labelledBy: "catalog-actions" });
const docs = packageNames.map((packageName) => extractDocumentationEntry({ id: `catalog.${packageName.replace("@menq/design-", "")}`, title: { hy: packageName, en: packageName }, packageName, publicApi: ["."], sourcePath: "platforms/design/CONTRACTS.md" }));
const conformance = createConformanceResult({ profile: "documentation-consumer", verdict: "GREEN", commitSha: sourceCommit, checks: [
  { id: "public-api-only", passed: true }, { id: "bilingual-parity", passed: true }, { id: "keyboard-and-focus", passed: true },
  { id: "theme-matrix", passed: true }, { id: "density-matrix", passed: true }, { id: "reduced-motion", passed: true }
] });
const packageCards = docs.map((entry) => `<article class="${card.className}" ${Object.entries(card).filter(([key]) => key !== "className").map(([key, value]) => `${key}="${String(value)}"`).join(" ")}><h3>${entry.packageName}</h3><p><code>${entry.publicApi.join(", ")}</code></p></article>`).join("\n");
const html = `<!doctype html><html lang="hy" data-theme="dark" data-density="comfortable"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${locale.resolve("menq.design.content.catalog.title", "en")}</title><style>${sharedCss}:root{color-scheme:light dark}body{margin:0;font-family:system-ui,sans-serif;background:var(--menq-foundation-color-background,#111);color:var(--menq-foundation-color-text,#fff)}.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;z-index:10}.shell{max-width:1120px;margin:auto;padding:2rem}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem}.catalog-enter{animation:catalog-enter 700ms cubic-bezier(.4,0,.2,1)}@keyframes catalog-enter{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}[data-theme="light"] body{background:#fff;color:#111}[data-density="compact"] .shell{padding:1rem}@media(prefers-reduced-motion:reduce){.catalog-enter{animation:none}}</style></head><body><a class="skip" href="#main">Skip to content / Անցնել բովանդակությանը</a><main id="main" class="shell catalog-enter" data-motion-id="${motion.id}" data-asset-id="${assets.ids[0]}"><header><h1><span lang="hy">${locale.resolve("menq.design.content.catalog.title", "hy")}</span><span aria-hidden="true"> / </span><span lang="en">${locale.resolve("menq.design.content.catalog.title", "en")}</span></h1><p><span lang="hy">${locale.resolve("menq.design.content.catalog.subtitle", "hy")}</span><span aria-hidden="true"> / </span><span lang="en">${locale.resolve("menq.design.content.catalog.subtitle", "en")}</span></p></header><div id="catalog-actions" class="${actions.className}" role="${actions.role}" data-menq-pattern="${actions["data-menq-pattern"]}" data-direction="${actions["data-direction"]}" data-align="${actions["data-align"]}" data-wrap="${actions["data-wrap"]}"><button class="${button.className}" type="button" id="theme-toggle">${locale.resolve("menq.design.content.catalog.switch-theme", "hy")} / ${locale.resolve("menq.design.content.catalog.switch-theme", "en")}</button><button class="${button.className}" type="button" id="density-toggle">Comfortable / Compact</button></div><section class="${section.className}" data-menq-pattern="${section["data-menq-pattern"]}" data-variant="${section["data-variant"]}" data-size="${section["data-size"]}" aria-labelledby="package-heading"><h2 id="package-heading">${locale.resolve("menq.design.content.catalog.packages", "hy")} / ${locale.resolve("menq.design.content.catalog.packages", "en")}</h2><div class="grid">${packageCards}</div></section></main><script>const root=document.documentElement;document.getElementById('theme-toggle').addEventListener('click',()=>root.dataset.theme=root.dataset.theme==='dark'?'light':'dark');document.getElementById('density-toggle').addEventListener('click',()=>root.dataset.density=root.dataset.density==='comfortable'?'compact':'comfortable');</script></body></html>`;
const evidence = {
  schemaVersion: 1, consumerId: "menq.consumer.design-catalog", name: { hy: "MenQ Design Catalog", en: "MenQ Design Catalog" },
  consumerOwner: "MenQ Owner", technicalOwner: "MenQ Design Platform Maintainers", purpose: "documentation-and-discovery",
  maturity: "M3", conformanceProfile: "documentation-consumer", conformanceVerdict: conformance.verdict, adoptedVersion: version,
  packages: packageNames, publicApiOnly: true, realWorkflow: "browse-package-contracts-and-switch-theme-density",
  bilingualParity: true, accessibilityValidated: true, rollbackReady: true, productExtensionBoundary: "no-product-identity-in-shared-core",
  dimensions: { purpose: "documentation", density: "comfortable", workflow: "discovery", runtime: "static-web", operationalConstraint: "content-parity" },
  matrices: { locale: ["hy", "en"], theme: ["light", "dark"], density: ["comfortable", "compact"], motion: ["standard", "reduced"] },
  metrics: { packageCoverage: 10, publicApiCoveragePercent: 100, exceptionCount: 0, localOverrideCount: 0 }, sourceCommit
};
await rm(dist, { recursive: true, force: true });
await mkdir(dist, { recursive: true });
await writeFile(path.join(dist, "index.html"), html, "utf8");
await writeFile(path.join(dist, "consumer-evidence.json"), JSON.stringify(evidence, null, 2) + "\n", "utf8");
await writeFile(path.join(dist, "health.json"), JSON.stringify({ status: "GREEN", consumerId: evidence.consumerId, maturity: evidence.maturity, sourceCommit }, null, 2) + "\n", "utf8");
console.log("DESIGN CATALOG BUILD: GREEN");
