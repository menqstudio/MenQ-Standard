#!/usr/bin/env python3
"""Build the MenQ brand expression token outputs (D-027) from the canonical source.

Reads  source/brand-tokens.source.json
Writes tokens.css   — CSS custom properties for consumers
       tokens.json  — design-tool mirror (claude.ai Design System format)

Both outputs are generated and non-canonical. `--check` fails if either is out of date.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/brand-tokens.source.json"
OUT_CSS = ROOT / "tokens.css"
OUT_JSON = ROOT / "tokens.json"
LAYER_ORDER = {"Reference": 0, "Semantic": 1, "Component": 2, "Pattern": 3, "Product Extension": 4}
MODES = ("light", "dark")
HEADER = "/* MenQ brand expression (D-027) — GENERATED from source/brand-tokens.source.json. Do not edit. */"


def fail(errors: list[str]) -> int:
    print("BRAND TOKENS: RED")
    for error in errors:
        print("- " + error)
    return 1


def entry_of(token: dict, mode: str) -> dict:
    if "modes" in token:
        return token["modes"][mode]
    return {key: token[key] for key in ("value", "reference") if key in token}


def check(source: dict) -> list[str]:
    errors: list[str] = []
    by_id: dict[str, dict] = {}
    css_names: set[str] = set()
    for token in source["tokens"]:
        if token["id"] in by_id:
            errors.append(f"duplicate token id {token['id']}")
        by_id[token["id"]] = token
        if token["cssName"] in css_names:
            errors.append(f"duplicate cssName {token['cssName']}")
        css_names.add(token["cssName"])
        prefix = token["id"].split(".")[3]
        expected = {"reference": "Reference", "semantic": "Semantic", "component": "Component", "pattern": "Pattern", "product-extension": "Product Extension"}[prefix]
        if token["layer"] != expected:
            errors.append(f"{token['id']}: layer {token['layer']} does not match id prefix")
        for lang in ("hy", "en"):
            if not token["description"].get(lang, "").strip():
                errors.append(f"{token['id']}: missing {lang} description")
    for token in source["tokens"]:
        for mode in MODES:
            entry = entry_of(token, mode)
            ref = entry.get("reference")
            if ref is None:
                continue
            target = by_id.get(ref)
            if target is None:
                errors.append(f"{token['id']}: unresolved reference {ref}")
                continue
            if LAYER_ORDER[target["layer"]] >= LAYER_ORDER[token["layer"]]:
                errors.append(f"{token['id']}: invalid dependency direction to {ref}")
            if target["type"] != token["type"]:
                errors.append(f"{token['id']}: type mismatch with {ref}")
    for style in source["typeStyles"]:
        for lang in ("hy", "en"):
            if not style["description"].get(lang, "").strip():
                errors.append(f"type style {style['name']}: missing {lang} description")
    for font in source["fonts"]:
        if not (ROOT / font["file"]).is_file():
            errors.append(f"missing font file {font['file']}")
    return errors


def css_value(entry: dict, by_id: dict[str, dict]) -> str:
    if "reference" in entry:
        return f"var(--{by_id[entry['reference']]['cssName']})"
    return str(entry["value"])


def build_css(source: dict) -> str:
    by_id = {token["id"]: token for token in source["tokens"]}
    themed = [t for t in source["tokens"] if t["type"] in ("color", "shadow")]
    rooted = [t for t in source["tokens"] if t["type"] not in ("color", "shadow")]
    lines = [HEADER, ':root, [data-theme="light"] {']
    lines += [f"  --{t['cssName']}: {css_value(entry_of(t, 'light'), by_id)};" for t in themed]
    # .section-contrast is a dark scope in both themes. Tokens whose value is a var() are re-declared
    # so they resolve against the scope instead of inheriting a value computed at :root.
    lines += ["}", '[data-theme="dark"], .section-contrast {']
    lines += [f"  --{t['cssName']}: {css_value(entry_of(t, 'dark'), by_id)};" for t in themed if "modes" in t or "reference" in t]
    lines += ["}", ":root {"]
    lines += [f"  --{t['cssName']}: {css_value(entry_of(t, 'light'), by_id)};" for t in rooted]
    lines += ["}"]
    for style in source["typeStyles"]:
        props = [f"font-family: var(--font-{style['family']})", f"font-size: {style['fontSize']}", f"line-height: {style['lineHeight']}", f"font-weight: {style['fontWeight']}"]
        if "letterSpacing" in style:
            props.append(f"letter-spacing: {style['letterSpacing']}")
        lines.append(f".{style['name']} {{ {'; '.join(props)}; }}")
    for font in source["fonts"]:
        lines.append(f'@font-face {{ font-family: "{font["family"]}"; src: url("{font["file"]}") format("woff2"); font-weight: {font["weight"]}; font-style: {font["style"]}; font-display: swap; }}')
    return "\n".join(lines) + "\n"


def mirror_value(entry: dict, by_id: dict[str, dict]):
    if "reference" in entry:
        return "{" + by_id[entry["reference"]]["cssName"] + "}"
    return entry["value"]


def build_mirror(source: dict) -> str:
    by_id = {token["id"]: token for token in source["tokens"]}
    def item(token: dict) -> dict:
        if "modes" in token:
            value = {mode: mirror_value(token["modes"][mode], by_id) for mode in MODES}
        else:
            value = mirror_value(entry_of(token, "light"), by_id)
        return {"name": token["cssName"], "value": value, "usage": token["description"]["en"]}
    families = {"dimension": None}
    group = lambda pred: {"tokens": [item(t) for t in source["tokens"] if pred(t)]}
    css = lambda t: t["cssName"]
    mirror = {
        "name": "MenQ",
        "version": 3,
        "color": {"themes": [{"id": "light", "name": "Light"}, {"id": "dark", "name": "Dark"}], "tokens": [item(t) for t in source["tokens"] if t["type"] == "color"]},
        "type": {
            "fonts": source["fonts"],
            "families": {css(t)[len("font-"):]: t["value"] for t in source["tokens"] if t["type"] == "font-family"},
            "groups": [],
        },
        "spacing": group(lambda t: css(t).startswith("space-")),
        "radius": group(lambda t: css(t).startswith("radius-")),
        "shadow": group(lambda t: t["type"] == "shadow"),
        "size": group(lambda t: t["type"] == "dimension" and not css(t).startswith(("space-", "radius-"))),
        "zIndex": group(lambda t: css(t).startswith("z-")),
        "opacity": group(lambda t: css(t).startswith("opacity-")),
        "meta": {"source": "github", "repo": "menqstudio/MenQ-Standard", "path": "platforms/design/brand-expression/source/brand-tokens.source.json", "decision": "D-027"},
    }
    del families
    groups: dict[str, list] = {}
    for style in source["typeStyles"]:
        entry = {k: style[k] for k in ("name", "fontSize", "lineHeight", "fontWeight") }
        if "letterSpacing" in style:
            entry["letterSpacing"] = style["letterSpacing"]
        entry["usage"] = style["description"]["en"]
        groups.setdefault((style["group"], style["family"]), []).append(entry)
    mirror["type"]["groups"] = [{"name": g, "family": f, "styles": s} for (g, f), s in groups.items()]
    return json.dumps(mirror, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    mode_check = "--check" in sys.argv[1:]
    try:
        source = json.loads(SOURCE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return fail([f"cannot read source: {exc}"])
    errors = check(source)
    if errors:
        return fail(errors)
    outputs = {OUT_CSS: build_css(source), OUT_JSON: build_mirror(source)}
    if mode_check:
        stale = [p.name for p, text in outputs.items() if not p.is_file() or p.read_text(encoding="utf-8") != text]
        if stale:
            return fail([f"{name} is out of date — run build_brand_tokens.py" for name in stale])
    else:
        for path, text in outputs.items():
            with path.open("w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
    print(f"BRAND TOKENS: GREEN ({len(source['tokens'])} tokens, {len(source['typeStyles'])} type styles)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
