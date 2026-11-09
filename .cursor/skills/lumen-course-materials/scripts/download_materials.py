#!/usr/bin/env python3
"""Download Lumen manifest entries via curl (handles gzip/br)."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


def download(url: str, dest: Path, cookie: str | None) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["curl", "-fsSL", "--compressed"]
    if cookie:
        cmd.extend(["-H", f"Cookie: {cookie.strip()}"])
    cmd.extend(["-H", "User-Agent: Mozilla/5.0", "-o", str(dest), url])
    subprocess.run(cmd, check=True, timeout=120)
    head = dest.read_bytes()[:16]
    if head.startswith(b"WEBVTT"):
        return
    if head.startswith(b"%PDF"):
        return
    preview = dest.read_text(errors="replace")[:120]
    dest.unlink(missing_ok=True)
    raise RuntimeError(f"expected VTT or PDF, got: {preview!r}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dir",
        type=Path,
        required=True,
        help="Course folder containing manifest.json",
    )
    args = parser.parse_args()
    base = args.dir.resolve()
    manifest = base / "manifest.json"
    cookie_file = base / ".session_cookie"
    if not manifest.is_file():
        print(f"Missing {manifest}", file=sys.stderr)
        sys.exit(1)
    cookie = cookie_file.read_text().strip() if cookie_file.is_file() else None
    if not cookie:
        print("Warning: no .session_cookie; downloads may fail", file=sys.stderr)

    for entry in json.loads(manifest.read_text()):
        sub = "Transcripts" if entry.get("kind") == "transcript" else "Presentations"
        dest = base / entry["week_folder"] / sub / unquote(entry["filename"])
        if dest.is_file() and dest.stat().st_size > 0:
            head = dest.read_bytes()[:8]
            if head.startswith(b"WEBVTT") or head.startswith(b"%PDF"):
                print(f"skip {dest}")
                continue
        try:
            download(entry["url"], dest, cookie)
            print(f"OK {dest} ({dest.stat().st_size} bytes)")
        except Exception as e:
            print(f"FAIL {entry.get('filename')}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
