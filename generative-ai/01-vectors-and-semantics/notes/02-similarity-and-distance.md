# Similarity and distance

Retrieval quality depends on how you compare vectors. The embedding model and the index must agree on geometry.

## Common metrics

For vectors $a, b \in \mathbb{R}^d$:

**Cosine similarity** (direction, scale-invariant after normalization):

$$\text{cos}(a, b) = \frac{a \cdot b}{\|a\|_2 \, \|b\|_2}$$

**Euclidean distance** ($L_2$):

$$\|a - b\|_2 = \sqrt{\sum_{i=1}^{d} (a_i - b_i)^2}$$

**Inner product** (dot product):

$$a \cdot b = \sum_{i=1}^{d} a_i b_i$$

If all vectors are **unit-normalized**, ranking by cosine similarity is equivalent to ranking by dot product. Many APIs expose "cosine" or "dot" modes; pick one and keep encoders and queries consistent.

## When to use which

| Metric | Favors | Watch out |
| :--- | :--- | :--- |
| Cosine | Semantic direction, text embeddings | Vectors must be comparable scale across corpus |
| Dot product | Some bi-encoder training setups | Magnitude can dominate if not normalized |
| $L_2$ | Spatial clustering, some classical ML | Sensitive to scale; often used after PCA for viz only |

## Normalization checklist

1. Apply the **same** preprocessing at index and query time (same model, same pooling, same truncation).
2. If the provider returns unnormalized vectors, document whether you L2-normalize before insert.
3. Re-rank with a **cross-encoder** when bi-encoder similarity is noisy (covered in the RAG module).

## Visualization vs retrieval

PCA or UMAP projections are for **human inspection** only. Do not use 2D distances for production retrieval; always search in the original $d$-dimensional space (or in the index's quantized form).
