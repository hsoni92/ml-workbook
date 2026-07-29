# Content to Stories — Examples

## Filled section (Mode A)

Source concept: single neuron / perceptron.

```markdown
## Neuron as a Simple Feature Detector

**The Story:** Think of each neuron as a **bouncer at a club** with a specific guest list (the weights). The bouncer checks: "Does this person (input) match my list?" If yes → let them in (activate). If no → turn them away (stay silent).

The **set of weights** in a neuron IS the template/list. The input is checked against it. Strong match = strong activation.

**One neuron = one simple pattern detector.** That's why it's weak on its own — one bouncer can't run a whole club.

**Exam Tip:** Weights define the template; activation is the threshold decision. One neuron = linear decision boundary only.

> **One neuron** = weighted evidence aggregation = one simple pattern detector
```

## Week-level section with table (Mode A variant)

```markdown
## Week 3 — Practice Test vs Final Exam (Evaluation)

**The story:** **Training error** is how you do on homework you already saw. **Test error** is the final exam on **unseen** questions. A model that only crushes homework has not proved it **generalizes**.

| Story | ML term |
|-------|---------|
| Homework score | **Train** error |
| Final exam | **Test** error |
| Tally of hits and misses | **Confusion matrix** |
| Trust of positive alarms | **Precision** |
| Catch rate of true problems | **Recall** |

> **Choose metrics to match the cost of mistakes — not every problem treats FP and FN equally.**

**Key properties / pitfalls:**
- High accuracy + rare positives can hide a useless detector.
- **Overfitting:** low train error, high test error — memorized noise.
```

## Standalone story opening (Mode B)

```markdown
# Finding the Best Split — The Wedding Planner Story

## Context
**Source:** bits-pilani/trimester-2/notes/machine-learning/week-4/2-Finding the Best Split.md
**Topic:** Decision Tree splitting criteria — Entropy, Gini, Information Gain
**Date:** 2026-05-01

---

## The Story

Imagine you're a **wedding planner**. Your job? Seat 100 guests at tables so that every table has people who **actually like each other**. No awkward silences. Every table = one tribe.

That's literally what a decision tree does — it's a seating planner.
```

## ONE-LINE SUMMARIES excerpt

```markdown
# ONE-LINE SUMMARIES — The Complete Set

> **AI** = perceive → decide → act toward a goal
> **ML** = learn f(x;θ) from data instead of programming rules
> **Chain rule** = multiply your way back from loss to weights
> **ReLU** = light switch: on if positive, off if negative
> **Dropout** = train while randomly removing team members
```

## Weak vs strong analogies

**Weak:** "Gradient descent is like walking down a hill." (too generic; no mechanism)

**Strong:** "At any point on the loss mountain, the gradient is the direction of steepest ascent. Flip the sign, and it's steepest descent — which way to take the next step. The blind hiker can't see the whole mountain; they feel the slope underfoot and take small steps until no direction goes lower."

The strong version names direction, magnitude, and the update rule's *why*.
