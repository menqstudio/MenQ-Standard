#!/usr/bin/env python3
"""Validate MenQ Design Platform release-candidate artifacts and evidence."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import tarfile
from pathlib import Path
from typing import Any

SCRIPT = Path(__file__).resolve()
ROOT = SCRIPT.parents[3]
WORKSPACE = ROOT / "platforms/design/implementation"
CONFIG_PATH = WORKSPACE / "release/release-config.json"
REGISTRY_PATH = ROOT / "platforms/design/specifications/design-platform-registry.json"


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read JSON {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"top-level JSON must be an object: {path}")
        return {}
    return value


def tree_digest_map(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): sha256(path)
        for path in sorted(root.rglob("*"))
        if path.is_file() and path.name != "release-evidence.json"
    }


def validate_checksums(root: Path, errors: list[str]) -> None:
    checksum_file = root / "checksums.sha256"
    if not checksum_file.is_file():
        errors.append("missing checksums.sha256")
        return
    listed: dict[str, str] = {}
    for line in checksum_file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            digest, relative = line.split("  ", 1)
        except ValueError:
            errors.append(f"invalid checksum line: {line!r}")
            continue
        listed[relative] = digest
        path = root / relative
        if not path.is_file():
            errors.append(f"checksummed artifact is missing: {relative}")
        elif sha256(path) != digest:
            errors.append(f"checksum mismatch: {relative}")
    actual = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and path.name not in {"checksums.sha256", "release-evidence.json"}
    }
    if set(listed) != actual:
        errors.append(f"checksum coverage mismatch: listed={sorted(listed)} actual={sorted(actual)}")


def validate_archive(root: Path, record: dict[str, Any], version: str, errors: list[str]) -> None:
    relative = record.get("archive")
    archive_path = root / str(relative)
    if not archive_path.is_file():
        errors.append(f"missing package archive: {relative}")
        return
    data = archive_path.read_bytes()
    if len(data) != record.get("bytes") or hashlib.sha256(data).hexdigest() != record.get("sha256"):
        errors.append(f"package archive manifest mismatch: {relative}")
    if len(data) < 10 or int.from_bytes(data[4:8], "little") != 0:
        errors.append(f"gzip timestamp must be zero: {relative}")
    expected_files = {item["path"]: item for item in record.get("files", [])}
    actual_files: dict[str, bytes] = {}
    try:
        with gzip.GzipFile(fileobj=__import__("io").BytesIO(data), mode="rb") as gz:
            with tarfile.open(fileobj=gz, mode="r:") as archive:
                for member in archive.getmembers():
                    if not member.isfile():
                        errors.append(f"archive may contain files only: {relative}:{member.name}")
                        continue
                    if not member.name.startswith("package/") or ".." in Path(member.name).parts:
                        errors.append(f"unsafe archive path: {relative}:{member.name}")
                        continue
                    if member.mtime != 0 or member.uid != 0 or member.gid != 0:
                        errors.append(f"non-deterministic tar metadata: {relative}:{member.name}")
                    extracted = archive.extractfile(member)
                    actual_files[member.name] = extracted.read() if extracted else b""
    except (OSError, tarfile.TarError) as exc:
        errors.append(f"invalid archive {relative}: {exc}")
        return
    if set(actual_files) != set(expected_files):
        errors.append(f"archive file set mismatch: {relative}")
    for path, file_record in expected_files.items():
        content = actual_files.get(path)
        if content is None:
            continue
        if len(content) != file_record.get("bytes") or hashlib.sha256(content).hexdigest() != file_record.get("sha256"):
            errors.append(f"archive file checksum mismatch: {relative}:{path}")
    package_json = actual_files.get("package/package.json")
    if package_json:
        try:
            manifest = json.loads(package_json.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"invalid archived package.json in {relative}: {exc}")
        else:
            if manifest.get("name") != record.get("name") or manifest.get("version") != version:
                errors.append(f"archived name/version mismatch: {relative}")
            if manifest.get("private") is not True:
                errors.append(f"preview archive must remain private: {relative}")
            for dependency, dependency_version in (manifest.get("dependencies") or {}).items():
                if dependency.startswith("@menq/design-") and dependency_version != version:
                    errors.append(f"release dependency version drift: {relative}:{dependency}")
            release_meta = manifest.get("menqRelease") or {}
            if release_meta.get("publishAuthorized") is not False or release_meta.get("stableReleaseAuthorized") is not False:
                errors.append(f"archive authority guard missing: {relative}")


def validate_docs(config: dict[str, Any], errors: list[str]) -> None:
    for key in ("compatibilityPolicy", "migrationDeprecationGuide", "rollbackContract"):
        relative = config.get(key)
        path = ROOT / str(relative)
        if not path.is_file():
            errors.append(f"missing release contract: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        if "## Հայերեն" not in text or "## English" not in text or not text.rstrip().endswith("— End of document —"):
            errors.append(f"release contract is incomplete or not bilingual: {relative}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--comparison", type=Path)
    parser.add_argument("--write-evidence", action="store_true")
    args = parser.parse_args()
    primary = args.primary.resolve()
    comparison = args.comparison.resolve() if args.comparison else None
    errors: list[str] = []

    config = load_json(CONFIG_PATH, errors)
    registry = load_json(REGISTRY_PATH, errors)
    release_manifest = load_json(primary / "release-manifest.json", errors)
    package_manifest = load_json(primary / "package-manifest.json", errors)
    current_api = load_json(primary / "public-api-current.json", errors)
    api_diff = load_json(primary / "public-api-diff.json", errors)
    build_evidence = load_json(primary / "build-evidence.json", errors)

    version = config.get("version")
    expected_packages = config.get("packages", [])
    if config.get("status") != "Preview Candidate" or config.get("releaseChannel") != "next":
        errors.append("release configuration must remain Preview Candidate on next channel")
    if config.get("publishAuthorized") is not False or config.get("stableReleaseAuthorized") is not False:
        errors.append("release configuration may not authorize publish or Stable release")
    if config.get("ownerApprovalStatus") != "pending":
        errors.append("Owner release approval must remain pending")
    validate_docs(config, errors)
    validate_checksums(primary, errors)

    baseline = load_json(ROOT / config.get("publicApiBaseline", ""), errors)
    expected_contracts = {
        "contracts/release-config.json": canonical_json(config).encode("utf-8"),
        "contracts/public-api-baseline.json": canonical_json(baseline).encode("utf-8"),
        "contracts/COMPATIBILITY_POLICY.md": (ROOT / config.get("compatibilityPolicy", "")).read_bytes(),
        "contracts/MIGRATION_DEPRECATION_GUIDE.md": (ROOT / config.get("migrationDeprecationGuide", "")).read_bytes(),
        "contracts/ROLLBACK_CONTRACT.md": (ROOT / config.get("rollbackContract", "")).read_bytes(),
    }
    for relative, expected in expected_contracts.items():
        path = primary / relative
        if not path.is_file() or path.read_bytes() != expected:
            errors.append(f"release evidence contract copy drift: {relative}")

    if release_manifest.get("version") != version or release_manifest.get("releaseId") != config.get("releaseId"):
        errors.append("release manifest identity/version drift")
    if release_manifest.get("sourceCommit") in (None, "", "unknown"):
        errors.append("release manifest must contain a real source commit")
    if release_manifest.get("publishAuthorized") is not False or release_manifest.get("stableReleaseAuthorized") is not False:
        errors.append("release manifest authority guard failure")
    for artifact in release_manifest.get("artifacts", []):
        relative = artifact.get("path")
        path = primary / str(relative)
        if not path.is_file():
            errors.append(f"release manifest artifact is missing: {relative}")
        elif path.stat().st_size != artifact.get("bytes") or sha256(path) != artifact.get("sha256"):
            errors.append(f"release manifest artifact mismatch: {relative}")

    package_records = package_manifest.get("packages", [])
    if not isinstance(package_records, list) or [item.get("name") for item in package_records] != expected_packages:
        errors.append("package manifest order/content must match release configuration")
        package_records = []
    registry_names = [item.get("name") for item in registry.get("packages", [])]
    if registry_names != expected_packages:
        errors.append("release configuration package list must match canonical registry")
    for record in package_records:
        if record.get("version") != version or record.get("status") != "Preview" or record.get("private") is not True:
            errors.append(f"package release metadata drift: {record.get('name')}")
        validate_archive(primary, record, str(version), errors)

    api_packages = current_api.get("packages", {})
    if sorted(api_packages) != sorted(expected_packages):
        errors.append("public API snapshot package coverage mismatch")
    for record in package_records:
        api_entry = api_packages.get(record.get("name"), {})
        if api_entry.get("version") != version or api_entry.get("status") != "Preview":
            errors.append(f"public API package metadata drift: {record.get('name')}")
        if sorted((api_entry.get("exports") or {}).keys()) != sorted(record.get("publicApi", [])):
            errors.append(f"public API export coverage drift: {record.get('name')}")
    if current_api.get("stableCompatibilityPromise") is not False:
        errors.append("Stable compatibility promise must remain false")
    if api_diff.get("breaking") is not False:
        errors.append("public API diff contains a breaking change")
    if build_evidence.get("independentRebuildComparison") != "required-before-GREEN":
        errors.append("build evidence must not self-claim deterministic comparison")

    deterministic = None
    if comparison:
        if not comparison.is_dir():
            errors.append(f"comparison directory is missing: {comparison}")
        else:
            primary_map = tree_digest_map(primary)
            comparison_map = tree_digest_map(comparison)
            deterministic = primary_map == comparison_map
            if not deterministic:
                errors.append("independent deterministic rebuild comparison failed")

    if errors:
        print("DESIGN PLATFORM RELEASE VALIDATION: RED")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.write_evidence:
        evidence = {
            "schemaVersion": 1,
            "evidenceType": "release-candidate-validation",
            "releaseId": config["releaseId"],
            "version": version,
            "releaseChannel": config["releaseChannel"],
            "sourceCommit": release_manifest["sourceCommit"],
            "verdict": "GREEN",
            "checks": {
                "packageArchives": "GREEN",
                "artifactManifests": "GREEN",
                "checksums": "GREEN",
                "publicApiDiff": "GREEN",
                "compatibilityMigrationRollbackContracts": "GREEN",
                "independentDeterministicRebuild": "GREEN" if deterministic else "NOT_RUN",
            },
            "packageCount": len(package_records),
            "publishAuthorized": False,
            "stableReleaseAuthorized": False,
            "ownerApprovalStatus": config["ownerApprovalStatus"],
            "remainingReleaseBlocks": config["releaseBlocks"],
            "checksumsSha256": sha256(primary / "checksums.sha256"),
            "releaseManifestSha256": sha256(primary / "release-manifest.json"),
        }
        (primary / "release-evidence.json").write_text(canonical_json(evidence), encoding="utf-8", newline="\n")

    print("DESIGN PLATFORM RELEASE VALIDATION: GREEN")
    print(f"Validated {len(package_records)} private preview archives for {version}.")
    if deterministic:
        print("Independent deterministic rebuild comparison: GREEN")
    print("Release/merge/lock authorization: NOT GRANTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
