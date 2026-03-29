# Supervised Learning – Learning from Labelled Data – Machine Learning (Module 1)

## Learning Objectives

By the end of this video you will:

1. **Define** supervised learning and its core concepts (data, labels, model).
2. **Distinguish** between **classification** and **regression**.
3. **Describe** the process of **training** and **testing** a classification model.
4. **Give** real-world examples of classification and regression.

---

## Two Fundamental Types of Learning

| Type | Also called | Goal | Data |
|------|-------------|-----|------|
| **Supervised learning** | Prediction methods | **Predict** unknown values | Data **with** correct answers (labels) |
| **Unsupervised learning** | Descriptive methods | **Find** patterns and structure | Data **without** labels |

---

## What Is Supervised Learning?

- **Idea:** Learn from examples where the **correct answer (label)** is known, then **predict** for new inputs.
- **Labels** = correct answers = class labels = target. Terms are used interchangeably.
- **Training examples:** Pairs **(input features, desired output)**. Input = **X**, output = **Y** (label/target).
- The model learns a **function f** that maps **X → Y**. At deployment we get only **X** and use **f** to predict **Y**.

**Analogy:** Student learns from a textbook with answers at the back (data + labels), then solves new questions (prediction).

---

## Classification vs Regression

Both are **supervised**: we have **X** and **Y** and want to predict **Y** for new **X**.

| | Classification | Regression |
|--|----------------|------------|
| **Output Y** | **Categorical** (finite, discrete classes) | **Continuous / numerical** |
| **Examples** | Rain yes/no, spam/not spam, dog/cat, cheat yes/no | Petrol price, stock price, salary, vehicle mileage |
| **Number of possible values** | Fixed (e.g. 2, 3, 5) | Effectively infinite (any number in a range) |

- **Classification:** Predict one of a **fixed set of categories** (e.g. spam vs not spam, malignant vs benign).
- **Regression:** Predict a **numeric value** (e.g. price, salary, distance).

---

## Classification in More Detail

- Data is often in **tabular form**: rows = records (tuples), columns = **attributes**. One special attribute is the **class label** (target **Y**); the rest are **X**.
- **Goal:** Build a model that, for a **new or unseen** record (given only **X**), assigns a **class label** as accurately as possible.

**Example – Cheat detection:**

- Attributes: e.g. Refund (yes/no), Marital status (single/married/divorced), Taxable income.
- Class label: Cheat (yes/no).
- Training: Learn from many (X, Y) pairs. At test time: given only X (e.g. refund=no, marital=married, income=125K), predict cheat = yes or no.

---

## Training and Testing a Classification Model

1. **Split data:** Divide the full dataset into two **disjoint** parts:
   - **Training set** — used to **build** the model **f**.
   - **Test set** — used to **evaluate** the model (never used for training).

2. **Training phase:**
   - Use **training data** (X and Y) and a **learning algorithm** to obtain the model **f**.
   - **f** captures the relationship between X and Y.

3. **Testing phase:**
   - Take **test data** (we have both X and true Y, but **ignore Y** for the moment).
   - Feed **only X** from each test record into **f**; get **predicted Y**.
   - **Compare** predicted Y with the **true Y** (which we had hidden).
   - If they match often → model is good; if not → model needs improvement.

4. **Deployment:** Once performance is satisfactory, use **f** in the real world: input **X**, output predicted **Y**.

> **Exam tip:** Training data → build **f**. Test data → measure performance; test set must be **independent** of training (no overlap). Never evaluate only on training data for final performance.

---

## Real-World Applications (Recap)

**Classification (discrete labels):**

- Weather: rain vs no rain.
- Spam: spam vs not spam.
- Cheat detection: cheated vs not.
- Image: dog vs cat (or multi-class).
- Medical: malignant vs benign; disease vs no disease.

**Regression (continuous output):**

- Petrol/oil/gold/stock price.
- Salary given age/experience.
- Vehicle mileage (e.g. km/l).
- Stopping distance given speed.

---

## Summary

- **Supervised learning** = learning from **(X, Y)** to predict **Y** for new **X**.
- **Classification:** Y is categorical (finite classes).
- **Regression:** Y is continuous/numerical.
- **Process:** Split data → train on training set → test on separate test set → deploy if good.
- Use this note for exam questions on definitions, classification vs regression, and train/test procedure.
