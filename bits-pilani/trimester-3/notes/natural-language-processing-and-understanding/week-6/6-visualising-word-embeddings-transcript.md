# Visualizing Word Embeddings

## Intuition: Seeing Semantic Space

Word embeddings live in 50–300 dimensions — impossible to visualize directly. Dimensionality reduction projects these high-dimensional vectors onto a 2D plane, revealing clusters of semantically related words. Seeing `king`, `queen`, `man`, `woman` grouped together makes the abstract concept of embedding space concrete.

---

## Why Visualization Matters

| Without visualization | With visualization |
|----------------------|-------------------|
| Vectors are abstract number arrays | Clusters reveal semantic groups |
| Similarity is a cosine score | Proximity on a plot is intuitive |
| Hard to debug bad embeddings | Outliers and noise become visible |

In ML experimentation (e.g., comparing custom-trained embeddings vs pretrained), 2D plots provide a quick sanity check before deploying to production.

---

## Pipeline Overview

```mermaid
flowchart LR
    W[Word List] --> E[Lookup Embedding Vectors]
    E --> P[PCA to 2D]
    P --> S[Scatter Plot]
```

---

## Step 1: Load Pretrained Model and Select Words

```python
import gensim.downloader as api

glove_model = api.load("glove-twitter-25")

words = [
    "king", "queen", "man", "woman",
    "apple", "orange", "fruit",
    "car", "bus"
]
```

---

## Step 2: Extract Embedding Vectors

```python
vectors = [glove_model[word] for word in words]
```

Each vector has dimension equal to the model's `vector_size` (e.g., 25 for `glove-twitter-25`).

---

## Step 3: Dimensionality Reduction with PCA

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
reduced = pca.fit_transform(vectors)
```

**PCA (Principal Component Analysis)** finds the two directions of maximum variance in the high-dimensional data and projects onto them.

| Method | Speed | Preserves | Best for |
|--------|-------|-----------|----------|
| PCA | Fast | Global variance | Quick exploration |
| t-SNE | Slow | Local neighborhoods | Cluster visualization |
| UMAP | Moderate | Both local and global | Publication-quality plots |

PCA is preferred for quick inspection; t-SNE better reveals tight clusters at the cost of global structure distortion.

---

## Step 4: Scatter Plot

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
plt.scatter(reduced[:, 0], reduced[:, 1])

for i, word in enumerate(words):
    plt.annotate(word, (reduced[i, 0], reduced[i, 1]))

plt.title("Word Embeddings in 2D (PCA)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
```

---

## Expected Cluster Patterns

| Cluster | Words | Why close |
|---------|-------|-----------|
| Royalty/gender | king, queen, man, woman | Shared gender and authority attributes |
| Food | apple, orange, fruit | Culinary co-occurrence |
| Transport | car, bus | Vehicle domain |

Words in the same semantic domain cluster together; unrelated domains occupy different regions of the plot.

---

## Interpreting the Plot

- **Distance ≈ dissimilarity** — but only approximately; PCA loses information
- **Cluster tightness** — reflects consistency of co-occurrence patterns in training data
- **Outliers** — words with unusual usage patterns or polysemy may appear misplaced

---

## Common Pitfalls / Exam Traps

- **Treating 2D distances as exact** — PCA/t-SNE distort high-dimensional relationships; cosine similarity in original space is authoritative.
- **Too few words** — clusters are meaningless with 3–4 words; use 20+ for meaningful patterns.
- **Mixing models** — vectors from different models/dimensions cannot be plotted together.
- **Exam trap: PCA purpose** — reduces $d$-dimensional vectors to 2D for visualization, not for production inference.

---

## Quick Revision Summary

- High-dimensional embeddings (50–300D) require dimensionality reduction for visualization.
- PCA projects vectors to 2D by preserving maximum variance directions.
- Semantic clusters emerge: royalty words together, food words together, transport words together.
- Pipeline: load model → extract vectors → PCA → scatter plot with labels.
- t-SNE is an alternative that better preserves local neighborhoods.
- 2D plots are for exploration; use cosine similarity in original space for production.
