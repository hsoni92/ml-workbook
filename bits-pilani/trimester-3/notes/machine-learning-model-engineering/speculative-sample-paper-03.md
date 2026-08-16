# Sample Question Paper (Speculative — 3 of 2)

## BITS Digital Comprehensive Examination — Model Question Paper

> **Note:** This is a speculative paper, constructed from the breadth of the course notes to help you practise patterns that did not appear in `sample-paper-01.md` or `sample-paper-02.md`. Question numbering and marks are indicative.

| Field | Value |
|-------|-------|
| Course Title | ML Model Engineering |
| Nature of Exam | Closed Book (No Internet) |
| Weightage | 40% |
| Duration | 2.5 Hours |

### Note to Students

1. Please follow all the Instructions to Candidates given on the cover page of the answer book.
2. Read each question carefully and write to-the-point answer.
3. All parts of a question should be answered consecutively. Each answer should start from a fresh page.
4. Assumptions made if any, should be stated clearly at the beginning of your answer.
5. Show all the calculations/derivations in fair and box/highlight the final answer.

---

## Q.1

### Q.1.1 — Why Monitoring ML Models Is Different (5 Marks)

A model-serving API reports HTTP 200, low latency, and zero errors — yet predictions are getting worse. Explain why **"the service is up" does not mean "the model is good"**, and list the ML-specific signals a monitoring system must track in addition to infrastructure metrics.

#### Answer

**The core insight:** traditional software monitoring asks *"is the system healthy enough to serve requests?"* — CPU, memory, error rate, latency, requests/sec. An ML service can be **perfectly healthy from an infrastructure perspective while being actively wrong**: every request returns 200 in a few milliseconds, but the predictions are based on drifted inputs, changed labels, or a shifted feature–label relationship. Infra metrics give **false confidence**.

**ML-specific signals to add:**

| Signal | What it catches |
|--------|-----------------|
| **Data quality & drift** | PSI / KS on feature distributions, missing-value rate, out-of-range values (covariate drift) |
| **Prediction metrics** | Rolling AUC / precision / recall on freshly labelled data (concept drift) |
| **Label / base rate** | Class-ratio shift (label drift) — affects thresholds even if AUC is stable |
| **Segment fairness** | Group-wise metrics — a 95% global accuracy can hide an 88% group |
| **Business KPIs** | Conversion rate, churn, loss rates — the outcomes the model exists to move |

**Pro tip:** This is the "service is up ≠ model is good" question — the course's favourite framing. The mark structure is: (1) name the two questions (infra vs ML), (2) name the drift types that infra metrics miss ($P(X)$, $P(Y)$, $P(Y\mid X)$), (3) one concrete example where 200 OK hides a wrong model (e.g. fraud model calibrated on 1% fraud rate now seeing 5%). Never answer with infrastructure metrics only.

---

### Q.1.2 — Replication vs Sharding for Scaling Inference (5 Marks)

A single model instance is hitting its QPS ceiling under load. Compare **replication** and **sharding** as scaling primitives for the model-serving layer, and recommend when each is appropriate.

#### Answer

**Replication** runs $N$ identical copies of the **same** model behind a load balancer. Any request can hit any replica.

- **Benefits:** roughly $N\times$ throughput, fault tolerance (a replica can die without taking the service down), no request affinity.
- **Limitations:** does not help a *single* slow request (that needs model optimisation, not more copies); all replicas must stay in sync on model version; cost grows linearly.

**Sharding** divides traffic/data into **subsets**, each served by a dedicated group of model instances — like separate departments per region.

- **Benefits:** each shard is smaller and specialised (e.g. per-geography or per-model routing), so per-shard load and model size are bounded; useful when different slices need different models or data.
- **Limitations:** routing logic is more complex; a shard failure only affects its subset; skewed shards need rebalancing.

**Recommendation:** use **replication first** — it is the standard answer for a single model hitting a QPS ceiling, and it gives HA for free. Introduce **sharding** when there is a natural division of traffic (region, model variant, tenant) or when the model/dataset is too big for one replica to hold, so each shard only serves its slice.

**Pro tip:** The exam shape is *two primitives + when to pick which*. The supermarket analogy helps: more checkout counters (replication) vs separate departments (sharding). Mention the single-request caveat ("replication won't fix a slow model") — it is the trap that separates good answers from great ones.

---

## Q.2

### Q.2.1 — RAG as a Multi-Model System (6 Marks)

Explain how a **Retrieval-Augmented Generation (RAG)** pipeline works, and identify the distinct model components involved. Explain how RAG addresses the problem of an LLM producing answers from stale or hallucinated memorised knowledge.

#### Answer

**RAG = retrieval + generation.** Instead of relying only on what the LLM memorised in its weights, the system retrieves relevant documents from an external knowledge base and feeds them to the generator as context. Intuition: an **open-book exam** (RAG) vs a **closed-book exam** (pure LLM) — the open-book student looks up passages before writing.

**Pipeline stages:**

1. **Embed the query** — an embedding model converts the user query into a dense vector.
2. **Retrieve top-K documents** — the query vector searches a **vector database** of pre-embedded document chunks; returns the most similar chunks.
3. **Re-rank (optional)** — a **reranker** (e.g. cross-encoder) refines the ordering by scoring (query, document) pairs directly.
4. **Generate** — the generator LLM receives the query plus the retrieved chunks as context and produces a **grounded** answer.

**Multi-model components:**

| Role | Function | Example |
|------|----------|---------|
| Embedding model | Text → dense vector | `text-embedding-3-small`, BGE, E5 |
| Vector database | Store + ANN search over vectors | Pinecone, Milvus, pgvector |
| Reranker | Refine retrieval order | Cross-encoder, Cohere Rerank |
| Generator LLM | Produce final grounded text | GPT-4, Llama, Mistral |

**Why RAG fixes stale/hallucinated answers:** the generator is *anchored* to retrieved evidence from the current knowledge base. Facts that changed after training (or were never in training) come from retrieval, not from memorised weights; the answer can cite the source. It also avoids retraining for every knowledge update — you update the knowledge base instead of the model. It does **not** fully eliminate hallucination (the generator can still ignore the context), but it grounds generation in fresh, external, attributable information.

**Pro tip:** Multi-model questions are scored on *component identification* — name all four roles (embedder, vector DB, reranker, generator). The one-sentence "open-book vs closed-book" intuition anchors the answer. Mention the two failure notes examiners like: reranking is optional-but-improves-quality, and RAG reduces but does not eliminate hallucination.

---

### Q.2.2 — Exact vs Approximate Nearest-Neighbour Search (4 Marks)

A RAG system must serve search over 100 million vectors in under 50 ms. Compare **exact nearest-neighbour (ENN)** search with **approximate nearest-neighbour (ANN)** search, and describe the key trade-off you would tune.

#### Answer

**Exact search (ENN)** compares the query against every stored vector — guaranteed correct but $O(N)$ per query: fine at 10k vectors (~10 ms), borderline at 1M, and **minutes at 100M+**. **Approximate search (ANN)** returns neighbours that are *good enough* but **orders of magnitude faster** by only searching promising parts of the index (e.g. HNSW graphs, IVF partitions).

$$\text{ANN: speed }\uparrow,\quad \text{exactness }\downarrow\text{ slightly}$$

**The key trade-off to tune: latency vs recall.** Recall@K = fraction of the *true* top-K neighbours the ANN actually returns. Higher recall requires deeper search (more probes), which raises latency; lower latency sacrifices recall. For real-time RAG the course's typical operating point is **90–95% recall under 50 ms** — good enough because the reranker/generator can tolerate an imperfect-but-close top-K.

Index build time is the third dimension — the one-time cost to construct the search index, traded against query latency.

**Pro tip:** The answer is a single formula in words: *more probes ⟹ higher recall ⟹ higher latency*; pick the operating point to fit the use case. Quote the scale table (10k ~ 10 ms → 100M ~ minutes) to show *why* exact fails at production scale. And remember ANN is "good enough" — name Recall@K explicitly.

---

## Q.3

### Q.3.1 — PII, Privacy, and Secure Feature Handling (5 Marks)

(a) Distinguish **direct identifiers** from **quasi-identifiers**, and explain the **re-identification risk** they create. `[2 Marks]`

(b) Describe how privacy constraints propagate into the ML platform — feature stores, logging, and monitoring. `[3 Marks]`

#### Answer

**(a)** **Direct identifiers** unambiguously identify a specific individual: full name, email, phone number, government ID, exact address. **Quasi-identifiers** are harmless alone but identifying **in combination**: date of birth, ZIP/postal code, IP/device ID, precise timestamps. **Re-identification risk:** a *record-linkage* attack combines quasi-identifiers (DOB + ZIP + gender) to pinpoint an individual even when no name is present. Removing the direct identifier alone is therefore not enough — quasi-identifier combinations must be assessed.

**(b)** Privacy is a **non-functional requirement** that shapes the whole platform:

- **Feature stores / data pipelines** — minimise collection ("borrow, don't own"), define retention, and apply anonymisation/minimisation so raw PII does not enter training or serving features.
- **Logging** — never log raw PII in inference logs (per-request feature values, scores, and IDs must be scrubbed); log what is needed for drift/audit, not the full personal record.
- **Monitoring** — track access and usage (who can see what, RBAC), and treat data-access events as auditable signals; monitor for *leakage of sensitive attributes* rather than only model metrics.

The mental model: *what data are we collecting, how long do we keep it, who can access it and for what purpose?* — answered in feature stores, pipelines, logging, and monitoring from day one.

**Pro tip:** PII questions reward the *combination* idea — quasi-identifiers in combination cause re-identification (the record-linkage diagram: DOB + ZIP + gender → identity). For part (b), the phrase "privacy is a non-functional requirement that propagates into features, logs, and monitoring" is the framing that earns the marks; give one concrete example per layer (scrubbed logs, minimised features, RBAC-gated access).

---

### Q.3.2 — Segmented Evaluation and Fairness (5 Marks)

A loan-approval model reports 95% overall accuracy. Explain why a **single global metric** can hide harmful performance disparities, and describe how **segmented (group-wise) evaluation** surfaces them. Give one fairness-driven action the team could take.

#### Answer

**The global-metric problem:** a 95% aggregate accuracy can hide systematic underperformance for specific groups — e.g. Group A at 97% and Group B at 88%. When group sizes differ or error distributions are asymmetric, the aggregate is a **dangerous summary statistic**: it looks reassuring while a real group is underserved (or worse, the model's mistakes concentrate on a protected segment).

**Segmented evaluation:** compute metrics **independently per group** by filtering validation data on the `group` column and scoring each subset separately. The workflow: load model + validation data → compute global metrics → loop over groups → compute group metrics → compare in a table/bar chart. The gap (e.g. 9 pp) becomes visible, whereas the global number hid it.

This is the foundational practice for **fairness analysis**: you cannot fix a disparity you cannot measure.

**Fairness-driven action (example):** rebalance the training data for the underperforming group, adjust the decision threshold per segment, or change the loss function (e.g. group-aware weighting) — then re-run segmented evaluation to verify the gap closed. Any action must be validated by the same group-wise metrics that exposed the disparity.

**Pro tip:** The answer is *aggregate hides → disaggregate exposes → act and re-validate*. The one-line example (95% global = 97% group A + 88% group B) is worth a mark by itself. Name a concrete action (threshold tune, data rebalance, loss weighting) and close the loop by re-measuring — examiners reward the closed loop over a one-off fix.

---

## Q.4

### Q.4.1 — Explainability: Local vs Global, and the Audit Trail (6 Marks)

(a) Distinguish **local explainability** from **global explainability**, and give one method or example for each. `[3 Marks]`

(b) Explain how explainability and **audit trails** work together as an accountability toolkit for production ML. `[3 Marks]`

#### Answer

**(a)** **Local explainability** answers *"why did the model make THIS prediction?"* for a single instance — the audience is the end user, support, or an appeals process. Example: a loan denial explained as "low income and recent delinquency contributed most to the rejection." Methods: SHAP values, LIME, feature contributions. **Global explainability** summarises behaviour **across many cases** — the audience is model reviewers, risk analysts, and engineers. Example: "across all applicants, credit history and income are the dominant features driving approvals." Methods: global feature importance, partial dependence, model-agnostic summaries.

| | Local | Global |
|---|---|---|
| Question | Why this prediction? | What drives behaviour in general? |
| Audience | End user, support, appeals | Reviewers, risk analysts, engineers |
| Methods | SHAP, LIME | Global importance, PDP |

**(b)** Explainability and audit trails together form the **accountability toolkit**:

- **Explainability** answers *why* a decision was made (human-reasoning layer).
- **Audit trails** answer *what happened* — which model version, trained on what data, promoted by whom, when. The registry records lineage (data snapshot, code commit, config), evaluation summary, stage transitions with approvers, and rollback history.

Together they let an organisation both **explain an individual decision** and **prove how the system was built and operated** — the two halves of accountability that regulators (finance, healthcare) demand. Without the audit trail, an explanation is unverifiable; without explainability, an audit trail shows *what* but not *why*.

**Pro tip:** The two-part structure mirrors the question — define local vs global with an audience + method each, then connect the pair with the word *accountability*. The sentence "explainability answers *why*; the audit trail answers *what happened*" is the differentiator. Mention SHAP/LIME names to show method fluency — one line each is enough.

---

### Q.4.2 — Capacity Planning: Traffic to Infrastructure (4 Marks)

A search-ranking service must handle **500 average QPS, peaking at 5,000 QPS** during flash sales. Estimate how many replicas are needed, given each replica reliably serves **200 QPS**, and state what additional design decisions the peak demands. State your assumptions.

#### Answer

**Assumption:** a single replica sustainably serves 200 QPS; we size for the **peak** (flash sales) since under-provisioning peaks causes timeouts; the model is the same on every replica (pure replication, no shard).

**Average sizing:**

$$\frac{500}{200} = 2.5 \rightarrow 3 \text{ replicas}$$

**Peak sizing:**

$$\frac{5000}{200} = 25 \text{ replicas}$$

**Design decisions the peak demands:**

1. **Autoscaling** — do not run 25 replicas permanently; scale out on QPS/P95 toward the peak and scale in after, with min/max bounds and cooldowns (avoid flapping).
2. **Headroom** — add ~20–30% over the raw number (say 30–33 replicas at peak) so a replica failure or latency spike does not breach the P95 target.
3. **Load balancing and health checks** — the load balancer must spread 5,000 QPS evenly and take unhealthy replicas out of rotation.
4. **Tested capacity** — the 200 QPS/replica figure must be measured (benchmark on target hardware), not assumed; flash-sale traffic should be load-tested in advance.

**Pro tip:** Capacity questions want *assumptions stated, math shown, and peak-driven reasoning*. Always size on **peak**, not average, and add headroom. The two numbers (3 vs 25) and the autoscaling bridge are the marks; "benchmark the 200 QPS figure" is the expert extra.
