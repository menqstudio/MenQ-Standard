#!/usr/bin/env python3
"""Validate MenQ Design Platform governance (Part 14).

Checks the ownership registry, the approval matrix, every change-request
record, and, for pull requests, that changes to the Design Platform are
linked to a change request.

Usage:
  validate_governance.py
  validate_governance.py --changed-files FILE --pr-body FILE   (pull-request gate)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DESIGN = ROOT / "platforms/design"
GOV = DESIGN / "governance"
OWNERSHIP = GOV / "ownership-registry.json"
OWNERSHIP_SCHEMA = GOV / "ownership-registry.schema.json"
MATRIX = GOV / "approval-matrix.json"
CR_DIR = GOV / "change-requests"
DESIGN_REGISTRY = DESIGN / "specifications/design-platform-registry.json"
DECISION_INDEX = ROOT / "DECISION_INDEX.md"

CR_FILE = re.compile(r"^CR-(\d{4})-[a-z0-9-]+\.md$")
CR_REF = re.compile(r"Change-Request:\s*(CR-\d{4})\b")
EDITORIAL = re.compile(r"Change-Class:\s*editorial\b", re.I)
JSON_BLOCK = re.compile(r"```json\n(.*?)\n```", re.S)
STATUSES = {"proposed", "approved", "implementing", "closed", "rejected", "withdrawn"}
APPROVED_STATUSES = {"approved", "implementing", "closed"}
CR_REQUIRED = {"id", "title", "class", "status", "proposer", "approvals", "affectedAssets", "risk",
               "rollback", "pullRequests", "evidencePlan"}
GOVERNED_PREFIXES = ("platforms/design/",)
GOVERNED_WORKFLOWS = re.compile(r"^\.github/workflows/(design-[a-z0-9-]+|publish-release)\.yml$")


def load(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read {path.relative_to(ROOT)}: {exc}")
        return None


def expected_assets() -> dict[str, str]:
    """Canonical assets that must have an owner: path -> kind."""
    found: dict[str, str] = {}
    for path in sorted((DESIGN / "validation").glob("*.py")):
        found[path.relative_to(ROOT).as_posix()] = "validator"
    for pattern in ("implementation/scripts/*.py", "brand-expression/scripts/*.py"):
        for path in sorted(DESIGN.glob(pattern)):
            found[path.relative_to(ROOT).as_posix()] = "build-script"
    for pattern, kind in (("implementation/packages/*", "package"), ("implementation/consumers/*", "consumer"),
                          ("product-extensions/*", "product-extension")):
        for path in sorted(DESIGN.glob(pattern)):
            if path.is_dir():
                found[path.relative_to(ROOT).as_posix()] = kind
    for path in sorted((ROOT / ".github/workflows").glob("*.yml")):
        rel = path.relative_to(ROOT).as_posix()
        if GOVERNED_WORKFLOWS.match(rel):
            found[rel] = "workflow"
    return found


def check_ownership(errors: list[str]) -> dict[str, dict]:
    doc = load(OWNERSHIP, errors)
    schema = load(OWNERSHIP_SCHEMA, errors)
    registry = load(DESIGN_REGISTRY, errors) or {}
    if doc is None:
        return {}
    if schema is not None:
        try:
            import jsonschema
        except ImportError:
            errors.append("jsonschema is required (pip install jsonschema)")
        else:
            for error in jsonschema.Draft202012Validator(schema).iter_errors(doc):
                errors.append(f"ownership registry schema: {'/'.join(map(str, error.path))}: {error.message}")
    owners = {o.get("ownerId") for o in registry.get("owners", [])}
    assets = doc.get("assets", [])
    by_id: dict[str, dict] = {}
    by_path: dict[str, dict] = {}
    for asset in assets:
        aid = asset.get("id")
        if aid in by_id:
            errors.append(f"duplicate ownership id {aid}")
        by_id[aid] = asset
        by_path.setdefault(asset.get("path"), asset)
        for field in ("ownerId", "backupOwnerId"):
            if asset.get(field) not in owners:
                errors.append(f"{aid}: {field} {asset.get(field)!r} is not a registered owner")
        if asset.get("ownerId") == asset.get("backupOwnerId") and asset.get("changeAuthority") != "owner":
            errors.append(f"{aid}: backup owner must differ from owner for maintainer-authority assets")
        if not (ROOT / str(asset.get("path", ""))).exists():
            errors.append(f"{aid}: path {asset.get('path')} does not exist")
        for consumer in asset.get("affectedConsumers", []):
            if consumer not in {a.get("id") for a in assets}:
                errors.append(f"{aid}: affected consumer {consumer} is not in the ownership registry")
    if doc.get("escalation", {}).get("ownerId") not in owners:
        errors.append("escalation owner is not a registered owner")
    # Coverage: every canonical asset is owned (an unowned canonical asset is a RED governance defect).
    for spec in registry.get("specifications", []):
        if spec.get("id") not in by_id:
            errors.append(f"unowned specification {spec.get('id')}")
    for rel, kind in expected_assets().items():
        asset = by_path.get(rel)
        if asset is None:
            errors.append(f"unowned canonical asset ({kind}): {rel}")
        elif asset.get("kind") != kind:
            errors.append(f"{rel}: ownership kind {asset.get('kind')!r} should be {kind!r}")
    return by_id


def check_matrix(errors: list[str]) -> dict:
    matrix = load(MATRIX, errors) or {}
    expected = {"editorial", "compatible-implementation", "contract-extension", "breaking", "emergency"}
    classes = matrix.get("classes", {})
    if set(classes) != expected:
        errors.append(f"approval matrix classes must be exactly {sorted(expected)}")
    roles = matrix.get("roles", {})
    for name, rule in classes.items():
        groups = rule.get("requiredApproverRoles")
        if not groups or not all(isinstance(g, list) and g for g in groups):
            errors.append(f"approval matrix {name}: requiredApproverRoles must be non-empty role groups")
            continue
        for group in groups:
            for role in group:
                if role not in roles:
                    errors.append(f"approval matrix {name}: unknown role {role}")
        if set(rule.get("title", {})) != {"hy", "en"}:
            errors.append(f"approval matrix {name}: title must be hy/en")
    if classes.get("breaking", {}).get("requiresDecision") is not True:
        errors.append("approval matrix: breaking changes must require a formal decision")
    if classes.get("breaking", {}).get("requiredApproverRoles") != [["owner"]]:
        errors.append("approval matrix: breaking changes must require MenQ Owner approval")
    return matrix


def role_members(role: str, matrix: dict, affected_owners: set[str]) -> set[str]:
    final = matrix.get("rules", {}).get("ownerSatisfiesAllRoles")
    extra = {final} if final else set()
    if role == "domain-owner":
        return affected_owners | extra
    members = matrix.get("roles", {}).get(role, [])
    return (set(members) if isinstance(members, list) else set()) | extra


def check_change_requests(errors: list[str], assets: dict[str, dict], matrix: dict) -> dict[str, dict]:
    records: dict[str, dict] = {}
    if not CR_DIR.is_dir():
        errors.append("change-requests directory is missing")
        return records
    decisions = DECISION_INDEX.read_text(encoding="utf-8")
    for path in sorted(CR_DIR.glob("*.md")):
        rel = path.relative_to(ROOT)
        if path.name == "README.md":
            continue
        match = CR_FILE.match(path.name)
        if not match:
            errors.append(f"{rel}: file name must be CR-NNNN-slug.md")
            continue
        text = path.read_text(encoding="utf-8")
        block = JSON_BLOCK.search(text)
        if not block:
            errors.append(f"{rel}: missing ```json metadata block")
            continue
        try:
            cr = json.loads(block.group(1))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel}: invalid metadata JSON: {exc}")
            continue
        cid = f"CR-{match.group(1)}"
        records[cid] = cr
        missing = CR_REQUIRED - set(cr)
        if missing:
            errors.append(f"{cid}: missing fields {sorted(missing)}")
            continue
        if cr["id"] != cid:
            errors.append(f"{cid}: metadata id {cr['id']} does not match the file name")
        if set(cr.get("title", {})) != {"hy", "en"}:
            errors.append(f"{cid}: title must be hy/en")
        if "## Հայերեն" not in text or "## English" not in text:
            errors.append(f"{cid}: missing '## Հայերեն' or '## English' section")
        if not re.search(rf"<!-- END: {cid} -->\s*$", text):
            errors.append(f"{cid}: missing END marker <!-- END: {cid} -->")
        rule = matrix.get("classes", {}).get(cr["class"])
        if rule is None:
            errors.append(f"{cid}: unknown change class {cr['class']!r}")
            continue
        if cr["status"] not in STATUSES:
            errors.append(f"{cid}: unknown status {cr['status']!r}")
        affected_owners = set()
        for aid in cr["affectedAssets"]:
            if aid not in assets:
                errors.append(f"{cid}: affected asset {aid} is not in the ownership registry")
            else:
                affected_owners.add(assets[aid]["ownerId"])
        if not cr["affectedAssets"]:
            errors.append(f"{cid}: affectedAssets must not be empty")
        approver_ids = {a.get("ownerId") for a in cr["approvals"]}
        for approval in cr["approvals"]:
            if not approval.get("date") or not approval.get("evidence"):
                errors.append(f"{cid}: every approval needs a date and evidence")
        if cr["status"] in APPROVED_STATUSES:
            for group in rule["requiredApproverRoles"]:
                allowed = set().union(*(role_members(r, matrix, affected_owners) for r in group))
                if not approver_ids & allowed:
                    errors.append(f"{cid}: class {cr['class']} needs an approval from {group}")
            proposer = cr.get("proposerOwnerId")
            if (cr["class"] in matrix.get("rules", {}).get("selfApprovalForbiddenFor", [])
                    and proposer and approver_ids == {proposer}):
                errors.append(f"{cid}: self-approval is forbidden for class {cr['class']}")
        if rule.get("requiresDecision"):
            decision = cr.get("decision")
            if not decision or decision not in decisions:
                errors.append(f"{cid}: class {cr['class']} requires a decision registered in DECISION_INDEX.md")
        if rule.get("requiresConsumerEvidencePlan") and not cr.get("consumerEvidencePlan"):
            errors.append(f"{cid}: class {cr['class']} requires consumerEvidencePlan")
        if rule.get("requiresMigrationPlan") and not cr.get("migrationPlan"):
            errors.append(f"{cid}: class {cr['class']} requires migrationPlan")
        if cr["status"] == "closed":
            closure = cr.get("closure") or {}
            if not closure.get("date") or not closure.get("evidence"):
                errors.append(f"{cid}: closed change requests need closure date and evidence")
            if not cr["pullRequests"]:
                errors.append(f"{cid}: closed change requests must link at least one pull request")
            if rule.get("requiresRetrospective") and not cr.get("retrospective"):
                errors.append(f"{cid}: emergency changes need a retrospective before closing")
    return records


def check_pull_request(errors: list[str], changed_path: Path, body_path: Path, records: dict[str, dict]) -> None:
    changed = [line.strip() for line in changed_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    body = body_path.read_text(encoding="utf-8") if body_path.is_file() else ""
    governed = [f for f in changed if f.startswith(GOVERNED_PREFIXES) or GOVERNED_WORKFLOWS.match(f)]
    if not governed:
        print("PR gate: no governed Design Platform files changed.")
        return
    refs = CR_REF.findall(body)
    if refs:
        for ref in refs:
            cr = records.get(ref)
            if cr is None:
                errors.append(f"PR references {ref}, but no change-request record exists")
            elif cr.get("status") in {"rejected", "withdrawn"}:
                errors.append(f"PR references {ref}, which is {cr.get('status')}")
        print(f"PR gate: {len(governed)} governed file(s) linked to {', '.join(refs)}.")
        return
    if EDITORIAL.search(body):
        non_docs = [f for f in governed if not f.endswith(".md")]
        if non_docs:
            errors.append(f"Change-Class: editorial is limited to Markdown; non-editorial files changed: {non_docs[:5]}")
        print("PR gate: editorial change declared.")
        return
    errors.append("PR changes governed Design Platform files but its description has no "
                  "'Change-Request: CR-NNNN' line or 'Change-Class: editorial' declaration")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed-files", type=Path)
    parser.add_argument("--pr-body", type=Path)
    args = parser.parse_args()
    errors: list[str] = []
    assets = check_ownership(errors)
    matrix = check_matrix(errors)
    records = check_change_requests(errors, assets, matrix)
    if args.changed_files:
        check_pull_request(errors, args.changed_files, args.pr_body or Path("/nonexistent"), records)
    if errors:
        print("DESIGN GOVERNANCE VALIDATION: RED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("DESIGN GOVERNANCE VALIDATION: GREEN")
    print(f"Validated {len(assets)} owned assets, {len(matrix.get('classes', {}))} change classes and {len(records)} change requests.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
