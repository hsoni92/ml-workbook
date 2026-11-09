#!/usr/bin/env python3
"""Number, index, and cross-link course notes under ``bits-pilani/.../notes``.

Three jobs, all idempotent so the script can be re-run after adding weeks:

1. Zero-pad ``week-N`` folders and ``N-*`` note files (under each subject and
   under ``transcriptions/``) so GitHub's lexicographic listing shows them in
   reading order.
2. Write a ``README.md`` index per subject: notes by week, plus an alphabetical
   topic index and any ``stories/`` files.
3. Append a ``← Previous · Index · Next →`` footer to every note, chaining all
   notes of a subject into one linear sequence.

Run from anywhere: ``python3 scripts/number-notes.py [NOTES_DIR]``
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = REPO_ROOT / "bits-pilani" / "trimester-3" / "notes"

WEEK_RE = re.compile(r"^week-(\d+)$")
NOTE_NUM_RE = re.compile(r"^(\d+)-")
FOOTER_RE = re.compile(
    r"\n---\n\n\*\*← \[Previous\]\([^\n]*\) · \[Index\]\([^\n]*\) · \[Next\]\([^\n]*\) →\*\*\s*$"
)


def git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True)


def humanize(name: str) -> str:
    """Turn a filename slug into display text."""
    name = NOTE_NUM_RE.sub("", name)
    for suffix in (
        "-summary-presentation",
        "-makeup-transcript",
        "-transcript",
        "-presentation",
    ):
        name = re.sub(re.escape(suffix) + r"$", "", name)
    return " ".join(w.capitalize() for w in name.replace("-", " ").split())


def subject_title(subject: str) -> str:
    return " ".join(w.capitalize() for w in subject.split("-"))


def first_h1(path: Path) -> str | None:
    """Return the file's first H1 heading, or None."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("# "):
            return stripped[2:].strip()
        break
    return None


def rename(src: Path, dst: Path) -> None:
    """Rename via git mv so the change is staged; fall back to os.rename."""
    try:
        git(REPO_ROOT, "mv", str(src), str(dst))
    except subprocess.CalledProcessError:
        os.rename(src, dst)


def zero_pad_week(path: Path) -> Path:
    """Zero-pad a week folder name (week-1 -> week-01). Returns new path."""
    m = WEEK_RE.match(path.name)
    if not m:
        return path
    n = int(m.group(1))
    if 0 < n < 10:
        target = path.with_name(f"week-{n:02d}")
        if not target.exists():
            rename(path, target)
            return target
    return path


def zero_pad_note(path: Path) -> Path:
    """Zero-pad a numbered note filename (1-foo.md -> 01-foo.md)."""
    m = NOTE_NUM_RE.match(path.stem)
    if not m:
        return path
    n = int(m.group(1))
    if n < 10:
        new_stem = NOTE_NUM_RE.sub(f"{n:02d}-", path.stem)
        target = path.with_name(new_stem + path.suffix)
        if not target.exists():
            rename(path, target)
            return target
    return path


def process_weeks_root(root: Path) -> None:
    """Zero-pad week folders directly under ``root`` and the files inside them."""
    for week_dir in list(root.iterdir()):
        if not (week_dir.is_dir() and WEEK_RE.match(week_dir.name)):
            continue
        week_dir = zero_pad_week(week_dir)
        for f in list(week_dir.iterdir()):
            if f.is_file():
                zero_pad_note(f)


def collect_notes(subject_dir: Path) -> list[Path]:
    """All note files in reading order (week number, then note number)."""
    entries: list[tuple[int, int, Path]] = []
    for week_dir in subject_dir.iterdir():
        m = WEEK_RE.match(week_dir.name)
        if not (week_dir.is_dir() and m):
            continue
        for f in week_dir.iterdir():
            if f.is_file() and f.suffix == ".md":
                n = NOTE_NUM_RE.match(f.stem)
                num = int(n.group(1)) if n else 2**31 - 1
                entries.append((int(m.group(1)), num, f))
    entries.sort()
    return [p for _, _, p in entries]


def link_to(note: Path, target: Path) -> str:
    return os.path.relpath(str(target), start=str(note.parent))


def write_footer(note: Path, prev: str, next_link: str) -> None:
    """Append (or refresh) the navigation footer on a note."""
    footer = f"---\n\n**← [Previous]({prev}) · [Index](../README.md) · [Next]({next_link}) →**\n"
    text = note.read_text(encoding="utf-8")
    if FOOTER_RE.search(text):
        text = FOOTER_RE.sub("", text).rstrip("\n") + "\n"
    text = text.rstrip("\n") + "\n\n" + footer
    note.write_text(encoding="utf-8", data=text)


def generate_subject_index(subject_dir: Path, notes: list[Path]) -> None:
    lines = [
        f"# {subject_title(subject_dir.name)}",
        "",
        "Lecture and deck notes grouped by teaching week. File names match the",
        "topic in each note's title. Jump by week below or use the",
        "[topic index](#topic-index) for alphabetical lookup.",
        "",
    ]
    mind_map = subject_dir / "mind-map.md"
    if mind_map.is_file():
        lines += [
            "**Revision:** [Mind map](mind-map.md) — acronyms and one-liners for the whole course.",
            "",
        ]
    current_week: int | None = None
    topic_rows: list[tuple[str, str, int, Path]] = []
    for note in notes:
        week_num = int(WEEK_RE.match(note.parent.name).group(1))
        title = first_h1(note) or humanize(note.stem)
        topic_rows.append((title.lower(), title, week_num, note))
        if week_num != current_week:
            if current_week is not None:
                lines.append("")
            lines += [f"## Week {week_num}", ""]
            current_week = week_num
        lines.append(f"1. [{title}]({note.relative_to(subject_dir).as_posix()})")
    if not notes:
        lines += ["_No week notes yet. Transcripts may still be under_ `transcriptions/`.", ""]
    if topic_rows:
        lines += ["", "## Topic index", ""]
        lines.append("| Topic | Week |")
        lines.append("| --- | --- |")
        for _, title, week_num, note in sorted(topic_rows, key=lambda r: r[0]):
            rel = note.relative_to(subject_dir).as_posix()
            lines.append(f"| [{title}]({rel}) | {week_num} |")
    stories = subject_dir / "stories"
    if stories.is_dir():
        story_files = sorted(stories.glob("*.md"))
        if story_files:
            lines += ["", "## Stories", ""]
            for sf in story_files:
                title = first_h1(sf) or sf.stem
                lines.append(f"1. [{title}](stories/{sf.name})")
    (subject_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate_top_index() -> None:
    subjects = sorted(d for d in NOTES_DIR.iterdir() if d.is_dir())
    trimester = NOTES_DIR.parent.name
    title = " ".join(w.capitalize() for w in trimester.split("-")) + " Notes"
    rel_notes = NOTES_DIR.relative_to(REPO_ROOT)
    lines = [
        f"# {title}",
        "",
        "Course notes by subject. Open a subject index for a **week-by-week** list",
        "and an alphabetical **topic index**. Each note links to the previous and",
        "next topic in reading order.",
        "",
        "Maintain indexes and cross-links:",
        "",
        "```bash",
        f"python3 scripts/rename-notes-by-topic.py {rel_notes.as_posix()}",
        f"python3 scripts/number-notes.py {rel_notes.as_posix()}",
        "```",
        "",
        "## Subjects",
        "",
        "| Subject | Topics | Index |",
        "| --- | ---: | --- |",
    ]
    for d in subjects:
        count = len(collect_notes(d))
        name = subject_title(d.name)
        mind = " — [mind map]({}/mind-map.md)".format(d.name) if (d / "mind-map.md").is_file() else ""
        lines.append(
            f"| {name} | {count} | [{name}]({d.name}/README.md){mind} |"
        )
    (NOTES_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    global NOTES_DIR
    notes_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else NOTES_DIR
    NOTES_DIR = notes_dir
    subjects = sorted(p for p in notes_dir.iterdir() if p.is_dir())
    for subject_dir in subjects:
        process_weeks_root(subject_dir)
        trans = subject_dir / "transcriptions"
        if trans.is_dir():
            process_weeks_root(trans)
    for subject_dir in subjects:
        notes = collect_notes(subject_dir)
        for i, note in enumerate(notes):
            prev = link_to(note, notes[i - 1]) if i > 0 else "../README.md"
            next_link = link_to(note, notes[i + 1]) if i < len(notes) - 1 else "../README.md"
            write_footer(note, prev, next_link)
        generate_subject_index(subject_dir, notes)
    generate_top_index()
    total = sum(len(collect_notes(d)) for d in subjects)
    print(f"Done: {len(subjects)} subjects, {total} notes under {notes_dir}")


if __name__ == "__main__":
    main()
