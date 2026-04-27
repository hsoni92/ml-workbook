# Machine Learning: Connect the Dots (Weeks 1-13)

This note is one continuous story across the course: you frame the learning problem, shape data so algorithms can use it, build supervised predictors that generalize by matching method to structure, then turn to unsupervised discovery when labels are absent or beside the point. Along the way, the same ideas recur—data quality before model complexity, what is being optimized, and whether the output scales to real data. Tags like `[week-3]` mark where a topic is developed in depth.

---

## From paradigms to honest evaluation

Machine learning is not a catalog of tricks; it is learning a mapping from data to decisions under assumptions you must state up front [week-1]. Supervised learning uses labels to predict outcomes; unsupervised learning looks for structure without them. The practical lifecycle—problem definition, data, modeling, evaluation, deployment—means every algorithm is only as credible as the pipeline around it [week-1].

Before you choose a learner, you fix how the world is represented: objects, attributes, types, formats, and the semantic meaning of each field [week-2]. Noise, missing values, inconsistent scales, and bad encodings cap what any later model can do; preprocessing is not optional polish but part of the inductive bias you inject [week-2]. That data-first thread runs through everything that follows: the same representation choices that help or hurt classifiers also determine whether clusters or association patterns mean anything [week-2].

With labels in hand, classification becomes the default supervised question: assign discrete outcomes from inputs [week-3]. The central tension is generalization—performance on new data—not memorizing the training set [week-3]. Evaluation metrics and validation discipline make that tension visible; overfitting and underfitting name the two ways a model can lie about how well it will generalize [week-3]. From here on, algorithm families are different answers to the same question: how to control bias and variance while staying interpretable or accurate enough for the task.

Decision trees grow piecewise boundaries by recursive splits on attributes, handling nominal, ordinal, and continuous features with explicit split criteria [week-4]. They read as nested if-then logic, so humans can audit them; pruning and stopping rules are direct levers on overfitting [week-4]. Rule-based classification peels that logic into standalone rules—coverage, accuracy, and conflict resolution—either indirectly from trees or directly via sequential covering and related mining ideas [week-5]. You trade the tidy tree shape for modular, sometimes more controllable, rule sets [week-5].

k-nearest neighbors flips the script: unlike eager methods that fold training data into a global model before prediction, kNN is lazy—it stores data and predicts by the geometry of local neighborhoods [week-6]. Distance metrics, feature scaling, the choice of $k$, and the curse of dimensionality are not implementation details; they are the model [week-6]. Ensembles then ask what happens when many learners disagree: bagging and random forests average or diversify high-variance base models; boosting chains weak learners so later stages emphasize what earlier ones missed [week-7]. The through-line is stability and error reduction by combining what single trees or shallow rules might miss [week-7].

---

## Continuous targets, then discovery without labels

Regression shifts the target from a class to a real-valued quantity [week-8]. You state a cost—sum of squared errors, mean squared error—and fit parameters so that cost falls, often via gradient descent, where step size and curvature determine whether optimization helps or diverges [week-8]. The generalization story from classification still applies; here the objective is simply explicit in the algebra [week-8].

When labels are unavailable or not the goal, you still need a notion of similarity and a purpose: partition points, soft assignments, flat versus hierarchical structure, and how you will argue that a grouping is valid [week-9]. Clustering quality is driven by those assumptions, not by ground-truth labels you do not have [week-9].

k-means fixes $k$ centroids and alternates assigning points to nearest centers and recomputing centers to reduce within-cluster dispersion—an SSE-style objective and a prototype for alternating optimization, with local optima and sensitivity to initialization and $k$ [week-10]. Hierarchical clustering instead builds a nested tree of merges or splits, exposing many possible cuts through a dendrogram and paying complexity for that flexibility via linkage choices and distance updates [week-11]. When clusters are not round blobs or noise is heavy, density-based methods such as DBSCAN follow connected dense regions; when data are huge, structures like BIRCH compress summaries in a CF-tree so clustering can scale [week-12]. That scalability arc—moving from basic prototypes to methods that respect shape, noise, and memory—is the same practical pressure that showed up in data prep and in ensemble training costs [week-12].

Association rule mining is a different unsupervised face: not grouping rows in metric space, but finding frequent itemsets and rules in transactions, with support, confidence, and lift framing what “interesting” means and Apriori-style search exploiting structure to keep the search feasible [week-13]. The output is still interpretable pattern knowledge, but tied to co-occurrence rather than Euclidean neighborhoods [week-13].

Two optimization templates echo across the course: gradient-style steps on a smooth supervised loss [week-8] and discrete alternating updates that chase a clustering objective [week-10]. Keeping sight of what is actually minimized—and where greedy or local procedures can stall—keeps both supervised and unsupervised methods honest.

---

## Hub notes by week

Depth lives in the week folders. Starting points:

- [week-1/1-Foundations of Machine Learning.md](week-1/1-Foundations of Machine Learning.md)
- [week-2/1-Building Blocks of Data - Objects Attributes and Types.md](week-2/1-Building Blocks of Data - Objects Attributes and Types.md)
- [week-3/1-Foundations of ML and Supervised Learning.md](week-3/1-Foundations of ML and Supervised Learning.md)
- [week-4/1-Introduction to Decision Trees.md](week-4/1-Introduction to Decision Trees.md)
- [week-5/1-Introduction to Rule-Based Classification - Machine Learning.md](week-5/1-Introduction to Rule-Based Classification - Machine Learning.md)
- [week-6/1-Introduction to Lazy Learning and kNN - Machine Learning.md](week-6/1-Introduction to Lazy Learning and kNN - Machine Learning.md)
- [week-7/1-Foundations of Ensemble Learning The Power of Many - Machine Learning.md](week-7/1-Foundations of Ensemble Learning The Power of Many - Machine Learning.md)
- [week-8/1-Introduction to Regression - Machine Learning.md](week-8/1-Introduction to Regression - Machine Learning.md)
- [week-9/1-Introduction to Clustering - Machine Learning.md](week-9/1-Introduction to Clustering - Machine Learning.md)
- [week-10/1-K-means Clustering Algorithm - Machine Learning.md](week-10/1-K-means Clustering Algorithm - Machine Learning.md)
- [week-11/1-Introduction to Hierarchical Clustering - Machine Learning.md](week-11/1-Introduction to Hierarchical Clustering - Machine Learning.md)
- [week-12/1-Density-Based Clustering and DBSCAN - Machine Learning.md](week-12/1-Density-Based Clustering and DBSCAN - Machine Learning.md)
- [week-13/1-Introduction to Association Rule Mining - Machine Learning.md](week-13/1-Introduction to Association Rule Mining - Machine Learning.md)

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

## Thirteen hinges (rapid revision)

1. ML starts with learning paradigm clarity, not algorithm choice. [week-1]
2. Better data representation beats premature model complexity. [week-2]
3. Generalization is the central test of supervised learning. [week-3]
4. Decision trees convert feature tests into human-readable logic. [week-4]
5. Rules trade structure for interpretability and modular control. [week-5]
6. kNN predicts by local neighborhoods, so distance design is everything. [week-6]
7. Ensembles improve stability by aggregating diverse learners. [week-7]
8. Regression formalizes continuous prediction through explicit cost minimization. [week-8]
9. Clustering quality depends on similarity assumptions, not labels. [week-9]
10. k-means is efficient but sensitive to initialization and chosen $k$. [week-10]
11. Hierarchical clustering provides nested structure, not just one cut. [week-11]
12. DBSCAN/BIRCH address noise, shape, and scale limits of basic clustering. [week-12]
13. Association rules turn transactions into interpretable co-occurrence knowledge. [week-13]

---

Use this page for conceptual continuity across the full course; use the week notes for derivations, algorithms, and exercises.
