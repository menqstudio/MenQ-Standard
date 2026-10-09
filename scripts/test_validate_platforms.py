#!/usr/bin/env python3
"""Tests for validate_platforms.py.

Every check in the validator has a test here that breaks exactly its subject in a temporary git
repository and asserts RED with the specific message, next to positive controls that are GREEN.
The fixture is a copy of this repository's own tracked files, so the real rules run against the
real content.  Fixture files are written as bytes, never as text, so the tests behave the same on
a platform that checks files out with CRLF.  Run:

    python scripts/test_validate_platforms.py
"""

from __future__ import annotations

import json
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
import validate_platforms as vp  # noqa: E402

SCRIPT = "scripts/validate_platforms.py"
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
    _BASE = Path(tempfile.mkdtemp(prefix="menq-platforms-base-"))
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


class Case(unittest.TestCase):
    maxDiff = None

    def fresh(self) -> Repo:
        root = Path(tempfile.mkdtemp(prefix="menq-platforms-"))
        self.addCleanup(shutil.rmtree, root, onerror=_force_remove)
        shutil.copytree(_BASE, root, dirs_exist_ok=True)
        return Repo(root)

    def verdict(self, repo: Repo, add: bool = True) -> subprocess.CompletedProcess:
        if add:
            repo.git("add", "-A")
        return repo.run(SCRIPT)

    def assertRed(self, result: subprocess.CompletedProcess, *needles: str) -> None:
        output = result.stdout + result.stderr
        self.assertNotIn("Traceback", output)
        self.assertEqual(result.returncode, 1, output)
        self.assertEqual(result.stdout.splitlines()[0], "PLATFORMS VALIDATION: RED", output)
        for needle in needles:
            self.assertIn(needle, result.stdout)

    def assertGreen(self, result: subprocess.CompletedProcess) -> None:
        self.assertEqual(result.stdout.splitlines()[:1], ["PLATFORMS VALIDATION: GREEN"], result.stdout + result.stderr)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")



RECORD = vp.RECORD_REL
REGISTRY = vp.REGISTRY_REL
CORRECTION = "platforms/design/D-025_EVIDENCE_CORRECTION_RECORD.md"
DESIGN_ROADMAP = "platforms/design/ROADMAP.md"
CHARTER = "platforms/design/PLATFORM_CHARTER.md"
LOCK = "platforms/design/D-025_LOCK_RECORD.md"
URL = "https://github.com/menqstudio/MenQ-Standard/releases/tag/"


def record(*assignments: tuple[str, object]):
    """A mutation that sets dotted paths in the readiness record ("a.b.-1.c"; a list index is an integer)."""

    def apply(r: Repo) -> None:
        data = json.loads(r.read(RECORD))
        for dotted, value in assignments:
            node = data
            keys = [int(key) if key.lstrip("-").isdigit() else key for key in dotted.split(".")]
            for key in keys[:-1]:
                node = node[key]
            assert value is DELETE or repr(node[keys[-1]]) != repr(value), f"{dotted} already holds {value!r}: the mutation would change nothing"
            if value is DELETE:
                del node[keys[-1]]
            else:
                node[keys[-1]] = value
        r.write(RECORD, json.dumps(data, ensure_ascii=False, indent=2))

    return apply


DELETE = object()
LATEST = "evidenceCorrections.-1."
RELEASE = LATEST + "permanentRelease."
OBLIGATION = LATEST + "realConsumerObligation."

def met(second: str = "menqstudio/Scout", evidence: str = "PR #9, CI run GREEN", date: str = "2026-10-09"):
    def apply(r: Repo) -> None:
        data = json.loads(r.read(RECORD))
        obligation = data["evidenceCorrections"][-1]["realConsumerObligation"]
        obligation["status"] = "met"
        obligation["secondRealConsumer"] = second
        obligation["progress"].append({"date": date, "consumer": second, "evidence": evidence})
        r.write(RECORD, json.dumps(data, ensure_ascii=False, indent=2))

    return apply


def registry(armenian: int, english: int, row: str = "| MenQ Design Platform | `platforms/design/validation/` |") -> str:
    return (
        "# Platform Registry / Platform-ների registry\n\n**Status / Կարգավիճակ:** Active\n\n"
        f"**HY:** {ARM * armenian}\n\n**EN:** {ENG * english}\n\n| Platform | Validation path |\n|---|---|\n{row}\n\n"
        "<!-- END: PLATFORM_REGISTRY -->\n"
    )


NEW_DOC = "# New / Նոր\n\n**HY:** Հայերեն տեքստ։\n\n**EN:** English text.\n\n<!-- END: NEW_DOC -->\n"
MERGE = "D-025 "

# (test name, mutation, RED lines expected, leave the index alone)
RED_CASES = [
    # --- the readiness record as a whole (item 12) ---
    ("record_empty_object", lambda r: r.write(RECORD, "{}"), ["D-025 readiness record must be a non-empty JSON object"], False),
    ("record_empty_list", lambda r: r.write(RECORD, "[]"), ["D-025 readiness record must be a non-empty JSON object"], False),
    ("record_non_empty_list", lambda r: r.write(RECORD, '[{"status": "Locked and GREEN"}]'), ["D-025 readiness record must be a non-empty JSON object"], False),
    ("record_not_json", lambda r: r.write(RECORD, "{not json"), ["Invalid D-025 readiness record:"], False),
    ("record_missing", lambda r: (r.root / RECORD).unlink(), ["Invalid D-025 readiness record:"], True),
    ("record_section_not_an_object", record(("evidenceSnapshot", 5)), ["D-025 readiness record field 'evidenceSnapshot' must be an object"], False),
    ("record_status", record(("status", "Draft")), ["D-025 readiness record is not Locked and GREEN"], False),
    ("record_workflow_conclusion", record(("evidenceSnapshot.workflowConclusion", "failure")), ["D-025 readiness workflow evidence is not successful"], False),
    ("record_cross_consumer", record(("crossConsumerValidation", "RED")), ["D-025 cross-consumer or quality evidence is not GREEN"], False),
    ("record_quality", record(("qualityAndAdoptionEvidence", "RED")), ["D-025 cross-consumer or quality evidence is not GREEN"], False),
    # --- the evidence correction ---
    ("correction_absent", record(("evidenceCorrections", [])), ["D-025 readiness record has no evidence correction"], False),
    ("correction_artifact_not_expired", record((LATEST + "artifactExpired", False)), ["D-025 evidence correction must record the expired workflow artifact"], False),
    ("correction_record_file_missing", record((LATEST + "record", "platforms/design/NO_SUCH_RECORD.md")), ["D-025 evidence correction record file is missing"], False),
    ("correction_regrade_above_m2", record((LATEST + "consumerRegrade.0.maturity", "M3")), ["menq.design.consumer.catalog must stay re-graded at or below M2 until independent evidence exists"], False),
    # --- the permanent release (item 14) ---
    ("release_url_not_a_github_release", record((RELEASE + "url", "https://example.com/release")), ["D-025 evidence correction must point to a permanent GitHub Release"], False),
    ("release_url_of_another_tag", record((RELEASE + "url", URL + "no-such-tag-ever")), ["D-025 permanent release URL is not the URL of its recorded tag"], False),
    ("release_url_and_tag_of_another_version", record((RELEASE + "url", URL + "design-platform-v9.9.9"), (RELEASE + "tag", "design-platform-v9.9.9")), ["D-025 permanent release tag is not the tag of the recorded release version (0.1.0-next.0)"], False),
    ("release_asset_of_another_version", record((RELEASE + "asset", "something-else.zip")), ["D-025 permanent release asset is not the bundle of the recorded release version"], False),
    ("release_digest_malformed", record((RELEASE + "assetSha256", "abc")), ["D-025 permanent release asset digest is missing"], False),
    ("release_digest_not_the_recorded_one", record((RELEASE + "assetSha256", "f" * 64)), ["D-025 permanent release asset digest is not the one stated in " + CORRECTION], False),
    ("release_source_commit_not_the_recorded_one", record((RELEASE + "sourceCommit", "0" * 40)), ["D-025 permanent release source commit is not the one stated in " + CORRECTION], False),
    ("release_url_not_in_the_correction_document", lambda r: r.sub(CORRECTION, "releases/tag/design-platform-v0.1.0-next.0", "releases/tag/elsewhere", 99), ["D-025 permanent release URL is not the one stated in " + CORRECTION], False),
    # --- the real-consumer obligation (item 15) ---
    ("obligation_status_unknown", record((OBLIGATION + "status", "done")), ["D-025 real-consumer obligation status is missing"], False),
    ("obligation_met_without_a_second_consumer", record((OBLIGATION + "status", "met")), ["D-025 real-consumer obligation is marked met without two distinct named real consumers"], False),
    ("obligation_met_with_one_consumer_twice", met(second="menqstudio/WEBPAGE"), ["D-025 real-consumer obligation is marked met without two distinct named real consumers"], False),
    ("obligation_met_with_an_unnamed_consumer", met(second="a team to be selected"), ["D-025 real-consumer obligation is marked met without two distinct named real consumers"], False),
    ("obligation_met_without_evidence", met(evidence=" "), ["D-025 real-consumer obligation is marked met without two distinct named real consumers"], False),
    ("obligation_met_without_a_date", met(date="soon"), ["D-025 real-consumer obligation is marked met without two distinct named real consumers"], False),
    # --- the top-level consumer maturity (item 13) ---
    ("maturity_not_a_level", record(("consumers.0.maturity", "M9-BANANA")), ["D-025 readiness record top-level maturity of menq.design.consumer.catalog is not one of M0-M4: 'M9-BANANA'"], False),
    ("maturity_not_the_superseded_grade", record(("consumers.1.maturity", "M3")), ["D-025 readiness record top-level maturity of menq.design.consumer.release-console (M3) is not the grade the latest evidence correction superseded (M4)"], False),
    ("maturity_consumer_missing", record(("consumers", [])), ["D-025 readiness record top-level maturity of menq.design.consumer.catalog is not one of M0-M4: None"], False),
    # --- merge, authority and audit evidence ---
    ("merge_not_merged", record(("mergeEvidence.merged", False)), [MERGE + "merge evidence does not confirm merge"], False),
    ("merge_implementation_pr", record(("mergeEvidence.implementationPullRequest", 9)), [MERGE + "implementation merge evidence does not identify PR #3"], False),
    ("merge_closure_pr", record(("mergeEvidence.closurePullRequest", 9)), [MERGE + "closure merge evidence does not identify PR #4"], False),
    ("merge_lock_pr", record(("mergeEvidence.lockPullRequest", 9)), [MERGE + "lock merge evidence does not identify PR #5"], False),
    ("merge_implementation_commit", record(("mergeEvidence.implementationMergeCommit", "0" * 40)), [MERGE + "implementation merge commit evidence is incorrect"], False),
    ("merge_closure_commit", record(("mergeEvidence.closureMergeCommit", "0" * 40)), [MERGE + "closure merge commit evidence is incorrect"], False),
    ("merge_lock_commit", record(("mergeEvidence.lockMergeCommit", "0" * 40)), [MERGE + "lock merge commit evidence is incorrect"], False),
    ("merge_validated_lock_head", record(("mergeEvidence.validatedLockHead", "0" * 40)), [MERGE + "validated lock head evidence is incorrect"], False),
    ("merge_tree_difference", record(("mergeEvidence.treeDifferenceCount", 2)), [MERGE + "lock tree equivalence is not exact"], False),
    ("merge_tree_difference_false", record(("mergeEvidence.treeDifferenceCount", False)), [MERGE + "lock tree equivalence is not exact"], False),
    ("authority_ready_for_review", record(("authority.readyForReviewAuthorized", False)), [MERGE + "readiness record does not preserve Owner ready/merge authority"], False),
    ("authority_merge", record(("authority.mergeAuthorized", False)), [MERGE + "readiness record does not preserve Owner ready/merge authority"], False),
    ("authority_lock", record(("authority.lockAuthorized", False)), [MERGE + "readiness record does not preserve Owner lock authority"], False),
    ("authority_approval_status", record(("authority.ownerApprovalStatus", "pending")), [MERGE + "Owner approval state is not Locked"], False),
    ("authority_owner", record(("authority.owner", "Someone Else")), [MERGE + "lock owner is not recorded"], False),
    ("audit_verdict", record(("finalAudit.verdict", "RED")), [MERGE + "final post-lock audit is not GREEN and closed"], False),
    ("audit_transaction_open", record(("finalAudit.transactionClosed", False)), [MERGE + "final post-lock audit is not GREEN and closed"], False),
    # --- required documents (items 16 and 17) ---
    ("required_file_deleted_from_disk", lambda r: (r.root / DESIGN_ROADMAP).unlink(), ["Missing required file: " + DESIGN_ROADMAP, "Cannot check required terms, file is missing from the checkout: " + DESIGN_ROADMAP], True),
    ("required_file_not_utf8", lambda r: r.write(CHARTER, b"# caf\xe9\n"), ["Required file is not valid UTF-8: " + CHARTER], False),
    ("ending_marker_misplaced", lambda r: r.write(CHARTER, r.read(CHARTER) + "\ntrailing text\n"), ["Missing or misplaced ending marker: " + CHARTER], False),
    ("registry_reduced_to_three_lines", lambda r: r.write(REGISTRY, "**HY:** x\n**EN:** x\n<!-- END: PLATFORM_REGISTRY -->\n"), ["Required document is too small: " + REGISTRY + " has 18 body bytes, minimum 1200"], False),
    ("required_document_without_title", lambda r: r.resub(REGISTRY, r"^# .*\n", ""), ["Required document has no level-1 title: " + REGISTRY], False),
    ("required_document_without_status", lambda r: r.resub(REGISTRY, r"^\*\*Status[^\n]*\n", ""), ["Required document has no Status metadata line: " + REGISTRY], False),
    ("required_document_too_little_armenian", lambda r: r.resub(REGISTRY, r"[Ա-֏]+", "", 0), ["Required document has too little Armenian text: " + REGISTRY], False),
    ("required_document_too_little_english", lambda r: r.write(REGISTRY, registry(30, 1)), ["Required document has too little English text: " + REGISTRY], False),
    ("registry_without_a_row", lambda r: r.write(REGISTRY, registry(30, 30, row="")), [REGISTRY + " registers no Platform (the registry table has no row)"], False),
    ("registry_without_a_row_for_a_platform", lambda r: r.write("platforms/data/README.md", NEW_DOC), [REGISTRY + " has no row for the platform directory platforms/data/"], False),
    ("registry_mentions_a_platform_outside_the_table", lambda r: (r.write("platforms/data/README.md", NEW_DOC), r.before_end(REGISTRY, "**HY:** `platforms/data/` դեռ գրանցված չէ։\n\n**EN:** `platforms/data/` is not registered yet.")), [REGISTRY + " has no row for the platform directory platforms/data/"], False),
    ("bilingual_canonical_sections_missing", lambda r: r.sub(LOCK, "## English", "### English"), ["Missing bilingual canonical sections: " + LOCK], False),
    ("platforms_markdown_without_english", lambda r: r.write("platforms/design/NEW.md", NEW_DOC.replace("**EN:** English text.\n\n", "")), ["Missing Armenian or English section: platforms/design/NEW.md"], False),
    ("platforms_markdown_without_armenian", lambda r: r.write("platforms/design/NEW.md", NEW_DOC.replace("**HY:** Հայերեն տեքստ։\n\n", "")), ["Missing Armenian or English section: platforms/design/NEW.md"], False),
    ("platforms_markdown_without_end_marker", lambda r: r.write("platforms/design/my new.md", NEW_DOC.replace("<!-- END: NEW_DOC -->\n", "")), ["Missing ending marker: platforms/design/my new.md"], False),
    ("required_term_missing", lambda r: r.sub(DESIGN_ROADMAP, "M4 operational", "M4 planned", 99), [DESIGN_ROADMAP + " missing required term: M4 operational"], False),
    ("tracked_markdown_deleted_from_disk", lambda r: (r.root / "platforms/design/brand-expression/components/Field/README.md").unlink(), ["Tracked Markdown file is missing from the checkout: platforms/design/brand-expression/components/Field/README.md"], True),
    ("not_a_git_repository", lambda r: shutil.rmtree(r.root / ".git", onerror=_force_remove), ["cannot enumerate tracked files with git ls-files -z"], True),
]


def _red_test(mutate, needles, leave_index):
    def test(self: Case) -> None:
        repo = self.fresh()
        mutate(repo)
        self.assertRed(self.verdict(repo, add=not leave_index), *needles)

    return test


class RedCases(Case):
    """Generated: one test per row of RED_CASES."""


for _name, _mutate, _needles, _leave in RED_CASES:
    assert not hasattr(RedCases, "test_" + _name), _name
    setattr(RedCases, "test_" + _name, _red_test(_mutate, _needles, _leave))


class GreenControls(Case):
    def test_real_repository_is_green_and_its_summary_is_read_from_the_record(self) -> None:
        result = self.verdict(self.fresh())
        self.assertGreen(result)
        self.assertIn(f"Validated {len(vp.REQUIRED_MARKERS)} required Platforms and D-025 canonical files.", result.stdout)
        self.assertIn("D-025 readiness record: Locked and GREEN; Owner approval: locked", result.stdout)
        self.assertIn("D-025 final post-lock audit: GREEN; transaction closed: True", result.stdout)
        self.assertIn("D-025 consumer maturity in force: catalog=M2, release-console=M2; real-consumer obligation: open", result.stdout)

    def test_known_inconsistency_is_printed_while_the_record_contradicts_itself(self) -> None:
        # Item 13, the part that is NOT fixed: the committed record shows M3/M4 at the top level
        # and M2/M2 in the correction.  The validator says so on every run instead of hiding it.
        result = self.verdict(self.fresh())
        self.assertGreen(result)
        notes = [line for line in result.stdout.splitlines() if line.startswith("KNOWN INCONSISTENCY: ")]
        self.assertEqual(len(notes), 2, result.stdout)
        self.assertIn("still shows menq.design.consumer.catalog at M3", notes[0])
        self.assertIn("re-graded it to M2", notes[0])
        self.assertIn("still shows menq.design.consumer.release-console at M4", notes[1])

    def test_no_inconsistency_line_once_the_record_agrees_with_itself(self) -> None:
        repo = self.fresh()
        record(
            ("consumers.0.maturity", "M2"), ("consumers.1.maturity", "M2"),
            (LATEST + "consumerRegrade.0.previousMaturity", "M2"), (LATEST + "consumerRegrade.1.previousMaturity", "M2"),
        )(repo)
        result = self.verdict(repo)
        self.assertGreen(result)
        self.assertNotIn("KNOWN INCONSISTENCY", result.stdout)

    def test_summary_follows_the_record(self) -> None:
        repo = self.fresh()
        record((LATEST + "consumerRegrade.0.maturity", "M1"))(repo)
        result = self.verdict(repo)
        self.assertGreen(result)
        self.assertIn("D-025 consumer maturity in force: catalog=M1, release-console=M2", result.stdout)

    def test_obligation_met_with_two_evidenced_consumers_is_green(self) -> None:
        repo = self.fresh()
        met()(repo)
        result = self.verdict(repo)
        self.assertGreen(result)
        self.assertIn("real-consumer obligation: met", result.stdout)

    def test_registered_second_platform_is_green(self) -> None:
        repo = self.fresh()
        repo.write("platforms/data/README.md", NEW_DOC)
        repo.sub(REGISTRY, "\n\n## Admission checklist", "\n| MenQ Data Platform | Proposed | MenQ Owner | none | Data | none | `platforms/data/` |\n\n## Admission checklist")
        self.assertGreen(self.verdict(repo))

    def test_names_with_a_space_and_non_ascii_are_green(self) -> None:
        repo = self.fresh()
        for rel in ("platforms/design/my note.md", "platforms/design/նշում.md", "platforms/design/NOTE.MD"):
            repo.write(rel, NEW_DOC)
        self.assertGreen(self.verdict(repo))

    def test_untracked_markdown_is_not_validated(self) -> None:
        repo = self.fresh()
        repo.write("platforms/design/untracked.md", "no languages, no marker\n")
        self.assertGreen(self.verdict(repo, add=False))

    def test_content_floors_sit_below_a_small_but_real_document(self) -> None:
        repo = self.fresh()
        repo.write(REGISTRY, registry(8, 12))
        self.assertGreen(self.verdict(repo))

    def test_body_floor_alone_is_red(self) -> None:
        repo = self.fresh()
        repo.write(REGISTRY, registry(3, 10))
        result = self.verdict(repo)
        self.assertRed(result, "Required document is too small: " + REGISTRY)
        self.assertNotIn("too little", result.stdout)


class Guard(unittest.TestCase):
    def test_an_unexpected_exception_in_a_check_is_a_red_line_not_a_traceback(self) -> None:
        import contextlib
        import io

        def boom(*_args):
            raise RuntimeError("boom")

        self.addCleanup(setattr, vp, "validate_registry", vp.validate_registry)
        vp.validate_registry = boom
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            code = vp.main()
        self.assertEqual(code, 1)
        self.assertIn("PLATFORMS VALIDATION: RED\n- internal validator error: RuntimeError: boom\n", captured.getvalue())


if __name__ == "__main__":
    unittest.main()
