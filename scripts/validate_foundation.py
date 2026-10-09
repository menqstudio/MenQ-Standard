#!/usr/bin/env python3
"""Validate MenQ Foundation documentation, workflow policy and D-026 session-read integrity.

Every check here must be able to give both answers; ``scripts/test_validate_foundation.py`` breaks
each subject once and asserts the RED line.  The validator never answers with a traceback: a
missing, malformed or surprising input is a RED line that names the file and the reason.
"""

from __future__ import annotations

import hashlib
import json
import posixpath
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
INVENTORY_REL = "foundation/ai-collaboration/MARKDOWN_INVENTORY.json"
INVENTORY = ROOT / INVENTORY_REL
WORKFLOW_DIR = ".github/workflows/"

CHAPTERS = (
    "philosophy",
    "principles",
    "terminology",
    "governance",
    "decision-system",
    "documentation",
    "ai-collaboration",
)

REQUIRED_ROOT = (
    "README.md",
    "PROJECT_CONTEXT.md",
    "AI_WORKING_CONTEXT.md",
    "DECISIONS.md",
    "DECISION_INDEX.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "COLLABORATION_STYLE.md",
)

REQUIRED_FOUNDATION = (
    "foundation/README.md",
    "foundation/PROJECT_CONTEXT.md",
    "foundation/FOUNDATION_NORMATIVE_METADATA_REGISTRY.md",
    "foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md",
    "foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md",
    "foundation/ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md",
    INVENTORY_REL,
)

EXPECTED_MARKERS = {
    "README.md": "<!-- END: MENQ_STANDARD_ROOT_README -->",
    "PROJECT_CONTEXT.md": "<!-- END: MENQ_STANDARD_PROJECT_CONTEXT -->",
    "DECISION_INDEX.md": "<!-- END: MENQ_DECISION_INDEX -->",
    "ROADMAP.md": "<!-- END: MENQ_STANDARD_ROADMAP -->",
    "COLLABORATION_STYLE.md": "<!-- END: MENQ_COLLABORATION_STYLE -->",
    "foundation/README.md": "<!-- END: FOUNDATION_README_V1 -->",
    "foundation/PROJECT_CONTEXT.md": "<!-- END: FOUNDATION_PROJECT_CONTEXT -->",
    "foundation/FOUNDATION_NORMATIVE_METADATA_REGISTRY.md": "<!-- END: FOUNDATION_NORMATIVE_METADATA_REGISTRY -->",
    "foundation/documentation/CANONICAL_WRITE_INTEGRITY_LAW.md": "<!-- END: CANONICAL_WRITE_INTEGRITY_LAW_V1 -->",
    "foundation/ai-collaboration/CANONICAL_SESSION_READ_LAW.md": "<!-- END: CANONICAL_SESSION_READ_LAW_V1 -->",
    "foundation/ai-collaboration/D-026-CANONICAL-SESSION-READ-LAW.md": "<!-- END: D-026-CANONICAL-SESSION-READ-LAW -->",
    "DECISIONS.md": "<!-- END: MENQ_DECISIONS_REGISTRY -->",
    "ECOSYSTEM_ARCHITECTURE.md": "<!-- END: MENQ_ECOSYSTEM_ARCHITECTURE -->",
    "foundation/decision-system/README.md": "<!-- END: FOUNDATION_DECISION_SYSTEM_README -->",
    "foundation/documentation/README.md": "<!-- END: FOUNDATION_DOCUMENTATION_README -->",
    "foundation/governance/README.md": "<!-- END: FOUNDATION_GOVERNANCE_README -->",
    "foundation/philosophy/ENGINEERING_PHILOSOPHY.md": "<!-- END: FOUNDATION_ENGINEERING_PHILOSOPHY -->",
    "foundation/philosophy/PRODUCT_PHILOSOPHY.md": "<!-- END: FOUNDATION_PRODUCT_PHILOSOPHY -->",
    "foundation/philosophy/README.md": "<!-- END: FOUNDATION_PHILOSOPHY_README -->",
    "foundation/principles/README.md": "<!-- END: FOUNDATION_PRINCIPLES_README -->",
    "foundation/terminology/README.md": "<!-- END: FOUNDATION_TERMINOLOGY_README -->",
}

D026_REQUIRED_REFERENCES = {
    "README.md": (
        "CANONICAL_SESSION_READ_LAW.md",
        "D-026-CANONICAL-SESSION-READ-LAW.md",
    ),
    "PROJECT_CONTEXT.md": ("CANONICAL_SESSION_READ_LAW.md",),
    "AI_WORKING_CONTEXT.md": ("D-026",),
    "NEXT_CHAT_HANDOFF.md": (
        "CANONICAL_SESSION_READ_LAW.md",
        "D-026",
    ),
    "DECISION_INDEX.md": ("D-026",),
    "foundation/README.md": (
        "CANONICAL_SESSION_READ_LAW.md",
        "D-026-CANONICAL-SESSION-READ-LAW.md",
    ),
    "foundation/ai-collaboration/PROJECT_CONTEXT.md": ("D-026",),
}

BILINGUAL_PARITY_CONTROLS = (
    "foundation/documentation/BILINGUAL_PARITY_ADDENDUM.md",
    "foundation/ai-collaboration/BILINGUAL_PARITY_ADDENDUM.md",
)

# --- Content minimums for a required document (2026-10-09) -------------------------------------
# Measured over the 34 required documents on 2026-10-09 with document_body() below.  The smallest
# was foundation/decision-system/PROJECT_CONTEXT.md: 952 body bytes, 527 Latin letters; the fewest
# Armenian letters were 66, in foundation/FOUNDATION_NORMATIVE_METADATA_REGISTRY.md.  Each floor is
# set below the smallest real value, so no existing document was edited to meet it.
MIN_BODY_BYTES = 600
MIN_ARMENIAN_LETTERS = 50
MIN_LATIN_LETTERS = 300
# Three required documents carry no "**Status ...:**" metadata line today.  They are exempt by
# name rather than by relaxing the rule for every document.
STATUS_METADATA_EXEMPT = ("README.md", "CHANGELOG.md", "ECOSYSTEM_ARCHITECTURE.md")

# --- Bilingual rules ---------------------------------------------------------------------------
# A section that is not inside a "Հայերեն"/"English" language block may not hold this many English
# prose words with no Armenian letter at all.  Measured 2026-10-09: no section of the 134 tracked
# Markdown files reaches it once the one exception below is applied.
ENGLISH_ONLY_WORD_LIMIT = 12
# ECOSYSTEM_ARCHITECTURE.md writes each language half as "## Հայերեն" / "## English" followed by
# PEER "## ..." sections, so its language block runs to the next language heading, not to the next
# heading of the same level.  Every other file ends a language block at the next peer heading.
LANGUAGE_BLOCK_SPANS_PEERS = ("ECOSYSTEM_ARCHITECTURE.md",)
# A pull-request form: its "**HY:**" / "**EN:**" labels are blanks for the author to fill in.
EMPTY_LABEL_EXEMPT = (".github/pull_request_template.md",)

# --- Workflow policy ---------------------------------------------------------------------------
# The workflows that must exist, the job in each that must run, and the commands that job must
# run unconditionally.  Replacing a command with "echo ok" is RED.
REQUIRED_WORKFLOW_RUNS = {
    # The reusable workflow a product repository calls (D-029).  It must run the standard's own
    # copy of the checker, against the standard: "--standard" is what makes the pin's commit and
    # hashes be compared with this repository instead of believed.
    "consumer-conformance.yml": {
        "conformance": ("consumer/check_conformance.py check --consumer --standard --standard-ref",),
    },
    "design-brand-expression.yml": {
        "validate": (
            "platforms/design/brand-expression/scripts/build_brand_tokens.py --check",
            "platforms/design/validation/validate_brand_expression.py",
            "platforms/design/validation/test_validate_brand_expression.py",
        ),
    },
    "design-governance.yml": {
        "governance": ("platforms/design/validation/validate_governance.py",),
    },
    "design-platform-phase-a.yml": {
        "validate-phase-a": (
            "platforms/design/validation/validate_phase_a.py",
            "platforms/design/validation/validate_public_api.py",
        ),
    },
    "design-platform-preview-release.yml": {
        "release-candidate-and-consumers": (
            "platforms/design/validation/validate_release_candidate.py",
            "platforms/design/validation/validate_consumers.py",
        ),
    },
    "foundation-integrity.yml": {"validate": ("scripts/validate_foundation.py",)},
    "foundation-v1-package.yml": {"package": ("scripts/validate_foundation.py",)},
    "markdown-inventory-bootstrap.yml": {
        "validate": (
            "scripts/generate_markdown_inventory.py --check",
            "scripts/validate_foundation.py",
            "scripts/validate_platforms.py",
            "scripts/test_generate_markdown_inventory.py",
            "scripts/test_validate_foundation.py",
            "scripts/test_validate_platforms.py",
            "scripts/test_check_session_read_budget.py",
            "scripts/check_session_read_budget.py",
            # The consumer layer (D-029): the kit manifest, the version gate, the template policy,
            # and the tests of each, of the checker and of sync_facts.
            "scripts/generate_kit_manifest.py --check",
            "scripts/check_standard_version.py",
            "scripts/check_consumer_templates.py",
            "scripts/test_generate_kit_manifest.py",
            "scripts/test_check_standard_version.py",
            "scripts/test_check_consumer_templates.py",
            "scripts/test_check_conformance.py",
            "consumer/test_sync_facts.py",
        ),
    },
    "platforms-integrity.yml": {"validate-platforms": ("scripts/validate_platforms.py",)},
    "publish-release.yml": {
        "foundation": ("scripts/validate_foundation.py",),
        "design-platform": (
            "platforms/design/validation/validate_public_api.py",
            "platforms/design/validation/validate_release_candidate.py",
        ),
    },
}
# The only jobs that may hold "contents: write", and the only jobs that may carry a job-level "if".
PUBLISHING_JOBS = (("publish-release.yml", "foundation"), ("publish-release.yml", "design-platform"))
# publish-release.yml runs on a tag push, and consumer-conformance.yml runs only when a product
# repository calls it; every other required workflow must run on pull requests.
REQUIRED_TRIGGER = {"publish-release.yml": "push", "consumer-conformance.yml": "workflow_call"}
DEFAULT_REQUIRED_TRIGGER = "pull_request"

PINNED_ACTION = re.compile(r"^[\w.-]+/[\w./-]+@[0-9a-f]{40}$")
DOWNLOADERS = ("curl", "wget")
INTERPRETERS = ("sh", "bash", "zsh", "dash", "ksh", "python", "python3", "node", "perl", "ruby", "pwsh", "powershell")
SUBSTITUTED_DOWNLOAD = re.compile(
    r"(?:\b(?:sh|bash|zsh|dash|ksh|source|eval|python3?)|(?:^|\s)\.)\s[^|;&]*?(?:<\(|\$\(|`)\s*(?:curl|wget)\b"
)

ARMENIAN = re.compile(r"[Ա-֏]")
LATIN = re.compile(r"[A-Za-z]")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
END_MARKER = re.compile(r"<!-- END: [A-Za-z0-9_.-]+ -->")
HY_MARK = re.compile(r"^(#{2,3} Հայերեն|\s*(?:>\s*)?\*\*HY:?\*\*)", re.M)
EN_MARK = re.compile(r"^(#{2,3} English|\s*(?:>\s*)?\*\*EN:?\*\*)", re.M)
STATUS_LINE = re.compile(r"^\*\*Status\b[^*\n]*:\*\*[ \t]*\S", re.M)
LANGUAGE_HEADING = re.compile(r"^(Հայերեն|English)\b")
LABEL = re.compile(r"^\s*(?:>\s*)?\*\*(HY|EN):?\*\*:?(.*)$")
DECISION_FILE = re.compile(r"^(D-\d+)[-_]")
FENCE = re.compile(r"```.*?```", re.S)


# ================================================================================================
# Repository access
# ================================================================================================

_TEXT_CACHE: dict[str, tuple[str | None, str]] = {}


def is_markdown(rel: str) -> bool:
    return rel.lower().endswith(".md")


def tracked_files(errors: list[str]) -> list[str] | None:
    """Every tracked path, from ``git ls-files -z`` so a space or a non-ASCII name is one path."""
    try:
        result = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True)
        return sorted(part for part in result.stdout.decode("utf-8").split("\0") if part)
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError) as exc:
        errors.append(f"cannot enumerate tracked files with git ls-files -z: {exc}")
        return None


def load(rel: str) -> tuple[str | None, str]:
    """Return (text with LF line endings, "") or (None, reason).  Never raises."""
    if rel not in _TEXT_CACHE:
        path = ROOT / rel
        try:
            if not path.is_file():
                _TEXT_CACHE[rel] = (None, "is missing from the checkout")
            else:
                _TEXT_CACHE[rel] = (path.read_bytes().decode("utf-8").replace("\r\n", "\n"), "")
        except UnicodeDecodeError:
            _TEXT_CACHE[rel] = (None, "is not valid UTF-8")
        except OSError as exc:
            _TEXT_CACHE[rel] = (None, f"cannot be read ({exc.strerror or exc})")
    return _TEXT_CACHE[rel]


def text_of(rel: str) -> str | None:
    return load(rel)[0]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_tracked_markdown_readable(errors: list[str], markdown: list[str]) -> None:
    if not markdown:
        errors.append("tracked Markdown inventory is empty")
    for rel in markdown:
        text, reason = load(rel)
        if text is None:
            errors.append(f"tracked Markdown file {reason}: {rel}")


# ================================================================================================
# A strict parser for the YAML subset the workflows use
# ================================================================================================
# CI installs no YAML library (the workflows pip-install jsonschema only), and a validator that
# enforces supply-chain policy should not itself need a download to run.  So this is a small
# strict parser: block mappings and sequences, plain and quoted scalars, literal and folded block
# scalars, and single-line flow collections.  Anything else -- anchors, aliases, tags, merge keys,
# tabs, duplicate keys, multi-line plain or flow scalars, several documents -- is refused, and a
# refused workflow is RED.  scripts/test_validate_foundation.py compares it with PyYAML on the
# real workflows wherever PyYAML happens to be installed.


class WorkflowSyntaxError(ValueError):
    pass


_PLAIN_KEY = re.compile(r"[A-Za-z_][A-Za-z0-9_.-]*")
_ESCAPES = {'"': '"', "\\": "\\", "/": "/", "n": "\n", "t": "\t", "0": "\0", " ": " "}


class _YamlSubset:
    def __init__(self, text: str) -> None:
        if text.startswith("﻿"):
            raise WorkflowSyntaxError("line 1: a byte-order mark is not supported")
        self.raw = text.replace("\r\n", "\n").split("\n")
        self.i = 0
        self.line = 0  # index of the line being read, for the message

    def fail(self, message: str) -> None:
        raise WorkflowSyntaxError(f"line {min(self.line, len(self.raw) - 1) + 1}: {message}")

    def significant(self) -> tuple[int, str] | None:
        while self.i < len(self.raw):
            line = self.raw[self.i]
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                self.i += 1
                continue
            self.line = self.i
            lead = line[: len(line) - len(line.lstrip())]
            if lead.strip(" "):
                self.fail("indentation must be spaces only")
            return len(lead), line[len(lead):].rstrip()
        return None

    def document(self) -> object:
        current = self.significant()
        if current is not None and current[1] == "---":
            self.i += 1
            current = self.significant()
        if current is None:
            self.fail("the document is empty")
        if current[0] != 0:
            self.fail("the top level must not be indented")
        if self.is_entry(current[1]):
            self.fail("the top level must be a mapping")
        return self.mapping(0)  # returns only at the end of the text: nothing can follow it

    @staticmethod
    def is_entry(content: str) -> bool:
        return content == "-" or content.startswith("- ")

    def node(self, indent: int) -> object:
        current = self.significant()
        if current is not None and self.is_entry(current[1]):
            return self.sequence(indent)
        return self.mapping(indent)

    def mapping(self, indent: int) -> dict:
        result: dict = {}
        while True:
            current = self.significant()
            if current is None or current[0] < indent:
                return result
            if current[0] > indent:
                self.fail("unexpected indentation (multi-line plain scalars are not supported)")
            content = current[1]
            if content in ("---", "..."):
                self.fail("several documents in one file are not supported")
            if self.is_entry(content):
                self.fail("a sequence entry where a mapping key was expected")
            split = self.split_key(content)
            if split is None:
                self.fail(f"not a 'key: value' line: {content[:60]!r}")
            key, rest = split
            if key in result:
                self.fail(f"duplicate key {key!r}")
            self.i += 1
            result[key] = self.value(rest, indent, True)

    def sequence(self, indent: int) -> list:
        items: list = []
        while True:
            current = self.significant()
            if current is None or current[0] < indent:
                return items
            if current[0] > indent:
                self.fail("unexpected indentation (multi-line plain scalars are not supported)")
            content = current[1]
            if not self.is_entry(content):
                return items
            rest = content[1:].lstrip(" ")
            offset = len(content) - len(rest)
            if rest and not rest.startswith("#") and self.split_key(rest) is not None:
                self.raw[self.i] = " " * (indent + offset) + rest
                items.append(self.mapping(indent + offset))
                continue
            if self.is_entry(rest):
                self.fail("a sequence nested on one line is not supported")
            self.i += 1
            items.append(self.value(rest, indent, False))

    def value(self, rest: str, indent: int, same_indent_sequence: bool) -> object:
        rest = rest.strip()
        if rest == "" or rest.startswith("#"):
            current = self.significant()
            if current is not None:
                if current[0] > indent:
                    return self.node(current[0])
                if same_indent_sequence and current[0] == indent and self.is_entry(current[1]):
                    return self.sequence(indent)
            return ""
        if rest[0] in "|>":
            return self.block_scalar(rest, indent)
        return self.inline(rest)

    def split_key(self, content: str) -> tuple[str, str] | None:
        if content[0] in "\"'":
            try:
                key, end = self.quoted(content, 0)
            except WorkflowSyntaxError:
                return None
        else:
            match = _PLAIN_KEY.match(content)
            if not match:
                return None
            key, end = match.group(0), match.end()
        tail = content[end:]
        if tail.startswith(":") and (len(tail) == 1 or tail[1] == " "):
            return key, tail[1:]
        return None

    def inline(self, rest: str) -> object:
        first = rest[0]
        if first in "\"'":
            value, end = self.quoted(rest, 0)
            self.only_comment(rest[end:])
            return value
        if first in "[{":
            value, end = self.flow(rest, 0)
            self.only_comment(rest[end:])
            return value
        if first in "&*!%@`|>?,]}":
            self.fail(f"unsupported YAML construct starting with {first!r}")
        comment = re.search(r"\s#", rest)
        if comment:
            rest = rest[: comment.start()]
        rest = rest.rstrip()
        if ": " in rest or rest.endswith(":"):
            self.fail("a plain scalar may not contain ': '")
        if self.is_entry(rest):
            self.fail("a sequence entry may not follow a key on the same line")
        return rest

    def only_comment(self, tail: str) -> None:
        tail = tail.strip()
        if tail and not tail.startswith("#"):
            self.fail(f"unexpected text after a value: {tail[:40]!r}")

    def quoted(self, text: str, start: int) -> tuple[str, int]:
        quote = text[start]
        out: list[str] = []
        i = start + 1
        while i < len(text):
            char = text[i]
            if quote == "'":
                if char == "'":
                    if text[i + 1 : i + 2] == "'":
                        out.append("'")
                        i += 2
                        continue
                    return "".join(out), i + 1
            elif char == "\\":
                escape = text[i + 1 : i + 2]
                if escape not in _ESCAPES:
                    self.fail(f"unsupported escape sequence \\{escape}")
                out.append(_ESCAPES[escape])
                i += 2
                continue
            elif char == '"':
                return "".join(out), i + 1
            out.append(char)
            i += 1
        self.fail("unterminated quoted scalar (multi-line quoted scalars are not supported)")
        raise AssertionError  # pragma: no cover - fail() always raises

    def flow(self, text: str, i: int) -> tuple[object, int]:
        is_map = text[i] == "{"
        close = "}" if is_map else "]"
        result: object = {} if is_map else []
        i += 1
        while True:
            i = self.skip_spaces(text, i)
            if i >= len(text):
                self.fail("unterminated flow collection (multi-line flow collections are not supported)")
            if text[i] == close:
                return result, i + 1
            if is_map:
                key, i = self.flow_scalar(text, i, True)
                i = self.skip_spaces(text, i)
                if text[i : i + 1] != ":":
                    self.fail("a flow mapping entry needs 'key: value'")
                value, i = self.flow_value(text, i + 1)
                if key in result:
                    self.fail(f"duplicate key {key!r}")
                result[key] = value
            else:
                value, i = self.flow_value(text, i)
                result.append(value)
            i = self.skip_spaces(text, i)
            if text[i : i + 1] == ",":
                i += 1
            elif text[i : i + 1] != close:
                self.fail("malformed flow collection")

    @staticmethod
    def skip_spaces(text: str, i: int) -> int:
        while i < len(text) and text[i] == " ":
            i += 1
        return i

    def flow_value(self, text: str, i: int) -> tuple[object, int]:
        i = self.skip_spaces(text, i)
        if text[i : i + 1] in ("[", "{"):
            return self.flow(text, i)
        return self.flow_scalar(text, i, False)

    def flow_scalar(self, text: str, i: int, is_key: bool) -> tuple[str, int]:
        i = self.skip_spaces(text, i)
        if text[i : i + 1] in ('"', "'"):
            return self.quoted(text, i)
        j = i
        while j < len(text) and text[j] not in ",[]{}":
            if text[j] == ":" and (is_key or text[j + 1 : j + 2] in ("", " ")):
                break
            if text[j] == "#" and (j == i or text[j - 1] == " "):
                self.fail("a comment inside a flow collection is not supported")
            j += 1
        scalar = text[i:j].strip()
        if not scalar:
            self.fail("empty entry in a flow collection")
        if scalar[0] in "&*!%@`|>?":
            self.fail(f"unsupported YAML construct starting with {scalar[0]!r}")
        return scalar, j

    def block_scalar(self, header: str, indent: int) -> str:
        match = re.fullmatch(r"([|>])([+-]?)\s*(#.*)?", header)
        if not match:
            self.fail(f"unsupported block scalar header {header!r}")
        style, chomp = match.group(1), match.group(2)
        lines: list[str] = []
        block_indent: int | None = None
        while self.i < len(self.raw):
            line = self.raw[self.i]
            if not line.strip():
                lines.append("")
                self.i += 1
                continue
            lead = len(line) - len(line.lstrip(" "))
            self.line = self.i
            if block_indent is None:
                if lead <= indent:
                    break
                block_indent = lead
            if lead < block_indent:
                if lead > indent:
                    self.fail("a block scalar line is indented less than its first line")
                break
            lines.append(line[block_indent:])
            self.i += 1
        trailing = 0
        while lines and lines[-1] == "":
            lines.pop()
            trailing += 1
        if style == ">":
            if any(line == "" or line.startswith(" ") for line in lines):
                self.fail("a folded block scalar with blank or more-indented lines is not supported")
            body = " ".join(lines)
        else:
            body = "\n".join(lines)
        if not lines:
            return ""
        if chomp == "-":
            return body
        return body + "\n" * (1 + trailing if chomp == "+" else 1)


def parse_workflow_yaml(text: str) -> object:
    return _YamlSubset(text).document()


# ================================================================================================
# Workflow policy
# ================================================================================================


def logical_lines(script: str) -> list[str]:
    """Shell lines of a ``run`` script: continuations joined, here-document bodies and comments dropped."""
    out: list[str] = []
    pending = ""
    heredoc_end: str | None = None
    for raw in script.replace("\r\n", "\n").split("\n"):
        if heredoc_end is not None:
            if raw.strip() == heredoc_end:
                heredoc_end = None
            continue
        line = pending + raw.strip()
        if line.endswith("\\"):
            pending = line[:-1].rstrip() + " "
            continue
        pending = ""
        heredoc = re.search(r"<<-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1", line)
        if heredoc:
            heredoc_end = heredoc.group(2)
        if line and not line.startswith("#"):
            out.append(line)
    if pending.strip():
        out.append(pending.strip())
    return out


def split_commands(line: str) -> list[tuple[list[str], str]]:
    """Split one shell line into simple commands, each with the operator that follows it."""
    commands: list[tuple[list[str], str]] = []
    tokens: list[str] = []
    current = ""
    started = False
    quote = ""
    i = 0

    def flush() -> None:
        nonlocal current, started
        if started:
            tokens.append(current)
        current, started = "", False

    while i < len(line):
        char = line[i]
        if quote:
            if char == quote:
                quote = ""
            else:
                current += char
        elif char in "'\"":
            quote, started = char, True
        elif char.isspace():
            flush()
        elif char == "#" and not started:
            break
        elif line.startswith(("&&", "||"), i):
            flush()
            commands.append((tokens, line[i : i + 2]))
            tokens = []
            i += 1
        elif char in ";|&" and not (char == "&" and line[i - 1 : i] in (">", "<")) and line[i + 1 : i + 2] != ">":
            flush()
            commands.append((tokens, char))
            tokens = []
        else:
            current += char
            started = True
        i += 1
    flush()
    if tokens:
        commands.append((tokens, ""))
    return commands


_COMMAND_PREFIXES = ("{", "(", "!", "then", "do", "else", "if", "sudo", "env", "exec", "time", "command", "npx", "corepack")


def command_words(tokens: list[str]) -> list[str]:
    """The command proper: grouping characters, ``sudo``/``env`` and ``VAR=value`` prefixes removed."""
    words = [token.lstrip("({`$").rstrip(")}`") for token in tokens]
    while words and (not words[0] or words[0] in _COMMAND_PREFIXES or re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", words[0])):
        words = words[1:]
    return words


def run_script_violations(script: str) -> list[str]:
    found: list[str] = []
    for line in logical_lines(script):
        commands = split_commands(line)
        words = [command_words(tokens) for tokens, _ in commands]
        for index, (_, operator) in enumerate(commands):
            following = words[index + 1] if index + 1 < len(words) else []
            if operator == "||" and (following[:1] in (["true"], [":"]) or following[:2] == ["exit", "0"]):
                found.append(f"'|| {' '.join(following[:2])}' swallows a failure: {line[:80]}")
            if operator == "|" and words[index][:1] and words[index][0] in DOWNLOADERS and following[:1] and following[0] in INTERPRETERS:
                found.append(f"a download is piped into {following[0]}: {line[:80]}")
            current = words[index]
            for position, word in enumerate(current[:-1]):
                if word == "pnpm" and current[position + 1] in ("install", "i") and (
                    "--frozen-lockfile" not in current or "--no-frozen-lockfile" in current
                ):
                    found.append("pnpm install must use --frozen-lockfile")
        if SUBSTITUTED_DOWNLOAD.search(line):
            found.append(f"a download is executed through a shell substitution: {line[:80]}")
    return found


def runs_command(script: str, required: str) -> bool:
    """True when the script runs ``python <required...>`` as one simple command that can fail the step."""
    wanted = required.split()
    for line in logical_lines(script):
        commands = split_commands(line)
        first = command_words(commands[0][0]) if commands else []
        if first[:2] in (["exit", "0"], ["set", "+e"]):
            return False
        if len(commands) != 1 or commands[0][1] != "":
            continue
        if first[:1] in (["python"], ["python3"]) and first[1:2] == wanted[:1] and all(arg in first[2:] for arg in wanted[1:]):
            return True
    return False


def workflow_triggers(on: object) -> set[str] | None:
    if isinstance(on, str) and on:
        return {on}
    if isinstance(on, list) and on and all(isinstance(item, str) for item in on):
        return set(on)
    if isinstance(on, dict) and on:
        return set(on)
    return None


def walk_uses(node: object, found: list[object]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "uses":
                found.append(value)
            else:
                walk_uses(value, found)
    elif isinstance(node, list):
        for item in node:
            walk_uses(item, found)


def is_false(value: object) -> bool:
    return isinstance(value, str) and value.strip().lower() == "false"


def check_workflow(name: str, rel: str, text: str, tracked: set[str], errors: list[str]) -> None:
    if "--no-frozen-lockfile" in text:
        errors.append(f"{rel}: pnpm install must use --frozen-lockfile")
    try:
        tree = parse_workflow_yaml(text)
    except WorkflowSyntaxError as exc:
        errors.append(f"{rel}: cannot be parsed as a workflow ({exc})")
        return
    except (RecursionError, IndexError, TypeError, ValueError) as exc:  # pathological input: still RED, by name
        errors.append(f"{rel}: cannot be parsed as a workflow ({type(exc).__name__})")
        return

    triggers = workflow_triggers(tree.get("on"))
    if triggers is None:
        errors.append(f"{rel}: missing or malformed 'on' triggers")
        triggers = set()
    if "pull_request_target" in triggers:
        errors.append(f"{rel}: pull_request_target is not allowed")

    if "permissions" not in tree:
        errors.append(f"{rel}: missing top-level permissions block")
    elif tree["permissions"] != {"contents": "read"}:
        errors.append(f"{rel}: top-level permissions must be exactly 'contents: read'")

    uses: list[object] = []
    walk_uses(tree, uses)
    for ref in uses:
        if not isinstance(ref, str) or not (ref.startswith("./") or PINNED_ACTION.match(ref)):
            errors.append(f"{rel}: action {ref} is not pinned to a full commit SHA")

    jobs = tree.get("jobs")
    if not isinstance(jobs, dict) or not jobs:
        errors.append(f"{rel}: 'jobs' must be a non-empty mapping")
        jobs = {}
    for job_id, job in jobs.items():
        where = f"{rel}: job '{job_id}'"
        if not isinstance(job, dict):
            errors.append(f"{where} is not a mapping")
            continue
        publishing = (name, job_id) in PUBLISHING_JOBS
        if "permissions" in job and job["permissions"] != {"contents": "read"}:
            if not (publishing and job["permissions"] == {"contents": "write"}):
                errors.append(f"{where} may not widen permissions beyond 'contents: read'")
        if "if" in job and not publishing:
            errors.append(f"{where} may not be conditional ('if' is allowed on the publishing jobs only)")
        if "continue-on-error" in job and not is_false(job["continue-on-error"]):
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
            if "continue-on-error" in step and not is_false(step["continue-on-error"]):
                errors.append(f"{where} step {number} sets continue-on-error")
            if "run" in step:
                if not isinstance(step["run"], str):
                    errors.append(f"{where} step {number} has a 'run' that is not a script")
                    continue
                for violation in run_script_violations(step["run"]):
                    errors.append(f"{where} step {number}: {violation}")

    required = REQUIRED_WORKFLOW_RUNS.get(name)
    if required is None:
        return
    trigger = REQUIRED_TRIGGER.get(name, DEFAULT_REQUIRED_TRIGGER)
    if trigger not in triggers:
        errors.append(f"{rel}: required workflow no longer runs on '{trigger}'")
    for job_id, commands in required.items():
        job = jobs.get(job_id)
        steps = job.get("steps") if isinstance(job, dict) else None
        if not isinstance(steps, list):
            errors.append(f"{rel}: required job '{job_id}' is missing")
            continue
        for command in commands:
            script = command.split()[0]
            if script not in tracked:
                errors.append(f"{rel}: required command names a script that is not tracked: {script}")
            if not any(
                isinstance(step, dict)
                and isinstance(step.get("run"), str)
                and "if" not in step
                and step.get("shell", "bash") == "bash"
                and runs_command(step["run"], command)
                for step in steps
            ):
                errors.append(f"{rel}: job '{job_id}' does not run 'python {command}' unconditionally")


def validate_workflows(errors: list[str], tracked: list[str]) -> int:
    """Parse every tracked workflow and hold it to the policy; require the declared workflows to exist."""
    tracked_set = set(tracked)
    workflows = [
        rel
        for rel in tracked
        if rel.startswith(WORKFLOW_DIR) and "/" not in rel[len(WORKFLOW_DIR):] and rel.lower().endswith((".yml", ".yaml"))
    ]
    if not workflows:
        errors.append("no GitHub workflows found")
    for name in REQUIRED_WORKFLOW_RUNS:
        if WORKFLOW_DIR + name not in tracked_set:
            errors.append(f"missing required workflow: {WORKFLOW_DIR}{name}")
    for rel in workflows:
        text, reason = load(rel)
        if text is None:
            errors.append(f"{rel}: workflow {reason}")
            continue
        check_workflow(rel[len(WORKFLOW_DIR):], rel, text, tracked_set, errors)
    return len(workflows)


# ================================================================================================
# Documents
# ================================================================================================


def outside_fences(text: str) -> list[tuple[int, str]]:
    """(line number, line) for every line that is not inside or delimiting a fenced code block."""
    lines: list[tuple[int, str]] = []
    in_code = False
    for number, line in enumerate(text.split("\n"), 1):
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            lines.append((number, line))
    return lines


def document_body(text: str) -> list[str]:
    """The lines that carry a document's content: not blank, not a heading, not a comment, not code."""
    return [
        line.strip()
        for _, line in outside_fences(text)
        if line.strip() and not line.lstrip().startswith(("#", "<!--"))
    ]


def required_documents() -> list[str]:
    documents = [
        *REQUIRED_ROOT,
        *(rel for rel in REQUIRED_FOUNDATION if is_markdown(rel)),
        *(f"foundation/{chapter}/{name}" for chapter in CHAPTERS for name in ("README.md", "PROJECT_CONTEXT.md")),
        *EXPECTED_MARKERS,
        *D026_REQUIRED_REFERENCES,
        *BILINGUAL_PARITY_CONTROLS,
    ]
    return list(dict.fromkeys(documents))


def validate_required_documents(errors: list[str]) -> None:
    """A required document must be a real document, not merely exist (2026-10-09 review, item 1)."""
    for rel in required_documents():
        text, reason = load(rel)
        if text is None:
            continue  # reported by the existence checks, each with its own message
        body = document_body(text)
        joined = " ".join(body)
        body_bytes = sum(len(line.encode("utf-8")) for line in body)
        if not any(re.match(r"^# \S", line) for _, line in outside_fences(text)):
            errors.append(f"required document has no level-1 title: {rel}")
        if rel not in STATUS_METADATA_EXEMPT and not STATUS_LINE.search(text):
            errors.append(f"required document has no Status metadata line: {rel}")
        if body_bytes < MIN_BODY_BYTES:
            errors.append(f"required document is too small: {rel} has {body_bytes} body bytes, minimum {MIN_BODY_BYTES}")
        if not HY_MARK.search(text) or not EN_MARK.search(text):
            errors.append(f"required document lacks an Armenian or an English section: {rel}")
        armenian = len(ARMENIAN.findall(joined))
        latin = len(LATIN.findall(joined))
        if armenian < MIN_ARMENIAN_LETTERS:
            errors.append(f"required document has too little Armenian text: {rel} has {armenian} letters, minimum {MIN_ARMENIAN_LETTERS}")
        if latin < MIN_LATIN_LETTERS:
            errors.append(f"required document has too little English text: {rel} has {latin} letters, minimum {MIN_LATIN_LETTERS}")
        if rel not in EXPECTED_MARKERS and not re.search(END_MARKER.pattern + r"\s*$", text):
            errors.append(f"missing ending marker at the end of {rel}")


def validate_end_markers(errors: list[str]) -> None:
    """The END marker must be the last thing in the file, not merely present (item 2)."""
    for rel, marker in EXPECTED_MARKERS.items():
        text, reason = load(rel)
        if text is None:
            errors.append(f"marker-governed file {reason}: {rel}")
        elif marker not in text:
            errors.append(f"missing ending marker in {rel}: {marker}")
        elif not text.rstrip().endswith(marker):
            errors.append(f"ending marker is not at the end of {rel}: {marker}")


def prose_words(line: str) -> int:
    stripped = line.strip()
    if stripped.startswith(("|", "<")):
        return 0
    stripped = re.sub(r"`[^`]*`", " ", stripped)
    stripped = re.sub(r"\]\([^)]*\)", "]", stripped)
    stripped = re.sub(r"https?://\S+", " ", stripped)
    return len(re.findall(r"[A-Za-z]{2,}", stripped))


def validate_bilingual(errors: list[str], markdown: list[str]) -> None:
    """HY and EN must pair up, a label must be followed by text, and no section may be English-only."""
    for rel in markdown:
        text = text_of(rel)
        if text is None:
            continue
        lines = outside_fences(text)
        spans_peers = rel in LANGUAGE_BLOCK_SPANS_PEERS
        section, section_line = "(top)", 1
        counts: dict[str, list[int]] = {}
        language_level = 0  # heading level of the open language block, 0 when none
        language_headings = {"Հայերեն": 0, "English": 0}
        open_language: tuple[str, int, bool] | None = None  # (name, line, has content)
        words = armenian = 0

        def close_section() -> None:
            if not language_level and words >= ENGLISH_ONLY_WORD_LIMIT and armenian == 0:
                errors.append(
                    f"English-only section in {rel}: '{section}' (line {section_line}) has {words} English words and no Armenian"
                )

        def close_language() -> None:
            if open_language is not None and not open_language[2]:
                errors.append(f"empty language section in {rel}: '{open_language[0]}' (line {open_language[1]})")

        for index, (number, line) in enumerate(lines):
            heading = HEADING.match(line)
            if heading:
                close_section()
                level, title = len(heading.group(1)), heading.group(2)
                is_language = LANGUAGE_HEADING.match(title)
                if language_level and (level < language_level or is_language or (level == language_level and not spans_peers)):
                    close_language()
                    language_level, open_language = 0, None
                if is_language:
                    language_level = level
                    language_headings[is_language.group(1)] += 1
                    open_language = (title, number, False)
                section, section_line = title, number
                words, armenian = 0, len(ARMENIAN.findall(title))
                continue
            if line.strip() and open_language is not None and not END_MARKER.search(line):
                open_language = (open_language[0], open_language[1], True)
            words += prose_words(line)
            armenian += len(ARMENIAN.findall(line))
            label = LABEL.match(line)
            if label:
                counts.setdefault(section, [0, 0])[0 if label.group(1) == "HY" else 1] += 1
                if not label.group(2).strip() and rel not in EMPTY_LABEL_EXEMPT:
                    following = next((text for _, text in lines[index + 1 :] if text.strip()), "")
                    if not following or HEADING.match(following) or LABEL.match(following) or END_MARKER.search(following):
                        errors.append(f"bilingual label with no text in {rel} line {number}: **{label.group(1)}:**")
        close_section()
        close_language()
        for name, (hy, en) in counts.items():
            if hy != en:
                errors.append(f"bilingual label parity in {rel} section '{name}': HY={hy} EN={en}")
        if language_headings["Հայերեն"] != language_headings["English"]:
            errors.append(
                f"language section parity in {rel}: Հայերեն={language_headings['Հայերեն']} English={language_headings['English']}"
            )


def validate_decision_index(errors: list[str], tracked: list[str]) -> None:
    """Every decision file, whatever its number, must be named in the index (item 7)."""
    text = text_of("DECISION_INDEX.md")
    if text is None:
        return
    for decision_id in ("D-022", "D-023", "D-024", "D-025", "D-026", "D-027"):
        if decision_id not in text:
            errors.append(f"decision index missing {decision_id}")
    for rel in tracked:
        name = posixpath.basename(rel)
        match = DECISION_FILE.match(name)
        if not match or not is_markdown(rel) or "VALIDATION_RECORD" in name:
            continue
        if not re.search(rf"(?<![\w-]){re.escape(match.group(1))}(?!\d)", text):
            errors.append(f"decision index missing {match.group(1)} ({rel})")


INLINE_LINK = re.compile(r"\]\(\s*(<[^>\n]*>|[^)\s]+)(?:\s+(?:\"[^\"\n]*\"|'[^'\n]*'))?\s*\)")
REFERENCE_DEFINITION = re.compile(r"^ {0,3}\[(?!\^)[^\]\n]+\]:[ \t]*(<[^>\n]*>|\S+)", re.M)
HTML_TAG = re.compile(r"<[A-Za-z][^>]*>")
HTML_ATTRIBUTE = re.compile(r"\b(src|href|poster|srcset)\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s\"'>]+))")
HTML_ANCHOR = re.compile(r"\b(?:id|name)\s*=\s*(?:\"([^\"]*)\"|'([^']*)')")
_ANCHOR_CACHE: dict[str, set[str]] = {}


def link_targets(text: str) -> list[str]:
    """Every link target in a document: inline (with or without a title), reference-style, and HTML."""
    text = FENCE.sub("", text)
    targets = [match.group(1) for match in INLINE_LINK.finditer(text)]
    targets += [match.group(1) for match in REFERENCE_DEFINITION.finditer(text)]
    for tag in HTML_TAG.findall(text):
        for name, double, single, bare in HTML_ATTRIBUTE.findall(tag):
            value = double or single or bare
            if name == "srcset":
                targets += [part.split()[0] for part in value.split(",") if part.split()]
            elif value:
                targets.append(value)
    return [target[1:-1] if target.startswith("<") and target.endswith(">") else target for target in targets]


def anchors_of(rel: str) -> set[str]:
    """The anchors GitHub generates for a Markdown file's headings, plus explicit id/name attributes."""
    if rel not in _ANCHOR_CACHE:
        anchors: set[str] = set()
        seen: dict[str, int] = {}
        text = text_of(rel) or ""
        for _, line in outside_fences(text):
            heading = HEADING.match(line)
            if not heading:
                continue
            title = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading.group(2))
            title = re.sub(r"[`*]|<[^>]*>", "", title).strip().lower()
            slug = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
            count = seen.get(slug, 0)
            seen[slug] = count + 1
            anchors.add(slug if count == 0 else f"{slug}-{count}")
        for double, single in HTML_ANCHOR.findall(text):
            anchors.add(double or single)
        _ANCHOR_CACHE[rel] = anchors
    return _ANCHOR_CACHE[rel]


def validate_links(errors: list[str], tracked: list[str], markdown: list[str]) -> None:
    """Every relative link in tracked Markdown must reach a TRACKED file, and its anchor must exist."""
    tracked_set = set(tracked)
    directories = {rel[:index] for rel in tracked for index, char in enumerate(rel) if char == "/"}
    for rel in markdown:
        text = text_of(rel)
        if text is None:
            continue
        for target in link_targets(text):
            if re.match(r"^(https?:|mailto:)", target):
                continue
            path, _, fragment = target.partition("#")
            path = unquote(path.split("?", 1)[0])
            if not path:
                resolved = rel
            elif path.startswith("/"):
                resolved = posixpath.normpath(path.lstrip("/"))
            else:
                resolved = posixpath.normpath(posixpath.join(posixpath.dirname(rel), path))
            if resolved == ".." or resolved.startswith("../"):
                errors.append(f"relative link in {rel} leaves the repository: {target}")
            elif resolved == "." or resolved in directories:
                continue
            elif resolved not in tracked_set:
                if (ROOT / resolved).exists():
                    errors.append(f"relative link in {rel} points to an untracked file: {target}")
                else:
                    errors.append(f"broken relative link in {rel}: {target}")
            elif fragment and is_markdown(resolved) and unquote(fragment).lower() not in anchors_of(resolved):
                errors.append(f"broken anchor in {rel}: {target}")


def validate_inventory(errors: list[str], markdown: list[str]) -> None:
    if not INVENTORY.is_file():
        errors.append(f"missing canonical Markdown inventory: {INVENTORY_REL}")
        return
    try:
        data = json.loads(INVENTORY.read_bytes().decode("utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"invalid canonical Markdown inventory: {exc}")
        return
    if not isinstance(data, dict):
        errors.append("Markdown inventory must be a JSON object")
        return

    entries = data.get("files")
    declared_count = data.get("file_count")
    if not isinstance(entries, list):
        errors.append("Markdown inventory 'files' must be a list")
        return
    if declared_count != len(entries):
        errors.append(f"Markdown inventory count mismatch: declared {declared_count}, actual {len(entries)}")

    manifest_paths = [
        entry.get("path") for entry in entries if isinstance(entry, dict) and isinstance(entry.get("path"), str)
    ]
    if len(manifest_paths) != len(entries):
        errors.append("Markdown inventory contains entries without a path")
    if manifest_paths != sorted(manifest_paths):
        errors.append("Markdown inventory paths are not sorted")
    if len(manifest_paths) != len(set(manifest_paths)):
        errors.append("Markdown inventory contains duplicate paths")
    if manifest_paths != markdown:
        missing = sorted(set(markdown) - set(manifest_paths))
        stale = sorted(set(manifest_paths) - set(markdown))
        if missing:
            errors.append(f"Markdown inventory missing tracked files: {', '.join(missing)}")
        if stale:
            errors.append(f"Markdown inventory contains untracked files: {', '.join(stale)}")
        if not missing and not stale:
            errors.append("Markdown inventory path ordering differs from git ls-files")

    by_path = {entry["path"]: entry for entry in entries if isinstance(entry, dict) and isinstance(entry.get("path"), str)}
    for rel in markdown:
        path = ROOT / rel
        entry = by_path.get(rel)
        if entry is None or not path.is_file():
            continue  # a tracked file missing from the checkout is reported once, by name, elsewhere
        try:
            actual_size = path.stat().st_size
            actual_sha = sha256_file(path)
        except OSError as exc:
            errors.append(f"cannot read inventoried file {rel}: {exc.strerror or exc}")
            continue
        if entry.get("bytes") != actual_size:
            errors.append(
                f"Markdown inventory size drift for {rel}: expected {entry.get('bytes')}, actual {actual_size}"
            )
        if entry.get("sha256") != actual_sha:
            errors.append(f"Markdown inventory SHA-256 drift for {rel}")


def validate_required_files(errors: list[str]) -> None:
    for rel in (*REQUIRED_ROOT, *REQUIRED_FOUNDATION):
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")
    for chapter in CHAPTERS:
        for name in ("README.md", "PROJECT_CONTEXT.md"):
            rel = f"foundation/{chapter}/{name}"
            if not (ROOT / rel).is_file():
                errors.append(f"missing chapter file: {rel}")


def validate_d026_synchronization(errors: list[str]) -> None:
    for rel, references in D026_REQUIRED_REFERENCES.items():
        text, reason = load(rel)
        if text is None:
            errors.append(f"D-026 synchronization file {reason}: {rel}")
            continue
        for reference in references:
            if reference not in text:
                errors.append(f"{rel} missing D-026 reference: {reference}")

    text = text_of("foundation/PROJECT_CONTEXT.md")
    if text is not None and re.search(r"AI Collaboration.*Pending", text, flags=re.IGNORECASE):
        errors.append("foundation context still marks AI Collaboration Pending")

    for rel in BILINGUAL_PARITY_CONTROLS:
        text, reason = load(rel)
        if text is None:
            errors.append(f"bilingual parity control {reason}: {rel}")
        elif not re.search(r"^## Հայերեն", text, re.M) or not re.search(r"^## English", text, re.M):
            errors.append(f"bilingual sections missing in {rel}")


def main() -> int:
    errors: list[str] = []
    counts = {"workflows": 0, "markdown": 0}

    def guarded(name: str, check, *args) -> object:
        try:
            return check(errors, *args)
        except Exception as exc:  # a validator answers RED, never with a traceback
            errors.append(f"internal validator error in {name}: {type(exc).__name__}: {exc}")
            return None

    tracked = guarded("tracked files", tracked_files)
    if tracked is not None:
        markdown = [rel for rel in tracked if is_markdown(rel)]
        counts["markdown"] = len(markdown)
        counts["workflows"] = guarded("workflow policy", validate_workflows, tracked) or 0
        guarded("tracked Markdown", validate_tracked_markdown_readable, markdown)
        guarded("bilingual parity", validate_bilingual, markdown)
        guarded("required files", validate_required_files)
        guarded("required document content", validate_required_documents)
        guarded("ending markers", validate_end_markers)
        guarded("decision index", validate_decision_index, tracked)
        guarded("D-026 synchronization", validate_d026_synchronization)
        guarded("links", validate_links, tracked, markdown)
        guarded("Markdown inventory", validate_inventory, markdown)

    if errors:
        print("FOUNDATION VALIDATION: RED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("FOUNDATION VALIDATION: GREEN")
    print(
        f"Validated {len(CHAPTERS)} Foundation chapters, root controls, "
        f"D-026 synchronization, {counts['workflows']} workflows, and {counts['markdown']} tracked Markdown files."
    )
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    sys.exit(main())
