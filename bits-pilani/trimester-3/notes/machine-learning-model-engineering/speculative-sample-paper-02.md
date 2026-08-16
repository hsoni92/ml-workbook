# Sample Question Paper (Speculative — 2 of 2)

## BITS Digital Comprehensive Examination — Model Question Paper

> **Note:** This is a speculative paper, constructed from the breadth of the course notes to help you practise patterns that did not appear in `sample-paper-01.md`. Question numbering and marks are indicative.

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

### Q.1.1 — Streaming vs Micro-Batching for Real-Time Features (5 Marks)

A fraud-detection team currently runs a nightly batch job that computes risk features (e.g. `spend_last_24h`, `failed_logins_last_24h`). They want fresher features without building a fully event-by-event system. Compare **streaming inference** with **micro-batching**, and recommend which the team should adopt, with justification.

#### Answer

**Streaming inference** processes a continuous flow of events through a long-running pipeline: event source → stream transport → stream processing → model step → sinks. There is no blocking caller per row; outputs feed alerts, feature stores, or dashboards. It is best when data arrives continuously and you must react per-event (sub-second).

**Micro-batching** is still *batching* — small batches run frequently (every 1–5 minutes). Conceptually it feels like streaming but is implemented as many small scheduled jobs (Spark Structured Streaming default, Flink micro-batch, or a cron script).

| Dimension | Batch (current) | Micro-Batch | Streaming |
|-----------|-----------------|-------------|-----------|
| Window / freshness | Hours–days | 1–5 minutes | Per event |
| Latency | High | Medium | Low |
| Complexity | Low | Medium | High |
| Implementation | Cron + Spark | Spark SS / Flink / cron | Kafka + Flink/Beam |

**Recommendation: micro-batching.** The team's stated need is *minute-level freshness, not per-event reaction*. Micro-batch reuses their existing batch tooling, avoids the state-management complexity of true streaming (windowing, watermarks, checkpoints), and is "good enough" for near-real-time risk features. Streaming is the escalation path if fraud requires sub-second per-transaction scoring — but that is a different requirement than the one stated. Watch for the micro-batch gap: events within a window are invisible until the next run, and jobs need idempotency (no double-counting on re-run).

**Pro tip:** Pattern-selection questions are scored on *matching the requirement to the middle option*. The phrase "without building a fully event-by-event system" is the giveaway for micro-batch. Answer with the three-row comparison, then a recommendation + one failure mode (staleness window) + when to escalate to true streaming.

---

### Q.1.2 — Online vs Offline Features and Training–Serving Skew (5 Marks)

Distinguish **online features** from **offline features** in a feature-store architecture. Explain how failing to keep the two consistent can produce "training–serving skew", and describe one concrete practice that prevents it.

#### Answer

**Offline features** build the **training dataset**: they are computed over large historical windows with batch jobs (Spark/SQL), stored in a warehouse, and used during model training. **Online features** serve a single **live inference** request: precomputed/cached values retrieved by entity key (e.g. `customer_id`) from a low-latency store (Redis, DynamoDB) in milliseconds.

| Property | Offline features | Online features |
|----------|------------------|-----------------|
| Used for | Training | Live prediction |
| Computation | Batch, over history | Pre-materialised, at request time |
| Latency | Irrelevant (job time) | Few ms per lookup |
| Access | Scan/join over rows | Key-based lookup |

**Training–serving skew** is what happens when the two disagree: the model trains on feature values computed one way (say `spend_last_24h` from a nightly aggregation at time $t_0$) but serves on values computed differently (live aggregation including the current in-flight transaction). The model sees a different distribution at inference than at training, so offline accuracy does not transfer to production.

**Prevention practice:** compute features **once with a shared definition and write both copies from the same pipeline** — e.g. an offline table built by the same code that populates the online cache, plus **training data logged at request time** (log the actual feature vector used in production and backfill it into training). This is the course's "compute once, reuse for train and serve" principle; it makes the online and offline copies differ only in storage, not in logic.

**Pro tip:** The exam pattern is *definition → the skew failure mode → the fix*. The fix sentence that earns the mark is "the same feature-definition code populates both the offline table and the online cache" — plus logging live feature vectors to audit skew. Never answer "use Redis" as the whole answer; storage choice is secondary to definition consistency.

---

## Q.2

### Q.2.1 — Canary vs Shadow Deployment and Champion–Challenger Promotion (6 Marks)

A credit-risk team wants to promote a new model version (challenger) that beat the production champion on a holdout set. Compare **canary deployment** with **shadow (dark) deployment** during promotion. Then outline the promotion rule (including why a **tolerance threshold** matters) and the **rollback** guarantee.

#### Answer

**Canary deployment** routes a **small percentage of live traffic** to the new model while the champion serves the rest. A subset of real users is affected, so you must monitor not just HTTP status but prediction quality and business KPIs. **Shadow (dark) deployment** runs the challenger **in parallel** on the *same real inputs*, but **only the champion's output is served** — the challenger's predictions are logged for comparison. Zero user risk, real production inputs.

| Aspect | Canary | Shadow |
|--------|--------|--------|
| User impact | Partial (small % of traffic) | None |
| Evidence | Live behaviour on real users | Logged comparisons, offline evaluation |
| Risk | Low but non-zero | ~Zero |

**Promotion rule (champion vs challenger):** load the champion by `Production` stage tag and the challenger by explicit version; evaluate both on the **same** holdout data using statistical **and** business metrics. Promote only if the challenger wins on both, and only if it beats the champion **by a margin $\delta$**:

$$\text{promote if: } \text{metric}_{\text{challenger}} > \text{metric}_{\text{champion}} + \delta$$

The tolerance $\delta$ prevents promoting on statistically insignificant, noise-level improvements (a recurring course trap). If it passes, move the challenger to `Production` and **archive — never delete — the old champion**.

**Rollback guarantee:** keep the previous version available and **pin the version** in serving config (never `latest`). Rollback is then a stage/version flag flip — minutes, not redeployments.

**Pro tip:** Contrast questions want a two-column table plus a numeric promotion rule. Always include the $\delta$ margin — examiners love it. And the one-line rollback principle — "archive, don't destroy; pin, don't use latest" — is worth a mark on its own in every deployment question.

---

### Q.2.2 — Serverless vs Spot Instances as Cost Levers (4 Marks)

A company serves a low-volume internal model (~200 requests/day) that spikes to tens of thousands during product launches. Compare **serverless inference** with **spot/preemptible instances** as cost levers, and recommend the appropriate fit for this workload.

#### Answer

**Serverless inference (FaaS)** packages the model as a function; the provider auto-scales and you pay **per invocation** with no idle cost. Ideal for spiky, low–medium volume, lightweight models. **Spot/preemptible instances** are discounted compute that the provider can reclaim at short notice — cheap but **not reliable**, so they fit batch and non-critical workloads, not latency-critical online APIs.

| Lever | Cost model | Reliability | Best fit |
|-------|-----------|-------------|----------|
| Serverless | Pay per invocation | Managed; cold starts on first call | Spiky low-volume, lightweight models |
| Spot instances | Deep discount, reclaimable | Interruptible | Offline/batch, overflow, retraining jobs |

**Recommendation for this workload: serverless.** Traffic is low-volume and bursty (the exact shape serverless is built for — the course's marketing-team Lambda example: 200 invocations/day spiking to 50k at a webinar). It scales down to zero between bursts, so the company does not pay for idle servers. Spot is a complement for the *offline* side (e.g. nightly retraining) but the wrong fit for an interactive API whose latency matters.

**Pro tip:** Cost-lever questions are scored on *workload shape matching*. The two questions to answer: "Does a user wait?" (yes → on-demand/serverless; no → spot) and "Is traffic bursty and low-volume?" (yes → serverless). Name the failure mode of the rejected option (spot can be reclaimed mid-job; serverless cold-start delays the first call) — one line on the rejected option's downside is the differentiator.

---

## Q.3

### Q.3.1 — SLOs, Dashboards, and Alert Design (5 Marks)

(a) Define a **Service Level Objective (SLO)** and give two examples of ML-specific SLOs. Explain the difference between an SLO and an SLA. `[2 Marks]`

(b) Describe how **alert design** should be structured to avoid alert fatigue, including severity routing and the role of **runbooks**. `[3 Marks]`

#### Answer

**(a)** An **SLO** is a measurable target for a specific metric over a defined window — an *internal* target that drives capacity planning, isolation, and incident prioritisation. An **SLA** is a *contractual* agreement with customers (usually with penalties). SLOs inform engineering; SLAs govern promises. The course's rule of thumb: 3–5 SLOs per model, derived from the bad outcomes you must avoid.

ML-specific SLO examples:

- **Latency SLO:** P95 inference latency < 150 ms over a rolling 1-hour window.
- **Accuracy SLO:** AUC ≥ 0.85 on the last 7 days of labelled data.
- **Drift SLO:** PSI < 0.2 on the top 5 critical features over a rolling 24-hour window.

**(b)** Good alert design treats alerts as **push monitoring** tied to SLOs, not "alert on every metric bump":

- **Condition on sustained breaches** — e.g. PSI > 0.2 for 4 consecutive hours, or P95 > 200 ms for 15 minutes — never single noisy spikes. Require the metric to return inside band before the alert resolves.
- **Severity routing** — Info → dashboard/log only; Warning → Slack/email, investigate within hours; Critical → pager/on-call, immediate action.
- **Runbooks** — every alert carries a one-line business explanation, common causes, a check sequence (which dashboard/logs/queries), and a menu of next actions (rollback, threshold tune, retrain ticket, escalate). Runbooks turn incidents from panicked debugging into triage.
- **Ownership** — primary + escalation owner per alert type (data engineering for pipelines, ML engineering for drift/performance, platform for infra), so alerts never bounce between teams.

**Pro tip:** SLO questions reward the SLO-vs-SLA distinction in one crisp sentence ("internal target vs contractual promise"), then concrete examples with thresholds + windows. Alert questions reward the *sustained-breach* principle and the *info/warning/critical* tiering — mention a pager/Slack split and a runbook link to hit all the marks.

---

### Q.3.2 — Audit Trails and Rollback for Regulated Deployment (5 Marks)

A bank deploys a lending model in production. Regulators require proof of how each model version was trained and what happened during deployment. Describe the **audit trail** the bank should keep, and explain how it enables **rollback** when a production incident occurs.

#### Answer

**Audit trail — record per production model version:**

- **Version and stage** — v7, Production (identifies the current live model).
- **Training lineage** — data snapshot ID/hash, code Git commit, config file version, random seed, and the run ID that produced the artefact.
- **Evaluation summary** — metrics at promotion time (justifies why this version was chosen).
- **Deployment history** — stage transitions (None → Staging → Production) with timestamps and approver names.
- **Rollback history** — when and why a rollback occurred (for post-incident analysis).

A model registry stores these as structured metadata (versioned folders + `registry.json` or MLflow), making compliance a *query* ("show all models trained on data containing feature X after date Y") instead of a manual scramble.

**How it enables rollback:** when an incident happens (say the new version starts approving bad loans), the trail tells you exactly which version was serving and what changed from the previous one. Rollback itself depends on two practices the trail supports: **(1) keep the previous champion available** — archive, never overwrite or delete; **(2) pin the serving version** (`model_version: 6`, not `latest`). Recovery is then a stage/version flag flip with no code redeployment — minutes, not hours. Regularly **tested** rollback (in the deployment playbook) ensures traffic actually routes back to the previous model.

**Pro tip:** The answer structure is *what to record → where it lives → how it makes rollback fast*. The two rollback principles — "keep old champion, pin version" — appear in every compliance/rollback question; state them verbatim. Mention the registry as the *single source of truth* for version + stage to connect to the Q.2.2 material.

---

## Q.4

### Q.4.1 — Distillation vs Quantization vs Pruning (6 Marks)

Compare **knowledge distillation**, **quantization**, and **pruning** as model-compression techniques. For a latency-critical mobile classifier, state which combination you would use and justify the order of applying them.

#### Answer

| Technique | What it changes | Mechanism | Typical accuracy impact |
|-----------|-----------------|-----------|-------------------------|
| **Pruning** | Number of parameters | Remove low-importance weights (unstructured, needs sparse kernels) or whole channels (structured, dense-friendly) | Small if fine-tuned after pruning |
| **Quantization** | Bit width of values | FP32 → FP16/INT8; ~4× smaller at INT8; faster integer math on CPU | Small (<1 pp typically) with PTQ; better with QAT |
| **Distillation** | Model architecture | Train a small **student** on the teacher's **soft labels** (dark knowledge), not just hard labels | Student often better than same-size model trained from scratch |

The key distinction: pruning and quantization reduce an *existing* model; distillation designs a *smaller model* that learns from a larger one. They are complementary — not interchangeable.

**Recommendation for a latency-critical mobile classifier:** a combined pipeline.

1. **Distill** — train a small student from a large accurate teacher (best possible accuracy-per-parameter for the constraint).
2. **Prune** (structured) — remove whole channels to shrink further, then **fine-tune** to recover accuracy.
3. **Quantize (PTQ to INT8)** last — the largest size/speed win (4×) with the least additional work; escalate to QAT if the accuracy drop exceeds the target.

Order matters: quantize **last** because it operates on the final trained weights; pruning before fine-tuning interacts badly with quantization noise.

**Pro tip:** Comparison tables earn the marks — one row per technique with *what changes + mechanism + accuracy impact*. The differentiator sentence: "quantization changes bits, pruning changes parameter count, distillation changes the architecture." Always justify the *order* (distill → prune → fine-tune → quantize) — examiners check whether you understand quantization is a final precision step, not a training step.

---

### Q.4.2 — Choosing the Right Inference Pattern: Latency, Throughput, Cost (4 Marks)

A startup is choosing an inference pattern for a recommendation model. Traffic is expected to be a stable 5,000 requests/second with sub-100 ms P95 requirements. Compare **online**, **batch**, and **streaming** inference for this requirement, and justify which pattern (or combination) fits.

#### Answer

| Dimension | Online | Batch | Streaming |
|-----------|--------|-------|-----------|
| Data input | Single request | Static snapshot | Continuous event stream |
| Caller | Blocked until response | Nobody waits per row | No direct caller; downstream sinks |
| Primary latency | P95/P99 per request | Total job time | Event-to-action |
| Primary metric | RPS + P95 | Rows per job / throughput | Sustained events per second |

**Recommendation: online (request–response) inference** as the primary serving path — a caller is blocked (the user's app needs the recommendation before rendering) and the P95 < 100 ms target is per-request latency, which only online serving can meet. The stable 5,000 RPS load is handled with **horizontal scaling + autoscaling** on QPS/P95, plus **micro-batching** inside the service to amortise the forward-pass cost while keeping P95 inside the SLA.

**Batch** is a complement, not a replacement here: precomputing candidate pools overnight (offline) reduces the online workload, but the live recommendation must still be online. **Streaming** is unnecessary — this is a request-driven product, not an event-driven pipeline reacting to a stream.

**Pro tip:** The decision guide is three questions in the course notes: (1) is a caller blocked now? → online; (2) millions of rows by a deadline? → batch; (3) continuous event stream? → streaming. Answer the question by *running those three questions*, then name the cost lever (micro-batching) that bridges online latency and throughput. Mentioning "no streaming because there is no blocking-caller-free event stream" shows you understand *why* streaming is excluded, not just what it is.
