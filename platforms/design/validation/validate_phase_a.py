#!/usr/bin/env python3
"""Validate the MenQ Design Platform Phase A registry without external dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "platforms/design/specifications/design-platform-registry.json"
SCHEMA = ROOT / "platforms/design/specifications/design-platform-registry.schema.json"

REQUIRED_TOP_LEVEL = {
    "schemaVersion",
    "registryId",
    "decision",
    "status",
    "canonicalSource",
    "generatedOutputsAreCanonical",
    "owners",
    "specifications",
    "packages",
    "constraints",
}


def load_json(path: Path, errors: list[str]) -> dict:
    if not path.is_file():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(data, dict):
        errors.append(f"top-level JSON must be an object: {path.relative_to(ROOT)}")
        return {}
    return data


def detect_cycle(graph: dict[str, list[str]]) -> list[str] | None:
    state: dict[str, int] = {}
    stack: list[str] = []

    def visit(node: str) -> list[str] | None:
        marker = state.get(node, 0)
        if marker == 1:
            start = stack.index(node)
            return stack[start:] + [node]
        if marker == 2:
            return None
        state[node] = 1
        stack.append(node)
        for dependency in graph.get(node, []):
            cycle = visit(dependency)
            if cycle:
                return cycle
        stack.pop()
        state[node] = 2
        return None

    for node in graph:
        cycle = visit(node)
        if cycle:
            return cycle
    return None


def main() -> int:
    errors: list[str] = []
    registry = load_json(REGISTRY, errors)
    load_json(SCHEMA, errors)

    if registry:
        missing = REQUIRED_TOP_LEVEL - set(registry)
        if missing:
            errors.append(f"registry missing fields: {', '.join(sorted(missing))}")

        if registry.get("schemaVersion") != 1:
            errors.append("schemaVersion must be 1")
        if registry.get("decision") != "D-025":
            errors.append("decision must be D-025")
        if registry.get("status") != "Approved — Implementing":
            errors.append("status must remain Approved — Implementing")
        if registry.get("generatedOutputsAreCanonical") is not False:
            errors.append("generatedOutputsAreCanonical must be false")

        owners = registry.get("owners", [])
        owner_ids = [owner.get("ownerId") for owner in owners if isinstance(owner, dict)]
        if len(owner_ids) != len(set(owner_ids)):
            errors.append("owner IDs must be unique")
        if "owner.menq" not in owner_ids:
            errors.append("final MenQ Owner record is missing")

        specifications = registry.get("specifications", [])
        spec_ids = [spec.get("id") for spec in specifications if isinstance(spec, dict)]
        if len(spec_ids) != len(set(spec_ids)):
            errors.append("specification IDs must be unique")
        spec_id_set = set(spec_ids)

        spec_graph: dict[str, list[str]] = {}
        for spec in specifications:
            if not isinstance(spec, dict):
                errors.append("specification entry must be an object")
                continue
            spec_id = spec.get("id")
            owner_id = spec.get("ownerId")
            source_path = spec.get("sourcePath")
            if owner_id not in owner_ids:
                errors.append(f"unknown owner {owner_id!r} for specification {spec_id!r}")
            if not isinstance(source_path, str) or not (ROOT / source_path).is_file():
                errors.append(f"missing sourcePath for specification {spec_id!r}: {source_path!r}")
            dependencies = spec.get("dependencies", [])
            if not isinstance(dependencies, list):
                errors.append(f"dependencies must be a list for specification {spec_id!r}")
                dependencies = []
            for dependency in dependencies:
                if dependency not in spec_id_set:
                    errors.append(f"unresolved specification dependency {dependency!r} from {spec_id!r}")
            if isinstance(spec_id, str):
                spec_graph[spec_id] = dependencies

        spec_cycle = detect_cycle(spec_graph)
        if spec_cycle:
            errors.append("specification dependency cycle: " + " -> ".join(spec_cycle))

        packages = registry.get("packages", [])
        package_names = [package.get("name") for package in packages if isinstance(package, dict)]
        if len(package_names) != len(set(package_names)):
            errors.append("package names must be unique")
        package_set = set(package_names)

        package_graph: dict[str, list[str]] = {}
        for package in packages:
            if not isinstance(package, dict):
                errors.append("package entry must be an object")
                continue
            name = package.get("name")
            owner_id = package.get("ownerId")
            if owner_id not in owner_ids:
                errors.append(f"unknown owner {owner_id!r} for package {name!r}")
            dependencies = package.get("dependsOn", [])
            if not isinstance(dependencies, list):
                errors.append(f"dependsOn must be a list for package {name!r}")
                dependencies = []
            for dependency in dependencies:
                if dependency not in package_set:
                    errors.append(f"unresolved package dependency {dependency!r} from {name!r}")
            if isinstance(name, str):
                package_graph[name] = dependencies

        package_cycle = detect_cycle(package_graph)
        if package_cycle:
            errors.append("package dependency cycle: " + " -> ".join(package_cycle))

        constraints = registry.get("constraints", {})
        expected_constraints = {
            "productNeutralCore": True,
            "canonicalLanguages": ["hy", "en"],
            "noPrivateDeepImports": True,
            "twoConsumerValidationRequired": True,
            "ownerApprovalRequiredForMergeAndLock": True,
        }
        for key, expected in expected_constraints.items():
            if constraints.get(key) != expected:
                errors.append(f"constraint {key} must equal {expected!r}")

        if not any(package.get("status") == "Skeleton" for package in packages if isinstance(package, dict)):
            errors.append("at least one package boundary must be in Skeleton state")
        if any(package.get("status") == "Stable" for package in packages if isinstance(package, dict)):
            errors.append("Phase A may not claim Stable packages")

    if errors:
        print("DESIGN PLATFORM PHASE A VALIDATION: RED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("DESIGN PLATFORM PHASE A VALIDATION: GREEN")
    print(f"Validated {len(registry['owners'])} owners, {len(registry['specifications'])} specifications, and {len(registry['packages'])} package boundaries.")
    print("Implementation/package readiness: YELLOW (expected until package and consumer evidence exist).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
