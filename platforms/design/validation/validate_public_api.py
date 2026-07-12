#!/usr/bin/env python3
"""Validate Design Platform registry status and public export parity."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "platforms/design/specifications/design-platform-registry.json"
PACKAGES = ROOT / "platforms/design/implementation/packages"


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
