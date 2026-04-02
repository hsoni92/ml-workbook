# AI, ML and Deep Learning – Artificial Neural Networks (Module 1)

## Learning Objectives

By the end of this video you will:

1. **Define** and clearly **distinguish** between Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning.
2. **Identify** where neural networks fit in the overall AI ecosystem.
3. **Explain** the feature-engineering bottleneck in classical ML and why deep learning addresses it.

---

## Why Definitions Matter

The terms **AI**, **ML**, and **deep learning** are used everywhere—chatbots, self-driving cars, recommendation systems, camera filters. For this course we need a **precise engineering definition**, not a marketing one. This note places AI, ML, and deep learning into a **single functional framework** so you know exactly where neural networks fit in the overall AI ecosystem.

---

## Artificial Intelligence (AI)

### Engineering Definition

From an **engineering perspective**, an **artificial intelligence system** is any system that:

1. **Perceives** its environment
2. **Makes decisions**
3. **Takes actions**
4. In order to **maximize a defined objective**

So at its core, every AI system follows this loop:

| Step | Meaning |
|------|--------|
| **Perception** | Take in information from the environment (sensors, data). |
| **Decision** | Choose what to do based on that information. |
| **Action** | Execute the chosen behavior. |
| **Feedback** | (Implicit) Outcome influences future perception and decisions. |

### Examples

- **Self-driving car**: Perceives the road through sensors → decides how to steer and brake → acts through its control system.
- **Recommendation system**: Perceives user behavior → decides what content to show → acts by ranking items.

### What We Are *Not* Defining

In this definition we are **not** talking about consciousness or human-like thinking. We are purely talking about **goal-driven, intelligent behavior implemented computationally**.

> **Exam tip:** AI = perception → decision → action to maximize an objective. No need to mention consciousness.

---

## Two Paradigms of AI

Historically, AI has been built using two very different paradigms.

### 1. Symbolic or Rule-Based AI

- **Idea:** Intelligence is **encoded manually** using:
  - If–then rules
  - Logic
  - Knowledge bases
- **Era:** Dominant from the **1950s to the late 1980s**.
- **Examples:** Expert systems in medicine and engineering.

### 2. Data-Driven AI

- **Idea:** The system **does not rely on human-written rules**. Instead it **learns behavior directly from data** using statistics and optimization.
- **Era:** The **modern approach**.
- **Reality:** Today’s AI systems—whether in vision, speech, language, or recommendation—are **almost entirely data-driven**. This is where **machine learning** enters the picture.

---

## Machine Learning (ML)

### Definition

**Machine learning** is the branch of AI where we **allow the system to learn a function from data** instead of programming the rules manually.

### Mathematical Form

We assume the system learns a function of the form:

**f(x; θ)**

where:

- **x** = input data
- **θ** (theta) = model parameters
- **f** = the function, **trained** using a **loss function** and an **optimization algorithm** (e.g. gradient descent).

### Four Essential Components of Every ML System

| Component | Role |
|-----------|------|
| **Data** | Historical examples the system learns from. |
| **Model** | The function f(x; θ) that maps inputs to outputs. |
| **Loss function** | Measures how wrong the model’s predictions are; we minimize it. |
| **Optimization method** | e.g. **gradient descent** — updates parameters so the loss decreases. |

So instead of **writing rules** for decision-making, we **optimize the model parameters** so that the system performs well on the historical data.

> **Exam tip:** ML = learn f(x; θ) from data using loss + optimization. No hand-coded rules for the mapping.

---

## Limitations of Classical Machine Learning

### The Feature-Engineering Bottleneck

In **classical machine learning**:

- The **model learns parameters** (e.g. weights in a linear model).
- The **features are designed by humans**.

Examples of **hand-designed features**:

| Domain | Hand-designed features |
|--------|-------------------------|
| **Computer vision** | Edges, textures, SIFT, HOG, etc. |
| **Text analysis** | TF-IDF, bag of words, n-grams. |
| **Speech** | MFCCs (Mel-frequency cepstral coefficients). |

This creates the **feature-engineering bottleneck**:

- The performance of the model often **depends more on the quality of handcrafted features** than on the learning algorithm itself.
- Human-designed features **do not scale well** when:
  - Data becomes more complex,
  - Dimensionality becomes very high,
  - Patterns become highly abstract.

This bottleneck is the **main reason** we need something beyond classical ML.

---

## Deep Learning

### Definition

**Deep learning** is a **subfield of machine learning** where we use **deep neural networks** to learn:

- Not only the **model parameters**, but also
- The **features and representations** themselves.

### How It Differs from Classical ML

- **Classical ML:** We use a **single** function f(x). **Features are fixed**; only **parameters** are learned.
- **Deep learning:** We use a **composition of many functions** (many layers). **Each layer** transforms the data into a **new representation**. **Features, representations, and parameters** are **all learned jointly** from the data.

So:

| | Classical ML | Deep learning |
|---|--------------|----------------|
| **Features** | Fixed, human-designed | Learned from data |
| **Parameters** | Learned | Learned |
| **Representations** | Hand-crafted | Learned layer by layer |
| **Function form** | Often single f(x) | Composition of many layers f_L(…f_2(f_1(x))…) |

> **Exam tip:** In classical ML, features are fixed and only parameters are learned. In deep learning, features, representations, and parameters are all learned jointly.

---

## Relationship: AI ⊃ ML ⊃ Deep Learning

Think of them as **nested sets**:

- **Artificial intelligence** = the **broadest** field (all goal-driven intelligent systems).
- **Machine learning** = a **subset of AI** that focuses on **learning from data**.
- **Deep learning** = a **subset of machine learning** that uses **deep neural networks**.

So:

- Every **deep learning** system is a **machine learning** system.
- Every **machine learning** system is an **AI** system.
- The **reverse** is not true (not every AI system uses ML; not every ML system uses deep learning).

---

## Why Neural Networks Are the Core of Modern AI

Neural networks have become the **core engine** of modern AI because they enable:

1. **Automatic feature learning** — no need to hand-design features.
2. **High-dimensional representation learning** — scale to very large input spaces.
3. **End-to-end differentiable optimization** — one loss, one training loop for the whole pipeline.
4. **Large-scale parameter learning** — millions or even billions of parameters.

They allow us to **train systems directly from raw**:

- Pixels (vision)
- Audio (speech)
- Text (NLP)

This capability powers **modern computer vision**, **speech recognition**, **natural language processing**, **recommendation systems**, and **generative AI models**.

---

## Summary and Exam-Ready Takeaways

- **AI** = umbrella field of goal-driven intelligent systems (perceive → decide → act to maximize an objective).
- **ML** = data-driven AI that **learns model parameters** from data (data + model + loss + optimization).
- **Deep learning** = ML using **deep neural networks**; it learns **features, representations, and predictions jointly**.
- **Classical ML** = fixed, human-designed features → **feature-engineering bottleneck**.
- **Deep learning** = learned features and representations → scales to complex, high-dimensional, abstract patterns.
- **Neural networks** sit inside ML, which sits inside AI; they are the main engine of modern AI because of automatic feature learning, representation learning, and end-to-end optimization.

**Bridge to next video:** Why did deep learning suddenly start working so well, even though neural networks have existed for decades?

---

## Quick Revision and Exam Checklist

- [ ] Give the **engineering definition of AI** (perceive, decide, act, maximize objective).
- [ ] Name the **two paradigms** of AI (symbolic vs data-driven) and which one dominates today.
- [ ] Define **machine learning** and state the **four components** (data, model, loss, optimization).
- [ ] Explain the **feature-engineering bottleneck** in classical ML with examples (e.g. edges, TF-IDF, MFCCs).
- [ ] Define **deep learning** and contrast it with classical ML (fixed vs learned features/representations).
- [ ] Draw the **nested relationship**: AI ⊃ ML ⊃ Deep learning.
- [ ] List **why neural networks** are the core of modern AI (automatic feature learning, representation learning, end-to-end optimization, scale).
