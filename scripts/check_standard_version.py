#!/usr/bin/env python3
"""Hold the standard's version to what a product repository receives (decision D-029).

A repository that follows MenQ Standard learns that something changed from one number, the file
VERSION at the repository root.  This gate is RED when:

    1. VERSION is not exactly one MAJOR.MINOR.PATCH line;
    2. CHANGELOG.md has no heading naming "MenQ Standard v<VERSION>", or its newest such heading
       names another version (the update pull request cuts the changelog at those headings);
    3. a file of the consumer interface changed against the base and VERSION did not increase;
    4. VERSION went backwards against the base.

The consumer interface is everything under consumer/ and the reusable workflow
.github/workflows/consumer-conformance.yml.

Checks 3 and 4 need a base, and the comparison is always with the WORKING TREE, so uncommitted
and untracked changes count.  The base is:

    the merge base of HEAD and ``--base`` (default origin/main)   on a branch or a pull request;
    HEAD itself                    when HEAD is contained in the base and the tree has changes;
    the first parent of HEAD       when HEAD is contained in the base and the tree is clean,
                                   which is main after a merge: the merge is what gets judged.

When no base can be found the first line is not GREEN: it says the comparison did NOT run, and
the exit code is 1 unless ``--allow-no-base`` is given.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_REL = "VERSION"
CHANGELOG_REL = "CHANGELOG.md"
INTERFACE_PATHS = ("consumer", ".github/workflows/consumer-conformance.yml")
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
VERSION_HEADING = re.compile(r"^## .*\bMenQ Standard v(\d+\.\d+\.\d+)(?![\w.])")
SHOWN = 12


def parse(text: str) -> tuple[int, int, int] | None:
    match = SEMVER.match(text)
    return (int(match.group(1)), int(match.group(2)), int(match.group(3))) if match else None


def git(root: Path, *args: str) -> tuple[int, bytes]:
    try:
        result = subprocess.run(["git", *args], cwd=root, capture_output=True)
    except OSError:
        return 127, b""
    return result.returncode, result.stdout


def read_version(data: bytes) -> tuple[str | None, str]:
    """(version, "") or (None, reason)."""
    try:
        text = data.decode("utf-8").replace("\r\n", "\n")
    except UnicodeDecodeError:
        return None, "is not valid UTF-8"
    if not text.endswith("\n") or "\n" in text[:-1]:
        return None, "must be exactly one line ending in a newline"
    if parse(text[:-1]) is None:
        return None, f"is {text[:-1]!r}, not MAJOR.MINOR.PATCH"
    return text[:-1], ""


def static_errors(root: Path) -> tuple[list[str], str | None]:
    """Checks 1 and 2, which need no base.  Returns (errors, version or None)."""
    path = root / VERSION_REL
    if not path.is_file():
        return [f"{VERSION_REL} is missing"], None
    version, reason = read_version(path.read_bytes())
    if version is None:
        return [f"{VERSION_REL} {reason}"], None
    changelog = root / CHANGELOG_REL
    if not changelog.is_file():
        return [f"{CHANGELOG_REL} is missing"], version
    try:
        lines = changelog.read_bytes().decode("utf-8").replace("\r\n", "\n").split("\n")
    except UnicodeDecodeError:
        return [f"{CHANGELOG_REL} is not valid UTF-8"], version
    named = [match.group(1) for match in map(VERSION_HEADING.match, lines) if match]
    if version not in named:
        return [f"{CHANGELOG_REL} has no '## ' heading naming MenQ Standard v{version}"], version
    if named[0] != version:
        return [
            f"the newest version heading of {CHANGELOG_REL} names MenQ Standard v{named[0]}, but {VERSION_REL} is {version}"
        ], version
    return [], version


def find_base(root: Path, base: str) -> tuple[str | None, str]:
    """(commit to compare the working tree with, how it was found) or (None, why there is none)."""
    if git(root, "rev-parse", "--git-dir")[0] != 0:
        return None, "this is not a git repository"
    code, head = git(root, "rev-parse", "--verify", "--quiet", "HEAD^{commit}")
    if code != 0:
        return None, "the repository has no commit"
    code, tip = git(root, "rev-parse", "--verify", "--quiet", base + "^{commit}")
    if code != 0:
        return None, f"the ref {base} does not exist here (a shallow or single-branch checkout?)"
    code, merge_base = git(root, "merge-base", "HEAD", tip.decode().strip())
    if code != 0 or not merge_base.strip():
        return None, f"HEAD and {base} share no history here"
    commit = merge_base.decode().strip()
    if commit != head.decode().strip():
        return commit, f"the merge base of HEAD and {base}"
    own = differing_paths(root, commit, (*INTERFACE_PATHS, VERSION_REL))
    if own is None:
        return None, "git could not compare the working tree with HEAD"
    if own:
        return commit, f"HEAD itself, because HEAD is contained in {base} and the working tree has changes of its own"
    code, parent = git(root, "rev-parse", "--verify", "--quiet", "HEAD^1^{commit}")
    if code != 0:
        return None, f"HEAD is contained in {base} and has no parent to compare with"
    return parent.decode().strip(), f"the first parent of HEAD, because HEAD is contained in {base} and the working tree is clean"


def differing_paths(root: Path, commit: str, paths: tuple[str, ...]) -> list[str] | None:
    """The given paths that differ between a commit and the working tree, untracked files included."""
    code, tracked = git(root, "diff", "--name-only", "-z", commit, "--", *paths)
    if code != 0:
        return None
    code, untracked = git(root, "ls-files", "-z", "--others", "--exclude-standard", "--", *paths)
    if code != 0:
        return None
    return sorted({part.decode("utf-8", "replace") for part in (tracked + untracked).split(b"\0") if part})


def changed_interface_files(root: Path, commit: str) -> list[str] | None:
    return differing_paths(root, commit, INTERFACE_PATHS)


def base_errors(root: Path, commit: str, version: str, report: list[str]) -> list[str]:
    """Checks 3 and 4."""
    changed = changed_interface_files(root, commit)
    if changed is None:
        return [f"git could not compare the working tree with {commit[:12]}"]
    code, blob = git(root, "cat-file", "blob", f"{commit}:{VERSION_REL}")
    if code != 0:
        report.append(f"the base has no {VERSION_REL}: this change introduces the version, at {version}")
        report.append(f"consumer interface files changed against the base: {len(changed)}")
        return []
    before, reason = read_version(blob)
    if before is None:
        return [f"{VERSION_REL} at the base {commit[:12]} {reason}"]
    report.append(f"version at the base: {before}; here: {version}")
    report.append(f"consumer interface files changed against the base: {len(changed)}")
    if parse(version) < parse(before):
        return [f"{VERSION_REL} went backwards: {before} at the base, {version} here"]
    if changed and parse(version) == parse(before):
        shown = ", ".join(changed[:SHOWN]) + (f" and {len(changed) - SHOWN} more" if len(changed) > SHOWN else "")
        return [
            f"the consumer interface changed and {VERSION_REL} did not: it is {version} at the base and here; changed: {shown}"
        ]
    return []


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (default: this checkout)")
    parser.add_argument("--base", default="origin/main", help="the ref to compare with (default: origin/main)")
    parser.add_argument(
        "--allow-no-base", action="store_true", help="exit 0 when no base exists; the comparison is still reported as NOT RUN"
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()

    errors, version = static_errors(root)
    report: list[str] = []
    commit: str | None = None
    why = "the version could not be read"
    if version is not None:
        commit, why = find_base(root, args.base)
        if commit is not None:
            errors += base_errors(root, commit, version, report)

    if errors:
        print("STANDARD VERSION: RED")
        for error in errors:
            print(f"- {error}")
        return 1
    if commit is None:
        print("STANDARD VERSION: BASE COMPARISON NOT RUN")
        print(f"- no base to compare with: {why}")
        print(f"- checked without a base: {VERSION_REL} is {version}, and {CHANGELOG_REL} names it in its newest version heading")
        print("- NOT checked: whether the consumer interface changed without a version change")
        return 0 if args.allow_no_base else 1
    print(f"STANDARD VERSION: GREEN ({version})")
    print(f"compared the working tree with {commit[:12]}, {why}")
    for line in report:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
