# Retrieval quality

Bi-encoder similarity is fast but approximate. Production RAG often stacks techniques.

## Hybrid retrieval

Combine **lexical** (BM25, splade-style sparse) with **dense** vectors. **Reciprocal Rank Fusion (RRF)** merges ranked lists without calibrating scores to a common scale.

## Reranking

Run a **cross-encoder** (query + document jointly encoded) on the top 50–200 candidates; keep top 5–10 for the LLM. Adds latency but sharply improves precision.

## Metadata filters

Filter by tenant, product, date, or ACL **before** or **after** vector search. Pre-filtering is efficient but can miss relevant docs if filters are too strict.

## Query transformation

- Hypothetical document embeddings (HyDE) — generate a fake answer, embed it, retrieve.
- Multi-query — paraphrase the user question and union results.

Use sparingly; each variant adds embedding calls.
