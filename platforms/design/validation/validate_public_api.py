#!/usr/bin/env python3
"""Validate Design Platform registry status and public export parity."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "platforms/design/specifications/design-platform-registry.json"
PACKAGES = ROOT / "platforms/design/implementation/packages"
BASELINE = ROOT / "platforms/design/implementation/release/public-api-baseline.json"
JS_EXPORT = re.compile(r"^export\s+(?:async\s+)?(?:function|const|let|class)\s+([A-Za-z_$][\w$]*)", re.M)
DTS_EXPORT = re.compile(r"^export\s+(?:declare\s+)?(?:function|const|let|class)\s+([A-Za-z_$][\w$]*)", re.M)


def export_parity(name: str, directory: Path, errors: list[str]) -> None:
    """Runtime exports in src/index.js must match the declarations in src/index.d.ts."""
    js, dts = directory / "src/index.js", directory / "src/index.d.ts"
    if not js.is_file() or not dts.is_file():
        return
    runtime = set(JS_EXPORT.findall(js.read_text(encoding="utf-8")))
    declared = set(DTS_EXPORT.findall(dts.read_text(encoding="utf-8")))
    for missing in sorted(declared - runtime):
        errors.append(f"{name}: declared in index.d.ts but not exported by index.js: {missing}")
    for missing in sorted(runtime - declared):
        errors.append(f"{name}: exported by index.js but not declared in index.d.ts: {missing}")


def main() -> int:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    errors: list[str] = []

    for package in registry["packages"]:
        name = package["name"]
        status = package["status"]
        expected = package["publicApi"]
        directory = PACKAGES / name.removeprefix("@menq/")
        manifest_path = directory / "package.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        exports = manifest.get("exports") or {}
        actual = list(exports.keys())

        if status == "Preview" and not expected:
            errors.append(f"Preview package {name} must declare a public API")
        if status in {"Planned", "Skeleton"} and expected:
            errors.append(f"{status} package {name} may not claim a public API")
        if actual != expected:
            errors.append(f"public API drift for {name}: registry={expected}, manifest={actual}")

        export_parity(name, directory, errors)

        for export_name, target in exports.items():
            candidates: list[str] = []
            if isinstance(target, str):
                candidates.append(target)
            elif isinstance(target, dict):
                candidates.extend(value for value in target.values() if isinstance(value, str))
            else:
                errors.append(f"unsupported export target for {name} {export_name}")
                continue
            for candidate in candidates:
                path = directory / candidate
                if not path.is_file():
                    errors.append(f"missing public export target for {name} {export_name}: {candidate}")

    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    if not baseline.get("packages"):
        errors.append("public API baseline is empty: breaking-change detection cannot work")
    else:
        registered = {p["name"] for p in registry["packages"]}
        for gone in sorted(set(baseline["packages"]) - registered):
            errors.append(f"package {gone} is in the public API baseline but no longer registered (breaking)")

    if errors:
        print("DESIGN PLATFORM PUBLIC API VALIDATION: RED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("DESIGN PLATFORM PUBLIC API VALIDATION: GREEN")
    print("Registry package states and public exports are synchronized.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
