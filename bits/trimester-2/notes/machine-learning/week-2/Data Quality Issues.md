# Data Quality Issues – Machine Learning (Module 2)

## Learning Objectives

By the end of this video you will:

1. **Define** data quality and why it matters for ML.
2. **List** key **dimensions** to measure data quality.
3. **Describe** common data quality **problems**: noise, outliers, missing values, duplicates, inconsistency.
4. **Explain** the principle **“garbage in, garbage out.”**
5. **State** the role of **data pre-processing** as a solution.

---

## Why Data Quality Matters

- **Ideal:** Data is perfect, complete, and ready for analysis.
- **Reality:** Raw data is often **messy**, **incomplete**, and **inconsistent**.
- **Principle:** **Garbage in, garbage out (GIGO).** If we build a model (prediction or descriptive) on **low-quality data**, the results will be **low-quality or unreliable**.

---

## Definition of Data Quality

- **Data quality** = the **overall utility** of the dataset and its **fitness for the intended purpose** (e.g. building a credit-card fraud detector, answering business questions).
- **Golden rule:** Data has quality **if it satisfies the requirements of the intended user**.
- **High-quality data** correctly represents the real-world construct it is meant to represent.
- **Subjective:** The same dataset can be “high quality” for one user (e.g. R&amp;D) and “low quality” for another (e.g. delivery) depending on the questions they ask.

---

## Dimensions of Data Quality

Data quality is **multi-dimensional**. Key dimensions include:

| Dimension | Meaning |
|-----------|---------|
| **Accuracy** | Is the data **correct**? (e.g. names spelled correctly, values not wrong.) |
| **Completeness** | Is **all necessary** information present? (e.g. address fully filled.) |
| **Consistency** | Does the data **contradict** itself? (e.g. age vs date of birth mismatch.) |
| **Timeliness** | Is the data **up to date**? (e.g. current address.) |
| **Believability** | How much can we **trust** the data? |
| **Interpretability** | Can we **understand** the data easily? |

These dimensions give a **framework** to **measure** and **improve** data quality.

---

## Common Data Quality Problems

### 1. Noisy Data

- **Noise** = random **error or variance** in a measured variable; a **modification** of the true value.
- **Causes:** Faulty sensors, transmission errors, **data entry mistakes** (e.g. census, digitization), intentional misreporting.
- **Effect:** Distorts analysis and models. Like static on a phone call — the true signal is corrupted.

### 2. Outliers

- **Outliers** = data objects that are **legitimate** (real values) but **very different** from most of the other objects.
- **Not the same as noise:** Noise is **error**; outliers are **extreme but true** values.
- **Two roles:**
  - **Nuisance:** They can **distort** statistics (e.g. average) and models. Example: values 1, 2, 3, 4, 100 → average 22; without outlier, average 2.5.
  - **Goal:** Sometimes **finding** outliers is the objective (e.g. **credit card fraud**, **intrusion detection** — the “bad” cases are rare and outlier-like).

### 3. Missing Values

- Some **values are absent** (empty fields).
- **Causes:** Information not collected, attribute not applicable, equipment failure, human oversight.
- **Effect:** Incomplete records; many algorithms cannot handle missing values directly — we must **handle** them (e.g. impute, remove, or model).

### 4. Duplicate Data

- Two (or more) **records or attributes** are **same or nearly same**.
- **Common when:** Merging data from **multiple sources** without careful deduplication.
- **Effect:** Redundancy, biased counts, and wasted storage; can distort statistics and models.

### 5. Inconsistent Data

- Data **contradicts** itself (e.g. age 25 but date of birth implies 30).
- **Effect:** Unreliable conclusions; we need rules and checks to enforce consistency.

---

## Real-World Reality and Pre-Processing

- In practice, data is often **incomplete**, **noisy**, **inconsistent**, and may contain **outliers** and **duplicates**.
- **Consequence:** Bad business decisions, loss of trust, waste of time and resources.
- **Solution:** **Data pre-processing** — a set of steps to **improve** quality and **prepare** data for the next stages (e.g. modeling).
- **Goals of pre-processing:**
  1. **Improve quality** — handle noise, missing values, outliers, inconsistency, duplicates.
  2. **Make data fit the model** — structure and transform data so it is suitable for the chosen ML/data mining algorithm.

---

## Summary

- **Data quality** = fitness for intended use; measured by accuracy, completeness, consistency, timeliness, believability, interpretability.
- **Common problems:** Noise (error), outliers (extreme but real), missing values, duplicates, inconsistency.
- **GIGO:** Poor data → poor model and poor decisions.
- **Pre-processing** is the main way we address quality issues before building models.

Use this note for exam questions on “what is data quality,” “dimensions of quality,” and “common data quality problems.”
