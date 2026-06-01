**Problem Statement Number:** P4

# Advanced Apex Project-2 — Week-2 Project Outline

## ANN-Based Customer Response Prediction

| Field | Value |
| --- | --- |
| **Problem Statement** | P4 |
| **Project ID** | BITS-Pilani-T3-APEX-2 |
| **Course** | Advanced Apex Project-2 |
| **Domain** | Banking, Telecom, Retail, ECommerce, EdTech |
| **Student** | Himanshu Soni (2025EM1100506) |
| **Date** | 2026-05-31 |

> Markdown explanations, observations, and interpretations will be included between code cells in the implementation notebook to support readability, reproducibility, and evaluation.

## Table of Contents

1. [Problem Statement & Business Goal](#1-problem-statement--business-goal)
2. [Dataset Details](#2-dataset-details)
3. [Initial Dataset Understanding](#3-initial-dataset-understanding)
4. [Proposed Workflow](#4-proposed-workflow)
5. [Proposed Baseline & Advanced Models](#5-proposed-baseline--advanced-models)
6. [Evaluation Metrics & Tuning Plan](#6-evaluation-metrics--tuning-plan)
7. [Tools & Technologies](#7-tools--technologies)
8. [References](#8-references)

---

## 1. Problem Statement & Business Goal

### Problem statement

Organizations in banking, telecom, retail, e-commerce, and ed-tech run outbound marketing campaigns (calls, SMS, email, in-app offers) to drive subscriptions, renewals, and product adoption. Campaigns are costly when applied uniformly: most customers do not convert, contact limits are wasted on low-intent profiles, and sales or call-center capacity is fixed. The core problem is **predicting which customers are likely to respond positively** to a campaign before outreach, so marketing effort can be targeted rather than broadcast.

This project addresses **binary customer response prediction**: given historical customer and campaign interaction data, estimate the probability that a customer will accept the marketed outcome (e.g., subscribe to a term deposit, renew a plan, or accept an offer).

### Business objective

Build and compare an **Artificial Neural Network (ANN)**-based classifier against a simple baseline to:

- Rank customers by predicted response likelihood for campaign prioritization.
- Reduce wasted contacts and improve conversion rate on a fixed outreach budget.
- Provide a reproducible pipeline (preprocessing through evaluation) suitable for extension to other domains listed in the project brief.

Success is measured primarily by **ranking quality** (ROC-AUC, PR-AUC) and **positive-class detection** (recall, F1) under class imbalance, not raw accuracy alone.

---

## 2. Dataset Details

### Source

| Item | Detail |
| --- | --- |
| **Dataset** | Bank Marketing (UCI Machine Learning Repository) |
| **URL** | https://archive.ics.uci.edu/dataset/222/bank+marketing |
| **Context** | Portuguese banking institution; direct marketing calls promoting term deposit subscription |
| **License** | Public, academic use (UCI) |

The same modeling approach (tabular features + binary outcome) generalizes to telecom churn/upsell, retail coupon redemption, and similar campaign-response problems; banking data is used as the primary benchmark.

### Size

| Split / version | Approximate size |
| --- | --- |
| **Records** | ~41,188 (standard subset used in coursework); full repository versions up to ~45,211 |
| **Features** | 16 input attributes + 7 additional social/economic indicators in extended variants (20+ columns total depending on version) |
| **Instances** | One row per contact/campaign interaction |

### Target variable

| Attribute | Description |
| --- | --- |
| **`y` (subscription)** | Binary: **yes** = customer subscribed to term deposit; **no** = did not subscribe |
| **Task type** | Binary classification |
| **Positive class** | Minority class (~11–15% **yes**), requiring imbalance-aware metrics and training |

### Important features (grouped)

| Group | Features (examples) | Role |
| --- | --- | --- |
| **Demographics** | `age`, `job`, `marital`, `education` | Customer profile segmentation |
| **Credit / account** | `default`, `balance`, `housing`, `loan` | Financial standing and obligations |
| **Campaign contact** | `contact`, `month`, `day`, `duration` | How and when the customer was reached; `duration` is highly predictive but only known after contact |
| **Campaign history** | `campaign`, `pdays`, `previous`, `poutcome` | Intensity and outcome of past contacts |
| **Macro (optional)** | `emp.var.rate`, `cons.price.idx`, `euribor3m`, `nr.employed` | Economic context at time of contact |

**Note for modelling:** `duration` may cause **leakage** if used to predict response before a call ends; the workflow will document whether duration is excluded for realistic deployment scenarios or retained for benchmark comparison, with rationale in markdown cells.

---

## 3. Initial Dataset Understanding

### Initial observations (expected after EDA)

- **Class imbalance:** Positive (`yes`) rate typically ~11–15%; accuracy can look high while failing to detect converters.
- **Mixed types:** Numeric (`age`, `balance`, `duration`, `campaign`) and categorical (`job`, `marital`, `education`, `month`, `poutcome`).
- **Ordinal / low-cardinality categoricals:** `education`, `month` require encoding (one-hot, target encoding, or embeddings for neural nets).
- **Skewed numerics:** `balance`, `duration`, and `campaign` may be right-skewed; scaling (standardization, robust scaling) will be needed for ANNs.
- **Correlations:** `duration` and `poutcome` / `previous` often correlate strongly with `y`; multicollinearity and leakage must be checked.
- **Temporal pattern:** `month` and macro indicators introduce seasonality; train/validation split should avoid random shuffle-only if time-based generalization is claimed (stratified split acceptable for outline phase).
- **Missing values:** UCI bank dataset often has few explicit nulls; `"unknown"` categories act as missing proxies for `job`, `education`, etc.

### Expected challenges

| Challenge | Mitigation (planned) |
| --- | --- |
| Class imbalance | Class weights, threshold tuning, PR-AUC focus, stratified splits |
| Leakage from `duration` | Report models with and without `duration`; prefer no-duration for deployment narrative |
| High cardinality / unknowns | Group rare categories; explicit `"unknown"` handling |
| Interpretability vs. ANN performance | Compare baseline coefficients / feature importance with SHAP or permutation importance on best ANN |
| Overfitting on ANNs | Dropout, early stopping, validation monitoring, regularization |
| Hyperparameter sensitivity | Structured tuning (grid/random search or Keras Tuner) with fixed random seeds |

---

## 4. Proposed Workflow

End-to-end pipeline aligned with the course template (DPP → EDA → FE → modelling → tuning → evaluation):

```mermaid
flowchart LR
  A[Raw data] --> B[DPP]
  B --> C[EDA]
  C --> D[FE]
  D --> E[Modelling]
  E --> F[Tuning]
  F --> G[Evaluation]
```

| Step | Activity | Deliverables |
| --- | --- | --- |
| **1. Data Preprocessing & Preparation (DPP)** | Load UCI data; define target; handle `"unknown"`; impute if needed; train/validation/test split (stratified); scale numeric features; encode categoricals | Clean train/val/test tensors or arrays; data dictionary in markdown |
| **2. Exploratory Data Analysis (EDA)** | Class distribution; univariate and bivariate plots; correlation heatmap; outlier checks; leakage analysis for `duration` | Figures + written observations between code cells |
| **3. Feature Engineering (FE)** | Interaction features (optional); binning `age`; cyclical encoding for `month`; feature selection; final feature matrix for sklearn and Keras | Feature list documented; rationale for kept/dropped columns |
| **4. Modelling** | Train **baseline** (Logistic Regression); train **ANN** models (MLP primary; DNN depth variants); optional comparative runs (e.g., simpler tree-based model for sanity check) | Saved models; training curves; comparison table |
| **5. Hyperparameter tuning** | Tune learning rate, layers/units, dropout, batch size, epochs (early stopping); class weights for imbalance | Best hyperparameters logged; validation metric traces |
| **6. Evaluation** | Test-set metrics; confusion matrix; ROC and PR curves; threshold analysis; short business interpretation (lift, contact reduction scenario) | Final metric table; conclusion and limitations |

**Reproducibility:** Fixed random seeds, version-pinned libraries, and notebook section headers matching sections 1–8 above.

---

## 5. Proposed Baseline & Advanced Models

### Baseline

| Model | Purpose |
| --- | --- |
| **Logistic Regression** | Interpretable linear baseline; fast; establishes minimum performance with scaled + encoded features |

### Comparison / advanced models

| Model | Role in project |
| --- | --- |
| **Multi-Layer Perceptron (MLP)** | Primary ANN; fully connected layers on engineered tabular features |
| **Deep Neural Network (DNN)** | Deeper MLP variant (more hidden layers/units) to test capacity vs. overfitting |
| **Convolutional Neural Network (CNN)** | Optional experiment: reshape engineered feature matrix (e.g., grouped channels) for architecture comparison—not the main production candidate for pure tabular data |
| **Recurrent Neural Network (RNN/LSTM)** | Optional experiment if sequential features are constructed (e.g., past campaign sequence); exploratory comparison only |

**Comparison strategy:** Same splits and metrics for all models; tabular summary (validation and test); best model selected by **PR-AUC** and **F1** on validation, then confirmed on held-out test.

---

## 6. Evaluation Metrics & Tuning Plan

### Evaluation metrics

| Category | Metrics | Why |
| --- | --- | --- |
| **Technical — classification** | Accuracy, Precision, Recall, F1-score | Standard reporting; F1 balances precision/recall under imbalance |
| **Technical — ranking** | ROC-AUC, PR-AUC | Threshold-independent; PR-AUC emphasized for rare positive class |
| **Business-oriented** | Lift at top deciles, campaign conversion rate on targeted subset, simple cost model (cost per contact vs. benefit per conversion) | Links model scores to prioritization value |

Primary model selection criterion: **validation PR-AUC**, with **recall at fixed precision** or **F1** as secondary checks.

### Tuning plan

| Aspect | Approach |
| --- | --- |
| **Baseline (Logistic Regression)** | `C` regularization inverse; solver; class_weight=`balanced` |
| **ANN (Keras/TensorFlow)** | Grid or random search over: hidden units (e.g., 64–256), number of layers (2–4), dropout (0.2–0.5), learning rate (1e-4–1e-2), batch size (32–256), epochs with **early stopping** (patience on `val_loss` or `val_pr_auc`) |
| **Imbalance** | `class_weight` in `fit()` or balanced sampling; threshold moved on validation set to meet recall/precision target |
| **Validation protocol** | Stratified k-fold (k=5) or single stratified hold-out; same folds for baseline and ANNs |
| **Overfitting control** | Early stopping, dropout, L2 if needed; plot train vs. validation loss |
| **Final test** | Touch test set once after tuning locked; report all metrics in section 6 table |

Document every tuning choice in markdown (what was tried, what was selected, why).

---

## 7. Tools & Technologies

| Layer | Tools |
| --- | --- |
| **Language** | Python 3.10+ |
| **Data & ML** | pandas, NumPy, scikit-learn |
| **Neural networks** | TensorFlow 2.x / Keras (primary); PyTorch (optional if needed for a variant) |
| **Visualization** | matplotlib, seaborn |
| **Interpretability** | SHAP or scikit-learn permutation importance (for best model) |
| **Experiment tracking** | CSV/logs in notebook; optional MLflow |
| **Environment** | Jupyter Notebook / JupyterLab; Google Colab or local VS Code |
| **Version control** | Git |
| **Containerization (optional)** | Docker for reproducible environment |

---

## 8. References

1. Moro, S., Rita, P., & Cortez, P. (2014). *A data-driven approach to predict the success of bank telemarketing.* Decision Support Systems, 62, 22–31. https://doi.org/10.1016/j.dss.2014.03.001

2. UCI Machine Learning Repository — **Bank Marketing Data Set** (donated by S. Moro).
   https://archive.ics.uci.edu/dataset/222/bank+marketing

3. Keras Documentation — Multi-layer perceptron and training callbacks (EarlyStopping).
   https://keras.io/

4. scikit-learn Documentation — `LogisticRegression`, metrics (`roc_auc_score`, `average_precision_score`), and `class_weight`.
   https://scikit-learn.org/stable/

5. Chollet, F. (2021). *Deep Learning with Python* (2nd ed.). Manning. (Chapters on binary classification and fighting overfitting.)

6. He, H., & Garcia, E. A. (2009). Learning from imbalanced data. *IEEE Transactions on Knowledge and Data Engineering*, 21(9), 1263–1284. (Imbalance-aware evaluation and training.)

---

*Outline prepared for Week-2 submission — Advanced Apex Project-2 (BITS-Pilani-T3-APEX-2).*
