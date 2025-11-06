# Feature Engineering for Predictive Modeling - House Prices Dataset

## Overview

Your ability will be judged by **how thoughtful and justified** your feature engineering decisions are. You are not graded on model accuracy - the focus is data reasoning.

**Due Date:** 07 November 2025 10:00 PM
**Available From:** 24 October 2025 10:00 PM
**Available Until:** 07 November 2025 10:00 PM

---

## Dataset

**Kaggle Competition:** House Prices - Advanced Regression Techniques

**Dataset Link:** https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data

You are provided with a dataset containing property details and sale prices.

---

## Assignment Objectives

Your task is to design and execute a feature engineering strategy that transforms this raw dataset into a version ready for predictive modeling.

Your final dataset should be suitable for machine learning, but you are **not required to train or interpret a model**. The goal is to demonstrate strategic thinking, technical correctness, and justification of each choice you make during data preparation.

---

## Assignment Tasks

There are no fixed instructions - you must decide:

- Which data issues to clean, modify, or ignore
- Which transformations to apply and why
- Which features to create, merge, or remove
- Whether to apply dimensionality reduction, and to what extent
- How to represent text-based or categorical data meaningfully

Your notebook should clearly show:

- The decisions you made, not just the operations you ran
- Why each technique was chosen
- Evidence (plots, metrics, reasoning) that supports those choices

---

## Specific Instructions: Student-Specific Feature

Each student must generate a **unique feature** based on their student ID.

### Steps:

1. Let `ID_last7` = last 7 digits of your student ID.
   - Example: for ID `2025EB1100221`, `ID_last7 = 1100221`

2. Use the following random function code snippet to generate a new column in your dataset:

```python
import numpy as np

def generate_student_feature(df, ID_last7):
    np.random.seed(ID_last7 % 1000)
    return np.random.randint(low=1, high=100, size=len(df)) + (ID_last7 % 7)
```

3. Add this new column to your dataset as: `student_random_feature`

4. Treat it like any other numeric variable:
   - Include it in your EDA, correlation analysis and dimensionality reduction (if applied)
   - Decide how to scale or transform it, and justify your choice

---

## Exploratory Data Analysis (EDA)

To ensure originality and understanding, include at least the following visualizations with short explanations:

### Required Visualizations:

- Distribution plots for key numeric features before and after transformation
- Missing-value visualization (bar chart or heatmap)
- Correlation heatmap for numeric features
- Boxplots showing categorical vs. SalePrice relationships
- Scatterplots showing engineered numeric features vs. SalePrice

**Note:** Visuals must include your random feature.

### Required Questions to Answer:

1. Which 3 features appear most correlated with your random feature? Why do you think this occurs?

2. After dimensionality reduction, did your random feature load significantly on any principal component? Explain briefly.

---

## Deliverables

### 1. Jupyter Notebook (.ipynb)

- Must include both **code and output** (fully executed)
- Each key decision (cleaning, transformation, encoding, etc.) should have:
  - A one-line explanation **before** execution
  - Evidence (summary stats, plots, or metrics) **after** execution
- Organize work with clear Markdown headers and concise comments

### 2. Report (PDF)

- Small 1-2 pages PDF
- Summarize your feature engineering pipeline and reasoning behind each key decision

---

## Evaluation Rubric (Total = 40 Marks)

| Criteria | Description | Marks |
|----------|-------------|-------|
| **Data Familiarity & Initial Understanding** | Demonstrates understanding of variable types, data distribution, and relationships; identifies potential data issues independently. | 4 |
| **Data Cleaning Decisions** | Handles missing values, outliers, or inconsistencies logically with clear justification and before–after evidence. | 6 |
| **Numeric Feature Engineering** | Applies appropriate scaling, transformation, or discretization techniques thoughtfully; avoids mechanical use. | 6 |
| **Feature Creation & Encoding** | Constructs meaningful new variables (including random-function feature); applies correct encoding for categorical data. | 8 |
| **Dimensionality Reduction & Correlation Handling** | Identifies redundancy and multicollinearity; applies or justifies PCA or similar technique appropriately. | 6 |
| **Text-Based Feature Representation** | Combines descriptive fields into text; cleans and encodes text meaningfully. | 6 |
| **Documentation & Clarity** | Notebook readability, logical flow, commentary quality, and clarity in the PDF report. | 2 |
| **Bonus** | Shows exceptional creativity or deeper exploration beyond syllabus expectations. | 2 |

---

## Important Notes

- **Avoid using automated pipelines without explanation** - Every transformation must have a clear "why"
- **Simplicity with strong justification** will score higher than complexity without reasoning
- Focus on **data reasoning** over model accuracy
