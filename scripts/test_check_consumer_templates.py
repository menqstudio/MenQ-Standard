#!/usr/bin/env python3
"""Tests for check_consumer_templates.py.

The fixture is a temporary git repository holding a byte copy of this checkout's two workflow
templates and of the reusable workflow.  Each rule has a test that breaks exactly its subject and
asserts RED with the specific message, next to GREEN controls.  Run:

    python scripts/test_check_consumer_templates.py
"""

from __future__ import annotations

import contextlib
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
import check_consumer_templates as cct  # noqa: E402
import validate_foundation as vf  # noqa: E402

CONFORMANCE = "consumer/templates/menq-standard-conformance.yml"
UPDATE = "consumer/templates/menq-standard-update.yml"
REUSABLE = ".github/workflows/consumer-conformance.yml"
CHECKOUT = "      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4\n"
PR_CREATE = '          gh pr create --base "$base" --head "$branch" --title "MenQ Standard $old -> $new" --body-file "$report/body.md"\n'
PUSH = '          git push --quiet origin "$branch"\n'


def git(root: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


class Fixture:
    def __init__(self, case: unittest.TestCase) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="menq-templates-"))
        case.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        for rel in (CONFORMANCE, UPDATE, REUSABLE):
            self.write(rel, (REPO / rel).read_bytes())
        git(self.root, "init", "--quiet")
        git(self.root, "config", "core.autocrlf", "false")
        self.add()

    def write(self, rel: str, data: bytes) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def add(self) -> None:
        git(self.root, "add", "--all")

    def sub(self, rel: str, old: str, new: str) -> None:
        text = (self.root / rel).read_bytes().decode("utf-8")
        assert text.count(old) == 1, f"{old!r} occurs {text.count(old)} times in {rel}: the mutation would not be exact"
        self.write(rel, text.replace(old, new).encode("utf-8"))

    def run(self) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = cct.main([str(self.root)])
        return code, out.getvalue()


class Case(unittest.TestCase):
    def assert_red(self, fixture: Fixture, *fragments: str) -> str:
        code, out = fixture.run()
        self.assertNotIn("Traceback", out)
        self.assertEqual(code, 1, out)
        self.assertEqual(out.splitlines()[0], "CONSUMER TEMPLATES: RED", out)
        for fragment in fragments:
            self.assertIn(fragment, out)
        return out

    def mutated(self, rel: str, old: str, new: str, *fragments: str) -> str:
        fixture = Fixture(self)
        fixture.sub(rel, old, new)
        return self.assert_red(fixture, *fragments)


class GreenControls(Case):
    def test_this_repository_is_green(self) -> None:
        self.assertEqual(cct.check(REPO), ([], 2))

    def test_fixture_is_green(self) -> None:
        self.assertEqual(Fixture(self).run(), (0, "CONSUMER TEMPLATES: GREEN (2 templates and the reusable workflow)\n"))

    def test_crlf_checkout_is_green(self) -> None:
        fixture = Fixture(self)
        for rel in (CONFORMANCE, UPDATE, REUSABLE):
            fixture.write(rel, (fixture.root / rel).read_bytes().replace(b"\n", b"\r\n"))
        self.assertEqual(fixture.run()[0], 0)

    def test_the_foundation_validator_does_not_read_templates_as_workflows(self) -> None:
        listing = subprocess.run(["git", "ls-files", "-z"], cwd=REPO, check=True, capture_output=True).stdout.decode("utf-8")
        tracked = sorted(part for part in listing.split("\0") if part)
        self.assertIn(CONFORMANCE, tracked)
        self.assertIn(UPDATE, tracked)
        errors: list[str] = []
        count = vf.validate_workflows(errors, tracked)
        self.assertEqual(count, len([rel for rel in tracked if rel.startswith(".github/workflows/")]))
        self.assertEqual([error for error in errors if "consumer/templates" in error], [])

    def test_the_update_template_would_break_this_repositorys_own_policy(self) -> None:
        # The reason it is a template and not a workflow here: as a workflow it is RED by name.
        errors: list[str] = []
        text = (REPO / UPDATE).read_bytes().decode("utf-8").replace(cct.KIT_DIR_PLACEHOLDER, "menq-standard")
        vf.check_workflow("menq-standard-update.yml", ".github/workflows/menq-standard-update.yml", text, set(), errors)
        self.assertEqual(errors, [".github/workflows/menq-standard-update.yml: top-level permissions must be exactly 'contents: read'"])

    def test_placeholders_are_the_checkers_own(self) -> None:
        checker = __import__("generate_kit_manifest").load_checker(REPO)
        self.assertEqual((cct.COMMIT_PLACEHOLDER, cct.KIT_DIR_PLACEHOLDER), (checker.COMMIT_PLACEHOLDER, checker.KIT_DIR_PLACEHOLDER))
        self.assertEqual(sorted(f"templates/{name}" for name in cct.TEMPLATES), sorted(checker.WORKFLOW_TEMPLATES.values()))


class Declaration(Case):
    def test_undeclared_template(self) -> None:
        fixture = Fixture(self)
        fixture.write("consumer/templates/extra.yml", b"on: push\n")
        fixture.add()
        self.assert_red(fixture, "consumer/templates/extra.yml: is not a declared template")

    def test_declared_template_not_tracked(self) -> None:
        fixture = Fixture(self)
        git(fixture.root, "rm", "--quiet", "--cached", UPDATE)
        self.assert_red(fixture, f"{UPDATE}: declared template is not tracked by git")

    def test_template_missing_from_the_checkout(self) -> None:
        fixture = Fixture(self)
        (fixture.root / CONFORMANCE).unlink()
        self.assert_red(fixture, f"{CONFORMANCE}: is missing from the checkout or not valid UTF-8")

    def test_template_that_is_not_a_workflow(self) -> None:
        fixture = Fixture(self)
        fixture.write(UPDATE, b"permissions:\nthis is {{{ not yaml\n")
        self.assert_red(fixture, f"{UPDATE}: cannot be parsed as a workflow (line 2")

    def test_not_a_git_repository(self) -> None:
        fixture = Fixture(self)
        shutil.rmtree(fixture.root / ".git")
        self.assert_red(fixture, "cannot enumerate tracked files with git ls-files -z")


class Pinning(Case):
    def test_action_on_a_tag(self) -> None:
        self.mutated(UPDATE, CHECKOUT, "      - uses: actions/checkout@v4\n", f"{UPDATE}: action actions/checkout@v4 is not pinned to a full commit SHA")

    def test_placeholder_on_another_action(self) -> None:
        self.mutated(
            UPDATE, CHECKOUT, "      - uses: actions/checkout@__MENQ_STANDARD_COMMIT__\n",
            f"{UPDATE}: the commit placeholder may pin only menqstudio/MenQ-Standard/.github/workflows/consumer-conformance.yml, not actions/checkout@__MENQ_STANDARD_COMMIT__",
        )

    def test_reusable_workflow_called_on_a_branch(self) -> None:
        self.mutated(CONFORMANCE, "@__MENQ_STANDARD_COMMIT__", "@main", "consumer-conformance.yml@main is not pinned to a full commit SHA")

    def test_placeholder_the_installer_does_not_fill(self) -> None:
        self.mutated(UPDATE, 'checker="__MENQ_KIT_DIR__/', 'checker="__MENQ_KIT__/', f"{UPDATE}: holds a placeholder the installer does not fill in")


class Permissions(Case):
    def test_update_template_widened(self) -> None:
        self.mutated(UPDATE, "  pull-requests: write\n", "  pull-requests: write\n  id-token: write\n", f"{UPDATE}: top-level permissions must be exactly 'contents: write, pull-requests: write'")

    def test_conformance_template_given_write(self) -> None:
        self.mutated(CONFORMANCE, "  contents: read\n", "  contents: write\n", f"{CONFORMANCE}: top-level permissions must be exactly 'contents: read'")

    def test_permissions_removed(self) -> None:
        self.mutated(CONFORMANCE, "permissions:\n  contents: read\n", "", f"{CONFORMANCE}: top-level permissions must be exactly 'contents: read'")

    def test_job_level_permissions(self) -> None:
        self.mutated(UPDATE, "    runs-on: ubuntu-latest\n", "    runs-on: ubuntu-latest\n    permissions:\n      actions: write\n", f"{UPDATE}: job 'update' may not set its own permissions")


class Triggers(Case):
    def test_pull_request_target(self) -> None:
        self.mutated(CONFORMANCE, "  pull_request:\n", "  pull_request_target:\n", f"{CONFORMANCE}: pull_request_target is not allowed", f"{CONFORMANCE}: must run on 'pull_request'")

    def test_update_template_on_a_pull_request(self) -> None:
        self.mutated(UPDATE, "  workflow_dispatch:\n", "  workflow_dispatch:\n  pull_request:\n", f"{UPDATE}: may not run on 'pull_request' (allowed: schedule, workflow_dispatch)")

    def test_update_template_on_a_push(self) -> None:
        self.mutated(UPDATE, "  workflow_dispatch:\n", "  workflow_dispatch:\n  push:\n", f"{UPDATE}: may not run on 'push'")

    def test_update_template_without_its_schedule(self) -> None:
        self.mutated(UPDATE, '  schedule:\n    - cron: "17 5 * * 1"\n', "", f"{UPDATE}: must run on 'schedule'")

    def test_conformance_template_without_pull_request(self) -> None:
        self.mutated(CONFORMANCE, "  pull_request:\n", "", f"{CONFORMANCE}: must run on 'pull_request'")

    def test_no_triggers(self) -> None:
        self.mutated(CONFORMANCE, "on:\n  pull_request:\n  push:\n    branches:\n      - main\n      - master\n  workflow_dispatch:\n", "", f"{CONFORMANCE}: missing or malformed 'on' triggers")


class Scripts(Case):
    def test_continue_on_error_on_a_step(self) -> None:
        self.mutated(UPDATE, "      - name: Fetch MenQ Standard (public, no token)\n", "      - name: Fetch MenQ Standard (public, no token)\n        continue-on-error: true\n", f"{UPDATE}: job 'update' step 3 sets continue-on-error")

    def test_continue_on_error_on_a_job(self) -> None:
        self.mutated(UPDATE, "    runs-on: ubuntu-latest\n", "    runs-on: ubuntu-latest\n    continue-on-error: true\n", f"{UPDATE}: job 'update' sets continue-on-error")

    def test_download_piped_into_a_shell(self) -> None:
        out = self.mutated(UPDATE, PUSH, PUSH + "          curl -fsSL https://example.invalid/x.sh | sh\n", f"{UPDATE}: job 'update' step 4: a download is piped into sh")
        self.assertIn("downloads with curl or wget", out)

    def test_failure_swallowed(self) -> None:
        self.mutated(UPDATE, PUSH, PUSH.rstrip("\n") + " || true\n", f"{UPDATE}: job 'update' step 4: '|| true' swallows a failure")

    def test_forbidden_commands(self) -> None:
        cases = {
            'gh pr merge "$branch" --squash': "merges a pull request",
            'gh pr merge --auto "$branch"': "asks for auto-merge",
            'gh pr review "$branch" --approve': "reviews or approves a pull request",
            'git merge "$branch"': "merges a branch",
            "gh api repos/x/y/pulls/1/merge -X PUT": "calls the GitHub API directly",
            "wget -q https://example.invalid/tool": "downloads with curl or wget",
            "curl -fsSL https://example.invalid/tool -o tool": "downloads with curl or wget",
        }
        for command, message in cases.items():
            with self.subTest(command=command):
                out = self.mutated(UPDATE, PR_CREATE, PR_CREATE + f"          {command}\n", f"{UPDATE}: job 'update' step 4 {message}: {command[:60]}")
                self.assertEqual(len([line for line in out.splitlines() if message in line]), 1, out)

    def test_update_template_that_opens_no_pull_request(self) -> None:
        self.mutated(UPDATE, PR_CREATE, '          echo "pushed $branch"\n', f"{UPDATE}: must open a pull request with 'gh pr create'")

    def test_job_without_steps_and_step_without_action(self) -> None:
        fixture = Fixture(self)
        text = (fixture.root / UPDATE).read_bytes().decode("utf-8")
        head = text[: text.index("    steps:\n")]
        fixture.write(UPDATE, (head + "    timeout-minutes: 5\n").encode("utf-8"))
        self.assert_red(fixture, f"{UPDATE}: job 'update' has no steps")
        fixture.write(UPDATE, (head + "    steps:\n      - name: nothing\n").encode("utf-8"))
        self.assert_red(fixture, f"{UPDATE}: job 'update' step 1 is neither 'uses' nor 'run'")
        fixture.write(UPDATE, (head + "    steps:\n      - run: [gh, pr, create]\n").encode("utf-8"))
        self.assert_red(fixture, f"{UPDATE}: job 'update' step 1 has a 'run' that is not a script")
        fixture.write(UPDATE, (text[: text.index("jobs:\n")] + "jobs: none\n").encode("utf-8"))
        self.assert_red(fixture, f"{UPDATE}: 'jobs' must be a non-empty mapping")


class ReusableWorkflow(Case):
    def test_runs_the_callers_copy_of_the_checker(self) -> None:
        self.mutated(
            REUSABLE,
            "run: python consumer/check_conformance.py check --consumer consumer-repo",
            "run: python consumer-repo/menq-standard/check_conformance.py check --consumer consumer-repo",
            f"{REUSABLE}: job 'conformance' step 5 runs consumer-repo/menq-standard/check_conformance.py; it may run only the standard's own copy under consumer/",
            f"{REUSABLE}: job 'conformance' step 5 runs a script of the calling repository",
        )

    def test_reaches_the_callers_copy_through_a_path_that_starts_in_the_kit(self) -> None:
        out = self.mutated(
            REUSABLE,
            "run: python consumer/check_conformance.py check --consumer consumer-repo",
            "run: python consumer/../consumer-repo/menq-standard/check_conformance.py check --consumer consumer-repo",
            f"{REUSABLE}: job 'conformance' step 5 runs a script of the calling repository",
        )
        self.assertNotIn("it may run only the standard's own copy", out)

    def test_runs_a_script_outside_the_kit(self) -> None:
        self.mutated(REUSABLE, '$(python consumer/check_conformance.py pin-commit', '$(python3 scripts/other.py pin-commit', f"{REUSABLE}: job 'conformance' step 4 runs scripts/other.py")

    def test_runs_no_python_at_all(self) -> None:
        fixture = Fixture(self)
        text = (fixture.root / REUSABLE).read_bytes().decode("utf-8")
        fixture.write(REUSABLE, (text[: text.index("      - name: Move the standard")] + "      - run: echo ok\n").encode("utf-8"))
        self.assert_red(fixture, f"{REUSABLE}: runs no Python script, so it judges nothing")

    def test_missing(self) -> None:
        fixture = Fixture(self)
        (fixture.root / REUSABLE).unlink()
        self.assert_red(fixture, f"{REUSABLE}: is missing or not valid UTF-8")

    def test_not_a_workflow(self) -> None:
        fixture = Fixture(self)
        fixture.write(REUSABLE, b"- a\n")
        self.assert_red(fixture, f"{REUSABLE}: cannot be parsed as a workflow (line 1: the top level must be a mapping)")


class CommandLine(Case):
    def test_runs_as_a_script(self) -> None:
        fixture = Fixture(self)
        command = [sys.executable, str(REPO / "scripts/check_consumer_templates.py"), str(fixture.root)]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual((result.returncode, result.stdout), (0, "CONSUMER TEMPLATES: GREEN (2 templates and the reusable workflow)\n"), result.stderr)
        fixture.sub(CONFORMANCE, "@__MENQ_STANDARD_COMMIT__", "@main")
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual((result.returncode, result.stdout.splitlines()[0]), (1, "CONSUMER TEMPLATES: RED"), result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
