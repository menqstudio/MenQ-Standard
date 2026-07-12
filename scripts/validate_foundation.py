#!/usr/bin/env python3
"""Validate MenQ Foundation documentation and D-026 session-read integrity."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "foundation/ai-collaboration/MARKDOWN_INVENTORY.json"

CHAPTERS = (
    "philosophy",
    "principles",
    "terminology",
    "governance",
    "decision-system",
    "documentation",
    "ai-collaboration",
)

