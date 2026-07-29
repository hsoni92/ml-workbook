# Examples — Student Voice

## Good (notebook markdown)

```markdown
## Baseline — Logistic Regression

I trained logistic regression on scaled, one-hot encoded features (without `duration`).
With `class_weight='balanced'`, validation PR-AUC was 0.38 and F1 about 0.31.
That is a reasonable floor — the MLP should beat this without relying on leaky features.
```

## Bad (AI slop — do not use)

```markdown
## Baseline Model Results

In this comprehensive analysis, we leveraged a robust logistic regression model to establish
a strong baseline. The results demonstrate excellent performance and provide valuable insights
into our data landscape. It's worth noting that this foundational approach sets the stage for
our cutting-edge neural network exploration.
```

## Good (written answer)

The marketing funnel breaks down because awareness does not convert to trial in our segment.
From the case data, trial rate is 4% versus 11% for the industry benchmark (p. 12), so the
gap is in consideration, not reach. I would test a shorter onboarding flow before spending
more on top-of-funnel ads.

## Bad (written answer)

Marketing is a multifaceted landscape where organizations must leverage holistic strategies
to unlock robust growth. It is worth noting that a comprehensive approach to the funnel
empowers teams to dive deep into customer journeys and deliver cutting-edge outcomes.

---

## Course-specific example: ML project notebook

Use this structure only when the brief asks for an ML pipeline. Sections come from the assignment — not from this list.

Typical progress-report sections for a modelling project:

1. Data Preparation
2. EDA
3. Feature Engineering (or justify if skipped)
4. Baseline Model
5. Model Comparison (at least one alternative)
6. Hyperparameter Tuning
7. Evaluation
8. Planned Improvements

Example paths in this repo (Apex Project-2):

- Brief: `bits-pilani/trimester-3/apex-project/week-5-submission/note-from-faculty.txt`
- Outline: `bits-pilani/trimester-3/apex-project/project-outline.md`
- Prior notebook: `bits-pilani/trimester-3/apex-project/Apex2_Week2_Notebook_2025EM1100506_Himanshu_Soni.ipynb`

Always read the current week's faculty note — section names and file naming may differ.

---

## AI authorship markers — avoid in college work

### Bad (reveals AI or template scaffolding)

```markdown
## Task 2: Traditional Machine Learning Pipeline

As per the assignment requirements, below is a comprehensive implementation of the
traditional ML pipeline. This section addresses Task 2 and demonstrates robust
sentiment classification using TF-IDF vectorization.

[Insert accuracy results here]
```

```python
# Step 1: Load the NLTK Movie Reviews dataset as required by the assignment
# Step 2: Apply comprehensive text preprocessing
print("Preprocessing complete! Moving to the next step...")
```

### Good (sounds like a student who ran the work)

```markdown
## TF-IDF + Logistic Regression

I vectorized the cleaned reviews with TF-IDF (max 5000 features, English stop words removed)
and trained logistic regression with `class_weight='balanced'`.
On the held-out 20% test set, accuracy was 0.86 and F1 was 0.85 — slightly better than Naive Bayes.
Training took under 2 seconds on my laptop.
```

```python
# 80/20 split — same test set for all three pipelines
X_train, X_test, y_train, y_test = train_test_split(
    reviews, labels, test_size=0.2, random_state=42, stratify=labels
)
```
