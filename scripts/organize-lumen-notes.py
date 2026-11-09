#!/usr/bin/env python3
"""Organize raw Lumen course folders into trimester notes layout (trimester-3 style).

- ``{subject}/transcriptions/week-NN/`` — plain text from ``.vtt``
- ``{subject}/week-NN/`` — Markdown from module presentation ``.pdf``

Run from repo root:

    python3 scripts/organize-lumen-notes.py bits-pilani/trimester-4
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

COURSE_SLUGS: dict[str, str] = {
    "Analytics_for_E-Commerce_Lumen": "analytics-for-e-commerce",
    "Analytics_for_Retail_Management_Lumen": "analytics-for-retail-management",
    "Deep_Learning_Lumen": "deep-learning",
    "Optimization_Methods_for_Analytics_Lumen": "optimization-methods-for-analytics",
}

WEEK_DIR_RE = re.compile(r"^Week_(\d+)$", re.IGNORECASE)
TIMESTAMP_RE = re.compile(
    r"^\d{2}:\d{2}:\d{2}\.\d{3}\s+-->\s+\d{2}:\d{2}:\d{2}\.\d{3}\s*$"
)
NOTE_INDEX_RE = re.compile(r"^(\d+)$")


def slugify(name: str) -> str:
    name = re.sub(r"\.(vtt|pdf)$", "", name, flags=re.IGNORECASE)
    name = re.sub(r"^Week_\d+_", "", name, flags=re.IGNORECASE)
    name = name.replace("_", "-").lower()
    name = re.sub(r"[^a-z0-9-]+", "-", name)
    return re.sub(r"-+", "-", name).strip("-")


def humanize_slug(slug: str) -> str:
    slug = re.sub(r"-(transcript|presentation)$", "", slug)
    return " ".join(w.capitalize() for w in slug.split("-"))


def vtt_to_plaintext(path: Path) -> str:
    lines: list[str] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line == "WEBVTT":
            continue
        if TIMESTAMP_RE.match(line) or NOTE_INDEX_RE.match(line):
            continue
        # Drop speaker prefix when present (e.g. "Name: text")
        if ": " in line and line.split(": ", 1)[0].split() and len(line.split(": ", 1)[0]) < 40:
            _, text = line.split(": ", 1)
            line = text.strip()
        lines.append(line)
    return "\n".join(lines)


def pdf_to_markdown(pdf_path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        capture_output=True,
        text=True,
        check=True,
    )
    body = result.stdout.replace("\f", "\n\n").strip()
    title = humanize_slug(slugify(pdf_path.name))
    return f"# {title}\n\n{body}\n"


def transcript_sort_key(filename: str) -> tuple[int, str]:
    lower = filename.lower()
    if "makeup" in lower:
        return (1, filename)
    return (0, filename)


def organize_course(raw_dir: Path, notes_root: Path) -> None:
    slug = COURSE_SLUGS.get(raw_dir.name)
    if not slug:
        print(f"skip unknown course folder: {raw_dir.name}")
        return

    subject_dir = notes_root / slug
    subject_dir.mkdir(parents=True, exist_ok=True)

    for week_dir in sorted(raw_dir.iterdir()):
        m = WEEK_DIR_RE.match(week_dir.name)
        if not (week_dir.is_dir() and m):
            continue
        week_num = int(m.group(1))
        week_slug = f"week-{week_num:02d}"

        trans_dir = subject_dir / "transcriptions" / week_slug
        note_week_dir = subject_dir / week_slug

        transcripts = week_dir / "Transcripts"
        if transcripts.is_dir():
            trans_dir.mkdir(parents=True, exist_ok=True)
            vtt_files = sorted(
                transcripts.glob("*.vtt"),
                key=lambda p: transcript_sort_key(p.name),
            )
            for i, vtt in enumerate(vtt_files, start=1):
                stem = slugify(vtt.name)
                if not stem.endswith("-transcript"):
                    stem += "-transcript"
                out = trans_dir / f"{i:02d}-{stem}.txt"
                out.write_text(vtt_to_plaintext(vtt) + "\n", encoding="utf-8")
                print(f"  txt  {out.relative_to(REPO_ROOT)}")

        presentations = week_dir / "Presentations"
        if presentations.is_dir():
            note_week_dir.mkdir(parents=True, exist_ok=True)
            pdfs = sorted(presentations.glob("*.pdf"), key=lambda p: p.name)
            for i, pdf in enumerate(pdfs, start=1):
                stem = slugify(pdf.name)
                if not stem.endswith("-presentation"):
                    stem += "-presentation"
                out = note_week_dir / f"{i:02d}-{stem}.md"
                out.write_text(pdf_to_markdown(pdf), encoding="utf-8")
                print(f"  md   {out.relative_to(REPO_ROOT)}")


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    trimester_dir = Path(sys.argv[1]).resolve()
    if not trimester_dir.is_dir():
        print(f"not a directory: {trimester_dir}")
        sys.exit(1)

    notes_root = trimester_dir / "notes"
    notes_root.mkdir(parents=True, exist_ok=True)

    raw_dirs = [
        p
        for p in trimester_dir.iterdir()
        if p.is_dir() and p.name.endswith("_Lumen")
    ]
    if not raw_dirs:
        print(f"no *_Lumen folders under {trimester_dir}")
        sys.exit(1)

    for raw in sorted(raw_dirs):
        print(f"course {raw.name} -> {COURSE_SLUGS.get(raw.name, '?')}")
        organize_course(raw, notes_root)

    if "--remove-raw" in sys.argv:
        for raw in raw_dirs:
            shutil.rmtree(raw)
            print(f"removed {raw.relative_to(REPO_ROOT)}")

    print(f"Done. Notes under {notes_root.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
