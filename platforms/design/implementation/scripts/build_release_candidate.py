#!/usr/bin/env python3
"""Build deterministic MenQ Design Platform preview release-candidate artifacts."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import os
import shutil
import subprocess
import tarfile
from pathlib import Path
from typing import Any

SCRIPT = Path(__file__).resolve()
WORKSPACE = SCRIPT.parents[1]
ROOT = SCRIPT.parents[4]
CONFIG_PATH = WORKSPACE / "release/release-config.json"
REGISTRY_PATH = ROOT / "platforms/design/specifications/design-platform-registry.json"
BASELINE_PATH = WORKSPACE / "release/public-api-baseline.json"


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_bytes(path: Path, data: bytes) -> dict[str, Any]:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return {"path": path.name, "bytes": len(data), "sha256": sha256_bytes(data)}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"top-level JSON must be an object: {path}")
    return value


def source_commit() -> str:
    override = os.environ.get("MENQ_SOURCE_COMMIT")
    if override:
        return override
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def package_dir(package_name: str) -> Path:
    return WORKSPACE / "packages" / package_name.removeprefix("@menq/")


def collect_declared_files(directory: Path, manifest: dict[str, Any]) -> dict[str, bytes]:
    selected: dict[str, bytes] = {"package.json": b""}
    declared = manifest.get("files", [])
    if not isinstance(declared, list) or not declared:
        raise ValueError(f"package {manifest.get('name')} must declare a non-empty files list")
    for entry in declared:
        if not isinstance(entry, str) or not entry or entry.startswith(("/", "..")):
            raise ValueError(f"invalid files entry {entry!r} in {manifest.get('name')}")
        target = directory / entry
        if target.is_file():
            selected[target.relative_to(directory).as_posix()] = target.read_bytes()
        elif target.is_dir():
            for path in sorted(target.rglob("*")):
                if path.is_file():
                    relative = path.relative_to(directory).as_posix()
                    if "/node_modules/" not in f"/{relative}/" and not relative.endswith(".pyc"):
                        selected[relative] = path.read_bytes()
        else:
            raise ValueError(f"declared package file is missing: {target.relative_to(ROOT)}")
    return dict(sorted(selected.items()))


def release_manifest_for_package(source: dict[str, Any], version: str, channel: str, status: str) -> dict[str, Any]:
    manifest = json.loads(json.dumps(source))
    manifest["version"] = version
    manifest["private"] = True
    dependencies = manifest.get("dependencies") or {}
    if not isinstance(dependencies, dict):
        raise ValueError(f"dependencies must be an object in {manifest.get('name')}")
    manifest["dependencies"] = {
        name: version if name.startswith("@menq/design-") else value
        for name, value in sorted(dependencies.items())
    }
    manifest["menqRelease"] = {
        "channel": channel,
        "packageStatus": status,
        "publishAuthorized": False,
        "stableReleaseAuthorized": False,
    }
    return manifest


def deterministic_tgz(files: dict[str, bytes]) -> bytes:
    raw = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=9) as gz:
        with tarfile.open(fileobj=gz, mode="w", format=tarfile.USTAR_FORMAT) as archive:
            for relative, data in sorted(files.items()):
                info = tarfile.TarInfo(f"package/{relative}")
                info.size = len(data)
                info.mtime = 0
                info.uid = 0
                info.gid = 0
                info.uname = ""
                info.gname = ""
                info.mode = 0o644
                archive.addfile(info, io.BytesIO(data))
    return raw.getvalue()


def normalize_exports(exports: Any) -> dict[str, Any]:
    if isinstance(exports, str):
        return {".": exports}
    if not isinstance(exports, dict):
        raise ValueError("package exports must be a string or object")
    return {str(key): exports[key] for key in sorted(exports)}


def public_api_diff(baseline: dict[str, Any], current: dict[str, Any]) -> dict[str, Any]:
    old = baseline.get("packages", {})
    new = current.get("packages", {})
    if not isinstance(old, dict) or not isinstance(new, dict):
        raise ValueError("public API package maps must be objects")
    added_packages = sorted(set(new) - set(old))
    removed_packages = sorted(set(old) - set(new))
    changes: list[dict[str, Any]] = []
    for name in sorted(set(old) & set(new)):
        old_exports = old[name].get("exports", {})
        new_exports = new[name].get("exports", {})
        added = sorted(set(new_exports) - set(old_exports))
        removed = sorted(set(old_exports) - set(new_exports))
        changed = [
            {"export": key, "from": old_exports[key], "to": new_exports[key]}
            for key in sorted(set(old_exports) & set(new_exports))
            if old_exports[key] != new_exports[key]
        ]
        if added or removed or changed:
            changes.append(
                {"package": name, "addedExports": added, "removedExports": removed, "changedTargets": changed}
            )
    breaking = bool(removed_packages) or any(item["removedExports"] or item["changedTargets"] for item in changes)
    return {
        "schemaVersion": 1,
        "baselineId": baseline.get("baselineId"),
        "addedPackages": added_packages,
        "removedPackages": removed_packages,
        "changedPackages": changes,
        "breaking": breaking,
        "classification": "breaking" if breaking else ("additive" if added_packages or changes else "none"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=WORKSPACE / "release/generated")
    args = parser.parse_args()
    output = args.output.resolve()

    config = load_json(CONFIG_PATH)
    registry = load_json(REGISTRY_PATH)
    baseline = load_json(BASELINE_PATH)
    version = config["version"]
    channel = config["releaseChannel"]
    status = config["packageStatus"]
    expected_names = config["packages"]
    registry_packages = {item["name"]: item for item in registry["packages"]}
    if list(expected_names) != [item["name"] for item in registry["packages"]]:
        raise ValueError("release package order must exactly match the canonical registry")

    if output.exists():
        shutil.rmtree(output)
    package_output = output / "packages"
    package_output.mkdir(parents=True)

    package_records: list[dict[str, Any]] = []
    api_packages: dict[str, Any] = {}
    for name in expected_names:
        directory = package_dir(name)
        source_manifest = load_json(directory / "package.json")
        if source_manifest.get("name") != name:
            raise ValueError(f"package name mismatch for {name}")
        if source_manifest.get("version") != config["sourcePackageVersion"]:
            raise ValueError(f"source version mismatch for {name}")
        release_manifest = release_manifest_for_package(source_manifest, version, channel, status)
        files = collect_declared_files(directory, source_manifest)
        files["package.json"] = canonical_json(release_manifest)
        files = dict(sorted(files.items()))
        archive_name = f"{name.removeprefix('@').replace('/', '-')}-{version}.tgz"
        archive_bytes = deterministic_tgz(files)
        archive_path = package_output / archive_name
        archive_path.write_bytes(archive_bytes)
        exports = normalize_exports(source_manifest.get("exports"))
        expected_public_api = sorted(registry_packages[name].get("publicApi", []))
        if sorted(exports) != expected_public_api:
            raise ValueError(f"registry/export drift for {name}: {expected_public_api} != {sorted(exports)}")
        package_records.append(
            {
                "name": name,
                "version": version,
                "status": status,
                "private": True,
                "archive": f"packages/{archive_name}",
                "bytes": len(archive_bytes),
                "sha256": sha256_bytes(archive_bytes),
                "dependencies": release_manifest.get("dependencies", {}),
                "publicApi": expected_public_api,
                "files": [
                    {"path": f"package/{path}", "bytes": len(data), "sha256": sha256_bytes(data)}
                    for path, data in files.items()
                ],
            }
        )
        api_packages[name] = {"version": version, "status": status, "exports": exports}

    current_api = {
        "schemaVersion": 1,
        "releaseId": config["releaseId"],
        "version": version,
        "stableCompatibilityPromise": False,
        "packages": api_packages,
    }
    api_diff = public_api_diff(baseline, current_api)
    if api_diff["breaking"]:
        raise ValueError("preview release candidate contains an unapproved breaking public API diff")

    package_manifest = {
        "schemaVersion": 1,
        "releaseId": config["releaseId"],
        "version": version,
        "packageVersionPolicy": config["packageVersionPolicy"],
        "packages": package_records,
    }
    write_bytes(output / "package-manifest.json", canonical_json(package_manifest))
    write_bytes(output / "public-api-current.json", canonical_json(current_api))
    write_bytes(output / "public-api-diff.json", canonical_json(api_diff))

    contract_copies = {
        "contracts/release-config.json": canonical_json(config),
        "contracts/public-api-baseline.json": canonical_json(baseline),
        "contracts/COMPATIBILITY_POLICY.md": (ROOT / config["compatibilityPolicy"]).read_bytes(),
        "contracts/MIGRATION_DEPRECATION_GUIDE.md": (ROOT / config["migrationDeprecationGuide"]).read_bytes(),
        "contracts/ROLLBACK_CONTRACT.md": (ROOT / config["rollbackContract"]).read_bytes(),
    }
    for relative, data in contract_copies.items():
        write_bytes(output / relative, data)

    commit = source_commit()
    artifact_paths = [record["archive"] for record in package_records] + [
        "package-manifest.json",
        "public-api-current.json",
        "public-api-diff.json",
        *sorted(contract_copies),
    ]
    release_artifacts = []
    for relative in sorted(artifact_paths):
        data = (output / relative).read_bytes()
        release_artifacts.append({"path": relative, "bytes": len(data), "sha256": sha256_bytes(data)})
    release_manifest = {
        "schemaVersion": 1,
        "releaseId": config["releaseId"],
        "decision": config["decision"],
        "status": config["status"],
        "version": version,
        "releaseChannel": channel,
        "sourceCommit": commit,
        "packageVersionPolicy": config["packageVersionPolicy"],
        "publishAuthorized": config["publishAuthorized"],
        "stableReleaseAuthorized": config["stableReleaseAuthorized"],
        "ownerApprovalStatus": config["ownerApprovalStatus"],
        "artifacts": release_artifacts,
        "releaseBlocks": config["releaseBlocks"],
    }
    write_bytes(output / "release-manifest.json", canonical_json(release_manifest))

    build_evidence = {
        "schemaVersion": 1,
        "evidenceType": "deterministic-build-candidate",
        "releaseId": config["releaseId"],
        "sourceCommit": commit,
        "packageCount": len(package_records),
        "publicApiDiff": {"breaking": False, "classification": api_diff["classification"]},
        "independentRebuildComparison": "required-before-GREEN",
        "publishAuthorized": False,
        "stableReleaseAuthorized": False,
        "ownerApprovalStatus": config["ownerApprovalStatus"],
    }
    write_bytes(output / "build-evidence.json", canonical_json(build_evidence))

    checksum_paths = sorted(
        path.relative_to(output).as_posix()
        for path in output.rglob("*")
        if path.is_file() and path.name != "checksums.sha256"
    )
    checksum_text = "".join(
        f"{sha256_bytes((output / relative).read_bytes())}  {relative}\n" for relative in checksum_paths
    )
    (output / "checksums.sha256").write_text(checksum_text, encoding="utf-8", newline="\n")

    print("DESIGN PLATFORM RELEASE BUILD: GREEN")
    print(f"Built {len(package_records)} deterministic private package archives for {version} ({channel}).")
    print(f"Output: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
