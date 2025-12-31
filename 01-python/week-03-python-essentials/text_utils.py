from __future__ import annotations

import re
from typing import List


_WHITESPACE_RE = re.compile(r"\s+")
_SENTENCE_SPLIT_RE = re.compile(r"[.!?]+")


def clean_text(text: str, *, lowercase: bool = False) -> str:
    """Normalize whitespace and optionally lowercase.

    - Collapses runs of whitespace (spaces/newlines/tabs) into single spaces
    - Trims leading/trailing whitespace
    """
    if text is None:
        return ""
    cleaned = _WHITESPACE_RE.sub(" ", text).strip()
    return cleaned.lower() if lowercase else cleaned


def split_sentences(text: str) -> List[str]:
    """Very simple sentence splitter on `.`, `!`, `?`.

    Returns non-empty, trimmed sentence strings.
    """
    if not text:
        return []
    parts = _SENTENCE_SPLIT_RE.split(text)
    return [p.strip() for p in parts if p.strip()]
