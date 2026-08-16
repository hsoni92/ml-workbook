# Sample Question Paper

## BITS Digital Comprehensive Examination — Model Question Paper

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

### Q.1.1 — Horizontal vs. Vertical Autoscaling (5 Marks)

Explain the difference between "horizontal" and "vertical" autoscaling for a model-serving system. Discuss one advantage and one limitation of each.

#### Answer

**Vertical autoscaling (scale up / down)** changes the *size* of the machine that already runs the model service: more (or fewer) vCPUs, RAM, or attaching a GPU. The number of instances stays essentially one (or a few).

- **Advantage:** Minimal architecture change. Same process, same code path, often the fastest latency win for small-to-medium traffic.
- **Limitation:** A hard ceiling on one box, worse price/performance at the top tier, and a **single point of failure** — if that instance dies, serving is down.

**Horizontal autoscaling (scale out / in)** changes the *number of replicas* of the same model service. A load balancer spreads requests. Autoscaling policies add or remove replicas from metrics such as CPU, QPS, or P95 latency, with min/max replica caps and cooldown.

- **Advantage:** Higher total throughput with stable per-request latency under concurrent load, plus **high availability** — one replica can fail while others keep serving.
- **Limitation:** Needs **shared state** (no sticky in-memory caches), coordinated rolling deploys, and **cost control**. Unbounded max replicas or over-sensitive rules cause flapping (rapid scale-out then scale-in) and runaway bills.

**Assumption:** “Autoscaling” here means automatically applying those two patterns, not only Kubernetes HPA.

**Pro tip:** Exam pattern is *mechanism + one win + one failure mode*. Vertical = bigger box / simple / ceiling + SPOF. Horizontal = more replicas + LB / HA + throughput / state + cost + flapping. Always mention **min/max replicas and cooldown** when the word autoscaling appears. If the scenario is a prototype at low RPS, prefer vertical first; if spikes + HA, prefer horizontal + autoscaling.

---

### Q.1.2 — Online vs. Batch Processing for Churn Prediction (5 Marks)

A telecom company predicts customer churn. Predictions must be available instantly when a customer contacts support, while the model itself is retrained weekly using a large historical dataset.

Compare "online" and "batch" processing for these two needs, and recommend the appropriate approach for each, with justification.

#### Answer

| Dimension | Online | Batch |
|-----------|--------|-------|
| Who waits | Caller blocked until a response | Nobody waits per row |
| Latency | Per-request P95/P99 (ms) | Total job time / throughput |
| Shape | One request, one response | Large static snapshot, start → end |
| Output | Synchronous HTTP/gRPC | Bulk write to DB / warehouse / feature store |

**Support-time predictions (recommend online, optionally with a lookup):** A support agent cannot wait for a nightly job. The prediction is part of a live interaction, so **online (request–response) inference** is the right serving pattern: fetch features, score, return churn risk in the same call.

A valid hybrid: **nightly/hourly batch scores** written to a store, and support **looks up** the latest score. That still needs an online *read* path. Pure batch with no lookup cannot meet “instantly when a customer contacts support.”

**Weekly retraining on a large historical dataset (recommend batch):** Retraining is a scheduled bulk job: snapshot data, train, evaluate, register. No user is blocked per row. **Batch processing** (scheduler + job + monitoring) is cheaper, uses spot/preemptible capacity, and optimises **rows/sec and finish-by deadline**, not per-row milliseconds.

So: **batch for the weekly train/score-the-base pipeline; online (or online lookup of batch scores) for the support interaction.**

**Pro tip:** Pattern-selection questions always ask *who is waiting?* If a human/API is blocked → online. If millions of rows by a deadline → batch. One product often needs **both** (this question is designed that way). Do not recommend streaming unless events must be scored as they flow with no blocking caller.

---

## Q.2

### Q.2.1 — Dynamic Batching Throughput (6 Marks)

A recommendation-serving endpoint uses dynamic batching; each batch takes 30 ms to process regardless of size (max batch size = 20).

- a. If the system receives 500 requests/second, calculate the minimum number of full batches/second required.
- b. Calculate the maximum theoretical throughput (requests/sec) the system can support.
- c. If actual traffic drops to 100 requests/second, briefly explain how this affects batching efficiency and suggest one mitigation.

#### Answer

**Assumption:** One serving replica; batch time $30\,\text{ms}$ is independent of how full the batch is; max batch size $N_{\max} = 20$.

**(a)** Minimum full batches/second at $500$ rps:

$$\frac{500}{20} = 25 \text{ batches/s}$$

(If batches are not always full, more batches/s would be needed.)

**(b)** Batch processing rate:

$$\frac{1}{0.030} \approx 33.33 \text{ batches/s}$$

Maximum theoretical throughput (always-full batches):

$$33.33 \times 20 \approx 667 \text{ requests/s}$$

(Exactly: $1000/30 \times 20 = 20000/30 \approx 666.7$ rps.)

$500$ rps is below this ceiling ($\approx 667$), so one replica can theoretically keep up **if** batches stay full.

**(c)** At $100$ rps, time to fill $20$ requests is $20/100 = 0.2\,\text{s} = 200\,\text{ms}$ of **queueing**, then $30\,\text{ms}$ compute. GPU/CPU utilisation falls (smaller or slower-to-fill batches), while **P95 latency can worsen** because of wait-for-batch. Mitigation: **lower max wait time and/or max batch size** (e.g. size $4$–$8$) so latency stays inside SLA; alternatively scale in replicas. Offline large-batch thinking does not apply to an online API.

**Pro tip:** Dynamic-batching arithmetic is always two rates: **arrival / max batch size** vs **$1/t_{\text{batch}} \times$ max batch size**. At low traffic, name the failure mode **queueing delay vs utilisation**, then tune **max batch size and max wait** against **P95 SLA** — not average latency.

---

### Q.2.2 — Reproducibility and Model Registry (4 Marks)

> **Note:** The original paper labels this question as Q.2.1 as well — likely a typo for Q.2.2.

Explain the importance of reproducibility and experiment lineage tracking in ML deployment pipelines. Describe two practices that would ensure a previously deployed churn-prediction model version could be exactly reproduced later. Briefly explain how a model registry supports this as new model versions move toward production.

#### Answer

**Why it matters:** Reproducibility means the same **code + config + data snapshot** (plus seed) yields an equivalent model (metrics within a small tolerance under GPU noise). Lineage is the provenance graph: which commit, data version, hyperparameters, run ID, and evaluation produced which artefact. Without both, you cannot debug a production drop, pass audit (“how was this churn model trained?”), onboard a teammate, or roll back with evidence.

**Two practices to reproduce a past churn model:**

1. **Version everything used in the run:** Git commit hash, frozen data snapshot (not `data/latest.csv`), externalised config (YAML), pinned environment (lockfile / Docker image), and logged random seed. Pipeline encodes *what to do*; the tracker records *what was done*.
2. **Log the run as a unit:** experiment tracker (e.g. MLflow) stores params, metrics, and the model artefact under a unique run ID so “replay run $X$” is possible.

**Registry role:** The registry is the **catalogue of versions and stages** (None → Staging → Production), with paths, metrics, and lineage pointers — not ad-hoc `model_final.pkl`. Promotion moves a challenger to Production **without deleting** the old champion. Serving pins a **specific version** (not `latest`). New churn versions can be compared, audited, and rolled back by changing stage/version, not by hunting files.

**Pro tip:** Split three nouns examiners mix up: **tracker** = runs/params/metrics; **lineage** = links among data/code/config/model; **registry** = versions + stages + promotion. Always say **never overwrite the champion** and **never train from a mutable “latest” path**.

---

## Q.3

### Q.3.1 — Drift Detection and Observability (5 Marks)

(a) Explain the various drift detection techniques used to monitor production ML systems. Describe how each works and the type of drift it is best suited to detect. `[3 Marks]`

(b) Describe the key components of an observability stack (e.g., logs, metrics, traces, alerts, dashboards) for a production ML system, and explain how they complement drift detection in maintaining model performance. `[2 Marks]`

#### Answer

**(a)** Drift means production diverges from the training snapshot while weights stay frozen. Detection should match *what* changed:

| Technique | How it works | Best for |
|-----------|--------------|----------|
| Mean / std / min-max / missing rate | Compare recent window vs training (or stable) reference | **Covariate (feature) drift** $P(X)$ — cheap early warning |
| Histograms | Overlay full shape of a feature | Covariate drift when the mean is stable but the shape moves |
| PSI | Bin reference vs production; $\mathrm{PSI}=\sum (A_i-E_i)\ln(A_i/E_i)$; $>0.2$ major shift | Numeric/binned **covariate** drift (credit-style monitoring) |
| KS test | Compare CDFs of two continuous samples | Continuous **covariate** drift |
| Chi-square | Observed vs expected category frequencies | Categorical **covariate** drift |
| Label / base-rate monitoring | Class ratio or positive rate vs training | **Label (target) drift** $P(Y)$ |
| Performance on fresh labels (AUC, precision, recall, FN rate) | Needs ground truth | **Concept drift** $P(Y\mid X)$ — inputs may look stable while the mapping changed |

Covariate methods do **not** prove the model is wrong; concept drift **requires labels**. Drift is an **investigate** signal, not an automatic retrain.

**(b) Observability stack**

| Component | Role | Complements drift how |
|-----------|------|------------------------|
| **Logs** | Per-request features, score, model version | Forensic reconstruction of PSI/KS and delayed-label joins |
| **Metrics** | Time series: latency, error rate, PSI, rolling AUC, volume | Alertable trends; SLOs (e.g. PSI $< 0.2$, AUC $\ge$ threshold) |
| **Traces** | Path: gateway → feature store → inference | Separates “model is wrong” from “features/latency broke” |
| **Dashboards** | Pull: system + data + prediction health in $\sim 30$ s | Humans triage drift vs infra vs data quality |
| **Alerts + runbooks** | Push on *sustained* SLO breach; owner + next actions | Turns PSI/AUC breaches into fix, threshold tune, or retrain — without alert fatigue |

Together: drift detectors supply ML-specific signals; logs/metrics/traces/alerts/dashboards turn those signals into **owned action** (pipeline fix vs threshold vs retrain vs rollback).

**Pro tip:** Always name the three drifts $P(X)$, $P(Y)$, $P(Y\mid X)$ and map **one detector to each**. Examiners punish “PSI detects concept drift.” For (b), pillars + *how they feed investigation* scores more than a tool dump (Prometheus, Jaeger, …).

---

### Q.3.2 — Diagnosing Drift and Designing a Retraining Workflow (5 Marks)

An online education platform's dropout-prediction model has been in production for eight months. After a major course-catalog redesign, the team observes rising false negatives and a gradual decline in prediction accuracy.

Based on the techniques discussed in Q.3.1(a), identify which would be most suitable to diagnose this issue, and justify your choice. Then design an automated retraining workflow, covering retraining triggers, validation steps, deployment strategy, and rollback mechanism. Justify why each component is necessary.

#### Answer

**Diagnosis:** A catalog redesign is a **product/policy change**: which behaviours lead to dropout likely changed, so **concept drift** $P(Y\mid X)$ is the primary hypothesis. Rising **false negatives** and falling accuracy on (presumably) labelled outcomes are **performance-on-fresh-labels** signals — the right detector for concept drift.

Still run **covariate checks** (PSI/KS on catalog-related features, new course IDs, missing rates) to see if $P(X)$ also shifted, and **label-rate** checks in case dropout prevalence changed. Do not stop at PSI: feature histograms can look “fine” while the mapping to dropout has changed. Investigate pipeline bugs and evaluation-window artefacts **before** retraining.

**Automated retraining workflow**

1. **Triggers (necessary so you retrain on evidence, not a calendar only):** sustained accuracy/FN SLO breach on fresh labels; PSI $> 0.2$ on catalog features for several days; explicit **policy trigger** = catalog redesign. Investigate first (broken ETL vs real change).
2. **Snapshot + train:** versioned data after the redesign, pinned code/config, log the run.
3. **Validation (champion vs challenger):** same holdout / recent labelled window; statistical metrics **and** business cost of missed dropouts; promote only if challenger beats champion by a margin $\delta$. Prevents shipping a worse model.
4. **Deployment:** staging smoke tests → **shadow** (log new scores, serve old) or **canary** (small traffic %) → full production. Offline eval is not live traffic.
5. **Rollback:** keep previous champion in the registry; **pin version** (not `latest`); one flag/stage flip back. Catalog launches can fail fast; minutes of rollback beat hours of debug.

Closed loop: monitor → trigger → train → evaluate → promote → monitor.

**Pro tip:** Scenario questions want **concept drift after a product change** plus a **four-part loop**: trigger → validate vs champion → staged deploy → rollback of the old artefact. Mention “drift $\neq$ instant retrain” in one sentence to pick up the course trap mark.

---

## Q.4

### Q.4.1 — Edge Quantization Trade-offs (6 Marks)

A drone-based crop-monitoring company wants to deploy an image-classification model directly on the drone's onboard hardware, which has strict power and memory constraints. A candidate model has 30 million parameters stored in FP32 (32-bit).

- a. Calculate the model size in MB before quantization.
- b. If quantized to INT8, calculate the new size and compression ratio achieved.
- c. If this causes accuracy to drop from 93.0% to 90.5%, discuss whether the trade-off is acceptable for this use case.

#### Answer

**Assumption:** Size $\approx$ number of parameters $\times$ bytes per weight (ignore optimiser states, activations, and framework overhead). $1\,\text{MB} = 10^6$ bytes (course-style decimal MB).

**(a)** FP32 uses $4$ bytes/parameter:

$$30 \times 10^6 \times 4 = 120 \times 10^6 \text{ bytes} = 120\,\text{MB}$$

(If $1\,\text{MiB}=2^{20}$ bytes: $120\times 10^6 / 2^{20} \approx 114.4\,\text{MiB}$.)

**(b)** INT8 uses $1$ byte/parameter:

$$30 \times 10^6 \times 1 = 30\,\text{MB}$$

$$\text{compression ratio} = \frac{120}{30} = 4\times \quad (\sim 75\% \text{ smaller})$$

**(c)** Accuracy drop $= 93.0\% - 90.5\% = 2.5$ percentage points.

For **on-drone** crop classification, INT8 is the course default for edge: $\sim 4\times$ less memory, faster integer math, less battery/thermal load. Crop monitoring is **not** a medical/fraud high-stakes domain where a fraction of a point dominates cost. A $2.5$ pp drop is **acceptable if** field trials still catch the diseases/stress the business cares about (validate per class, especially rare blight). It would be **unacceptable** if $2.5$ pp is concentrated in a critical minority class. Given explicit power/memory limits, shipping $120\,\text{MB}$ FP32 may be infeasible, so a slightly weaker but runnable INT8 model is the better product fit — after measuring on a holdout of real aerial imagery.

**Pro tip:** Size questions are always $\text{params} \times \text{bytes}$. FP32 $\to$ INT8 is **$4\times$**, not “a bit smaller.” Trade-off answers must **name the domain’s risk**: edge/mobile → favour compression; medical/fraud → keep FP32 unless recall is proven safe.

---

### Q.4.2 — Edge vs. Cloud Deployment (4 Marks)

The same image-classification model could alternatively be deployed as a cloud-hosted service, with drones uploading images for remote inference. Discuss two trade-offs between edge and cloud deployment for this use case (e.g., latency, connectivity in remote fields, cost, data bandwidth). Recommend which deployment target is more suitable, with justification.

#### Answer

**Trade-off 1 — Connectivity and bandwidth vs accuracy/compute.** Fields often have weak or no uplink. Cloud inference **requires uploading images**; that burns battery, may miss the SLA, and can leak farm imagery off-device. Edge runs INT8 locally with no WAN. Cloud can host a larger FP32/GPU model with higher accuracy and easier updates.

**Trade-off 2 — Latency / mission loop vs operational cost.** Edge gives **per-frame latency** and can steer the drone immediately (spray, recapture). Cloud adds radio RTT + queueing; a coverage hole means **no prediction**. Cloud centralises GPUs (pay per hour, simpler model ops) but **data egress and radio** dominate cost in the air. Edge shifts cost to onboard hardware and compression engineering.

**Recommendation: edge (INT8 on the drone) as primary**, with optional cloud for post-flight bulk re-scoring when docked. The constraint set is onboard power/memory **and** remote fields — the same pattern as the course mobile/edge camera scenario. Cloud-only serving fails when the radio fails, which is when monitoring is most needed.

**Pro tip:** Edge vs cloud is a **constraint matching** question: who is disconnected, who waits, how large is the artefact, how costly is a miss. Answer with **two explicit axes** then **one recommendation with a failure mode of the rejected option**. Hybrid (edge now, cloud later) is a high-scoring extra sentence when the brief allows it.
