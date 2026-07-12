#!/usr/bin/env python3
"""Validate and deterministically compile the MenQ Design Platform token source."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[1]
SOURCE = WORKSPACE / "packages/design-tokens/source/tokens.json"
OUTPUT = WORKSPACE / "packages/design-tokens/generated"
TOKEN_ID = re.compile(r"^menq\.design\.token\.(reference|semantic|component|pattern|product-extension)\.[a-z0-9.-]+$")
LAYER_ORDER = {
    "Reference": 0,
    "Semantic": 1,
    "Component": 2,
    "Pattern": 3,
    "Product Extension": 4,
}


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def css_name(token_id: str) -> str:
    return "--" + token_id.replace("menq.design.token.", "menq-").replace(".", "-")


def resolve(token_id: str, by_id: dict[str, dict], stack: list[str]) -> str | int | float:
    if token_id in stack:
        raise ValueError("token reference cycle: " + " -> ".join(stack + [token_id]))
    token = by_id[token_id]
    if "value" in token:
        return token["value"]
    reference = token.get("reference")
    if reference not in by_id:
        raise ValueError(f"unresolved token reference {reference!r} from {token_id!r}")
    if LAYER_ORDER[by_id[reference]["layer"]] >= LAYER_ORDER[token["layer"]]:
        raise ValueError(f"invalid dependency direction {token_id!r} -> {reference!r}")
    if by_id[reference]["type"] != token["type"]:
        raise ValueError(f"token type mismatch {token_id!r} -> {reference!r}")
    return resolve(reference, by_id, stack + [token_id])


def main() -> int:
    errors: list[str] = []
    try:
        source = json.loads(SOURCE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"TOKEN BUILD: RED\n- cannot read token source: {exc}")
        return 1

    if source.get("schemaVersion") != 1:
        errors.append("schemaVersion must be 1")
    if source.get("decision") != "D-025":
        errors.append("decision must be D-025")
    if source.get("canonicalLanguages") != ["hy", "en"]:
        errors.append("canonicalLanguages must be [hy, en]")
    if source.get("generatedOutputsAreCanonical") is not False:
        errors.append("generatedOutputsAreCanonical must be false")

    tokens = source.get("tokens")
    if not isinstance(tokens, list) or not tokens:
        errors.append("tokens must be a non-empty list")
        tokens = []

    by_id: dict[str, dict] = {}
    for token in tokens:
        if not isinstance(token, dict):
            errors.append("every token must be an object")
            continue
        token_id = token.get("id")
        if not isinstance(token_id, str) or not TOKEN_ID.fullmatch(token_id):
            errors.append(f"invalid token id: {token_id!r}")
            continue
        if token_id in by_id:
            errors.append(f"duplicate token id: {token_id}")
        by_id[token_id] = token
        if token.get("layer") not in LAYER_ORDER:
            errors.append(f"invalid layer for {token_id}")
        description = token.get("description")
        if not isinstance(description, dict) or not description.get("hy") or not description.get("en"):
            errors.append(f"bilingual description missing for {token_id}")
        has_value = "value" in token
        has_reference = "reference" in token
        if has_value == has_reference:
            errors.append(f"{token_id} must define exactly one of value or reference")
        if token.get("layer") == "Reference" and has_reference:
            errors.append(f"Reference token may not reference another token: {token_id}")

    resolved: dict[str, str | int | float] = {}
    if not errors:
        for token_id in sorted(by_id):
            try:
                resolved[token_id] = resolve(token_id, by_id, [])
            except ValueError as exc:
                errors.append(str(exc))

    if errors:
        print("TOKEN BUILD: RED")
        for error in errors:
            print(f"- {error}")
        return 1

    OUTPUT.mkdir(parents=True, exist_ok=True)
    resolved_text = canonical_json({"schemaVersion": 1, "sourceId": source["sourceId"], "tokens": resolved})
    css_lines = [":root {"]
    for token_id in sorted(resolved):
        css_lines.append(f"  {css_name(token_id)}: {resolved[token_id]};")
    css_lines.append("}")
    css_text = "\n".join(css_lines) + "\n"
    js_text = "export const tokens = Object.freeze(" + json.dumps(resolved, ensure_ascii=False, sort_keys=True) + ");\n"
    dts_text = "export declare const tokens: Readonly<Record<string, string | number>>;\n"

    artifacts = {
        "tokens.resolved.json": resolved_text.encode("utf-8"),
        "tokens.css": css_text.encode("utf-8"),
        "tokens.js": js_text.encode("utf-8"),
        "tokens.d.ts": dts_text.encode("utf-8"),
    }
    for name, data in artifacts.items():
        (OUTPUT / name).write_bytes(data)

    source_bytes = SOURCE.read_bytes()
    manifest = {
        "schemaVersion": 1,
        "source": str(SOURCE.relative_to(WORKSPACE)).replace("\\", "/"),
        "sourceSha256": sha256_bytes(source_bytes),
        "tokenCount": len(resolved),
        "artifacts": [
            {"path": name, "bytes": len(data), "sha256": sha256_bytes(data)}
            for name, data in sorted(artifacts.items())
        ],
        "generatedOutputsAreCanonical": False,
    }
    (OUTPUT / "manifest.json").write_text(canonical_json(manifest), encoding="utf-8")

    print("TOKEN BUILD: GREEN")
    print(f"Compiled {len(resolved)} tokens into {len(artifacts)} deterministic artifacts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
