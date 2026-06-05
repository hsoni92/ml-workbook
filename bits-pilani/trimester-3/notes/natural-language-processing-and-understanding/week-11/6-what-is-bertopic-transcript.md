# BERTopic: Semantic Topic Modelling

## The Problem BERTopic Solves

Classical LDA models word co-occurrence in a bag-of-words space. It cannot recognise that *"cloud computing"* and *"AWS infrastructure"* belong to the same theme unless those exact words co-occur frequently. BERTopic addresses this by operating in **semantic embedding space** rather than raw word-count space.

---

## What Is BERTopic?

BERTopic is a modern topic modelling technique that:

1. Uses a **transformer model** (typically BERT-based) to create dense sentence/document embeddings
2. **Clusters** documents by semantic similarity in embedding space
3. **Extracts** interpretable topic words from each cluster using classical NLP techniques

The name reflects its foundation: **BERT** embeddings + **topic** discovery.

### Key Idea

Instead of modelling word distributions directly (as LDA does), BERTopic:

- Groups **semantically similar documents** together
- Derives topic labels from the words most characteristic of each cluster

```mermaid
flowchart LR
    A[Documents] --> B[BERT Embeddings]
    B --> C[Cluster by Semantic Similarity]
    C --> D[Extract Topic Words per Cluster]
    D --> E[Named Topics]
```

---

## How BERTopic Differs from LDA

| Aspect | LDA | BERTopic |
|--------|-----|----------|
| Representation | Bag of words | Dense embeddings |
| Semantics | Co-occurrence only | Contextual meaning |
| Word order | Ignored | Captured in embeddings |
| Short text | Poor | Better (embedding quality helps) |
| Topic words | Global word distributions | Per-cluster TF-IDF |
| Topic count | Manual $K$ | Clustering algorithm determines groups |

---

## Why It Works in Practice

Consider a corpus of ML platform reviews mentioning *"SageMaker"*, *"model deployment"*, *"inference latency"*, and *"endpoint scaling"*. LDA might split these across topics based on word frequency alone. BERTopic groups the reviews semantically because the embeddings capture that these phrases describe the same operational concern — model serving infrastructure.

---

## When to Use BERTopic

- Customer feedback analysis where paraphrasing is common
- Research paper clustering with varied terminology
- Any corpus where **meaning** matters more than **exact word overlap**
- Situations where LDA produces overlapping or incoherent topics

---

## Common Pitfalls / Exam Traps

- **Saying BERTopic is "just LDA with BERT"** — the architecture is fundamentally different: embed → reduce → cluster → c-TF-IDF.
- **Expecting BERTopic to need no classical NLP** — it still uses TF-IDF (c-TF-IDF) for interpretable topic words.
- **Forgetting the embedding model dependency** — topic quality depends on the chosen sentence transformer.
- **Confusing BERTopic with BERT fine-tuning** — BERTopic uses pretrained embeddings for clustering; it does not fine-tune BERT for classification.

---

## Quick Revision Summary

- BERTopic uses transformer embeddings to capture semantic document similarity.
- Documents are clustered in embedding space, not bag-of-words space.
- Topic words are extracted per cluster using a TF-IDF variant (c-TF-IDF).
- It addresses LDA's lack of context, semantics, and poor short-text handling.
- The pipeline: embed → dimensionality reduction → cluster → topic representation.
- Best for corpora where meaning and paraphrase variation matter.
