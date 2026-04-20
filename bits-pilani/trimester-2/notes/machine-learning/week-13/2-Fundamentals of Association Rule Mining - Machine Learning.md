# Fundamentals of Association Rule Mining

## 1. Terminology

- **Itemset:** any subset of items (e.g. \(\{\text{milk}, \text{bread}\}\)).
- **k-itemset:** itemset of **size** \(k\).
- **Support count:** number of transactions **containing** the itemset.
- **Support** (fraction):
  \[
  \text{supp}(X) = \frac{\text{\# transactions containing } X}{\text{total transactions}}
  \]
- **Frequent itemset:** \(\text{supp}(X) \geq \text{minSupp}\) (user threshold).

---

## 2. Association rule

Notation: \(X \Rightarrow Y\) where \(X \cap Y = \emptyset\) (disjoint itemsets).

**Support of rule** \(X \Rightarrow Y\):
\[
\text{supp}(X \Rightarrow Y) = \text{supp}(X \cup Y)
\]
(same for any rule built from the **same** union itemset—different splits change **confidence**, not support).

**Confidence:**
\[
\text{conf}(X \Rightarrow Y) = \frac{\text{supp}(X \cup Y)}{\text{supp}(X)} = P(Y \mid X) \text{ (empirical)}
\]

**Interpretation:** among transactions containing **X**, what fraction also contains **Y**.

---

## 3. Key observation

From a fixed frequent itemset **Z**, many rules \(X \Rightarrow Z\setminus X\) share the **same support** (that of **Z**) but **different confidence** values.

---

## 4. Brute-force blowup

If there are **d** distinct items, there are **2^d** possible itemsets (excluding empty depending on convention). Rules scale **worse**—enumeration is **intractable** for large **d**.

---

## 5. Apriori principle (anti-monotonicity)

If \(X \subseteq Y\) then \(\text{supp}(Y) \leq \text{supp}(X)\).

**Contraposition:** if **X** is **infrequent**, **every superset** of **X** is infrequent \(\Rightarrow\) **prune** the exponential lattice **early**.

This is the logical backbone of the **Apriori** algorithm (next note).

---

## Common Pitfalls / Exam Traps

- Mixing **support count** vs **support** fraction in formulas.
- Thinking **confidence** can exceed 1—it's a **conditional** fraction.
- Forgetting **X** and **Y** must be **disjoint** in standard rule statements.

---

## Quick Revision Summary

- **Itemset**, **k-itemset**, **support** / **support count**, **frequent** itemset.
- Rule **support** = support of **X ∪ Y**; **confidence** = supp(X∪Y)/supp(X).
- Same itemset **Z** \(\Rightarrow\) same **support** for all derived rules; **confidence** differs.
- **2^d** itemsets—brute force fails.
- **Apriori principle:** subset **frequent** \(\Rightarrow\) supersets **bounded**; infrequent subset **prunes** supersets.
