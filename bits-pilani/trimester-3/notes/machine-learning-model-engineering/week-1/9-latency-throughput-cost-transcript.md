# Production Constraints: Latency, Throughput, Cost, and Reliability

## Offline Metrics vs Production Reality

Offline metrics (accuracy, F1, AUC, loss curves) resemble Kaggle competitions. Shipping a real ML product operates under entirely different constraints.

Great offline performance is **necessary but not sufficient** for production readiness. A model with amazing test metrics can still be impossible to ship because it is too slow, too expensive, or too fragile.

---

## Constraint 1: Latency

Users do not experience **average** latency — they feel the **slowest** calls. That is why production systems focus on **percentile latencies**:

| Metric | Meaning |
|--------|---------|
| **P95** | 95% of requests complete faster than this value |
| **P99** | 99% of requests complete faster than this value |

At scale, even 1% slow requests = a huge number of bad experiences (timeouts, spinning loaders, broken workflows).

**Budget reality:** The model gets only a slice of total request latency. Network hops, databases, and upstream services consume the rest. Model engineers must design for strict latency budgets in user-facing real-time applications.

---

## Constraint 2: Throughput

How many requests per second (RPS) can the system handle?

| Traffic Pattern | Challenge |
|-----------------|-----------|
| Daily cycles | Morning/evening peaks, weekend dips |
| Event spikes | Marketing campaigns, product launches, news events |

**Key questions:**

- Can the system handle **peak RPS**, not just average?
- What happens if traffic doubles overnight?
- Is autoscaling configured? Is there spare capacity?

Sometimes a simpler model wins — not because it is more accurate, but because it scales predictably and does not collapse under load.

---

## Constraint 3: Cost

Each prediction has a price:

| Cost Component | What Drives It |
|----------------|----------------|
| **Compute** | CPU/GPU time per request |
| **Memory** | RAM/VRAM to keep model loaded |
| **Storage & bandwidth** | Model artifacts, features, data movement |

At millions of requests per day, even small per-request costs compound rapidly.

**Trade-off question:** Is an extra 1–2% accuracy worth 3–4x the cost per prediction?

---

## Constraint 4: Reliability

Products operate under explicit uptime targets (99.99%, 99.999%) with **error budgets** — how many failures per month are acceptable.

| Question | Why It Matters |
|----------|----------------|
| What if the model is unavailable or too slow? | Need fallback heuristics or cached results |
| Does the system degrade gracefully? | Partial failure vs hard crash |

A slightly less accurate but rock-solid model often beats a fancy model that is frequently down. **Reliability is part of the product.**

---

## Constraint 5: Compliance and Privacy

Depending on industry and region:

- Data residency requirements (data must stay in specific countries/regions)
- PII and sensitive data handling (financial, health)
- Audit and explainability requirements for model decisions

These affect cloud region choice, external API usage, and how predictions/inputs are logged. Compliance must be **by design**, not an afterthought.

---

## Common Pitfalls / Exam Traps

- Optimizing average latency while ignoring P99 — tail latency drives user experience at scale
- Sizing for average RPS instead of peak — systems collapse during traffic spikes
- Ignoring per-request cost at low traffic — costs explode at scale
- Treating reliability as infra-only — model engineers must design fallbacks and graceful degradation
- Adding compliance as a post-deployment patch — retrofitting is expensive and risky

---

## Quick Revision Summary

- Offline metrics necessary but not sufficient for production
- Latency: focus on P95/P99; model gets only part of total budget
- Throughput: design for peak RPS and traffic spikes, not averages
- Cost: per-request compute + memory + storage compounds at scale
- Reliability: uptime targets, error budgets, graceful degradation, fallbacks
- Compliance: data residency, PII, auditability — design in from the start
