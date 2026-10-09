#!/usr/bin/env python3
"""Validate the MenQ brand expression layer and product extensions (D-027)."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRAND = ROOT / "platforms/design/brand-expression"
EXT = ROOT / "platforms/design/product-extensions"
BRO = EXT / "bro"
SOURCE = BRAND / "source/brand-tokens.source.json"
SCHEMA = BRAND / "source/brand-token-source.schema.json"
GENERATOR = BRAND / "scripts/build_brand_tokens.py"
REGISTRY = ROOT / "platforms/design/specifications/design-platform-registry.json"
DECISION_INDEX = ROOT / "DECISION_INDEX.md"
DECISION = ROOT / "platforms/design/decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md"
PRODUCT_COMPONENTS = {"Timeline", "ChatMessage", "AgentCard", "ApprovalCard", "CommandComposer"}
FORBIDDEN_CLAIMS = [
    (re.compile(r"canonical live copy", re.I), "a design tool must not be named as the canonical copy"),
    (re.compile(r"\(`ru`\)\s+are equal", re.I), "Russian is a locale pack, not an equal canonical language"),
]
VAR_USE = re.compile(r"var\(\s*(--[A-Za-z0-9_-]+)\s*[,)]")
VAR_DEF = re.compile(r"(--[A-Za-z0-9_-]+)\s*:")
HEADER = re.compile(r"^/\* @ds-bundle: (\{.*?\}) \*/", re.S)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read {path.relative_to(ROOT)}: {exc}")
        return None


def check_schema(errors: list[str]) -> None:
    source, schema = load_json(SOURCE, errors), load_json(SCHEMA, errors)
    if source is None or schema is None:
        return
    try:
        import jsonschema
    except ImportError:
        errors.append("jsonschema is required (pip install jsonschema)")
        return
    for error in sorted(jsonschema.Draft202012Validator(schema).iter_errors(source), key=lambda e: list(e.path)):
        errors.append(f"token source schema: {'/'.join(map(str, error.path))}: {error.message}")


def check_generated(errors: list[str]) -> None:
    result = subprocess.run([sys.executable, str(GENERATOR), "--check"], capture_output=True, text=True)
    if result.returncode != 0:
        errors.append("generated outputs: " + (result.stdout + result.stderr).strip().replace("\n", " | "))


def bundle_header(path: Path, errors: list[str]) -> list[str]:
    match = HEADER.match(path.read_text(encoding="utf-8"))
    if not match:
        errors.append(f"{path.relative_to(ROOT)}: missing @ds-bundle header")
        return []
    return [c["name"] for c in json.loads(match.group(1))["components"]]


def check_components(errors: list[str]) -> None:
    core = bundle_header(BRAND / "components/bundle.js", errors)
    bro = bundle_header(BRO / "components/bro.bundle.js", errors)
    leaked = PRODUCT_COMPONENTS & set(core)
    if leaked:
        errors.append(f"product components in the shared core bundle: {sorted(leaked)}")
    for name in PRODUCT_COMPONENTS:
        if (BRAND / "components" / name).exists():
            errors.append(f"product component folder in the shared core: {name}")
    for base, names in ((BRAND / "components", core), (BRO / "components", bro)):
        for name in names:
            for required in ("README.md", "preview.html"):
                if not (base / name / required).is_file():
                    errors.append(f"{(base / name / required).relative_to(ROOT)} is missing")
        for folder in sorted(p for p in base.iterdir() if p.is_dir()):
            if folder.name not in names and folder.name != "Cover":
                errors.append(f"{folder.relative_to(ROOT)} is not listed in its bundle header")
    if shutil.which("node"):
        for js in (BRAND / "components/bundle.js", BRO / "components/bro.bundle.js"):
            result = subprocess.run(["node", "--check", str(js)], capture_output=True, text=True)
            if result.returncode != 0:
                errors.append(f"{js.relative_to(ROOT)}: syntax error: {result.stderr.strip().splitlines()[-1]}")


def check_vars(errors: list[str]) -> None:
    defined: set[str] = set()
    for css in (BRAND / "tokens.css", BRAND / "components/bundle.css", BRO / "components/bro.css"):
        defined |= set(VAR_DEF.findall(css.read_text(encoding="utf-8")))
    files = [BRAND / "components/bundle.css", BRO / "components/bro.css", BRAND / "tokens.css"]
    files += sorted(BRAND.glob("components/*/preview.html")) + sorted(BRO.glob("components/*/preview.html"))
    for path in files:
        for name in sorted(set(VAR_USE.findall(path.read_text(encoding="utf-8")))):
            if name not in defined:
                errors.append(f"{path.relative_to(ROOT)}: unresolved {name}")


def check_markdown(errors: list[str]) -> None:
    for md in sorted(list(BRAND.rglob("*.md")) + list(EXT.rglob("*.md"))):
        text = md.read_text(encoding="utf-8")
        rel = md.relative_to(ROOT)
        if "## Հայերեն" not in text or "## English" not in text:
            errors.append(f"{rel}: missing '## Հայերեն' or '## English' section")
        if not re.search(r"<!-- END: [A-Z0-9_-]+ -->\s*$", text):
            errors.append(f"{rel}: missing END marker")
        for pattern, why in FORBIDDEN_CLAIMS:
            if pattern.search(text):
                errors.append(f"{rel}: {why}")
        if "## Հայերեն" in text and "## English" in text:
            hy = text.split("## Հայերեն", 1)[1].split("## English", 1)[0]
            if not re.search(r"[Ա-և]", hy):
                errors.append(f"{rel}: Armenian section has no Armenian text")


def check_assets(errors: list[str]) -> None:
    required = {"id", "kind", "file", "description", "ownerId", "provenance", "license", "lifecycle", "sha256"}
    for base, scan in ((BRAND, ["assets/**/*", "fonts/*.woff2"]), (BRO, ["assets/**/*"])):
        doc = load_json(base / "assets/ASSET_RECORDS.json", errors)
        if doc is None:
            continue
        records = {r.get("file"): r for r in doc.get("records", [])}
        for record in records.values():
            missing = required - set(record)
            if missing:
                errors.append(f"asset record {record.get('id')}: missing {sorted(missing)}")
                continue
            path = base / record["file"]
            if not path.is_file():
                errors.append(f"asset record {record['id']}: file {record['file']} not found")
            elif sha256(path) != record["sha256"]:
                errors.append(f"asset record {record['id']}: sha256 mismatch")
            if set(record["description"]) != {"hy", "en"}:
                errors.append(f"asset record {record['id']}: description must be hy/en")
        for pattern in scan:
            for path in base.glob(pattern):
                if path.is_file() and path.suffix not in (".md", ".json") and str(path.relative_to(base)) not in records:
                    errors.append(f"{path.relative_to(ROOT)} has no asset record")


def check_governance(errors: list[str]) -> None:
    if not DECISION.is_file():
        errors.append("D-027 decision record is missing")
    if "D-027" not in DECISION_INDEX.read_text(encoding="utf-8"):
        errors.append("D-027 is not in DECISION_INDEX.md")
    registry = load_json(REGISTRY, errors) or {}
    ids = {s.get("id") for s in registry.get("specifications", [])}
    for spec in ("menq.design.spec.brand-expression.v1", "menq.design.spec.product-extension.bro.v1"):
        if spec not in ids:
            errors.append(f"registry is missing {spec}")
    if (ROOT / "platforms/design/menq-design-system").exists():
        errors.append("legacy platforms/design/menq-design-system/ must not exist")


# WCAG 2.1 AA text pairs (4.5:1) that every theme must satisfy. A token change that breaks one is RED.
CONTRAST_PAIRS = [(f, b) for f in ("color-content-primary", "color-content-secondary", "color-content-muted")
                  for b in ("color-page-bg", "color-surface-primary", "color-surface-secondary")] + [
    ("color-content-inverse", "color-action-primary"), ("color-content-inverse", "color-surface-inverse"),
    ("color-action-primary-strong", "color-page-bg"), ("color-action-primary-strong", "color-surface-primary"),
    ("color-accent-text", "color-page-bg"), ("color-success-text", "color-page-bg"),
    ("color-warning-text", "color-page-bg"), ("color-danger-text", "color-page-bg"),
]


THRESHOLD = 4.5


class Unresolved(ValueError):
    """A colour, a custom property or a gradient stop that cannot be reduced to one opaque sRGB colour."""


def shown(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def token_resolver(source: dict):
    by_id = {t["id"]: t for t in source["tokens"]}
    by_css = {t["cssName"]: t for t in source["tokens"]}

    def resolve(key: str, mode: str, depth: int = 0) -> str:
        token = by_css.get(key) or by_id[key]
        entry = token["modes"][mode] if "modes" in token else token
        if "reference" in entry:
            if depth > 8:
                raise ValueError(f"reference loop at {key}")
            return resolve(entry["reference"], mode, depth + 1)
        return entry["value"]

    return resolve


def rgba(value: str) -> tuple[float, float, float, float]:
    value = value.strip()
    if re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        return tuple(int(value[i:i + 2], 16) for i in (1, 3, 5)) + (1.0,)
    match = re.fullmatch(r"rgba?\(([^)]*)\)", value)
    if not match:
        raise Unresolved(f"unsupported color {value!r}")
    try:
        parts = [float(x) for x in re.split(r"[,\s/]+", match.group(1).strip()) if x]
    except ValueError:
        raise Unresolved(f"unsupported color {value!r}") from None
    if len(parts) not in (3, 4):
        raise Unresolved(f"unsupported color {value!r}")
    return (parts[0], parts[1], parts[2], parts[3] if len(parts) > 3 else 1.0)


def luminance(c) -> float:
    def channel(x: float) -> float:
        x /= 255
        return x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    return 0.2126 * channel(c[0]) + 0.7152 * channel(c[1]) + 0.0722 * channel(c[2])


def contrast_ratio(fg, bg) -> float:
    """WCAG 2.1 contrast of a foreground (its alpha composited over the background) on an opaque background."""
    a = fg[3]
    fg = tuple(fg[i] * a + bg[i] * (1 - a) for i in range(3))
    hi, lo = sorted([luminance(fg), luminance(bg)], reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def check_contrast(errors: list[str], source_path: Path = SOURCE) -> None:
    source = load_json(source_path, errors)
    if source is None:
        return
    resolve = token_resolver(source)
    for mode in ("light", "dark"):
        for fg_name, bg_name in CONTRAST_PAIRS:
            try:
                bg = rgba(resolve(bg_name, mode))
                fg = rgba(resolve(fg_name, mode))
            except (KeyError, ValueError) as exc:
                errors.append(f"contrast {mode} {fg_name} on {bg_name}: {exc}")
                continue
            ratio = contrast_ratio(fg, bg)
            if ratio < THRESHOLD:
                errors.append(f"contrast {mode}: {fg_name} on {bg_name} is {ratio:.2f}:1 (< 4.5:1, WCAG AA)")


# --- Text painted over a surface in the component stylesheets (CR-0013) ----------------------------
# The 17 pairs above are a list somebody wrote, and a list cannot name a pair nobody thought of: the
# primary Button put white text on gradient-brand, whose cyan end is 2.43:1 in Light, and all 34
# checks were GREEN.  This check reads the stylesheets instead.  For every rule that paints a
# background under a foreground colour it resolves both through the token source, in every theme
# scope, and requires 4.5:1.  A gradient is held to the threshold at EVERY colour stop; a stop it
# cannot reduce to one opaque colour is RED, never skipped.
SURFACE_CSS = (BRAND / "components/bundle.css", BRO / "components/bro.css")
# How the stylesheets address a theme.  tokens.css: ':root, [data-theme="light"]' holds the light
# values and '[data-theme="dark"], .section-contrast' the dark ones; bundle.css re-evaluates its
# derived properties under ':root, [data-theme], .section-contrast'.  Each scope is (token mode,
# selectors that match the theme root, selectors of a nested scope whose declarations win inside it).
THEME_SCOPES = {
    "light": ("light", (":root", "[data-theme]", '[data-theme="light"]'), ()),
    "dark": ("dark", (":root", "[data-theme]", '[data-theme="dark"]'), ()),
    "section-contrast": ("dark", (":root", "[data-theme]", '[data-theme="light"]'), (".section-contrast",)),
}
NESTING_AT_RULES = ("@media", "@supports", "@layer", "@container")
BACKGROUND_PROPERTIES = ("background", "background-image", "background-color")
STATE = re.compile(r":(?:hover|active|focus-visible|focus-within|focus|visited|disabled|checked)(?![\w-])")
GRADIENT = re.compile(r"(?:repeating-)?(?:linear|radial|conic)-gradient\(")
GEOMETRY = re.compile(
    r"(?:to|at|from|in|circle|ellipse|top|bottom|left|right|center|srgb|closest-side|closest-corner|farthest-side|farthest-corner"
    r"|[-+]?(?:\d+\.?\d*|\.\d+)(?:deg|grad|rad|turn|%|px|rem|em|vw|vh)?)"
)
NAMED_COLORS = {"white": "#ffffff", "black": "#000000"}


def split_top(text: str, separator: str) -> list[str]:
    """Split on a separator (',' ';' or ' ' for runs of whitespace) that is outside every parenthesis."""
    parts, depth, current = [], 0, []
    for char in text:
        depth += (char == "(") - (char == ")")
        if depth == 0 and (char.isspace() if separator == " " else char == separator):
            parts.append("".join(current))
            current = []
        else:
            current.append(char)
    parts.append("".join(current))
    return [part.strip() for part in parts if part.strip()]


def closing(text: str, opened: int) -> int:
    """Index just past the ')' that closes the '(' at ``opened``."""
    depth = 0
    for index in range(opened, len(text)):
        depth += (text[index] == "(") - (text[index] == ")")
        if depth == 0:
            return index + 1
    raise Unresolved(f"unbalanced parentheses in {text!r}")


def normal(selector: str) -> str:
    return re.sub(r"\s+", " ", selector.replace("'", '"')).strip()


def parse_css(text: str) -> list[tuple[str, list[tuple[str, str]]]]:
    """(selector, declarations) in source order, one entry per selector of a selector list."""
    text = re.sub(r"/\*.*?\*/", " ", text, flags=re.S)
    if re.search(r"""(["'])[^"'\n]*[{};][^"'\n]*\1""", text):
        raise ValueError("a string holding '{', '}' or ';' is not supported by this parser")
    rules: list[tuple[str, list[tuple[str, str]]]] = []

    def walk(chunk: str) -> None:
        index = 0
        while True:
            opened = chunk.find("{", index)
            if opened < 0:
                if "}" in chunk[index:]:
                    raise ValueError("unbalanced braces")
                return
            prelude = chunk[index:opened].rsplit(";", 1)[-1].strip()
            depth, end = 1, opened + 1
            while end < len(chunk) and depth:
                depth += (chunk[end] == "{") - (chunk[end] == "}")
                end += 1
            if depth or "}" in prelude:
                raise ValueError("unbalanced braces")
            body = chunk[opened + 1:end - 1]
            index = end
            if prelude.startswith("@"):
                if prelude.split()[0].lower() in NESTING_AT_RULES:
                    walk(body)
                continue  # @keyframes, @font-face: no selector paints text over a surface
            declarations = []
            for declaration in split_top(body, ";"):
                name, colon, value = declaration.partition(":")
                if not colon:
                    raise ValueError(f"declaration without ':' in {prelude!r}: {declaration!r}")
                name = name.strip()
                declarations.append((name if name.startswith("--") else name.lower(), value.strip()))
            for selector in split_top(prelude, ","):
                rules.append((normal(selector), declarations))

    walk(text)
    return rules


def expand(value: str, lookup, depth: int = 0) -> str:
    """Replace every var() that ``lookup`` knows.  ``lookup`` returns the value, None to leave the
    var() as written, or raises Unresolved."""
    if depth > 16:
        raise Unresolved(f"custom-property loop at {value!r}")
    out, index = [], 0
    while True:
        start = value.find("var(", index)
        if start < 0:
            return "".join(out) + value[index:]
        end = closing(value, start + 3)
        name, _, fallback = value[start + 4:end - 1].partition(",")
        found = lookup(name.strip(), fallback.strip() or None)
        out.append(value[index:start])
        out.append(value[start:end] if found is None else expand(found, lookup, depth + 1))
        index = end


def css_color(text: str) -> tuple[float, float, float, float]:
    """One sRGB colour written out in full: #rgb, #rrggbb, rgb(), rgba(), white or black.  Anything else is Unresolved."""
    text = NAMED_COLORS.get(text.strip().lower(), text.strip())
    if re.fullmatch(r"#[0-9a-fA-F]{3}", text):
        text = "#" + "".join(char * 2 for char in text[1:])
    return rgba(text)


def opaque(text: str) -> tuple[float, float, float, float]:
    """A colour that hides what is under it; a translucent one is Unresolved, because the backdrop is not known."""
    color = css_color(text)
    if color[3] < 1:
        raise Unresolved(f"{text} is translucent (alpha {color[3]:g}) and what lies under it is not known")
    return color


def gradient_stops(gradient: str) -> list[str]:
    """The colour-stop arguments of one gradient function; its direction, shape and hints are not stops."""
    arguments = split_top(gradient[gradient.index("(") + 1:-1], ",")
    stops = [a for a in arguments if not all(GEOMETRY.fullmatch(word) for word in split_top(a, " "))]
    if not stops:
        raise Unresolved(f"no colour stop found in {gradient}")
    return stops


def check_surface_contrast(errors: list[str], css_paths=SURFACE_CSS, source_path: Path = SOURCE) -> dict[str, int]:
    counts = {"gradient_stops": 0, "solid": 0, "translucent": 0, "decorative": 0}
    source = load_json(source_path, errors)
    if source is None:
        return counts
    resolve = token_resolver(source)
    rules: list[tuple[Path, str, list[tuple[str, str]]]] = []
    for path in css_paths:
        try:
            rules += [(path, selector, declarations) for selector, declarations in parse_css(path.read_text(encoding="utf-8"))]
        except (OSError, ValueError) as exc:
            errors.append(f"surface contrast: cannot parse {shown(path)}: {exc}")
            return counts
    foreground: dict[str, str] = {}
    for _, selector, declarations in rules:
        for name, value in declarations:
            if name == "color":
                foreground[selector] = value

    def environment(scope: str):
        mode, roots, nested = THEME_SCOPES[scope]
        custom: dict[str, str] = {}
        for matching in (roots, nested):
            for _, selector, declarations in rules:
                if selector in matching:
                    custom.update((name, value) for name, value in declarations if name.startswith("--"))

        def derived(name: str, fallback: str | None) -> str | None:
            return custom.get(name)

        def everything(name: str, fallback: str | None) -> str:
            if name in custom:
                return custom[name]
            try:
                return str(resolve(name[2:], mode))
            except (KeyError, ValueError):
                if fallback is None:
                    raise Unresolved(f"var({name}) is not a token and no stylesheet defines it for this scope") from None
                return fallback

        return derived, everything

    environments = {scope: environment(scope) for scope in THEME_SCOPES}
    for path, selector, declarations in rules:
        painted = [(name, value) for name, value in declarations if name in BACKGROUND_PROPERTIES]
        if not painted:
            continue
        # The colour the cascade leaves on this selector; a state rule (:hover, :active ...) that sets
        # none paints under the text colour of its base rule.
        ink = foreground.get(selector) or foreground.get(normal(STATE.sub("", selector)))
        where = f"{selector} ({shown(path)})"
        for name, value in painted:
            # The derived properties are expanded first and the tokens second, so that a stop is
            # reported under the token it names: "var(--color-accent) = #06b6d4".
            shapes: dict[str, tuple[list[str], list[str]] | Unresolved] = {}
            for scope, (derived, _) in environments.items():
                try:
                    partly = expand(value, derived)
                    found = [partly[m.start():closing(partly, m.end() - 1)] for m in GRADIENT.finditer(partly)]
                    shapes[scope] = ([stop for gradient in found for stop in gradient_stops(gradient)], [partly])
                except Unresolved as exc:
                    shapes[scope] = exc
            is_gradient = any(isinstance(shape, Unresolved) or shape[0] for shape in shapes.values())
            if ink is None:
                counts["decorative"] += is_gradient
                continue
            for scope, shape in shapes.items():
                everything = environments[scope][1]
                if isinstance(shape, Unresolved):
                    errors.append(f"surface contrast {scope}: {where} {name}: cannot be resolved: {shape}")
                    continue
                stops, plain = shape
                try:
                    ink_color = css_color(expand(ink, everything))
                except Unresolved as exc:
                    if is_gradient:
                        errors.append(f"surface contrast {scope}: {where}: the foreground {ink} cannot be resolved: {exc}")
                    else:
                        counts["translucent"] += 1
                    continue
                for number, stop in enumerate(stops if stops else plain, 1):
                    label = f"gradient stop {number} {stop}" if stops else f"{name} {value}"
                    try:
                        words = split_top(expand(stop, everything), " ")
                        if any(not GEOMETRY.fullmatch(word) for word in words[1:]):
                            raise Unresolved(f"{stop!r} is not one colour with an optional position")
                        surface = opaque(words[0])
                    except Unresolved as exc:
                        if is_gradient:
                            errors.append(f"surface contrast {scope}: {where}: {label} cannot be resolved to one opaque colour: {exc}")
                        else:
                            counts["translucent"] += 1  # e.g. transparent, a tint: the backdrop is another rule's
                        continue
                    counts["gradient_stops" if stops else "solid"] += 1
                    ratio = contrast_ratio(ink_color, surface)
                    if ratio < THRESHOLD:
                        errors.append(
                            f"surface contrast {scope}: {where} paints color {ink} over {label} = "
                            f"{'#%02x%02x%02x' % tuple(round(x) for x in surface[:3])} at {ratio:.2f}:1 (< 4.5:1, WCAG AA)"
                        )
    return counts


def main() -> int:
    errors: list[str] = []
    surfaces: dict[str, int] = {}
    for check in (check_schema, check_generated, check_components, check_vars, check_contrast, check_surface_contrast, check_markdown, check_assets, check_governance):
        try:
            counted = check(errors)
        except Exception as exc:  # report, never traceback-green
            errors.append(f"{check.__name__} crashed: {exc!r}")
        else:
            if check is check_surface_contrast:
                surfaces = counted
    if errors:
        print("BRAND EXPRESSION VALIDATION: RED")
        for error in errors:
            print("- " + error)
        return 1
    print("BRAND EXPRESSION VALIDATION: GREEN")
    print(f"Validated token source schema, generated outputs, components, CSS variables, {len(CONTRAST_PAIRS) * 2} WCAG AA contrast pairs, bilingual docs, asset records and D-027 registration.")
    print(
        f"Text over a painted surface in the component stylesheets, in {len(THEME_SCOPES)} theme scopes ({', '.join(THEME_SCOPES)}): "
        f"{surfaces.get('gradient_stops', 0)} gradient colour stops and {surfaces.get('solid', 0)} solid fills at >= 4.5:1. "
        f"Not measured: {surfaces.get('translucent', 0)} fills that are transparent or translucent (the backdrop belongs to another rule) "
        f"and {surfaces.get('decorative', 0)} gradient declarations in rules that set no text colour."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
