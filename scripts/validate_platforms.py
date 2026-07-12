from pathlib import Path
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
    "platforms/design/NEXT_CHAT_HANDOFF.md",
]

REQUIRED_TERMS = {
    "platforms/PLATFORM_REGISTRY.md": ["MenQ Design Platform", "Owner", "Status", "Validation"],
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
        "Architecture GREEN — Implementation YELLOW",
        "Architecture verdict:** GREEN",
        "Implementation/lock verdict:** YELLOW",
        "explicit MenQ Owner decision",
    ],
    "platforms/design/CANONICAL_SPECIFICATION_INDEX_IMPLEMENTATION_PACKAGE_PLAN_V1.md": [
        "@menq/design-contracts",
        "@menq/design-tokens",
        "@menq/design-components",
        "release manifest",
        "two-consumer evidence",
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
    if "## Հայերեն" not in text:
        errors.append(f"Missing Armenian section: {rel}")
    if "## English" not in text:
        errors.append(f"Missing English section: {rel}")

for rel, terms in REQUIRED_TERMS.items():
    path = ROOT / rel
    if not path.is_file():
        continue
    text = path.read_text(encoding="utf-8")
    for term in terms:
        if term not in text:
            errors.append(f"{rel} missing required term: {term}")

context_path = ROOT / "platforms/design/PROJECT_CONTEXT.md"
if context_path.is_file():
    context = context_path.read_text(encoding="utf-8")
    for part in ["Part 12", "Part 13", "Part 14", "Part 15", "Part 16"]:
        if part not in context:
            errors.append(f"Design Platform context missing canonical state: {part}")
    if "D-025 completeness audit and architecture gap analysis" not in context:
        errors.append("Design Platform context missing current audit continuation point")

roadmap_path = ROOT / "platforms/design/ROADMAP.md"
if roadmap_path.is_file():
    roadmap = roadmap_path.read_text(encoding="utf-8")
    for part in ["Part 12", "Part 13", "Part 14", "Part 15", "Part 16"]:
        if f"[x] {part}" not in roadmap:
            errors.append(f"Design Platform roadmap does not mark complete: {part}")

audit_path = ROOT / "platforms/design/D-025_COMPLETENESS_AUDIT.md"
if audit_path.is_file():
    audit = audit_path.read_text(encoding="utf-8")
    forbidden_claims = [
        "Implementation GREEN",
        "D-025 is Locked",
        "D-025 — Locked",
        "two consumers validated",
    ]
    for claim in forbidden_claims:
        if claim in audit:
            errors.append(f"Audit contains unsupported completion claim: {claim}")

if errors:
    print("PLATFORMS VALIDATION: RED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("PLATFORMS VALIDATION: GREEN")
print(f"Validated {len(REQUIRED_MARKERS)} required Platforms and D-025 canonical files.")
print("D-025 architecture: GREEN")
print("D-025 implementation/lock readiness: YELLOW (expected until package and consumer evidence exist)")
