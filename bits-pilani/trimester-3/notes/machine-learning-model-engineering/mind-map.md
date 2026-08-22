# Machine Learning Model Engineering — Revision Mind Map

> Everything important, in acronyms and one-liners. Pair with `sample-paper-01.md` and the speculative papers for exam patterns.

## Foundations & Lifecycle

```
MODEL ENGINEERING = turn trained artifact into production service
MLOPS = the operating system for production ML
```

- **7-stage ML lifecycle** — problem → data → train → evaluate → deploy → monitor → retrain (loop)
- **Production loop** — deploy → monitor → retrain → redeploy (never a one-time ship)
- **Four constraints** — latency, throughput, cost, reliability
- **Failure modes** — training-serving skew, stale models, data drift, silent degradation

## Inference Patterns

| Pattern | Style | Latency | Use case |
|---------|-------|---------|----------|
| **Batch** | Precompute offline | Hours–days | Nightly scoring, retraining data |
| **Online** | Request–response | ms (P95 < 100 ms) | Interactive apps, fraud |
| **Streaming** | Event-by-event | ms–s | Real-time alerts, recommendations |

- **Metrics triangle** — latency (P50/P95/P99) × throughput (QPS/RPS) × cost; pick pattern by the latency SLO
- **Batch pros** — simple, efficient, huge volumes · **Online pros** — immediate, per-request control · **Streaming pros** — freshest, reacts to events

## Serving & Deployment

- **Serving = artifact → service**; core layer responsibilities: load model, accept requests, return predictions, scale, observe
- **Architectures** — **monolith** (all-in-one), **microservice** (isolated model APIs), **serverless** (pay-per-call; watch **cold starts**)
- **APIs** — **REST** (JSON, easy) vs **gRPC** (protobuf, binary, lower latency, streaming-friendly)
- **Sync vs async** — sync blocks for the answer; async returns a job id, polls later (long tasks, batch)
- **Deployment strategies** — **blue-green** (flip traffic between two full environments) · **canary** (small % traffic to new version, watch metrics) · **shadow** (run new model in parallel, discard output, compare logs — zero user risk)
- **Champion–challenger** — promote challenger only if it beats champion by tolerance $\delta$: $\text{metric}_{challenger} > \text{metric}_{champion} + \delta$; **archive, never delete** the old version; **pin version, never `latest`**
- **Scaling** — **vertical** (bigger box) vs **horizontal** (more replicas) vs **autoscaling** (scale on CPU/QPS/P95 with min/max + cooldown)
- **Cost levers** — **spot/preemptible instances** (cheap, interruptible), **serverless**, **micro-batching** (amortise forward pass)

## MLOps & Pipelines

- **CI/CD for ML** — CI tests code + data + model (data checks, data drift tests, model eval); CD deploys the trained model
- **ML vs classic CI/CD** — ML pipelines move **artifacts** (model, data, code), need **reproducibility** and **lineage**
- **MLflow** — experiment tracking: log params, metrics, models, inspect runs
- **Lineage** — every artifact answers: *what data? what code? what hyperparams? what parent model?*
- **Model registry** — versioned model store; promotion = move stage (staging → production)

## Monitoring & Observability

- **Why different from SW monitoring** — "service is up" ≠ "model is good"; infras metrics give false confidence
- **Three-layer framework** — **system** (CPU, memory, latency, errors) · **data** (schema, missing rates, drift) · **model** (accuracy, AUC on fresh labels)
- **Drift types** — **covariate** $P(X)$, **label** $P(Y)$, **concept** $P(Y\mid X)$

| Drift | Detect with |
|-------|-------------|
| Covariate $P(X)$ | **PSI**, KS test, mean/std shift, histograms |
| Label $P(Y)$ | Class-ratio / base-rate shift |
| Concept $P(Y\mid X)$ | Performance on fresh labels (AUC, accuracy, F1) |

$$\text{PSI} = \sum (A_i - E_i)\ln\frac{A_i}{E_i} \quad (>0.2 = \text{major shift})$$

- **Observability stack** — **logs** (per-request features, score, version) · **metrics** (latency, error, PSI, rolling AUC) · **traces** (path: gateway → feature store → inference) · **alerts** (push on *sustained* SLO breach) · **dashboards**
- **SLO vs SLA** — SLO = internal measurable target (e.g. PSI < 0.2); SLA = contractual promise with penalties
- **Alert design** — condition on sustained breaches (e.g. PSI > 0.2 for 4 hrs), not single spikes; info/warning/critical tiers + runbooks

## Retraining

- **Triggers** — drift, performance SLO breach, **policy** (scheduled/calendar), explicit product change
- **Scheduled vs event-driven** — calendar-based vs triggered by metrics
- **Evaluation ladder** — offline eval → **backtesting** → **shadow** → **A/B** → promote
- **Guardrails** — approvals, audit trails, traceability, **rollback** = version pin flip

## Optimisation & Compression

| Technique | What changes | Effect |
|-----------|-------------|--------|
| **Quantisation** | Bit width: FP32 → FP16/INT8 | ~4× smaller at INT8, faster CPU |
| **Pruning** | Remove low-importance weights/channels | Fewer params (fine-tune after) |
| **Distillation** | Small student learns from large teacher | Smaller architecture, preserves accuracy |

- **Order** — distill → prune → fine-tune → **quantise last** (operates on final weights)
- **Formats** — **ONNX** (standard interchange), **TensorFlow Lite** (mobile/edge), **OpenVINO** (Intel CPU/edge)
- **Runtimes** — **ONNX Runtime**, **TensorRT** (NVIDIA GPU), **XLA** (TPU); benchmark on **target hardware**
- **Size formula** — $\text{params} \times \text{bytes}$; FP32 (4 B) → INT8 (1 B) = **4×**
- **Trade-offs** — accuracy vs latency vs cost vs UX (the four-way tug-of-war); edge = INT8 when power/memory constrained; keep FP32 for high-stakes (medical/fraud) unless recall proven

## Features & Data Pipelines

- **Offline features** — batch-computed, build training data, warehouse/Spark
- **Online features** — precomputed, key-based lookup (Redis), ms retrieval, serve live requests
- **Training-serving skew** — offline and online compute features differently → model sees different distribution at inference
- **Prevention** — define each feature **once**, share code between train & serve; log live feature vectors
- **Feature store** — single source of truth (Feast open-source; Tecton/Hopsworks managed); versioning + lineage
- **Pipelines** — **ETL** (extract-transform-load) vs **ELT** (load first, transform in warehouse); batch / micro-batch / streaming
- **Streaming tools** — Kafka (durable event log), Spark Streaming, Flink, Beam
- **Data quality** — schema evolution, **data contracts**, completeness/correctness checks, **idempotency** (no double-count on re-run)

## Security, Privacy, Fairness

- **Threats** — data/input attacks (poisoning, evasion), model **extraction**, privacy leakage
- **PII** — personally identifiable information; **data minimisation** + **anonymisation**
- **RBAC** — role-based access control for data/model/registry
- **Fairness metrics** — compute confusion matrix **per group**, derive FPR/recall, compare

$$\text{FPR} = \frac{FP}{FP + TN} \quad \text{Recall} = \frac{TP}{TP + FN}$$

- **Recall** critical for opportunity models (lending); **FPR** critical for punitive models (fraud)
- **Explainability** — local (SHAP/LIME, why this prediction) vs global (feature importance)
- **Audit trails** — log version, data, decisions, approvals across the pipeline (for regulators)

## Multi-Model Systems

- **Routing** — rule-based (by region/tenant) or **learned router** (small model picks the big model)
- **Fallback & ensembles** — accuracy–cost trade-off; fallback to cheap model on degradation
- **Scaling inference** — **replication** (more copies; HA) vs **sharding** (split model/data; each shard serves its slice)
- **Caching** — cache model results / embeddings (identical inputs skip recompute)
- **Multi-tenancy** — **noisy neighbour problem** (one tenant's spike breaks another's SLO) → per-tenant SLOs, quotas, isolation
- **Vector DB & ANN** — embeddings stored in vector DB; **ANN** (HNSW, IVF) ≈ fast "good enough" search

$$\text{ANN: speed }\uparrow,\ \text{exactness }\downarrow \text{ slightly};\quad \text{trade-off} = \text{recall@K vs latency}$$

- **RAG** — **retrieval-augmented generation**: embed query → retrieve top-K from vector DB → rerank → generate; fixes stale/hallucinated answers (open-book vs closed-book exam)

## System Design & Capacity

- **Layered ML platform** — data layer → feature store → training/experimentation → serving → monitoring/feedback (closed loop)
- **Requirements & SLAs** — clarify QPS, P95 latency, availability, accuracy, cost before design
- **Capacity planning** — size on **peak**, not average

$$\text{replicas} = \frac{\text{peak QPS}}{\text{QPS per replica}}$$

- **Resilience** — failure scenarios (dependency down, drift, traffic spike) → circuit breakers, cached fallback, retries, rollback

## Formula Cheat Sheet

| Formula | Expression |
|---------|-----------|
| PSI | $\sum (A_i - E_i)\ln\frac{A_i}{E_i}$ |
| FPR | $\frac{FP}{FP + TN}$ |
| Recall | $\frac{TP}{TP + FN}$ |
| Model size | params × bytes (FP32 4B, INT8 1B) |
| Promotion rule | $\text{metric}_{challenger} > \text{metric}_{champion} + \delta$ |
| Replicas | peak QPS ÷ QPS per replica |
