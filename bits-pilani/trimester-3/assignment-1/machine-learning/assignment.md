# Assignment — Design and Build a Mini Production ML System

| Field | Detail |
| --- | --- |
| **Weightage** | 28% of course grade |
| **Team** | Individual or pairs (your choice; instructions below are phrased for individual work but apply to pairs too) |
| **Time window** | 2 weeks |

---

## 1. Problem & Scenario

Pick one ML use case:

- **Binary classification** — e.g., churn, fraud, conversion prediction
- **Regression** — e.g., demand / price prediction
- **Ranking / recommendation** — a simple ranking or recommendation task

You may reuse a dataset from earlier labs or pick any public dataset.

You will **not** be graded on beating state-of-the-art accuracy.

You **will** be graded on:

- How well you apply the production ML concepts from M1–M10
- Code structure, reproducibility, and documentation
- Clear reasoning about trade-offs and design choices

---

## Deliverables

Submit the following:

### Code repository (zipped or link)

- Training pipeline
- Inference service (FastAPI or similar)
- Simple data ingestion script (batch / micro-batch)
- Basic tests and configs

### Short design document (4–6 pages or ~1500–2000 words)

Cover:

1. Problem definition and metrics
2. Data and feature design
3. Model choice and evaluation
4. Serving and inference pattern
5. Data pipeline and retraining strategy
6. Monitoring plan and basic alerts
7. Key trade-offs, limitations, and future work

### Architecture diagram (1 image)

Boxes and arrows from:

```
data sources → pipelines → features → training → model registry (optional) → serving → monitoring → retraining
```

### Quick demo artifact (pick one)

- 3–5 screenshots (API call, monitoring output, pipeline run), **or**
- A 3–5 slide mini-deck, **or**
- A short 2–3 minute screencast (if allowed by the course)

---

## Required Components

### A. Data & Features (M2, M4, M9, M10) — 25% of assignment

Students must:

**Describe the data**

- Source / dataset
- Target label
- Any important assumptions or cleaning steps

**Construct features**

- At least **5 non-trivial features** (aggregations, ratios, encodings, time-window features, etc.)
- Document which features are offline vs online (or how they would be in production)

**Show awareness of training–serving skew**

Explain how you would ensure consistent features between training and serving, for example:

- Shared preprocessing module
- Same code for offline and online
- A mini feature table plus lookup

**Data pipeline step**

Simple batch or micro-batch ingestion script that:

- Reads new data file(s) (e.g., daily CSV)
- Appends/merges to a training data table or file
- Logs what it ingested (N rows, date)

**What you grade:** clarity of data description, quality of features, and whether students are thinking about offline vs online features and skew.

---

### B. Model Training & Offline Evaluation (M1–M2, M4, M6, M11) — 25%

Students must:

**Implement a training script/pipeline**

Can be a Python script or notebook, but should look like a repeatable pipeline:

```
load data → split train/val (or train/val/test) → train model → evaluate → save artifacts
```

**Choose and justify metrics**

- E.g., accuracy + ROC AUC for classification, or RMSE for regression
- Brief explanation of why these metrics matter for this use case

**Offline evaluation harness**

Evaluate at least two versions:

1. A **baseline model** (simpler)
2. A **candidate model**

Compare metrics and state whether you would promote the candidate.

> **Optional:** simple threshold/guardrail rule — e.g., “Only promote if AUC ≥ 0.8 and not worse than baseline by more than 0.01”.

**Save artifacts**

- Save trained model and evaluation report (JSON / CSV / Markdown)
- Use a simple directory layout such as `models/` and `artifacts/eval/`

**What you grade:** pipeline structure, metric choice and explanation, and evidence of baseline vs candidate comparison.

---

### C. Serving & Inference Pattern (M2–M3–M7–M8) — 25%

Students must:

**Expose the model as a minimal API**

- Preferably FastAPI (or Flask/Django if that is what the course used)
- At least one endpoint: `/predict` taking a JSON body with input fields
- Response should include prediction and a `model_version` or similar

**Choose an inference pattern**

Online API (request–response), batch script, or a hybrid (precompute + online ranking).

Explain the choice in the design doc using M2 concepts:

- Is a human waiting?
- What latency is acceptable?
- Is the use case naturally batch / streaming?

**Basic latency/throughput measurement**

Simple script that sends multiple requests or processes many rows.

Report:

- Average latency and maybe p95 (even from a small run)
- For batch: total time and rows/sec

> **Optional but nice:** Dockerfile to run the API. Not mandatory if time is tight, but bonus or extra credit.

**What you grade:** functioning service, clear request/response design, inference pattern justification, and basic performance measurement.

---

### D. Monitoring, Data Quality, and Retraining Trigger (M5–M6–M10–M11) — 25%

Students must design (not fully implement production-grade tools) a monitoring and retraining plan.

**Monitoring plan**

List at least:

| Category | Examples |
| --- | --- |
| **Infra metrics** | Latency (avg, p95), error rate |
| **Data / feature metrics** | Counts, missing values, basic drift signals |
| **Model / business metrics** | Accuracy on labeled feedback or proxy business KPI |

Explain which dashboards/alerts you would create and for whom.

**Simple drift / data quality check**

Implement one lightweight check in code or a notebook, for example:

- Count nulls / out-of-range values
- Compare mean/std of a feature between training and a recent batch
- Print or log a simple warning if drift or a quality issue is detected

**Retraining trigger logic (pseudo-code is fine)**

Define 2–3 signals, e.g.:

- Retrain if we have N new days of data
- Retrain if AUC on recent labeled feedback drops by X points
- Retrain if drift score exceeds threshold

Write this as pseudo-code or a short function (does not need to be wired to a scheduler).

**Brief incident scenario**

In the design doc, describe one failure scenario (e.g., upstream schema change, data drop, model degradation).

Outline how your monitoring would detect it and what you would do (rollback, retrain, fix pipeline, etc.).

**What you grade:** thoughtfulness of monitoring plan, one working data quality/drift check, and a realistic retraining/incident story.

---

## Suggested Marking Rubric (for the 28%)

You can tweak the exact numbers, but here is a clean breakdown:

| Component | Points (of 28) |
| --- | ---: |
| Data and Features (A) | 7 |
| Training and Evaluation (B) | 7 |
| Serving and Inference (C) | 7 |
| Monitoring and Retraining Plan (D) | 5 |
| Code Quality and Reproducibility | 1 |
| Design Doc and Communication | 1 |

**Code Quality and Reproducibility:** clear structure, instructions, runs without major issues.

**Design Doc and Communication:** clarity, diagrams, explanation of trade-offs.

> If you prefer integers in %: 25% + 25% + 25% + 18% + 4% + 3% ≈ 100% of the assignment, scaled to 28% course weight.

---

## Optional: Assignment Variants

If you want two tracks, you can specify:

| Track | Emphasis |
| --- | --- |
| **Track A — Online scoring focus** | Stronger emphasis on latency measurement and online monitoring |
| **Track B — Batch / pipeline focus** | Stronger emphasis on data ingestion, retraining schedule, and cost |

The same rubric still works; only the examples students implement differ.

---

## Evaluation Rubric

**Rubric name:** Mini Production ML System — Evaluation Rubric
**Total score:** 20 points (5 criteria × 4 points each)

| Criterion | Level 4 (3.1–4.0) | Level 3 (2.1–3.0) | Level 2 (1.1–2.0) | Level 1 (0.0–1.0) | Max |
| --- | --- | --- | --- | --- | ---: |
| **Problem Understanding and Use Case** | Clearly defines the ML problem, intended users, inputs, outputs, and production requirements. | Defines the problem and use case clearly, with minor missing details. | Provides a basic problem description, but important aspects such as users, inputs, outputs, or requirements are unclear. | Problem definition is incomplete, unclear, or inconsistent with the submitted system. | / 4 |
| **Data Preparation and Model Development** | Data is appropriately prepared, the model choice is justified, and suitable training and evaluation methods are used. | Data preparation and modelling are mostly correct, with minor issues or missing justification. | A model is developed, but data preparation, model selection, or evaluation has noticeable weaknesses. | Data preparation or model development is substantially incomplete or technically incorrect. | / 4 |
| **Production System Design and Implementation** | Presents and implements a clear end-to-end workflow from input data to model prediction, with appropriate system components. | The main workflow is implemented correctly, with minor missing components or integration issues. | The system is partially implemented, but important parts of the workflow are incomplete or unclear. | The submission contains little evidence of a working end-to-end ML system. | / 4 |
| **Evaluation and Production Considerations** | Evaluates model performance and discusses relevant production considerations such as latency, scalability, monitoring, reliability, or cost. | Provides suitable evaluation and discusses some production considerations, with minor gaps. | Provides limited evaluation or only a basic discussion of production considerations. | Evaluation is insufficient, incorrect, or unrelated to the stated system requirements. | / 4 |
| **Documentation and Presentation** | The submission is clear, well-structured, technically accurate, and includes sufficient diagrams, results, and explanations. | The submission is understandable and mostly complete, with minor documentation or presentation issues. | The submission contains the main information, but explanations, structure, diagrams, or results are incomplete. | The submission is poorly documented, difficult to understand, or missing substantial required information. | / 4 |
| **Total** | | | | | **/ 20** |

### Overall Score

| Overall level | Minimum total points (out of 20) |
| --- | ---: |
| **Level 4** | 11 |
| **Level 3** | 8 |
| **Level 2** | 5 |
| **Level 1** | 0 |
