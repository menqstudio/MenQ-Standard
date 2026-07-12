#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace(path: str, old: str, new: str) -> None:
    file = ROOT / path
    text = file.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"Missing expected block in {path}: {old[:90]!r}")
    file.write_text(text.replace(old, new, 1), encoding="utf-8")


def prepend(path: str, section: str) ->