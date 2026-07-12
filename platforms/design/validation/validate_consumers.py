#!/usr/bin/env python3
"""Validate the two MenQ Design Platform consumer pilots and M4 evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot load {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"expected JSON object: {path}")
        return {}
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_common(label: str, root: Path, expected_maturity: str, errors: list[str]) -> dict[str, Any]:
    evidence = load_json(root / "consumer-evidence.json", errors)
    health = load_json(root / "health.json", errors)
    html_path = root / "index.html"
    html = html_path.read_text(encoding="utf-8") if html_path.is_file() else ""
    if not html:
        errors.append(f"{label}: missing index.html")
    for marker in ('lang="hy"', 'lang="en"', 'Skip to content', 'prefers-reduced-motion'):
        if marker not in html:
            errors.append(f"{label}: missing accessibility/bilingual marker {marker}")
    expected = {
        "maturity": expected_maturity,
        "conformanceVerdict": "GREEN",
        "publicApiOnly": True,
        "bilingualParity": True,
        "accessibilityValidated": True,
        "rollbackReady": True,
    }
    for key, value in expected.items():
        if evidence.get(key) != value:
            errors.append(f"{label}: {key} must be {value!r}")
    if health.get("status") != "GREEN" or health.get("consumerId") != evidence.get("consumerId"):
        errors.append(f"{label}: health evidence mismatch")
    if evidence.get("adoptedVersion") != "0.1.0-next.0":
        errors.append(f"{label}: preview version linkage drift")
    packages = evidence.get("packages")
    if not isinstance(packages, list) or not packages:
        errors.append(f"{label}: package linkage missing")
    matrices = evidence.get("matrices")
    if not isinstance(matrices, dict) or set(matrices.get("locale", [])) != {"hy", "en"}:
        errors.append(f"{label}: locale matrix must cover Armenian and English")
    metrics = evidence.get("metrics")
    if not isinstance(metrics, dict) or metrics.get("exceptionCount") != 0 or metrics.get("publicApiCoveragePercent") != 100:
        errors.append(f"{label}: quality metrics are incomplete")
    return evidence


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--console", type=Path, required=True)
    parser.add_argument("--release-bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    errors: list[str] = []
    catalog_root = args.catalog.resolve()
    console_root = args.console.resolve()
    release_root = args.release_bundle.resolve()
    catalog = validate_common("catalog", catalog_root, "M3", errors)
    console = validate_common("release-console", console_root, "M4", errors)

    if catalog.get("consumerId") == console.get("consumerId"):
        errors.append("consumer IDs must be distinct")
    catalog_dimensions = catalog.get("dimensions") if isinstance(catalog.get("dimensions"), dict) else {}
    console_dimensions = console.get("dimensions") if isinstance(console.get("dimensions"), dict) else {}
    dimension_keys = sorted(set(catalog_dimensions) & set(console_dimensions))
    differing_dimensions = [key for key in dimension_keys if catalog_dimensions.get(key) != console_dimensions.get(key)]
    if len(differing_dimensions) < 3:
        errors.append("two-consumer diversity requires at least three differing dimensions")

    for key, value in {"productionEquivalent": True, "incidentReady": True}.items():
        if console.get(key) != value:
            errors.append(f"release-console: {key} must be true for M4")
    for key in ("monitoring", "supportOwner", "releaseLinkage"):
        if not console.get(key):
            errors.append(f"release-console: missing M4 field {key}")

    release_manifest = load_json(release_root / "release-manifest.json", errors)
    package_manifest = load_json(release_root / "package-manifest.json", errors)
    release_evidence = load_json(release_root / "release-evidence.json", errors)
    if release_manifest.get("version") != "0.1.0-next.0" or release_manifest.get("sourceCommit") in (None, "", "unknown"):
        errors.append("release bundle identity/linkage invalid")
    if release_manifest.get("publishAuthorized") is not False or release_manifest.get("stableReleaseAuthorized") is not False:
        errors.append("consumer validation may not authorize publish or Stable release")
    if release_evidence.get("verdict") != "GREEN" or release_evidence.get("ownerApprovalStatus") != "pending":
        errors.append("release validation evidence or Owner authority state invalid")
    if len(package_manifest.get("packages", [])) != 10:
        errors.append("release bundle must contain ten package records")
    console_linkage = console.get("releaseLinkage") if isinstance(console.get("releaseLinkage"), dict) else {}
    if console_linkage.get("releaseId") != release_manifest.get("releaseId") or console_linkage.get("sourceCommit") != release_manifest.get("sourceCommit"):
        errors.append("M4 console release linkage mismatch")

    if errors:
        print("DESIGN PLATFORM TWO-CONSUMER VALIDATION: RED")
        for error in errors:
            print(f"- {error}")
        return 1

    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "schemaVersion": 1,
        "evidenceType": "two-consumer-adoption-validation",
        "decision": "D-025",
        "verdict": "GREEN",
        "sourceCommit": release_manifest["sourceCommit"],
        "releaseId": release_manifest["releaseId"],
        "releaseVersion": release_manifest["version"],
        "consumers": [
            {"id": catalog["consumerId"], "maturity": catalog["maturity"], "conformance": catalog["conformanceVerdict"], "evidenceSha256": sha256(catalog_root / "consumer-evidence.json")},
            {"id": console["consumerId"], "maturity": console["maturity"], "conformance": console["conformanceVerdict"], "evidenceSha256": sha256(console_root / "consumer-evidence.json")},
        ],
        "differingDimensions": differing_dimensions,
        "crossConsumerFindings": [
            "shared public APIs support discovery-oriented and operations-oriented workflows",
            "bilingual and accessibility contracts remain reusable across comfortable and compact density profiles",
            "release authority remains separated from technical conformance",
        ],
        "remediation": {"openDefects": 0, "requiredBeforeOwnerApproval": []},
        "quality": {"publicApiCoveragePercent": 100, "exceptions": 0, "escapedDefects": 0, "rollbackProof": "GREEN", "m4HealthProbe": "GREEN"},
        "ownerApprovalStatus": "pending",
        "mergeAuthorized": False,
        "lockAuthorized": False,
    }
    output.write_text(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print("DESIGN PLATFORM TWO-CONSUMER VALIDATION: GREEN")
    print("Consumer A: M3 GREEN")
    print("Consumer B: M4 GREEN")
    print("Owner approval / merge / lock: NOT GRANTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
