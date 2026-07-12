from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "platforms/README.md",
    "platforms/PROJECT_CONTEXT.md",
    "platforms/PLATFORM_REGISTRY.md",
    "platforms/D-024-PLATFORMS-ARCHITECTURE-V1.md",
    "platforms/design/README.md",
    "platforms/design/PROJECT_CONTEXT.md",
    "platforms/design/PLATFORM_CHARTER.md",
    "platforms/design/ARCHITECTURE.md",
    "platforms/design/CONTRACTS.md",
]

MARKERS = {
    "platforms/README.md": "<!-- END: PLATFORMS_ROOT_README -->",
    "platforms/PROJECT_CONTEXT.md": "<!-- END: PLATFORMS_PROJECT_CONTEXT -->",
    "platforms/PLATFORM_REGISTRY.md": "<!-- END: PLATFORM_REGISTRY -->",
    "platforms/D-024-PLATFORMS-ARCHITECTURE-V1.md": "<!-- END: D-024-PLATFORMS-ARCHITECTURE-V1 -->",
    "platforms/design/README.md": "<!-- END: MENQ_DESIGN_PLATFORM_README -->",
    "platforms/design/PROJECT_CONTEXT.md": "<!-- END: MENQ_DESIGN_PLATFORM_PROJECT_CONTEXT -->",
    "platforms/design/PLATFORM_CHARTER.md": "<!-- END: MENQ_DESIGN_PLATFORM_CHARTER -->",
    "platforms/design/ARCHITECTURE.md": "<!-- END: MENQ_DESIGN_PLATFORM_ARCHITECTURE -->",
    "platforms/design/CONTRACTS.md": "<!-- END: MENQ_DESIGN_PLATFORM_CONTRACTS -->",
}

errors = []
for rel in REQUIRED:
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"Missing required file: {rel}")
        continue
    text = path.read_text(encoding="utf-8")
    marker = MARKERS.get(rel)
    if marker and not text.rstrip().endswith(marker):
        errors.append(f"Missing or misplaced ending marker: {rel}")

registry = (ROOT / "platforms/PLATFORM_REGISTRY.md").read_text(encoding="utf-8") if (ROOT / "platforms/PLATFORM_REGISTRY.md").is_file() else ""
for required_term in ["MenQ Design Platform", "Owner", "Status", "Validation"]:
    if required_term not in registry:
        errors.append(f"Registry missing required term: {required_term}")

if errors:
    print("PLATFORMS VALIDATION: RED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("PLATFORMS VALIDATION: GREEN")
print("Validated Platforms root controls and MenQ Design Platform skeleton.")
