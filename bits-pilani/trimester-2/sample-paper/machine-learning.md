# BITS Digital — Comprehensive Exam (Model QP)

| Field | Details |
| --- | --- |
| Course No. | |
| Course Title | Machine Learning |
| Nature of Exam | Closed Book (No Internet) |
| Weightage | 40% |
| Duration | 2 Hours |
| Date of Exam | |

## Note to students

1. Please follow all the Instructions to Candidates given on the cover page of the answer book.
2. Read each question carefully and write to-the-point answers.
3. All parts of a question should be answered consecutively. Each answer should start from a fresh page.
4. Assumptions made, if any, should be stated clearly at the beginning of your answer.
5. Show all calculations and derivations clearly and box or highlight the final answer.

---

## Q.1

### Q.1.1

Explain the difference between **Agglomerative** and **Divisive** clustering with examples.

**Answer.** **Agglomerative** clustering is bottom-up: each observation starts as its own cluster, and the algorithm repeatedly merges the two closest clusters until one cluster remains (or until a stopping rule). Example: merging the two nearest customers by purchase similarity, then merging that group with the next closest cluster. **Divisive** clustering is top-down: all points begin in one cluster, and the algorithm recursively splits clusters (e.g., by the weakest internal link or a partition criterion) until each point is alone or a stopping rule applies. Example: splitting a document collection into broad topics first, then splitting each topic into finer subtopics.

### Q.1.2

In a dataset shaped like two concentric circles, which clustering method should be used to identify natural clusters? Justify your answer.

**[5 Marks]**

**Answer.** Use a method that does **not** assume globular, centroid-separated groups in the original feature space—e.g. **DBSCAN** (density-connected regions), **spectral clustering** (separation via graph/eigenstructure), or **kernel $k$-means** / similarity graphs. Two concentric circles are **non-convex**; **$k$-means**, **Ward**, and other Euclidean centroid methods tend to split along a line through the centers or average both rings, failing to recover the inner and outer rings.

---

## Q.2

### Q.2.1

Is feature scaling relevant for the $k$-NN classification algorithm? Justify your answer.

**[5 Marks]**

**Answer.** **Yes.** $k$-NN predicts by neighbor votes using a distance (often Euclidean). Features with larger numeric ranges dominate the distance unless **standardization** (zero mean, unit variance) or **min–max scaling** is applied, so neighbors reflect all attributes fairly.

### Q.2.2

Consider a binary classification problem where we have 50 positive examples and 50 negative examples. Compute the Gini index for this dataset. Give a short description of your interpretation of this value for this data.

**[5 Marks]**

**Answer.** Let $p_+ = 50/100 = 0.5$ and $p_- = 50/100 = 0.5$. Gini impurity is $\text{Gini} = 1 - \sum_k p_k^2 = 1 - (0.5^2 + 0.5^2) = 1 - 0.5 = 0.5$. For a binary node, $0.5$ is the **maximum** Gini—labels are as mixed as possible—so any informative split should **reduce** this value; a split that keeps a $50/50$ balance in a child leaves impurity unchanged.

---

## Q.3

Consider a dataset with the following attributes: **age** (numeric), **gender** (binary), **income** (numeric), **education level** (categorical), and **occupation** (categorical). Assume that you have generated a set of rules using a rule-based classifier. The rules are:

- **Rule 1:** If age $\leq 35$ and gender = Male and education level = Bachelor's degree, then the predicted class is Class A.
- **Rule 2:** If age $> 35$ and gender = Female and occupation = Executive, then the predicted class is Class B.
- **Rule 3:** If age $\leq 30$ and income $\geq 50000$, then the predicted class is Class A.
- **Rule 4:** If age $> 30$ and age $\leq 40$ and gender = Female, then the predicted class is Class B.
- **Rule 5:** If age $> 40$ and income $< 30000$ and education level = High school, then the predicted class is Class C.

**(a)** Calculate the coverage and accuracy for each rule. **[5 marks]**

**Answer.** For rule $R$: **coverage**$(R) = |\{x : \text{antecedent}(x)\}| / |D|$; **accuracy**$(R) = |\{x : \text{antecedent}(x) \land y = \text{predicted class}\}| / |\{x : \text{antecedent}(x)\}|$. The question does not give $|D|$ or match counts; below is an **illustrative** dataset with $|D| = 200$ (replace numbers if the exam supplies a table).

| Rule | Instances matching antecedent | Correctly classified among matches | Coverage | Accuracy |
| --- | ---: | ---: | ---: | ---: |
| 1 | 40 | 35 | $40/200 = 0.20$ | $35/40 = 0.875$ |
| 2 | 25 | 22 | $25/200 = 0.125$ | $22/25 = 0.88$ |
| 3 | 60 | 45 | $60/200 = 0.30$ | $45/60 = 0.75$ |
| 4 | 30 | 28 | $30/200 = 0.15$ | $28/30 \approx 0.933$ |
| 5 | 15 | 12 | $15/200 = 0.075$ | $12/15 = 0.80$ |

**(b)** Assess the quality of the rules based on their coverage and accuracy. **[5 marks]**

**Answer.** **Coverage vs accuracy:** high coverage with low accuracy means the rule fires often but mislabels many covered cases (noisy or overly general antecedent). Under the illustration, Rule 3 reaches many instances but is the **least** accurate—worth refining conditions or ordering it after stricter rules. Rules 2 and 4 are **narrower** but relatively **precise**. Rule 5 is specialized (low coverage), which can be acceptable for a rare but important class. **Overlap:** Rules 1 and 3 both predict Class A on different subsets; if examples satisfy both, a **rule order** or conflict-resolution policy is needed.

---

## Q.4

Cluster the following data points $(0, 4, 5, 20, 25, 39, 43, 44)$ using hierarchical agglomerative clustering with:

1. Single linkage (min)
2. Complete linkage (max)
3. Average linkage

Show the proximity matrix, calculations to merge clusters at each step, and the dendrogram.

**[10 Marks]**

**Answer.** Treat the values as one-dimensional; **proximity** is $d(x_i, x_j) = |x_i - x_j|$.

**Initial proximity matrix** (rows/columns in order $0,4,5,20,25,39,43,44$):

|  | 0 | 4 | 5 | 20 | 25 | 39 | 43 | 44 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **0** | 0 | 4 | 5 | 20 | 25 | 39 | 43 | 44 |
| **4** | 4 | 0 | 1 | 16 | 21 | 35 | 39 | 40 |
| **5** | 5 | 1 | 0 | 15 | 20 | 34 | 38 | 39 |
| **20** | 20 | 16 | 15 | 0 | 5 | 19 | 23 | 24 |
| **25** | 25 | 21 | 20 | 5 | 0 | 14 | 18 | 19 |
| **39** | 39 | 35 | 34 | 19 | 14 | 0 | 4 | 5 |
| **43** | 43 | 39 | 38 | 23 | 18 | 4 | 0 | 1 |
| **44** | 44 | 40 | 39 | 24 | 19 | 5 | 1 | 0 |

At each step, merge the pair (or pair of clusters) with **minimum** linkage distance; distances between clusters use **min** (single), **max** (complete), or **mean** (average) over cross-cluster pairs of points.

**1. Single linkage**

| Step | Merge (height) |
| --- | --- |
| 1 | $\{4\}$ and $\{5\}$ at $1$ |
| 2 | $\{43\}$ and $\{44\}$ at $1$ |
| 3 | $\{0\}$ and $\{4,5\}$ at $4$ |
| 4 | $\{39\}$ and $\{43,44\}$ at $4$ |
| 5 | $\{20\}$ and $\{25\}$ at $5$ |
| 6 | $\{39,43,44\}$ and $\{20,25\}$ at $14$ |
| 7 | $\{0,4,5\}$ and $\{20,25,39,43,44\}$ at $15$ |

**Dendrogram (single):** very close pairs $(4,5)$ and $(43,44)$ fuse first; **chaining** then connects $\{0,4,5\}$ to the rest via the smallest cross-cluster gaps, so the two main arms join at height $15$.

**2. Complete linkage**

| Step | Merge (height) |
| --- | --- |
| 1 | $\{4\}$ and $\{5\}$ at $1$ |
| 2 | $\{43\}$ and $\{44\}$ at $1$ |
| 3 | $\{0\}$ and $\{4,5\}$ at $5$ |
| 4 | $\{20\}$ and $\{25\}$ at $5$ |
| 5 | $\{39\}$ and $\{43,44\}$ at $5$ |
| 6 | $\{20,25\}$ and $\{39,43,44\}$ at $24$ |
| 7 | $\{0,4,5\}$ and $\{20,25,39,43,44\}$ at $44$ |

**Dendrogram (complete):** same tiny merges first; larger merges wait until the **worst** within-group pair allows it, so the final merge is at **$44$** (diameter across the left and right groups).

**3. Average linkage**

| Step | Merge (height) |
| --- | --- |
| 1 | $\{4\}$ and $\{5\}$ at $1$ |
| 2 | $\{43\}$ and $\{44\}$ at $1$ |
| 3 | $\{0\}$ and $\{4,5\}$ at $4.5$ |
| 4 | $\{39\}$ and $\{43,44\}$ at $4.5$ |
| 5 | $\{20\}$ and $\{25\}$ at $5$ |
| 6 | $\{0,4,5\}$ and $\{20,25\}$ at $19.5$ |
| 7 | $\{39,43,44\}$ and $\{0,4,5,20,25\}$ at $31.2$ |

**Dendrogram (average):** between single and complete—local tight pairs merge early; the **middle** block $\{20,25\}$ joins $\{0,4,5\}$ before the high-$39/43/44$ group attaches to that larger cluster.
