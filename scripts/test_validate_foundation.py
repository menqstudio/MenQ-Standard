#!/usr/bin/env python3
"""Tests for validate_foundation.py.

Every check in the validator has a test here that breaks exactly its subject in a temporary git
repository and asserts RED with the specific message, next to positive controls that are GREEN.
The fixture is a copy of this repository's own tracked files, so the real rules run against the
real content.  Fixture files are written as bytes, never as text, so the tests behave the same on
a platform that checks files out with CRLF.  Run:

    python scripts/test_validate_foundation.py
"""

from __future__ import annotations

import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
import validate_foundation as vf  # noqa: E402

SCRIPT = "scripts/validate_foundation.py"
WF = ".github/workflows/"
INVENTORY = "foundation/ai-collaboration/MARKDOWN_INVENTORY.json"
ARM = "Սա հայերեն նախադասություն է, որը բավականաչափ տառ ունի։ "
ENG = "This is an English sentence that carries enough letters for the floor. "
END = re.compile(r"\n*<!-- END: [A-Za-z0-9_.-]+ -->\s*$")
_BASE: Path | None = None


def _force_remove(function, path, _info) -> None:
    os.chmod(path, stat.S_IWRITE)
    function(path)


def setUpModule() -> None:
    """Copy the tracked files of the real repository into one base git repository."""
    global _BASE
    _BASE = Path(tempfile.mkdtemp(prefix="menq-foundation-base-"))
    listing = subprocess.run(["git", "ls-files", "-z"], cwd=REPO, check=True, capture_output=True).stdout
    for rel in filter(None, listing.decode("utf-8").split("\0")):
        if (REPO / rel).is_file():
            (_BASE / rel).parent.mkdir(parents=True, exist_ok=True)
            (_BASE / rel).write_bytes((REPO / rel).read_bytes())
    for args in (("init", "-q"), ("config", "core.autocrlf", "false"), ("config", "core.quotepath", "true"), ("add", "-A")):
        subprocess.run(["git", *args], cwd=_BASE, check=True, capture_output=True)


def tearDownModule() -> None:
    if _BASE is not None:
        shutil.rmtree(_BASE, onerror=_force_remove)


class Repo:
    def __init__(self, root: Path) -> None:
        self.root = root

    def read(self, rel: str) -> str:
        return (self.root / rel).read_bytes().decode("utf-8")

    def write(self, rel: str, text: str | bytes) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text if isinstance(text, bytes) else text.encode("utf-8"))

    def sub(self, rel: str, old: str, new: str, count: int = 1) -> None:
        text = self.read(rel)
        assert old in text, f"{old!r} is not in {rel}: the mutation would change nothing"
        self.write(rel, text.replace(old, new, count))

    def resub(self, rel: str, pattern: str, replacement: str, count: int = 1) -> None:
        text, changed = re.subn(pattern, replacement, self.read(rel), count=count, flags=re.M)
        assert changed, f"{pattern!r} matches nothing in {rel}: the mutation would change nothing"
        self.write(rel, text)

    def before_end(self, rel: str, addition: str) -> None:
        text = self.read(rel)
        match = END.search(text)
        assert match, f"{rel} has no trailing END marker"
        self.write(rel, text[: match.start()] + "\n\n" + addition.strip("\n") + text[match.start():])

    def git(self, *args: str) -> None:
        subprocess.run(["git", *args], cwd=self.root, check=True, capture_output=True)

    def run(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, *args], cwd=self.root, capture_output=True, text=True, encoding="utf-8"
        )


def document(armenian: int, english: int, status: bool = True, title: bool = True) -> str:
    """A well-formed bilingual document with a chosen amount of text in each language."""
    parts = ["# Title / Վերնագիր\n"] if title else []
    if status:
        parts.append("**Status / Կարգավիճակ:** Active\n")
    parts += ["## Հայերեն\n", ARM * armenian + "\n", "## English\n", ENG * english + "\n", "<!-- END: FIXTURE -->\n"]
    return "\n".join(parts)


class Case(unittest.TestCase):
    maxDiff = None

    def fresh(self) -> Repo:
        root = Path(tempfile.mkdtemp(prefix="menq-foundation-"))
        self.addCleanup(shutil.rmtree, root, onerror=_force_remove)
        shutil.copytree(_BASE, root, dirs_exist_ok=True)
        return Repo(root)

    def verdict(self, repo: Repo, regen: bool = True, add: bool = True) -> subprocess.CompletedProcess:
        if add:
            repo.git("add", "-A")
        if regen:
            written = repo.run("scripts/generate_markdown_inventory.py", "--write")
            self.assertEqual(written.returncode, 0, written.stdout + written.stderr)
            repo.git("add", INVENTORY)
        return repo.run(SCRIPT)

    def assertRed(self, result: subprocess.CompletedProcess, *needles: str) -> None:
        output = result.stdout + result.stderr
        self.assertNotIn("Traceback", output)
        self.assertEqual(result.returncode, 1, output)
        self.assertEqual(result.stdout.splitlines()[0], "FOUNDATION VALIDATION: RED", output)
        for needle in needles:
            self.assertIn(needle, result.stdout)

    def assertGreen(self, result: subprocess.CompletedProcess) -> None:
        self.assertEqual(result.stdout.splitlines()[:1], ["FOUNDATION VALIDATION: GREEN"], result.stdout + result.stderr)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")


# ------------------------------------------------------------------------------------------------
# One row per check: (test name, mutation, RED lines expected, options).  Each mutation breaks one
# subject of the real repository.  Options: regen=False leaves the inventory as committed,
# add=False leaves the index as it was (for an untracked or a deleted file).
# ------------------------------------------------------------------------------------------------

FI, PI, PH, PUB = WF + "foundation-integrity.yml", WF + "platforms-integrity.yml", WF + "design-platform-phase-a.yml", WF + "publish-release.yml"
RUN_F = "        run: python scripts/validate_foundation.py"
CHECKOUT = "      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4"
PERMS = "permissions:\n  contents: read"
PENDING = "pending"


def _delete_tracked(rel: str):
    return lambda r: r.git("rm", "-q", "--cached", rel) or (r.root / rel).unlink()


def _inventory(mutate):
    import json

    def apply(r: Repo) -> None:
        data = json.loads(r.read(INVENTORY))
        mutate(data)
        r.write(INVENTORY, json.dumps(data, ensure_ascii=False, separators=(",", ":")))

    return apply


def _untracked_link(r: Repo) -> None:
    r.before_end("ROADMAP.md", "[x](local-only.md)")
    r.git("add", "-A")
    r.run("scripts/generate_markdown_inventory.py", "--write")
    r.git("add", "-A")
    r.write("local-only.md", "# local\n")


RED_CASES = [
    # --- required files and their content (item 1) ---
    ("required_file_missing", _delete_tracked("COLLABORATION_STYLE.md"), ["missing required file: COLLABORATION_STYLE.md", "marker-governed file is missing from the checkout: COLLABORATION_STYLE.md"], {}),
    ("chapter_file_missing", _delete_tracked("foundation/governance/PROJECT_CONTEXT.md"), ["missing chapter file: foundation/governance/PROJECT_CONTEXT.md"], {}),
    ("required_document_emptied", lambda r: r.write("CHANGELOG.md", b""), ["required document is too small: CHANGELOG.md has 0 body bytes, minimum 600"], {}),
    ("required_document_reduced_to_marker", lambda r: r.write("ROADMAP.md", "<!-- END: MENQ_STANDARD_ROADMAP -->\n"), ["required document is too small: ROADMAP.md", "required document has no level-1 title: ROADMAP.md"], {}),
    ("required_document_without_title", lambda r: r.write("foundation/governance/PROJECT_CONTEXT.md", document(20, 20, title=False)), ["required document has no level-1 title: foundation/governance/PROJECT_CONTEXT.md"], {}),
    ("required_document_without_status", lambda r: r.write("foundation/governance/PROJECT_CONTEXT.md", document(20, 20, status=False)), ["required document has no Status metadata line: foundation/governance/PROJECT_CONTEXT.md"], {}),
    ("required_document_too_little_armenian", lambda r: r.write("foundation/governance/PROJECT_CONTEXT.md", document(1, 20).replace(ARM, "Կարճ։ ")), ["required document has too little Armenian text: foundation/governance/PROJECT_CONTEXT.md has 15 letters, minimum 50"], {}),
    ("required_document_too_little_english", lambda r: r.write("foundation/governance/PROJECT_CONTEXT.md", document(20, 1)), ["required document has too little English text: foundation/governance/PROJECT_CONTEXT.md"], {}),
    ("required_document_without_english_section", lambda r: r.write("foundation/governance/PROJECT_CONTEXT.md", document(20, 20).replace("## English\n", "")), ["required document lacks an Armenian or an English section: foundation/governance/PROJECT_CONTEXT.md"], {}),
    # --- END markers (item 2) ---
    ("end_marker_absent", lambda r: r.resub("ROADMAP.md", r"<!-- END: MENQ_STANDARD_ROADMAP -->", ""), ["missing ending marker in ROADMAP.md: <!-- END: MENQ_STANDARD_ROADMAP -->"], {}),
    ("end_marker_not_at_end", lambda r: r.write("ROADMAP.md", "<!-- END: MENQ_STANDARD_ROADMAP -->\n" + r.read("ROADMAP.md").replace("<!-- END: MENQ_STANDARD_ROADMAP -->", "")), ["ending marker is not at the end of ROADMAP.md: <!-- END: MENQ_STANDARD_ROADMAP -->"], {}),
    ("generic_end_marker_missing", lambda r: r.resub("AI_WORKING_CONTEXT.md", r"<!-- END: MENQ_STANDARD_AI_WORKING_CONTEXT -->", ""), ["missing ending marker at the end of AI_WORKING_CONTEXT.md"], {}),
    # --- bilingual parity (item 6) ---
    ("label_parity", lambda r: r.before_end("ROADMAP.md", "## Extra / Լրացուցիչ\n\n**HY:** Հայերեն տեքստ։"), ["bilingual label parity in ROADMAP.md section 'Extra / Լրացուցիչ': HY=1 EN=0"], {}),
    ("label_with_no_text", lambda r: r.before_end("ROADMAP.md", "## Extra / Լրացուցիչ\n\n**HY:** Հայերեն տեքստ։\n\n**EN:**"), ["bilingual label with no text in ROADMAP.md line", ": **EN:**"], {}),
    ("label_followed_by_a_heading", lambda r: r.before_end("ROADMAP.md", "## Extra / Լրացուցիչ\n\n**HY:** Հայերեն տեքստ։\n\n**EN:**\n\n## Next / Հաջորդ\n\nՀայերեն և English։"), ["bilingual label with no text in ROADMAP.md line", ": **EN:**"], {}),
    ("label_followed_by_another_label", lambda r: r.before_end("ROADMAP.md", "## Extra / Լրացուցիչ\n\n**HY:**\n**EN:** English text."), ["bilingual label with no text in ROADMAP.md line", ": **HY:**"], {}),
    ("english_only_section", lambda r: r.before_end("ROADMAP.md", "## A brand new section\n\n" + ENG * 2), ["English-only section in ROADMAP.md: 'A brand new section'"], {}),
    ("english_only_peer_section_after_language_block", lambda r: r.before_end("PROJECT_CONTEXT.md", "## A brand new section\n\n" + ENG * 2), ["English-only section in PROJECT_CONTEXT.md: 'A brand new section'"], {}),
    ("empty_language_section", lambda r: r.sub("foundation/governance/PROJECT_CONTEXT.md", "## English\n", "## English\n\n## Other / Այլ\n"), ["empty language section in foundation/governance/PROJECT_CONTEXT.md: 'English'"], {}),
    ("language_section_parity", lambda r: r.before_end("ROADMAP.md", "### English\n\nShort."), ["language section parity in ROADMAP.md: Հայերեն=0 English=1"], {}),
    # --- decision index (item 7) ---
    ("decision_index_missing_listed_id", lambda r: r.sub("DECISION_INDEX.md", "D-027", "D-0X7", 9), ["decision index missing D-027"], {}),
    ("decision_index_missing_listed_id_whose_file_is_gone", lambda r: (r.resub("DECISION_INDEX.md", r"^- `D-027`.*\n", ""), r.git("rm", "-q", "-f", "platforms/design/decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md")), ["- decision index missing D-027\n"], {}),
    ("decision_file_three_digits_not_indexed", lambda r: r.write("foundation/D-100-NEW-LAW.md", document(1, 1)), ["decision index missing D-100 (foundation/D-100-NEW-LAW.md)"], {}),
    ("decision_file_below_range_not_indexed", lambda r: r.write("foundation/D-019_OLD-LAW.md", document(1, 1)), ["decision index missing D-019 (foundation/D-019_OLD-LAW.md)"], {}),
    ("decision_id_is_matched_whole", lambda r: r.write("foundation/D-02-SHORT.md", document(1, 1)), ["decision index missing D-02 (foundation/D-02-SHORT.md)"], {}),
    # --- D-026 synchronization ---
    ("d026_reference_missing", lambda r: r.sub("AI_WORKING_CONTEXT.md", "D-026", "D-0X6", 99), ["AI_WORKING_CONTEXT.md missing D-026 reference: D-026"], {}),
    ("d026_synchronization_file_missing", _delete_tracked("NEXT_CHAT_HANDOFF.md"), ["D-026 synchronization file is missing from the checkout: NEXT_CHAT_HANDOFF.md"], {}),
    ("parity_control_missing", _delete_tracked("foundation/documentation/BILINGUAL_PARITY_ADDENDUM.md"), ["bilingual parity control is missing from the checkout: foundation/documentation/BILINGUAL_PARITY_ADDENDUM.md"], {}),
    ("ai_collaboration_still_pending", lambda r: r.before_end("foundation/PROJECT_CONTEXT.md", "AI Collaboration — Pending / Սպասման մեջ"), ["foundation context still marks AI Collaboration Pending"], {}),
    ("parity_control_without_sections", lambda r: r.sub("foundation/documentation/BILINGUAL_PARITY_ADDENDUM.md", "## English", "### English"), ["bilingual sections missing in foundation/documentation/BILINGUAL_PARITY_ADDENDUM.md"], {}),
    # --- links (item 5) ---
    ("link_plain_broken", lambda r: r.before_end("ROADMAP.md", "[x](missing-file.md)"), ["broken relative link in ROADMAP.md: missing-file.md"], {}),
    ("link_with_title_broken", lambda r: r.before_end("ROADMAP.md", '[x](missing-file.md "a title")'), ["broken relative link in ROADMAP.md: missing-file.md"], {}),
    ("link_in_angle_brackets_broken", lambda r: r.before_end("ROADMAP.md", "[x](<missing file.md>)"), ["broken relative link in ROADMAP.md: missing file.md"], {}),
    ("link_reference_style_broken", lambda r: r.before_end("ROADMAP.md", "[x][ref]\n\n[ref]: missing-file.md"), ["broken relative link in ROADMAP.md: missing-file.md"], {}),
    ("link_anchor_broken", lambda r: r.before_end("ROADMAP.md", "[x](README.md#no-such-anchor)"), ["broken anchor in ROADMAP.md: README.md#no-such-anchor"], {}),
    ("link_same_file_anchor_broken", lambda r: r.before_end("ROADMAP.md", "[x](#no-such-anchor)"), ["broken anchor in ROADMAP.md: #no-such-anchor"], {}),
    ("link_img_src_broken", lambda r: r.before_end("ROADMAP.md", '<img src="docs/missing.svg" alt="x">'), ["broken relative link in ROADMAP.md: docs/missing.svg"], {}),
    ("link_srcset_broken", lambda r: r.before_end("ROADMAP.md", '<picture><source srcset="docs/missing-2x.svg 2x"></picture>'), ["broken relative link in ROADMAP.md: docs/missing-2x.svg"], {}),
    ("link_to_untracked_file", _untracked_link, ["relative link in ROADMAP.md points to an untracked file: local-only.md"], {"regen": False, "add": False}),
    ("link_leaves_repository", lambda r: r.before_end("ROADMAP.md", "[x](../outside.md)"), ["relative link in ROADMAP.md leaves the repository: ../outside.md"], {}),
    # --- inventory ---
    ("inventory_missing", _delete_tracked(INVENTORY), ["missing canonical Markdown inventory: " + INVENTORY], {"regen": False, "add": False}),
    ("inventory_not_json", lambda r: r.write(INVENTORY, "{not json"), ["invalid canonical Markdown inventory:"], {"regen": False}),
    ("inventory_not_an_object", lambda r: r.write(INVENTORY, "[]"), ["Markdown inventory must be a JSON object"], {"regen": False}),
    ("inventory_files_not_a_list", _inventory(lambda d: d.__setitem__("files", {})), ["Markdown inventory 'files' must be a list"], {"regen": False}),
    ("inventory_count_mismatch", _inventory(lambda d: d.__setitem__("file_count", 1)), ["Markdown inventory count mismatch: declared 1"], {"regen": False}),
    ("inventory_entry_without_path", _inventory(lambda d: d["files"].__setitem__(0, "README.md")), ["Markdown inventory contains entries without a path"], {"regen": False}),
    ("inventory_unsorted", _inventory(lambda d: d["files"].reverse()), ["Markdown inventory paths are not sorted", "Markdown inventory path ordering differs from git ls-files"], {"regen": False}),
    ("inventory_duplicate", _inventory(lambda d: d["files"].insert(0, d["files"][0])), ["Markdown inventory contains duplicate paths"], {"regen": False}),
    ("inventory_missing_tracked_file", lambda r: r.write("docs/new.md", document(1, 1)), ["Markdown inventory missing tracked files: docs/new.md"], {"regen": False}),
    ("inventory_lists_untracked_file", _inventory(lambda d: d["files"].append({"path": "zzz.md", "bytes": 1, "sha256": "0" * 64})), ["Markdown inventory contains untracked files: zzz.md"], {"regen": False}),
    ("inventory_size_drift", _inventory(lambda d: d["files"][0].__setitem__("bytes", 1)), ["Markdown inventory size drift for "], {"regen": False}),
    ("inventory_sha_drift", _inventory(lambda d: d["files"][0].__setitem__("sha256", "0" * 64)), ["Markdown inventory SHA-256 drift for "], {"regen": False}),
    # --- never a traceback (item 8) ---
    ("no_tracked_markdown", lambda r: r.git("rm", "-q", "-r", "--cached", "--", "*.md"), ["tracked Markdown inventory is empty"], {"regen": False, "add": False}),
    ("tracked_markdown_deleted_from_disk", lambda r: (r.root / "FOUNDATION_V1_REMEDIATION_CHANGELOG.md").unlink(), ["tracked Markdown file is missing from the checkout: FOUNDATION_V1_REMEDIATION_CHANGELOG.md"], {"regen": False, "add": False}),
    ("tracked_markdown_not_utf8", lambda r: r.write("docs/latin1.md", b"# caf\xe9\n"), ["tracked Markdown file is not valid UTF-8: docs/latin1.md"], {}),
    ("not_a_git_repository", lambda r: shutil.rmtree(r.root / ".git", onerror=_force_remove), ["cannot enumerate tracked files with git ls-files -z"], {"regen": False, "add": False}),
    # --- workflow policy (items 3 and 4) ---
    ("workflow_permissions_missing", lambda r: r.sub(FI, PERMS + "\n", ""), [FI + ": missing top-level permissions block"], {"regen": False}),
    ("workflow_permissions_write_all", lambda r: r.sub(FI, PERMS, "permissions: write-all"), [FI + ": top-level permissions must be exactly 'contents: read'"], {"regen": False}),
    ("workflow_permissions_broad_block", lambda r: r.sub(FI, PERMS, "permissions:\n  contents: write\n  id-token: write\n  actions: write"), [FI + ": top-level permissions must be exactly 'contents: read'"], {"regen": False}),
    ("workflow_permissions_extra_scope", lambda r: r.sub(FI, PERMS, PERMS + "\n  id-token: write"), [FI + ": top-level permissions must be exactly 'contents: read'"], {"regen": False}),
    ("workflow_job_permissions_on_non_publishing_job", lambda r: r.sub(FI, "    runs-on: ubuntu-latest", "    runs-on: ubuntu-latest\n    permissions:\n      contents: write"), [FI + ": job 'validate' may not widen permissions beyond 'contents: read'"], {"regen": False}),
    ("workflow_publishing_job_permissions_widened", lambda r: r.sub(PUB, "    permissions:\n      contents: write", "    permissions:\n      contents: write\n      id-token: write"), [PUB + ": job 'foundation' may not widen permissions beyond 'contents: read'"], {"regen": False}),
    ("workflow_action_unpinned", lambda r: r.sub(FI, CHECKOUT, "      - uses: actions/checkout@v4"), [FI + ": action actions/checkout@v4 is not pinned to a full commit SHA"], {"regen": False}),
    ("workflow_action_pinned_to_a_short_sha", lambda r: r.sub(FI, CHECKOUT, "      - uses: actions/checkout@11d5960"), [FI + ": action actions/checkout@11d5960 is not pinned to a full commit SHA"], {"regen": False}),
    ("workflow_action_unpinned_flow_style", lambda r: r.sub(FI, CHECKOUT, "      - { uses: actions/checkout@main }"), [FI + ": action actions/checkout@main is not pinned to a full commit SHA"], {"regen": False}),
    ("workflow_action_unpinned_quoted_key", lambda r: r.sub(FI, CHECKOUT, '      - "uses": actions/checkout@main'), [FI + ": action actions/checkout@main is not pinned to a full commit SHA"], {"regen": False}),
    ("workflow_reusable_workflow_unpinned", lambda r: r.sub(FI, "jobs:\n", "jobs:\n  reuse:\n    uses: org/repo/.github/workflows/x.yml@main\n"), [FI + ": action org/repo/.github/workflows/x.yml@main is not pinned to a full commit SHA"], {"regen": False}),
    ("workflow_pipe_to_shell", lambda r: r.sub(FI, RUN_F, "        run: |\n          curl -fsSL https://example.com/x.sh | sh\n          python scripts/validate_foundation.py"), [FI + ": job 'validate' step 3: a download is piped into sh"], {"regen": False}),
    ("workflow_pipe_to_sudo_bash", lambda r: r.sub(FI, RUN_F, "        run: |\n          wget -qO- https://example.com/x.sh | sudo bash\n          python scripts/validate_foundation.py"), [FI + ": job 'validate' step 3: a download is piped into bash"], {"regen": False}),
    ("workflow_shell_substitution_download", lambda r: r.sub(FI, RUN_F, "        run: |\n          bash <(curl -fsSL https://example.com/x.sh)\n          python scripts/validate_foundation.py"), [FI + ": job 'validate' step 3: a download is executed through a shell substitution"], {"regen": False}),
    ("workflow_pull_request_target", lambda r: r.sub(FI, "  pull_request:", "  pull_request_target:"), [FI + ": pull_request_target is not allowed"], {"regen": False}),
    ("workflow_pull_request_target_in_a_list", lambda r: r.resub(PI, r"(?s)^on:\n.*?\n(?=permissions:)", "on: [pull_request, pull_request_target]\n\n"), [PI + ": pull_request_target is not allowed"], {"regen": False}),
    ("workflow_or_true", lambda r: r.sub(FI, RUN_F, RUN_F + " || true"), [FI + ": job 'validate' step 3: '|| true' swallows a failure"], {"regen": False}),
    ("workflow_or_exit_zero", lambda r: r.sub(PH, "run: python platforms/design/validation/validate_phase_a.py", "run: python platforms/design/validation/validate_phase_a.py || exit 0"), [PH + ": job 'validate-phase-a' step 7: '|| exit 0' swallows a failure"], {"regen": False}),
    ("workflow_step_continue_on_error", lambda r: r.sub(FI, RUN_F, "        continue-on-error: true\n" + RUN_F), [FI + ": job 'validate' step 3 sets continue-on-error"], {"regen": False}),
    ("workflow_job_continue_on_error", lambda r: r.sub(FI, "    runs-on: ubuntu-latest", "    runs-on: ubuntu-latest\n    continue-on-error: ${{ true }}"), [FI + ": job 'validate' sets continue-on-error"], {"regen": False}),
    ("workflow_not_yaml", lambda r: r.write(FI, "permissions:\nthis is {{{ not yaml at all\n"), [FI + ": cannot be parsed as a workflow (line 2: not a 'key: value' line"], {"regen": False}),
    ("workflow_pathologically_nested", lambda r: r.write(FI, "on: " + "[" * 20000 + "\n"), [FI + ": cannot be parsed as a workflow (RecursionError)"], {"regen": False}),
    ("workflow_tab_indented", lambda r: r.sub(FI, "  contents: read", "\tcontents: read"), [FI + ": cannot be parsed as a workflow (line", "indentation must be spaces only"], {"regen": False}),
    ("workflow_duplicate_key", lambda r: r.sub(FI, "jobs:\n", "permissions: write-all\n\njobs:\n"), [FI + ": cannot be parsed as a workflow (line", "duplicate key 'permissions'"], {"regen": False}),
    ("workflow_pnpm_without_frozen_lockfile", lambda r: r.sub(PH, "pnpm install --frozen-lockfile --ignore-scripts", "pnpm install --ignore-scripts"), [PH + ": job 'validate-phase-a' step 5: pnpm install must use --frozen-lockfile"], {"regen": False}),
    ("workflow_pnpm_no_frozen_lockfile", lambda r: r.sub(PH, "pnpm install --frozen-lockfile", "pnpm install --frozen-lockfile --no-frozen-lockfile"), [PH + ": pnpm install must use --frozen-lockfile"], {"regen": False}),
    ("workflow_required_workflow_deleted", lambda r: r.git("rm", "-q", "-f", PI), ["missing required workflow: " + PI], {"regen": False}),
    ("workflow_validator_replaced_by_echo", lambda r: r.sub(PI, "run: python scripts/validate_platforms.py", "run: echo ok"), [PI + ": job 'validate-platforms' does not run 'python scripts/validate_platforms.py' unconditionally"], {"regen": False}),
    ("workflow_validator_only_echoed", lambda r: r.sub(PI, "run: python scripts/validate_platforms.py", "run: echo scripts/validate_platforms.py"), [PI + ": job 'validate-platforms' does not run 'python scripts/validate_platforms.py' unconditionally"], {"regen": False}),
    ("workflow_validator_step_conditional", lambda r: r.sub(PI, "        run: python scripts/validate_platforms.py", "        if: false\n        run: python scripts/validate_platforms.py"), [PI + ": job 'validate-platforms' does not run 'python scripts/validate_platforms.py' unconditionally"], {"regen": False}),
    ("workflow_validator_piped", lambda r: r.sub(PI, "run: python scripts/validate_platforms.py", "run: python scripts/validate_platforms.py | tee log.txt"), [PI + ": job 'validate-platforms' does not run 'python scripts/validate_platforms.py' unconditionally"], {"regen": False}),
    ("workflow_validator_after_exit_zero", lambda r: r.sub(PI, "        run: python scripts/validate_platforms.py", "        run: |\n          exit 0\n          python scripts/validate_platforms.py"), [PI + ": job 'validate-platforms' does not run 'python scripts/validate_platforms.py' unconditionally"], {"regen": False}),
    ("workflow_validator_custom_shell", lambda r: r.sub(PI, "        run: python scripts/validate_platforms.py", "        shell: bash {0}\n        run: python scripts/validate_platforms.py"), [PI + ": job 'validate-platforms' does not run 'python scripts/validate_platforms.py' unconditionally"], {"regen": False}),
    ("workflow_validator_missing_required_argument", lambda r: r.sub(WF + "markdown-inventory-bootstrap.yml", "run: python scripts/generate_markdown_inventory.py --check", "run: python scripts/generate_markdown_inventory.py --write"), ["job 'validate' does not run 'python scripts/generate_markdown_inventory.py --check' unconditionally"], {"regen": False}),
    ("workflow_required_job_missing", lambda r: r.sub(PI, "  validate-platforms:", "  something-else:"), [PI + ": required job 'validate-platforms' is missing"], {"regen": False}),
    ("workflow_required_job_conditional", lambda r: r.sub(PI, "    runs-on: ubuntu-latest", "    if: false\n    runs-on: ubuntu-latest"), [PI + ": job 'validate-platforms' may not be conditional"], {"regen": False}),
    ("workflow_required_trigger_removed", lambda r: r.resub(PI, r"(?s)^on:\n.*?\n(?=permissions:)", "on:\n  workflow_dispatch:\n\n"), [PI + ": required workflow no longer runs on 'pull_request'"], {"regen": False}),
    ("workflow_required_script_not_tracked", lambda r: r.git("rm", "-q", "--cached", "scripts/validate_platforms.py"), [PI + ": required command names a script that is not tracked: scripts/validate_platforms.py"], {"regen": False, "add": False}),
    ("workflow_without_triggers", lambda r: r.resub(PI, r"(?s)^on:\n.*?\n(?=permissions:)", ""), [PI + ": missing or malformed 'on' triggers"], {"regen": False}),
    ("workflow_without_jobs", lambda r: r.resub(PI, r"(?s)^jobs:\n.*\Z", "jobs: none\n"), [PI + ": 'jobs' must be a non-empty mapping"], {"regen": False}),
    ("workflow_job_without_steps", lambda r: r.resub(PI, r"(?s)^    steps:\n.*\Z", "    timeout-minutes: 5\n"), [PI + ": job 'validate-platforms' has no steps"], {"regen": False}),
    ("workflow_job_not_a_mapping", lambda r: r.sub(FI, "jobs:\n", "jobs:\n  broken: 5\n"), [FI + ": job 'broken' is not a mapping"], {"regen": False}),
    ("workflow_run_not_a_script", lambda r: r.sub(PI, "run: python scripts/validate_platforms.py", "run: [python, scripts/validate_platforms.py]"), [PI + ": job 'validate-platforms' step 3 has a 'run' that is not a script"], {"regen": False}),
    ("workflow_step_neither_uses_nor_run", lambda r: r.sub(PI, "        run: python scripts/validate_platforms.py", "        with:\n          x: y"), [PI + ": job 'validate-platforms' step 3 is neither 'uses' nor 'run'"], {"regen": False}),
    ("workflow_deleted_from_disk", lambda r: (r.root / PI).unlink(), [PI + ": workflow is missing from the checkout"], {"regen": False, "add": False}),
    ("no_workflows_at_all", lambda r: r.git("rm", "-q", "-r", "-f", ".github/workflows"), ["no GitHub workflows found", "missing required workflow: " + FI], {"regen": False}),
]


def _red_test(mutate, needles, options):
    def test(self: Case) -> None:
        repo = self.fresh()
        mutate(repo)
        self.assertRed(self.verdict(repo, **options), *needles)

    return test


class RedCases(Case):
    """Generated: one test per row of RED_CASES."""


for _name, _mutate, _needles, _options in RED_CASES:
    assert not hasattr(RedCases, "test_" + _name), _name
    setattr(RedCases, "test_" + _name, _red_test(_mutate, _needles, _options))


class GreenControls(Case):
    def test_real_repository_is_green(self) -> None:
        self.assertGreen(self.verdict(self.fresh(), regen=False))

    def test_every_required_workflow_is_declared_and_present(self) -> None:
        present = {path.name for path in (REPO / ".github/workflows").glob("*.yml")}
        self.assertEqual(set(vf.REQUIRED_WORKFLOW_RUNS), present)

    def test_every_validator_the_real_workflows_run_is_declared_required(self) -> None:
        # Deleting a command from REQUIRED_WORKFLOW_RUNS must not go unnoticed: every validator,
        # check or test script a real workflow runs has to be declared for that workflow and job.
        gate = re.compile(r"(^|/)(validate_|check_|test_)\w*\.py$")
        seen = 0
        for path in sorted((REPO / ".github/workflows").glob("*.yml")):
            tree = vf.parse_workflow_yaml(path.read_bytes().decode("utf-8"))
            for job_id, job in tree["jobs"].items():
                declared = [command.split() for command in vf.REQUIRED_WORKFLOW_RUNS[path.name].get(job_id, ())]
                for step in job["steps"]:
                    for line in vf.logical_lines(step.get("run", "")):
                        words = vf.command_words(vf.split_commands(line)[0][0])
                        if words[:1] in (["python"], ["python3"]) and len(words) > 1 and (gate.search(words[1]) or "--check" in words):
                            seen += 1
                            with self.subTest(workflow=path.name, job=job_id, command=" ".join(words[1:3])):
                                self.assertTrue(any(d[0] == words[1] and set(d[1:]) <= set(words[2:]) for d in declared))
        self.assertGreaterEqual(seen, 20)

    def test_names_with_a_space_non_ascii_and_upper_case_extension_are_green(self) -> None:
        # Items 8 and 9: these were a traceback, a traceback, and a state no inventory satisfied.
        repo = self.fresh()
        # Counted here, not written down: this said "137" and went red the day the repository
        # gained two Markdown files, with nothing wrong in the validator.
        counted = re.search(r"(\d+) tracked Markdown files", self.verdict(repo).stdout)
        self.assertIsNotNone(counted)
        before = int(counted.group(1))
        note = "# Note / Նշում\n\n**HY:** Հայերեն տեքստ։\n\n**EN:** English text.\n\n<!-- END: NOTE -->\n"
        for rel in ("docs/my note.md", "docs/նշում.md", "docs/NOTE.MD"):
            repo.write(rel, note)
        result = self.verdict(repo)
        self.assertGreen(result)
        self.assertIn(f"{before + 3} tracked Markdown files", result.stdout)

    def test_valid_link_forms_are_green(self) -> None:
        repo = self.fresh()
        repo.before_end(
            "ROADMAP.md",
            '[a](README.md "a title") [b](<DECISION_INDEX.md>) [c][ref] [d](README.md#purpose--նպատակ) '
            '[e](#rule--կանոն) [f](foundation/) [g](docs/assets/front/cover-light.svg#gh-light-mode-only) '
            '[h](/README.md) [i](https://example.com/missing.md) <img src="docs/assets/front/cover-light.svg" alt="x">\n\n'
            "[ref]: PROJECT_CONTEXT.md",
        )
        self.assertGreen(self.verdict(repo))

    def test_bilingual_forms_that_must_stay_green(self) -> None:
        repo = self.fresh()
        repo.before_end(
            "ROADMAP.md",
            "## Extra / Լրացուցիչ\n\n**HY:**\nՀայերեն տեքստը հաջորդ տողում է։\n\n**EN:**\nThe English text is on the next line.\n\n"
            "## Short English heading\n\nFewer than twelve English words here.\n\n"
            "## Mixed / Խառը\n\n" + ENG * 2 + "\n\n" + ARM,
        )
        repo.before_end("PROJECT_CONTEXT.md", "### A subsection inside the English block\n\n" + ENG * 2)
        self.assertGreen(self.verdict(repo))

    def test_decision_file_named_in_the_index_is_green(self) -> None:
        repo = self.fresh()
        repo.write("foundation/D-100-NEW-LAW.md", document(1, 1))
        repo.before_end("DECISION_INDEX.md", "- `D-100` — [`foundation/D-100-NEW-LAW.md`](foundation/D-100-NEW-LAW.md)")
        self.assertGreen(self.verdict(repo))

    def test_validation_record_is_not_a_decision_file(self) -> None:
        repo = self.fresh()
        repo.write("foundation/D-100_VALIDATION_RECORD.md", document(1, 1))
        self.assertGreen(self.verdict(repo))

    def test_content_floors_sit_below_a_small_but_real_document(self) -> None:
        # 7 Armenian and 5 English sentences: above every floor, far smaller than any real required document.
        repo = self.fresh()
        repo.write("foundation/governance/PROJECT_CONTEXT.md", document(7, 5))
        self.assertGreen(self.verdict(repo))

    def test_body_floor_alone_is_red(self) -> None:
        # Enough letters in both languages, yet under the body floor: only the size line may appear.
        repo = self.fresh()
        repo.write("foundation/governance/PROJECT_CONTEXT.md", document(2, 5))
        result = self.verdict(repo)
        self.assertRed(result, "required document is too small: foundation/governance/PROJECT_CONTEXT.md")
        self.assertNotIn("too little", result.stdout)

    def test_extra_workflow_is_held_to_the_policy_and_may_be_green(self) -> None:
        repo = self.fresh()
        repo.write(WF + "extra.yaml", "on: push\n" + PERMS + "\njobs:\n  a:\n    runs-on: ubuntu-latest\n    continue-on-error: false\n    steps:\n    - run: echo ok\n      continue-on-error: false\n")
        self.assertGreen(self.verdict(repo, regen=False))
        repo.sub(WF + "extra.yaml", "- run: echo ok", "- uses: actions/checkout@v4")
        self.assertRed(self.verdict(repo, regen=False), WF + "extra.yaml: action actions/checkout@v4 is not pinned")


class YamlSubset(unittest.TestCase):
    """The strict parser, in process: what it accepts, what it refuses, and agreement with PyYAML."""

    def test_agrees_with_pyyaml_on_every_real_workflow(self) -> None:
        try:
            import yaml
        except ImportError:
            self.skipTest("PyYAML is not installed; CI installs no YAML library")
        workflows = sorted((REPO / ".github/workflows").glob("*.yml"))
        self.assertGreaterEqual(len(workflows), 9)
        for path in workflows:
            text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
            with self.subTest(workflow=path.name):
                self.assertEqual(vf.parse_workflow_yaml(text), yaml.load(text, Loader=yaml.BaseLoader))

    def test_accepted_forms(self) -> None:
        text = (
            "---\n# comment\non: [push, 'pull_request']\n\"quoted key\": \"a\\tb\"  # trailing\n"
            "empty:\nflow: { uses: a/b@c, n: [1, 2] }\nlist:\n- one\n- name: two\n  run: |\n    echo a  # kept\n\n    echo b\n"
            "- >-\n  folded\n  text\nkeep: |+\n  x\n\nlast: 'it''s'\n"
        )
        self.assertEqual(
            vf.parse_workflow_yaml(text),
            {
                "on": ["push", "pull_request"],
                "quoted key": "a\tb",
                "empty": "",
                "flow": {"uses": "a/b@c", "n": ["1", "2"]},
                "list": ["one", {"name": "two", "run": "echo a  # kept\n\necho b\n"}, "folded text"],
                "keep": "x\n\n",
                "last": "it's",
            },
        )

    def test_refused_forms(self) -> None:
        refused = {
            "anchor": ("a: &x 1\n", "line 1: unsupported YAML construct starting with '&'"),
            "alias": ("a: *x\n", "unsupported YAML construct starting with '*'"),
            "tag": ("a: !!str 1\n", "unsupported YAML construct starting with '!'"),
            "merge key": ("a:\n  <<: b\n", "line 2: not a 'key: value' line: '<<: b'"),
            "tab": ("a:\n\tb: 1\n", "line 2: indentation must be spaces only"),
            "tab in a block scalar": ("a: |\n\tx\n", "line 2: indentation must be spaces only"),
            "duplicate key": ("a: 1\na: 2\n", "line 2: duplicate key 'a'"),
            "duplicate flow key": ("a: {b: 1, b: 2}\n", "duplicate key 'b'"),
            "second document": ("a: 1\n---\nb: 2\n", "line 2: several documents in one file are not supported"),
            "multi-line plain scalar": ("a: one\n  two\n", "line 2: unexpected indentation"),
            "multi-line plain scalar in a sequence": ("a:\n  - b\n    c\n", "line 3: unexpected indentation"),
            "over-indented sequence entry": ("a:\n  - b\n    - c\n", "line 3: unexpected indentation"),
            "unterminated quote": ("a: \"one\n", "unterminated quoted scalar"),
            "unterminated flow": ("a: [one,\n  two]\n", "unterminated flow collection"),
            "text after a quoted value": ("a: \"one\" two\n", "unexpected text after a value: 'two'"),
            "colon in a plain scalar": ("a: b: c\n", "a plain scalar may not contain ': '"),
            "top-level sequence": ("- a\n", "line 1: the top level must be a mapping"),
            "indented top level": ("  a: 1\n", "line 1: the top level must not be indented"),
            "empty": ("# nothing\n", "the document is empty"),
            "complex key": ("? a\n: b\n", "line 1: not a 'key: value' line: '? a'"),
            "block scalar indentation indicator": ("a: |2\n    x\n", "unsupported block scalar header '|2'"),
            "folded scalar with a blank line": ("a: >\n  x\n\n  y\n", "a folded block scalar with blank or more-indented lines is not supported"),
            "under-indented block line": ("a:\n  b: |\n      x\n    y\n", "line 4: a block scalar line is indented less than its first line"),
            "unknown escape": ("a: \"\\q\"\n", "unsupported escape sequence \\q"),
            "byte-order mark": ("\ufeffa: 1\n", "line 1: a byte-order mark is not supported"),
            "nested inline sequence": ("a:\n- - b\n", "line 2: a sequence nested on one line is not supported"),
            "sequence after a key": ("a: - b\n", "a sequence entry may not follow a key on the same line"),
            "sequence where a key belongs": ("a: 1\n- b\n", "line 2: a sequence entry where a mapping key was expected"),
            "empty flow entry": ("a: [b, , c]\n", "empty entry in a flow collection"),
            "flow comment": ("a: [b, #c\n", "a comment inside a flow collection is not supported"),
            "malformed flow": ("a: [b c: d]\n", "malformed flow collection"),
            "flow mapping without a value": ("a: {b}\n", "a flow mapping entry needs 'key: value'"),
            "unsupported flow scalar": ("a: [*b]\n", "unsupported YAML construct starting with '*'"),
        }
        for name, (text, message) in refused.items():
            with self.subTest(form=name):
                with self.assertRaises(vf.WorkflowSyntaxError) as raised:
                    vf.parse_workflow_yaml(text)
                self.assertIn(message, str(raised.exception))

    def test_shell_helpers(self) -> None:
        script = "set -e\n# a comment\npython a.py \\\n  --flag\nnode <<'JS'\nif (a || true) {}\nJS\necho \"a | b\" && (cd x; pnpm install)\n"
        self.assertEqual(
            vf.logical_lines(script), ["set -e", "python a.py --flag", "node <<'JS'", 'echo "a | b" && (cd x; pnpm install)']
        )
        self.assertEqual(
            vf.split_commands('echo "a | b" && (cd x; pnpm install) 2>&1 | tee log # note'),
            [(["echo", "a | b"], "&&"), (["(cd", "x"], ";"), (["pnpm", "install)", "2>&1"], "|"), (["tee", "log"], "")],
        )
        self.assertEqual(vf.command_words(["FOO=1", "sudo", "(pnpm", "install"]), ["pnpm", "install"])
        self.assertEqual(vf.run_script_violations(script), ["pnpm install must use --frozen-lockfile"])
        self.assertEqual(vf.run_script_violations("test -f x || { echo missing; exit 1; }\ncurl -fsSL https://x -o y\n"), [])
        self.assertEqual(len(vf.run_script_violations("(cd x && pnpm i --frozen-lockfile --no-frozen-lockfile)")), 1)
        self.assertEqual(vf.run_script_violations("npx pnpm install --frozen-lockfile\npnpm build\n"), [])
        self.assertEqual(vf.run_script_violations("python a.py || :"), ["'|| :' swallows a failure: python a.py || :"])
        self.assertEqual(len(vf.run_script_violations("eval \"$(wget -qO- https://x)\"")), 1)
        self.assertEqual(len(vf.run_script_violations("curl -fsSL https://x | python3 -")), 1)
        self.assertTrue(vf.runs_command("set -euo pipefail\npython3 a.py \\\n  --check --x\n", "a.py --check"))
        self.assertFalse(vf.runs_command("python a.py && true\n", "a.py"))
        self.assertFalse(vf.runs_command("set +e\npython a.py\n", "a.py"))

    def test_anchor_slugs_follow_github(self) -> None:
        vf._TEXT_CACHE["x.md"] = ("# One `Two` / Երեք\n\n## Same\n\n## Same\n\n```\n# not a heading\n```\n<a id=\"explicit\"></a>\n", "")
        self.addCleanup(vf._TEXT_CACHE.pop, "x.md")
        self.addCleanup(vf._ANCHOR_CACHE.pop, "x.md", None)
        self.assertEqual(vf.anchors_of("x.md"), {"one-two--երեք", "same", "same-1", "explicit"})


class Guard(unittest.TestCase):
    def test_an_unexpected_exception_in_a_check_is_a_red_line_not_a_traceback(self) -> None:
        import contextlib
        import io

        def boom(*_args):
            raise RuntimeError("boom")

        self.addCleanup(setattr, vf, "validate_links", vf.validate_links)
        vf.validate_links = boom
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            code = vf.main()
        self.assertEqual(code, 1)
        self.assertIn("FOUNDATION VALIDATION: RED\n- internal validator error in links: RuntimeError: boom\n", captured.getvalue())


if __name__ == "__main__":
    unittest.main()
