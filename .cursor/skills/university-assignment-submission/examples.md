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
