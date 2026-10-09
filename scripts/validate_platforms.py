#!/usr/bin/env python3
"""Validate the MenQ Platforms documents and the D-025 readiness record.

Every check here must be able to give both answers; ``scripts/test_validate_platforms.py`` breaks
each subject once and asserts the RED line.  The validator never answers with a traceback: a
missing, malformed or surprising input is a RED line that names the file and the reason.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORD_REL = "platforms/design/implementation/release/d-025-readiness-record.json"
REGISTRY_REL = "platforms/PLATFORM_REGISTRY.md"

REQUIRED_MARKERS = {
    "platforms/README.md": "<!-- END: PLATFORMS_ROOT_README -->",
    "platforms/PROJECT_CONTEXT.md": "<!-- END: PLATFORMS_PROJECT_CONTEXT -->",
    "platforms/PLATFORM_REGISTRY.md": "<!-- END: PLATFORM_REGISTRY -->",
    "platforms/D-024-PLATFORMS-ARCHITECTURE-V1.md": "<!-- END: D-024-PLATFORMS-ARCHITECTURE-V1 -->",
    "platforms/design/README.md": "<!-- END: MENQ_DESIGN_PLATFORM_README -->",
    "platforms/design/PROJECT_CONTEXT.md": "<!-- END: MENQ_DESIGN_PLATFORM_PROJECT_CONTEXT -->",
    "platforms/design/PLATFORM_CHARTER.md": "<!-- END: MENQ_DESIGN_PLATFORM_CHARTER -->",
    "platforms/design/ARCHITECTURE.md": "<!-- END: MENQ_DESIGN_PLATFORM_ARCHITECTURE -->",
    "platforms/design/CONTRACTS.md": "<!-- END: MENQ_DESIGN_PLATFORM_CONTRACTS -->",
    "platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md": "<!-- END: MENQ_DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1 -->",
    "platforms/design/VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md": "<!-- END: DESIGN_PLATFORM_VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1 -->",
    "platforms/design/DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1.md": "<!-- END: DESIGN_PLATFORM_DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1 -->",
    "platforms/design/GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md": "<!-- END: DESIGN_PLATFORM_GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1 -->",
    "platforms/design/PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md": "<!-- END: DESIGN_PLATFORM_PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1 -->",
    "platforms/design/CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md": "<!-- END: DESIGN_PLATFORM_CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1 -->",
    "platforms/design/D-025_COMPLETENESS_AUDIT.md": "<!-- END: D-025_COMPLETENESS_AUDIT -->",
    "platforms/design/D-025_DRAFT_PR_REVIEW_RECORD.md": "<!-- END: D-025_DRAFT_PR_REVIEW_RECORD -->",
    "platforms/design/D-025_POST_MERGE_CLOSURE_RECORD.md": "<!-- END: D-025_POST_MERGE_CLOSURE_RECORD -->",
    "platforms/design/D-025_LOCK_RECORD.md": "<!-- END: D-025_LOCK_RECORD -->",
    "platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md": "<!-- END: D-025_FINAL_POST_LOCK_AUDIT -->",
    "platforms/design/D-025_EVIDENCE_CORRECTION_RECORD.md": "<!-- END: D-025_EVIDENCE_CORRECTION_RECORD -->",
    "platforms/design/decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md": "<!-- END: D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1 -->",
    "platforms/design/ROADMAP.md": "<!-- END: MENQ_DESIGN_PLATFORM_ROADMAP -->",
    "platforms/design/CHANGELOG.md": "<!-- END: MENQ_DESIGN_PLATFORM_CHANGELOG -->",
    "platforms/design/NEXT_CHAT_HANDOFF.md": "<!-- END: MENQ_DESIGN_PLATFORM_NEXT_CHAT_HANDOFF -->",
}

BILINGUAL_SECTION_FILES = [
    "platforms/design/PROJECT_CONTEXT.md",
    "platforms/design/DESIGN_PLATFORM_ARCHITECTURE_BASELINE_V1.md",
    "platforms/design/VALIDATION_CI_CONFORMANCE_QUALITY_GATES_ARCHITECTURE_V1.md",
    "platforms/design/DOCUMENTATION_PORTAL_COMPONENT_CATALOG_DESIGN_TOOL_INTEGRATION_ARCHITECTURE_V1.md",
    "platforms/design/GOVERNANCE_CONTRIBUTION_OWNERSHIP_CHANGE_REQUEST_LIFECYCLE_ARCHITECTURE_V1.md",
    "platforms/design/PRODUCT_ADOPTION_MATURITY_MODEL_TWO_CONSUMER_VALIDATION_PLAN_V1.md",
    "platforms/design/CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md",
    "platforms/design/D-025_COMPLETENESS_AUDIT.md",
    "platforms/design/D-025_DRAFT_PR_REVIEW_RECORD.md",
    "platforms/design/D-025_POST_MERGE_CLOSURE_RECORD.md",
    "platforms/design/D-025_LOCK_RECORD.md",
    "platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md",
    "platforms/design/NEXT_CHAT_HANDOFF.md",
]

REQUIRED_TERMS = {
    "platforms/design/decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md": [
        "Status / Կարգավիճակ:** Locked",
        "Reference",
        "Semantic",
        "Component",
        "Pattern",
        "Product Extension",
        "two distinct real MenQ consumers",
        "Explicit Owner lock approval was given on 2026-07-13",
    ],
    "platforms/design/PROJECT_CONTEXT.md": [
        "Parts 1–16",
        "0.1.0-next.0",
        "MenQ Design Catalog",
        "MenQ Release Evidence Console",
        "261f85e5b20d726a0ab1f05da84a4dc45a248873",
        "D-025 transaction is closed",
    ],
    "platforms/design/D-025_POST_MERGE_CLOSURE_RECORD.md": [
        "9a833339b1d707d6cd8a792e031dd8ca2857d556",
        "Overall closure verdict — GREEN",
    ],
    "platforms/design/D-025_LOCK_RECORD.md": [
        "Explicit Owner lock approval",
        "261f85e5b20d726a0ab1f05da84a4dc45a248873",
        "treeDifferenceCount",
    ],
    "platforms/design/D-025_FINAL_POST_LOCK_AUDIT.md": [
        "Status / Կարգավիճակ:** GREEN",
        "No open D-025 implementation, closure, or lock action remains",
        "261f85e5b20d726a0ab1f05da84a4dc45a248873",
    ],
}
# platforms/design/ROADMAP.md had three required terms until 2026-10-09 ("M4 operational",
# "D-025 Locked and GREEN", "No open implementation, closure, or lock action remains").  They forced
# the roadmap to keep quoting what the 2026-10-07 evidence correction withdrew, so they were removed.

# --- Content minimums for a required Platforms document (2026-10-09) ----------------------------
# Measured over the 25 documents in REQUIRED_MARKERS on 2026-10-09 with document_body() below.
# The smallest was platforms/PLATFORM_REGISTRY.md: 1847 body bytes, 1053 Latin letters; the fewest
# Armenian letters were 167, in platforms/design/PLATFORM_CHARTER.md.  Each floor is set below the
# smallest real value, so no existing document was edited to meet it.
MIN_BODY_BYTES = 1200
MIN_ARMENIAN_LETTERS = 100
MIN_LATIN_LETTERS = 600
# The one required Platforms document with no "**Status ...:**" metadata line today.
STATUS_METADATA_EXEMPT = ("platforms/design/CHANGELOG.md",)

CONSUMER_IDS = ("menq.design.consumer.catalog", "menq.design.consumer.release-console")

# --- Layout of the readiness record (schemaVersion 2, 2026-10-09, CR-0012) ----------------------
# The values recorded at the 2026-07-13 lock live under SNAPSHOT_KEY and nowhere else; the state in
# force lives under "current" and must agree with the latest entry of "evidenceCorrections".
RECORD_SCHEMA_VERSION = 2
SNAPSHOT_KEY = "snapshot2026-07-13"
SNAPSHOT_FIELDS = (
    "status",
    "evidenceSnapshot",
    "consumers",
    "crossConsumerValidation",
    "qualityAndAdoptionEvidence",
    "finalAudit",
    "remainingAction",
)
# SHA-256 of the snapshot block as canonical JSON (snapshot_digest below), taken on 2026-10-09 from
# the seven top-level values the record carried at 391ff55.  History is corrected by adding an entry
# to "evidenceCorrections"; a snapshot whose content changes is RED.
SNAPSHOT_SHA256 = "70fb3afdba8c8e56f1400749f7b09797b85f9c4b0a3d48442fdf62e8aba9df82"
CURRENT_FIELDS = (
    "asOf",
    "derivedFrom",
    "decisionStatus",
    "twoRealConsumerCondition",
    "consumers",
    "realConsumerObligation",
    "workflowArtifactExpired",
    "permanentReleaseTag",
    "remainingAction",
)
CONFUSED = "D-025 readiness record confuses the 2026-07-13 snapshot with the current block: "
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
MATURITY_LEVELS = ("M0", "M1", "M2", "M3", "M4")
RELEASE_URL_BASE = "https://github.com/menqstudio/MenQ-Standard/releases/tag/"
REAL_CONSUMER = re.compile(r"^menqstudio/[A-Za-z0-9._-]+$")

ARMENIAN = re.compile(r"[Ա-֏]")
LATIN = re.compile(r"[A-Za-z]")
STATUS_LINE = re.compile(r"^\*\*Status\b[^*\n]*:\*\*[ \t]*\S", re.M)
# Every Markdown file under platforms/ (not only the allowlist above) must carry both canonical
# languages and an END marker, so new files cannot merge English-only or unterminated.
HY_MARK = re.compile(r"^(#{2,3} Հայերեն|\*\*HY:?\*\*)", re.M)
EN_MARK = re.compile(r"^(#{2,3} English|\*\*EN:?\*\*)", re.M)

_TEXT_CACHE: dict[str, tuple[str | None, str]] = {}


def load(rel: str) -> tuple[str | None, str]:
    """Return (text with LF line endings, "") or (None, reason).  Never raises."""
    if rel not in _TEXT_CACHE:
        path = ROOT / rel
        try:
            if not path.is_file():
                _TEXT_CACHE[rel] = (None, "is missing from the checkout")
            else:
                _TEXT_CACHE[rel] = (path.read_bytes().decode("utf-8").replace("\r\n", "\n"), "")
        except UnicodeDecodeError:
            _TEXT_CACHE[rel] = (None, "is not valid UTF-8")
        except OSError as exc:
            _TEXT_CACHE[rel] = (None, f"cannot be read ({exc.strerror or exc})")
    return _TEXT_CACHE[rel]


def tracked_files(errors: list[str]) -> list[str]:
    """Every tracked path, from ``git ls-files -z`` so a space or a non-ASCII name is one path."""
    try:
        result = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True)
        return sorted(part for part in result.stdout.decode("utf-8").split("\0") if part)
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError) as exc:
        errors.append(f"cannot enumerate tracked files with git ls-files -z: {exc}")
        return []


def document_body(text: str) -> list[str]:
    """The lines that carry a document's content: not blank, not a heading, not a comment, not code."""
    body: list[str] = []
    in_code = False
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if not in_code and stripped and not stripped.startswith(("#", "<!--")):
            body.append(stripped)
    return body


def validate_documents(errors: list[str], tracked: list[str]) -> None:
    for rel, marker in REQUIRED_MARKERS.items():
        text, reason = load(rel)
        if text is None:
            errors.append(f"Missing required file: {rel}" if "missing" in reason else f"Required file {reason}: {rel}")
            continue
        if not text.rstrip().endswith(marker):
            errors.append(f"Missing or misplaced ending marker: {rel}")
        # A required document must be a real document, not merely exist (2026-10-09 review, item 16).
        body = document_body(text)
        joined = " ".join(body)
        body_bytes = sum(len(line.encode("utf-8")) for line in body)
        if not re.search(r"^# \S", text, re.M):
            errors.append(f"Required document has no level-1 title: {rel}")
        if rel not in STATUS_METADATA_EXEMPT and not STATUS_LINE.search(text):
            errors.append(f"Required document has no Status metadata line: {rel}")
        if body_bytes < MIN_BODY_BYTES:
            errors.append(f"Required document is too small: {rel} has {body_bytes} body bytes, minimum {MIN_BODY_BYTES}")
        if len(ARMENIAN.findall(joined)) < MIN_ARMENIAN_LETTERS:
            errors.append(f"Required document has too little Armenian text: {rel} (minimum {MIN_ARMENIAN_LETTERS} letters)")
        if len(LATIN.findall(joined)) < MIN_LATIN_LETTERS:
            errors.append(f"Required document has too little English text: {rel} (minimum {MIN_LATIN_LETTERS} letters)")

    for rel in BILINGUAL_SECTION_FILES:
        text = load(rel)[0]
        if text is None:
            continue  # every file in this list is also in REQUIRED_MARKERS, which reports it
        if not re.search(r"^## Հայերեն", text, re.M) or not re.search(r"^## English", text, re.M):
            errors.append(f"Missing bilingual canonical sections: {rel}")

    for rel in tracked:
        if not rel.startswith("platforms/") or not rel.lower().endswith(".md") or "node_modules" in rel.split("/"):
            continue
        text, reason = load(rel)
        if text is None:
            errors.append(f"Tracked Markdown file {reason}: {rel}")
            continue
        if not HY_MARK.search(text) or not EN_MARK.search(text):
            errors.append(f"Missing Armenian or English section: {rel}")
        if not re.search(r"<!-- END: [A-Za-z0-9_.-]+ -->\s*(— End of document —\s*)?$", text):
            errors.append(f"Missing ending marker: {rel}")

    for rel, terms in REQUIRED_TERMS.items():
        text, reason = load(rel)
        if text is None:
            errors.append(f"Cannot check required terms, file {reason}: {rel}")
            continue
        for term in terms:
            if term not in text:
                errors.append(f"{rel} missing required term: {term}")


def validate_registry(errors: list[str], tracked: list[str]) -> None:
    """Every platform directory that exists must have a row in the registry table."""
    text = load(REGISTRY_REL)[0]
    if text is None:
        return  # reported as a missing required file
    rows = [line for line in text.split("\n") if line.startswith("|")]
    data_rows = [row for row in rows[2:] if row.strip("|").strip()]
    if len(rows) < 3 or not data_rows:
        errors.append(f"{REGISTRY_REL} registers no Platform (the registry table has no row)")
    platforms = sorted({rel.split("/")[1] for rel in tracked if rel.startswith("platforms/") and rel.count("/") >= 2})
    for name in platforms:
        if not any(f"platforms/{name}/" in row for row in data_rows):
            errors.append(f"{REGISTRY_REL} has no row for the platform directory platforms/{name}/")


def as_object(parent: dict, key: str, errors: list[str], prefix: str = "") -> dict:
    value = parent.get(key)
    if isinstance(value, dict):
        return value
    errors.append(f"D-025 readiness record field '{prefix}{key}' must be an object")
    return {}


def snapshot_digest(snapshot: dict) -> str:
    canonical = json.dumps(snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def same(left: object, right: object) -> bool:
    """Equal in value and in type, so that True is not 1 and "M2" is not ["M2"]."""
    return type(left) is type(right) and left == right


def maturity_by_consumer(items: object, field: str) -> dict:
    if not isinstance(items, list):
        return {}
    return {item.get("consumerId"): item.get(field) for item in items if isinstance(item, dict)}


def validate_record(errors: list[str]) -> dict:
    """Validate the readiness record; return the facts the final summary is printed from."""
    try:
        record = json.loads((ROOT / RECORD_REL).read_bytes().decode("utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"Invalid D-025 readiness record: {exc}")
        return {}
    if not isinstance(record, dict) or not record:
        errors.append("D-025 readiness record must be a non-empty JSON object")
        return {}

    if not same(record.get("schemaVersion"), RECORD_SCHEMA_VERSION):
        errors.append(
            f"D-025 readiness record schemaVersion must be {RECORD_SCHEMA_VERSION}: the 2026-07-13 values under "
            f"'{SNAPSHOT_KEY}' and the state in force under 'current'"
        )
    merge_evidence = as_object(record, "mergeEvidence", errors)
    authority = as_object(record, "authority", errors)
    release_facts = as_object(record, "release", errors)
    snapshot = as_object(record, SNAPSHOT_KEY, errors)
    current = as_object(record, "current", errors)
    final_audit = snapshot.get("finalAudit") if isinstance(snapshot.get("finalAudit"), dict) else {}

    corrections = record.get("evidenceCorrections")
    latest = corrections[-1] if isinstance(corrections, list) and corrections and isinstance(corrections[-1], dict) else {}
    regrade = maturity_by_consumer(latest.get("consumerRegrade"), "maturity")
    previous = maturity_by_consumer(latest.get("consumerRegrade"), "previousMaturity")
    obligation = latest.get("realConsumerObligation") if isinstance(latest.get("realConsumerObligation"), dict) else {}
    if not latest:
        errors.append("D-025 readiness record has no evidence correction (expired artifact, self-attested consumers)")
    else:
        if latest.get("artifactExpired") is not True:
            errors.append("D-025 evidence correction must record the expired workflow artifact")
        validate_permanent_release(errors, latest, release_facts)
        for consumer_id in CONSUMER_IDS:
            if regrade.get(consumer_id) not in {"M0", "M1", "M2"}:
                errors.append(f"{consumer_id} must stay re-graded at or below M2 until independent evidence exists")
        validate_obligation(errors, obligation)

    # The record has two blocks that must never be read for each other.  The snapshot is history: it
    # is held to what the latest correction says it superseded and to its own content hash.  The
    # current block is a restatement of the latest correction and is held equal to it, so it cannot
    # drift and cannot claim more than the correction supports.
    validate_snapshot(errors, record, snapshot, latest, previous)
    validate_current(errors, record, current, snapshot, latest, regrade, obligation)

    if merge_evidence.get("merged") is not True:
        errors.append("D-025 merge evidence does not confirm merge")
    if merge_evidence.get("implementationPullRequest") != 3:
        errors.append("D-025 implementation merge evidence does not identify PR #3")
    if merge_evidence.get("closurePullRequest") != 4:
        errors.append("D-025 closure merge evidence does not identify PR #4")
    if merge_evidence.get("lockPullRequest") != 5:
        errors.append("D-025 lock merge evidence does not identify PR #5")
    if merge_evidence.get("implementationMergeCommit") != "2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc":
        errors.append("D-025 implementation merge commit evidence is incorrect")
    if merge_evidence.get("closureMergeCommit") != "9a833339b1d707d6cd8a792e031dd8ca2857d556":
        errors.append("D-025 closure merge commit evidence is incorrect")
    if merge_evidence.get("lockMergeCommit") != "261f85e5b20d726a0ab1f05da84a4dc45a248873":
        errors.append("D-025 lock merge commit evidence is incorrect")
    if merge_evidence.get("validatedLockHead") != "8ba2e987ff6dab2c25fda18744c7376953d0108f":
        errors.append("D-025 validated lock head evidence is incorrect")
    if merge_evidence.get("treeDifferenceCount") != 0 or merge_evidence.get("treeDifferenceCount") is False:
        errors.append("D-025 lock tree equivalence is not exact")
    if authority.get("readyForReviewAuthorized") is not True or authority.get("mergeAuthorized") is not True:
        errors.append("D-025 readiness record does not preserve Owner ready/merge authority")
    if authority.get("lockAuthorized") is not True:
        errors.append("D-025 readiness record does not preserve Owner lock authority")
    if authority.get("ownerApprovalStatus") != "locked":
        errors.append("D-025 Owner approval state is not Locked")
    if authority.get("owner") != "Gevorg Ohanyan":
        errors.append("D-025 lock owner is not recorded")
    if final_audit.get("verdict") != "GREEN" or final_audit.get("transactionClosed") is not True:
        errors.append("D-025 final post-lock audit is not GREEN and closed")

    in_force = maturity_by_consumer(current.get("consumers"), "maturity")
    return {
        "status": current.get("decisionStatus"),
        "approval": authority.get("ownerApprovalStatus"),
        "maturity": ", ".join(f"{consumer_id.rsplit('.', 1)[-1]}={in_force.get(consumer_id)}" for consumer_id in CONSUMER_IDS),
        "obligation": current.get("realConsumerObligation"),
        "condition": current.get("twoRealConsumerCondition"),
        "snapshot_status": snapshot.get("status"),
        "audit": final_audit.get("verdict"),
        "closed": final_audit.get("transactionClosed"),
    }


def validate_snapshot(errors: list[str], record: dict, snapshot: dict, latest: dict, previous: dict) -> None:
    """The values recorded on 2026-07-13: all seven, nothing else, unchanged, and nowhere but here."""
    for name in SNAPSHOT_FIELDS:
        if name in record:
            errors.append(
                CONFUSED + f"'{name}' is at the top level; the value recorded on 2026-07-13 belongs under "
                f"'{SNAPSHOT_KEY}' and the value in force under 'current'"
            )
    if not isinstance(record.get(SNAPSHOT_KEY), dict):
        return  # as_object() reported it
    for name in SNAPSHOT_FIELDS:
        if name not in snapshot:
            errors.append(f"D-025 readiness record '{SNAPSHOT_KEY}' is missing the field recorded on 2026-07-13: '{name}'")
    for name in sorted(set(snapshot) - set(SNAPSHOT_FIELDS)):
        errors.append(CONFUSED + f"'{name}' is inside '{SNAPSHOT_KEY}', which holds only the fields recorded on 2026-07-13")
    if snapshot_digest(snapshot) != SNAPSHOT_SHA256:
        errors.append(
            f"D-025 readiness record '{SNAPSHOT_KEY}' is not the snapshot recorded on 2026-07-13 (its content hash "
            "differs): history is corrected in 'evidenceCorrections', never rewritten"
        )

    evidence = as_object(snapshot, "evidenceSnapshot", errors, SNAPSHOT_KEY + ".")
    if snapshot.get("status") != "Locked and GREEN":
        errors.append(f"D-025 readiness record '{SNAPSHOT_KEY}.status' is not the status recorded at lock ('Locked and GREEN')")
    if evidence.get("workflowConclusion") != "success":
        errors.append("D-025 readiness workflow evidence is not successful")
    if snapshot.get("crossConsumerValidation") != "GREEN" or snapshot.get("qualityAndAdoptionEvidence") != "GREEN":
        errors.append(f"D-025 readiness record '{SNAPSHOT_KEY}' does not carry the cross-consumer and quality verdicts recorded at lock (GREEN)")

    # The snapshot's maturity is the grade the correction superseded.  It is held to the correction's
    # own "previousMaturity", so the two halves of the record cannot tell different histories.
    declared = maturity_by_consumer(snapshot.get("consumers"), "maturity")
    for consumer_id in CONSUMER_IDS:
        value = declared.get(consumer_id)
        if value not in MATURITY_LEVELS:
            errors.append(f"D-025 readiness record '{SNAPSHOT_KEY}' maturity of {consumer_id} is not one of M0-M4: {value!r}")
        elif latest and value != previous.get(consumer_id):
            errors.append(
                f"D-025 readiness record '{SNAPSHOT_KEY}' maturity of {consumer_id} ({value}) is not the grade the latest "
                f"evidence correction superseded ({previous.get(consumer_id)})"
            )
    if latest and not same(evidence.get("artifactId"), latest.get("expiredArtifactId")):
        errors.append(
            f"D-025 evidence correction names an expired artifact ({latest.get('expiredArtifactId')!r}) that is not the "
            f"artifact of '{SNAPSHOT_KEY}' ({evidence.get('artifactId')!r})"
        )


def strings_in(value: object, path: str):
    """Every string inside a JSON value, with the dotted path that leads to it."""
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from strings_in(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from strings_in(item, f"{path}.{index}")


def validate_current(
    errors: list[str], record: dict, current: dict, snapshot: dict, latest: dict, regrade: dict, obligation: dict
) -> None:
    """The state in force.  Every field restates the latest evidence correction and must equal it."""
    if not isinstance(record.get("current"), dict):
        return  # as_object() reported it
    for name in CURRENT_FIELDS:
        if name not in current:
            errors.append(f"D-025 readiness record 'current' is missing the field '{name}'")
    for name in sorted(set(current) - set(CURRENT_FIELDS)):
        if name in SNAPSHOT_FIELDS:
            errors.append(CONFUSED + f"'{name}' is inside 'current'; it is a field recorded on 2026-07-13 and belongs under '{SNAPSHOT_KEY}'")
        else:
            errors.append(f"D-025 readiness record 'current' has the field '{name}', which no rule ties to the latest evidence correction")
    if not latest:
        return  # reported: with no correction there is nothing for the current block to agree with

    def agree(field: str, expected: object, source: str) -> None:
        if field in current and not same(current[field], expected):
            errors.append(
                f"D-025 readiness record 'current.{field}' ({current[field]!r}) does not agree with the latest evidence "
                f"correction ({source}: {expected!r})"
            )

    met = obligation.get("status") == "met"
    release = latest.get("permanentRelease") if isinstance(latest.get("permanentRelease"), dict) else {}
    agree("decisionStatus", latest.get("d025Status"), "d025Status")
    agree("realConsumerObligation", obligation.get("status"), "realConsumerObligation.status")
    agree("twoRealConsumerCondition", "evidenced" if met else "not evidenced", "realConsumerObligation.status " + repr(obligation.get("status")))
    agree("workflowArtifactExpired", latest.get("artifactExpired"), "artifactExpired")
    agree("permanentReleaseTag", release.get("tag"), "permanentRelease.tag")

    regraded = latest.get("consumerRegrade") if isinstance(latest.get("consumerRegrade"), list) else []
    in_force = [{"consumerId": item.get("consumerId"), "maturity": item.get("maturity")} for item in regraded if isinstance(item, dict)]
    listed = current.get("consumers")
    key = lambda item: json.dumps(item, sort_keys=True, ensure_ascii=False)  # noqa: E731
    if "consumers" in current and (not isinstance(listed, list) or sorted(map(key, listed)) != sorted(map(key, in_force))):
        errors.append(
            "D-025 readiness record 'current.consumers' is not the list of consumers and maturities in force under the "
            f"latest evidence correction: expected {json.dumps(in_force)}, found {json.dumps(listed)}"
        )

    as_of, correction_date = current.get("asOf"), str(latest.get("date", ""))
    if "asOf" in current and (not isinstance(as_of, str) or not ISO_DATE.fullmatch(as_of) or as_of < correction_date):
        errors.append(f"D-025 readiness record 'current.asOf' ({as_of!r}) must be a date on or after the latest evidence correction ({correction_date})")
    derived = current.get("derivedFrom")
    if "derivedFrom" in current and (not isinstance(derived, str) or "evidenceCorrections" not in derived or not correction_date or correction_date not in derived):
        errors.append(f"D-025 readiness record 'current.derivedFrom' does not name the latest entry of evidenceCorrections ({correction_date})")

    action = current.get("remainingAction")
    if "remainingAction" in current:
        texts = [action.get(language) for language in ("hy", "en")] if isinstance(action, dict) else []
        if len(texts) != 2 or not all(isinstance(text, str) and text.strip() for text in texts):
            errors.append("D-025 readiness record 'current.remainingAction' must carry a non-empty 'hy' and 'en' text")
        else:
            historical = snapshot.get("remainingAction") if isinstance(snapshot.get("remainingAction"), dict) else {}
            for language, text in zip(("hy", "en"), texts):
                if text == historical.get(language):
                    errors.append(CONFUSED + f"'current.remainingAction.{language}' repeats the text recorded on 2026-07-13")

    # A claim the latest correction does not support is refused by name, whatever else disagrees.
    for path, text in strings_in(current, "current"):
        if re.search(r"\bGREEN\b", text):
            errors.append(f"D-025 readiness record '{path}' claims GREEN; the latest evidence correction supports no GREEN verdict")
    if current.get("realConsumerObligation") == "met" and not met:
        errors.append(
            "D-025 readiness record 'current' claims the real-consumer obligation is met; the latest evidence correction "
            f"records it as {obligation.get('status')!r}"
        )
    if current.get("twoRealConsumerCondition") == "evidenced" and not met:
        errors.append(
            "D-025 readiness record 'current' claims the two-real-consumer condition is evidenced; the latest evidence "
            f"correction records the obligation as {obligation.get('status')!r}"
        )
    levels = MATURITY_LEVELS + ("M5",)
    for item in listed if isinstance(listed, list) else []:
        claimed = item.get("maturity") if isinstance(item, dict) else None
        if claimed not in levels[3:]:
            continue
        supported = regrade.get(item.get("consumerId"))
        if supported not in levels or levels.index(supported) < levels.index(claimed):
            errors.append(
                f"D-025 readiness record 'current' claims {item.get('maturity')} for {item.get('consumerId')}; the latest "
                f"evidence correction supports {supported or 'no grade for it'}"
            )


def validate_permanent_release(errors: list[str], latest: dict, release_facts: dict) -> None:
    """The release evidence must agree with itself, with the release version, and with its record.

    Whether the tag exists on GitHub cannot be checked offline and is NOT checked here.  What is
    checked is everything that can be: the URL is the tag's URL, the tag and asset are the ones
    publish-release.yml produces for the recorded version, and the digest, URL and source commit
    are the ones the correction record document states.
    """
    release = latest.get("permanentRelease") if isinstance(latest.get("permanentRelease"), dict) else {}
    url, tag, digest = str(release.get("url", "")), str(release.get("tag", "")), str(release.get("assetSha256", ""))
    version = str(release_facts.get("version", ""))
    if not url.startswith(RELEASE_URL_BASE):
        errors.append("D-025 evidence correction must point to a permanent GitHub Release")
    elif not tag or url != RELEASE_URL_BASE + tag:
        errors.append("D-025 permanent release URL is not the URL of its recorded tag")
    if not version or tag != f"design-platform-v{version}":
        errors.append(f"D-025 permanent release tag is not the tag of the recorded release version ({version or 'none'})")
    if not version or release.get("asset") != f"menq-design-platform-{version}.zip":
        errors.append("D-025 permanent release asset is not the bundle of the recorded release version")
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        errors.append("D-025 permanent release asset digest is missing")
    record_rel = str(latest.get("record", ""))
    record_text = load(record_rel)[0] if record_rel.endswith(".md") and not record_rel.startswith(("/", "..")) else None
    if record_text is None:
        errors.append("D-025 evidence correction record file is missing")
        return
    for name, value in (("asset digest", digest), ("URL", url), ("source commit", str(release.get("sourceCommit", "")))):
        if not value or value not in record_text:
            errors.append(f"D-025 permanent release {name} is not the one stated in {record_rel}")


def validate_obligation(errors: list[str], obligation: dict) -> None:
    """"met" is a claim: it needs two named, distinct real consumers that each have recorded evidence."""
    status = obligation.get("status")
    if status not in {"open", "met"}:
        errors.append("D-025 real-consumer obligation status is missing")
        return
    if status == "open":
        return
    consumers = [str(obligation.get(key, "")) for key in ("firstRealConsumer", "secondRealConsumer")]
    progress = obligation.get("progress") if isinstance(obligation.get("progress"), list) else []
    evidenced = {
        str(item.get("consumer", "")).lower()
        for item in progress
        if isinstance(item, dict)
        and str(item.get("evidence", "")).strip()
        and re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(item.get("date", "")))
    }
    named = all(REAL_CONSUMER.match(consumer) for consumer in consumers)
    if not named or consumers[0].lower() == consumers[1].lower() or not all(c.lower() in evidenced for c in consumers):
        errors.append(
            "D-025 real-consumer obligation is marked met without two distinct named real consumers "
            "that each have dated evidence"
        )


def main() -> int:
    errors: list[str] = []
    facts: dict = {}
    try:
        tracked = tracked_files(errors)
        validate_documents(errors, tracked)
        validate_registry(errors, tracked)
        facts = validate_record(errors)
    except Exception as exc:  # a validator answers RED, never with a traceback
        errors.append(f"internal validator error: {type(exc).__name__}: {exc}")

    if errors:
        print("PLATFORMS VALIDATION: RED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PLATFORMS VALIDATION: GREEN")
    print(f"Validated {len(REQUIRED_MARKERS)} required Platforms and D-025 canonical files.")
    # Each value below is read from the record the checks above just passed; none is a literal.  The
    # first two lines are the state in force (the record's "current" block); the third is history.
    print(f"D-025 decision status: {facts['status']}; Owner approval: {facts['approval']}")
    print(
        f"D-025 consumer maturity in force: {facts['maturity']}; real-consumer obligation: {facts['obligation']}; "
        f"two-real-consumer condition: {facts['condition']}"
    )
    print(
        f"D-025 {SNAPSHOT_KEY} (history, not the state in force): status {facts['snapshot_status']!r}; "
        f"final post-lock audit: {facts['audit']}; transaction closed: {facts['closed']}"
    )
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    sys.exit(main())
