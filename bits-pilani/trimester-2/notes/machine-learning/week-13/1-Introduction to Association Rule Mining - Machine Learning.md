# Introduction to Association Rule Mining

## 1. Unsupervised pattern discovery in transactions

**Association rule mining** finds **frequent co-occurrences** among **items** in transactional data (market baskets, click streams, log **itemsets**).

**Contrast:**

- **Clustering:** similarity of **rows** (customers, documents).
- **Association rules:** patterns among **columns/items** within **transactions**.

**Not prediction of a single target** in the supervised sense—it quantifies **co-occurrence strength** (used for layout, bundles, recommendations).

---

## 2. Transaction format

Rows = **transactions** (orders, sessions); values = **items** purchased or **binary** presence in basket. Typical preprocessing: **binary** “item present / absent” per row (multiplicity often ignored in basic treatments).

**Cloud example:** which **API** endpoints appear together in **sessions** for dependency or cache **bundling**.

---

## 3. Two-stage mining view

1. Find **frequent itemsets** (item groups appearing often).
2. Derive **rules** \(X \Rightarrow Y\) with quality measures (**support**, **confidence**—next notes).

---

## 4. Applications

- **Market basket:** bundle pricing, **shelf** placement (place associated items nearby).
- **Recommendations:** “customers who bought X also bought Y.”
- **Inventory:** regional **spare-part** co-failure patterns.
- **Clickstream / logs:** frequent path segments.

---

## 5. Related pattern types

- **Frequent itemset:** set of items co-occurring often.
- **Frequent subsequence / substructure:** ordered or structured variants (advanced).

---

## Common Pitfalls / Exam Traps

- Treating association as **causation**—**correlation** of baskets, not causal impact.
- Ignoring **seasonality**—rules drift over time.
- Using raw **counts** without **support** denominators—rules look strong on tiny bases.

---

## Quick Revision Summary

- **Association mining:** frequent **item co-occurrence** in transactions.
- **Unsupervised** on transactional logs.
- Pipeline: **frequent itemsets** \(\rightarrow\) **rules** with quality metrics.
- **Applications:** retail layout, bundles, recommendations, inventory.
- Distinguish **association** from **causal** claims.
