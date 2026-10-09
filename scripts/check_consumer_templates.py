#!/usr/bin/env python3
"""Hold the consumer-kit workflow templates, and the reusable workflow, to a policy (decision D-029).

consumer/templates/*.yml are workflows a product repository runs, not workflows of this
repository: they live outside .github/workflows/, so scripts/validate_foundation.py does not read
them, and one of them holds write permissions this repository's own policy forbids.  They are
still code this repository ships into other repositories, so this gate holds them to the same
supply-chain rules, read from validate_foundation.py rather than restated, and to a few of their
own:

    - a template is declared here by name, with its exact permissions and its allowed triggers;
    - every ``uses`` is pinned to a 40-character SHA; the one placeholder allowed is the commit of
      this repository's own reusable workflow;
    - no ``continue-on-error``, no ``pull_request_target``, no job-level permissions, nothing the
      shared rule refuses in a ``run`` script (a download piped to a shell, ``|| true``);
    - no curl, wget or ``gh api`` at all;
    - the update template opens a pull request and never merges, approves or auto-merges one, and
      runs only on a schedule or by hand, never on an event a pull request can trigger.

For .github/workflows/consumer-conformance.yml, which validate_foundation.py already holds to the
general policy, one rule more: every Python script it runs is the standard's own copy under
consumer/, never a file of the repository being judged.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_foundation as vf  # noqa: E402

TEMPLATE_DIR = "consumer/templates"
REUSABLE_WORKFLOW = ".github/workflows/consumer-conformance.yml"
CALLER_CHECKOUT = "consumer-repo"
COMMIT_PLACEHOLDER = "__MENQ_STANDARD_COMMIT__"
KIT_DIR_PLACEHOLDER = "__MENQ_KIT_DIR__"
REUSABLE_USES = f"menqstudio/MenQ-Standard/{REUSABLE_WORKFLOW}@{COMMIT_PLACEHOLDER}"
SAMPLE_COMMIT = "0123456789abcdef0123456789abcdef01234567"
SAMPLE_KIT_DIR = "menq-standard"

# name -> (exact top-level permissions, triggers allowed, triggers required, must open a pull request)
TEMPLATES = {
    "menq-standard-conformance.yml": (
        {"contents": "read"},
        {"pull_request", "push", "workflow_dispatch"},
        {"pull_request"},
        False,
    ),
    "menq-standard-update.yml": (
        {"contents": "write", "pull-requests": "write"},
        {"schedule", "workflow_dispatch"},
        {"schedule", "workflow_dispatch"},
        True,
    ),
}
FORBIDDEN_COMMANDS = (
    (re.compile(r"\bgh\s+pr\s+merge\b"), "merges a pull request"),
    (re.compile(r"\bgh\s+pr\s+review\b"), "reviews or approves a pull request"),
    (re.compile(r"\bgit\s+merge\b"), "merges a branch"),
    (re.compile(r"(?<![\w-])--auto(?![\w-])"), "asks for auto-merge"),
    (re.compile(r"\bgh\s+api\b"), "calls the GitHub API directly"),
    (re.compile(r"\b(curl|wget)\b"), "downloads with curl or wget"),
)
OPENS_PULL_REQUEST = re.compile(r"\bgh\s+pr\s+create\b")


def tracked_templates(root: Path) -> list[str] | None:
    try:
        result = subprocess.run(["git", "ls-files", "-z", "--", TEMPLATE_DIR], cwd=root, check=True, capture_output=True)
        return sorted(part for part in result.stdout.decode("utf-8").split("\0") if part)
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError):
        return None


def read(root: Path, rel: str) -> str | None:
    try:
        return (root / rel).read_bytes().decode("utf-8").replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError):
        return None


def parse(rel: str, text: str, errors: list[str]) -> dict | None:
    try:
        tree = vf.parse_workflow_yaml(text)
    except vf.WorkflowSyntaxError as exc:
        errors.append(f"{rel}: cannot be parsed as a workflow ({exc})")
        return None
    except (RecursionError, IndexError, TypeError, ValueError) as exc:
        errors.append(f"{rel}: cannot be parsed as a workflow ({type(exc).__name__})")
        return None
    return tree if isinstance(tree, dict) else None


def run_scripts(tree: dict) -> list[tuple[str, int, str]]:
    """(job id, step number, script) for every run step."""
    found: list[tuple[str, int, str]] = []
    jobs = tree.get("jobs")
    for job_id, job in (jobs.items() if isinstance(jobs, dict) else ()):
        steps = job.get("steps") if isinstance(job, dict) else None
        for number, step in enumerate(steps if isinstance(steps, list) else (), 1):
            if isinstance(step, dict) and isinstance(step.get("run"), str):
                found.append((job_id, number, step["run"]))
    return found


def check_template(name: str, rel: str, text: str, errors: list[str]) -> None:
    permissions, allowed, required, opens_pull_request = TEMPLATES[name]

    # The placeholder may stand only where this repository's own reusable workflow is called.
    raw = parse(rel, text, errors)
    if raw is None:
        return
    raw_uses: list[object] = []
    vf.walk_uses(raw, raw_uses)
    for ref in raw_uses:
        if isinstance(ref, str) and COMMIT_PLACEHOLDER in ref and ref != REUSABLE_USES:
            errors.append(f"{rel}: the commit placeholder may pin only {REUSABLE_USES.split('@')[0]}, not {ref}")

    rendered = text.replace(COMMIT_PLACEHOLDER, SAMPLE_COMMIT).replace(KIT_DIR_PLACEHOLDER, SAMPLE_KIT_DIR)
    if "__MENQ_" in rendered:
        errors.append(f"{rel}: holds a placeholder the installer does not fill in")
    tree = parse(rel, rendered, errors)
    if tree is None:
        return

    triggers = vf.workflow_triggers(tree.get("on"))
    if triggers is None:
        errors.append(f"{rel}: missing or malformed 'on' triggers")
        triggers = set()
    if "pull_request_target" in triggers:
        errors.append(f"{rel}: pull_request_target is not allowed")
    for trigger in sorted(triggers - allowed):
        errors.append(f"{rel}: may not run on '{trigger}' (allowed: {', '.join(sorted(allowed))})")
    for trigger in sorted(required - triggers):
        errors.append(f"{rel}: must run on '{trigger}'")

    if tree.get("permissions") != permissions:
        wanted = ", ".join(f"{key}: {value}" for key, value in permissions.items())
        errors.append(f"{rel}: top-level permissions must be exactly '{wanted}'")

    uses: list[object] = []
    vf.walk_uses(tree, uses)
    for ref in uses:
        if not isinstance(ref, str) or not vf.PINNED_ACTION.match(ref):
            errors.append(f"{rel}: action {ref} is not pinned to a full commit SHA")

    jobs = tree.get("jobs")
    if not isinstance(jobs, dict) or not jobs:
        errors.append(f"{rel}: 'jobs' must be a non-empty mapping")
        return
    for job_id, job in jobs.items():
        where = f"{rel}: job '{job_id}'"
        if not isinstance(job, dict):
            errors.append(f"{where} is not a mapping")
            continue
        if "permissions" in job:
            errors.append(f"{where} may not set its own permissions")
        if "continue-on-error" in job and not vf.is_false(job["continue-on-error"]):
            errors.append(f"{where} sets continue-on-error")
        if "uses" in job:
            continue
        steps = job.get("steps")
        if not isinstance(steps, list) or not steps:
            errors.append(f"{where} has no steps")
            continue
        for number, step in enumerate(steps, 1):
            if not isinstance(step, dict) or not ("uses" in step or "run" in step):
                errors.append(f"{where} step {number} is neither 'uses' nor 'run'")
                continue
            if "continue-on-error" in step and not vf.is_false(step["continue-on-error"]):
                errors.append(f"{where} step {number} sets continue-on-error")
            if "run" in step and not isinstance(step["run"], str):
                errors.append(f"{where} step {number} has a 'run' that is not a script")

    opened = False
    for job_id, number, script in run_scripts(tree):
        where = f"{rel}: job '{job_id}' step {number}"
        for violation in vf.run_script_violations(script):
            errors.append(f"{where}: {violation}")
        for line in vf.logical_lines(script):
            for pattern, what in FORBIDDEN_COMMANDS:
                if pattern.search(line):
                    errors.append(f"{where} {what}: {line[:80]}")
            opened = opened or bool(OPENS_PULL_REQUEST.search(line))
    if opens_pull_request and not opened:
        errors.append(f"{rel}: must open a pull request with 'gh pr create'; an update reaches a repository no other way")


def check_reusable(root: Path, errors: list[str]) -> None:
    text = read(root, REUSABLE_WORKFLOW)
    if text is None:
        errors.append(f"{REUSABLE_WORKFLOW}: is missing or not valid UTF-8")
        return
    tree = parse(REUSABLE_WORKFLOW, text, errors)
    if tree is None:
        return
    ran = 0
    for job_id, number, script in run_scripts(tree):
        for line in vf.logical_lines(script):
            for words in re.findall(r"\bpython3?\s+(\S+)", line):
                ran += 1
                if not words.startswith("consumer/"):
                    errors.append(
                        f"{REUSABLE_WORKFLOW}: job '{job_id}' step {number} runs {words}; it may run only the standard's "
                        "own copy under consumer/, never a file of the calling repository"
                    )
            if re.search(rf"\bpython3?\s+\S*{re.escape(CALLER_CHECKOUT)}/", line):
                errors.append(f"{REUSABLE_WORKFLOW}: job '{job_id}' step {number} runs a script of the calling repository")
    if ran == 0:
        errors.append(f"{REUSABLE_WORKFLOW}: runs no Python script, so it judges nothing")


def check(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    tracked = tracked_templates(root)
    if tracked is None:
        return ["cannot enumerate tracked files with git ls-files -z"], 0
    names = {rel[len(TEMPLATE_DIR) + 1:]: rel for rel in tracked}
    for name in sorted(set(names) - set(TEMPLATES)):
        errors.append(f"{names[name]}: is not a declared template; declare its permissions and triggers in {Path(__file__).name}")
    for name in TEMPLATES:
        rel = f"{TEMPLATE_DIR}/{name}"
        if name not in names:
            errors.append(f"{rel}: declared template is not tracked by git")
            continue
        text = read(root, rel)
        if text is None:
            errors.append(f"{rel}: is missing from the checkout or not valid UTF-8")
            continue
        check_template(name, rel, text, errors)
    check_reusable(root, errors)
    return errors, len(TEMPLATES)


def main(argv: list[str] | None = None) -> int:
    root = Path(argv[0]).resolve() if argv else ROOT
    try:
        errors, count = check(root)
    except Exception as exc:  # a gate answers RED, never with a traceback
        errors, count = [f"internal error: {type(exc).__name__}: {exc}"], 0
    if errors:
        print("CONSUMER TEMPLATES: RED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"CONSUMER TEMPLATES: GREEN ({count} templates and the reusable workflow)")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    sys.exit(main(sys.argv[1:]))
