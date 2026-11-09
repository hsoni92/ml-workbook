# Optimization Methods for Analytics — Revision Mind Map

> Week notes now exist for weeks 2, 3, 5, 6, 7 and 8 (see [README](README.md)). The map below follows the planned course structure; the Week 1 introduction recording was not available (its export duplicated the gradient-descent session), so Week 1 has no note.

## Planned week coverage (from course structure)

| Week | Typical focus (optimization for analytics) |
| --- | --- |
| 1 | Introduction: models, variables, objectives, constraints; OR vs ML optimizers |
| 2 | Linear programming formulation; geometry of feasible region |
| 3 | Simplex method; basic feasible solutions; optimality conditions |
| 4 | Duality; shadow prices; sensitivity |
| 5 | Nonlinear optimization; convex sets and functions |
| 6 | Unconstrained methods: gradient descent, Newton; line search |
| 7 | Constrained NLP: KKT conditions; Lagrange multipliers |
| 8 | Integer / mixed-integer programs; applications in analytics |

---

## Core vocabulary

```
OPTIMIZATION = minimize (or maximize) f(x) subject to constraints
FEASIBLE SET = all x that satisfy constraints
OPTIMAL x* = feasible point with best objective value
```

| Symbol | Meaning |
| --- | --- |
| $x$ | Decision variables (what we choose) |
| $f(x)$ | Objective (cost, error, negative profit) |
| $g_i(x) \le 0$, $h_j(x) = 0$ | Inequality / equality constraints |

**LP** — linear objective + linear constraints; optimum at **vertex** of polyhedron (if bounded)

**NLP** — nonlinear $f$ and/or constraints; may need local vs global optima

**MIP** — some variables integer (assignments, facility open/close, cardinality)

---

## Linear programming (Weeks 2–4)

- **Standard form** — minimize $c^T x$ s.t. $Ax = b$, $x \ge 0$
- **Slack/surplus** — turn inequalities into equalities + nonnegativity
- **Simplex** — move along edges; pivot to improving adjacent vertex
- **Degeneracy** — zero steps possible; tie-breaking rules matter in theory
- **Duality** — every LP has dual; **weak** $d^T y \le c^T x$; **strong** at optimum (if both feasible)
- **Shadow price** — dual variable = rate of improvement in objective per unit relaxation of constraint
- **Sensitivity** — how optimal $x^*$ and value change with $c$, $b$, $A$

---

## Convexity and nonlinear methods (Weeks 5–7)

- **Convex set** — line segment between any two points stays in set
- **Convex function** — local minimum = global minimum (on convex domain)
- **Gradient** $\nabla f$ — direction of steepest ascent; **descent** $= -\nabla f$
- **GD update** — $x_{k+1} = x_k - \alpha_k \nabla f(x_k)$; step $\alpha_k$ from line search or schedule
- **Newton** — uses Hessian; faster near optimum, costly per step
- **Constraints** — **Lagrangian** $L(x,\lambda) = f(x) + \sum \lambda_i h_i(x)$; **KKT**: stationarity, primal/dual feasibility, complementarity

$$\nabla f(x^*) + \sum_i \lambda_i \nabla h_i(x^*) = 0$$

---

## Analytics applications (cross-cutting)

| Problem | Optimization view |
| --- | --- |
| Regression | Minimize MSE / regularized loss |
| SVM | Margin maximization with constraints |
| Portfolio | Mean-variance or CVaR under budget constraints |
| Routing / assignment | Integer programs |
| Hyperparameter search | Black-box vs constrained budget |

**OR vs ML** — OR emphasises **provable feasibility** and interpretable constraints; ML often optimizes surrogate losses at scale with heuristics (Adam, early stopping)

---

## When week notes exist — refresh checklist

1. Run `transcripts-to-notes` per week
2. `rename-notes-by-topic.py` + `number-notes.py`
3. Replace the week table above with exam traps and formulas from each note's Quick Revision section

---

## Exam traps (generic)

- Maximization ↔ minimize: multiply objective by $-1$
- Forgetting **nonnegativity** on slack variables in standard LP form
- Confusing **dual price** with primal variable value
- Claiming **global** optimum for non-convex NLP without justification
- Integer problems — **relaxing** integrality gives a **lower bound** (min problem), not the true optimum
