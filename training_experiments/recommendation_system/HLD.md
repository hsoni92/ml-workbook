# High-Level Design: Two-Tower Recommendation System

## 1. Overview

A **two-tower** model learns separate embeddings for **users** and **items**. At inference, user and item embeddings are computed independently; relevance is the dot product (or cosine similarity) of the two vectors. This allows precomputing item embeddings and serving recommendations via fast approximate nearest-neighbor (ANN) search.

```
┌─────────────────┐                    ┌─────────────────┐
│   User Tower    │                    │   Item Tower    │
│  (user features │   dot product      │ (item features  │
│   → embedding)  │ ────────────────►  │  → embedding)  │
└─────────────────┘      score        └─────────────────┘
```

**Why two-tower:** Scalable retrieval. Item tower runs offline to build an index; user tower runs online once per request. No need to score every item against the user in real time.

---

## 2. Components

| Component        | Role |
|-----------------|------|
| **User Tower**  | Maps user ID + user context (e.g. device, time) → fixed-size user embedding. |
| **Item Tower**  | Maps item ID + item attributes (e.g. category, title) → same-size item embedding. |
| **Scoring**     | `score(user, item) = user_embed · item_embed` (or cosine). Trained with contrastive / softmax loss. |

Shared constraint: **both towers output the same embedding dimension** (e.g. 64 or 128).

---

## 3. Data Flow

### 3.1 Training

- **Input:** Logs of (user_id, item_id, context). Positive = user interacted (click/watch/like); negatives = random or in-batch negatives.
- **Flow:** For each batch, pass user side through user tower → user embeddings; item side through item tower → item embeddings. Compute similarity matrix (e.g. logits = user_emb @ item_emb.T), apply cross-entropy / contrastive loss, backprop.

### 3.2 Serving (retrieval)

1. **Offline:** Run all items through the item tower; write embeddings to an ANN index (e.g. FAISS, ScaNN, or vector DB).
2. **Online:** For a request, run user features through the user tower once → user embedding. Query the ANN index with this embedding → top-K item IDs. Optionally rerank (e.g. with a separate model or business rules).

```
Request → User Tower → user_embed → ANN lookup → top-K item IDs → response
```

---

## 4. Project Layout (prod-style, no notebooks)

Keep scripts small and single-purpose. No Jupyter; everything runnable from CLI or a job runner.

```
recommendation_system/
├── HLD.md
├── config/
│   └── config.yaml              # embedding_dim, tower hidden dims, paths, etc.
├── src/
│   ├── __init__.py
│   ├── model.py                 # Two-tower (user + item) model definition
│   ├── dataset.py              # PyTorch/TF dataset: (user_features, item_features, label)
│   ├── train.py                # Training loop: load data, model, train, save checkpoint
│   ├── embed.py                # Scripts: embed all items OR embed one user (for serving)
│   └── evaluate.py             # Offline metrics: recall@K, MRR, NDCG on holdout set
├── scripts/
│   ├── run_train.sh            # Invoke train.py with config
│   ├── run_build_index.sh      # Run embed.py for all items, build ANN index
│   └── run_eval.sh             # Run evaluate.py
├── requirements.txt
└── README.md
```

- **config.yaml:** Single place for embedding dim, hidden layers, data paths, batch size, epochs.
- **model.py:** User tower and item tower (e.g. MLPs or small transformers); output same dim.
- **dataset.py:** Loads positive pairs + samples negatives (random or in-batch); yields (user_features, item_features, label).
- **train.py:** Standard loop: dataset → model → loss (e.g. cross-entropy over in-batch negatives) → optimizer → save best checkpoint.
- **embed.py:** Two modes: (1) batch over all items, write item embeddings; (2) given user features, return user embedding (for serving).
- **evaluate.py:** Load model, compute user and item embeddings for test set, compute recall@K / MRR / NDCG.

No notebooks; all entrypoints are scripts (e.g. `python -m src.train --config config/config.yaml`).

---

## 5. Training Objective (simple and effective)

- **In-batch negatives:** For a batch of B (user, item) pairs, treat the B user embeddings and B item embeddings as a B×B similarity matrix. Diagonal = positives; rest = negatives. Cross-entropy loss over each row (or each column) is simple and effective.
- **Optional:** Add random negatives per example if batch size is small.

Formula (conceptually): for each user in batch, softmax over scores with all items in batch; maximize score of the positive item.

---

## 6. Technology Choices (minimal)

| Concern        | Option |
|----------------|--------|
| Framework     | PyTorch or TensorFlow; pick one and stick to it. |
| Config        | YAML + simple parser (e.g. PyYAML). |
| ANN index     | FAISS (local) or a vector DB (e.g. Milvus, Pinecone) for distributed serving. |
| Checkpoints   | Save model weights + config used; version with run ID or timestamp. |

---

## 7. Out of Scope for This HLD

- Feature store and real-time feature computation (assume features are in the dataset or precomputed).
- A/B testing and experiment tracking (can be added later).
- Reranker model (optional second stage; not in this HLD).
- Distributed training (single-node training is enough to start).

---

## 8. Success Criteria

- **Offline:** Recall@K and NDCG improve over a simple baseline (e.g. random or popularity).
- **Online:** Latency of user embedding + ANN query within SLA (e.g. p99 < 50 ms for retrieval).
- **Simplicity:** One config, one train script, one embed script, one eval script; no notebooks in the critical path.
