#!/usr/bin/env python3
"""Generate one PDF per subject under bits-pilani/trimester-2/notes.

Concatenates every week-*/*.md note into a single HTML bundle, renders mermaid
diagrams with mermaid.js and LaTeX math with MathJax (mirroring GitHub's
rendering), then prints to PDF via headless Chromium (Playwright).

Usage
-----
First-time setup (once per machine, installs Chromium):

    make notes-pdf-setup
    # or, equivalently:
    cd scripts && uv sync && uv run playwright install chromium

Generate PDFs for every subject (writes to
``<notes-root>/<subject>/<subject>.pdf``):

    make notes-pdf
    # or directly:
    cd scripts && uv run notes-pdf-gen.py

Generate PDFs for one or more specific subjects:

    make notes-pdf ARGS="--subject neural-networks"
    cd scripts && uv run notes-pdf-gen.py --subject cloud-services-and-platforms \\
        --subject machine-learning

Also keep the intermediate HTML alongside the PDF (for debugging):

    cd scripts && uv run notes-pdf-gen.py --subject neural-networks --keep-html

Use a different notes root:

    cd scripts && uv run notes-pdf-gen.py --notes-root /path/to/notes

Flags
-----
    --subject NAME     Subject dir name to process. Repeatable. Defaults to all.
    --notes-root PATH  Root notes directory. Default: bits-pilani/trimester-2/notes.
    --keep-html        Write <subject>.html next to the PDF for debugging.

Requires network access on first run because mermaid.js, MathJax, and
github-markdown-css are loaded from a CDN when Chromium opens the HTML.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import tempfile
from pathlib import Path
from typing import Iterable

from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.deflist import deflist_plugin
from mdit_py_plugins.dollarmath import dollarmath_plugin
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.tasklists import tasklists_plugin

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_NOTES_ROOT = REPO_ROOT / "bits-pilani/trimester-2/notes"
EXCLUDED_DIR_NAMES = {"transcriptions"}
WEEK_DIR_RE = re.compile(r"^week-(\d+)$", re.IGNORECASE)
LEADING_NUM_RE = re.compile(r"^(\d+)")


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------


def discover_subjects(notes_root: Path) -> list[Path]:
    """Return top-level subject directories under `notes_root` (sorted)."""
    return sorted(
        p
        for p in notes_root.iterdir()
        if p.is_dir() and p.name not in EXCLUDED_DIR_NAMES and not p.name.startswith(".")
    )


def _week_sort_key(path: Path) -> tuple[int, str]:
    m = WEEK_DIR_RE.match(path.name)
    return (int(m.group(1)) if m else 10_000, path.name.lower())


def _file_sort_key(path: Path) -> tuple[int, str]:
    m = LEADING_NUM_RE.match(path.name)
    return (int(m.group(1)) if m else 10_000, path.name.lower())


def discover_week_dirs(subject_dir: Path) -> list[Path]:
    return sorted(
        (
            p
            for p in subject_dir.iterdir()
            if p.is_dir() and WEEK_DIR_RE.match(p.name) and p.name not in EXCLUDED_DIR_NAMES
        ),
        key=_week_sort_key,
    )


def discover_md_files(week_dir: Path) -> list[Path]:
    return sorted(
        (p for p in week_dir.glob("*.md") if p.is_file()),
        key=_file_sort_key,
    )


# ---------------------------------------------------------------------------
# Markdown -> HTML
# ---------------------------------------------------------------------------


def build_markdown() -> MarkdownIt:
    md = (
        MarkdownIt("gfm-like", {"html": True, "linkify": True, "typographer": False})
        .enable(["table", "strikethrough", "linkify"])
        .use(front_matter_plugin)
        .use(footnote_plugin)
        .use(deflist_plugin)
        .use(tasklists_plugin, enabled=True)
        .use(anchors_plugin, max_level=6, permalink=False)
        .use(
            dollarmath_plugin,
            allow_labels=True,
            allow_space=True,
            allow_digits=True,
            double_inline=False,
        )
    )

    def render_fence(self, tokens, idx, options, env):  # type: ignore[no-untyped-def]
        tok = tokens[idx]
        info = (tok.info or "").strip().lower()
        content = tok.content
        if info == "mermaid":
            # mermaid.js reads text content of <pre class="mermaid">.
            return f'<pre class="mermaid">{html.escape(content)}</pre>\n'
        if info == "math":
            # MathJax picks up \[...\] for display math.
            return f'<div class="math-display">\\[{content}\\]</div>\n'
        lang_class = f' class="language-{html.escape(info)}"' if info else ""
        return f"<pre><code{lang_class}>{html.escape(content)}</code></pre>\n"

    md.add_render_rule("fence", render_fence)
    return md


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------


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
  body.markdown-body {{
    box-sizing: border-box;
    max-width: 960px;
    margin: 0 auto;
    padding: 24px 28px;
    font-size: 13.5px;
    line-height: 1.55;
  }}
  /* Start each top-level file on a fresh page */
  .file-section {{
    page-break-before: always;
    break-before: page;
  }}
  .file-section:first-of-type,
  .subject-title {{
    page-break-before: auto;
    break-before: auto;
  }}
  .subject-title {{
    text-align: center;
    padding: 40px 0 24px;
    border-bottom: 1px solid #d0d7de;
    margin-bottom: 24px;
  }}
  .subject-title h1 {{
    font-size: 32px;
    margin: 0 0 8px;
    border: none;
    padding: 0;
  }}
  .subject-title .meta {{
    color: #57606a;
    font-size: 13px;
  }}
  /* Prevent code blocks and diagrams from being cut across pages */
  pre, .mermaid, table, blockquote, mjx-container[display="true"] {{
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  pre {{
    white-space: pre-wrap;
    word-wrap: break-word;
    overflow-wrap: anywhere;
  }}
  pre.mermaid {{
    background: transparent;
    text-align: center;
  }}
  img {{ max-width: 100%; }}
  @page {{
    size: A4;
    margin: 18mm 14mm;
  }}
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
<section class="subject-title">
  <h1>{heading}</h1>
  <div class="meta">{meta}</div>
</section>
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


def humanize(name: str) -> str:
    return name.replace("-", " ").replace("_", " ").strip().title()


def render_subject_html(
    subject_dir: Path,
    md: MarkdownIt,
) -> tuple[str, int]:
    """Return (html_document, num_files_rendered)."""
    week_dirs = discover_week_dirs(subject_dir)
    body_parts: list[str] = []
    file_count = 0

    for week_dir in week_dirs:
        md_files = discover_md_files(week_dir)
        if not md_files:
            continue
        body_parts.append(
            f'<section class="week-section"><h1 class="week-heading">{html.escape(humanize(week_dir.name))}</h1></section>'
        )
        for md_file in md_files:
            raw = md_file.read_text(encoding="utf-8")
            rendered = md.render(raw)
            rel = md_file.relative_to(subject_dir)
            body_parts.append(
                f'<article class="file-section" data-source="{html.escape(str(rel))}">\n{rendered}\n</article>'
            )
            file_count += 1

    subject_label = humanize(subject_dir.name)
    document = HTML_TEMPLATE.format(
        title=html.escape(subject_label),
        heading=html.escape(subject_label),
        meta=html.escape(f"{file_count} notes across {len(week_dirs)} week(s)"),
        body="\n".join(body_parts),
    )
    return document, file_count


# ---------------------------------------------------------------------------
# HTML -> PDF (Playwright)
# ---------------------------------------------------------------------------


def html_to_pdf(html_path: Path, pdf_path: Path, timeout_ms: int = 180_000) -> None:
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
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            try:
                context = browser.new_context()
                page = context.new_page()
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
                    margin={"top": "18mm", "bottom": "18mm", "left": "14mm", "right": "14mm"},
                    print_background=True,
                    prefer_css_page_size=True,
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


def generate_for_subject(
    subject_dir: Path,
    md: MarkdownIt,
    keep_html: bool,
) -> Path | None:
    doc, n = render_subject_html(subject_dir, md)
    if n == 0:
        print(f"[skip] {subject_dir.name}: no markdown files found")
        return None

    pdf_path = subject_dir / f"{subject_dir.name}.pdf"

    if keep_html:
        html_path = subject_dir / f"{subject_dir.name}.html"
        html_path.write_text(doc, encoding="utf-8")
        print(f"[html] {html_path.relative_to(REPO_ROOT)}")
        html_to_pdf(html_path, pdf_path)
    else:
        with tempfile.TemporaryDirectory(prefix="notes-pdf-") as td:
            html_path = Path(td) / f"{subject_dir.name}.html"
            html_path.write_text(doc, encoding="utf-8")
            html_to_pdf(html_path, pdf_path)

    print(f"[pdf]  {pdf_path.relative_to(REPO_ROOT)}  ({n} files)")
    return pdf_path


def iter_targets(notes_root: Path, selected: Iterable[str] | None) -> list[Path]:
    available = discover_subjects(notes_root)
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

    md = build_markdown()
    for subject_dir in targets:
        print(f"==> {subject_dir.name}")
        generate_for_subject(subject_dir, md, keep_html=args.keep_html)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
