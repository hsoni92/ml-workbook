# Evaluating Model Performance and Common Pitfalls – Machine Learning (Module 3)

## Learning Objectives

By the end of this video you will:

1. **Define** train error vs test error and how they are computed.
2. **Build** a **confusion matrix** (TP, TN, FP, FN) for binary classification.
3. **Define** and compute **accuracy**, **precision (PPV)**, **recall (TPR/sensitivity)**, **NPV**, **TNR (selectivity)**.
4. **Describe** other evaluation aspects: **speed** (training/prediction), **interpretability**, **scalability**, **robustness**.
5. **Compare** evaluation for **classification** vs **regression** (correct/incorrect vs error magnitude).

---

## Train Error vs Test Error

- **Train error:** Train the model on **training data**, then **evaluate on the same training data**. Measures how well the model **fits** the training set.
- **Test error:** Train the model on **training data**, then **evaluate on held-out test data**. Measures how well the model **generalizes** to unseen data.

We **care most** about **test** performance for real-world use.

---

## Evaluating a Classification Model (Correct vs Incorrect)

- For each **test** record we have **true label Y** and **predicted label ŷ**.
- **Correct prediction:** ŷ = Y. **Incorrect prediction:** ŷ ≠ Y.
- We **count** correct and incorrect over all test samples. These counts underlie **accuracy** and the **confusion matrix**.

---

## Confusion Matrix (Binary Classification)

Assume two classes: **Positive** (e.g. Malware) and **Negative** (e.g. Benign). Rows = **true** class, columns = **predicted** class.

| | Predicted Positive | Predicted Negative |
|--|--------------------|--------------------|
| **True Positive** | **TP** (correct) | **FN** (wrong) |
| **True Negative** | **FP** (wrong) | **TN** (correct) |

- **TP:** True class = Positive, Predicted = Positive. ✓  
- **TN:** True class = Negative, Predicted = Negative. ✓  
- **FP:** True class = Negative, Predicted = Positive. ✗ (false alarm)  
- **FN:** True class = Positive, Predicted = Negative. ✗ (miss)

**Correct predictions** = TP + TN. **Incorrect** = FP + FN.

---

## Accuracy

- **Accuracy** = (Correct predictions) / (Total predictions) = **(TP + TN) / (TP + TN + FP + FN)**.
- Often expressed as a percentage (× 100). Higher accuracy = better overall correctness.

---

## Precision (PPV – Positive Predictive Value)

- **Precision** = Of **all** instances **predicted as Positive**, how many were **actually** Positive?
- **Formula:** **Precision = TP / (TP + FP)**.
- Focus: **How reliable are our positive predictions?**

---

## Recall (TPR – True Positive Rate / Sensitivity)

- **Recall** = Of **all** instances that are **actually Positive**, how many did we **correctly** predict as Positive?
- **Formula:** **Recall = TP / (TP + FN)**.
- Focus: **How many of the true positives did we catch?**

---

## NPV (Negative Predictive Value)

- Of all instances **predicted as Negative**, how many were **actually** Negative?
- **Formula:** **NPV = TN / (TN + FN)**.

---

## TNR (True Negative Rate / Selectivity)

- Of **all** instances that are **actually Negative**, how many did we **correctly** predict as Negative?
- **Formula:** **TNR = TN / (TN + FP)**.

---

## Train/Test Split (Typical Ratios)

- Common: **70–30** or **80–20** (train–test). Also **90–10**, **60–40** in literature. **No fixed rule**; data and problem dictate.
- Idea: Most data for **training**, a separate portion for **testing** only.

---

## Evaluating a Regression Model

- For regression, **Y** and **ŷ** are **continuous**. We cannot just count “correct/incorrect.”
- **Error** for one sample: **ŷ − Y** (or |ŷ − Y|).
- **Aggregate measures:**
  - **Sum of absolute errors:** Σ |ŷ − Y| over test samples.
  - **Mean absolute error (MAE):** (1/n) Σ |ŷ − Y|.
  - **Sum of squared errors (SSE):** Σ (ŷ − Y)².
  - **Mean squared error (MSE):** (1/n) Σ (ŷ − Y)².

---

## Other Performance Criteria

| Criterion | Meaning |
|-----------|---------|
| **Speed (training)** | Time to train the model (seconds to days). |
| **Speed (prediction)** | Time to predict one (or many) sample(s). Critical in real-time systems (e.g. intrusion detection). |
| **Interpretability** | Can we **explain** how the model reached a decision? High = white box; low = black box (e.g. complex neural nets). |
| **Scalability** | Does performance (time, memory) remain acceptable as **data size** or **load** grows? |
| **Robustness** | Does the model handle **noise** and **outliers** reasonably? |

---

## Summary

- **Train error** = error on training data; **test error** = error on held-out test data.
- **Confusion matrix:** TP, TN, FP, FN. **Accuracy** = (TP + TN) / total.
- **Precision** = TP/(TP+FP); **Recall** = TP/(TP+FN). PPV/NPV and TPR/TNR give a full picture.
- **Regression:** Use **absolute** or **squared** errors (e.g. MAE, MSE).
- Also consider **speed**, **interpretability**, **scalability**, **robustness** for real systems.

Use this note for computing and interpreting confusion matrix, accuracy, precision, and recall in exams.
