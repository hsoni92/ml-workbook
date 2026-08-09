#!/usr/bin/env python3
"""Generate one compact PDF per subject under bits-pilani/trimester-3/notes.

Concatenates every week-*/*.md note (plus stories/) into a single, densely
typeset HTML bundle — compact font, tight margins, no forced page break per
file, an in-document table of contents, and page-number footer — then prints
to PDF via headless Chromium (Playwright). Mermaid diagrams and LaTeX math are
rendered just like on GitHub, reusing the pipeline in scripts/notes-pdf-gen.py.

Usage
-----
First-time setup (once per machine, installs Chromium):

    make notes-pdf-setup
    # or, equivalently:
    cd scripts && uv sync && uv run playwright install chromium

Generate PDFs for every subject (writes to
``<notes-root>/<subject>/<subject>.pdf``):

    make notes-pdf-t3
    # or directly:
    cd scripts && uv run python ../notes-pdf-compact.py

Generate PDFs for one or more specific subjects:

    make notes-pdf-t3 ARGS="--subject natural-language-processing-and-understanding"
    cd scripts && uv run python ../notes-pdf-compact.py --subject principle-of-marketing

Keep the intermediate HTML alongside the PDF (for debugging):

    cd scripts && uv run python ../notes-pdf-compact.py --subject neural-networks --keep-html

Use a different notes root:

    cd scripts && uv run python ../notes-pdf-compact.py --notes-root /path/to/notes

Flags
-----
    --subject NAME     Subject dir name to process. Repeatable. Defaults to all.
    --notes-root PATH  Root notes directory. Default: bits-pilani/trimester-3/notes.
    --keep-html        Write <subject>.html next to the PDF for debugging.

Requires network access on first run because mermaid.js, MathJax, and
github-markdown-css are loaded from a CDN when Chromium opens the HTML.
"""
from __future__ import annotations

import argparse
import html
import importlib.util
import re
import sys
import tempfile
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
DEFAULT_NOTES_ROOT = REPO_ROOT / "bits-pilani" / "trimester-3" / "notes"

# Reuse the markdown renderer and discovery helpers from the existing script.
_SPEC = importlib.util.spec_from_file_location(
    "notes_pdf_gen", SCRIPTS_DIR / "notes-pdf-gen.py"
)
gen = importlib.util.module_from_spec(_SPEC)
assert _SPEC.loader is not None
_SPEC.loader.exec_module(gen)

FIRST_H1_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)


# ---------------------------------------------------------------------------
# Content discovery
# ---------------------------------------------------------------------------


def collect_notes(subject_dir: Path) -> list[tuple[int | None, Path]]:
    """Return (week_number, note_path) pairs in reading order; stories last."""
    items: list[tuple[int | None, Path]] = []
    for week_dir in gen.discover_week_dirs(subject_dir):
        m = gen.WEEK_DIR_RE.match(week_dir.name)
        week_num = int(m.group(1)) if m else 0
        for f in gen.discover_md_files(week_dir):
            items.append((week_num, f))
    stories_dir = subject_dir / "stories"
    if stories_dir.is_dir():
        for f in sorted(stories_dir.glob("*.md")):
            items.append((None, f))
    return items


def first_h1(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = FIRST_H1_RE.search(text)
    return m.group(1).strip() if m else gen.humanize(path.stem)


# ---------------------------------------------------------------------------
# Compact HTML template
# ---------------------------------------------------------------------------


HEADER_TEMPLATE = """\
<div style="width:100%;font-size:8px;color:#57606a;padding:0 10mm;box-sizing:border-box;border-bottom:0.5pt solid #d0d7de;">
  {subject}
</div>
"""

FOOTER_TEMPLATE = """\
<div style="width:100%;font-size:8px;color:#57606a;text-align:center;">
  Page <span class="pageNumber"></span> of <span class="totalPages"></span>
</div>
"""

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>{title}</title>
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/github-markdown-css@5/github-markdown-light.css"
/>
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/highlight.js@11/styles/github.min.css"
/>
<style>
  html, body {{
    margin: 0;
    padding: 0;
    background: #fff;
  }}
  @page {{
    size: A4;
    margin: 12mm 10mm;
  }}
  body.markdown-body {{
    box-sizing: border-box;
    max-width: none;
    margin: 0;
    padding: 0;
    font-size: 10.5px;
    line-height: 1.45;
    color: #1f2328;
  }}
  body.markdown-body h1 {{ font-size: 16px; }}
  body.markdown-body h2 {{ font-size: 14px; }}
  body.markdown-body h3 {{ font-size: 12.5px; }}
  body.markdown-body h4 {{ font-size: 11.5px; }}
  body.markdown-body h5,
  body.markdown-body h6 {{ font-size: 10.5px; }}
  body.markdown-body h1,
  body.markdown-body h2,
  body.markdown-body h3,
  body.markdown-body h4,
  body.markdown-body h5,
  body.markdown-body h6 {{
    page-break-after: avoid;
    break-after: avoid;
  }}
  .cover {{
    text-align: center;
    margin: 48px 0 28px;
  }}
  .cover h1 {{
    font-size: 22px;
    margin: 0 0 6px;
    border: none;
    padding: 0;
  }}
  .cover .meta {{
    color: #57606a;
    font-size: 11px;
  }}
  .toc {{
    font-size: 10px;
    margin-bottom: 16px;
  }}
  .toc .week {{
    font-weight: 700;
    margin-top: 8px;
  }}
  .toc .item a {{
    color: #0969da;
    text-decoration: none;
  }}
  .week-heading {{
    font-size: 13px;
    font-weight: 700;
    color: #24292f;
    border-bottom: 2px solid #0969da;
    padding-bottom: 3px;
    margin: 14px 0 6px;
  }}
  .file-section {{
    margin-bottom: 2px;
  }}
  pre, table, blockquote, .mermaid, mjx-container {{
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  pre {{
    white-space: pre-wrap;
    word-wrap: break-word;
    overflow-wrap: anywhere;
    font-size: 9px;
  }}
  pre.mermaid {{
    background: transparent;
    text-align: center;
  }}
  img {{ max-width: 100%; }}
  table {{ font-size: 9.5px; }}
</style>
<script>
  window.MathJax = {{
    tex: {{
      inlineMath: [["\\\\(", "\\\\)"]],
      displayMath: [["\\\\[", "\\\\]"]],
    }},
    svg: {{ fontCache: "global" }},
    startup: {{ typeset: false }},
  }};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11/lib/common.min.js"></script>
</head>
<body class="markdown-body">
{body}
<script>
  window.__ready = false;
  function waitFor(test, timeoutMs) {{
    return new Promise((resolve, reject) => {{
      if (test()) return resolve();
      const start = Date.now();
      const id = setInterval(() => {{
        if (test()) {{
          clearInterval(id);
          resolve();
        }} else if (Date.now() - start > timeoutMs) {{
          clearInterval(id);
          reject(new Error("timeout waiting for dependency"));
        }}
      }}, 40);
    }});
  }}
  window.addEventListener("load", async () => {{
    try {{
      if (window.hljs) {{
        document
          .querySelectorAll("pre code")
          .forEach((el) => window.hljs.highlightElement(el));
      }}
      await waitFor(() => typeof window.mermaid !== "undefined", 30000);
      window.mermaid.initialize({{
        startOnLoad: false,
        theme: "default",
        securityLevel: "loose",
      }});
      await window.mermaid.run({{ querySelector: "pre.mermaid" }});
      await waitFor(
        () => window.MathJax && typeof window.MathJax.typesetPromise === "function",
        60000
      );
      await window.MathJax.typesetPromise();
    }} catch (err) {{
      window.__error = String(err && err.stack ? err.stack : err);
      console.error(err);
    }} finally {{
      window.__ready = true;
    }}
  }});
</script>
</body>
</html>
"""


def render_subject_html(subject_dir: Path, md: gen.MarkdownIt) -> tuple[str, int]:
    """Return (html_document, num_files_rendered)."""
    notes = collect_notes(subject_dir)
    if not notes:
        return "", 0

    cover_title = gen.humanize(subject_dir.name)
    weeks = sorted({w for w, _ in notes if w is not None})
    parts = [
        '<section class="cover">',
        f"<h1>{html.escape(cover_title)}</h1>",
        f'<div class="meta">{len(notes)} notes across {len(weeks)} week(s)</div>',
        "</section>",
        '<section class="toc"><div class="week">Contents</div>',
    ]

    current_week: int | None = None
    stories_seen = False
    sec = 0
    for week_num, f in notes:
        if week_num is not None:
            if week_num != current_week:
                current_week = week_num
                parts.append(f'<div class="week">Week {week_num}</div>')
                parts.append(f'<h1 class="week-heading">Week {week_num}</h1>')
        else:
            if not stories_seen:
                stories_seen = True
                parts.append('<div class="week">Stories</div>')
                parts.append('<h1 class="week-heading">Stories</h1>')
        title = first_h1(f)
        parts.append(f'<div class="item"><a href="#sec-{sec}">{html.escape(title)}</a></div>')
        rendered = md.render(f.read_text(encoding="utf-8"))
        rel = f.relative_to(subject_dir).as_posix()
        parts.append(
            f'<article class="file-section" id="sec-{sec}" data-source="{html.escape(rel)}">\n'
            f"{rendered}\n</article>"
        )
        sec += 1

    parts.append("</section>")
    document = HTML_TEMPLATE.format(
        title=html.escape(cover_title),
        body="\n".join(parts),
    )
    return document, len(notes)


# ---------------------------------------------------------------------------
# HTML -> PDF (Playwright)
# ---------------------------------------------------------------------------


def html_to_pdf(
    html_path: Path,
    pdf_path: Path,
    subject_label: str,
    timeout_ms: int = 180_000,
) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise SystemExit(
            "playwright is not installed. Run `make notes-pdf-setup` or "
            "`cd scripts && uv sync && uv run playwright install chromium`."
        ) from exc

    try:
        from playwright._impl._errors import Error as PlaywrightError  # type: ignore
    except ImportError:  # pragma: no cover - older playwright
        PlaywrightError = Exception  # type: ignore[assignment,misc]

    url = html_path.resolve().as_uri()
    header = HEADER_TEMPLATE.format(subject=html.escape(subject_label))
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            try:
                page = browser.new_page()
                page.goto(url, wait_until="networkidle", timeout=timeout_ms)
                page.wait_for_function("window.__ready === true", timeout=timeout_ms)
                err = page.evaluate("window.__error || null")
                if err:
                    print(
                        f"[warn] renderer reported error while processing {html_path.name}: {err}",
                        file=sys.stderr,
                    )
                page.emulate_media(media="print")
                pdf_path.parent.mkdir(parents=True, exist_ok=True)
                page.pdf(
                    path=str(pdf_path),
                    format="A4",
                    margin={"top": "12mm", "bottom": "12mm", "left": "10mm", "right": "10mm"},
                    print_background=True,
                    prefer_css_page_size=True,
                    display_header_footer=True,
                    header_template=header,
                    footer_template=FOOTER_TEMPLATE,
                )
            finally:
                browser.close()
    except PlaywrightError as exc:  # type: ignore[misc]
        msg = str(exc)
        if "Executable doesn't exist" in msg or "playwright install" in msg:
            raise SystemExit(
                "Chromium is not installed for Playwright. Run "
                "`make notes-pdf-setup` or "
                "`cd scripts && uv run playwright install chromium`."
            ) from exc
        raise


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def generate_for_subject(subject_dir: Path, md: gen.MarkdownIt, keep_html: bool) -> Path | None:
    doc, n = render_subject_html(subject_dir, md)
    if n == 0:
        print(f"[skip] {subject_dir.name}: no markdown files found")
        return None

    pdf_path = subject_dir / f"{subject_dir.name}.pdf"
    if keep_html:
        html_path = subject_dir / f"{subject_dir.name}.html"
        html_path.write_text(doc, encoding="utf-8")
        print(f"[html] {html_path.relative_to(REPO_ROOT)}")
        html_to_pdf(html_path, pdf_path, gen.humanize(subject_dir.name))
    else:
        with tempfile.TemporaryDirectory(prefix="notes-pdf-") as td:
            html_path = Path(td) / f"{subject_dir.name}.html"
            html_path.write_text(doc, encoding="utf-8")
            html_to_pdf(html_path, pdf_path, gen.humanize(subject_dir.name))

    print(f"[pdf]  {pdf_path.relative_to(REPO_ROOT)}  ({n} files)")
    return pdf_path


def iter_targets(notes_root: Path, selected: Iterable[str] | None) -> list[Path]:
    available = gen.discover_subjects(notes_root)
    if not selected:
        return available

    by_name = {p.name: p for p in available}
    missing = [s for s in selected if s not in by_name]
    if missing:
        raise SystemExit(
            f"Unknown subject(s): {', '.join(missing)}. "
            f"Available: {', '.join(sorted(by_name))}"
        )
    return [by_name[s] for s in selected]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--notes-root",
        type=Path,
        default=DEFAULT_NOTES_ROOT,
        help=f"Root notes directory (default: {DEFAULT_NOTES_ROOT.relative_to(REPO_ROOT)})",
    )
    parser.add_argument(
        "--subject",
        action="append",
        dest="subjects",
        metavar="NAME",
        help="Subject directory name to process. Repeatable. Defaults to all.",
    )
    parser.add_argument(
        "--keep-html",
        action="store_true",
        help="Write the intermediate <subject>.html alongside the PDF for debugging.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    notes_root: Path = args.notes_root.resolve()
    if not notes_root.is_dir():
        raise SystemExit(f"Notes root not found: {notes_root}")

    targets = iter_targets(notes_root, args.subjects)
    if not targets:
        print(f"No subjects found under {notes_root}")
        return 0

    md = gen.build_markdown()
    for subject_dir in targets:
        print(f"==> {subject_dir.name}")
        generate_for_subject(subject_dir, md, keep_html=args.keep_html)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
