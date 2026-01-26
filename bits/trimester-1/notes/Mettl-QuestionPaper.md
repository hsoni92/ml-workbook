# Question 1: Normalization

**Dataset:** 10, 20, 30, 40, 50

## (a) Min–Max Normalization (min = 0, max = 1)

**Formula:**

```
x' = (x - x_min) / (x_max - x_min)
```

**Given:**
- Min = 10
- Max = 50

**Result:**
```
[0, 0.25, 0.5, 0.75, 1]
```

## (b) Z-score Normalization

**Formula:**

```
z = (x - μ) / σ
```

**Given:**
- Mean μ = 30
- Standard deviation σ ≈ 14.14

**Calculation of Standard Deviation:**

**Step 1: Calculate deviations from mean (x - μ)**
- (10 - 30)² = (-20)² = 400
- (20 - 30)² = (-10)² = 100
- (30 - 30)² = 0² = 0
- (40 - 30)² = 10² = 100
- (50 - 30)² = 20² = 400

**Step 2: Sum of squared deviations**
Σ(x - μ)² = 400 + 100 + 0 + 100 + 400 = 1000

**Step 3: Calculate standard deviation**
σ = √[Σ(x - μ)² / n] = √(1000 / 5) = √200 ≈ 14.14

**Result (approx):**
```
[-1.41, -0.71, 0, 0.71, 1.41]
```

## (c) Decimal Scaling (scaling factor = 10)

**Formula:**

```
x' = x / 10
```

**Result:**
```
[1, 2, 3, 4, 5]
```

---

# Question 2: Visual Attributes

Visual attributes such as color, size, shape, position, and orientation help encode data visually, making patterns, comparisons, and trends easier to perceive and understand quickly.

---

# Question 3: Spam Detection

## (a) TF-IDF vs Boolean Bag-of-Words

TF-IDF is more useful because it down-weights common words and highlights discriminative terms that are important for distinguishing spam from non-spam emails.

## (b) Why One-Hot Encoding is a Bad Idea

One-hot encoding every unique word leads to extremely high dimensionality, sparsity, and poor scalability, making training inefficient and prone to overfitting.

---

# Question 4: Lakehouse Architecture

## (a) Lakehouse Design

- **Raw Layer:** Stores raw clickstream logs (JSON, CSV, Parquet)
- **Cleaned Layer:** Stores cleaned and structured transactional data
- **Aggregated Layer:** Stores summarized sales reports for analytics (tables, views)

Supports cheap storage + fast SQL analytics on the same platform.

## (b) Benefits of Lakehouse

- Single system for both analytics and storage (no duplication)
- Lower cost and better performance compared to maintaining separate data lake and warehouse

---

# Question 5: Proportion Estimation

## (a) Required Sample Size (99% Confidence)

**Formula:**

```
n = (z² × p(1-p)) / E²
```

**Given:**
- z = 2.576 (99% confidence)
- p = 0.5 (no prior info)
- Margin of error E = 0.05

**Result:**
```
n ≈ 664
```

## (b) 99% Confidence Interval

**Given:**
- Sample size n = 520
- Upgrades = 156 → p̂ = 0.3

**Formula:**

```
p̂ ± z × √(p̂(1-p̂)/n)
```

**Confidence Interval (approx):**
```
(0.25, 0.35)
```

**Interpretation:**
The company can be 99% confident that 25%–35% of users would upgrade, helping guide premium pricing and marketing decisions.
