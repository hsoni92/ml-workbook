# Fairness Metrics and Detection - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. **Explain** why fairness must be measured explicitly.
2. **Describe** common fairness metrics such as demographic parity, equal opportunity, and equalized odds.
3. **Recognize** that different fairness metrics can conflict and require trade-offs.

---

## Why This Topic Matters

Once we accept that fairness is different from accuracy, we need a practical way to detect unfair behavior.

That is the role of fairness metrics.

A model may show 90% overall accuracy and still behave very differently across groups. Fairness metrics force us to stop looking only at averages and start asking:

- Who receives positive outcomes?
- Who gets missed?
- Which groups experience higher error rates?

---

## The Starting Point: Group-Wise Evaluation

Fairness detection usually begins by identifying relevant protected or sensitive attributes, such as:

- gender,
- race,
- age group,
- other context-specific categories.

We then split the validation data by group and compute performance separately.

This is the key shift:

- standard evaluation asks, **"How good is the model overall?"**
- fairness evaluation asks, **"How does the model behave for different groups?"**

---

## Why Accuracy Is Not Enough

Imagine a loan approval model with high overall accuracy.

Now suppose:

- Group A receives approvals 80% of the time,
- Group B receives approvals only 50% of the time,
- and the two groups have similar financial profiles.

The aggregate metric hides an important disparity.

This is why fairness must be measured directly rather than assumed from strong predictive performance.

---

## Common Fairness Metrics

| Metric | Informal meaning | What it checks |
|---|---|---|
| **Demographic parity** | Are positive outcomes assigned at similar rates? | Compares approval or selection rates across groups |
| **Equal opportunity** | Are qualified people treated similarly? | Compares true positive rates across groups |
| **Equalized odds** | Are both positive recognition and error behavior balanced? | Compares both true positive and false positive behavior |

These metrics reflect different ideas of what it means to be fair.

That is important: fairness is not one single definition.

---

## Intuition Behind the Metrics

### Demographic parity

This focuses on outcome rates.

Example: are loan approvals equally frequent across groups?

### Equal opportunity

This focuses on qualified individuals.

Example: among applicants who truly deserve approval, are some groups being missed more often than others?

### Equalized odds

This goes further by considering multiple kinds of error.

Example: are both correct approvals and incorrect approvals balanced across groups?

---

## A Crucial Reality: Metrics Can Conflict

One of the most important ideas in fairness is that these metrics can be incompatible.

If two groups have different base rates, it may be mathematically difficult or impossible to satisfy multiple fairness definitions at the same time.

That means fairness is not something we can "solve once" with one formula.

Instead, choosing a metric often reflects:

- the application context,
- the type of harm we care most about,
- the values and policy goals of the system.

---

## Fairness Detection in Practice

A practical fairness detection workflow looks like this:

1. Identify protected attributes relevant to the application.
2. Slice the validation data by group.
3. Compute standard task metrics for each group.
4. Compute fairness metrics and disparity gaps.
5. Investigate any large or harmful differences.
6. Continue monitoring after deployment.

This last point matters because fairness can change over time as data and user populations shift.

---

## Common Misunderstandings

- **"There is one universal fairness metric."**
  Different metrics capture different ethical goals.

- **"Once fairness is measured, the problem is solved."**
  Measurement is only the first step.

- **"Fairness evaluation is a one-time certification."**
  Fairness must be monitored continuously because distributions change.

---

## Summary and Exam-Ready Takeaways

- Fairness must be measured explicitly because overall accuracy can hide disparities.
- Fairness detection begins with group-wise evaluation using protected or sensitive attributes.
- Demographic parity, equal opportunity, and equalized odds represent different notions of fairness.
- These metrics can conflict, especially when groups have different base rates.
- Metric choice is a value-laden design decision, not just a mathematical one.
- Fairness monitoring should continue during deployment, not stop after validation.

---

## Bridge to the Next Note

Once unfairness has been detected, the next practical question is:

**What can we do to reduce it?**
