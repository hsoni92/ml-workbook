# Machine Learning — Detailed Revision for Recollection

## How to use this sheet

- Read one section and then pause for 30 seconds to recall it without looking.
- Focus on the sequence: **what it is -> why it matters -> when to use -> common confusion**.
- Use formulas as memory anchors, not as full derivations.
- At the end of each section, answer the self-check prompts out loud.

---

## 1) Foundations and workflow (Weeks 1-2)

### What it is

Machine Learning is a way to learn patterns from data when writing all rules manually is difficult or impossible.

- **Supervised learning**: data has labels; model learns input-output mapping.
- **Unsupervised learning**: data has no labels; model finds hidden structure (clusters, associations).
- **Classification vs regression**: classification predicts a category, regression predicts a number.

### Why it matters

Raw data by itself does not give decisions. ML converts large data into usable predictions or insights.

### Workflow to remember

- **KDD view**: collect data -> clean/integrate -> select relevant subset -> mine/model -> evaluate -> knowledge.
- **CRISP-DM view**: business understanding -> data preparation -> modeling -> evaluation -> deployment.
- These are not competing frameworks; both describe iterative ML project lifecycles.

### Common confusion

- Confusing AI, ML, and data science: ML is one major technical part inside broader AI/data science ecosystems.
- Thinking “run algorithm once and done”: real ML is iterative and loops back after evaluation.

### Self-check

- Can you explain classification vs regression with one example each?
- Why is preprocessing done before model training?

---

## 2) Data preprocessing and data quality (Week 2)

### What it is

Preprocessing improves data quality and representation before training.

- **Cleaning**: missing values, noise, outliers, inconsistent entries.
- **Integration**: combine sources and resolve entity/value conflicts.
- **Transformation**: normalization, aggregation, representation changes.
- **Reduction**: fewer rows/features while preserving information.

### Why it matters

Model quality is bounded by data quality. Poor input creates unstable or misleading models.

### When to use what

- Use normalization for distance-based methods (`kNN`, `k-means`) and gradient-based optimization.
- Use reduction when computation is heavy but data redundancy is high.
- Use careful integration when merging multi-source enterprise data.

### Common confusion

- Cleaning vs transformation: cleaning fixes data problems; transformation changes form/scale.
- Dropping missing records by default can silently bias datasets.

### Self-check

- Why does unscaled data hurt distance-based algorithms?
- Name one risk of aggressive row dropping for missing values.

---

## 3) Evaluation and generalization (Week 3)

### What it is

Evaluation checks whether a model generalizes to unseen data.

- **Train error**: performance on seen data.
- **Test error**: performance on unseen data.
- Generalization quality is judged mostly by test/validation behavior.

### Classification metrics

- Confusion matrix terms: `TP`, `TN`, `FP`, `FN`.
- `Accuracy = (TP + TN) / (TP + TN + FP + FN)`.
- `Precision = TP / (TP + FP)` (reliability of positive predictions).
- `Recall = TP / (TP + FN)` (ability to capture actual positives).

### Regression metrics

- `MAE`: average absolute error.
- `SSE`: sum of squared errors.
- `MSE`: average squared error.

### Why it matters

Different business problems prioritize different errors. For example, missing fraud (`FN`) may be worse than false alarms (`FP`).

### Common confusion

- High accuracy on imbalanced data can still mean poor minority-class performance.
- Precision and recall are often mixed up; remember denominator meaning.

### Self-check

- In medical screening, which is usually more critical: precision or recall, and why?
- What does low train error + high test error indicate?

---

## 4) Decision trees and rule-based classification (Weeks 4-5)

### What it is

Both trees and rules are interpretable methods built on explicit conditions.

- Trees recursively split data using impurity reduction.
- Rule-based methods use `IF (LHS) THEN (RHS)` statements.

### Split criteria in trees

- **Entropy** and **Information Gain**: choose split with highest uncertainty reduction.
- **Gini index**: choose split with lowest child impurity.
- **Misclassification error**: simpler impurity estimate.

### Why it matters

Interpretable logic is useful in domains where decisions must be explained.

### Rule quality

- **Coverage**: fraction of data where rule antecedent (`LHS`) is true.
- **Accuracy of rule**: correctness among covered instances.

### Common confusion

- Coverage is not the same as accuracy.
- Deep trees can memorize training data; pruning/stopping is needed.

### Self-check

- If a rule has high coverage but low accuracy, what does it mean?
- Why can pruning improve test performance?

---

## 5) kNN and ensemble learning (Weeks 6-7)

### kNN: concept

kNN predicts using nearby training points in feature space.

- Choose `k` neighbors, aggregate their labels/values.
- Distance metric and scaling directly affect neighborhood geometry.

### kNN intuition

- Small `k`: flexible boundary, high variance, noise sensitive.
- Large `k`: smoother boundary, higher bias, may miss local structure.

### Ensemble concept

Ensembles combine multiple models to improve stability or accuracy.

- **Bagging**: parallel models on bootstrap samples; mainly variance reduction.
- **Random Forest**: bagging + random feature subsets per split to decorrelate trees.
- **Boosting**: sequential models that focus on previous errors; mainly bias reduction.

### Common confusion

- Random Forest is not just bagging; feature randomness is essential.
- Boosting is sequential, so it is not naturally parallel like bagging.

### Self-check

- If your model is unstable and high-variance, which ensemble family is a better first choice?
- Why must features be normalized before kNN?

---

## 6) Linear regression and gradient descent (Week 8)

### What it is

Linear regression fits parameters that minimize prediction error, typically using squared loss.

- Objective anchors: `SSE` and `MSE`.
- Gradient descent update idea: move parameters opposite gradient direction.

### Why it matters

This is a foundational model and optimization pattern used across advanced ML methods.

### Learning rate behavior

- Too high: oscillation or divergence.
- Too low: very slow convergence.

### Common confusion

- Updating parameters one-by-one inside the same iteration (instead of simultaneously) changes algorithm behavior.
- Assuming every optimization landscape is convex like basic linear regression.

### Self-check

- What happens when learning rate is extremely large?
- Why is convexity important in linear regression optimization?

---

## 7) Clustering family (Weeks 9-12)

### What it is

Clustering groups unlabeled points based on similarity/density/structure.

### k-means

- Iterative loop: initialize centroids -> assign points -> update centroids -> repeat.
- Works best for compact, roughly spherical clusters.
- Requires `k` in advance and is sensitive to initialization.

### Hierarchical clustering

- Builds nested cluster tree (dendrogram).
- Choose final cluster count by cutting the dendrogram at a chosen height.
- Useful when multi-level grouping is meaningful.

### DBSCAN

- Density-based with `eps` and `minPts`.
- Finds arbitrary-shaped clusters and identifies noise/outliers.
- Struggles when cluster densities vary significantly.

### BIRCH

- Uses a CF-tree summary for scalable clustering.
- Good for large datasets where full pairwise clustering is expensive.

### Common confusion

- k-means and DBSCAN optimize different assumptions; they are not interchangeable.
- DBSCAN does not automatically choose good parameter values.

### Self-check

- When would you prefer DBSCAN over k-means?
- Why might hierarchical clustering be chosen when `k` is unknown?

---

## 8) Association rule mining (Week 13)

### What it is

Association mining discovers item co-occurrence patterns in transactional datasets.

- Rule form: `X => Y`, where `X` and `Y` are disjoint itemsets.
- **Support**: frequency of `X U Y` in dataset.
- **Confidence**: `support(X U Y) / support(X)`.
- **Lift**: association strength relative to independence baseline.

### Why it matters

Useful for basket analysis, recommendation hints, and co-occurrence behavior discovery.

### Apriori logic

- If an itemset is infrequent, all its supersets are infrequent.
- This anti-monotonicity enables pruning and avoids brute-force search explosion.

### Common confusion

- High confidence does not always imply strong interestingness without checking lift/support context.
- Confusing support count with support fraction.

### Self-check

- Why is confidence alone sometimes misleading?
- How does Apriori reduce computation?

---

## 9) High-yield comparisons (quick recap)

- **Classification vs regression**: class label vs numeric output.
- **Train vs test error**: fitting seen data vs generalizing to unseen data.
- **Precision vs recall**: correctness of predicted positives vs coverage of actual positives.
- **Bagging vs boosting**: parallel variance reduction vs sequential error-focused bias reduction.
- **k-means vs DBSCAN**: centroid/known-`k` compact clusters vs density/arbitrary-shape/noise handling.
- **Tree vs rule model**: hierarchical splits vs explicit if-then logic.

---

## 10) Exam traps and last-day checklist

### Frequent traps

- Data leakage between train and test split.
- Ignoring feature scaling before kNN/k-means.
- Trusting accuracy alone for imbalanced data.
- Treating Random Forest and bagging as identical.
- Assuming boosting is parallel.
- Forgetting that wrong `k` in k-means still returns output.
- Assuming DBSCAN works without parameter tuning.

### Last-day checklist

- Can I explain each algorithm in 3 lines: idea, use-case, limitation?
- Can I compute or interpret core metrics (`accuracy`, `precision`, `recall`, `MSE`)?
- Can I choose a model based on data shape, noise, interpretability, and scale?
- Can I state one common pitfall and correction for each major topic?
