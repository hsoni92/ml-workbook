---
name: lumen-course-materials
description: >-
  Downloads lecture recording transcripts (.vtt) and module presentations (.pptx as PDF) from BITS Pilani Lumen (Brightspace) courses and organizes them on the user Desktop. Use when the user shares a lumen.bitspilani-digital.edu.in course or lessons URL, asks to download transcripts, module decks, or weekly materials from Lumen, or references a prior Deep Learning / Retail / E-Commerce course download.
---

# Lumen course materials

## Prerequisites

1. **Browser MCP** (`browsermcp` in `~/.cursor/mcp.json`) connected to Chrome where the user is logged into Lumen. See [browser-mcp-setup.md](browser-mcp-setup.md) if MCP fails (`nvm` `PATH` on Linux).
2. User session must be active (SSO). If downloads return HTML login pages, refresh Lumen in Chrome and re-read cookies from Browser MCP `request` headers.

## Inputs

| Input | Example |
|-------|---------|
| Course lessons URL | `https://lumen.bitspilani-digital.edu.in/d2l/le/lessons/7207` |
| Org unit ID (`ou`) | `7207` (from URL path) |

Derive a Desktop folder name from the course title (`get title` after navigation), e.g. `Deep_Learning_Lumen`, `Analytics_for_E-Commerce_Lumen`.

**Base path:** `~/Desktop/<Course_Slug>_Lumen/`

**Layout:**

```text
Week_01/Transcripts/*.vtt
Week_01/Presentations/*.pdf
```

Use zero-padded week numbers (`Week_01` … `Week_13`). Put makeup sessions in the same week folder with `Makeup` in the filename.

## Workflow

Copy and track progress:

```text
- [ ] Open course in Browser MCP (Chrome profile with Lumen login)
- [ ] List week units
- [ ] Per week: find Transcript + Module/pptx topics
- [ ] Resolve enforced file URLs
- [ ] Write manifest.json + download
- [ ] Validate WEBVTT / PDF bytes
- [ ] Remove .session_cookie
- [ ] Summarize gaps (missing weeks, no decks)
```

### 1. Discover weeks

```text
browser use "Chrome"
goto <lessons_url>
wait 5000
find "Week" --max all
```

Week unit links look like `/d2l/le/lessons/<ou>/units/<unitId>`.

### 2. Per-week topics

For each week unit URL:

```text
goto https://lumen.bitspilani-digital.edu.in/d2l/le/lessons/<ou>/units/<unitId>
wait 1500
find "Transcript"
find "pptx"
find "Recording"    # if Transcript empty
```

Course-wide (optional): `find "pptx" --max all` on the lessons root.

**Presentations:** Often titled `ModuleN_...Summary.pptx`. Open the topic → `requests --filter "enforced"` → use the `...pptx.pdf` URL under `/content/enforced/`.

**Transcripts:** Open topic → `find ".vtt"` → note the `url=` on the inner link (relative filename).

### 3. Enforced content prefix

Pattern: `https://lumen.bitspilani-digital.edu.in/content/enforced/<ou>-T1-26_<COURSE_CODE>/`

Discover `<COURSE_CODE>` by opening any `.vtt` in the browser (`click` inner link or `goto` full URL) and matching `requests --filter "enforced"`.

Full transcript URL:

```text
https://lumen.bitspilani-digital.edu.in/content/enforced/<prefix>/<URL-encoded-filename>.vtt
```

### 4. manifest.json

Write `~/Desktop/<Course_Slug>_Lumen/manifest.json`:

```json
[
  {
    "week_folder": "Week_01",
    "kind": "transcript",
    "filename": "Week_1_Lecture_Recording_Transcript.vtt",
    "url": "https://lumen.bitspilani-digital.edu.in/content/enforced/..."
  },
  {
    "week_folder": "Week_01",
    "kind": "presentation",
    "filename": "Module1_Summary.pdf",
    "url": "https://lumen.bitspilani-digital.edu.in/content/enforced/....pptx.pdf"
  }
]
```

`kind`: `transcript` → `Transcripts/` subfolder; anything else → `Presentations/`.

### 5. Download (required method)

**Do not use `urllib` without decompression** — it often saves Lumen login HTML as `.vtt`.

1. Copy `Cookie` from Browser MCP `request` on a successful `GET` to an enforced file (same host).
2. Write `.<course_dir>/.session_cookie` (one line, no `Cookie:` prefix).
3. From the **ml-workbook** repo root, run:

```bash
python3 .cursor/skills/lumen-course-materials/scripts/download_materials.py \
  --dir ~/Desktop/<Course_Slug>_Lumen
```

4. Delete `.session_cookie` when done.

**Validation:** Transcripts must start with `WEBVTT`. PDFs should start with `%PDF`. Re-download any file that begins with `<!DOCTYPE html>`.

**Presentations:** Lumen usually serves slide decks as PDF (`Module....pptx.pdf`), not raw `.pptx`.

### 6. Report to user

Include a table: week × transcript × presentation, note missing uploads, duplicate/mislinked Lumen files, and manifest/script paths for re-runs.

## Browser MCP command cheatsheet

| Goal | Commands |
|------|----------|
| Topic file link | `find ".vtt"` on transcript topic page |
| Deck URL | `goto` topic → `wait 4000` → `requests --filter "enforced"` |
| Session cookie | `request <id>` after loading enforced file in browser |
| Download button (viewer) | `click getByText('Download')` |

Iframe refs (e.g. `f51e5`) change per page — always `find` or `snapshot -i` before `click`.

## Security

- Never commit `.session_cookie` or paste cookies into chat.
- Do not store passwords; user logs in via Chrome SSO.

## Scripts

| Script | Purpose |
|--------|---------|
| [scripts/download_materials.py](scripts/download_materials.py) | `curl --compressed` downloader + WEBVTT/PDF checks |

Optional: copy `download_materials.py` into the course Desktop folder so the user can re-run after updating `manifest.json`.

## Additional resources

- [browser-mcp-setup.md](browser-mcp-setup.md) — `~/.cursor/mcp.json` for Browser MCP on Linux/nvm
