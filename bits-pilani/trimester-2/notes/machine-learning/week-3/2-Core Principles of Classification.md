# The Core Principles of Classification – Machine Learning (Module 3)

## Learning Objectives

By the end of this video you will:

1. **Define** the classification task formally (training data, attribute set X, class label Y, model f).
2. **State** that class labels must be **mutually exclusive** and **exhaustive**.
3. **Describe** the **two-step** process: **model training** and **model testing**.
4. **Explain** why test set must be **independent** of training set.
5. **Give** real-world applications (e.g. spam, tumor, malware).

---

## Formal Definition of Classification

- **Training data:** A collection of **records**; each record has **X** (attribute set) and **Y** (class label).
- **X (attribute set):** Set of **features** (e.g. x1, x2, x3) that **describe** each record.
- **Y (class label):** **Predefined category** the record belongs to (what we want to predict).
- **Task:** Learn a **model (function) f** that **maps X → Y** so that for **new/unseen** records we can **assign a class label** as accurately as possible.

**Example – Customer churn:**

- **X:** Age, billing amount, months on platform, number of support calls.
- **Y:** Stay or Unsubscribe (two classes).
- **Goal:** Given a new customer’s **X**, predict whether they will **stay** or **unsubscribe**.

---

## Properties of Class Labels (Y)

- **Exhaustive:** Every possible outcome fits into **one** of the classes (we have a label for every record we care about).
- **Mutually exclusive:** No object belongs to **more than one** class. If two records have the **same X**, they must have the **same Y** (no contradiction).

---

## Real-World Examples

| Application | X (examples) | Y (classes) |
|-------------|--------------|-------------|
| **Email categorization** | Words, sender, attachment, etc. | Spam, Not spam |
| **Tumor / cancer** | Size, shape, texture, boundary (from image) | Malignant, Benign |
| **Malware detector** | File features (a1, a2, a3, …) | Malware (M), Benign (B) |

In each case we have **training (X, Y)**; we build **f**; for **new X** we **predict Y**.

---

## Two-Step Process: Training and Testing

### Step 1: Model Training

- **Input:** **Training set** (subset of full data) with **X** and **Y**.
- **Process:** Use a **learning algorithm** (e.g. decision tree, rules, SVM) to **learn** the mapping from **X** to **Y**.
- **Output:** **Model f** (e.g. a set of rules or a tree). Example rule: “If age = 60 and has_loan = true → class = high.”

### Step 2: Model Testing

- **Input:** **Test set** (different from training set). We have **X** and **Y** but **temporarily ignore Y**.
- **Process:** For each test record, feed **only X** into **f**; get **predicted Y** (e.g. ŷ). Compare **ŷ** with **true Y**.
- **Goal:** **Estimate** how well **f** will perform on **unseen** data. If predictions match true labels often → good model; else → need improvement.

**Critical:** **Test set must be independent** of training set (no overlap). Evaluating on training data would be “cheating” (like giving exam questions that are identical to practice). We want to test **generalization** to **new** data.

---

## Deployment (Inference)

- Once we are satisfied with **test performance**, we **deploy** the model.
- In production we only get **X** (e.g. new email, new image, new file). We use **f** to **predict Y** (spam/not, malignant/benign, malware/benign).
- This use of the **built** model for prediction is sometimes called **deduction** or **inference**.

---

## Full Pipeline (Recap)

1. Start with **full labeled data** (X, Y).
2. **Split** into **training** and **test** (disjoint).
3. **Train** model **f** on **training** data.
4. **Test** **f** on **test** data (feed X, compare predicted Y with true Y).
5. If performance is good → **deploy** **f** for real-world prediction.

---

## Summary

- **Classification** = learn **f: X → Y** from (X, Y), with **Y** categorical; **exhaustive** and **mutually exclusive**.
- **Training** = build **f** using **training set**; **testing** = evaluate **f** on **separate test set** (only X fed to f; compare predictions to true Y).
- **Test set** must be **independent** of training to measure true performance.
- **Deployment** = use **f** to predict **Y** for new **X** in the real world.

Use this note for exam questions on “formal definition of classification,” “training vs testing,” and “why test set must be separate.”
