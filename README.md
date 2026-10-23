# ML Workbook: Academic Coursework and Modern Generative AI Engineering

An open-source machine learning curriculum, study repository, and engineering workbook for students, practitioners, and ML aspirants.

This repository combines:

1. **BITS Pilani coursework**: Week-by-week lecture notes, mind maps, sample papers, and PDFs across machine learning, deep learning, NLP, big data, and MLOps.
2. **Modern generative AI curriculum**: Study notes on vector semantics, transformer internals, System 1 vs System 2 models, RAG, ontologies, GraphRAG, and agentic workflows.

---

## Modern generative AI track

Structured modules with theory (Markdown, MathJax, Mermaid). Start at the [Generative AI curriculum index](generative-ai/README.md).

| Module | Topics |
| :--- | :--- |
| [01. Vectors and semantics](generative-ai/01-vectors-and-semantics/README.md) | Embeddings, distance metrics, ANN indexing, quantization |
| [02. Transformers architecture](generative-ai/02-transformers-architecture/README.md) | Attention, KV cache, positional encodings, MoE |
| [03. System 1 vs System 2 models](generative-ai/03-system1-vs-system2-models/README.md) | Fast decoding vs test-time compute, CoT, PRM/ORM |
| [04. RAG systems](generative-ai/04-rag-systems/README.md) | Chunking, hybrid retrieval, reranking |
| [05. Ontologies and knowledge graphs](generative-ai/05-ontologies-and-kg/README.md) | Taxonomies, RDF/LPG, entity resolution |
| [06. GraphRAG](generative-ai/06-graph-rag/README.md) | Graph construction, community summaries, hybrid retrieval |
| [07. Agents and protocols](generative-ai/07-agents-and-protocols/README.md) | Tool use, LangGraph, MCP |

---

## BITS Pilani coursework

Public study notes, mind maps, and practice papers by trimester. Graded assignments under `bits-pilani/` are stored as encrypted `*.enc` files (see [Secure vault](#secure-vault-secureyaml) below).

### Trimester 3

- [Notes overview](bits-pilani/trimester-3/notes/README.md)
- [Machine learning model engineering](bits-pilani/trimester-3/notes/machine-learning-model-engineering/README.md) — [mind map](bits-pilani/trimester-3/notes/machine-learning-model-engineering/mind-map.md), [PDF](bits-pilani/trimester-3/notes/machine-learning-model-engineering/machine-learning-model-engineering.pdf), [exam-ready PDF](bits-pilani/trimester-3/notes/machine-learning-model-engineering-exam-ready-notes.pdf)
- [Natural language processing and understanding](bits-pilani/trimester-3/notes/natural-language-processing-and-understanding/README.md) — [mind map](bits-pilani/trimester-3/notes/natural-language-processing-and-understanding/mind-map.md), [PDF](bits-pilani/trimester-3/notes/natural-language-processing-and-understanding/natural-language-processing-and-understanding.pdf), [exam-ready PDF](bits-pilani/trimester-3/notes/natural-language-processing-and-understanding-exam-ready-notes.pdf)
- [Big data platforms and analytics](bits-pilani/trimester-3/notes/big-data-platforms-and-analytics/README.md) — [mind map](bits-pilani/trimester-3/notes/big-data-platforms-and-analytics/mind-map.md), [PDF](bits-pilani/trimester-3/notes/big-data-platforms-and-analytics/big-data-platforms-and-analytics.pdf), [exam-ready PDF](bits-pilani/trimester-3/notes/big-data-platforms-and-analytics-exam-ready-notes.pdf)
- [Principles of marketing](bits-pilani/trimester-3/notes/principle-of-marketing/README.md) — [mind map](bits-pilani/trimester-3/notes/principle-of-marketing/mind-map.md), [PDF](bits-pilani/trimester-3/notes/principle-of-marketing/principle-of-marketing.pdf), [exam-ready PDF](bits-pilani/trimester-3/notes/principle-of-marketing-exam-ready-notes.pdf)

### Trimester 2

- [Machine learning](bits-pilani/trimester-2/notes/machine-learning/index.md) — [stories](bits-pilani/trimester-2/notes/machine-learning/stories/Story-Based-Learning.md), [PDF](bits-pilani/trimester-2/notes/machine-learning/machine-learning.pdf), [numerical bank](bits-pilani/trimester-2/notes/machine-learning/ml_numerical_question_bank_exam_style_solved.pdf), [practice papers](bits-pilani/trimester-2/notes/machine-learning/ml_slot2_12_practice_papers_with_answers.pdf)
- [Neural networks](bits-pilani/trimester-2/notes/neural-networks/index.md) — [NN training](bits-pilani/trimester-2/notes/neural-networks/NN-Training.md), [stories](bits-pilani/trimester-2/notes/neural-networks/stories/Story-Based-Learning.md), [PDF](bits-pilani/trimester-2/notes/neural-networks/neural-networks.pdf)
- [Cloud services and platforms](bits-pilani/trimester-2/notes/cloud-services-and-platforms/index.md) — [revision](bits-pilani/trimester-2/notes/cloud-services-and-platforms/REVISION.md), [PDF](bits-pilani/trimester-2/notes/cloud-services-and-platforms/cloud-services-and-platforms.pdf)

### Trimester 1

- [Notes and practice papers](bits-pilani/trimester-1/notes) (PDFs for DPP, DSP, DVS, feature engineering, statistical modeling, and related subjects)

---

## Repository tooling

### Pre-commit

To run checks on every commit:

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. From the repository root:

   ```bash
   make setup
   ```

This installs project dependencies with `uv sync`, installs `pre-commit`, configures the Git hook, and installs Mermaid validation dependencies.

Useful commands:

- `make precommit-install` — (re)install the Git hook
- `make precommit-run` — run all hooks on all files
- `make mermaid-validate` — validate Mermaid diagrams in Markdown
- `make notes-pdf-setup` — install Chromium for PDF generation
- `make notes-pdf` / `make notes-pdf-t3` — compile trimester notes to PDF
- `python3 scripts/number-notes.py [NOTES_DIR]` — index trimester notes and add Previous / Index / Next footers (default: trimester-3 notes)

Every `make` target checks that `uv` is installed before running.

### Secure vault (`secure.yaml`)

Paths listed in [secure.yaml](secure.yaml) are encrypted with Fernet when you run `encrypt` locally. Each **regular file** under a configured path becomes **`filename.enc`** next to where the plaintext was (the original basename, including any extension, stays visible before `.enc`). Symlinks are skipped. Anything **Git ignores** (same rules as `git check-ignore`, including nested `.gitignore` files) is not encrypted.

**Safety / data-loss:** ciphertext is written with a same-directory temp file and `os.replace`, so you should not get a truncated `.enc` from a crash mid-write. Decrypt strips one `.enc` layer per run. Overwriting an existing `.enc` emits a warning. Very large single files must fit in one Fernet payload (no sharding).

Provide a Fernet key via `SECURE_VAULT_KEY` in the environment, or in repo-root `.env` as `SECURE_VAULT_KEY=...`, or on the first line of `.secure_key` (both gitignored). Generate a key:

```bash
python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())'
```

Encrypt or strip one encryption layer locally. With [uv](https://docs.astral.sh/uv/), run the script from `scripts/` so dependencies resolve correctly (do not use `uvx python`, which does not add `pyyaml` / `cryptography`):

```bash
make encrypt
make decrypt
```

If those packages are already on your `python`, plain `python scripts/secure_vault.py …` is fine.

**Pre-commit and Git index:** the hook checks that the working tree under secured paths has no remaining plaintext (same rules as `encrypt`), then verifies the index. Under secured paths you may only stage **`.enc`** files (except paths in `allow_staged_non_enc`). Run `encrypt` and `git add` the `.enc` paths (and drop plaintext from the index) before committing.

**Legacy `.vault`:** older versions stored whole directories as a single `dirname.vault` blob. That format is no longer supported. Decrypt any existing `.vault` with the script version that created it (for example from git history) before relying on the current flow.
