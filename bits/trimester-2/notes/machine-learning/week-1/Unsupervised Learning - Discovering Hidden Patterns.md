# Unsupervised Learning – Discovering Hidden Patterns – Machine Learning (Module 1)

## Learning Objectives

By the end of this video you will:

1. **Define** unsupervised learning and how it differs from supervised learning.
2. **Describe** two main types: **clustering** and **association rule mining**.
3. **Explain** the goal of clustering (homogeneous groups) and association rules (item relationships).
4. **Give** real-world applications of both.

---

## Supervised vs Unsupervised (Quick Recap)

| | Supervised | Unsupervised |
|--|------------|--------------|
| **Data** | X **and** Y (labels) | **Only X** (no labels) |
| **Goal** | **Prediction** (of Y) | **Discovery** of structure, patterns, relationships |
| **Also known as** | Prediction methods | Descriptive methods / knowledge discovery |

In unsupervised learning we **do not predict** a target; we **explore** the data to find **hidden structure and patterns**.

---

## Two Primary Types of Unsupervised Learning

### 1. Clustering

- **Goal:** Automatically **group similar** data points together; put **dissimilar** points in different groups.
- **No labels:** We only have **X**. The algorithm finds “natural” groups (e.g. by language, by topic, by behaviour).
- **Idea:** Minimize **intra-cluster distance** (points in same group are close) and maximize **inter-cluster distance** (different groups are far). Equivalently: maximize similarity within a group, minimize similarity across groups.
- **Similarity** can be defined in many ways (e.g. language, height, features); the choice defines what “similar” means.

**Example – Indian states (historical):**  
States were formed so that “similar” people (e.g. same language) are in one state and “dissimilar” (different language) in different states. Same idea as clustering: group by a notion of similarity (e.g. language).

**Applications:**

- **Google News:** Cluster news articles by **topic** (sports, finance, national, etc.).
- **Stock / market analysis:** Group companies (e.g. oil, tech, defence) that behave similarly.
- **Market segmentation:** Divide customers into segments for targeted marketing (e.g. high-income vs low-income for product launch).

### 2. Association Rule Mining

- **Goal:** Find **relationships / rules** between variables (e.g. “if item A is bought, then item B is often bought”).
- **Focus:** Co-occurrence, dependency rules: “occurrence of one item predicts occurrence of another.”
- **Example:** “If **samosa** is bought → **Coca-Cola** is often bought.” Used for shelf placement, inventory, recommendations.

**Applications:**

- **Market basket / supermarket:** Products bought together → place them together; inventory and layout.
- **Recommendations:** “Customers who bought X also bought Y.”

---

## Clustering in More Detail

- **Input:** Set of data points (only **X**), no class labels.
- **Output:** Groups (clusters) such that:
  - Points in the **same** cluster are **similar**.
  - Points in **different** clusters are **dissimilar**.
- **Pure/homogeneous cluster:** Ideally (or approximately) all points in one cluster belong to one “type”; then we can interpret or label the cluster.
- **Impure/heterogeneous:** Mix of types; may need further splitting or a different number of clusters.

---

## Summary Table

| Unsupervised type | Goal | Example |
|-------------------|------|---------|
| **Clustering** | Find **natural groups**; similar together, dissimilar apart | News by topic, customer segments, states by language |
| **Association rule mining** | Find **rules** like “if A then B” (frequent itemsets, dependencies) | Market basket, shelf layout, recommendations |

---

## Exam-Oriented Points

- Unsupervised = **no Y**; goal = **patterns/structure**, not prediction.
- **Clustering** = grouping by similarity; minimize within-group distance, maximize between-group.
- **Association rule mining** = dependency rules between items (e.g. purchase A → purchase B).
- Applications: document clustering, market segmentation, market basket, recommendations.

Use this note for definitions, difference from supervised learning, and application examples.
