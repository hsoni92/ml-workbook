# Foundations of Machine Learning and Supervised Learning – Machine Learning (Module 3)

## Learning Objectives

By the end of this video you will:

1. **Define** Machine Learning and its fundamental purpose (learn from data without explicit rules).
2. **Differentiate** **supervised** vs **unsupervised** (and briefly **reinforcement**) learning.
3. **Explain** core concepts of supervised learning: X, Y, model f, prediction.
4. **Distinguish** **classification** (discrete Y) vs **regression** (continuous Y).
5. **Describe** the end-to-end ML workflow (problem → data → preprocess → model → evaluate → deploy).

---

## What Is Machine Learning?

**Traditional approach (e.g. teaching a child to recognize a cat):** We give **rules** — “four legs, pointy ears, whiskers, meows = cat.” The learner follows explicit instructions.

**ML approach:** We give **many examples** (e.g. thousands of cat images) and let the **algorithm learn** patterns and features that associate images with “cat” **without** programming every rule.

**Definition:** Machine Learning is the **science of getting computers to learn and act** (e.g. like humans) **by learning patterns from data without being explicitly programmed** with rules.

---

## Traditional Programming vs Machine Learning

| Traditional | Machine Learning |
|-------------|------------------|
| Input + **Rules** → Output | **Data** + **Problem statement** → **Model** → Output (predictions) |
| We write the rules | Algorithm **learns** rules/patterns from data |

**ML workflow (high-level):**

1. **Problem** — e.g. “Distinguish cat vs dog in images.”
2. **Collect data** — e.g. thousands of images of cats and dogs.
3. **Pre-process** — clean and prepare data.
4. **Build model** — choose an algorithm (e.g. decision tree, random forest, SVM), **train** on data to get model **f**.
5. **Evaluate** — measure performance (e.g. on new images).
6. **Deploy** — use **f** in the real world for prediction.

We **do not** tell the algorithm exactly how to separate cat and dog; it **learns** from data.

---

## Three Types of Learning

| Type | Idea | Goal |
|------|------|------|
| **Supervised** | Learn with a “teacher” — we have **labels (Y)** | **Prediction** (of Y for new X) |
| **Unsupervised** | No labels; only **X** | **Find patterns and structure** in data |
| **Reinforcement** | Learn by **trial and error** with rewards/penalties | Learn **actions** that maximize reward |

This course focuses on **supervised** and **unsupervised** learning.

---

## Supervised Learning in Detail

- **Input:** Data **X** (e.g. attributes) and **labels Y** (correct answers / class labels).
- **Supervisor** = training data **with** labels (the “answer key”).
- **Goal:** Learn a **function f** such that **f(X) ≈ Y**. For **new/unseen X**, we **predict Y** using **f**.

**Example – Spam filter:**

- **X:** Email content, sender, attachments, etc.
- **Y:** Spam or Not spam.
- We build **f** from many (X, Y) examples. For a new email (X only), **f** predicts spam or not.

**Example – Unsupervised (contrast):**

- Only **X** (e.g. customer purchase data). No “spam/not spam.”
- Goal: **Find patterns** — e.g. “grocery shoppers,” “tech buyers,” “new parents” — **no prediction** of a label.

---

## Classification vs Regression (Supervised)

Both use **X** and **Y** to learn **f** and then **predict Y** for new **X**.

| | Classification | Regression |
|--|----------------|------------|
| **Y** | **Discrete / categorical** (finite classes) | **Continuous / numerical** |
| **Examples** | Spam/not spam, malignant/benign, cat/dog/bird | Petrol price, salary, stopping distance |
| **Number of values** | Fixed (e.g. 2, 3) | Infinite (any number in range) |

**Classification:** Separate **classes** (e.g. by a line/plane/curve). New point → assign one of the predefined classes.

**Regression:** Find a **relationship** between X and Y (e.g. age vs salary). New X → predict a **numeric** Y.

---

## Visual Intuition

- **Classification (binary):** Two classes (e.g. squares and circles). We learn a **boundary**; points on one side → class 1, other side → class 2. **Multi-class:** More than two classes; boundary separates all.
- **Regression:** Scatter of (X, Y) (e.g. age vs salary). We fit a **curve/line**; for new X we **predict** Y on that curve.

---

## Summary

- **ML** = learning patterns from data **without** explicit programming of rules.
- **Supervised:** Have **X** and **Y**; learn **f** to **predict Y** for new **X**.
- **Unsupervised:** Only **X**; find **patterns/structure** (no prediction of a label).
- **Classification:** Y = discrete/categorical. **Regression:** Y = continuous.
- **Workflow:** Problem → Data → Preprocess → Train model → Evaluate → Deploy.

Use this note for definitions and for comparing supervised vs unsupervised and classification vs regression in exams.
