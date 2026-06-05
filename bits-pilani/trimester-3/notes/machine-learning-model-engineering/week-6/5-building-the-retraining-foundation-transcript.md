# Designing a Retraining and Promotion Pipeline

## From "When to Retrain" to "How to Retrain Safely"

Knowing that retraining is warranted is only half the problem. Production MLOps requires a **structured, repeatable pipeline** that produces candidate models, compares them to the current champion, and promotes winners through controlled stages — with full auditability at every step.

**Intuition**: Ad-hoc retraining (a data scientist runs a notebook and emails a pickle file) does not scale. A pipeline turns retraining into an engineering process with predictable inputs, outputs, and gates.

---

## High-Level Pipeline Architecture

```mermaid
flowchart LR
    A[Data Snapshot] --> B[Feature Engineering]
    B --> C[Train Candidates]
    C --> D[Evaluate vs Champion]
    D --> E{Passes Rules?}
    E -->|Yes| F[Register in Model Registry]
    E -->|No| G[Archive & Log]
    F --> H[Staging / Canary]
    H --> I[Production Promotion]
```

| Stage | Purpose | Key Output |
|-------|---------|------------|
| 1. Data & Features | Reproducible training dataset | Snapshot + metadata (time window, sources, hashes) |
| 2. Train Candidates | Explore hyperparameters / architectures | Logged runs with code version, configs, metrics |
| 3. Evaluate & Select | Governance gate vs champion | Promotion decision with multi-metric evidence |
| 4. Register | First-class artefact with lineage | Versioned model entry in registry |
| 5. Promote | Safe rollout to production | Staging → canary/shadow → full production |

Everything is logged so any model can be audited: *exactly which data, code, and config produced this model*.

---

## Stage 1: Data Snapshot and Feature Engineering

**First principles**: A model is only as good as the data it learned from. Treating the training dataset as a first-class artefact enables reproducibility and compliance.

Steps:

1. **Define time window** — e.g., last 3 months of labelled data
2. **Pull from warehouse or feature store** — same sources used in production
3. **Apply production feature engineering logic** — identical transformations, no train-serve skew
4. **Record metadata**:
   - Time period covered
   - Source tables / feature views
   - Content hashes or version IDs

**Why metadata matters**: Six months later, when performance drops, you must answer: *"Which data produced model v7?"* Without snapshots and hashes, root cause analysis is impossible.

---

## Stage 2: Train Candidate Models

Instead of training a single model, production pipelines typically train **multiple candidates**:

- Different hyperparameter configurations
- Alternative model types (e.g., gradient boosting vs logistic regression)
- Varied training windows or feature subsets

For each candidate, log:

| Logged Item | Purpose |
|-------------|---------|
| Code version (git commit) | Reproduce exact training script |
| Config file (YAML/JSON) | Hyperparameters, data paths, feature lists |
| Data snapshot reference | Link model to specific dataset version |
| Training metrics | Loss curves, validation scores during training |

Tools like **MLflow**, Weights & Biases, or Neptune organise these runs so you can later say: *"These 3 candidates were trained on the same data snapshot with these different configurations."*

---

## Config-Driven Design Pattern

Production retraining pipelines are **config-driven**, not hardcoded:

```yaml
# Example: train_config_v2.yaml
data:
  path: "data/training_v2.parquet"
  window_start: "2025-01-01"
  window_end: "2025-03-31"
model:
  type: "xgboost"
  max_depth: 6
registry:
  model_name: "credit_risk_model"
```

Changing the data window or hyperparameters means editing a config file — not modifying training code. This makes retraining **repeatable and auditable**: each config file is a clear record of which data was used for which run.

---

## Real-World Example: Credit Risk Retraining

A fintech team refreshes their credit model quarterly (scheduled) and on drift alerts (event-driven):

1. Config `train_config_v1.yaml` points to Q1 data → produces champion v1
2. Three months later, config `train_config_v2.yaml` points to Q2 data → produces challenger v2
3. Both runs use the same `train.py` script, same feature pipeline, different config
4. MLflow logs parameters, metrics, config artefact, and registers each as a versioned candidate

---

## Common Pitfalls / Exam Traps

- **Hardcoding data paths in training scripts** — breaks reproducibility and auditability.
- **Training without production feature logic** — train-serve skew invalidates offline evaluation.
- **Single candidate, no comparison** — no way to know if the new model beats the champion.
- **Missing data snapshot metadata** — cannot answer lineage questions during incidents.
- **Skipping experiment tracking** — untraceable runs waste compute and create compliance risk.

---

## Quick Revision Summary

- Retraining pipeline: snapshot data → build features → train candidates → evaluate → register → promote.
- Stage 1 treats training data as a first-class artefact with time window, sources, and hashes.
- Stage 2 trains multiple candidates with full logging of code, config, data, and metrics.
- Config-driven pipelines make retraining repeatable — change config, not code.
- MLflow (or similar) organises runs and links candidates to the same data snapshot.
- Full logging enables audit, reproducibility, and rollback.
