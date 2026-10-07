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


def main() -> int:
    errors: list[str] = []
    for check in (check_schema, check_generated, check_components, check_vars, check_markdown, check_assets, check_governance):
        try:
            check(errors)
        except Exception as exc:  # report, never traceback-green
            errors.append(f"{check.__name__} crashed: {exc!r}")
    if errors:
        print("BRAND EXPRESSION VALIDATION: RED")
        for error in errors:
            print("- " + error)
        return 1
    print("BRAND EXPRESSION VALIDATION: GREEN")
    print("Validated token source schema, generated outputs, components, CSS variables, bilingual docs, asset records and D-027 registration.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
