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
CLOSURE = "platforms/design/D-025_POST_MERGE_CLOSURE_RECORD.md"
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
            present = isinstance(node, list) or keys[-1] in node
            assert present or value is not DELETE, f"{dotted} is absent: the deletion would change nothing"
            assert value is DELETE or not present or repr(node[keys[-1]]) != repr(value), f"{dotted} already holds {value!r}: the mutation would change nothing"
            if value is DELETE:
                del node[keys[-1]]
            else:
                node[keys[-1]] = value
        r.write(RECORD, json.dumps(data, ensure_ascii=False, indent=2))

    return apply


DELETE = object()
SNAPSHOT_KEY = vp.SNAPSHOT_KEY
SNAP = SNAPSHOT_KEY + "."
CURRENT = "current."
CONFUSED = vp.CONFUSED
LATEST = "evidenceCorrections.-1."
RELEASE = LATEST + "permanentRelease."
OBLIGATION = LATEST + "realConsumerObligation."

def met(second: str = "menqstudio/Scout", evidence: str = "PR #9, CI run GREEN", date: str = "2026-10-09"):
    """The correction records the obligation as met, and the current block restates it."""

    def apply(r: Repo) -> None:
        data = json.loads(r.read(RECORD))
        obligation = data["evidenceCorrections"][-1]["realConsumerObligation"]
        obligation["status"] = "met"
        obligation["secondRealConsumer"] = second
        obligation["progress"].append({"date": date, "consumer": second, "evidence": evidence})
        data["current"]["realConsumerObligation"] = "met"
        data["current"]["twoRealConsumerCondition"] = "evidenced"
        r.write(RECORD, json.dumps(data, ensure_ascii=False, indent=2))

    return apply


def registry(armenian: int, english: int, row: str = "| MenQ Design Platform | `platforms/design/validation/` |") -> str:
    return (
        "# Platform Registry / Platform-ների registry\n\n**Status / Կարգավիճակ:** Active\n\n"
        f"**HY:** {ARM * armenian}\n\n**EN:** {ENG * english}\n\n| Platform | Validation path |\n|---|---|\n{row}\n\n"
        "<!-- END: PLATFORM_REGISTRY -->\n"
    )


def both(*mutations):
    def apply(r: Repo) -> None:
        for mutate in mutations:
            mutate(r)

    return apply


def third_consumer(r: Repo) -> None:
    data = json.loads(r.read(RECORD))
    data["current"]["consumers"].append({"consumerId": "menqstudio/Webpage", "maturity": "M1"})
    r.write(RECORD, json.dumps(data, ensure_ascii=False, indent=2))


JULY_ACTION = "No D-025 action remains open. Govern future changes under locked change-control rules."
AGREE = "does not agree with the latest evidence correction"
IN_FORCE = "D-025 readiness record 'current.consumers' is not the list of consumers and maturities in force under the latest evidence correction"

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
    ("record_section_not_an_object", record(("mergeEvidence", 5)), ["D-025 readiness record field 'mergeEvidence' must be an object"], False),
    ("record_schema_version", record(("schemaVersion", 1)), ["D-025 readiness record schemaVersion must be 2"], False),
    ("record_schema_version_wrong_type", record(("schemaVersion", 2.0)), ["D-025 readiness record schemaVersion must be 2"], False),
    # --- the 2026-07-13 snapshot: present, complete, unchanged, and what the correction superseded ---
    ("snapshot_absent", record((SNAPSHOT_KEY, DELETE)), [f"D-025 readiness record field '{SNAPSHOT_KEY}' must be an object"], False),
    ("snapshot_field_missing", record((SNAP + "remainingAction", DELETE)), [f"D-025 readiness record '{SNAPSHOT_KEY}' is missing the field recorded on 2026-07-13: 'remainingAction'"], False),
    ("snapshot_rewritten", record((SNAP + "remainingAction.en", "Nothing to see.")), [f"D-025 readiness record '{SNAPSHOT_KEY}' is not the snapshot recorded on 2026-07-13 (its content hash differs)"], False),
    ("snapshot_section_not_an_object", record((SNAP + "evidenceSnapshot", 5)), [f"D-025 readiness record field '{SNAP}evidenceSnapshot' must be an object"], False),
    ("snapshot_status", record((SNAP + "status", "Draft")), [f"D-025 readiness record '{SNAP}status' is not the status recorded at lock ('Locked and GREEN')"], False),
    ("snapshot_workflow_conclusion", record((SNAP + "evidenceSnapshot.workflowConclusion", "failure")), ["D-025 readiness workflow evidence is not successful"], False),
    ("snapshot_cross_consumer", record((SNAP + "crossConsumerValidation", "RED")), [f"D-025 readiness record '{SNAPSHOT_KEY}' does not carry the cross-consumer and quality verdicts recorded at lock (GREEN)"], False),
    ("snapshot_quality", record((SNAP + "qualityAndAdoptionEvidence", "RED")), [f"D-025 readiness record '{SNAPSHOT_KEY}' does not carry the cross-consumer and quality verdicts recorded at lock (GREEN)"], False),
    ("snapshot_artifact_is_not_the_expired_one", record((LATEST + "expiredArtifactId", 1)), [f"D-025 evidence correction names an expired artifact (1) that is not the artifact of '{SNAPSHOT_KEY}' (8265108086)"], False),
    # --- the snapshot and the current block confused with each other ---
    ("confused_snapshot_field_at_top_level", record(("status", "Locked and GREEN")), [CONFUSED + "'status' is at the top level"], False),
    ("confused_current_field_inside_snapshot", record((SNAP + "decisionStatus", "Locked")), [CONFUSED + f"'decisionStatus' is inside '{SNAPSHOT_KEY}'"], False),
    ("confused_snapshot_field_inside_current", record((CURRENT + "crossConsumerValidation", "not evidenced")), [CONFUSED + "'crossConsumerValidation' is inside 'current'"], False),
    ("confused_current_action_is_the_july_text", record((CURRENT + "remainingAction.en", JULY_ACTION)), [CONFUSED + "'current.remainingAction.en' repeats the text recorded on 2026-07-13"], False),
    # --- the current block agrees with the latest correction ---
    ("current_absent", record(("current", DELETE)), ["D-025 readiness record field 'current' must be an object"], False),
    ("current_field_missing", record((CURRENT + "permanentReleaseTag", DELETE)), ["D-025 readiness record 'current' is missing the field 'permanentReleaseTag'"], False),
    ("current_unknown_field", record((CURRENT + "note", "x")), ["D-025 readiness record 'current' has the field 'note', which no rule ties to the latest evidence correction"], False),
    ("current_decision_status", record((CURRENT + "decisionStatus", "Draft")), ["'current.decisionStatus' ('Draft') " + AGREE + " (d025Status: 'Locked')"], False),
    ("current_obligation_lags_the_correction", both(met(), record((CURRENT + "realConsumerObligation", "open"))), ["'current.realConsumerObligation' ('open') " + AGREE], False),
    ("current_condition_lags_the_correction", both(met(), record((CURRENT + "twoRealConsumerCondition", "not evidenced"))), ["'current.twoRealConsumerCondition' ('not evidenced') " + AGREE], False),
    ("current_artifact_expiry", record((CURRENT + "workflowArtifactExpired", False)), ["'current.workflowArtifactExpired' (False) " + AGREE + " (artifactExpired: True)"], False),
    ("current_artifact_expiry_wrong_type", record((CURRENT + "workflowArtifactExpired", 1)), ["'current.workflowArtifactExpired' (1) " + AGREE], False),
    ("current_release_tag", record((CURRENT + "permanentReleaseTag", "design-platform-v9.9.9")), ["'current.permanentReleaseTag' ('design-platform-v9.9.9') " + AGREE], False),
    ("current_maturity_not_in_force", record((CURRENT + "consumers.0.maturity", "M1")), [IN_FORCE], False),
    ("current_lists_a_third_consumer", third_consumer, [IN_FORCE], False),
    ("current_consumer_carries_a_verdict", record((CURRENT + "consumers.0.verdict", "PASS")), [IN_FORCE], False),
    ("current_as_of_before_the_correction", record((CURRENT + "asOf", "2026-10-06")), ["D-025 readiness record 'current.asOf' ('2026-10-06') must be a date on or after the latest evidence correction (2026-10-07)"], False),
    ("current_as_of_not_a_date", record((CURRENT + "asOf", "today")), ["D-025 readiness record 'current.asOf' ('today') must be a date"], False),
    ("current_derived_from_elsewhere", record((CURRENT + "derivedFrom", "the correction record of 2026-10-07")), ["D-025 readiness record 'current.derivedFrom' does not name the latest entry of evidenceCorrections (2026-10-07)"], False),
    ("current_derived_from_an_older_correction", record((CURRENT + "derivedFrom", "the entry of evidenceCorrections dated 2026-09-01")), ["D-025 readiness record 'current.derivedFrom' does not name the latest entry of evidenceCorrections (2026-10-07)"], False),
    ("current_remaining_action_empty", record((CURRENT + "remainingAction.hy", " ")), ["D-025 readiness record 'current.remainingAction' must carry a non-empty 'hy' and 'en' text"], False),
    # --- the current block claims what the latest correction does not support ---
    ("current_claims_green", record((CURRENT + "remainingAction.en", "Everything is GREEN.")), ["D-025 readiness record 'current.remainingAction.en' claims GREEN; the latest evidence correction supports no GREEN verdict"], False),
    ("current_claims_the_obligation_is_met", record((CURRENT + "realConsumerObligation", "met")), ["D-025 readiness record 'current' claims the real-consumer obligation is met; the latest evidence correction records it as 'open'"], False),
    ("current_claims_the_condition_is_evidenced", record((CURRENT + "twoRealConsumerCondition", "evidenced")), ["D-025 readiness record 'current' claims the two-real-consumer condition is evidenced"], False),
    ("current_claims_m4", record((CURRENT + "consumers.1.maturity", "M4")), ["D-025 readiness record 'current' claims M4 for menq.design.consumer.release-console; the latest evidence correction supports M2"], False),
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
    # --- the snapshot's consumer maturity is the grade the correction superseded (item 13) ---
    ("snapshot_maturity_not_a_level", record((SNAP + "consumers.0.maturity", "M9-BANANA")), [f"D-025 readiness record '{SNAPSHOT_KEY}' maturity of menq.design.consumer.catalog is not one of M0-M4: 'M9-BANANA'"], False),
    ("snapshot_maturity_not_the_superseded_grade", record((LATEST + "consumerRegrade.1.previousMaturity", "M3")), [f"D-025 readiness record '{SNAPSHOT_KEY}' maturity of menq.design.consumer.release-console (M4) is not the grade the latest evidence correction superseded (M3)"], False),
    ("snapshot_maturity_consumer_missing", record((SNAP + "consumers", [])), [f"D-025 readiness record '{SNAPSHOT_KEY}' maturity of menq.design.consumer.catalog is not one of M0-M4: None"], False),
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
    ("audit_verdict", record((SNAP + "finalAudit.verdict", "RED")), [MERGE + "final post-lock audit is not GREEN and closed"], False),
    ("audit_transaction_open", record((SNAP + "finalAudit.transactionClosed", False)), [MERGE + "final post-lock audit is not GREEN and closed"], False),
    # --- required documents (items 16 and 17) ---
    ("required_file_deleted_from_disk", lambda r: (r.root / CLOSURE).unlink(), ["Missing required file: " + CLOSURE, "Cannot check required terms, file is missing from the checkout: " + CLOSURE], True),
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
    ("required_term_missing", lambda r: r.sub(CLOSURE, "Overall closure verdict — GREEN", "Overall closure verdict — pending", 99), [CLOSURE + " missing required term: Overall closure verdict — GREEN"], False),
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
        self.assertEqual(
            result.stdout.splitlines()[1:],
            [
                f"Validated {len(vp.REQUIRED_MARKERS)} required Platforms and D-025 canonical files.",
                "D-025 decision status: Locked; Owner approval: locked",
                "D-025 consumer maturity in force: catalog=M2, release-console=M2; real-consumer obligation: open; "
                "two-real-consumer condition: not evidenced",
                f"D-025 {SNAPSHOT_KEY} (history, not the state in force): status 'Locked and GREEN'; "
                "final post-lock audit: GREEN; transaction closed: True",
            ],
        )

    def test_a_consistent_record_prints_no_known_inconsistency(self) -> None:
        # Until 2026-10-09 the committed record showed M3/M4 at the top level beside M2/M2 in the
        # correction, and every run printed two KNOWN INCONSISTENCY lines.  The record no longer
        # contradicts itself, so nothing is printed; a record that does is RED (the cases above).
        result = self.verdict(self.fresh())
        self.assertGreen(result)
        self.assertNotIn("KNOWN INCONSISTENCY", result.stdout)
        self.assertNotIn("INCONSISTEN", result.stdout.upper())

    def test_the_snapshot_holds_the_july_values_and_the_current_block_the_corrected_ones(self) -> None:
        data = json.loads(self.fresh().read(RECORD))
        snapshot, current, latest = data[SNAPSHOT_KEY], data["current"], data["evidenceCorrections"][-1]
        self.assertEqual(sorted(snapshot), sorted(vp.SNAPSHOT_FIELDS))
        self.assertEqual(vp.snapshot_digest(snapshot), vp.SNAPSHOT_SHA256)
        self.assertEqual(vp.snapshot_digest(dict(reversed(list(snapshot.items())))), vp.SNAPSHOT_SHA256)
        self.assertEqual(snapshot["status"], "Locked and GREEN")
        self.assertEqual([item["maturity"] for item in snapshot["consumers"]], [item["previousMaturity"] for item in latest["consumerRegrade"]])
        self.assertEqual([item["maturity"] for item in current["consumers"]], [item["maturity"] for item in latest["consumerRegrade"]])
        self.assertEqual(sorted(current), sorted(vp.CURRENT_FIELDS))
        for name in vp.SNAPSHOT_FIELDS:
            self.assertNotIn(name, data)

    def test_summary_follows_the_record(self) -> None:
        repo = self.fresh()
        record((LATEST + "consumerRegrade.0.maturity", "M1"), (CURRENT + "consumers.0.maturity", "M1"))(repo)
        result = self.verdict(repo)
        self.assertGreen(result)
        self.assertIn("D-025 consumer maturity in force: catalog=M1, release-console=M2", result.stdout)

    def test_summary_status_is_the_current_block_not_a_literal(self) -> None:
        repo = self.fresh()
        record((LATEST + "d025Status", "Locked (amended)"), (CURRENT + "decisionStatus", "Locked (amended)"))(repo)
        result = self.verdict(repo)
        self.assertGreen(result)
        self.assertIn("D-025 decision status: Locked (amended); Owner approval: locked", result.stdout)

    def test_obligation_met_with_two_evidenced_consumers_is_green(self) -> None:
        repo = self.fresh()
        met()(repo)
        result = self.verdict(repo)
        self.assertGreen(result)
        self.assertIn("real-consumer obligation: met; two-real-consumer condition: evidenced", result.stdout)

    def test_a_later_as_of_date_is_green(self) -> None:
        repo = self.fresh()
        record((CURRENT + "asOf", "2027-01-01"))(repo)
        self.assertGreen(self.verdict(repo))

    def test_roadmap_is_no_longer_required_to_quote_what_was_corrected(self) -> None:
        # The three phrases were required terms of platforms/design/ROADMAP.md until 2026-10-09.
        repo = self.fresh()
        text = repo.read(DESIGN_ROADMAP)
        for phrase in ("M4 operational", "D-025 Locked and GREEN", "No open implementation, closure, or lock action remains"):
            text = text.replace(phrase, "[withdrawn]")
        repo.write(DESIGN_ROADMAP, text)
        self.assertNotIn(DESIGN_ROADMAP, vp.REQUIRED_TERMS)
        self.assertGreen(self.verdict(repo))

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
