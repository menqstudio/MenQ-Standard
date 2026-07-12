from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

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
    "platforms/design/NEXT_CHAT_HANDOFF.md",
]

REQUIRED_TERMS = {
    "platforms/design/decisions/D-025-MENQ-DESIGN-PLATFORM-ARCHITECTURE-V1.md": [
        "Approved — Implementing",
        "Reference",
        "Semantic",
        "Component",
        "Pattern",
        "Product Extension",
        "two distinct real MenQ consumers",
    ],
    "platforms/design/D-025_COMPLETENESS_AUDIT.md": [
        "Architecture GREEN — Technical/Adoption GREEN — Authority Pending",
        "Architecture verdict:** GREEN",
        "Technical/adoption verdict:** GREEN",
        "Owner authority verdict:** PENDING",
    ],
    "platforms/design/D-025_DRAFT_PR_REVIEW_RECORD.md": [
        "Architecture:** GREEN",
        "Implementation and consumer evidence:** GREEN",
        "Owner authority:** PENDING",
        "open, Draft, and unmerged",
    ],
    "platforms/design/PROJECT_CONTEXT.md": [
        "Parts 1–16",
        "0.1.0-next.0",
        "MenQ Design Catalog",
        "MenQ Release Evidence Console",
        "PR #3 merge commit",
        "D-025 was merged through PR #3",
    ],
    "platforms/design/D-025_POST_MERGE_CLOSURE_RECORD.md": [
        "2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc",
        "9c10c288c16ef319ce4d5aa91000f7b0a46ecf60",
        "PR #3 merge — COMPLETE",
        "D-025 lock authority — PENDING",
    ],
    "platforms/design/ROADMAP.md": [
        "Cross-consumer validation",
        "M4 operational",
        "post-merge validation on `main`",
        "separate explicit Owner lock decision",
    ],
}

errors = []

for rel, marker in REQUIRED_MARKERS.items():
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"Missing required file: {rel}")
        continue
    text = path.read_text(encoding="utf-8")
    if not text.rstrip().endswith(marker):
        errors.append(f"Missing or misplaced ending marker: {rel}")

for rel in BILINGUAL_SECTION_FILES:
    path = ROOT / rel
    if not path.is_file():
        continue
    text = path.read_text(encoding="utf-8")
    if "## Հայերեն" not in text or "## English" not in text:
        errors.append(f"Missing bilingual canonical sections: {rel}")

for rel, terms in REQUIRED_TERMS.items():
    text = (ROOT / rel).read_text(encoding="utf-8")
    for term in terms:
        if term not in text:
            errors.append(f"{rel} missing required term: {term}")

record_path = ROOT / "platforms/design/implementation/release/d-025-readiness-record.json"
try:
    record = json.loads(record_path.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    errors.append(f"Invalid D-025 readiness record: {exc}")
    record = {}

if record:
    evidence = record.get("evidenceSnapshot", {})
    merge_evidence = record.get("mergeEvidence", {})
    authority = record.get("authority", {})
    consumers = record.get("consumers", [])
    maturity = {item.get("consumerId"): item.get("maturity") for item in consumers}
    if evidence.get("workflowConclusion") != "success":
        errors.append("D-025 readiness workflow evidence is not successful")
    if record.get("crossConsumerValidation") != "GREEN" or record.get("qualityAndAdoptionEvidence") != "GREEN":
        errors.append("D-025 cross-consumer or quality evidence is not GREEN")
    if maturity.get("menq.design.consumer.catalog") != "M3":
        errors.append("Design Catalog consumer is not M3")
    if maturity.get("menq.design.consumer.release-console") != "M4":
        errors.append("Release Evidence Console consumer is not M4")
    if merge_evidence.get("merged") is not True:
        errors.append("D-025 merge evidence does not confirm merge")
    if merge_evidence.get("pullRequest") != 3:
        errors.append("D-025 merge evidence does not identify PR #3")
    if merge_evidence.get("mergeCommit") != "2682c99cdcbb058b66ab0cd4ee82d923e5c2a7cc":
        errors.append("D-025 merge commit evidence is incorrect")
    if authority.get("readyForReviewAuthorized") is not True or authority.get("mergeAuthorized") is not True:
        errors.append("D-025 readiness record does not preserve Owner ready/merge authority")
    if authority.get("lockAuthorized") is not False:
        errors.append("D-025 readiness record grants unauthorized lock authority")
    if authority.get("ownerApprovalStatus") != "merge-approved-lock-pending":
        errors.append("D-025 Owner approval state is not synchronized with post-merge closure")

if errors:
    print("PLATFORMS VALIDATION: RED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("PLATFORMS VALIDATION: GREEN")
print(f"Validated {len(REQUIRED_MARKERS)} required Platforms and D-025 canonical files.")
print("D-025 architecture: GREEN")
print("D-025 technical and adoption readiness: GREEN")
print("D-025 ready-for-review and merge authority: OWNER APPROVED AND EXECUTED")
print("D-025 lock authority: PENDING OWNER DECISION")
