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

## Week 6 — The Student Who Studies Only on Exam Day (kNN)

**The story:** **Eager learners** cram a compact model early. **Lazy learners** like **k-nearest neighbors (kNN)** keep the whole training set and only "think" at prediction time: find the **k** closest training points in feature space and **vote** (classification) or average (regression).

- **Small k:** wiggly, local, **sensitive to noise**. **Large k:** smoother, more **bias**, may wash out local structure.
- **Distance metric** and **feature scaling** define what "near" means — unscaled features distort neighborhoods.

| Story | ML term |
|-------|---------|
| No model until query time | **Lazy** learning |
| Closest classmates vote | **kNN** decision |
| Few voters | Small **k** (flexible, noisy) |
| Many voters | Large **k** (smooth, biased) |
| Same measuring cups for every feature | **Normalize** before distance |

> **kNN = democracy of proximity — redraw the map if you change scales.**

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

| Story | ML term |
|-------|---------|
| Daily merger diary | **Dendrogram** |
| Start alone, merge up | **Agglomerative** |
| Start one blob, split down | **Divisive** |
| Where you chop the diary | **Cut height** ↔ number of clusters |
| Definition of "closest groups" | **Linkage** rule |

> **Hierarchical clustering = build a merge tree first, decide K later by where you cut.**

**Key properties / pitfalls:**
- No upfront $k$ required to **build** the tree — but you still choose a cut.
- **Scalability:** naive agglomerative methods can be costly on huge $n$; BIRCH (Week 12) addresses big data differently.

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

**Key properties:**
- **No K needed** — discovers clusters automatically
- Finds **any shape** (even rings, spirals)
- Outliers → **marked as noise** automatically
- **$\varepsilon$ and MinPts are hand-picked** — the catch

**Core / Border / Noise:**
- **Core point:** ≥ MinPts within $\varepsilon$ → dense enough to form a cluster
- **Border point:** fewer than MinPts, but IS within $\varepsilon$ of a core point → on the edge
- **Noise point:** not a core, not near any core → loner

**The Algorithm (3 sentences):**
1. Find all core points — every point with ≥ MinPts neighbours within $\varepsilon$
2. Build clusters — breadth-first from every unvisited core point: mark all $\varepsilon$-neighbours as in the cluster; for each that is also core, add THEIR $\varepsilon$-neighbours too
3. Mark leftovers — any point not reached from a core = noise

---

## Week 12 (continued) — BIRCH: The Warehouse Clipboard (Scalable Clustering)

**The story:** You cannot fit every package in the office to measure pairwise distances. Instead, you maintain a **running summary** of each micro-cluster: count, linear sum, sum of squares — enough statistics to compute **centroid** and **radius** without storing every point. **BIRCH** builds a **CF-tree** (Clustering Feature tree): a height-balanced tree where each leaf entry holds a **subcluster summary** (CF) within a **radius threshold**, respecting memory.

- New point? Navigate the tree, find the leaf entry whose centroid is closest; if it still fits the **threshold**, absorb into that CF; else split/add leaf, maybe rebuild.
- After the tree, optional **global clustering** (e.g. run k-means on leaf centroids) can polish.

| Story | BIRCH Term |
|-------|------------|
| Summary stats instead of all rows | **Clustering Feature (CF)** |
| Hierarchical index of summaries | **CF-tree** |
| "Still compact enough?" | **Threshold** / **T** |
| Leaf summaries as micro-clusters | **CF entries** in leaves |

> **BIRCH = stream huge data through a tree of compact summaries, then refine if needed.**

**Key properties / pitfalls:**
- Built for **large** or streaming-ish data where $O(n^2)$ distance matrices hurt.
- Still sensitive to **parameter** choices (branching factor, threshold); not a magic auto-clusterer.

---

## K-Means vs DBSCAN

| | K-Means | DBSCAN |
|--|---------|--------|
| Clusters | You pick K upfront | Algorithm discovers them |
| Shape | Assumes spherical | Finds **any shape** |
| Outliers | Forced into nearest cluster | Marked **noise** |
| Centroids | Yes | No |
| Initialization sensitive | Yes | No (deterministic given params) |

DBSCAN can find a ring-shaped cluster. K-Means will always force it into overlapping spheres. That's massive.

**When to use:**
- You know number of clusters → **K-Means**
- You don't know how many / clusters are weird shapes → **DBSCAN**
- Data has clear noise/outliers → **DBSCAN**
- Data massive, streaming summaries → consider **BIRCH** before exact pairwise fantasies

---

## Week 13 — The Market Basket Detective (Association Rules)

**The story:** Cash registers log **transactions** (market baskets). You want rules like "if **bread and butter**, then **jam**" — not from physics, from **co-occurrence**.



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
