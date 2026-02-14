# Introduction to Decision Trees – Machine Learning (Module 4)

## Learning Objectives

By the end of this video you will:

1. **Define** a decision tree and its **role in classification**.
2. **Identify** core components: **root node**, **internal/decision nodes**, **branches/edges**, **leaf nodes**.
3. **Distinguish** **tree induction** (building the tree) vs **tree deduction** (using the tree for prediction).
4. **Explain** why decision trees are **white-box** and **easy to set up**.
5. **Trace** a simple example: tax-evasion (refund, marital status, taxable income) → approve/reject.

---

## Where Decision Trees Fit

- **ML** → **Supervised** → **Classification** (predict categorical label). **Decision trees** are a widely used **classification** algorithm.
- **Analogy:** Put items into **predefined buckets** (e.g. apple → bin 1, orange → bin 2). The tree implements a hierarchy of **questions** that route each sample to a **leaf** (class label).

**Applications:** Spam vs non-spam, loan approve/reject, medical diagnosis, etc.

---

## Human-Like Decision Making

Decision trees mirror how **humans** make decisions by a **sequence of criteria**:

**Example – Laptop purchase:**  
Criteria in order: Processor (e.g. i7?) → RAM (e.g. 64 GB?) → Disk (e.g. 1 TB?) → GPU. Each “yes/no” or “which value?” narrows the set; finally one laptop (or one class) is chosen.

**Example – Loan application:**  
Salaried? → Yes/No. If yes: ITR &gt; 10 lakh? → Approve/Reject. If no: ITR &gt; 20 lakh? → Approve/Reject. Again a **tree of questions** leading to **approve** or **reject**.

---

## Structure of a Decision Tree

| Component | Role |
|-----------|------|
| **Root node** | Top of the tree; first decision (one attribute + condition). |
| **Internal (decision) nodes** | Non-leaf nodes; each holds an **attribute + condition** and branches. |
| **Branches / edges** | Connect nodes; each branch corresponds to an **attribute value** (or range). |
| **Leaf nodes** | **Terminal** nodes; contain the **class label** (e.g. Approve, Reject, Yes, No). |

So: **non-leaf** = decision points (attribute + condition); **leaf** = predicted class.

---

## Why Decision Trees Are Popular

1. **White-box / interpretable:** We can **trace the path** from root to leaf and **explain** exactly why a sample got a particular class (e.g. “Salary=Yes, ITR&gt;10L → Approved”). Transparent for users and stakeholders.
2. **Easy to set up:** Require **minimal data pre-processing** compared to many other algorithms.

---

## Two Phases: Induction and Deduction

| Phase | Meaning |
|-------|---------|
| **Induction** | **Building** the tree from **training data** (how to choose attributes, how to split). This is the **training** phase. |
| **Deduction** | **Using** the built tree to **predict** for **new/unlabeled** data. Start at root, follow branches by attribute values, end at a leaf → that leaf’s label is the prediction. |

---

## Building a Tree (Induction) – High-Level

- **Input:** Tabular training data (e.g. Refund, Marital status, Taxable income; class = Cheat Yes/No).
- **Idea:** At each node, **choose an attribute** and **split** the data so that **child nodes** become as **pure** (homogeneous) as possible — ideally all one class.
- **Process:** Start at root → pick “best” attribute → split into children → repeat for impure children until a **stopping condition** (e.g. pure node, no more attributes, or pre-pruning). Details (how to choose “best” attribute, how to split) come in later videos.

**Example (simplified):**  
Root = Refund. Branch “Yes” → all “No” cheat → **leaf: No**. Branch “No” → mixed → split again by Marital status (e.g. Single/Divorced vs Married) and possibly Taxable income (e.g. &gt;80K) to get leaves Approve/Reject or Yes/No.

---

## Using the Tree (Deduction)

- **Input:** One **test** record (only **X**; no class label).
- **Process:** Start at **root**; check the attribute value (e.g. Refund = No) → follow the matching branch → next node; repeat until you reach a **leaf**.
- **Output:** The **class label** at that leaf is the **prediction**.

**Example:** Refund=No → Marital status=Married → (e.g. no further split) → **Leaf: No** (e.g. “not cheat” or “reject”). Prediction = No.

---

## Summary

- **Decision tree** = tree of **decision nodes** (attribute + condition) and **leaf nodes** (class labels). **Branches** = attribute values.
- **Induction** = building the tree from data; **deduction** = predicting by traversing from root to leaf.
- **White-box** and **easy to set up**; good for interpretation and quick prototyping.

Use this note for structure of a decision tree, induction vs deduction, and tracing a simple prediction path.
