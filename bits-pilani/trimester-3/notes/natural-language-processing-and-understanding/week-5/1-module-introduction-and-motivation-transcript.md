# Traditional Word Embeddings: Module Overview

## Why Machines Need Numbers, Not Text

Natural language processing models are mathematical engines. They operate on tensors of floating-point values — not on characters, sentences, or meaning in the human sense. Before any classifier, clustering algorithm, or neural network can process text, that text must be converted into a numerical representation. This conversion is called **vectorization** or **word embedding**.

Consider a cloud-based spam filter at scale: millions of emails arrive per hour. The pipeline cannot "read" each message; it must transform subject lines and body text into feature vectors that a logistic regression model or gradient-boosted tree can score in milliseconds.

```mermaid
flowchart LR
    T[Raw Text] --> V[Vectorization]
    V --> ML[ML Algorithm]
    ML --> P[Prediction / Score]
```

---

## The Evolution of Text Representation

Text processing in NLP has progressed through distinct eras:

| Era | Approach | Example Techniques |
|-----|----------|-------------------|
| Rule-based | Hand-crafted linguistic rules | Regex patterns, stemming, lemmatization |
| Statistical | Count-based numerical features | One-hot encoding, BoW, TF-IDF, n-grams |
| Dense semantic | Learned continuous vectors | Word2Vec, GloVe, contextual embeddings |

Earlier modules covered **preprocessing** — cleaning and normalizing text. This module enters **statistical NLP**, where words become vectors and mathematical operations (dot products, cosine similarity, matrix multiplication) become meaningful.

---

## Core Techniques Covered

This module introduces four foundational vectorization methods:

- **One-hot encoding (OHE)** — each word is an isolated category; presence/absence only
- **Bag of Words (BoW)** — word frequencies within a document; order discarded
- **TF-IDF** — frequency weighted by rarity across the corpus; downweights common words
- **N-grams** — contiguous token sequences that partially recover word order

Each technique trades off between **sparsity** (memory efficiency vs. wasted zeros) and **semantic retention** (whether related words appear mathematically similar).

---

## The Central Trade-off

| Dimension | Sparse methods (OHE, BoW, TF-IDF) | Dense methods (Word2Vec, GloVe) |
|-----------|----------------------------------|----------------------------------|
| Vector size | Vocabulary size (10,000+) | Fixed small dimension (50–300) |
| Semantic similarity | None — all words orthogonal | Captured — similar words cluster |
| Interpretability | High — each dimension is a word | Low — dimensions are latent features |
| Compute cost | Low for small vocab | Higher training cost |

Understanding these trade-offs is essential before moving to dense embeddings in the next module.

---

## Common Pitfalls / Exam Traps

- **Confusing vectorization with preprocessing** — stemming and stopword removal clean text; vectorization converts cleaned text to numbers. They are sequential steps, not the same operation.
- **Assuming "embedding" always means dense vectors** — one-hot encoding and BoW are also called word embeddings in the broad sense, but they are sparse and non-semantic.
- **Ignoring the vocabulary problem** — every vectorization method requires building a vocabulary from the training corpus. Words unseen at test time are typically dropped or mapped to an unknown token.
- **Treating all vectorization methods as interchangeable** — TF-IDF suits document classification; one-hot suits small categorical vocabularies; neither captures that "car" and "automobile" are synonyms.

---

## Quick Revision Summary

- NLP models require numerical input; vectorization bridges human language and machine computation.
- Statistical NLP converts words to vectors so mathematical operations can be applied.
- One-hot encoding, BoW, TF-IDF, and n-grams are the foundational sparse techniques.
- The core trade-off is sparsity (memory, dimensionality) versus semantic retention.
- Rule-based preprocessing precedes vectorization; they solve different problems.
- Dense embeddings (next module) address the semantic gap that sparse methods leave open.
- Real-world pipelines (spam filters, search ranking, document classifiers) depend on choosing the right representation for the task.
