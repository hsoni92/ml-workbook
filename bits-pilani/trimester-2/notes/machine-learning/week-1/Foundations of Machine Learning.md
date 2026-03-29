# Foundations of Machine Learning – Machine Learning (Module 1)

## Learning Objectives

By the end of this video you will:

1. **Define** Machine Learning and its relationship to Data Science and Artificial Intelligence.
2. **Identify** the key stages of a standard Machine Learning workflow (KDD, CRISP-DM).
3. **Recognize** why ML is needed: data abundance vs. knowledge scarcity.
4. **Describe** the evolution from empirical → theoretical → computational → data science age.
5. **List** data types used in ML: structured, unstructured/semi-structured, time series, stream data.

---

## Why Do We Need Machine Learning?

### Data Everywhere, Knowledge Scarce

- **Physical → Digital**: Many real-world processes are now digital (photos, shopping, search, trading). This generates huge volumes of data.
- **Storage has grown**: From small disks (e.g. 6–8 GB in 2000) to phones with 128 GB and systems with petabytes. Data can be stored and processed.
- **Paradox**: We are **drowning in data** but **starving for knowledge**. Asking relevant questions (e.g. “Which stock to buy?”, “How many orders are fake?”) often does not yield good answers from raw data.
- **Role of ML**: Extract patterns and knowledge from massive data automatically, so we can answer such questions.

### Evolution of Data and Science (Historical View)

| Era | Period | Focus |
|-----|--------|--------|
| **Empirical science** | Before ~1600 | Ideas from observation (e.g. sun rises in east, sets in west). |
| **Theoretical science** | ~1600–1950s | Mathematical models and generalizations from observations. |
| **Computational science** | ~1950s–1990s | Limited computers; simulations and more complex models. |
| **Data science / ML** | Today | High compute + storage + connectivity; algorithms **learn patterns from data** instead of only hand-written rules. |

---

## What Is Machine Learning?

**Definition:** Machine Learning is a field of study that gives computers the ability to **learn from data without being explicitly programmed**.

- We do **not** hand-code all rules. The system **discovers** patterns and rules from data.
- ML has roots in **data mining**: extracting useful, previously unknown knowledge from large datasets.
- In ML we discover meaningful patterns **automatically or semi-automatically**.

---

## The Machine Learning Pipeline (High-Level)

1. **Data + Questions** — Start with data and the question we want to answer (e.g. “Will it rain tomorrow?”).
2. **Data selection** — Choose a subset of data relevant to the question (full data can be costly, slow, noisy).
3. **Data pre-processing** — Clean, transform, remove noise, handle missing values, etc.
4. **ML / data mining** — Run algorithms on the prepared data.
5. **Interpretation & evaluation** — Use performance metrics and tools to interpret results.
6. **Knowledge** — If we can answer the original question from this knowledge, the pipeline is successful; otherwise we revisit earlier stages.

> **Exam tip:** Pipeline success = ability to answer the question you started with. If not, fix one or more stages (e.g. algorithm, data selection, cleaning).

---

## Origins of Machine Learning

ML is **multidisciplinary**. It uses ideas from:

- **Statistics & AI** — Theory and prediction.
- **Pattern recognition** — Detecting structure in data.
- **Database systems** — Storing and accessing large data.

---

## Machine Learning Workflows

ML is **not** “run one algorithm.” It is a **multi-step process**. Two standard frameworks:

### 1. KDD (Knowledge Discovery in Databases)

| Stage | Activity |
|-------|----------|
| 1 | **Raw data** — Gather and store data (e.g. weather: date, temperature, humidity, wind). |
| 2 | **Data integration & cleaning** — Merge sources, clean, preprocess; build a **data warehouse**. |
| 3 | **Data selection** — From the warehouse, select **task-relevant data**. |
| 4 | **Data mining / ML** — Apply algorithms to find patterns. |
| 5 | **Pattern evaluation** — Measure quality of extracted patterns. |
| 6 | **Knowledge** — Final, actionable insights; check if original questions are answered. |

### 2. CRISP-DM (Industry Framework)

| Stage | Activity |
|-------|----------|
| 1 | **Business understanding** — Data, prior knowledge, questions. |
| 2 | **Data preparation** — Integrate and prepare data (integration, cleaning). |
| 3 | **Modeling** — Select and apply ML algorithms to build models. |
| 4 | **Evaluation** — Apply model on new data and evaluate performance. |
| 5 | **Deployment / knowledge** — Use model and insights; verify that questions are answered. |

### Business Intelligence View (Alternative 5-Step View)

1. Data sources → 2. Pre-processing (integration, warehousing) → 3. Data exploration → 4. ML/data mining → 5. Presentation & decisions.

---

## Data Types in Machine Learning

| Type | Description | Examples |
|------|-------------|----------|
| **Structured** | Arranged and stored in a fixed structure | Tabular data, graphs (as structured representations). |
| **Unstructured / semi-structured** | No strict schema | News articles, web pages. Often converted to structured form before ML. |
| **Time series** | Values over time | Sensor logs, stock prices. |
| **Advanced** | Special handling | **Stream data** (real-time, e.g. IoT), **socio-temporal**, **spatial** data. |

---

## Summary

- **Why ML:** Lots of data, good storage and compute, but we need **knowledge**; ML extracts patterns from data.
- **What is ML:** Learning from data **without explicit programming**; evolved from data mining.
- **Pipeline:** Data + question → selection → pre-processing → ML → evaluation → knowledge.
- **Workflows:** KDD and CRISP-DM describe full lifecycle from raw data to knowledge.
- **Data types:** Structured, unstructured/semi-structured, time series, and stream/advanced types.

Use this note for definitions, pipeline stages, and exam-style questions on “why ML” and “what is ML.”
