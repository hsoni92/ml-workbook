# Implementing Bag of Words with scikit-learn

## Intuition: Automating the Counting Pipeline

Manual BoW implementation mirrors one-hot encoding but increments counters instead of flipping bits. In production, `CountVectorizer` from scikit-learn handles tokenization, vocabulary building, counting, and sparse matrix storage in a single `fit_transform` call.

---

## Pipeline Overview

```mermaid
flowchart LR
    C[Corpus] --> CV[CountVectorizer]
    CV --> F[fit_transform]
    F --> S[Sparse Matrix 3 x 12]
    S --> A[Convert to Dense Array]
    A --> DF[Pandas DataFrame]
```

---

## Step 1: Import and Prepare Corpus

```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "The cat sat on the mat",
    "The dog sat on the log",
    "Cats and dogs are enemies"
]
```

---

## Step 2: Fit and Transform

```python
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
```

`fit_transform` performs two operations:
- **fit** — learns the vocabulary from the corpus
- **transform** — converts each document to a count vector

**Output shape:** `(3, 12)` — 3 documents, 12 unique tokens in vocabulary.

The result is a **compressed sparse row (CSR) matrix** — efficient storage when most values are zero.

---

## Step 3: Inspect the Matrix

```python
import numpy as np
X.toarray()
```

**BoW vector for "The cat sat on the mat":**

| Word | Count |
|------|-------|
| cat | 1 |
| mat | 1 |
| on | 1 |
| sat | 1 |
| the | 2 |

The word `the` appears twice — the distinguishing feature of BoW over one-hot encoding.

```python
import pandas as pd

df = pd.DataFrame(
    X.toarray(),
    columns=vectorizer.get_feature_names_out(),
    index=corpus
)
```

---

## Key CountVectorizer Parameters

| Parameter | Default | Effect |
|-----------|---------|--------|
| `binary` | `False` | Set `True` for one-hot-style presence only |
| `lowercase` | `True` | Converts all tokens to lowercase |
| `stop_words` | `None` | Remove common words (`'english'` available) |
| `ngram_range` | `(1, 1)` | Use `(1, 2)` for unigrams + bigrams |
| `max_features` | `None` | Limit vocabulary to top-N frequent terms |
| `min_df` / `max_df` | `1` / `1.0` | Filter rare or overly common terms |

For a document classification API on Azure ML, `max_features=10000` and `min_df=2` are common starting points to control dimensionality.

---

## Sparse vs Dense Storage

| Format | When to Use |
|--------|-------------|
| CSR sparse matrix | Default; efficient for high-dimensional text |
| Dense array (`.toarray()`) | Debugging, small vocabularies, visualization |
| DataFrame | Human-readable inspection |

A `(10000, 50000)$ sparse matrix may store only millions of non-zero entries instead of 500 million floats.

---

## Common Pitfalls / Exam Traps

- **Forgetting `fit` before `transform` on new data** — vocabulary must be learned on training data only; applying a test corpus to `fit_transform` leaks future vocabulary.
- **Not lowercasing consistently** — `CountVectorizer` lowercases by default; custom preprocessing that preserves case creates mismatches.
- **Confusing `binary=True` with BoW** — `binary=True` produces one-hot-style vectors, not frequency counts.
- **Exam trap: output dtype** — BoW produces integers; TF-IDF produces floats.

---

## Quick Revision Summary

- `CountVectorizer` from scikit-learn implements BoW via `fit_transform`.
- Output is a sparse matrix: rows = documents, columns = vocabulary, values = word counts.
- `the` appearing twice in a sentence yields count 2, not 1.
- Convert to DataFrame with `get_feature_names_out()` for readable inspection.
- Key parameters: `binary`, `stop_words`, `ngram_range`, `max_features`, `min_df`.
- Always fit on training data only; transform test data with the learned vocabulary.
