# Machine Learning: Connect the Dots (Weeks 1-13)

This is the full ML course in one line of thought: define learning settings, build clean data representations, train supervised models that generalize, choose methods that match structure (rules, trees, neighbors, ensembles, regression), then move to unsupervised discovery (clustering, scalability, association rules) with disciplined evaluation and practical trade-off awareness.

---

## The 13-week spine (one connected story)

### Week 1 - ML foundations and learning paradigms
- Core: what ML is, supervised vs unsupervised learning, practical ML lifecycle concerns.
- Why it matters: frames every later algorithm as a data-to-decision mapping with assumptions.
- Enables next: Week 2 formalizes dataset structure and quality.
- Hub: [week-1/1-Foundations of Machine Learning.md](week-1/1-Foundations of Machine Learning.md)

### Week 2 - Data representation and preprocessing
- Core: objects/attributes/types, dataset formats, data quality issues, preprocessing.
- Why it matters: model quality is constrained by data quality and feature semantics.
- Enables next: Week 3 starts supervised classification with proper train/test thinking.
- Hub: [week-2/1-Building Blocks of Data - Objects Attributes and Types.md](week-2/1-Building Blocks of Data - Objects Attributes and Types.md)

### Week 3 - Supervised classification basics and pitfalls
- Core: classification principles, performance evaluation, overfitting vs underfitting.
- Why it matters: introduces the generalization lens before specific algorithms.
- Enables next: Week 4 uses decision trees as the first full classifier family.
- Hub: [week-3/1-Foundations of ML and Supervised Learning.md](week-3/1-Foundations of ML and Supervised Learning.md)

### Week 4 - Decision trees from induction to pruning
- Core: tree structure, split criteria, handling nominal/ordinal/continuous attributes, stopping and pruning.
- Why it matters: gives interpretable rule-like supervised learning with clear bias-variance behavior.
- Enables next: Week 5 converts tree logic into explicit rule-based systems.
- Hub: [week-4/1-Introduction to Decision Trees.md](week-4/1-Introduction to Decision Trees.md)

### Week 5 - Rule-based classification
- Core: rule anatomy, coverage/accuracy, indirect rule generation (from trees), direct rule mining (sequential covering).
- Why it matters: separates interpretable decision logic from tree structure.
- Enables next: Week 6 contrasts eager model-building with lazy, instance-based prediction.
- Hub: [week-5/1-Introduction to Rule-Based Classification - Machine Learning.md](week-5/1-Introduction to Rule-Based Classification - Machine Learning.md)

### Week 6 - Lazy learning with kNN
- Core: eager vs lazy learning, kNN algorithm, distance choices, scaling, choice of $k$, dimensionality effects.
- Why it matters: shows prediction by local neighborhood geometry instead of global parametric fit.
- Enables next: Week 7 reduces variance through ensembles of unstable learners.
- Hub: [week-6/1-Introduction to Lazy Learning and kNN - Machine Learning.md](week-6/1-Introduction to Lazy Learning and kNN - Machine Learning.md)

### Week 7 - Ensemble learning
- Core: bias-variance rationale, bagging, random forest diversity, boosting and AdaBoost sequential focus.
- Why it matters: combines weak/unstable learners into stronger, more robust predictors.
- Enables next: Week 8 shifts to regression for continuous targets.
- Hub: [week-7/1-Foundations of Ensemble Learning The Power of Many - Machine Learning.md](week-7/1-Foundations of Ensemble Learning The Power of Many - Machine Learning.md)

### Week 8 - Regression and optimization
- Core: regression framing, SSE/MSE cost, linear hypothesis, gradient descent dynamics and learning rate.
- Why it matters: formalizes continuous-output prediction and objective-driven optimization.
- Enables next: Week 9 transitions from labeled prediction to unlabeled structure discovery.
- Hub: [week-8/1-Introduction to Regression - Machine Learning.md](week-8/1-Introduction to Regression - Machine Learning.md)

### Week 9 - Clustering fundamentals
- Core: clustering purpose, hard vs soft, flat vs hierarchical, proximity choices, cluster validity intuition.
- Why it matters: unsupervised learning depends on similarity assumptions, not labels.
- Enables next: Week 10 operationalizes these ideas via k-means.
- Hub: [week-9/1-Introduction to Clustering - Machine Learning.md](week-9/1-Introduction to Clustering - Machine Learning.md)

### Week 10 - k-Means in depth
- Core: centroid-based clustering loop, objective function (SSE), convergence behavior, initialization and $k$ selection issues.
- Why it matters: illustrates alternating optimization and local-optimum trade-offs in unsupervised learning.
- Enables next: Week 11 explores hierarchical alternatives when fixed $k$ is limiting.
- Hub: [week-10/1-K-means Clustering Algorithm - Machine Learning.md](week-10/1-K-means Clustering Algorithm - Machine Learning.md)

### Week 11 - Hierarchical clustering
- Core: dendrogram view, agglomerative vs divisive strategies, linkage/proximity matrix, complexity costs.
- Why it matters: captures multi-resolution structure instead of forcing one partition.
- Enables next: Week 12 addresses density-based and scalable clustering for large or irregular data.
- Hub: [week-11/1-Introduction to Hierarchical Clustering - Machine Learning.md](week-11/1-Introduction to Hierarchical Clustering - Machine Learning.md)

### Week 12 - Density and scalability (DBSCAN, BIRCH)
- Core: density-connected clusters (DBSCAN), parameter sensitivity, BIRCH CF-tree compression for scale.
- Why it matters: handles noise, non-spherical shapes, and large-data constraints better than vanilla k-means.
- Enables next: Week 13 generalizes unsupervised discovery to transactional co-occurrence patterns.
- Hub: [week-12/1-Density-Based Clustering and DBSCAN - Machine Learning.md](week-12/1-Density-Based Clustering and DBSCAN - Machine Learning.md)

### Week 13 - Association rule mining
- Core: transactions/itemsets, support-confidence-lift framing, Apriori anti-monotonic search, rule generation.
- Why it matters: moves from grouping points to discovering actionable co-occurrence patterns.
- Enables next: practical deployment of interpretable unsupervised knowledge extraction.
- Hub: [week-13/1-Introduction to Association Rule Mining - Machine Learning.md](week-13/1-Introduction to Association Rule Mining - Machine Learning.md)

---

## Cross-week threads you should see instantly

- **Data-first thread:** Week 2 data quality choices control Week 3-8 supervised outcomes and Week 9-13 unsupervised structure quality.
- **Generalization thread:** Week 3 formalizes under/overfitting, Week 4-7 shows algorithmic controls (pruning, rules, $k$, ensembles), Week 8 ties this to objective optimization.
- **Structure-matching thread:** trees/rules for interpretability, kNN for local geometry, ensembles for variance reduction, regression for continuous targets, clustering/association for unlabeled discovery.
- **Optimization thread:** Week 8 gradient descent in regression and Week 10 alternating optimization in k-means are two objective-minimization templates.
- **Scalability thread:** moves from classic algorithms to hierarchical, density-based, and CF-tree compression to handle real-world data size and shape.

---

## End-to-end good-ML-system checklist

1. **Problem framing:** supervised vs unsupervised objective is explicit.
2. **Data readiness:** attribute types, missingness, scale, and noise are handled first.
3. **Model fit to structure:** choose algorithm family by data geometry and interpretability need.
4. **Generalization discipline:** detect overfitting early; use pruning/regularizing design choices.
5. **Objective awareness:** understand what the algorithm actually minimizes and where local optima appear.
6. **Evaluation validity:** metrics and validation strategy match business risk and task type.
7. **Scalability planning:** complexity and memory behavior are feasible for data size.
8. **Actionable outputs:** predictions/clusters/rules are interpretable enough for decisions.

---

## 13 one-line hinges (rapid revision)

| Week | Hinge |
|------|-------|
| 1 | ML starts with learning paradigm clarity, not algorithm choice. |
| 2 | Better data representation beats premature model complexity. |
| 3 | Generalization is the central test of supervised learning. |
| 4 | Decision trees convert feature tests into human-readable logic. |
| 5 | Rules trade structure for interpretability and modular control. |
| 6 | kNN predicts by local neighborhoods, so distance design is everything. |
| 7 | Ensembles improve stability by aggregating diverse learners. |
| 8 | Regression formalizes continuous prediction through explicit cost minimization. |
| 9 | Clustering quality depends on similarity assumptions, not labels. |
| 10 | k-means is efficient but sensitive to initialization and chosen $k$. |
| 11 | Hierarchical clustering provides nested structure, not just one cut. |
| 12 | DBSCAN/BIRCH address noise, shape, and scale limits of basic clustering. |
| 13 | Association rules turn transactions into interpretable co-occurrence knowledge. |

---

Use this note as the map. Use week notes for detail; use this page for conceptual continuity across the full course.
