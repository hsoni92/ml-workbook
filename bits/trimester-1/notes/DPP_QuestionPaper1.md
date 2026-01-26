# Data Preprocessing — Comprehensive Test (Sample)

**BITS Digital**
**First Semester 2025–2026**
**Comprehensive Test**

## Exam details

| Field | Value |
|---|---|
| Course No. |  |
| Course Title | Data Preprocessing |
| Nature of Exam | Closed Book (No Internet) |
| Weightage | 40% |
| Duration | 2.5 Hours |
| Date of Exam |  |

## Note to students

1. Please follow all the *Instructions to Candidates* given on the cover page of the answer book.
2. Read each question carefully and write a to-the-point answer.
3. All parts of a question should be answered consecutively. Each answer should start from a fresh page.
4. Assumptions made (if any) should be stated clearly at the beginning of your answer.
5. Show all calculations/derivations neatly and box/highlight the final answer.

---

## Q1

### Q1.1 (5 marks)

Explain the difference between **interval attribute** and **ratio attribute**. Provide one example for each.

**Answer**

- **Interval attribute**: Numeric scale where **differences are meaningful** but there is **no true (absolute) zero**. Ratios like “twice as much” are not meaningful.
  - **Example**: Temperature in **°C** or **°F** (0°C doesn’t mean “no temperature”).
- **Ratio attribute**: Numeric scale where both **differences and ratios are meaningful** because there is a **true zero**.
  - **Example**: **Weight** in kg, **height** in cm, **age** in years (0 kg means no weight).

**Key concept**: In data preprocessing/statistics, ratio data supports all arithmetic operations (including meaningful division), while interval data supports addition/subtraction but not meaningful ratio comparisons.

### Q1.2 (5 marks)

Explain the difference between **stratified sampling** and **cluster sampling**, with an example for each.

**Answer**

- **Stratified sampling**: Split the population into **homogeneous strata** (subgroups) based on an important attribute, then **sample from every stratum** (often proportionally). Goal: **reduce variance** and ensure representation of each subgroup.
  - **Example**: University has 60% UG and 40% PG students. For a sample of 100, take **60 UG + 40 PG** (random within each group).
- **Cluster sampling**: Split the population into **clusters** that are each a “mini-population” (often heterogeneous), then **randomly select some clusters** and survey **all units** in those clusters (or sample within selected clusters). Goal: **reduce cost/logistics**.
  - **Example**: Choose 5 random classrooms (clusters) and survey all students in those classrooms.

**Rule of thumb**: Stratified = sample **from all groups**; Cluster = sample **some groups entirely**.

---

## Q2

### Q2.1 (5 marks)

Which one should be handled first in data mining?

a. Remove noise and then outliers
b. Remove outliers and then noise

Justify your answer.

**Answer**

In most practical pipelines, **handle noise first, then detect/handle outliers**.

- **Why**:
  - **Noise** (random error, measurement glitches, typos) can **create fake outliers** or distort distributions.
  - Many outlier detectors rely on **distance, density, or distribution**; noisy data shifts these statistics and reduces detector reliability.
  - After smoothing/denoising (e.g., binning, regression smoothing, moving averages, robust filters), true outliers often become clearer.

- **Exception (when outliers first can help)**:
  - If outliers are **gross errors** (e.g., impossible values like negative age) that break downstream cleaning/normalization, removing them early may be necessary.

**Concept**: Think “improve signal quality” (noise reduction) before “find rare signals” (outliers), unless the outliers are clearly invalid and disruptive.

### Q2.2 (5 marks)

Assume students have obtained the following marks:

`10, 15, 20, 25, 30`

a. Compute the z-score for each student using z-score normalization.
b. Identify which students have scores within \( \pm 0.5 \) standard deviations of the mean.

**Answer**

Let the marks be \(x = \{10, 15, 20, 25, 30\}\).

- **Mean**:
  \[
  \mu = \frac{10 + 15 + 20 + 25 + 30}{5} = \frac{100}{5} = 20
  \]

- **Population standard deviation** (common in normalization; if you use sample SD, z-scores change slightly):
  \[
  \sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{n}} =
  \sqrt{\frac{( -10)^2 + (-5)^2 + 0^2 + 5^2 + 10^2}{5}}
  = \sqrt{\frac{100 + 25 + 0 + 25 + 100}{5}}
  = \sqrt{50}
  \approx 7.071
  \]

- **Z-score formula**:
  \[
  z_i = \frac{x_i - \mu}{\sigma}
  \]

| Marks \(x_i\) | \(x_i - \mu\) | \(z_i\) |
|---:|---:|---:|
| 10 | -10 | \(-10/7.071 \approx -1.414\) |
| 15 | -5 | \(-5/7.071 \approx -0.707\) |
| 20 | 0 | \(0\) |
| 25 | 5 | \(5/7.071 \approx 0.707\) |
| 30 | 10 | \(10/7.071 \approx 1.414\) |

- **Within \( \pm 0.5\sigma \)** means \(z \in [-0.5, 0.5]\).
  - Only **20** has \(z = 0\) (within the range).

**Concept**: z-score normalization converts values into “how many standard deviations from the mean,” enabling fair comparisons across different scales.

---

## Q3

### Q3.1 (3 marks)

Forward selection (attribute subselection method) is a **lossy** or **lossless** reduction technique? Justify your answer.

**Answer**

**Lossy.** Forward selection picks a **subset of features** and discards the rest. Once discarded, the original dataset cannot be perfectly reconstructed from the reduced set.

**Concept**: Feature selection (forward/backward selection, filters, wrappers) is **lossy**; feature construction/extraction methods like PCA are also lossy in general, while some encodings/compressions can be lossless (rare in typical ML preprocessing).

### Q3.2 (7 marks)

Discuss the mathematical similarity and dissimilarity between the **Simple Matching Coefficient (SMC)** and the **Jaccard index**.

**Answer**

Assume two binary vectors (or sets) and define the contingency counts:

- \(M_{11}\): count where both are 1
- \(M_{00}\): count where both are 0
- \(M_{10}\): first is 1, second is 0
- \(M_{01}\): first is 0, second is 1

**Similarity measures**

- **SMC (Simple Matching Coefficient)**:
  \[
  \text{SMC} = \frac{M_{11} + M_{00}}{M_{11} + M_{00} + M_{10} + M_{01}}
  \]
  It treats **matches on 1s and matches on 0s equally**.

- **Jaccard index**:
  \[
  J = \frac{M_{11}}{M_{11} + M_{10} + M_{01}}
  \]
  It **ignores \(M_{00}\)** (co-absence) and focuses on overlap of presences (1s).

**Similarity (commonality)**

- Both are **normalized similarities** in \([0,1]\).
- Both increase with more agreement and decrease with disagreements (\(M_{10}, M_{01}\)).

**Key dissimilarity (when to use which)**

- **SMC is appropriate** when **0 and 1 are equally informative** (e.g., answers to a questionnaire where “No” is meaningful).
- **Jaccard is appropriate** for **sparse binary data** where **1 indicates presence** and 0 is “absence/unknown/uninteresting” (e.g., market-basket items, keywords in documents).

**Dissimilarity versions**

- \(d_{\text{SMC}} = 1 - \text{SMC}\)
- \(d_J = 1 - J\)

---

## Q4 (10 marks)

Given the set `{8, 15, 49, 3, 24, 2, 36, 11, 1, 42, 4, 50}`, perform data transformation using:

a. Mean binning with a total of 3 bins
b. Boundary binning with a total of 3 bins
c. Min–max normalization
d. Decimal scaling

**Answer**

First, **sort** the data:

`1, 2, 3, 4, 8, 11, 15, 24, 36, 42, 49, 50`

With 12 values and **3 bins**, use **equal-depth binning** (4 values per bin):

- **Bin 1**: \( \{1, 2, 3, 4\} \)
- **Bin 2**: \( \{8, 11, 15, 24\} \)
- **Bin 3**: \( \{36, 42, 49, 50\} \)

### (a) Mean binning (3 bins)

Replace each value by the **mean of its bin**.

- Bin 1 mean: \( (1+2+3+4)/4 = 2.5 \)
- Bin 2 mean: \( (8+11+15+24)/4 = 58/4 = 14.5 \)
- Bin 3 mean: \( (36+42+49+50)/4 = 177/4 = 44.25 \)

**Transformed (in sorted order)**:

`2.5, 2.5, 2.5, 2.5, 14.5, 14.5, 14.5, 14.5, 44.25, 44.25, 44.25, 44.25`

### (b) Boundary binning (3 bins)

Replace each value by the **nearest boundary** (min or max) of its bin.

- Bin 1 boundaries: 1 and 4
  - \(1 \to 1\), \(2 \to 1\) (tie can go to lower), \(3 \to 4\), \(4 \to 4\)
- Bin 2 boundaries: 8 and 24
  - \(8 \to 8\), \(11 \to 8\), \(15 \to 8\) (tie/closer), \(24 \to 24\)
- Bin 3 boundaries: 36 and 50
  - \(36 \to 36\), \(42 \to 36\), \(49 \to 50\), \(50 \to 50\)

**Transformed (in sorted order)**:

`1, 1, 4, 4, 8, 8, 8, 24, 36, 36, 50, 50`

### (c) Min–max normalization

Normalize to \([0, 1]\) using:
\[
x' = \frac{x - \min(x)}{\max(x) - \min(x)}
\]
Here, \(\min = 1\), \(\max = 50\), range \(= 49\).

Some normalized values (rounded to 4 decimals):

- \(1 \to 0\)
- \(2 \to \frac{1}{49} \approx 0.0204\)
- \(3 \to \frac{2}{49} \approx 0.0408\)
- \(4 \to \frac{3}{49} \approx 0.0612\)
- \(8 \to \frac{7}{49} \approx 0.1429\)
- \(11 \to \frac{10}{49} \approx 0.2041\)
- \(15 \to \frac{14}{49} \approx 0.2857\)
- \(24 \to \frac{23}{49} \approx 0.4694\)
- \(36 \to \frac{35}{49} \approx 0.7143\)
- \(42 \to \frac{41}{49} \approx 0.8367\)
- \(49 \to \frac{48}{49} \approx 0.9796\)
- \(50 \to 1\)

### (d) Decimal scaling

Choose \(j\) such that \(\max(|x'|) < 1\) for:
\[
x' = \frac{x}{10^j}
\]
Here \(\max(x)=50\). Take \(j = 2\) (since \(50/10^2 = 0.50 < 1\)).

**Transformed values** (in original order):

`0.08, 0.15, 0.49, 0.03, 0.24, 0.02, 0.36, 0.11, 0.01, 0.42, 0.04, 0.50`

**Concept**: Binning reduces noise (smoothing). Min–max rescales to a target range. Decimal scaling rescales by powers of 10 and is simple but less adaptive than min–max.

---

## Meta

- **No. of Pages**: 1
- **No. of Questions**: 7