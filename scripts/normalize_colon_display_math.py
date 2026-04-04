#!/usr/bin/env python3
"""Merge colon-introduced single-line $$ blocks into inline $...$ under bits-pilani/trimester-2/notes."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "bits-pilani/trimester-2/notes"
FORMULA_MAX_LEN = 130

PATTERN_IND = re.compile(
    r"(^|\n)([^\n]+:)\s*\n( +)\$\$\n\3([^\n]+)\n\3\$\$",
    re.MULTILINE,
)
PATTERN_PLAIN = re.compile(
    r"(^|\n)([^\n]+:)\s*\n\$\$\n([^\n]+)\n\$\$",
    re.MULTILINE,
)


def should_inline(formula: str) -> bool:
    t = formula.strip()
    if not t or r"\\" in t or r"\begin{" in t:
        return False
    # Keep summations / stacked operators as display for readability
    if r"\sum" in t:
        return False
    return len(t) <= FORMULA_MAX_LEN


def immediate_next_is_display(suffix: str) -> bool:
    return bool(re.match(r"\s*\n\s*\$\$", suffix))


def merge_colon_blocks(text: str) -> str:
    while True:
        candidates: list[tuple[int, int, int, str, re.Match[str]]] = []
        for m in PATTERN_IND.finditer(text):
            candidates.append((m.start(), m.end(), 1, "ind", m))
        for m in PATTERN_PLAIN.finditer(text):
            candidates.append((m.start(), m.end(), 0, "plain", m))
        candidates.sort(key=lambda x: (x[0], -x[2], x[1]))
        applied = False
        for start, end, _prio, kind, m in candidates:
            prefix = m.group(1)
            colon_line = m.group(2).rstrip()
            formula = (m.group(4) if kind == "ind" else m.group(3)).strip()
            suffix = text[end:]
            if not should_inline(formula) or immediate_next_is_display(suffix):
                continue
            replacement = prefix + colon_line + " $" + formula + "$"
            text = text[:start] + replacement + text[end:]
            applied = True
            break
        if not applied:
            break
    return text


def add_spacing_after_colon_inline(text: str) -> str:
    text = re.sub(
        r"(^[^ \n\t][^\n]*: \$[^\n]+\$)\n(\*\*)",
        r"\1\n\n\2",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"(^[^ \n\t][^\n]*: \$[^\n]+\$)\n(- )",
        r"\1\n\n\2",
        text,
        flags=re.MULTILINE,
    )
    return text


def process_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    merged = merge_colon_blocks(raw)
    final = add_spacing_after_colon_inline(merged)
    if final != raw:
        path.write_text(final, encoding="utf-8")
        return True
    return False


def main() -> int:
    updated = 0
    for path in sorted(ROOT.rglob("*.md")):
        if process_file(path):
            print(path.relative_to(ROOT.parent.parent.parent))
            updated += 1
    print(f"Updated {updated} files.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
