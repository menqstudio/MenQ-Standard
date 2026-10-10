#!/usr/bin/env python3
"""Hold the session-read core to its byte budget (decision D-028).

This is MenQ Standard's entry point to the gate. The implementation is ONE
file, consumer/check_session_read_budget.py, which every product repository
holds as an unchanged copy of the consumer kit (decision D-029). Nothing is
implemented here: this file loads that one and supplies the two values that
are this repository's own.

    root      this checkout
    manifest  foundation/ai-collaboration/SESSION_READ_MANIFEST.json

Modes, messages and exit codes are the kit's:
    (default)                check the manifest and the budget
    --receipt                print one sha256 over the ordered core content
    --verify-receipt DIGEST  exit non-zero unless DIGEST is the current receipt
    --sync-areas             repair the manifest's "areas" from the tracked Markdown files

The gate does NOT check that any session read anything: no program in this
repository can. A receipt is a digest of the core content, nothing more.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_REL = "foundation/ai-collaboration/SESSION_READ_MANIFEST.json"
KIT_GATE = DEFAULT_ROOT / "consumer" / "check_session_read_budget.py"


def _load_kit():
    spec = importlib.util.spec_from_file_location("menq_kit_check_session_read_budget", KIT_GATE)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load the session-read budget gate from {KIT_GATE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


try:
    kit = _load_kit()
except (OSError, ImportError, SyntaxError) as exc:
    # A missing or broken kit file must be a RED line that fails the step, never a silent pass.
    print("SESSION READ BUDGET: RED")
    print(f"- the gate's implementation cannot be loaded: consumer/check_session_read_budget.py: {exc}")
    sys.exit(1)

# The kit's own objects, not copies: a test that reads or calls one of these exercises the kit.
SCHEMA_VERSION = kit.SCHEMA_VERSION
UNIVERSAL_TOTAL_BYTES_MAX = kit.UNIVERSAL_TOTAL_BYTES_MAX
ROOT_AREA = kit.ROOT_AREA
Refusal = kit.Refusal
normalised = kit.normalised
tracked_files = kit.tracked_files
is_positive_int = kit.is_positive_int
path_problem = kit.path_problem
load_manifest = kit.load_manifest
shape_errors = kit.shape_errors
core_measurements = kit.core_measurements
area_bytes = kit.area_bytes
is_markdown = kit.is_markdown
own_area = kit.own_area
repaired_areas = kit.repaired_areas


def check(root: Path, manifest_rel: str = MANIFEST_REL) -> tuple[list[str], list[str]]:
    """The kit's check, with this repository's manifest as the default."""
    return kit.check(root, manifest_rel)


def receipt(root: Path, manifest_rel: str = MANIFEST_REL) -> str:
    """The kit's receipt, with this repository's manifest as the default."""
    return kit.receipt(root, manifest_rel)


def sync_areas(root: Path, manifest_rel: str = MANIFEST_REL) -> tuple[list[str], list[str]]:
    """The kit's repair of "areas", with this repository's manifest as the default."""
    return kit.sync_areas(root, manifest_rel)


def main(argv: list[str] | None = None) -> int:
    return kit.main(argv, default_root=DEFAULT_ROOT, default_manifest=MANIFEST_REL)


if __name__ == "__main__":
    sys.exit(main())
