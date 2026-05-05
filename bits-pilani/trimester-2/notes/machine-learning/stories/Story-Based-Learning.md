# Machine Learning — Story-Based Learning

Memory-first stories aligned with the course week map. For topic navigation and drill, use the [week index](../index.md) and [revision sheet](../REVISION.md).

---

## Week 1 — The Kitchen You Cannot Fully Script (Foundations)

**The story:** You are opening a restaurant, but the world is too messy to write every rule by hand ("if humidity is 73% and day is Tuesday, then…"). **Machine learning** is hiring a cook who **learns patterns from examples** instead of following an infinite rulebook.

- **Supervised learning:** Every training plate comes with a label — "this was spicy," "this was mild." The model learns a mapping from ingredients to outcome. **Classification** if the answer is a category; **regression** if the answer is a number (Week 8 goes deeper on the latter).
- **Unsupervised learning:** Nobody tells you the dish names — you only see orders. You still **group, summarize, or structure** the chaos (clusters, associations later in the course).
- **Real projects loop:** You do not "train once and ship." You **collect → clean → model → evaluate → fix data or model → repeat**. KDD and CRISP-DM are two names for the same truth: discovery is **iterative**.

| Story | ML term |
|-------|---------|
| Infinite messy rules | Why we learn from **data** |
| Labeled training plates | **Supervised** learning |
| Mystery pile of orders | **Unsupervised** learning |
| Category vs amount as answer | **Classification** vs **regression** |
| Cook, taste, adjust, repeat | **Iterative** lifecycle (KDD / CRISP-DM) |

> **ML = turn data into decisions when hand-written rules cannot scale — and expect to loop back after evaluation.**

**Key properties / pitfalls:**
- ML sits inside broader **AI** (systems that perceive, decide, act) and overlaps **data science** — do not treat the three as identical.
- **Generalization** matters: performance on new situations beats memorizing the training set.

---

## Week 2 — Ingredients, Labels, and Prep (Data)

**The story:** Each **data object** is one row on your prep sheet. **Attributes** are the columns — what you measure. **Types** decide how you are allowed to compare or average: nominal (names), ordinal (ordered ranks), interval/ratio (numbers where distance means something).

- **Quality:** Missing values, noise, outliers, contradictions — like rotten produce mixed in. Blind deletion of rows can **bias** who remains in the dataset.
- **Preprocessing:** Clean, integrate sources, transform scales (**normalization** / standardization), sometimes **reduce** rows or features when redundancy is huge.
- **Why scaling haunts you later:** Distance-based methods (kNN, k-means) and gradient-based training treat feature magnitudes as geometry. Unscaled data = one loud feature dominates distance.

| Story | ML term |
|-------|---------|
| One prep row | **Object / instance** |
| Measured columns | **Attributes / features** |
| Names vs ranks vs true measurements | **Attribute types** |
| Rotten or missing items | **Data quality** issues |
| Chop, merge, rescale | **Preprocessing** |
| Loud ingredient drowns others | Need **scaling** for distance / gradients |

> **Garbage in, garbage out — preprocessing is not cosmetic; it changes the geometry the algorithm sees.**

**Key properties / pitfalls:**
- **Cleaning** fixes wrong/missing; **transformation** changes representation or scale — different jobs.
- Keep **train/test discipline** in mind before you even model (Week 3): decisions like imputation should not leak future information.

---

## Week 3 — Practice Test vs Final Exam (Evaluation)

**The story:** **Training error** is how you do on homework you already saw. **Test error** is the final exam on **unseen** questions. A model that only crushes homework has not proved it **generalizes**.

- **Confusion matrix** for classification: true positives (TP), true negatives (TN), false positives (FP), false negatives (FN).
- **Accuracy** = $(\mathrm{TP} + \mathrm{TN}) / (\mathrm{TP} + \mathrm{TN} + \mathrm{FP} + \mathrm{FN})$ — tempting, but misleading on **imbalanced** classes.
- **Precision** = $\mathrm{TP} / (\mathrm{TP} + \mathrm{FP})$ — "when I say positive, how often am I right?"
- **Recall** = $\mathrm{TP} / (\mathrm{TP} + \mathrm{FN})$ — "of all real positives, how many did I catch?"
- **Regression metrics** (preview): **MAE** (average absolute miss), **SSE** / **MSE** (penalize big errors harder).

| Story | ML term |
|-------|---------|
| Homework score | **Train** error |
| Final exam | **Test** error |
| Tally of hits and misses | **Confusion matrix** |
| Overall correctness | **Accuracy** |
| Trust of positive alarms | **Precision** |
| Catch rate of true problems | **Recall** |

> **Choose metrics to match the cost of mistakes — not every problem treats FP and FN equally.**

**Key properties / pitfalls:**
- High accuracy + rare positives can hide a useless detector (exam classic).
- **Overfitting:** low train error, high test error — memorized noise. **Underfitting:** both bad — model too simple.

---

## Week 3 (continued) — The Student Who Memorized the Syllabus (Overfitting)

**The story:** **Underfitting** is a student who only learns one slogan and fails every nuanced question. **Overfitting** is the student who memorizes every past exam pixel-perfect but freezes on a new wording.

- **Capacity / complexity** trades bias vs variance: too simple → underfits; too flexible → chases noise.
- **Mitigations** (theme for the whole course): more or better data, simpler model, constraints, pruning (trees), regularization elsewhere, honest validation.

| Story | ML term |
|-------|---------|
| One slogan | **Underfitting** (high bias) |
| Memorize past papers | **Overfitting** (high variance) |
| Fail new questions anyway | Poor **generalization** |

> **Low training error is not a trophy if test error screams.**

---

## Week 4 — Twenty Questions Until the Dish Is Known (Decision Trees)

**The story:** You play **20 questions** on a mystery dish. Each question splits the possibilities ("spicy?" → yes/no). You pick the next question that **reduces uncertainty the most**. A **decision tree** is exactly that: recursive **splits** on attributes until leaves predict a class (or value).

- **Impurity** measures how mixed a node is: **entropy**, **Gini** — the algorithm prefers splits that make children **purer**.
- **Nominal vs numeric attributes** change how you search for a good split (equality tests, thresholds, multi-way splits).
- **Pruning / stopping:** deep trees memorize training quirks; trimming or limiting depth often **helps test performance**.

| Story | ML term |
|-------|---------|
| Each yes/no question | **Split** on an attribute |
| Reducing mixed dishes in a bucket | **Impurity reduction** (e.g. information gain, Gini) |
| Final guess at a leaf | **Leaf prediction** |
| Cutting branches | **Pruning** / stop rules |

> **A decision tree is a hierarchy of questions optimized to separate classes fast — depth is a double-edged sword.**

**Key properties / pitfalls:**
- Strength: **interpretable** paths. Weakness: unstable, greedy; small data changes can reshape early splits.

---

## Week 5 — Traffic Lights vs Mining the Accident Log (Rule-Based Classification)

**The story:** A **rule** reads like city signage: **IF** (conditions on the left, the **antecedent**) **THEN** (prediction on the right, the **consequent**). A list of rules can classify incoming cases by firing the first match or aggregating.

- **Coverage:** fraction of data where the antecedent is true — how **wide** the rule reaches.
- **Accuracy of a rule:** among covered rows, how often the consequent is correct — how **sharp** it is when it fires.
- **Indirect rule generation:** extract rules from another structure (e.g. paths of a decision tree).
- **Direct rule mining:** search the space of rules with quality measures — more flexible, needs careful control of search.

| Story | ML term |
|-------|---------|
| IF lights red THEN stop | **Rule** (antecedent → consequent) |
| How often the IF is true | **Coverage** |
| How right the THEN is when IF fires | **Rule accuracy** |
| Rules read off a tree | **Indirect** generation |
| Search for strong rules in data | **Direct** rule mining |

> **High coverage with low accuracy means a loud rule that is often wrong — wide net, blunt hook.**

---

## Week 5 (continued) — The City Planner vs the Accident Detective (Indirect vs Direct Rule Mining)

**The story — Part A: Indirect (read rules from a tree).** Imagine a city planner who **first draws a full decision tree** of every intersection — which roads branch where, which lights change when — and then **reads off the sign rules** from the tree's paths. Every root-to-leaf path becomes one rule: the conjunction of all tests along the path gives the antecedent; the leaf label gives the consequent. This is the **indirect method**: build a surrogate model (a tree), then translate it into rules. Clean, structured, mutually exclusive (one tuple can only take one path), but the rules inherit the tree's complexity.

**The story — Part B: Direct (mine rules from data).** Now imagine an accident detective who **never builds a map**. Instead, they scan the accident log for **patterns**: "when the speed limit is high AND the intersection has no signal AND the driver is young → crash." They find one strong pattern, write it as a rule, then **remove all accidents that matched that rule** from the log, and start searching again. Keep going until no more useful patterns remain. Finally, add a **default rule** for any accident not covered by the discovered patterns. This is **sequential covering** — the direct method. The algorithm is called **RIPPER** when it adds careful pruning and optimization on top of this skeleton.

**What "general → specific" means in rule refinement.** A rule starts broad (covers many accidents, including ones you don't want). Each additional condition you tack onto the IF side narrows the rule — it becomes more **specific**. You stop adding conditions when the rule is **sharp enough** (high accuracy on covered examples). FOIL information gain measures whether adding one more condition actually improves the rule's ability to isolate the target class or just adds noise.

**What breaks after simplification.** If you strip conditions from rules to make them shorter (faster evaluation), you can **lose mutual exclusion** — one case might now match two rules with conflicting predictions. You can also **lose exhaustiveness** — a case might match nothing, hence the **default rule** (often the majority class of remaining uncovered examples) is always appended last.

| Story | ML term |
|-------|---------|
| Planner draws a full tree first | **Indirect**: tree → rules |
| Detective finds one pattern, removes covered cases | **Sequential covering** (direct) |
| Adding more AND conditions to narrow a rule | **General → specific** refinement |
| Stripping conditions for speed | **Rule simplification** (can break mutual exclusion) |
| "None of the above" catch-all | **Default rule** |
| Detective's scoring of "does this condition help?" | **FOIL information gain** |

> **Indirect rule mining = read the rulebook from a map someone else drew. Direct rule mining = patrol the accident scene yourself with a notebook, write down patterns, remove covered ground, repeat.**

**Key properties / pitfalls:**
- Indirect methods inherit the tree's **greedy** nature — rules are as good as the tree was before extraction.
- Direct methods need careful **stopping criteria** or they'll keep refining until rules memorize noise.
- Size ordering (specific rules first) vs quality ordering (best rules first) are two conflict-resolution policies — know the difference.
- RIPPER uses **pruning** to avoid overfitting long rules — that's what makes it practically strong on tabular data.

---

## Week 6 — The Student Who Studies Only on Exam Day (kNN)

**The story:** **Eager learners** (trees, rules, neural nets) spend training time building a compact model — studying all semester. **Lazy learners** like **k-nearest neighbors (kNN)** do almost nothing during training: they just **store the training data**. When the exam question comes (a new query), they frantically look around the exam hall, find the **k** people sitting nearest to them, and **copy their answers** (majority vote for classification, average for regression).

- **Small k:** wiggly, local, **sensitive to noise** — one bribed student can corrupt the answer. **Large k:** smoother, more **bias**, but might wash out the point of asking neighbors at all.
- **Distance metric** and **feature scaling** define what "near" means — unscaled features distort neighborhoods so badly that one huge-scale feature bullies all the rest out of the distance calculation.

| Story | ML term |
|-------|---------|
| No model until query time | **Lazy** learning |
| Closest classmates vote | **kNN** decision |
| Few voters | Small **k** (flexible, noisy) |
| Many voters | Large **k** (smooth, biased) |
| Same measuring cups for every feature | **Normalize** before distance |

> **kNN = democracy of proximity — redraw the map if you change scales.**

---

## Week 6 (continued) — The Voronoi Arena and the Blindfold Hike (kNN Geometry and Gradient Descent)

**The story — Part A: kNN's decision surface.** With **k=1**, every training point owns a patch of the exam hall — the region where it is the single closest person. Draw boundaries between patches owned by different classes. These boundaries form a **Voronoi tessellation**: each cell is the set of seats closer to you than to anyone else. The classification boundary is where cells of different classes meet. 1-NN can carve **extremely intricate** boundaries — it can memorize the training set perfectly. That's also its weakness: one mislabeled training point owns a little cell of wrong influence right in the middle of the correct region.

**Part B: Weighted voting.** Instead of giving every of the k neighbors equal vote, give closer neighbors **more** influence — typically weight proportional to **1 / distance**. This sharpens the decision: the two closest neighbors matter more than the 8th closest in a k=10 vote.

**Part C: The cost of being lazy.** kNN stores all training data — so memory scales with N. And each query scans all N rows plus dimension d. At large N and high d, this is expensive. **Approximate nearest neighbor** methods (k-d trees, FAISS-style inverted indexes) reduce the scan cost at the price of occasional missed neighbors.

| Story | ML term |
|-------|---------|
| Each person's seat territory | **Voronoi cell** (1-NN) |
| Carving complex territory piece by piece | **1-NN** creates highly flexible, nonlinear boundaries |
| One bribed student | **Label noise** → 1-NN is sensitive to it |
| Closer neighbors talk louder | **Distance-weighted** kNN |
| Store all past exams | **Full training set retention** (memory cost) |

> **kNN does zero work until the moment it needs to answer — then it asks the neighborhood. Zero model-building is its charm and its curse.**

**Key properties / pitfalls:**
- **k = N** collapses to predicting the **global majority** class — no locality survives.
- **Even k in binary classification** can tie without distance weighting — always have a tie-break policy.
- The **curse of dimensionality** hits kNN hard: in high-d spaces, all distances look similar and "nearest" loses meaning. Feature selection or PCA before kNN is often essential.
- **No scaling** → one dimension dominates distance → neighbors are chosen by that one dimension alone.

---

## Week 7 — The Jury, the Bootstraps, and the Tutor (Ensembles)

**The story:** One expert can be weirdly wrong. A **ensemble** combines many models to **stabilize** or **boost** performance.

- **Bagging:** train many models on **bootstrap** samples (draw rows with replacement), **average** or vote. Variance often drops — good when base learners are **high-variance** (deep trees).
- **Random Forest:** bagging **plus** random feature subsets at each split so trees are **decorrelated** — not "bagging alone."
- **Boosting:** models train **sequentially**; later models focus on what earlier ones got wrong — **not** embarrassingly parallel like bagging. Strong on reducing **bias** when weak learners are a bit better than random.

| Story | ML term |
|-------|---------|
| Many opinions averaged | **Ensemble** |
| Different study samples with replacement | **Bootstrap** + **bagging** |
| Randomized questions per tree | **Random Forest** decorrelation |
| Tutor fixes last week's mistakes | **Boosting** (e.g. AdaBoost) |

> **Bagging parallelizes diversity; boosting sequences correction — opposite engineering vibes.**

---

## Week 8 — The Line Through the Scatter (Regression and Gradient Descent)

**The story:** **Linear regression** fits a weighted line (or hyperplane) through points to predict a **number**. Wrong predictions cost you — classic choice is **squared error**, so big misses hurt a lot.

- **SSE** = sum of squared errors; **MSE** = mean squared error — both **cost** landscapes for linear models.
- **Gradient descent:** you stand on the cost hill, read the **gradient** (direction of steepest increase), and step **opposite** it by a **learning rate** $\eta$. Too large $\eta$ → oscillate or diverge; too small → crawl.
- Updates should treat parameters **consistently within an iteration** (batch view) — ad-hoc one-at-a-time tweaks change the algorithm story.

| Story | ML term |
|-------|---------|
| Predict a quantity | **Regression** |
| Total squared mistakes | **SSE** / **MSE** cost |
| Step downhill on the error surface | **Gradient descent** |
| Step size dial | **Learning rate** $\eta$ |

> **Regression minimizes prediction error; gradient descent is the blind hiker following the slope.**

---

## Week 8 (continued) — The Blind Hiker and the Ridge Regulator (Gradient Descent and Regularization)

**The story — Part A: Gradient descent in detail.** You're a blind hiker on a mountainside (the **MSE cost surface**). You can't see the whole mountain — you can only feel the slope under your feet. The gradient tells you the direction of steepest ascent. You want the lowest valley, so you step in the **opposite** direction: $\theta := \theta - \alpha \nabla J$. The **learning rate** $\alpha$ is how big a step you take. Too large and you overshoot, bouncing between two sides of the valley or even climbing back up. Too small and you inch forward, taking forever to reach the bottom. For **linear regression with MSE**, the surface is a smooth convex bowl — gradient descent is guaranteed to find the **global minimum** if you take small enough steps and run long enough.

**Simultaneous updates matter.** You compute the gradient for **all** parameters at the current $\theta$ before making any updates. If you update $\theta_0$, then compute the gradient for $\theta_1$ **using the already-updated $\theta_0$**, you've changed the problem mid-iteration — that's not gradient descent on the original surface, it's something messier.

**Part B: Why we regularize.** Without constraint, a linear model can fit the training data perfectly but behave catastrophically on new data — especially when features are highly correlated or when $d$ is large relative to $m$. **Regularization** adds a penalty term to the cost function that discourages the weights $\theta$ from growing unbounded:

- **Ridge (L2):** add $\lambda\sum\theta_j^2$ to the cost — pulls weights toward zero smoothly but rarely exactly zero.
- **Lasso (L1):** add $\lambda\sum|\theta_j|$ — can set some weights exactly to zero, performing **feature selection**.

The right analogy: you are not just trying to find the lowest valley, you are also trying to stay **near the origin** (small $\theta$). How strongly you enforce that depends on $\lambda$. Too little regularization → overfitting. Too much → underfitting (all $\theta$ near zero, model predicts near the mean everywhere).

**Part C: Closed form vs iterative.** The **normal equations** solve $\theta = (X^TX)^{-1}X^Ty$ directly — one-shot, no learning rate, but requires inverting a $d \times d$ matrix which is $O(d^3)$. For large $d$ (or sparse data), gradient descent scales much better. For small $d$ with invertible $X^TX$, closed form is often faster.

| Story | ML term |
|-------|---------|
| Feel slope under feet | **Gradient** of $J(\theta)$ |
| Step opposite the steepest direction | **Negative gradient** update |
| Step size | **Learning rate** $\alpha$ |
| Bouncing or climbing instead of descending | **Oscillation / divergence** from too-large $\alpha$ |
| Stay near the origin (low $\theta$) | **Regularization** (L2 = Ridge, L1 = Lasso) |
| One-shot matrix solve | **Normal equations** (closed form) |

> **Gradient descent is the blind hiker who takes small steps in the direction that goes most downhill — keep going until the ground feels flat. Regularization keeps the hiker from venturing into dangerous cliff regions where the view looks great but the drop is lethal.**

**Key properties / pitfalls:**
- Linear regression MSE is **convex** — one global minimum, no local trap. Deep learning cost surfaces are **not** convex, so gradient descent can get stuck.
- **Feature scaling** is critical for gradient descent speed — unscaled features make the bowl elongated and GD zigzag wastefully.
- **$\lambda$** (regularization strength) is a **hyperparameter** tuned by cross-validation, not learned from training data.
- **L1 regularization** can eliminate features entirely (set $\theta_j = 0$), which is useful when many features are irrelevant.

---

## Week 9 — Customers Without Name Tags (Clustering Landscape)

**The story:** You have **no labels** — just people moving in a mall. **Clustering** asks: who naturally clumps together? Algorithms differ by what "clump" means.

- **Partitional:** pick **k** groups and optimize (k-means family). **Hierarchical:** build a **tree** of merges or splits. **Density-based:** follow crowded regions, leave sparse areas as **noise**.
- **Proximity** (distance or similarity) and **representation** (raw features vs embedded space) decide what the algorithm can see.
- **Types of clusters:** tight globes, elongated chains, nested rings — different methods tolerate different shapes.

| Story | ML term |
|-------|---------|
| No answer key | **Unsupervised** clustering |
| Fixed number of tables | **Partitional** (e.g. k-means) |
| Merge diary / family tree | **Hierarchical** |
| Crowds vs empty floor | **Density-based** (e.g. DBSCAN) |

> **Clustering = find groups when nobody told you the group names — pick the algorithm that matches your geometry.**

---

## Week 10 — K-Means: The Wedding Planner

**The story:** You're a wedding planner with **K=3 tables** to arrange. You have no idea who likes sitting with whom. So:

1. **Randomly pick 3 people** as "table captains" — they define where each table is.
2. **Everyone picks the nearest captain's table.** Groups form naturally.
3. **Each captain moves to the center of their crowd** — repositions to the mean of everyone at their table.
4. **Everyone re-checks** if their nearest table changed. Some people switch.
5. **Repeat** until nobody moves.

**Everyone is now at their most appropriate table. The 3 groups are discovered.**

| Story | K-Means Term |
|-------|------------|
| Wedding tables to arrange | **K clusters** (you pick K upfront) |
| Random captains | **Centroids initialized randomly** |
| Everyone picks nearest table | **Assign points to nearest centroid** |
| Captain moves to center of crowd | **Recalculate centroid = mean of assigned points** |
| Nobody switching anymore | **Convergence** — stable clusters found |

> **K-Means = wedding planner arranging guests into K tables by repeatedly asking "who's closest to whom" until nobody moves.**

**Key properties:**
- Hard assignments (each point belongs to exactly one cluster)
- Spherical/globular clusters only
- Sensitive to random initialization (run multiple times!)
- Converges to **local minimum**, not global

**Objective and WCSS:** K-means is tied to minimizing **within-cluster sum of squares (WCSS)** — sum of squared distances from points to their centroid. Lower WCSS = tighter tables. Different random starts can land in different local minima; **compare WCSS** across runs.

**Choosing K — the elbow party:** Plot WCSS (or inertia) vs $k$. Early drops matter; the **elbow** is where shrinking error stops being worth extra complexity. Heuristics help, but domain sense still wins.

**Algorithm steps:**

```
1. Initialize K centroids randomly
2. Assign each point to nearest centroid (Euclidean distance)
3. Recalculate each centroid = mean of assigned points
4. Repeat step 2 & 3 until convergence (no point switches)
```

**Convergence = local minimum reached.** Since initialization is random, run K-Means multiple times and pick the run with lowest WCSS.

---

## Week 11 — The Merge Ledger (Hierarchical Clustering)

**The story:** Every customer starts as their own **singleton** cluster. Each day you **merge the two closest** mini-groups and write the merge in a ledger. Keep going until everyone is one big company. That ledger drawn vertically is a **dendrogram**. **Cut** the tree at a height → you choose how many clusters you want **after** seeing structure.

- **Agglomerative:** bottom-up merges (most common in courses). **Divisive:** top-down splits (e.g. bisecting k-means flavor).
- **Linkage** decides "closest groups" meaning: single-link (nearest pair), complete-link (farthest pair), average-link (average pair distance), Ward (merge cost in variance) — different sensitivities to chain shapes and cluster size.

**The Linkage — How Do You Measure Distance Between Two Tribes?**

You have two groups of people. How do you define the "distance" between them? Four common answers:

- **Single linkage:** pick the **closest two people** from each group, call that the group distance. Like connecting families by their friendliest member. Risk: **chaining** — a bridge of mediocre connections can merge two blobs that should stay separate.
- **Complete linkage:** pick the **farthest two people** from each group. Guarantees clusters are **compact and globular** — no member of one cluster is farther from the other cluster than the merge height. More conservative mergers.
- **Average linkage:** compute **all pairwise distances** between the two groups, take the mean. A fair compromise — neither swayed by the closest pair (single) nor the most distant pair (complete).
- **Ward linkage:** instead of distance, measure how much **within-cluster variance increases** if you merge. Like measuring the mess introduced — merging two tight families that each keep to themselves costs more than merging two already-messy groups.

| Story | ML term |
|-------|---------|
| Daily merger diary | **Dendrogram** |
| Start alone, merge up | **Agglomerative** |
| Start one blob, split down | **Divisive** |
| Where you chop the diary | **Cut height** ↔ number of clusters |
| Definition of "closest groups" | **Linkage** rule |
| Friendliest member bridge | **Single linkage** (chaining risk) |
| Most distant pair rule | **Complete linkage** (compact, globular) |
| Mean of all cross-group pairs | **Average linkage** (fair compromise) |
| "Mess cost" of merging | **Ward linkage** (variance increase) |

> **Hierarchical clustering = build a merge tree first, decide K later by where you cut.**

**Key properties / pitfalls:**
- No upfront $k$ required to **build** the tree — but you still choose a cut.
- **Scalability:** naive agglomerative methods can be costly on huge $n$; BIRCH (Week 12) addresses big data differently.
- **Single linkage** can produce elongated, chain-like clusters even when true blobs are spherical — know your linkage.
- **Divisive** (top-down) uses repeated k-means to split — faster in some implementations but greedy: once split, no merge to undo a bad early decision.

---

## Week 12 — DBSCAN: The Party Planner

**The story:** You're at a **house party**, observing from above. Some areas have **crowds of friends** chatting. Some people are **standing alone**. You have two dials:

- **MinPts** = how many people within arm's reach to call someone "part of a group"
- **EPS ($\varepsilon$)** = what you consider "arm's reach" (radius)

Now walk through the party:
- Anyone with ≥ MinPts within $\varepsilon$ → **core point** → "this is a cluster, mark everyone nearby"
- Border points (fewer than MinPts but within $\varepsilon$ of a core) → join that cluster
- Not a core, not near any core → **noise**, left alone

**The result:** You discovered clusters **without pre-deciding how many**. Loners were automatically tagged as noise.

| Story | DBSCAN Term |
|-------|------------|
| Arm's reach radius | **$\varepsilon$** — search radius |
| Min people to form a group | **MinPts** — minimum points in $\varepsilon$-neighbourhood |
| Crowd area | **Dense region** → cluster |
| Person standing alone | **Noise point** |
| Edge of a crowd | **Border point** |

> **DBSCAN = party planner who says "wherever enough people cluster within arm's reach, that's a group — everyone else is just standing alone."**

**Core / Border / Noise — The Three Guest Types:**

- **Core point:** at least MinPts neighbors within $\varepsilon$ — the social hub. If you're a core, you get to **pull in** everyone near you into your cluster.
- **Border point:** fewer than MinPts neighbors, but sits within $\varepsilon$ of some core. You don't have enough friends to be a hub, but you're **adjacent to** one, so you get grouped in.
- **Noise point:** not a core, and not within $\varepsilon$ of any core. Nobody's crowd. Marked -1 (or similar) and left unassigned.

**Reachability — How Clusters Grow:**

- **Directly density-reachable:** $q$ is a core, and $p$ is within $\varepsilon$ of $q$. One hop. Note this is **asymmetric** — a border point cannot pull in a core.
- **Density-reachable:** a chain of core points links $p$ to $q$. Think: $p$ is within reach of core $r$, $r$ is within reach of core $s$, and so on to $q$.
- **Density-connected:** $p$ and $q$ are both density-reachable from some third point $o$. Symmetric relation — used to tie together border regions of the same cluster.

The cluster grows via **breadth-first expansion** from core seeds: mark all core's $\varepsilon$-neighbors, and for any that are also cores, add their neighbors recursively.

**The Algorithm (3 sentences):**
1. Find all core points — every point with ≥ MinPts neighbours within $\varepsilon$
2. Build clusters — breadth-first from every unvisited core point: mark all $\varepsilon$-neighbours as in the cluster; for each that is also core, add THEIR $\varepsilon$-neighbours too
3. Mark leftovers — any point not reached from a core = noise

**Key properties:**
- **No K needed** — discovers clusters automatically
- Finds **any shape** (even rings, spirals)
- Outliers → **marked as noise** automatically
- **$\varepsilon$ and MinPts are hand-picked** — the catch

**BIRCH comparison:** DBSCAN is exact but needs full data in memory and pairwise neighbors. BIRCH (next section) summarizes data in a CF-tree for large/sparse data but introduces approximation. BIRCH has **Phases 1-4**: build CF-tree → optional condense → global clustering on leaf centroids → reassign raw points.

---

## Week 12 (continued) — BIRCH: The Warehouse Clipboard (Scalable Clustering)

**The story:** You cannot fit every package in the warehouse to measure pairwise distances. Instead, you maintain a **running summary** of each micro-cluster: count, linear sum, sum of squares — enough statistics to compute **centroid** and **radius** without storing every point. **BIRCH** builds a **CF-tree** (Clustering Feature tree): a height-balanced tree where each leaf entry holds a **subcluster summary** (CF) within a **radius threshold**, respecting memory.

- New point? Navigate the tree, find the leaf entry whose centroid is closest; if it still fits the **threshold**, absorb into that CF; else split/add leaf, maybe rebuild.
- After the tree, optional **global clustering** (e.g. run k-means on leaf centroids) can polish.

**Clustering Feature (CF) = The Three Numbers That Replace Thousands of Points:**

A CF is just three numbers: **N** (count), **LS** (linear sum of all points), **SS** (sum of squared norms). From these you can compute:
- **Centroid:** LS / N
- **Radius:** how spread out the micro-cluster is, derived from SS and LS
- **Merging two CFs:** just add N+N, LS+LS, SS+SS — instant, no raw points needed

This is the magic: you can merge or compare micro-clusters without ever storing a single raw point.

**CF-Tree Structure — The Height-Balanced Index of Summaries:**

- **Root and internal nodes:** store aggregated CF summaries of their children — enough to route a new point down the tree.
- **Leaf nodes:** hold CF entries, each summarizing a micro-cluster within a **threshold T** (radius/diameter constraint).
- **Branching factor B:** max children per node — controls tree width vs depth.
- **Threshold T:** max allowable radius of any leaf CF — too large → under-segmented; too small → huge tree.

**Insert flow:** point arrives → navigate from root, always choosing child whose centroid is closest → reach leaf → try to absorb into closest CF (update N, LS, SS) if still within T → else create new CF entry; if leaf overflows, split and propagate up like a B+ tree.

| Story | BIRCH Term |
|-------|------------|
| Summary stats instead of all rows | **Clustering Feature (CF) = (N, LS, SS)** |
| Hierarchical index of summaries | **CF-tree** |
| "Still compact enough?" | **Threshold** / **T** |
| Leaf summaries as micro-clusters | **CF entries** in leaves |
| Merge two clusters without raw data | **CF additivity** |

> **BIRCH = stream huge data through a tree of compact summaries, then refine if needed.**

**End-to-end flow:**
1. **Phase 1:** incrementally build CF-tree (single scan, or few)
2. **Phase 2:** optional condense/rebalance
3. **Phase 3:** global clustering on leaf CF centroids (e.g. k-means)
4. **Phase 4:** second pass — assign every original point to nearest final centroid

**Key properties / pitfalls:**
- Built for **large** or streaming-ish data where $O(n^2)$ distance matrices hurt.
- Each raw point touched **twice** max — not $O(n^2)$.
- **Order-sensitive:** different input order → different tree → possibly different micro-clusters.
- Still sensitive to **parameter** choices (branching factor, threshold T) — not a magic auto-clusterer.
- At the micro-cluster level, still assumes roughly **spherical** clusters (radius threshold).

---

## K-Means vs DBSCAN vs BIRCH

| | K-Means | DBSCAN | BIRCH |
|--|---------|--------|-------|
| Clusters | You pick K upfront | Algorithm discovers them | Algorithm discovers (on leaf summaries) |
| Shape | Assumes spherical | Finds **any shape** | Assumes spherical at micro level |
| Outliers | Forced into nearest | Marked **noise** | Absorbed into micro-clusters or left |
| Memory | All points | All points | **Summaries** (CF) — much smaller |
| Speed | $O(n \cdot k \cdot iter)$ | $O(n^2)$ naive; better with index | $O(n)$ to build tree |
| Parameters | $k$ | $\varepsilon$, MinPts | Branching factor, threshold T |

**When to use:**
- You know number of clusters + spherical → **K-Means**
- You don't know how many / clusters are weird shapes → **DBSCAN** (if data fits in memory)
- Data is massive / streaming → **BIRCH** first, then refine
- Data has clear noise/outliers → **DBSCAN** (algorithm explicitly labels noise)

DBSCAN can find a ring-shaped cluster. K-Means will always force it into overlapping spheres. That's massive.

---

## Week 13 — The Market Basket Detective (Association Rules)

**The story:** You run a grocery store. You have **10,000 receipts** from last week. You notice something: customers who buy **bread and butter** together seem to also buy **jam** more often than you'd expect by chance. Not a rule written down in the corporate playbook — discovered from the **co-occurrence pattern** in the transaction logs. That's **association rule mining**: finding rules not from physics or logic, but from **frequency of joint appearances**.

**Transaction format:** each row is a basket (receipt), each column is an item (present or absent). You don't care about quantities for basic rules — just **was it bought or not?** The data is binary transaction data.

**The two-step mining pipeline:**

1. **Find frequent itemsets** — groups of items that appear together in enough transactions (above a **minSupp** threshold). These are the raw material.
2. **Generate rules** from each frequent itemset — split it into antecedent $X$ and consequent $Y$; measure rule quality with **support**, **confidence**, and **lift**.

**Support — How Often Does This Actually Happen?**

$$\text{supp}(X) = \frac{\# \text{transactions containing } X}{\text{total transactions}}$$

If milk appears in 3,000 of 10,000 transactions, support = 0.30 (30%). This is the **baseline popularity** of an item or itemset. A rule needs to beat this baseline to be interesting.

**Confidence — When X Shows Up, How Often Does Y Show Up Too?**

$$\text{conf}(X \Rightarrow Y) = \frac{\text{supp}(X \cup Y)}{\text{supp}(X)}$$

This is **conditional probability** in empirical form: $P(Y | X)$. Of all transactions containing $X$, what fraction also contain $Y$?

Example: `{bread, butter} → {jam}` appears together in 600 transactions. `{bread, butter}` appears in 1000 transactions. Confidence = 600/1000 = 60%. Meaning: 60% of baskets with bread and butter also had jam.

**Lift — How Much Better Is This Rule Than Random Chance?**

$$\text{lift}(X \Rightarrow Y) = \frac{\text{conf}(X \Rightarrow Y)}{\text{supp}(Y)}$$

Compare the rule's confidence to the baseline rate of $Y$ appearing. If jam appears in 30% of all transactions (supp(jam)=0.30), and the rule `{bread, butter} → jam` has confidence 60%:

lift = 0.60 / 0.30 = 2.0

Interpretation: buying bread and butter makes customers **twice as likely** to buy jam than the average customer. Lift > 1 means positive association; lift < 1 means substitution effect.

**Why lift matters:** a rule can have high confidence but still be uninteresting if the consequent is just naturally common. High confidence + low lift = the consequent was going to sell anyway.

| Story | AR term |
|-------|---------|
| Receipt / shopping basket | **Transaction** |
| Items appearing together | **Itemset** |
| Appears in ≥ minSupp fraction | **Frequent itemset** |
| "Bread and butter, then jam" | **Rule** $X \Rightarrow Y$ |
| Fraction of all transactions | **Support** (popularity) |
| Of X-transactions, how many also have Y | **Confidence** (conditional probability) |
| Lift > 1 = positive association | **Lift** (vs baseline randomness) |

> **Association rules = finding "if X, then Y" not from logic but from co-occurrence frequency in transaction logs.**

**The Apriori Principle — The Anti-Monotonicity Shortcut:**

If an itemset is **infrequent**, every **superset** of it (adding more items) is also infrequent. Reason: adding items makes the set **harder** to appear in a transaction — support can only go down, never up.

Contraposition for pruning: if `{bread}` is infrequent, you can **immediately discard** all candidates containing bread — `{bread, butter}`, `{bread, milk}`, `{bread, butter, milk}`, everything. You never even count them.

This is the core insight that makes Apriori run: by checking small itemsets first and pruning supersets aggressively, you avoid counting the exponential $2^d$ possible itemsets naively.

**The Apriori Algorithm — Level by Level Up the Itemset Size:**

1. **k = 1:** scan all transactions, count each single item, keep those above minSupp → $F_1$ (frequent 1-itemsets)
2. **Generate $C_{k+1}$:** join $F_k$ with $F_k$ on items that differ only in the last element (standard join condition), then **prune** any candidate whose any (k-1)-subset is NOT in $F_{k-1}$ (that's the Apriori property check)
3. **Scan** all transactions to count support of every candidate in $C_{k+1}$ → keep survivors above minSupp → $F_{k+1}$
4. **Repeat** until $F_k$ is empty or no candidates generated

**The join step:** to make a (k+1)-itemset candidate from two k-itemsets, they must share k-1 items. Example: `{a,b,c}` and `{a,b,d}` join to `{a,b,c,d}`. The join only works if the first k-1 items are identical.

**The prune step:** before counting, discard any candidate containing a subset that wasn't frequent. E.g., if `{a,b}` is not in $F_2$, then `{a,b,c}` and `{a,b,d}` are both pruned — never scanned.

**After frequent itemsets — rule generation:** For each frequent itemset $Z$, generate rules $X \Rightarrow Z \setminus X$ for all non-empty $X \subset Z$. Keep those above minConf. Confidence = supp(Z) / supp(X). All rules from the same $Z$ share the same support (that of $Z$) but differ in confidence.

| Story | Apriori term |
|-------|-------------|
| Drop anything containing an infrequent subset | **Prune** by Apriori property |
| Combine two k-itemsets sharing k-1 items | **Join** to form (k+1)-candidates |
| Size-k itemsets that survived minSupp | **$F_k$** (frequent k-itemsets) |
| Candidate itemsets before support test | **$C_k$** (candidate k-itemsets) |
| Level 1 items → pairs → triples | **Level-wise** generation |
| Count transactions for every candidate | **Scan** the database |

> **Apriori = start with frequent singles, build pairs, prune anything containing an infrequent subset, scan, grow, repeat until nothing survives.**

**Key properties / pitfalls:**
- **Anti-monotonicity** is the computational key — without it, enumeration is $O(2^d)$.
- **Multiple DB scans** are the bottleneck — FP-growth addresses this with a prefix-tree that stores transaction paths compactly.
- **Lift** is essential alongside confidence — high confidence rules can still be trivial if the consequent is universally common.
- **minSupp** trades recall vs noise: low threshold → many itemsets (including spurious); high threshold → may miss interesting but rarer patterns.
- Association ≠ causation: just because bread and jam co-occur doesn't mean buying one causes buying the other.



---

## High-Yield Comparisons (One Glance)

| Fork | Left | Right |
|------|------|-------|
| Output type | **Classification** (label) | **Regression** (number) |
| Error view | **Train** (seen) | **Test** (unseen) |
| Positive alarms | **Precision** (trust when you say +) | **Recall** (catch real +) |
| Ensembles | **Bagging / RF** (parallel, variance) | **Boosting** (sequential, fix mistakes) |
| Clustering | **K-means** (known $k$, globes) | **DBSCAN** (density shapes, noise) |
| Models | **Decision tree** (nested splits) | **Rule list** (explicit IF-THEN) |

---

## Exam Traps — The Haunted Lab Tour

**The story:** You inherit a lab full of shortcuts that **look** successful. Each room is a trap.

- **Leakage:** training peeks at test information (preprocess on all data before split, future columns smuggled in). The model **cheats** the exam.
- **Distance without scaling:** kNN and k-means inherit distorted geometry — one giant feature becomes a tyrant.
- **Accuracy on imbalance:** everyone-negative classifier still "accurate." Switch to precision/recall or cost-aware metrics.
- **Random Forest vs bagging:** RF needs **feature randomness** per split — not identical to "many bagged trees default."
- **Boosting parallelism:** sequential stages are **not** trivially parallel like bagging.
- **K-means always outputs** something even if $k$ is wrong — **validate** structure; DBSCAN still needs **tuned** $\varepsilon$, MinPts.
- **Association rules:** confidence without **lift** can praise trivially popular consequents.

> **If the metric feels too good, ask who leaked, who was scaled, and whether the rare class was heard.**

---

## Week 9 — The Herding Problem (Clustering)

**The story:** No one told you how many tables to set at this dinner party. You just have to watch who gravitates toward whom and form natural groups. That's **clustering** — finding structure without being told the answer.

**K-Means Algorithm Steps**

```
1. Initialize K centroids randomly
2. Assign each point to nearest centroid (Euclidean distance)
3. Recalculate each centroid = mean of assigned points
4. Repeat step 2 & 3 until convergence (no point switches)
```

**Convergence = local minimum reached.** Since initialization is random, run K-Means multiple times and pick the run with lowest within-cluster sum of squares (WCSS).

---

### K-Means vs DBSCAN

| | K-Means | DBSCAN |
|--|--|--|
| Number of clusters | Must specify $k$ | Discovered automatically |
| Cluster shape | Spherical / globular | Arbitrary shapes |
| Outliers | Gets forced into a cluster | Labeled as noise (-1) |
| Sensitivity | Sensitive to initialization | Sensitive to $\varepsilon$, MinPts |

DBSCAN can find a ring-shaped cluster. K-Means will always force it into overlapping spheres. That's massive.

**When to use:**
- You know number of clusters → **K-Means**
- You don't know how many / clusters are weird shapes → **DBSCAN**
- Data has clear noise/outliers → **DBSCAN**
