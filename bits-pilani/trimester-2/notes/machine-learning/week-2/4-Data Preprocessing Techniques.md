# Data Preprocessing Techniques – Machine Learning (Module 2)

## Learning Objectives

By the end of this video you will:

1. **List** the four major **tasks** of data pre-processing: cleaning, integration, transformation, reduction.
2. **Describe** how to handle **missing values** and **noisy data**.
3. **Explain** **data integration** issues (e.g. entity identification, value conflicts, redundancy).
4. **Describe** **normalization** (min-max, z-score) and **aggregation**.
5. **Explain** **data reduction** (by attributes and by number of records).

---

## Why Pre-Processing?

- Real-world data is **messy**; **garbage in, garbage out**.
- Pre-processing is **not one step** but a **set of tasks** to improve quality and prepare data for ML/data mining.

---

## Four Major Categories of Pre-Processing Tasks

| Task | Purpose |
|------|---------|
| **Data cleaning** | Fix missing values, smooth noise, identify/handle outliers, resolve inconsistency. |
| **Data integration** | Merge data from multiple sources; handle conflicts and redundancy. |
| **Data transformation** | Change scale/structure (e.g. normalization, aggregation) for algorithms. |
| **Data reduction** | Reduce volume (rows/columns or both) while preserving integrity. |

---

## 1. Data Cleaning

### Handling Missing Values

- **Ignore the tuple** — drop records with missing values (simple but can lose data).
- **Fill manually** — often tedious or infeasible for large data.
- **Global constant** — replace missing with a constant (e.g. “Unknown,” “ABC”).
- **Central tendency** — for numerical attributes use **mean**, **median**, or **mode** of the attribute.
- **Conditional / model-based** — use rules (e.g. if A = 1 then fill B with 2) or a model to impute.

### Handling Noisy Data

- **Smoothing** — reduce impact of noise:
  - **Binning:** Sort data, partition into **bins**, then replace values in each bin by **bin mean**, **median**, or **boundary** (local smoothing).
  - **Regression:** Fit a regression; use fitted values as smoothed values.
  - **Outlier/cluster analysis:** Detect points outside clusters as potential noise and handle separately.

---

## 2. Data Integration

- **When:** Merging data from **multiple sources** (e.g. different DBs, departments).
- **Challenges:**
  - **Entity identification** — same real-world entity represented differently (e.g. multiple IDs for one person).
  - **Data value conflicts** — same entity with different values (e.g. “John Smith” vs “J.D. Smith,” “Hemant R” vs “H Rathaur” on different ID cards).
  - **Redundancy** — duplicate or overlapping attributes/tuples after merge.
- **Example (Aadhaar):** Government needed a single view of citizens across voter ID, passport, ration card, etc. Merging led to serious **integrity** issues; eventually a **new**, dedicated data collection (Aadhaar) was used. Integration is **tedious and error-prone**.

---

## 3. Data Transformation

- **Goal:** Convert data into a **form suitable** for mining (e.g. scale, structure), **not** primarily to fix errors.
- **Common methods:**

### Normalization

- **Why:** Avoid one attribute (e.g. income in lakhs) **dominating** distance-based or gradient-based calculations; often **speeds up** training.
- **Min-max normalization:** Map original range [min, max] to a new range [new_min, new_max]:
  - **Formula:**
    `v' = (v - min) / (max - min) * (new_max - new_min) + new_min`
  - Preserves **shape** of the distribution in the new range.
- **Z-score normalization:** Use mean and standard deviation:
  - **Formula:**
    `v' = (v - mean) / std_dev`
  - Result is in units of standard deviations from the mean.

### Aggregation

- **Combine** values to change **scale** or **granularity** (e.g. city → state → country; quarterly → yearly).
- **Benefits:** Data can become **more stable** and **less variable**; also **reduces** volume.

---

## 4. Data Reduction

- **Goal:** Obtain a **smaller** (reduced) dataset that is **representative** and **preserves** the integrity/properties of the original, so that analysis and mining are **faster** and more feasible.

### Reduction by Attributes (Dimensionality Reduction)

- **Idea:** Use fewer attributes (drop or combine).
  - **Irrelevant attributes** — not useful for the analysis (e.g. student ID for predicting GPA).
  - **Redundant attributes** — carry (almost) the same information; one can be removed.
- **Methods:** Attribute **subset selection** (e.g. forward selection, backward elimination), decision-tree-based selection, other feature selection techniques.

### Reduction by Number of Records

- **Sampling** — use a **representative sample** (e.g. simple random, stratified) so the sample behaves like the full data.
- **Histograms, clustering, aggregation** — summarize or group records to reduce count while preserving structure.

---

## End-to-End View

1. Start with **raw, messy** data.
2. **Clean** (missing values, noise, outliers, inconsistency).
3. **Integrate** carefully (entity ID, value conflicts, redundancy).
4. **Transform** (normalize, aggregate) for the algorithm.
5. **Reduce** (attributes and/or records) to a manageable, representative set.
6. Result: **higher-quality** data ready for **modeling**.

---

## Summary

- **Four task groups:** Cleaning, integration, transformation, reduction.
- **Cleaning:** Missing value strategies (ignore, constant, mean/median, model) and noise (binning, regression, outlier handling).
- **Integration:** Beware of entity identification, value conflicts, redundancy.
- **Transformation:** Normalization (min-max, z-score), aggregation.
- **Reduction:** Fewer attributes (subset selection), fewer records (sampling, histograms, clustering).

Use this note for exam questions on “steps of pre-processing” and “how to handle missing values and noise.”
