#!/usr/bin/env python3
"""Rename week note files to ``NN-<topic-slug>-<kind>.md`` using each file's H1.

Kinds: ``transcript``, ``makeup-transcript``, ``summary-presentation``.

Run from repo root::

    python3 scripts/rename-notes-by-topic.py bits-pilani/trimester-4/notes
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE_NUM_RE = re.compile(r"^(\d+)-")
WEEK_RE = re.compile(r"^week-(\d+)$")


def first_h1(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("# "):
            return stripped[2:].strip()
        break
    return None


def slugify_title(title: str, *, max_len: int = 72) -> str:
    t = title.lower().replace("&", "and")
    t = re.sub(r"[:/]", " ", t)
    t = re.sub(r"['']", "", t)
    t = re.sub(r"[^a-z0-9\s-]", "", t)
    t = re.sub(r"\s+", "-", t.strip())
    t = re.sub(r"-+", "-", t)
    if len(t) > max_len:
        t = t[:max_len].rsplit("-", 1)[0]
    return t or "topic"


def kind_suffix(stem: str) -> str:
    lower = stem.lower()
    if "presentation" in lower:
        return "summary-presentation"
    if "makeup" in lower:
        return "makeup-transcript"
    return "transcript"


def git_mv(src: Path, dst: Path) -> None:
    try:
        subprocess.run(
            ["git", "-C", str(REPO_ROOT), "mv", str(src), str(dst)],
            check=True,
        )
    except subprocess.CalledProcessError:
        os.rename(src, dst)


def target_name(path: Path) -> str:
    m = NOTE_NUM_RE.match(path.stem)
    num = int(m.group(1)) if m else 1
    h1 = first_h1(path) or path.stem
    slug = slugify_title(h1)
    suffix = kind_suffix(path.stem)
    return f"{num:02d}-{slug}-{suffix}.md"


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    notes_dir = Path(sys.argv[1]).resolve()
    renamed = 0
    for subject_dir in sorted(n for n in notes_dir.iterdir() if n.is_dir()):
        if subject_dir.name == "transcriptions":
            continue
        for week_dir in sorted(subject_dir.iterdir()):
            if not (week_dir.is_dir() and WEEK_RE.match(week_dir.name)):
                continue
            for path in sorted(week_dir.glob("*.md")):
                target = target_name(path)
                dst = path.with_name(target)
                if path.name == target:
                    continue
                if dst.exists() and dst != path:
                    raise SystemExit(
                        f"collision: {path} -> {target} (exists: {dst})"
                    )
                print(f"  {path.relative_to(REPO_ROOT)} -> {target}")
                git_mv(path, dst)
                renamed += 1
    print(f"Done: {renamed} rename(s) under {notes_dir}")


if __name__ == "__main__":
    main()
