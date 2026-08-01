# Machine Learning Model Engineering — Story-Based Learning
## From Factory Floor to Store Shelf: The Complete Mental Model

---

> *"A model in a notebook is a product in a warehouse. Model engineering is everything that gets it onto the shelf, keeps it fresh, and triggers a reorder when the world changes."*

---

# PART 1: THE FACTORY FLOOR (Week 1)
*From Notebook to Product*

---

## Why Models Die in the Notebook: The Integration Gap — The Abandoned Warehouse

**The Story:** A factory builds a brilliant new product. Lab tests show 98% quality. Everyone celebrates — then the product sits in a warehouse forever. No trucks arrive, no store shelves get stocked, no quality inspector watches for defects. This is the **integration gap**: high notebook metrics without **APIs**, **infrastructure**, and **monitoring** to turn weights into a product feature.

**Key mechanics:**
- High notebook metrics often lead nowhere without engineering around the model
- Production needs APIs, infrastructure, and monitoring — not just weights
- Model engineering is the layer between "trained model" and "product feature"
- Missing this layer is why most notebook models never ship
- The discipline focuses on integration and operations, not algorithm novelty

| Missing Piece | Consequence |
|---------------|-------------|
| **API or service** | Other systems cannot call the model |
| **Infrastructure** | Cannot run reliably at scale |
| **Monitoring** | Nobody notices when things break or drift |

**Exam Tip:** Blaming the model when the real blocker is missing infrastructure — great metrics do not auto-deploy

> **Why Models Die in the Notebook: The Integration Gap** = High notebook metrics often lead nowhere without engineering around the model

---

## Defining Model Engineering: From Artifact to Production Service — Artifact to Product

**The Story:** A finished widget on the factory floor is not a product on a store shelf. **Model engineering** is the logistics chain — packaging (**API**), trucking (**deployment**), store ops (**scaling**), quality control (**monitoring**) — that turns a trained **artifact** into an integrated, observable **production service**. Data science picks *what model*; model engineering picks *how to run it*.

**Key mechanics:**
- Model engineering = making models usable, reliable, and scalable in production
- Takes artifacts (checkpoints, pickles) and produces integrated, monitored services
- Data science: *what model*; model engineering: *how to run it*
- Not about inventing algorithms — about real-world operation
- Roles overlap in small teams but responsibilities remain distinct

| Focus Area | Data Science | Model Engineering |
|------------|--------------|-------------------|
| Question answered | What model should we use? | How do we run this safely in production every day? |
| Deliverable | Prototype + offline metrics | Callable, observable, versioned service |
| Time horizon | Experiment cycles | Continuous operation over months/years |

**Exam Tip:** Defining model engineering as "deployment only" — monitoring, versioning, and collaboration are equally core

> **Defining Model Engineering: From Artifact to Production Service** = Model engineering = making models usable, reliable, and scalable in production

---

## Four Core Responsibilities of Model Engineering — Four Department Heads

**The Story:** Beyond the assembly line sit four critical departments: shipping dock (**deployment**), quality lab (**monitoring**), reorder desk (**retraining**), and compliance office (**governance**). Model engineers refactor notebooks into modules, build **inference pipelines**, expose **APIs**, containerise with **Docker**, and balance **accuracy** with **P95/P99 latency**, uptime, and **cost per request**.

**Key mechanics:**
- Four responsibilities: services, constraints, change management, collaboration
- Notebook → modules → inference pipeline → API → Docker/deployable
- Balance accuracy with latency (P95/P99), uptime, and cost per request
- Version everything; use canary/shadow/A-B; enable fast rollback
- Collaborate with data, infra, and product teams — translation role is central

| Step | Detail |
|------|--------|
| Refactor | Notebook code → proper Python modules with tests |
| Inference logic | Preprocessing, model call, postprocessing — explicit and reusable |
| Service wrapper | REST API, gRPC, batch job, or streaming consumer |
| Deployability | Containers (Docker), environment-specific config (dev/staging/prod) |

**Exam Tip:** Focusing only on accuracy while ignoring P99 latency — users feel the slow tail, not the average

> **Four Core Responsibilities of Model Engineering** = Four responsibilities: services, constraints, change management, collaboration

---

## The Seven-Stage ML Lifecycle — Seven Stations on the Line

**The Story:** Station 1 frames the problem; stations 2–4 handle **data**, **features**, and **training**; station 5 **deploys**; station 6 **monitors**; station 7 **retrains**. Stages 1–4 are research; 5–7 are production where model engineering lives. Skip problem framing and you optimise the wrong metric from day one.

**Key mechanics:**
- Seven stages: framing → data → features → training → deployment → monitoring → retraining
- Stages 1–4 are research/exploration; 5–7 are production (model engineering focus)
- Problem framing defines success metrics before any code is written
- Feature consistency between training and serving prevents skew
- Offline metrics must connect to business/product outcomes

| Question | Why It Matters |
|----------|----------------|
| Where does data come from? | Logs, databases, third-party, sensors, user behavior |
| Do we have labels? | Ground truth vs manual labelling vs weak supervision |
| Is data representative? | Training distribution must match production |
| Privacy/compliance constraints? | GDPR, HIPAA, regional data residency |

**Exam Tip:** Skipping problem framing and jumping to model selection — optimizes the wrong metric

> **The Seven-Stage ML Lifecycle** = Seven stages: framing → data → features → training → deployment → monitoring → retraining

---

## Deployment, Monitoring, and Retraining: The Production Loop — The Production Loop

**The Story:** **Deployment** opens a new store — expose via **API** or **batch**, integrate into product, balance latency, uptime, cost, security. **Monitoring** watches system health, **data drift**, and **model performance**. **Retraining** responds when the world changes or cost exceeds benefit. This loop is the heartbeat of production ML.

**Key mechanics:**
- Deployment: expose model via API or batch; integrate into product; balance latency, uptime, cost, security
- Monitoring: system health + data drift + model performance — catch issues early
- Retraining/deprecation: respond to drift; retire models when cost exceeds benefit
- Lifecycle is a loop: deploy → monitor → retrain → deploy again
- Model engineering lives primarily in stages 5–7

| Deployment Mode | Example Use Case |
|-----------------|------------------|
| **Online API** | Real-time fraud score, search ranking |
| **Batch job** | Nightly churn predictions written to a warehouse |

**Exam Tip:** Treating deployment as a one-time event — it is the start of an ongoing loop

> **Deployment, Monitoring, and Retraining: The Production Loop** = Deployment: expose model via API or batch; integrate into product; balance latency, uptime, cost, security

---

## Where This Course Fits in the ML Lifecycle — The Operations Manual

**The Story:** Data science writes the recipe; model engineering builds the factory, runs trucks, staffs stores, manages reorders. This course focuses on **deployment**, **monitoring**, and **retraining** — not primary training. Earlier lifecycle stages appear as production context; use the seven-stage diagram as a mental map.

**Key mechanics:**
- Course focuses on deployment, monitoring, and retraining — not primary training/research
- Earlier stages (framing, data, features) appear as production context
- Use the lifecycle diagram as a mental map for every module
- Real-world ML = systems over time with feedback loops, not one-time training
- Each module deep-dives into production-focused lifecycle stages

| Stage | Course Coverage |
|-------|-----------------|
| Problem framing, data, features | Discussed as **context** for building production systems |
| **Deployment** | **Core focus** — turning models into services |
| **Monitoring** | **Core focus** — observing real-world behavior |
| **Retraining / deprecation** | **Core focus** — evolving models over time |

**Exam Tip:** Assuming this course teaches algorithm design — it teaches production operations

> **Where This Course Fits in the ML Lifecycle** = Course focuses on deployment, monitoring, and retraining — not primary training/research

---

## Production Constraints: Latency, Throughput, Cost, and Reliability — The Delivery Budget

**The Story:** Every shipment faces three constraints: arrival speed (**latency**, especially **P95/P99**), units per hour (**throughput**, peak **RPS**), and fuel cost (**cost**). Offline metrics like AUC are necessary but insufficient — preprocessing and network overhead consume part of the latency budget before the model even runs.

**Key mechanics:**
- Offline metrics necessary but not sufficient for production
- Latency: focus on P95/P99; model gets only part of total budget
- Throughput: design for peak RPS and traffic spikes, not averages
- Cost: per-request compute + memory + storage compounds at scale
- Reliability: uptime targets, error budgets, graceful degradation, fallbacks

| Metric | Meaning |
|--------|---------|
| **P95** | 95% of requests complete faster than this value |
| **P99** | 99% of requests complete faster than this value |

**Exam Tip:** Optimizing average latency while ignoring P99 — tail latency drives user experience at scale

> **Production Constraints: Latency, Throughput, Cost, and Reliability** = Offline metrics necessary but not sufficient for production

---

## Common Production Failure Modes — Two Recipe Books

**The Story:** Factory workers train on Recipe Book A (**30-day averages**); the store kitchen uses Recipe Book B (**7-day averages**) — same dish name, different ingredients. This is **training-serving skew**: different **feature logic** offline vs online. Fix with shared **pipelines** or a **feature store**, not hyperparameter tuning.

**Key mechanics:**
- Four recurring failure modes: training-serving skew, data drift/staleness, silent failures, infra/dependency issues
- Training-serving skew: different feature logic offline vs online — fix with shared pipelines/feature store
- Data drift: world changes, model does not — monitor inputs, retrain proactively
- Silent failures: healthy infra metrics masking broken data/model pipelines
- Infra issues: timeouts, scaling failures, dependency changes — versioning, observability, collaboration

| Divergence Source | Example |
|-------------------|---------|
| Different preprocessing code | Offline script vs online service |
| Different missing value handling | Training fills with median; serving fills with zero |
| Different encoding/normalization | Training uses one-hot; serving uses label encoding |

**Exam Tip:** Debugging training-serving skew with more tuning — fix the feature pipeline, not hyperparameters

> **Common Production Failure Modes** = Four recurring failure modes: training-serving skew, data drift/staleness, silent failures, infra/dependency issues

---

## Why ML Needs Engineering and Operations — Expired Best-Before Dates

**The Story:** Constraints plus failure modes explain why ML needs engineering: **integration**, **deployment**, **monitoring**, **maintenance** — not algorithm choice. A perfect-launch model rots as tastes shift. Better recipes alone cannot fix **skew**, **drift**, **silent failures**, or **infra issues**.

**Key mechanics:**
- Constraints + failure modes = why ML needs engineering and operations
- Failures are integration, deployment, monitoring, maintenance — not algorithm choice
- Better models alone do not fix skew, drift, silent failures, or infra issues
- Model engineering + MLOps address complexity around the model
- Use constraints and failures as backdrop for every design decision in the course

| What Looks Like a Model Problem | What It Actually Is |
|--------------------------------|---------------------|
| Poor online accuracy after great offline metrics | Training-serving skew (integration) |
| Gradual business metric decline | Data drift + stale model (operations) |
| "Everything is fine" but users complain | Silent failure (monitoring gap) |
| Sudden performance drop, weights unchanged | Infrastructure/dependency issue (deployment) |

**Exam Tip:** Proposing "use a better model" as the fix for integration bugs — engineering discipline is required

> **Why ML Needs Engineering and Operations** = Constraints + failure modes = why ML needs engineering and operations

---

## MLOps: The Operating System for Production ML — Factory OS vs Building Plumbing

**The Story:** **DevOps** keeps plumbing, electricity, and doors working. **MLOps** runs the factory floor where **data** changes daily, models degrade on shelves, and every batch needs a traceable recipe card. MLOps = **DevOps + Data + Models** — monitor system health *and* data/model health.

**Key mechanics:**
- MLOps = DevOps practices adapted for ML systems
- Handles changing data, model degradation, reproducibility, auditability
- MLOps = DevOps + Data + Models
- Monitor system health AND data/model health
- Alerts for drift, regressions, pipeline failures — prevent silent failures

| Pillar | Goal |
|--------|------|
| **Automation** | Training, testing, deployment, monitoring |
| **Reliability & scalability** | Model services as solid as any production service |
| **Collaboration** | Data scientists, ML engineers, infra engineers, product — working smoothly |
| **Ultimate goal** | Make it easy and safe to put models in production and keep them healthy as the world changes |

**Exam Tip:** Equating MLOps with "using Kubernetes" — it is a practice set, not a tool

> **MLOps: The Operating System for Production ML** = MLOps = DevOps practices adapted for ML systems

---

## MLOps Core Practices: Versioning, Pipelines, and CI/CD — Recipe Cards and Assembly Lines

**The Story:** Stamp every batch with a recipe card (**versioning**: **data**, **code**, **config**, **model**). The assembly line (**pipeline**) runs ingest → features → train → deploy with identical output for identical inputs. **CI** tests transforms and model quality gates; **CD** uses **canary**, **shadow**, and **A/B** releases.

**Key mechanics:**
- Version data, model artifacts, and config — for reproducibility, auditability, rollback
- Reproducible pipelines: ingest → features → train → deploy; same input = same output for anyone
- CI: test transforms, training, inference, model quality gates
- CD: canary, shadow, A/B — small frequent safe releases
- These three practices form the MLOps backbone alongside monitoring

| Artifact | Examples |
|----------|----------|
| **Data** | Exact dataset or feature snapshot used for training |
| **Model** | Checkpoints, serialized artifacts |
| **Config** | Hyperparameters, thresholds, routing rules, feature flags |

**Exam Tip:** Versioning only the model artifact — data and config changes cause silent behavior shifts

> **MLOps Core Practices: Versioning, Pipelines, and CI/CD** = Version data, model artifacts, and config — for reproducibility, auditability, rollback

---

## The ML Model Engineer Role — The Plant Manager

**The Story:** The data scientist invents the recipe. The **model engineer** — at the intersection of **research**, **infra**, and **product** — turns prototypes into robust, observable, scalable services via refactoring, **logging/metrics**, **CI/CD**, **versioning**, and cross-team collaboration.

**Key mechanics:**
- Model engineer: intersection of research, infra, and product
- Mission: prototypes → robust, observable, scalable services
- Day-to-day: refactor code, build services, logging/metrics, CI/CD, versioning, collaboration
- Primary lifecycle stages: deployment, monitoring, retraining
- Anchors the deploy-monitor-retrain loop

| Ownership Area | Scope |
|----------------|-------|
| **Serving path** | How inputs become predictions in production |
| **Deploy-monitor-retrain loop** | Safe deployment, observation, evolution |
| **Core principle** | Models must be usable in the real world — not just clever |

**Exam Tip:** Treating model engineer as "junior data scientist who deploys" — it is a distinct engineering specialization

> **The ML Model Engineer Role** = Model engineer: intersection of research, infra, and product

---

## Building an ML Project from Scratch — First Shift on the Floor

**The Story:** Before shipping, workers set up their station: **virtual environment** (isolated deps), project scaffold, **Jupyter** notebook, **Hugging Face** model, prediction run, packaging. **UV** accelerates venv creation — the first step from notebook experiment to deployable project.

**Key mechanics:**
- Lab flow: environment → project → notebook → Hugging Face → prediction → package
- Virtual environments isolate dependencies per project
- UV: fast package manager for venv creation and dependency install
- Jupyter in VS Code for experimentation with correct kernel selection
- Start with a lightweight use case (text assistant) to validate the full pipeline

| Component | Purpose |
|-----------|---------|
| Development environment | Clean, isolated workspace |
| Project structure | Organized files and dependencies |
| Experimentation | Jupyter notebooks for exploration |
| Model sourcing | Hugging Face Hub for pre-trained models |

**Exam Tip:** Skipping virtual environments — dependency conflicts cause "works locally, fails in CI" bugs

> **Building an ML Project from Scratch** = Lab flow: environment → project → notebook → Hugging Face → prediction → package

---

## Virtual Environments, Jupyter, and Hugging Face Setup — The Tool Bench

**The Story:** Activate the venv before touching tools: `source .venv/bin/activate`. **Jupyter** runs inside that kernel. **Hugging Face** is the parts catalogue — model hub, datasets, libraries, playground — where pre-trained components replace forging from scratch.

**Key mechanics:**
- Activate venv before any installs: `source .venv/bin/activate` (Mac/Linux)
- Jupyter: install extension, use `.ipynb`, select venv as kernel
- Hugging Face = model hub + datasets + libraries + playground
- Gated models need account + license acceptance + access token
- First lab use case: lightweight text assistant on CPU — validate pipeline, not quality

| Platform | Activate Command |
|----------|------------------|
| Linux / Mac | `source .venv/bin/activate` |
| Windows CMD | `.venv\Scripts\activate` |

**Exam Tip:** Forgetting to activate venv before `uv pip install` — packages install globally

> **Virtual Environments, Jupyter, and Hugging Face Setup** = Activate venv before any installs: source .venv/bin/activate (Mac/Linux)

---

## Hugging Face Ecosystem and Text Generation Pipeline — From Parts to Pipeline

**The Story:** DistilGPT-2 teaches the **text generation pipeline**: download → load → **tokenize** → generate → decode. The Hugging Face ecosystem mirrors how production composes pre-built components into a full **MLOps lifecycle** connecting lab work to deploy-monitor-retrain.

**Key mechanics:**
- Hugging Face = model hub + datasets + libraries + community ecosystem
- DistilGPT-2: lightweight CPU-friendly model for pipeline learning
- Pipeline: download → load → tokenize → generate → decode
- Two artifacts: tokenizer (text↔tokens) and model (weights)
- Imperfect output is fine — validate that the pipeline works end-to-end

| Role | What Hugging Face Provides |
|------|---------------------------|
| **Model hub** | Thousands of community and enterprise models |
| **Dataset hub** | Real-world data for fine-tuning |
| **Open-source libraries** | Transformers, Datasets, Accelerate |
| **Community** | Continuous model improvements and sharing |

**Exam Tip:** Judging lab success by output quality instead of pipeline correctness

> **Hugging Face Ecosystem and Text Generation Pipeline** = Hugging Face = model hub + datasets + libraries + community ecosystem

---

# PART 2: SHIPPING MODES (Week 2)
*Batch Trucks, Express Delivery, and Live Conveyors*

---

## Definition of Model Inference — The Cash Register

**The Story:** **Training** learns $f$ from historical data once; **inference** calls $f$ continuously — like a cash register after the store opens. Inference dominates call volume and cost. Every call: receive → validate → transform → predict → post-process → return.

**Key mechanics:**
- **Training** learns $f$ from historical data; **inference** calls $f$ on new data continuously
- Inference dominates the model lifecycle in call volume and operational cost
- Every inference call follows: receive → validate → transform → predict → post-process → return
- The same six-step pipeline applies to batch, online, and streaming — only scale and timing differ
- Feature preprocessing at inference must **exactly match** training to avoid silent accuracy loss


$f$
$\text{prediction} = f(\text{input features})$
$k$

| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| **Training** | Learn parameters from historical data | Labelled (or unlabelled) training set | Trained model weights |
| **Inference** | Apply the trained model to new, unseen data | Fresh features at serving time | Predictions, scores, embeddings |

**Exam Tip:** "Inference = forward pass only." — The forward pass is one step in a six-step pipeline; network, validation, and feature prep often dominate latency.

> **Definition of Model Inference** = Training learns $f$ from historical data; inference calls $f$ on new data continuously

---

## Latency, Throughput, and Cost: The Inference Metrics Triangle — The Metrics Triangle

**The Story:** Three numbers govern serving: **latency** (**P95/P99** tail matters most), **throughput** (**RPS** online, rows/sec batch, events/sec streaming), and **cost**. Optimising one without watching the others breaks the delivery promise.

**Key mechanics:**
- Three core inference metrics: **latency**, **throughput**, **cost** — they drive all serving design
- **P95/P99 latency** matters more than average for user-facing systems; users feel the tail
- **Throughput** = predictions per unit of time; measure in RPS (online), rows/sec (batch), events/sec (streaming)
- **Utilisation** reveals whether capacity is wasted (idle) or dangerously saturated (maxed out)
- Every prediction burns compute, memory, storage, and bandwidth — cost scales with call volume

| Metric | Definition | When It Matters |
|--------|------------|-----------------|
| **Average (mean)** | Mean across many requests | General system health |
| **P50 (median)** | 50% of requests are faster | Typical user experience |
| **P95** | 95% of requests are faster | Product SLA targets |
| **P99** | 99% of requests are faster | Worst-case user experience |

**Exam Tip:** Optimizing average latency when the SLA specifies P95/P99 — averages hide tail problems.

> **Latency, Throughput, and Cost: The Inference Metrics Triangle** = Three core inference metrics: latency, throughput, cost — they drive all serving design

---

## Inference Patterns: Setup and Mental Model — Three Shipping Modes

**The Story:** Inference is $\text{prediction} = f(\text{input features})$ — the function stays constant; delivery mode changes. **Batch** trucks on schedule; **online** couriers per doorbell; **streaming** conveyors never stop. Choice depends on **who waits**, **freshness**, and **volume**.

**Key mechanics:**
- Model inference is $\text{prediction} = f(\text{input features})$ — the function stays constant
- Three patterns: **batch** (scheduled bulk), **online** (synchronous request-response), **streaming** (continuous pipeline)
- Pattern choice depends on **who is waiting**, **freshness requirements**, and **data volume/frequency**
- Batch optimizes throughput; online optimizes P95/P99 latency; streaming optimizes event-to-action latency and sustained throughput
- Real systems often use **hybrid** architectures combining patterns


$\text{prediction} = f(\text{input features})$
$f$
$\hat{y} = f(x)$

| Dimension | What Varies | Examples |
|-----------|-------------|----------|
| **Frequency** | How often we invoke $f$ | Once a month, once a minute, thousands per second |
| **Batch size** | How many items per call | Single record, 10,000-row chunk, continuous stream |
| **Urgency** | Who is waiting | Nobody (batch), user in UI (online), downstream pipeline (streaming) |

**Exam Tip:** "We need real-time, so we must use online inference." — Streaming may be better for continuous event reaction without a blocking caller.

> **Inference Patterns: Setup and Mental Model** = Model inference is $	ext{prediction} = f(	ext{input features})$ — the function stays constant

---

## Batch Inference: Definition and Architecture — The Nightly Truck Run

**The Story:** **Batch inference** scores a warehouse snapshot — thousands to millions of rows — on a schedule; nobody waits per row. Pipeline: read → preprocess → parallel model inference → write predictions → monitor. Success = job finishes before the business deadline.

**Key mechanics:**
- **Batch inference** scores many items at once on a schedule; nobody waits per row
- Inputs: large static datasets; outputs: predictions written to warehouse/file/feature store
- Pipeline: read → preprocess → model inference (parallel/chunked) → write → monitor
- Success metric: **total job time** and **throughput** (rows/sec), not per-row latency
- Infrastructure: scheduler + batch job + output target + monitoring (not 24/7 API)

| Property | Batch Characteristic |
|----------|---------------------|
| **Schedule** | Periodic — once a day, hourly, every 15 minutes |
| **Caller** | No human waiting per row |
| **Latency concern** | Total job completion time, not per-row latency |
| **Output** | Bulk write to storage for later consumption |

**Exam Tip:** Measuring per-row latency in batch — it is irrelevant; only total job time matters.

> **Batch Inference: Definition and Architecture** = Batch inference scores many items at once on a schedule; nobody waits per row

---

## Batch Inference: Offline Use Cases and Trade-offs — Tomorrow's Price Tags

**The Story:** Churn scores, credit risk, offline recommendations, marketing lists, compliance reports: no one waits per row; predictions can be hours old. Choose **batch** for deadline-driven bulk scoring with simpler infra, higher throughput, heavier models.

**Key mechanics:**
- Classic batch use cases: churn scoring, credit risk, offline recommendations, marketing lists, compliance reports
- Choose batch when **no one waits per row** and predictions can be hours/days old
- Advantages: high throughput, simpler infra, easy rollback, supports heavier models
- Trade-offs: staleness, slower experimentation feedback loop, unsuitable for instant context-aware decisions
- **Hybrid pattern**: batch precomputes candidates/features; online serves fresh rankings

| Domain | Use Case | Freshness Tolerance |
|--------|----------|---------------------|
| **Customer analytics** | Monthly/weekly churn predictions for all customers | Days |
| **Credit risk** | Portfolio-wide risk scoring for all accounts | Daily |
| **Recommendations** | Precompute user-item scores and candidate lists overnight | Hours (served online later) |
| **Marketing** | Campaign audience selection — who receives tomorrow's email | Until next morning |

**Exam Tip:** "Batch predictions are always stale and therefore useless." — Many products (weekly campaigns, portfolio reports) explicitly tolerate staleness.

> **Batch Inference: Offline Use Cases and Trade-offs** = Classic batch use cases: churn scoring, credit risk, offline recommendations, marketing lists, compliance reports

---

## Batch Inference: Metrics, Pros, Cons, and Architecture — Throughput Over Speed

**The Story:** Batch optimises **total job time** and **throughput**; per-row latency is irrelevant. Savings from off-peak scheduling, **spot instances**, longer wall-clock tolerance. Architecture: source → **scheduler** → pipeline → output → alerting.

**Key mechanics:**
- Batch optimizes **throughput** and **total job time**; per-row latency is low priority
- Cost savings via off-peak scheduling, spot instances, and tolerating longer wall-clock times
- Architecture: data source → scheduler → batch pipeline → output target → alerting
- Pros: high throughput, simple infra, easy rollback, supports heavy models
- Cons: staleness, slow feedback loops, unsuitable for real-time user-facing decisions

| Metric | Batch Priority | Online Priority |
|--------|---------------|-----------------|
| **Total job time** | Top priority | N/A |
| **Throughput (rows/sec)** | Top priority | Important but secondary |
| **Per-row latency** | Low priority | Top priority (P95/P99) |
| **Cost** | Optimizable via scheduling | Critical at peak traffic |

**Exam Tip:** Applying online latency SLOs to batch jobs — per-row latency is irrelevant in batch.

> **Batch Inference: Metrics, Pros, Cons, and Architecture** = Batch optimizes throughput and total job time; per-row latency is low priority

---

## Online Inference: The Request-Response Pattern — The Express Courier

**The Story:** **Online inference**: one request in, one response out; caller blocks. Transport via **HTTP/JSON** or **gRPC/protobuf**. Same pipeline as batch but per-request under a millisecond **latency budget**.

**Key mechanics:**
- **Online inference** = one request in, one response out; caller is blocked until prediction arrives
- Transport: HTTP/JSON or gRPC/protobuf; caller can be UI, mobile app, or backend service
- Same inference pipeline as batch (validate → transform → predict → post-process) but per-request with tight latency budget
- Architecture includes load balancer, replicas, feature store, cache, and monitoring
- Total latency = sum of all pipeline stages; P95/P99 targets apply to the **entire path**, not just the model


$k$
$\text{Total Latency} = t_{\text{network}} + t_{\text{validate}} + t_{\text{features}} + t_{\text{model}} + t_{\text{postprocess}}$

| Step | Action | Latency Impact |
|------|--------|---------------|
| Receive payload | JSON over HTTP or protobuf over gRPC | Network RTT |
| Validate input | Check fields, types, ranges; reject bad requests early | Microseconds |
| Feature transform | Encoding, normalization, embeddings — same as training | Often significant |
| Forward pass | Compute logits, probabilities, scores | Model-dependent |

**Exam Tip:** "Online inference only means REST APIs." — gRPC, internal service-to-service calls, and even synchronous batch-of-one are all online patterns.

> **Online Inference: The Request-Response Pattern** = Online inference = one request in, one response out; caller is blocked until prediction arrives

---

## Online Inference: Interactive Use Cases and Metrics — The Impatient Shopper

**The Story:** Search ranking, real-time recommendations, fraud checks, personalisation: a **live interaction blocks** on the prediction. Latency hits page load, conversion, abandonment — users feel speed, not AUC.

**Key mechanics:**
- Online inference is required when a **live interaction blocks** on the prediction
- Use cases: search ranking, real-time recommendations, fraud checks, dynamic personalization
- Model latency directly impacts page load, responsiveness, conversion, and abandonment
- Key metrics: **P95/P99 latency** and **error rate** are product-level requirements
- Benefits: fresh context, per-request personalization, faster training feedback loops

| Domain | Scenario | Why Online? |
|--------|----------|-------------|
| **Search & ranking** | User types a query; results must be ranked in real time | User staring at search box |
| **Recommendations** | Homepage or product page shows personalized suggestions | Page load blocked on ranking |
| **Fraud / risk** | Payment, login, or password reset checked before proceeding | Transaction blocked until decision |
| **Dynamic UX** | Content layout, pricing, or personalization adapts to current user context | UI rendering depends on prediction |

**Exam Tip:** Reporting average latency when the SLA specifies P95 — always match the metric to the requirement.

> **Online Inference: Interactive Use Cases and Metrics** = Online inference is required when a live interaction blocks on the prediction

---

## Online Inference: Latency, Reliability, and Production Techniques — Express With Guardrails

**The Story:** Online serving needs **P95/P99 SLOs**, spike scaling, cascade protection. Techniques: **caching**, **auto-scaling**, **circuit breakers**, **rate limiting**, **hybrid batch+online** for non-real-time features.

**Key mechanics:**
- Online advantages: fresh context, per-request personalization, faster training feedback
- Online challenges: strict P95/P99 SLOs, scaling complexity, cascading failure risk
- Key production techniques: **caching**, **auto-scaling**, **circuit breakers/timeouts**, **rate limiting**, **hybrid batch+online**
- Hybrid pattern: batch precomputes heavy work; online does light real-time ranking
- Batch = backstage; online = on-stage — same model, different engineering constraints


$f(\text{input})$

| Advantage | Description |
|-----------|-------------|
| **Fresh predictions** | Latest session data, recent actions, geolocation, device type — context absent from yesterday's batch snapshot |
| **Per-request personalization** | Two users on the same page simultaneously see completely different rankings or recommendations |
| **Tighter feedback loop** | Log each prediction with user interactions; feed outcomes back into training faster than batch cycles allow |

**Exam Tip:** "Circuit breakers are only for microservices." — They are essential around feature stores, embedding services, and any inference dependency.

> **Online Inference: Latency, Reliability, and Production Techniques** = Online advantages: fresh context, per-request personalization, faster training feedback

---

## Streaming Inference: Architecture and Pattern Comparison — The Live Conveyor

**The Story:** **Streaming inference** processes continuous events: source → transport → processing → model → sinks. No job start/end — 24/7 conveyor. Outputs feed alerts, features, dashboards — not direct user responses.

**Key mechanics:**
- **Streaming inference** processes continuous event flows through a long-running pipeline
- Architecture: event source → stream transport → processing layer → model step → sinks
- No job start/end; pipeline runs 24/7; outputs go to alerts, features, dashboards — not direct user responses
- Differs from batch (static snapshot, scheduled) and online (single request, synchronous response)
- Introduces stateful concepts: windowing, watermarks, checkpoints

| Component | Role | Examples |
|-----------|------|----------|
| **Event source** | Where events originate | Applications, IoT sensors, click streams, server logs |
| **Stream transport** | Durable, ordered event delivery | Apache Kafka, AWS Kinesis, Google Pub/Sub |
| **Stream processing** | Transform, join, aggregate events | Apache Flink, Spark Structured Streaming |
| **Model step** | Call model on each event or mini-batch | Embedded inference within processing job |

**Exam Tip:** "Streaming = online but faster." — Streaming has no blocking caller; it is an always-on pipeline, not request-response.

> **Streaming Inference: Architecture and Pattern Comparison** = Streaming inference processes continuous event flows through a long-running pipeline

---

## Streaming Inference: Use Cases, Metrics, and Trade-offs — Conveyor Lag

**The Story:** Fraud, clickstream, IoT, security logs need **event-to-action latency**, sustained **throughput**, **lag/backpressure**. Growing lag means the conveyor falls behind reality even when no single request times out.

**Key mechanics:**
- Streaming use cases: fraud detection, clickstream analytics, IoT sensors, log/security analytics
- Key metrics: **event-to-action latency**, **sustained throughput**, **lag/backpressure**, **24/7 cost**
- Lag growing = pipeline falling behind; backpressure = system overloaded
- Benefits: near-real-time reaction, continuous behavioral view, temporal sequence context
- Costs: higher complexity, 24/7 operations, harder debugging, restart/replay challenges


$\text{Event-to-Action Latency} = t_{\text{action}} - t_{\text{event occurrence}}$

| Domain | Stream | Model Action | Downstream Effect |
|--------|--------|-------------|-------------------|
| **Fraud / anomaly detection** | Transaction, login, or system metric events | Score each event for suspiciousness | Trigger alert or automated block |
| **Clickstream analytics** | Page views, clicks, scrolls, interactions | Detect patterns, segment users, compute real-time features | Personalization, A/B test assignment |
| **IoT / sensor data** | Device readings from machines, vehicles, sensors | Predict failure, anomaly, or state transition | Maintenance alert, autonomous action |
| **Log / security analytics** | Application, infrastructure, security logs | Flag unusual patterns, correlate across streams | Security incident response |

**Exam Tip:** "Streaming is always better than batch because it is real-time." — Use streaming only when the problem genuinely demands it; daily batch may suffice.

> **Streaming Inference: Use Cases, Metrics, and Trade-offs** = Streaming use cases: fraud detection, clickstream analytics, IoT sensors, log/security analytics

---

## Choosing the Right Inference Pattern: Decision Guide — The Dispatch Desk

**The Story:** Three questions: sub-second user wait? scheduled bulk? continuous stream? **Online** = blocked caller; **batch** = deadline bulk; **streaming** = always-on. Match pattern to business — do not default to online.

**Key mechanics:**
- Three decision questions: sub-second user response? scheduled bulk? continuous event stream?
- **Online**: caller blocked, synchronous request-response
- **Batch**: millions of rows, deadline-driven, no one waiting per row
- **Streaming**: continuous events, near-real-time reaction, no direct caller
- Decision axes: who is waiting, freshness requirements, data volume/frequency

| Signal | Pattern |
|--------|---------|
| User clicked a button; system called an API; flow cannot proceed without prediction | **Online** |
| Payment checkout blocked until fraud decision | **Online** |
| Search results must rank before page renders | **Online** |

**Exam Tip:** Defaulting to online APIs by habit — batch is simpler and cheaper when freshness tolerance is hours or days.

> **Choosing the Right Inference Pattern: Decision Guide** = Three decision questions: sub-second user response? scheduled bulk? continuous event stream?

---

## Inference Patterns: Metrics Mapping and Scenario Guide — Pattern Scorecard

**The Story:** Each pattern optimises different metrics: **batch** (throughput/job time), **online** (**P95/P99**), **streaming** (event-to-action/lag). Weekly churn = batch; payment fraud = online; login monitoring = streaming.

**Key mechanics:**
- Each pattern optimizes different metrics: batch (throughput/job time), online (P95/P99), streaming (event-to-action/lag)
- Scenario mapping: weekly churn = batch, payment fraud = online, login monitoring = streaming
- Don't default to online — match pattern to business needs
- Same model $f(x)$, different serving wrapper and metric priorities
- Lab measures batch (total time, rows/sec) vs online (P95 latency, RPS) to make trade-offs tangible


$\text{prediction} = f(\text{input features})$
$f$
$f(x)$

| Pattern | Optimize For | De-prioritize | Cost Strategy |
|---------|-------------|---------------|---------------|
| **Batch** | Throughput, total job time | Per-row latency | Off-peak scheduling, spot instances |
| **Online** | P95/P99 latency, error rate | — | Right-sized replicas, caching, auto-scaling |
| **Streaming** | Event-to-action latency, sustained throughput | — | Efficient 24/7 workers, minimize lag |

**Exam Tip:** "Same model = same metrics matter." — The pattern determines metric priority, not the model.

> **Inference Patterns: Metrics Mapping and Scenario Guide** = Each pattern optimizes different metrics: batch (throughput/job time), online (P95/P99), streaming (event-to-action/lag)

---

## Model Selection and Single-Request Inference — Picking the Right Engine

**The Story:** Flan-T5 Small (77M params) balances capability and CPU constraints. **Causal LM** uses `AutoModelForCausalLM`; **Seq2Seq** uses `AutoModelForSeq2SeqLM`. Instruction-tuned Flan-T5 follows task prompts — pick the engine before building the truck.

**Key mechanics:**
- Model selection must balance capability with hardware constraints (Flan-T5 Small: 77M params, runs on CPU)
- **Causal LM** (GPT family) uses `AutoModelForCausalLM`; **Seq2Seq** (T5/Flan-T5) uses `AutoModelForSeq2SeqLM`
- Flan-T5 is instruction-tuned — follows task prompts like "translate" or "classify sentiment"
- Single-request inference: tokenize → generate → decode; ~60–70 ms on CPU
- Lab scales to 1,000-row CSV for bulk scoring experiments

| Factor | Impact on Inference |
|--------|-------------------|
| **Parameter count** | Larger models need more memory and compute per prediction |
| **Architecture type** | Determines which Hugging Face `AutoModel` class to use |
| **Instruction tuning** | Models trained on tasks (translation, classification) follow prompts rather than just predicting next token |

**Exam Tip:** Using `AutoModelForCausalLM` for T5/Flan-T5 models — must use `AutoModelForSeq2SeqLM`.

> **Model Selection and Single-Request Inference** = Model selection must balance capability with hardware constraints (Flan-T5 Small: 77M params, runs on CPU)

---

## Sequential vs Batch Inference Performance — One Box vs Pallet Load

**The Story:** Sequential: 1,000 inputs in ~61 sec (~16.25/sec CPU). **Batch inference** groups inputs per forward pass; **padding** for variable text adds overhead. Bigger pallets are not always faster on a small dock.

**Key mechanics:**
- Sequential baseline: 1,000 inputs in ~61 sec, ~16.25 inputs/sec on CPU
- Batch inference groups multiple inputs per forward pass for better hardware utilization
- **Padding** required for variable-length text; adds compute overhead
- Small batches (size 2) can be **slower** than sequential on CPU due to padding
- Large batches (16, 64) amortize padding cost and achieve higher throughput (21–26 inputs/sec)


$\text{Throughput} = \frac{\text{Number of inputs}}{\text{Total time}} = \frac{1000}{61} \approx 16.25 \text{ inputs/sec}$

| Task Type | Example Prompt |
|-----------|---------------|
| Sentiment classification | `classify the sentiment of this review: ...` |
| Translation | `translate English to French: ...` |
| Question answering | `What type of machine learning is ...` |
| Summarization | `summarize: ...` |

**Exam Tip:** "Batching is always faster." — Small batch sizes on CPU can be slower than sequential due to padding overhead.

> **Sequential vs Batch Inference Performance** = Sequential baseline: 1,000 inputs in ~61 sec, ~16.25 inputs/sec on CPU

---

## Summary: Interpreting Inference Metrics and Trade-offs — The Padding Tax

**The Story:** Batch size 2 worse (12.3/sec) than sequential (16.25) — padding tax exceeded parallelism gain on CPU. Batch 64 best (26.0). Measure before assuming; hardware determines the sweet spot.

**Key mechanics:**
- Batching trade-off: parallelism benefit vs padding cost
- Sequential baseline: 16.25 inputs/sec; batch size 2 was worse (12.3); batch size 64 was best (26.0)
- Small batches fail because padding overhead outweighs parallelism on CPU
- Large batches win by amortizing padding and setup costs across many inputs
- Choose batch size empirically: start small, increase, measure, stop at plateau or memory limit


$\text{Cost per input} = \frac{\text{Padding overhead} + \text{Setup cost}}{\text{Batch size}}$

| Term | Meaning |
|------|---------|
| **Batch size** | Number of inputs processed per forward pass |
| **Sequential** | Batch size = 1; one input per pass |
| **Padding** | Adding tokens to shorter inputs so all inputs in a batch have equal length |

**Exam Tip:** "Always use the largest batch size." — Memory limits and diminishing returns cap optimal size.

> **Summary: Interpreting Inference Metrics and Trade-offs** = Batching trade-off: parallelism benefit vs padding cost

---

# PART 3: THE RETAIL STOREFRONT (Week 3)
*Putting Models on the Shelf*

---

## Defining Model Serving: Artefact vs Service — Passive File, Active Clerk

**The Story:** A pickle on disk is a passive **artefact**; a running API is an active **service** with endpoints and ops integration. **Model serving** loads once, handles requests, returns predictions through receive → validate → transform → infer → post-process → respond.

**Key mechanics:**
- Model serving = long-lived service that loads a model, handles requests, and returns predictions.
- **Artefact** = passive file; **service** = active process with endpoints and operational integration.
- Each request flows through: receive → validate → transform → infer → post-process → respond.
- Serving orchestrates the full pipeline, not just `model.predict()`.
- Runtime can be FastAPI, Flask, gRPC, serverless, or specialised engines — the pattern is the same.


$p > 0.85$

| Aspect | Model Artefact | Model Service |
|--------|----------------|---------------|
| **Form** | Serialised file on disk (`.pkl`, `.pt`, `.onnx`) | Running process or container |
| **State** | Passive — waits to be loaded | Active — listens for requests |
| **Interface** | None | Exposes endpoints (`POST /predict`, `GET /health`) |
| **Integration** | None | Connects to clients, monitoring, logging |

**Exam Tip:** **Equating artefact with service** — having `model.pkl` on S3 is not model serving; serving requires a running process with an API.

> **Defining Model Serving: Artefact vs Service** = Model serving = long-lived service that loads a model, handles requests, and returns predictions.

---

## Core Responsibilities of the Model Serving Layer — Five Counter Duties

**The Story:** The serving counter handles five domains: model lifecycle, **input validation**, efficient inference, response formatting, operations. Load the model **once at startup** — never per request. **Schema enforcement** (Pydantic, protobuf) prevents garbage input and **training-serving skew**.

**Key mechanics:**
- Five responsibility domains: model lifecycle, input validation, efficient inference, response formatting, operations.
- Load model **once at startup**; never per request.
- Schema enforcement (Pydantic, protobuf, JSON Schema) prevents garbage input and training-serving skew.
- Inference must respect latency (P95/P99), throughput, and stability under real traffic.
- Responses need stable schemas with predictions plus optional metadata (version, confidence, request ID).

| Check | Purpose |
|-------|---------|
| Required fields present | Prevent partial inputs from reaching the model |
| Correct types (string, number, enum, array) | Catch client bugs early |
| Value ranges and constraints | Block out-of-distribution garbage |
| Graceful error handling | Return HTTP 400 with clear messages, not stack traces |

**Exam Tip:** **Per-request model loading** — the single most common serving anti-pattern; always load once at startup.

> **Core Responsibilities of the Model Serving Layer** = Five responsibility domains: model lifecycle, input validation, efficient inference, response formatting, operations.

---

## Monolithic Model Serving Architecture — Everything Under One Roof

**The Story:** A **monolith** embeds the model inside the main app — same process, no separate service. Simple deployment, low overhead, fast iteration — but you cannot scale the model independently, deployments are coupled, blast radius is large.

**Key mechanics:**
- Monolith = model embedded inside the main application, same process, no separate service.
- Pros: simple deployment, low overhead, fast iteration, easy local dev.
- Cons: cannot scale model independently, coupled deployments, tech stack lock-in, large blast radius.
- Good for: internal tools, POCs, low-traffic ML features.
- Move to microservices when: model is heavy/GPU-hungry, traffic grows, teams need independent evolution.

| Advantage | Explanation |
|-----------|-------------|
| **Simple deployment** | Build one artefact, deploy one artefact |
| **Low infrastructure overhead** | No extra services, configs, or deployment pipelines |
| **Straightforward local development** | Run one process; test end-to-end locally |
| **Fast iteration** | Speed matters more than perfect architecture for small teams |

**Exam Tip:** **Dismissing monoliths as always bad** — they are the correct choice for POCs, internal tools, and low-traffic features.

> **Monolithic Model Serving Architecture** = Monolith = model embedded inside the main application, same process, no separate service.

---

## Microservice Model Serving Architecture — Dedicated Prediction Counter

**The Story:** A **model microservice** is a separate container with its own `POST /predict`. Independent scaling, tech freedom, clear ownership, independent rollback — at the cost of more infra, API versioning, network overhead, distributed tracing.

**Key mechanics:**
- Model microservice = separate process/container with its own `POST /predict` API.
- Benefits: independent scaling, tech stack freedom, clear ownership, independent deploy/rollback.
- Costs: more infra, API versioning, network overhead, distributed tracing needs.
- Right when: model is critical, traffic is high, independent iteration is needed.
- The service contract (schema + SLOs) is the foundation that makes microservices work.

| Trade-off | Detail |
|-----------|--------|
| **Deployment complexity** | More services to deploy, configure, and monitor |
| **API design discipline** | Other teams depend on your predict API; breaking changes are costly |
| **Network overhead** | Calls go over HTTP/gRPC, not in-process — adds latency and failure points |
| **Distributed tracing** | When something fails, you must trace requests across multiple services |

**Exam Tip:** **Microservices for everything** — premature splitting adds complexity without benefit for low-traffic POCs.

> **Microservice Model Serving Architecture** = Model microservice = separate process/container with its own POST /predict API.

---

## Serverless Model Serving Architecture — Pop-Up Prediction Booth

**The Story:** **Serverless** packages the model as a cloud function (Lambda, Cloud Functions). Auto-scaling, pay-per-use, zero server management — but **cold starts**, time/memory limits, packaging constraints, and statelessness bite ML workloads.

**Key mechanics:**
- Serverless = model packaged as a cloud-managed function (Lambda, Cloud Functions).
- Pros: auto-scaling, pay-per-use, zero server management.
- Cons: cold starts, time/memory limits, packaging constraints, statelessness.
- Best for: spiky traffic, lightweight models, prototypes, event-driven ML.
- Poor for: latency-critical APIs, large GPU models, sustained high throughput.

| Advantage | Detail |
|-----------|--------|
| **Built-in autoscaling** | Traffic spikes → more function instances; traffic drops → instances spin down |
| **Pay per use** | Cost-effective for low or bursty traffic; no idle server charges |
| **Zero server management** | Cloud provider handles VMs, patching, and capacity |

**Exam Tip:** **Serverless for latency-critical models** — cold starts alone can violate P95 SLOs.

> **Serverless Model Serving Architecture** = Serverless = model packaged as a cloud-managed function (Lambda, Cloud Functions).

---

## Design Decisions in Model Serving Systems — Store Layout Choices

**The Story:** Three layouts: **monolith** (simple, coupled), **microservice** (independent, complex), **serverless** (auto-scale, constrained). No universal winner — depends on criticality, traffic, team structure, **SLOs**. Inference patterns and serving architecture are orthogonal layers.

**Key mechanics:**
- Three architectures: monolith (simple, coupled), microservice (independent, complex), serverless (auto-scale, constrained).
- No universal right answer — depends on criticality, traffic, team structure, and SLOs.
- Inference patterns (batch/online/streaming) and serving architectures are two orthogonal layers.
- Batch → jobs/queues; online → microservice or serverless; streaming → pipeline consumers.
- Lab Docker container works as monolith or microservice depending on deployment context.

| Dimension | Monolith | Microservice | Serverless |
|-----------|----------|--------------|------------|
| **Build & deploy** | One app, one artefact | Separate service with own pipeline | Function package to cloud |
| **Scale model independently** | No | Yes | Automatic (with limits) |
| **Coupling** | Model and app tightly coupled | Model is isolated with API contract | Model is ephemeral per invocation |
| **Operational complexity** | Low | Medium–High | Low (provider-managed) |

**Exam Tip:** **Treating architecture choice as permanent** — teams commonly start monolith and migrate to microservice as traffic grows.

> **Design Decisions in Model Serving Systems** = Three architectures: monolith (simple, coupled), microservice (independent, complex), serverless (auto-scale, constrained).

---

## REST APIs for Machine Learning Serving — The Universal Checkout Lane

**The Story:** **REST** = HTTP verbs + JSON — the default ML API. Dominant pattern: `POST /predict` with JSON features in, JSON predictions out. Universal tooling, human-readable, low friction — the checkout lane every developer knows.

**Key mechanics:**
- REST = HTTP verbs + JSON payloads; the default ML serving API style.
- Dominant pattern: `POST /predict` with JSON features in, JSON predictions out.
- Pros: universal, human-readable, excellent tooling, low friction.
- Cons: verbose payloads, no compile-time typing, inefficient at extreme scale.
- Best default for prototypes, external APIs, and moderate-traffic production.

| Reason | Detail |
|--------|--------|
| **Universal language support** | Callable from Python, JavaScript, Java, Go, curl, browsers |
| **Human-readable payloads** | Easy to inspect, log, and debug |
| **Excellent tooling** | curl, Postman, Bruno, Swagger/OpenAPI auto-documentation |
| **Low onboarding friction** | Any developer who knows web APIs can call your model |

**Exam Tip:** **Assuming REST means no schema enforcement** — Pydantic + OpenAPI provides strong runtime validation even with REST.

> **REST APIs for Machine Learning Serving** = REST = HTTP verbs + JSON payloads; the default ML serving API style.

---

## gRPC for Machine Learning Serving — The Express Lane With Contracts

**The Story:** **gRPC** is contract-first RPC with **Protocol Buffers** — binary, typed, fast. `.proto` schema generates clients; changes caught at compile time. Smaller payloads, strong typing, high throughput — ideal for internal service meshes.

**Key mechanics:**
- gRPC = high-performance, contract-first RPC using Protocol Buffers (binary, not JSON).
- `.proto` schema generates typed clients in multiple languages; changes caught at compile time.
- Advantages: smaller payloads, faster serialization, strong typing, high throughput.
- Best for: internal microservices, real-time systems, large distributed architectures.
- REST at the edge, gRPC inside — the common large-system hybrid pattern.

| Advantage | Detail |
|-----------|--------|
| **Binary encoding** | Payloads are much smaller; serialization/deserialization is much faster than JSON |
| **Strong typing** | Field changes caught at compile time, not discovered at runtime in production |
| **High throughput** | Efficient for service-to-service communication at scale |
| **Multi-language codegen** | One schema, clients in every language your org uses |

**Exam Tip:** **gRPC for external/public APIs** — browsers do not natively support gRPC; you need gRPC-Web or a REST gateway.

> **gRPC for Machine Learning Serving** = gRPC = high-performance, contract-first RPC using Protocol Buffers (binary, not JSON).

---

## Synchronous vs Asynchronous API Calls for ML Serving — Wait Here vs Ticket Number

**The Story:** **Sync**: client blocks until prediction arrives — for fast inference (<300 ms), real-time UX. **Async**: submit job, poll later — for heavy inference, peak smoothing, offline scoring. Pick based on who can wait.

**Key mechanics:**
- Sync = client blocks until prediction arrives; async = client submits job and moves on.
- Sync for: fast inference (< 300 ms), real-time UX, immediate business decisions.
- Async for: heavy/slow inference, peak smoothing, offline/near-real-time use cases.
- Batch → async queues; online → sync REST/gRPC; streaming → event-driven pipelines.
- Same model can be served both ways depending on consumption pattern.

| Use Case | Why Sync |
|----------|----------|
| UI fetching real-time recommendations | User is staring at the screen waiting |
| Mobile app getting sentiment score | Screen update depends on the result |
| Payment backend checking fraud before approving | Transaction cannot proceed without the score |

**Exam Tip:** **Sync for long-running inference** — blocking a client for minutes ties up connections and violates UX; use async.

> **Synchronous vs Asynchronous API Calls for ML Serving** = Sync = client blocks until prediction arrives; async = client submits job and moves on.

---

## Single-Instance Deployment of Model Services — One Store, One Door

**The Story:** Simplest deployment: one VM/container on one port. Build-Package-Run: CI tests → **Docker image** (tagged) → run with config. The image bundles code + model + deps into a portable, reproducible unit.

**Key mechanics:**
- Simplest deployment: one VM or container running the model API on a single port.
- Build-Package-Run pipeline: CI tests → Docker image (tagged) → run container with config.
- Docker image = portable, reproducible deployment unit (code + model + dependencies).
- Configuration via environment variables, config files, and secrets managers.
- Production rollouts need controlled strategies — not "deploy and hope."

| Step | What Happens | Tools |
|------|--------------|-------|
| **Build** | Commit code → CI runs tests, linters, health checks | GitHub Actions, GitLab CI, Jenkins |
| **Package** | Build Docker image containing code, model artefact, and dependencies; tag with version (e.g., `ml-serving-api:v1.0.0`) | Docker, BuildKit |
| **Run** | Run image as container on VM, Kubernetes, or container platform; pass env vars, configure ports, set secrets | Docker run, kubectl, ECS, Cloud Run |

**Exam Tip:** **Skipping CI before packaging** — deploying untested images to production is the most common deployment failure mode.

> **Single-Instance Deployment of Model Services** = Simplest deployment: one VM or container running the model API on a single port.

---

## Blue-Green and Canary Deployment for Model Services — Soft Opening vs Grand Switch

**The Story:** **Blue-green**: two environments; switch all traffic at once; instant rollback. **Canary**: route small % to new version; ramp gradually. Canary = safety question; **A/B test** = business impact question — do not conflate them.

**Key mechanics:**
- Blue-green: two environments side by side; switch all traffic at once; instant rollback.
- Canary: route small % to new version; ramp gradually; stop or rollback on problems.
- Canary = safety/reliability question; A/B test = business impact question.
- Watch error rates, P95/P99 latency, and model-specific quality metrics during canary.
- Blue-green costs 2x temporarily; canary costs minimal extra infrastructure.

| Advantage | Detail |
|-----------|--------|
| **Fast, simple rollback** | Switch traffic back to blue in seconds |
| **Parallel testing** | New version runs on real infrastructure before full exposure |
| **Clear separation** | Old and new environments are completely isolated |

**Exam Tip:** **Confusing canary with A/B test** — canary asks "is it safe?"; A/B asks "is it better?"

> **Blue-Green and Canary Deployment for Model Services** = Blue-green: two environments side by side; switch all traffic at once; instant rollback.

---

## Autoscaling for Model Services — Staffing by Queue Length

**The Story:** **Autoscaling** adjusts replicas from CPU, **RPS**, queue length, **P95/P99 latency**, GPU utilisation. ML-specific: model load time (**cold starts**), GPU vs CPU profiles, batch vs online preferences. Set min/max bounds and cooldowns.

**Key mechanics:**
- Autoscaling adjusts instance count based on load signals to balance SLOs and cost.
- Signals: CPU, RPS, queue length, P95/P99 latency, GPU utilisation, memory.
- ML-specific: model load time (cold starts), GPU vs CPU profiles, batch vs online preferences.
- Set min replicas (warm instances), max replicas (cost cap), combined signals.
- Full lifecycle: train → build image → staging → canary/blue-green → monitor → ramp/rollback.

| Signal | Scale Up When | Scale Down When |
|--------|---------------|-----------------|
| **CPU usage** | Average CPU stays too high across instances | CPU very low for extended period |
| **Request rate (RPS/QPS)** | Requests per second exceed per-instance capacity | Sustained low request rate |
| **Queue length** | Async job queue grows — system falling behind | Queue consistently empty |
| **Latency (P95/P99)** | Latency rises above target SLO | Latency well below target with excess capacity |

**Exam Tip:** **Scaling on CPU alone for GPU models** — GPU utilisation is the relevant signal, not CPU.

> **Autoscaling for Model Services** = Autoscaling adjusts instance count based on load signals to balance SLOs and cost.

---

## Building a FastAPI Model Service — The Fast Counter

**The Story:** **FastAPI** + **Pydantic** = schema-enforced ML API with auto-docs. Model loaded **once at startup** via `joblib.load()`. Three endpoints: health (`GET /`), predict (`POST /predict`), model info (`GET /model-info`).

**Key mechanics:**
- FastAPI app with Pydantic models = schema-enforced ML API with auto-generated docs.
- Model loaded **once at startup** via `joblib.load()`; reused across all requests.
- Three endpoints: health check (`GET /`), predict (`POST /predict`), model info (`GET /model-info`).
- Predict flow: receive → validate (Pydantic) → transform (NumPy) → infer → respond (JSON).
- Run with `uvicorn app:app`; test with Bruno, curl, or `/docs` UI.

| Why | Detail |
|-----|--------|
| **Performance** | Loading a large model takes seconds to minutes; doing it per request destroys latency |
| **Efficiency** | One loaded instance is reused across all incoming requests |
| **Robustness** | Graceful handling if model file is missing (service starts but predict returns error) |

**Exam Tip:** **Loading model inside predict handler** — the #1 serving anti-pattern; always load at startup.

> **Building a FastAPI Model Service** = FastAPI app with Pydantic models = schema-enforced ML API with auto-generated docs.

---

## Containerizing the ML Service with Docker — Shipping Crate Standard

**The Story:** **Docker image** bundles code, model, deps. Dockerfile: slim base → cached `pip install` → copy app + model → expose port → `CMD uvicorn`. Layer caching: requirements before application code.

**Key mechanics:**
- Docker image = portable unit bundling code, model, and dependencies.
- Dockerfile: slim base → install deps (cached layer) → copy app + model → expose port → CMD uvicorn.
- Layer caching: copy `requirements.txt` and `pip install` before application code.
- Build: `docker build -t name:version .` from the correct directory.
- Run: `docker run -d -p host:container --name name image:tag`.

| Instruction | Purpose |
|-------------|---------|
| `FROM python:3.11-slim` | Base image — slim variant keeps size small and attack surface low |
| `WORKDIR /app` | Set working directory inside container |
| `COPY requirements.txt` + `RUN pip install` | Install dependencies **first** (layer caching) |
| `COPY model.pkl app.py` | Copy application code and model artefact |

**Exam Tip:** **Wrong build context** — running `docker build` from the wrong directory causes "file not found" errors; always `cd` to the directory containing the Dockerfile.

> **Containerizing the ML Service with Docker** = Docker image = portable unit bundling code, model, and dependencies.

---

## Testing the Containerized Model Service Locally — Dry Run Before Launch

**The Story:** Test at `localhost:8000`: health, model info, predict, negative (404). Vary predict inputs to confirm live inference, not static responses. Local container test catches packaging bugs before production.

**Key mechanics:**
- Test containerised service at `localhost:8000` (mapped from container port 80).
- Test matrix: health (`GET /`), model info, predict (`POST /predict`), negative (404).
- Change predict inputs to verify model inference is live, not static.
- Invalid inputs should return 422 (Pydantic validation).
- Stop container after testing; verify endpoints are dead.

| Endpoint | Method | Request Body | Expected Result |
|----------|--------|--------------|-----------------|
| `/` | GET | — | `200 OK` — `{"message": "API is running"}` |
| `/model-info` | GET | — | `200 OK` — model metadata JSON |
| `/predict` | POST | `{"feature_1": 1.5, "feature_2": 2.3}` | `200 OK` — `{"prediction": <float>}` |
| `/nonexistent` | GET | — | `404 Not Found` |

**Exam Tip:** **Testing against local uvicorn instead of container** — always stop the dev server before testing the containerised version.

> **Testing the Containerized Model Service Locally** = Test containerised service at localhost:8000 (mapped from container port 80).

---

# PART 4: THE ASSEMBLY LINE (Week 4)
*CI/CD, Pipelines, and Reproducible Production*

---

## Manual Workflow Pain, Pipeline Definition, and Benefits — Tribal Knowledge on Post-Its

**The Story:** Manual notebook workflows hide steps in one person's head: train → save → copy → hand-edit config. Untraceable, fragile at team scale. **Pipelines** encode steps so anyone can reproduce production behaviour and pass audits.

**Key mechanics:**
- Manual notebook workflows hide steps in one person's head and break under team scale.
- Typical manual flow: train → save → copy → hand-edit config — fragile and untraceable.
- Lack of tracking means you cannot explain production behaviour changes or pass audits.
- A deployment pipeline automates data prep → train → evaluate → package → deploy with defined artefact I/O.
- Pipelines deliver repeatability, auditability, speed, and fewer human errors.

| Problem | Consequence |
|---------|-------------|
| Steps forgotten or done out of order | Wrong model or stale config in production |
| Model saved but config not updated | Serving code loads old weights |
| No central record of runs | Cannot identify which model is live |
| Metrics in screenshots or local logs | Cannot explain performance changes |

**Exam Tip:** "Manual deployment is fine for small teams." — It breaks as soon as multiple people and multiple models are involved.

> **Manual Workflow Pain, Pipeline Definition, and Benefits** = Manual notebook workflows hide steps in one person's head and break under team scale.

---

## Classic CI/CD in Software Engineering — Quality Gate at Every Station

**The Story:** **CI**: frequent commits + automated build/test. **CD**: promote tested artefacts in small, low-risk releases. Classic flow: checkout → build → test → package → deploy — the assembly line's quality gates.

**Key mechanics:**
- **CI**: frequent commits + automated build/test on every change; catch problems early.
- **CD**: promote tested artefacts to staging/production in small, low-risk releases.
- Classic pipeline: checkout → build → test → package → deploy.
- Traditional CI/CD produces one main artefact (binary/container) from code.
- System behaviour in classic software is determined by code version.

| Term | Emphasis |
|------|----------|
| **Continuous Delivery** | Changes are always in a deployable state; release is a manual or gated decision |
| **Continuous Deployment** | Every passing change is automatically deployed to production |

**Exam Tip:** "CI and CD are the same thing." — CI integrates and tests; CD delivers/deploys. They are related but distinct.

> **Classic CI/CD in Software Engineering** = CI: frequent commits + automated build/test on every change; catch problems early.

---

## ML-Specific Differences from Classic CI/CD — Recipe Changes the Product

**The Story:** ML behaviour depends on **code**, **data/labels**, and **model parameters** — not code alone. Data must be **versioned**, schema-checked, drift-monitored. Models are **artefacts**: weights, metrics, reports stored and versioned.

**Key mechanics:**
- ML behaviour depends on code, data/labels, and model parameters — not code alone.
- Data must be versioned, schema-checked, and drift-monitored as part of every release.
- Models are artefacts: weights, metrics, and reports must be stored and versioned.
- ML gate question: "Is this model good enough?" not just "Did tests pass?"
- ML-specific checks: schema, distribution, holdout validation vs baseline.


$P(X)$

| Artefact Type | Examples |
|---------------|----------|
| **Model files** | `.pkl`, `.pt`, `.onnx`, SavedModel |
| **Evaluation metrics** | AUC, accuracy, F1, business KPIs |
| **Analysis artefacts** | Fairness metrics, calibration plots, confusion matrices |

**Exam Tip:** "Green CI means safe to deploy the model." — Code tests passing does not mean the model beats baseline or passes fairness checks.

> **ML-Specific Differences from Classic CI/CD** = ML behaviour depends on code, data/labels, and model parameters — not code alone.

---

## The Hybrid Picture: Code CI/CD + ML Pipeline — Two Assembly Lines, One Factory

**The Story:** Production MLOps uses a **hybrid**: code **CI/CD** + ML **pipeline**. Code CI/CD builds and tests software; ML pipeline runs data quality → train → evaluate → register candidates — orchestrated together.

**Key mechanics:**
- Production MLOps uses a **hybrid**: code CI/CD + ML pipeline, orchestrated together.
- Code CI/CD: build, test, containerise software components.
- ML pipeline: data quality → train → evaluate → register candidate models.
- Deployment combines container/infrastructure from CI/CD with chosen model from registry.
- Code changes trigger CI; data/retrain triggers ML pipeline — different triggers, coordinated gates.

| Flow | Trigger | Primary Outputs | Validates |
|------|---------|-----------------|-----------|
| **Code CI/CD** | Git push, PR | Container, infra config | Code correctness, integration |
| **ML Pipeline** | Schedule, new data, manual trigger | Model version, metrics | Data quality, model performance |

**Exam Tip:** Running only code CI and assuming ML is covered — model quality and data drift require the ML pipeline.

> **The Hybrid Picture: Code CI/CD + ML Pipeline** = Production MLOps uses a hybrid: code CI/CD + ML pipeline, orchestrated together.

---

## ML Artefacts: What Pipelines Move and Track — The Factory Output Room

**The Story:** ML **artefacts** include code, configs, data snapshots, models, metrics, reports. Each stage consumes and produces artefacts — an artefact factory. Categories: code/config, data, models (`.pkl`, `.pt`, `.onnx`), metrics/reports.

**Key mechanics:**
- ML artefacts include code, configs, data snapshots, models, metrics, and reports — not just code.
- Each pipeline stage consumes artefacts and produces new artefacts (artefact factory pattern).
- Categories: code/config, data, models (`.pkl`, `.pt`, `.onnx`), metrics/reports.
- Tracking artefacts = knowing what, where, and how they relate — core of MLOps.
- Artefacts are versioned outside Git (registries, object storage); must link back to code commits.

| Item | Examples |
|------|----------|
| Training scripts | `train.py`, feature engineering modules |
| Serving code | FastAPI handlers, batch inference jobs |
| Config files | YAML/JSON hyperparameters, data paths, model output paths |

**Exam Tip:** Only versioning code, not model files — you cannot reproduce or roll back.

> **ML Artefacts: What Pipelines Move and Track** = ML artefacts include code, configs, data snapshots, models, metrics, and reports — not just code.

---

## Lineage and Traceability in ML Systems — The Batch Traceability Card

**The Story:** **Lineage** answers: which data/code/config produced which model, and what is in production? Graph: commit + config + data + run ID → metrics → model version → stage. Without lineage you guess; with it you inspect, compare, rollback.

**Key mechanics:**
- Lineage answers: which data/code/config produced which model, and what is in production.
- Model lineage as a graph: commit + config + data + run ID → metrics → model version → stage.
- Without lineage: guessing; with lineage: inspect, compare, rollback confidently.
- Tools: experiment tracker (MLflow), model registry, metadata store.
- Runs, parameters, metrics, and models must be recorded and linkable.

| Question | Why It Matters |
|----------|----------------|
| Which data + code produced this model? | Debugging, audit, reproducibility |
| Which model is in production right now? | Incident response, rollback |
| What changed between v3 and v4? | Root-cause analysis for behaviour shifts |
| Which experiments were considered? | Understanding decision history |

**Exam Tip:** Logging metrics but not linking them to model files — incomplete lineage.

> **Lineage and Traceability in ML Systems** = Lineage answers: which data/code/config produced which model, and what is in production.

---

## Reproducibility in Machine Learning Systems — Same Recipe, Same Batch

**The Story:** **Reproducibility**: same code + config + data snapshot → equivalent model (within tolerance). Critical for debugging, compliance, collaboration. Achieved via **pipeline** (encoded steps) + **tracking** (metadata per run).

**Key mechanics:**
- Reproducibility: same code + config + data snapshot → equivalent model (within tolerance).
- Critical for debugging, compliance, collaboration, and scientific validity.
- Achieved via pipeline (encoded steps) + tracking (recorded metadata per run).
- Capture: commit hash, data version, config, environment, outputs.
- Pipeline defines *what to do*; tracker records *what was done* — together enables replay.

| Use Case | Why Reproducibility Is Essential |
|----------|----------------------------------|
| **Debugging** | Replay exact training when production performance drops |
| **Compliance / audit** | Prove how a model was created in regulated industries |
| **Collaboration** | New teammate reruns your pipeline and extends your work confidently |
| **Scientific rigour** | Results should be repeatable, not one-off accidents |

**Exam Tip:** "Reproducibility = same notebook cell order" — notebooks are not reproducible deployment units.

> **Reproducibility in Machine Learning Systems** = Reproducibility: same code + config + data snapshot → equivalent model (within tolerance).

---

## CI/CD for Machine Learning — From Blueprint to Workflow

**The Story:** **CI/CD for ML** turns pipeline concepts into verification and promotion workflows. **CI** catches issues on every change; **CD** promotes validated artefacts safely — the operational backbone of MLOps.

**Key mechanics:**
- CI/CD for ML turns abstract pipeline concepts into concrete verification and promotion workflows.
- **CI**: automated checks on every change (push/PR) — catch issues early.
- **CD**: promote validated artefacts to staging/production safely.
- ML CI checks: code quality, ML unit tests, data schema, smoke training.
- ML CD promotes: specific model version + metrics + code/config — not just latest image.

| Layer | Examples |
|-------|----------|
| **Standard software** | Lint, format, unit tests, integration tests |
| **ML-specific code** | Feature function shape tests, model load/predict smoke tests |
| **Data assumptions** | Schema validation on sample data |
| **Pipeline health** | Smoke training run (tiny data, few epochs) |

**Exam Tip:** Equating CI with "running full training" — CI uses fast smoke runs; full training is CD/scheduled pipeline territory.

> **CI/CD for Machine Learning** = CI/CD for ML turns abstract pipeline concepts into concrete verification and promotion workflows.

---

## CI for Machine Learning — Testing the Ingredients Too

**The Story:** ML **CI** adds to standard software CI: feature shape tests, preprocessing tests, model load/predict on dummy data. **Data validation** in CI: schema, null rates, bounds — catch breaking data changes before training.

**Key mechanics:**
- ML CI starts with standard software CI: lint, unit tests, integration tests.
- ML-specific unit tests: feature shape, preprocessing, model load/predict on dummy data.
- Data validation in CI: schema, null rates, bounds on small sample — catch breaking data changes.
- Smoke training: tiny data, few epochs — verifies end-to-end pipeline health, not model quality.
- CI fails fast to block bad merges before expensive training or production deploy.

| Check | Purpose |
|-------|---------|
| **Linting / formatting** | Code style consistency (flake8, black, ruff) |
| **Unit tests** | Core logic correctness |
| **Integration tests** | Components work together (API starts, health check responds) |

**Exam Tip:** Running full training in CI — too slow; use smoke training instead.

> **CI for Machine Learning** = ML CI starts with standard software CI: lint, unit tests, integration tests.

---

## CD for Machine Learning — Promoting a Specific Batch

**The Story:** ML **CD** promotes a **specific model version + metrics + code + config** — not just latest image. Promotion rules: metric thresholds, beat baseline, fairness checks. **Model registry** tracks versions, metrics, lineage, stages.

**Key mechanics:**
- ML CD promotes a **specific model version + metrics + code + config** — not just latest image.
- Promotion rules: metric thresholds, beat baseline, fairness checks, integration tests.
- Model registry tracks versions, metrics, lineage, and stages (Staging → Production).
- Deployed unit = container (serving code) + model artefact + config.
- CD flow: pass rules → register staging → canary/integration → promote to production.


$\geq 0.85$

| Component | Why It Must Travel Together |
|-----------|------------------------------|
| **Model artefact** | Weights / serialised model file |
| **Metrics** | AUC, accuracy, business KPIs on validation data |
| **Code version** | Training and serving logic that produced the model |
| **Config** | Hyperparameters, thresholds, preprocessing settings |

**Exam Tip:** Promoting every model that finishes training — promotion rules exist for a reason.

> **CD for Machine Learning** = ML CD promotes a specific model version + metrics + code + config — not just latest image.

---

## Repository Structure for MLOps Pipelines — Organised Factory Floor

**The Story:** MLOps repo: `.github/`, `configs/`, `data/`, `models/`, `scripts/`, `src/`. `configs/` drives reproducibility; `scripts/` are entry points; `src/` holds reusable pipeline step logic.

**Key mechanics:**
- MLOps repo layout: `.github/`, `configs/`, `data/`, `models/`, `scripts/`, `src/`, `README.md`.
- `configs/` drives reproducibility — hyperparameters and paths externalised from code.
- `scripts/` = entry points; `src/` = reusable ML logic (pipeline step implementations).
- `data/` holds samples locally; production data lives in warehouse/lake.
- `models/` is local artefact placeholder; production uses registry + object storage.

| Directory | Responsibility |
|-----------|----------------|
| **`.github/`** | CI/CD workflow definitions (GitHub Actions `ci.yml`) |
| **`configs/`** | YAML configs: hyperparameters, data paths, model output paths |
| **`data/`** | Small sample data for local dev and CI (not full production datasets) |
| **`models/`** | Local artefact output (e.g., `model.pkl`); placeholder for registry in production |

**Exam Tip:** Hardcoding `data/training_data.csv` in Python instead of config — breaks reproducibility and environment portability.

> **Repository Structure for MLOps Pipelines** = MLOps repo layout: .github/, configs/, data/, models/, scripts/, src/, README.md.

---

## MLflow Experiment Tracking — The Experiment Logbook

**The Story:** **MLflow** pattern: `start_run` → `log_params` → train → `log_metrics` → `log_model`. Each run gets a unique ID; parameters are searchable for experiment comparison.

**Key mechanics:**
- MLflow pattern: `start_run` → `log_params` → train → `log_metrics` → `log_model`.
- `start_run()` groups all logged data under a unique run ID.
- Parameters from config are searchable for experiment comparison.
- `log_model` creates the core lineage link: run → model artefact.
- Run training via `python scripts/train.py --config configs/train_config.yaml`.

| Step | API | What Gets Captured |
|------|-----|-------------------|
| 1. Start run | `mlflow.start_run()` | Unique run ID; groups all logged data |
| 2. Log parameters | `mlflow.log_params()` | Hyperparameters from config (learning rate, epochs, paths) |
| 3. Log metrics | `mlflow.log_metrics()` | AUC, RMSE, accuracy, etc. (possibly per epoch) |
| 4. Log model | `mlflow.sklearn.log_model()` (framework-specific) | Serialised model linked to this run |

**Exam Tip:** Logging metrics outside `start_run()` context — data not associated with any run.

> **MLflow Experiment Tracking** = MLflow pattern: start_run → log_params → train → log_metrics → log_model.

---

## CI Workflow for ML Repositories — Automated Shift Supervisor

**The Story:** CI YAML in `.github/workflows/` runs on push/PR: checkout → Python → deps → lint → test → smoke training. Fresh Ubuntu runner; `requirements.txt` ensures parity with local dev.

**Key mechanics:**
- CI YAML in `.github/workflows/` defines automated jobs on push/PR to main.
- Job steps: checkout → setup Python → install deps → lint → test → smoke training.
- Fresh Ubuntu runner; `requirements.txt` ensures environment parity with local dev.
- Any failing step blocks merge — CI is the automated gatekeeper.
- ML-specific addition: smoke training run catches integration errors early.

| Event | When It Fires |
|-------|---------------|
| **Push to main** | Direct commits to protected branch |
| **Pull request to main** | Every PR targeting main — primary gate for code review |

**Exam Tip:** CI workflow only on push, not PR — PRs merge without checks.

> **CI Workflow for ML Repositories** = CI YAML in .github/workflows/ defines automated jobs on push/PR to main.

---

# PART 5: SHELF HEALTH MONITORING (Week 5)
*Watching for Spoilage and Drift*

---

## Why Monitoring ML Models Is Different — Green Light, Rotten Stock

**The Story:** Traditional monitoring asks: is the store open? ML monitoring asks: is the product still good? **Service up** does not mean **model good** — **silent degradation** is the defining ML risk. Monitor data quality, **drift**, and predictions — not just HTTP 200.

**Key mechanics:**
- ML services need traditional monitoring **and** data/prediction monitoring.
- "Service is up" does not mean "model is good" — silent degradation is the defining ML risk.
- Data layer: quality (missing, schema, range) + drift (distribution shift, new segments).
- Prediction layer: ML metrics over time, business KPIs, fairness across segments.
- Unmonitored models cause silent degradation, scaled wrong decisions, unfair outcomes, and stakeholder distrust.


$R^2$

| Category | Typical Metrics | Alert Trigger Examples |
|----------|-----------------|------------------------|
| Infrastructure | CPU, memory, disk, network | CPU > 85% for 10 min |
| Service health | HTTP 4xx/5xx rates, timeouts | Error rate > 1% |
| Performance | Latency (avg, P95, P99) | P99 > 500 ms |
| Traffic | Requests per second, per endpoint | Traffic drop > 50% |

**Exam Tip:** **"Green dashboards = healthy model"** — The most dangerous ML failure mode produces no HTTP errors.

> **Why Monitoring ML Models Is Different** = ML services need traditional monitoring and data/prediction monitoring.

---

## What to Monitor: The Three-Layer Framework — Three Inspection Layers

**The Story:** Layer 1 (**system**): **P95/P99 latency**, errors, traffic, CPU/memory. Layer 2 (**data**): schema, quality, cardinality, **drift** (PSI), volume. Layer 3 (**prediction/business**): task metrics on delayed labels, calibration, thresholds.

**Key mechanics:**
- ML monitoring uses three layers: system health, data health, prediction/business health.
- Layer 1 (system): latency P95/P99, errors, traffic, CPU/memory — same as any API.
- Layer 2 (data): schema, quality, cardinality, drift (mean/std, PSI), volume anomalies.
- Layer 3 (predictions): ML metrics on delayed labels, calibration, segments, business KPIs, fairness.
- Monitoring only one layer leaves critical blind spots.


$R^2$

| Metric | Why It Matters | Example Threshold |
|--------|----------------|-------------------|
| Latency (P95, P99) | Average hides tail latency; P99 reveals worst user experience | P95 < 100 ms |
| Error rates (4xx, 5xx) | Client bugs vs. server failures | 5xx < 0.5% |
| Connection timeouts | Network or overload issues | < 0.1% of requests |
| Traffic (RPS per endpoint) | Load spikes, upstream outages | Alert on >50% drop |

**Exam Tip:** **Single-layer monitoring** — Each layer catches different failure modes; all three are required.

> **What to Monitor: The Three-Layer Framework** = ML monitoring uses three layers: system health, data health, prediction/business health.

---

## System, Data, and Feature Metrics in Depth — Shelf Scanner Details

**The Story:** System: **P95/P99**, 4xx/5xx, RPS, restarts. Data: schema, missing rates, min/max, cardinality, **drift**, volume. Prediction: ML metrics by time window, segment, model version — all require structured per-prediction logging.

**Key mechanics:**
- System metrics: P95/P99 latency, 4xx/5xx errors, RPS, CPU/memory, restarts.
- Data metrics: schema, missing rates, min/max, cardinality, drift (mean/std, PSI), volume.
- Prediction metrics: task-appropriate ML metrics on delayed labels, calibration, thresholds.
- Always compute segment-level breakdowns — global averages hide local failures.
- Business KPIs and fairness gaps connect model behaviour to real impact.

| Code Class | Meaning | Action |
|------------|---------|--------|
| 4xx | Bad client requests (malformed features, auth) | Fix client or API contract |
| 5xx | Server failures (model crash, OOM) | Page on-call immediately |
| Timeouts | Overload or dependency failure | Scale or optimise |

**Exam Tip:** **Mean latency as sole SLA** — Always pair with P95/P99 for user-experience accuracy.

> **System, Data, and Feature Metrics in Depth** = System metrics: P95/P99 latency, 4xx/5xx errors, RPS, CPU/memory, restarts.

---

## Model Performance Metrics and Production Logging — Receipt for Every Sale

**The Story:** Structured per-prediction logs: metadata, privacy-safe inputs, outputs, latency; backfill ground truth when available. Compute metrics by time window, segment, and **model version** — receipts enable accounting.

**Key mechanics:**
- All monitoring metrics depend on structured per-prediction logging.
- Log: metadata, inputs (privacy-safe), outputs, latency; backfill ground truth when available.
- Compute metrics by time window, segment, and model version.
- Task-appropriate ML metrics: AUC/F1 (classification), RMSE (regression), NDCG (ranking).
- Monitor calibration and decision thresholds, not just ranking metrics.


$R^2$

| Category | Fields | Purpose |
|----------|--------|---------|
| Request metadata | Timestamp, model version, endpoint, request ID | Traceability, version comparison |
| Input | Feature values (privacy-safe), segment tags (country, product) | Drift detection, segment analysis |
| Output | Raw score, final decision after thresholds/rules | Performance and calibration tracking |
| Ground truth | Actual outcome (when available) | Delayed metric computation |

**Exam Tip:** **Print statements instead of structured logs** — Unsearchable, no severity levels, cannot be ingested by ELK/Prometheus.

> **Model Performance Metrics and Production Logging** = All monitoring metrics depend on structured per-prediction logging.

---

## Types of Drift in Production ML Systems — Ingredients Change Over Time

**The Story:** **Drift** = world changes, model does not. **Covariate drift**: $P(X)$ shifts — detect via **PSI**, histograms. **Label drift**: $P(Y)$ shifts — affects precision/recall at fixed thresholds. **Concept drift**: $P(Y|X)$ shifts.

**Key mechanics:**
- Drift = world changes, model does not; primary cause of silent production degradation.
- **Covariate drift**: $P(X)$ shifts — detect via PSI, histograms, mean/std comparison.
- **Label drift**: $P(Y)$ shifts — affects precision/recall at fixed thresholds.
- **Concept drift**: $P(Y|X)$ shifts — shows as performance drop; needs ground truth to detect.
- Covariate drift is an early warning; concept drift is the most insidious.


$P(X)$
$P(Y)$
$P(Y|X)$

| Type | What Changes | Detection Signal | Typical Response |
|------|--------------|------------------|------------------|
| **Covariate drift** | Input feature distributions | PSI, KS test, mean/std shift | Investigate population or pipeline change |
| **Label drift** | Target variable distribution | Class ratio shift, base rate change | Recalibrate thresholds, update business rules |
| **Concept drift** | Feature–label relationship | Performance degradation despite stable inputs | Retrain on fresh data |

**Exam Tip:** **Treating all drift as covariate drift** — Label and concept drift require different responses.

> **Types of Drift in Production ML Systems** = Drift = world changes, model does not; primary cause of silent production degradation.

---

## Drift Detection Methods and Alert Design — The Spoilage Thermometer

**The Story:** Start with mean, std, min/max, missing rates, histograms. **PSI**: <0.1 stable, 0.1–0.2 minor, >0.2 major. **KS test** for continuous; **chi-square** for categorical — simple thermometers before fancy sensors.

**Key mechanics:**
- Start drift detection with mean, std, min/max, missing rates, and histograms.
- PSI: single stability score; <0.1 stable, 0.1–0.2 minor, >0.2 major shift.
- KS test for continuous features; chi-square for categorical features.
- Compare reference (training/stable) vs. recent production window.
- Alert on sustained, significant, multi-feature drift — not every tiny bump.


$\text{PSI} = \sum (A_i - E_i) \cdot \ln(A_i / E_i)$
$A_i$
$i$

| Statistic | What It Catches |
|-----------|-----------------|
| Mean | Central tendency shift |
| Standard deviation | Spread/volatility change |
| Min / max | Out-of-range values |
| Missing rate | Pipeline or source degradation |

**Exam Tip:** **PSI > 0.2 always means retrain** — Investigate first; may be fixable upstream or expected seasonality.

> **Drift Detection Methods and Alert Design** = Start drift detection with mean, std, min/max, missing rates, and histograms.

---

## Responding to Drift: Detection, Investigation, and Action — Investigate Before Reordering

**The Story:** Drift response: detect → investigate → decide (threshold tweak, data fix, or retrain). Drift is a signal, not an automatic retrain command. Three types: covariate $P(X)$, label $P(Y)$, concept $P(Y|X)$.

**Key mechanics:**
- Drift response: detect → investigate → decide (threshold, data fix, or retrain).
- Drift is a signal for investigation, not an automatic retrain command.
- Three drift types: covariate ($P(X)$), label ($P(Y)$), concept ($P(Y|X)$).
- Detection: basic stats, histograms, PSI, KS, chi-square vs. training reference.
- Alert on sustained, significant, grouped signals with clear ownership and runbooks.


$P(X)$
$P(Y)$
$P(Y|X)$

| Question | Distinguishes... |
|----------|------------------|
| Is this a real business change? | Market expansion vs. bug |
| Is this a data pipeline bug? | Fixable without retraining |
| Is this expected seasonality? | Holiday spike vs. true drift |
| Is this isolated to one segment? | Localised issue vs. global shift |

**Exam Tip:** **"Drift detected = retrain now"** — Always investigate root cause first.

> **Responding to Drift: Detection, Investigation, and Action** = Drift response: detect → investigate → decide (threshold, data fix, or retrain).

---

## From Metrics to Action: Designing an ML Monitoring Workflow — Three Eyes on the Floor

**The Story:** **Logs** (events), **metrics** (time-series), **traces** (request paths) — all needed. Start with objectives → 3–5 **SLOs** per model. One dashboard: system + data + prediction zones; scannable in 30 seconds.

**Key mechanics:**
- Observability pillars: logs (events), metrics (time-series), traces (request paths) — all needed for ML.
- Start with monitoring objectives → translate to 3–5 SLOs per model.
- One dashboard per model: system + data + prediction health; scannable in 30 seconds.
- Alerts are push monitoring tied to SLOs; dashboards are pull monitoring.
- Severity tiers: info (log), warning (Slack), critical (pager).

| Pillar | Best For | ML-Specific Signal |
|--------|----------|-------------------|
| Logs | Forensics, drift analysis, audit | Feature values, ground truth backfill |
| Metrics | Dashboards, alerting, trends | PSI, AUC, error rate, latency percentiles |
| Traces | Latency debugging across services | Feature store vs. inference bottleneck |

**Exam Tip:** **Metrics without objectives** — Collecting everything but alerting on nothing meaningful.

> **From Metrics to Action: Designing an ML Monitoring Workflow** = Observability pillars: logs (events), metrics (time-series), traces (request paths) — all needed for ML.

---

## Dashboards, Alerts, and the Typical ML Monitoring Stack — The Nightly Inspection Rounds

**The Story:** One dashboard per model with alert tiers tied to **SLOs**. Ownership split: data eng (pipelines), ML eng (drift/performance), platform (infra). Alerts for sustained breach, grouped incidents.

**Key mechanics:**
- One primary dashboard per model: system + data + prediction zones; 30-second scan.
- Alerts tied to SLOs: sustained breach, severity tiers, grouped incidents.
- Ownership: data eng (pipelines), ML eng (drift/performance), platform (infra).
- Runbooks: business meaning, causes, checks, next actions.
- Typical stack: Prometheus + Grafana + ELK + Alertmanager (+ OpenTelemetry).

| Rule | Rationale |
|------|-----------|
| Highlight exceptions (red/amber) | Operators spot problems without reading every number |
| Compare to baseline | Absolute values lack context; deltas reveal drift |
| Show segment breakdowns | Global metrics hide local failures |
| 30-second scan test | If triage takes longer, simplify the dashboard |

**Exam Tip:** **Wall-of-numbers dashboards** — No exception highlighting; fails the 30-second scan test.

> **Dashboards, Alerts, and the Typical ML Monitoring Stack** = One primary dashboard per model: system + data + prediction zones; 30-second scan.

---

## Four Production Failure Scenarios — Four Simulated Crises

**The Story:** Lab scenarios: (1) **silent degradation** — green infra, collapsing accuracy; (2) **covariate drift** — population shift; (3) feature pipeline break; (4) infra dependency failure. Rehearse before real incidents.

**Key mechanics:**
- Lab uses simulated scenarios for reproducibility; patterns scale to production.
- Scenario 1: silent degradation — green infra, collapsing accuracy.
- Scenario 2: covariate drift — population shift, feature means change dramatically.
- Scenario 3: feedback loop — model output biases future training data (catalogue coverage drops).
- Scenario 4: label drift — fraud rate 1% → 5%, precision tanks at fixed threshold.

| Part | Focus | Data Source |
|------|-------|-------------|
| Part 0 | Why traditional monitoring fails | Synthetic scenario tables |
| Part 1 | System metrics + data metrics from logs | Sample `logs.csv` + `training_stats.json` |
| Part 2 | PSI, model performance, automated alerting | Same logs + alert config YAML |
| Part 3 | Full inference instrumentation | Simulated ML inference requests |

**Exam Tip:** **"Lab uses synthetic data so patterns don't apply"** — Patterns scale directly; only the data source changes.

> **Four Production Failure Scenarios** = Lab uses simulated scenarios for reproducibility; patterns scale to production.

---

## Instrumenting Model Services: Metrics, PSI, and Automated Alerting — Prometheus on the Loading Dock

**The Story:** Production monitoring: structured logs + stored training baselines. System metrics (**P95/P99**, error rate) as machine-readable entries. Data metrics: compare production mean/std and category frequencies to training stats; automate **PSI** alerts.

**Key mechanics:**
- Production monitoring starts with structured logs + stored training baselines.
- System metrics: P95/P99 latency, error rate — log as machine-readable entries.
- Data metrics: compare production mean/std and category frequencies to training stats.
- PSI: <0.1 stable, 0.1–0.2 minor, >0.2 major; lab example PSI 3.19 = catastrophic.
- AlertManager: config-driven thresholds (YAML), evaluate → alert → export → route.


$\text{PSI} = \sum (A_i - E_i) \cdot \ln(A_i / E_i)$

| Column | Purpose |
|--------|---------|
| `timestamp` | Time-window filtering |
| `latency_ms` | System metric computation |
| `status_code` | Error rate calculation |
| Input features | Drift detection |

**Exam Tip:** **Perfect AUC with high PSI and error rate** — Classic exam trap; check evaluation integrity and sample size.

> **Instrumenting Model Services: Metrics, PSI, and Automated Alerting** = Production monitoring starts with structured logs + stored training baselines.

---

# PART 6: THE REORDER SYSTEM (Week 6)
*Retraining, Promotion, and Governance*

---

## Static Models and the Retraining Loop — Frozen Menu, Changing Tastes

**The Story:** **Static models** degrade silently as the world changes. The loop: deploy → monitor → detect → investigate → retrain → evaluate → redeploy. **Meaningful change** requires persistence and investigation — not every alert triggers retraining.

**Key mechanics:**
- Static models degrade silently as the world changes; monitoring exposes this, retraining addresses it.
- The production lifecycle is a loop: deploy → monitor → detect → investigate → retrain → evaluate → redeploy.
- "Meaningful change" requires persistence and investigation — not every alert triggers retraining.
- Cheaper fixes (thresholds, rules, pipeline repairs) should be ruled out first.
- Real failures include data drift, adversarial adaptation, and structural product misalignment.

| Phase | What Happens | Failure Mode if Skipped |
|-------|-------------|------------------------|
| Deploy | Model serves predictions | N/A — starting point |
| Monitor | Track drift, metrics, KPIs | Silent degradation |
| Detect | Alerts on meaningful change | Problems discovered by users |
| Retrain | New model on recent data | Model becomes structurally misaligned |

**Exam Tip:** **"The model still runs, so it's fine"** — uptime does not equal prediction quality.

> **Static Models and the Retraining Loop** = Static models degrade silently as the world changes; monitoring exposes this, retraining addresses it.

---

## Retraining Triggers: Drift, Performance, and Policy — Three Reorder Triggers

**The Story:** Retraining triggers: **data drift/quality**, **performance degradation**, **policy/product changes**. All require investigation first. Performance drop on fresh labels is strongest — after ruling out evaluation and business changes.

**Key mechanics:**
- Three major retraining triggers: data drift/quality, performance degradation, policy/product changes.
- All triggers require investigation before action — drift alerts are not automatic retrain commands.
- Performance degradation on fresh labels is the strongest signal, after ruling out evaluation and business changes.
- Policy retrains align with intent and compliance, not just metric optimisation.
- Cheaper alternatives (threshold tuning, pipeline fixes) should be considered first.


$P(X)$
$P(Y|X)$

| Signal | Example | First Response |
|--------|---------|----------------|
| High drift scores on key features | Income distribution shifted after economic event | Investigate: business change or pipeline bug? |
| New segments/categories never seen in training | New product tier, new country code | Check if model handles unknowns gracefully |
| Persistent data quality issues | Missing-value rate jumped from 2% to 18% | Fix pipeline before retraining |

**Exam Tip:** **"High PSI → retrain immediately"** — drift requires investigation; pipeline bugs mimic drift.

> **Retraining Triggers: Drift, Performance, and Policy** = Three major retraining triggers: data drift/quality, performance degradation, policy/product changes.

---

## Continuous Training: Scheduled vs Event-Driven Retraining — Scheduled vs Alarm-Driven Reorders

**The Story:** **Continuous training**: **scheduled** (simple, prevents staleness), **event-driven** (responds to acute signals), or **hybrid** (baseline schedule + event triggers) — production best practice.

**Key mechanics:**
- Continuous training keeps models fresh via scheduled, event-driven, or hybrid retraining patterns.
- Scheduled retraining is simple and prevents staleness; event-driven responds to acute signals.
- Hybrid (baseline schedule + event triggers) is the production best practice.
- Retraining has real costs: compute, engineering time, and risk of deploying a worse model.
- Event triggers should often include human approval for high-impact models.


$N$
$K$

| Pattern | Trigger | Best For | Risk |
|---------|---------|----------|------|
| **Scheduled** | Calendar (weekly, monthly, quarter) | Steady data flow, reliable labels, low volatility | Model may be stale between cycles |
| **Event-driven** | Drift alert, SLO breach, major product change | Dynamic environments, high-stakes models | Alert fatigue; false triggers |
| **Hybrid** | Schedule + events | Most production systems | Requires tuning both layers |

**Exam Tip:** **"Event-driven only" without baseline schedule** — models go stale during quiet periods with no alerts.

> **Continuous Training: Scheduled vs Event-Driven Retraining** = Continuous training keeps models fresh via scheduled, event-driven, or hybrid retraining patterns.

---

## Designing a Retraining and Promotion Pipeline — The Reorder Assembly Line

**The Story:** Pipeline: snapshot data → features → train candidates → evaluate → register → promote. Stage 1 treats training data as first-class **artefact** with time window, sources, hashes. Stage 2 trains multiple candidates with full logging.

**Key mechanics:**
- Retraining pipeline: snapshot data → build features → train candidates → evaluate → register → promote.
- Stage 1 treats training data as a first-class artefact with time window, sources, and hashes.
- Stage 2 trains multiple candidates with full logging of code, config, data, and metrics.
- Config-driven pipelines make retraining repeatable — change config, not code.
- MLflow (or similar) organises runs and links candidates to the same data snapshot.

| Stage | Purpose | Key Output |
|-------|---------|------------|
| 1. Data & Features | Reproducible training dataset | Snapshot + metadata (time window, sources, hashes) |
| 2. Train Candidates | Explore hyperparameters / architectures | Logged runs with code version, configs, metrics |
| 3. Evaluate & Select | Governance gate vs champion | Promotion decision with multi-metric evidence |
| 4. Register | First-class artefact with lineage | Versioned model entry in registry |

**Exam Tip:** **Hardcoding data paths in training scripts** — breaks reproducibility and auditability.

> **Designing a Retraining and Promotion Pipeline** = Retraining pipeline: snapshot data → build features → train candidates → evaluate → register → promote.

---

## Evaluating and Selecting the Right Model: Champion vs Challenger — Champion vs Challenger

**The Story:** Compare challengers to **champion** on held-out data, time slices, ML metrics, business KPIs, segment fairness. Predefined promotion rules: minimum delta, no KPI/fairness degradation. Failed candidates archived.

**Key mechanics:**
- Stage 3 compares challengers to champion on held-out data, multiple time slices, ML metrics, business KPIs, and segment fairness.
- Promotion rules are predefined: minimum metric delta, no KPI/fairness degradation.
- Failed candidates are logged and archived; only rule-passing models proceed.
- Model registry stores version, lineage (data, code, config), metrics, and environment tags.
- Champion/challenger pattern: production stage = champion; explicit version = challenger.


$\delta$
$\text{Expected Profit} = \sum_i \left( \text{payoff}(\hat{y}_i, y_i) \right)$
$+P$

| Metric Category | Examples | Why It Matters |
|----------------|----------|----------------|
| **Statistical ML metrics** | Accuracy, AUC, RMSE, F1 | Core predictive quality |
| **Business KPIs** | Expected profit, fraud loss, conversion rate | Ties model to dollars-and-cents impact |
| **Segment-level metrics** | Performance by demographic, region, product | Fairness and equity checks |
| **Multi-time-slice** | Metrics across rolling weekly windows | Detects instability over time |

**Exam Tip:** **Promoting on a single metric** — AUC improvement with profit degradation is a net loss.

> **Evaluating and Selecting the Right Model: Champion vs Challenger** = Stage 3 compares challengers to champion on held-out data, multiple time slices, ML metrics, business KPIs, and segment fairness.

---

## Promotion, Deployment, and the Continuous Retraining Loop — Staging Before Full Shelf

**The Story:** Promote through staging → **canary/shadow** → full production; keep old champion for rollback. **Shadow testing**: real inputs, zero user impact. **Continuous retraining** closes the loop: monitor → signal → pipeline → promote.

**Key mechanics:**
- Stage 5 promotes models through staging → canary/shadow → full production, keeping old champion for rollback.
- Shadow testing uses real inputs with zero user impact; canary exposes a subset of users.
- Continuous retraining is a closed loop: monitor → signal → pipeline → promote → monitor.
- Triggers may be automatic or human-approved; judgement matters for risk and fairness.
- Promotion-phase monitoring validates behaviour under real traffic, not just service health.

| Stage | Purpose | User Impact |
|-------|---------|-------------|
| **Staging** | Run smoke tests, replay recorded traffic | None — isolated environment |
| **Canary** | Route small % of live traffic to new model | Partial — subset of users see new model |
| **Shadow (dark launch)** | New model runs in parallel; only champion output served | None — predictions logged but not used |
| **Full production** | New model serves all traffic | All users |

**Exam Tip:** **Promoting directly from offline eval to 100% traffic** — skips real-world validation under live distributions.

> **Promotion, Deployment, and the Continuous Retraining Loop** = Stage 5 promotes models through staging → canary/shadow → full production, keeping old champion for rollback.

---

## Offline Evaluation and Backtesting — Tasting Before Shipping

**The Story:** **Offline evaluation**: train/val/test splits, time-based splits, cross-validation — fast, zero user risk. Necessary but not sufficient; assumes past resembles future. **Backtesting** simulates counterfactual business outcomes.

**Key mechanics:**
- Offline evaluation: train/val/test splits, time-based splits, cross-validation — fast, cheap, zero user risk.
- Offline eval is necessary but not sufficient; it assumes the past looks like the future.
- Backtesting replays historical data through candidate models to simulate counterfactual business outcomes.
- Backtest quality depends on logged features, labels, and awareness of behavioural feedback limitations.
- Use time-based splits for sequential production data; random splits leak future information.


$) | False Declines ($
$2.1M | $
$2.4M | $

| Advantage | Limitation |
|-----------|-----------|
| Fast and cheap | Assumes past resembles future |
| Try many candidates in parallel | Cannot capture user behaviour changes from new model |
| Zero risk to real users | Misses UX interactions and downstream side effects |
| Reproducible and auditable | Depends on quality of logged features and labels |

**Exam Tip:** **"Best offline AUC → deploy"** — offline metrics miss user behaviour feedback and business impact.

> **Offline Evaluation and Backtesting** = Offline evaluation: train/val/test splits, time-based splits, cross-validation — fast, cheap, zero user risk.

---

## Live Environment Validation: Shadow Testing and A/B Testing — Shadow Shelf, A/B Aisle

**The Story:** **Shadow testing**: both models see same input; only champion served; challenger logged. Zero user risk, extra compute. **A/B testing** splits traffic; measures real business outcomes — revenue, conversion, fraud caught.

**Key mechanics:**
- Shadow testing: both models see same input; only champion output served; challenger logged for analysis.
- Shadow uses real production inputs with zero user risk; costs extra compute and logging.
- A/B testing splits traffic; measures real business outcomes (revenue, conversion, fraud, churn).
- A/B requires sufficient traffic, duration, a primary metric, guardrails, and no overlapping experiments.
- Typical progression: offline → backtest → shadow → A/B → full rollout.

| Benefit | Tradeoff |
|---------|----------|
| Real production input distributions | Extra compute cost (2× inference) |
| Zero user risk | Increased log volume and storage |
| Detects train-serve skew | Privacy and data retention considerations |
| Validates model before any user sees it | Cannot measure user behavioural response |

**Exam Tip:** **Skipping shadow and going straight to A/B** — wastes traffic on models with obvious offline/shadow failures.

> **Live Environment Validation: Shadow Testing and A/B Testing** = Shadow testing: both models see same input; only champion output served; challenger logged for analysis.

---

## Choosing Evaluation Methods and Connecting Them to Promotion — Depth Matches Stakes

**The Story:** Match evaluation depth to impact: backtest (cheap) → shadow (live inputs) → A/B (real users). Common: backtest → shadow → A/B → rollout. Promotion synthesises offline, shadow, A/B, and fairness evidence.

**Key mechanics:**
- Match evaluation depth to model impact: backtest (cheap) → shadow (live inputs) → A/B (real users).
- Common pattern: backtest → shadow → A/B → full rollout; not all stages always required.
- Promotion decisions synthesise offline metrics, backtest, shadow, A/B, and risk/fairness evidence.
- High-impact models require combined evidence; low-impact models may need offline comparison only.
- Evaluation is layered — each stage filters candidates before the next, more expensive stage.


$\delta$

| Technique | Cost | Risk to Users | When to Use |
|-----------|------|--------------|-------------|
| **Backtest** | Cheap, fast | None | Early exploration; narrowing many candidates; low-risk internal models |
| **Shadow testing** | Medium (2× compute) | None | Medium-to-high impact; validate on live inputs before user exposure |
| **A/B test** | High (traffic, time) | Partial (test group) | High-impact decisions; need proof of business metric improvement |
| **Full rollout** | Deployment cost | All users | After combined evidence justifies promotion |

**Exam Tip:** **Using A/B tests for every tiny model tweak** — wasteful; reserve for high-impact changes.

> **Choosing Evaluation Methods and Connecting Them to Promotion** = Match evaluation depth to model impact: backtest (cheap) → shadow (live inputs) → A/B (real users).

---

## Governance and Safety: Why Approvals Matter — Signed Release Forms

**The Story:** **Governance**: accountability (owners, approvers), traceability (lineage, audit trail), controlled risk. Model promotion is a visible, reviewable change — PR, ticket, or formal approval.

**Key mechanics:**
- Governance provides accountability (owners, approvers), traceability (lineage, audit trail), and controlled risk.
- Model promotion must be a visible, reviewable change — PR, ticket, or formal approval workflow.
- Three pillars: who owns it, can we reconstruct what happened, do big changes get proper review.
- Organisational roles: data science (train/evaluate), ML engineering (deploy/rollback), business (metrics), compliance (fairness).
- Governance enables faster iteration by building trust in deployment safety.

| Pillar | Definition | Production Mechanism |
|--------|-----------|---------------------|
| **Accountability** | Known owner for each model; clear approvers for major changes | Model owner field in registry; PR-based promotion |
| **Traceability** | Reconstruct what happened and why | Lineage tracking; audit logs; registry history |
| **Controlled risk** | Big changes get proper review | Staging gates; approval workflows; fairness reviews |

**Exam Tip:** **"Governance slows us down"** — untested deployments cause incidents that slow teams far more than review gates.

> **Governance and Safety: Why Approvals Matter** = Governance provides accountability (owners, approvers), traceability (lineage, audit trail), and controlled risk.

---

## Traceability, Audit Trails, and Rollback Mechanisms — The Recall Button

**The Story:** **Audit trail**: version, owner, stage, lineage, deployment history, approvers. **Rollback**: keep previous version, pin stage in config, test rollback in playbook — recall a bad batch in under 60 seconds.

**Key mechanics:**
- Audit trail: registry entry with version, owner, stage, training lineage, deployment history, approvers.
- Lineage links model to data snapshot, code commit, and config — essential for root cause analysis.
- Rollback: keep previous version, pin version/stage in config, test rollback in deployment playbook.
- Registry-driven rollback: change stage, restart service — no code or image rebuild needed.
- Assume production failures will happen; optimise for recovery speed, not just prevention.


$\text{Model v7} = f(\text{Data Snapshot D3},\ \text{Code Commit abc123},\ \text{Config train\_v2.yaml})$

| Audit Field | Content | Used For |
|-------------|---------|----------|
| **Version & stage** | v7, Production | Identify current live model |
| **Owner** | Team / individual | Incident response contact |
| **Training lineage** | Data snapshot, code commit, config | Reproduce or explain model behaviour |
| **Evaluation summary** | Metrics at promotion time | Justify why this model was chosen |

**Exam Tip:** **Deleting old model versions** — eliminates rollback capability entirely.

> **Traceability, Audit Trails, and Rollback Mechanisms** = Audit trail: registry entry with version, owner, stage, training lineage, deployment history, approvers.

---

## Guardrails and the Governed Promotion Workflow — Safety Rails on the Shelf

**The Story:** **Guardrails**: output sanity checks, rate limiting, kill switches, policy constraints, input validation, fallbacks. Assume models will misbehave; contain damage externally. Full lifecycle: monitor → retrain → evaluate → approve → rollout → guardrails → rollback.

**Key mechanics:**
- Guardrails: output sanity checks, rate limiting, kill switches, policy constraints, input validation, fallbacks.
- Mindset: assume models will misbehave; contain damage with external safety rails.
- Full governed lifecycle: monitor → retrain → evaluate → approve → controlled rollout → guardrails → rollback → monitor.
- Kill switches enable instant model disable via config flag without code deployment.
- Policy constraints must be technically enforced, not just documented.


$[0,1]$
$[300, 850]$
$[0, 1]$

| Guardrail | Purpose | Example |
|-----------|---------|---------|
| **Output sanity checks** | Reject impossible predictions | Probabilities outside $[0,1]$; credit scores below 0 or above 1000 |
| **Rate limiting** | Prevent traffic spikes from overwhelming model or downstream systems | Max 1000 predictions/sec per client |
| **Kill switches / feature flags** | Instantly disable a risky model or feature | Flip config flag to route all traffic to fallback rule |
| **Policy constraints** | Technical enforcement of regulatory rules | Block use of protected attributes (age, race) in feature vector |

**Exam Tip:** **No output sanity checks** — garbage predictions reach users silently.

> **Guardrails and the Governed Promotion Workflow** = Guardrails: output sanity checks, rate limiting, kill switches, policy constraints, input validation, fallbacks.

---

## Config-Driven Retraining Pipeline: Training Script and MLflow Integration — Config-Driven Reorder Line

**The Story:** Retraining is **config-driven**: same `train.py`, different configs for data/hyperparameters. **MLflow** logs params, metrics, config artefact, model; `register_model` creates registry version.

**Key mechanics:**
- Retraining pipeline is config-driven: same `train.py`, different config files for data/hyperparameters.
- Config files record which data powered which run — essential for audit and reproducibility.
- MLflow logs params, metrics, config artefact, and model; `register_model` creates official registry version.
- Simulating scheduled retrain: run pipeline with v1 config (champion), then v2 config (challenger).
- MLflow UI shows runs, registered versions, and enables head-to-head comparison.

| Config Change | Effect |
|--------------|--------|
| Different `data.path` | Retrain on newer snapshot |
| Different hyperparameters | New candidate with same data |
| Different model type | Architecture experiment |

**Exam Tip:** **Hardcoding data paths in train.py** — breaks config-driven pattern and auditability.

> **Config-Driven Retraining Pipeline: Training Script and MLflow Integration** = Retraining pipeline is config-driven: same train.py, different config files for data/hyperparameters.

---

## Champion vs Challenger Evaluation and Automated Promotion — Challenger Must Beat Champion

**The Story:** Champion by Production stage; challenger by version. Both evaluated on same holdout with statistical (MSE) and business (profit) metrics. Promotion rule: challenger beats champion on both (optional tolerance $\delta$).

**Key mechanics:**
- Champion loaded by Production stage; challenger by explicit version number.
- Both evaluated on same unseen holdout data with statistical (MSE) and business (profit) metrics.
- Promotion rule: challenger must beat champion on both metric types (with optional tolerance $\delta$).
- Automated promotion: challenger → Production, old champion → Archived.
- Pattern is production-ready; labs simplify data size and skip shadow/A/B stages.


$\text{Profit} = \sum_i \text{payoff}(\hat{y}_i, y_i)$
$+P$
$-L$

| Role | How Loaded | Registry Stage |
|------|-----------|---------------|
| **Champion** | Lookup by `Production` stage tag | `Production` |
| **Challenger** | Explicit version number (e.g., v2) | `None` or `Staging` |

**Exam Tip:** **Evaluating on different datasets** — invalidates head-to-head comparison.

> **Champion vs Challenger Evaluation and Automated Promotion** = Champion loaded by Production stage; challenger by explicit version number.

---

## Registry-Driven Serving, Promotion Updates, and Rollback — Registry, Not Hardcoded Paths

**The Story:** Serving loads from **MLflow registry** by name + stage via env vars. Promote and rollback by changing registry stage, not code. Rollback: v1 → Production, v2 → Staging, restart — under 60 seconds.

**Key mechanics:**
- Serving service loads model from MLflow registry by name + stage (via environment variables).
- No hardcoded paths — promote and rollback by changing registry stage, not code.
- Rollback: v1 → Production, v2 → Staging, restart service — under 60 seconds.
- End-to-end loop: retrain → register → evaluate → promote → serve → monitor → rollback/retrain.
- Registry-driven deployment separates model lifecycle from application code lifecycle.

| Environment Variable | Default | Effect |
|---------------------|---------|--------|
| `MODEL_NAME` | `credit_risk_model` | Which registered model to load |
| `MODEL_STAGE` | `Production` | Which stage (Production, Staging) |
| `MLFLOW_TRACKING_URI` | local URI | Where to find registry |

**Exam Tip:** **Hardcoded model paths in serving code** — rollback requires code change and redeployment.

> **Registry-Driven Serving, Promotion Updates, and Rollback** = Serving service loads model from MLflow registry by name + stage (via environment variables).

---

# PART 7: PRODUCT PACKAGING (Week 7)
*Compression, Formats, and Optimised Runtimes*

---

## The Research–Production Deployment Gap — Lab Prototype vs Store Reality

**The Story:** Production demands **P95/P99 latency**, throughput, cost-per-prediction, diverse hardware. Research uses FP32, single GPU, loose tolerance. Three pain buckets: **portability**, **latency/throughput**, **footprint**.

**Key mechanics:**
- Production constraints: P95/P99 latency, throughput, cost-per-prediction, diverse hardware
- Research uses FP32, single GPU, loose latency tolerance
- Three pain buckets: **portability**, **latency/throughput**, **footprint**
- Accurate models often fail on size, speed, or deployability
- Standardisation + optimisation close the research–production gap

| Metric | Definition | Why it hurts |
|--------|------------|--------------|
| **Latency** | Time per prediction | Bad UX, downstream timeouts |
| **P95 / P99 latency** | Tail of latency distribution | Worst-case user experience |
| **Throughput** | Requests/sec per instance | Determines fleet size and cost |

**Exam Tip:** Focusing only on average latency — P95/P99 tail latency is what breaks SLAs and user trust.

> **The Research–Production Deployment Gap** = Production constraints: P95/P99 latency, throughput, cost-per-prediction, diverse hardware

---

## Production Optimisation Goals: Portability, Speed, and Footprint — Three Packaging Goals

**The Story:** **Portability**: train anywhere, deploy anywhere via standard formats. **Latency**: per-prediction time; tails matter for SLAs. **Throughput**: req/s per instance drives server count and cost.

**Key mechanics:**
- **Portability**: train in any framework, deploy on any hardware via standard formats
- **Latency**: per-prediction time; P95/P99 tails matter most for SLAs
- **Throughput**: req/s per instance; drives server count and cost
- **Footprint**: disk, memory/VRAM, and power — especially critical for edge
- Identical-accuracy models can differ 3–5× in inference cost

| Property | Benefit |
|----------|---------|
| Framework-agnostic graph | One export, many runtimes |
| Shared inspection tools | Graph analysis, validation |
| Reduced glue code | Fewer bespoke converters |

**Exam Tip:** Optimising latency without measuring P95/P99 — average latency can hide severe tail problems.

> **Production Optimisation Goals: Portability, Speed, and Footprint** = Portability: train in any framework, deploy on any hardware via standard formats

---

## Three Levers for Production Model Optimisation — Three Compression Levers

**The Story:** Three levers: **standard formats**, **compression**, **optimised runtimes**. Formats → portability; compression → size/speed; runtimes → hardware-efficient execution. **ONNX** = cross-platform default.

**Key mechanics:**
- Three levers: **standard formats**, **compression**, **optimised runtimes**
- Formats → portability; compression → size/speed; runtimes → hardware-efficient execution
- ONNX = cross-platform default; TF Lite = mobile; OpenVINO = Intel-first
- Quantisation, pruning, distillation shrink models with accuracy trade-offs
- ONNX Runtime, TensorRT, XLA optimise graph execution on target hardware

| Format | Ecosystem | Best for |
|--------|-----------|----------|
| **ONNX** | Cross-framework | Cloud servers, general CPU/GPU |
| **TF Lite** | TensorFlow | Mobile, Android, iOS, IoT |
| **OpenVINO** | Intel | Intel CPUs, integrated GPUs, accelerators |

**Exam Tip:** Using only one lever — format export without runtime tuning or compression often yields minimal gains.

> **Three Levers for Production Model Optimisation** = Three levers: standard formats, compression, optimised runtimes

---

## Standard Model Formats: Foundations and ONNX — Universal Shipping Container

**The Story:** Model format = graph + parameters + metadata. Framework-native formats create portability pain. **ONNX** is the open, cross-framework, cross-runtime standard — one container fits any truck.

**Key mechanics:**
- Model format = graph + parameters + metadata (blueprint + numbers)
- Framework-native formats create portability pain across teams and hardware
- ONNX is the open, cross-framework, cross-runtime standard
- Export enables interoperability; compression and runtime tuning deliver speed/size gains
- ONNX is the practical default for cloud/server, multi-framework organisations

| Framework | Native artefact | Native runtime |
|-----------|----------------|----------------|
| PyTorch | `.pt` / `.pth` checkpoint | PyTorch |
| TensorFlow | SavedModel, `.h5` (Keras) | TensorFlow |
| JAX | Checkpoints + Python | JAX / XLA |

**Exam Tip:** Confusing model format with runtime — ONNX is the *representation*; ONNX Runtime is the *engine* that executes it.

> **Standard Model Formats: Foundations and ONNX** = Model format = graph + parameters + metadata (blueprint + numbers)

---

## TensorFlow Lite: Mobile and Edge Deployment — Pocket-Sized Product Line

**The Story:** **TF Lite** = format + runtime for **mobile/embedded**. Small binary, mobile CPU/NPU kernels, **INT8** inference — natural for TensorFlow-trained models on Android/iOS/IoT.

**Key mechanics:**
- TF Lite = format + runtime for **mobile and embedded** deployment
- Optimised for small binary, mobile CPU/NPU kernels, INT8 inference
- Natural choice when training in TensorFlow and deploying to Android/iOS/IoT
- INT8 quantisation is a first-class workflow, often yielding ~4× size reduction
- Not a replacement for ONNX in cloud/server multi-framework environments

| Goal | How TF Lite achieves it |
|------|--------------------------|
| Small runtime binary | Minimal interpreter, no full TensorFlow stack |
| Fast on mobile hardware | Optimised kernels for ARM CPUs and NPUs |
| Low memory | INT8 quantisation support, flatbuffer format |
| On-device inference | Android, iOS, Raspberry Pi, microcontrollers |

**Exam Tip:** Using TF Lite for cloud server deployment — it is mobile-first; ONNX Runtime or TensorRT are better server choices.

> **TensorFlow Lite: Mobile and Edge Deployment** = TF Lite = format + runtime for mobile and embedded deployment

---

## OpenVINO and the Standard Format Pipeline — Intel-Optimised Warehouse

**The Story:** **OpenVINO** optimises for **Intel CPUs, iGPUs, accelerators**. Flow: ONNX/TF → Model Optimizer → IR → OpenVINO Runtime — best when infra is Intel-heavy with limited GPU budget.

**Key mechanics:**
- OpenVINO optimises for **Intel CPUs, iGPUs, and accelerators**
- Flow: ONNX/TF → Model Optimizer → IR → OpenVINO Runtime
- Best when infra is Intel-heavy and GPU budget is limited
- Standard format = contract between training and serving teams
- ONNX = general cross-platform; TF Lite = mobile; OpenVINO = Intel-first

| Scenario | Why OpenVINO |
|----------|--------------|
| Intel-only data centre | Deep CPU kernel optimisation (AVX-512, AMX) |
| No NVIDIA GPU budget | Strong CPU inference without GPU capex |
| Edge with Intel hardware | Intel NUC, industrial PCs |
| Mixed ONNX source models | Single Intel runtime for all exports |

**Exam Tip:** Choosing OpenVINO for NVIDIA GPU servers — TensorRT is the NVIDIA-specific optimiser; OpenVINO targets Intel.

> **OpenVINO and the Standard Format Pipeline** = OpenVINO optimises for Intel CPUs, iGPUs, and accelerators

---

## Why Model Compression Matters in Production — Shrink-Wrap for Speed

**The Story:** **Compression** makes accurate models practical: faster inference, higher throughput, smaller footprint, edge feasibility. Three techniques: **quantisation**, **pruning**, **knowledge distillation**.

**Key mechanics:**
- Compression makes accurate models **practical** for production constraints
- Benefits: faster inference, higher throughput, smaller disk/memory, edge feasibility
- Three techniques: **quantisation**, **pruning**, **knowledge distillation**
- Compression stacks with standard formats and optimised runtimes
- Always measure size, latency, and accuracy before and after

| Benefit | Mechanism | Downstream effect |
|---------|-----------|-------------------|
| **Faster inference** | Fewer bits, fewer ops, smaller graphs | Lower latency |
| **Higher throughput** | Less memory bandwidth, faster arithmetic | More req/s per instance |
| **Smaller disk footprint** | INT8 weights, pruned parameters | Faster downloads, smaller apps |
| **Lower memory use** | Smaller tensors in RAM/VRAM | Larger batch sizes, more concurrency |

**Exam Tip:** Compressing before establishing baseline metrics — without before/after size, latency, and accuracy numbers, trade-offs cannot be evaluated.

> **Why Model Compression Matters in Production** = Compression makes accurate models practical for production constraints

---

## Quantisation and Pruning — Lighter Ingredients

**The Story:** **Quantisation**: FP32 → FP16/INT8; ~4× size reduction at INT8. **PTQ**: quantise after training; easy but may lose accuracy. **QAT**: simulate during training; better INT8 accuracy. **Pruning**: remove weights/neurons.

**Key mechanics:**
- Quantisation: FP32 → FP16/INT8; ~4× size reduction at INT8; faster memory-bound inference
- **PTQ**: quantise after training; easy but may lose accuracy at INT8
- **QAT**: simulate quantisation during training; better INT8 accuracy
- **Unstructured pruning**: zero individual weights; needs sparse kernels for speed
- **Structured pruning**: remove channels; smaller dense net; standard HW friendly

| Precision | Bits | Size vs FP32 | Typical use |
|-----------|------|--------------|-------------|
| FP32 | 32 | 1× (baseline) | Training, high-accuracy serving |
| FP16 | 16 | ~2× smaller | GPU inference (TensorRT, mixed precision) |
| INT8 | 8 | ~4× smaller | CPU/mobile inference, edge |

**Exam Tip:** Assuming PTQ always preserves accuracy — INT8 PTQ on small calibration sets can fail on out-of-distribution inputs.

> **Quantisation and Pruning** = Quantisation: FP32 → FP16/INT8; ~4× size reduction at INT8; faster memory-bound inference

---

## Knowledge Distillation — Apprentice Learns From Master

**The Story:** **Distillation**: small **student** mimics large **teacher**. Soft labels carry **dark knowledge** beyond hard targets. Students can be smaller, faster, *and* more accurate than same-size models on hard labels alone.

**Key mechanics:**
- Distillation: train a **small student** to mimic a **large teacher**
- Soft labels carry inter-class similarity (dark knowledge) beyond hard one-hot targets
- Students can be smaller, faster, **and** more accurate than same-size models trained on hard labels alone
- Loss combines soft-target (teacher distribution) and hard-target (ground truth) terms
- Popular for edge/mobile: design student architecture for hardware constraints


$x$
$\mathcal{L} = \alpha \cdot \mathcal{L}_{\text{soft}}(T(\mathbf{z}_s), T(\mathbf{z}_t)) + (1 - \alpha) \cdot \mathcal{L}_{\text{hard}}(y, \mathbf{z}_s)$
$T(\cdot)$

| Role | Model | Characteristics |
|------|-------|---------------|
| **Teacher** | Large, accurate, already trained | High capacity, slow inference |
| **Student** | Smaller, designed for constraints | Fewer parameters, fast inference |

**Exam Tip:** Distilling from a weak teacher — student quality is bounded by teacher quality.

> **Knowledge Distillation** = Distillation: train a small student to mimic a large teacher

---

## Compression Trade-offs and the MLOps Pipeline — Pick Your Packaging Tool

**The Story:** **Quantisation**: best first step. **Pruning**: for overparameterised models; structured > unstructured for HW. **Distillation**: powerful but training-intensive. Integrate into MLOps pipeline with benchmarks.

**Key mechanics:**
- **Quantisation**: best first step; easy PTQ, big INT8 gains
- **Pruning**: for overparameterised models; structured > unstructured for HW
- **Distillation**: powerful but training-intensive; design student for constraints
- Always measure **size, latency, accuracy** before and after
- Pipeline: train → compress → export → optimised runtime → serve

| Technique | Ease of application | Typical accuracy impact | Speed/size gain | Best first step? |
|-----------|--------------------|-----------------------|-----------------|------------------|
| **Quantisation** | High (especially PTQ) | Small at FP16; moderate at INT8 | Large (esp. INT8) | **Yes — often first** |
| **Pruning** | Medium | Moderate without fine-tune | Large if structured + fine-tuned | When model is overparameterised |
| **Distillation** | Low (requires retraining) | Can improve vs small baseline | Large (new architecture) | When architecture redesign is acceptable |

**Exam Tip:** Applying multiple techniques simultaneously without isolating effects — cannot attribute gains or regressions.

> **Compression Trade-offs and the MLOps Pipeline** = Quantisation: best first step; easy PTQ, big INT8 gains

---

## Optimised Runtimes: Foundations — Turbocharged Conveyor Belts

**The Story:** **Optimised runtimes** execute standard-format graphs with max hardware efficiency via graph fusion, kernel selection, memory reuse, accelerator exploitation. Same math; better latency, throughput, memory.

**Key mechanics:**
- Optimised runtimes execute standard-format graphs with maximum hardware efficiency
- Four mechanisms: graph fusion, kernel selection, memory reuse, accelerator exploitation
- Outputs stay mathematically the same; latency, throughput, and memory improve
- Three focus runtimes: **ONNX Runtime**, **TensorRT**, **XLA**
- Trade-off 1: portability (ONNX Runtime) vs peak perf (TensorRT)


$\text{Conv} \rightarrow \text{BatchNorm} \rightarrow \text{ReLU}$

| Objective | Runtime contribution |
|-----------|---------------------|
| Lower **latency** | Fused ops, tuned kernels |
| Higher **throughput** | Parallel execution, memory efficiency |
| Lower **memory** | Buffer reuse, in-place ops |
| Same **accuracy** | Optimisation is execution-level, not mathematical |

**Exam Tip:** Expecting runtime optimisation to fix a bad model — runtimes optimise execution, not accuracy.

> **Optimised Runtimes: Foundations** = Optimised runtimes execute standard-format graphs with maximum hardware efficiency

---

## ONNX Runtime, TensorRT, and XLA — Three Engine Choices

**The Story:** **ONNX Runtime**: portable, execution providers for CPU/GPU/TensorRT. **TensorRT**: NVIDIA peak perf; per-GPU engine; FP16/INT8. **XLA**: TF/JAX compiler; fuses ops to machine code.

**Key mechanics:**
- **ONNX Runtime**: portable, ONNX-native, execution providers for CPU/GPU/TensorRT
- **TensorRT**: NVIDIA GPU peak performance; builds per-GPU engine; FP16/INT8
- **XLA**: TF/JAX compiler; fuses ops to machine code; CPU/GPU/TPU
- ORT = general-purpose default; TensorRT = NVIDIA latency champion; XLA = TF/JAX ecosystem
- TensorRT and XLA pay compile-time cost for runtime speed

| Feature | Detail |
|---------|--------|
| Hardware | CPU, GPU, and accelerators via **Execution Providers** |
| Execution Providers | `CPUExecutionProvider`, `CUDAExecutionProvider`, `TensorrtExecutionProvider`, others |
| Graph optimisations | Built-in fusion, constant folding, layout optimisation |
| APIs | Python, C, C++, C#, Java, JavaScript |

**Exam Tip:** Using TensorRT for CPU inference — TensorRT is GPU-only.

> **ONNX Runtime, TensorRT, and XLA** = ONNX Runtime: portable, ONNX-native, execution providers for CPU/GPU/TensorRT

---

## Runtime Trade-offs and Deployment Fit — Portable vs Peak Performance

**The Story:** **Portable**: ONNX + ORT — one format, many platforms. **Hardware-specific**: TensorRT — best NVIDIA latency; less portable. Compile-time investment (TensorRT/XLA) pays per-request savings.

**Key mechanics:**
- **Portable**: ONNX + ORT — one format, many platforms; may sacrifice peak perf
- **Hardware-specific**: TensorRT — best NVIDIA latency; less portable, more setup
- **Compile vs runtime**: TensorRT/XLA invest upfront for per-request savings
- Strategy: portable first → measure → hardware-specific for critical paths
- Full pipeline: train → compress → export → runtime

| Advantage | Limitation |
|-----------|------------|
| One model format across teams | May not reach absolute peak on every device |
| One runtime, multiple execution providers | Generic kernels vs hand-tuned vendor kernels |
| Simpler standardisation story | GPU speed may trail TensorRT |

**Exam Tip:** Defaulting to TensorRT for all models — over-engineering if PyTorch or ORT already meets SLA on CPU.

> **Runtime Trade-offs and Deployment Fit** = Portable: ONNX + ORT — one format, many platforms; may sacrifice peak perf

---

## Establishing a Baseline: Model Size and Latency — Weigh Before Shrink-Wrapping

**The Story:** Baseline = disk size + avg/**P95 latency** before optimisation. ResNet-18 on CPU: realistic reference. **Warm-up loop** essential for steady-state measurements — first run lies.

**Key mechanics:**
- Baseline = disk size + avg/P95 latency before any optimisation
- ResNet-18 on CPU: realistic, well-known reference architecture
- Warm-up loop essential for steady-state measurements
- Save metrics to JSON for automated downstream comparison
- PyTorch CPU backend is highly optimised for standard small CNNs

| Aspect | PyTorch | ONNX Runtime |
|--------|---------|--------------|
| Primary goal | Full ML lifecycle | Inference only |
| Graph optimisation | Runtime-level | Dedicated fusion passes |
| Input type | `torch.Tensor` | `numpy.ndarray` |
| Portability | PyTorch required | Any ORT-supported platform |

**Exam Tip:** Timing without `model.eval()` — dropout and batch norm behave differently in train mode.

> **Establishing a Baseline: Model Size and Latency** = Baseline = disk size + avg/P95 latency before any optimisation

---

## Exporting a CNN to ONNX Format — Export to Universal Crate

**The Story:** `torch.onnx.export` traces graph with dummy input; names define runtime API. `dynamic_axes` enables variable batch size. `onnx.checker.check_model` validates structure.

**Key mechanics:**
- `torch.onnx.export` traces graph with dummy input; names define runtime API
- `dynamic_axes` enables variable batch size at inference
- `onnx.checker.check_model` validates graph structure and node count
- FP32 export is size-neutral and lossless — same weights, different container
- Gain is portability and multi-runtime optimisation potential, not immediate speed

| Parameter | Role |
|-----------|------|
| `model` | Network in eval mode with trained weights |
| `dummy_input` | Representative tensor for graph tracing |
| `input_names` / `output_names` | Public API names used by all runtimes |
| `dynamic_axes` | Allow variable batch size at inference time |

**Exam Tip:** Exporting in train mode — batch norm and dropout produce wrong graph.

> **Exporting a CNN to ONNX Format** = torch.onnx.export traces graph with dummy input; names define runtime API

---

## ONNX Runtime Benchmarking and Interpreting Results — ORT vs PyTorch Showdown

**The Story:** ORT: `InferenceSession` + `session.run` with numpy arrays. Match CPU provider to PyTorch for fair comparison. ResNet-18 + batch=1 + vanilla ORT can be **slower** than PyTorch — measure, do not assume.

**Key mechanics:**
- ORT inference: `InferenceSession` + `session.run` with numpy arrays and named inputs
- Match CPU provider to PyTorch CPU baseline for fair comparison
- ResNet-18 + CPU + batch=1 + vanilla ORT can be **slower** than PyTorch
- Reasons: small model, CPU-only, batch=1, no graph optimisations enabled
- ORT wins on large models, GPU, quantisation, cross-platform production

| PyTorch | ONNX Runtime |
|---------|--------------|
| `torch.Tensor` input | `numpy.ndarray` input |
| `model(tensor)` | `session.run(None, {name: array})` |
| Implicit I/O | Explicit `input_names` from export |

**Exam Tip:** "ONNX Runtime is always faster" — disproven by this exact experiment; context matters.

> **ONNX Runtime Benchmarking and Interpreting Results** = ORT inference: InferenceSession + session.run with numpy arrays and named inputs

---

# PART 8: SCALING THE CHAIN (Week 8)
*The Four-Way Tug-of-War*

---

## The Four-Way Tug-of-War Mental Model — Four Teams Pulling the Rope

**The Story:** Production ML sits at a four-way **tug-of-war**: **accuracy** (bigger models), **latency** (speed), **cost** (frugality), **UX** (what customers feel). Isolated optimisation on one axis damages the others.

**Key mechanics:**
- Production ML sits at the centre of a four-way tug-of-war: accuracy, latency, cost, UX.
- Accuracy pulls toward bigger models; latency pulls toward speed; cost pulls toward frugality; UX reflects all three.
- Isolated optimisation on one axis reliably damages the others.
- The goal is an acceptable balance for product and business constraints, not winning one side.

| Force | Pulls toward… | Typical mechanism |
|-------|---------------|-------------------|
| **Accuracy** | Larger, deeper, more powerful models | More parameters, heavier compute per request |
| **Latency** | Sub-second (often sub-100 ms) responses | Smaller models, more replicas, specialised hardware |
| **Cost** | Minimal infrastructure spend | Fewer/smaller instances, batch workloads, spot pricing |
| **UX** | Snappy, reliable, trustworthy interactions | Balance of the other three — users never see AUC |

**Exam Tip:** "We improved accuracy, so the release is a success" — ignore latency/UX at your peril.

> **The Four-Way Tug-of-War Mental Model** = Production ML sits at the centre of a four-way tug-of-war: accuracy, latency, cost, UX.

---

## Accuracy, Latency, Cost, and User Experience — Bigger Factory, Slower Truck

**The Story:** Accuracy improves with complexity but raises **latency** and **cost**. UX is sensitive: ~100–200 ms feels instant; >1 s feels slow. Users feel responsiveness, not AUC.

**Key mechanics:**
- Accuracy improves with model complexity but raises latency and cost per request.
- Human UX is sensitive to latency: ~100–200 ms feels instant; >1 s feels slow.
- Users feel responsiveness, not AUC — latency is an invisible but critical force.
- Cost scales with replicas, instance type, and engineering overhead.
- UX synthesises speed, correctness, reliability, and trust — it is the ultimate product metric.

| Latency range | User perception |
|---------------|-----------------|
| ~100–200 ms | Feels almost instant |
| ~500 ms – 1 s | Noticeable delay |
| > 1–2 s | Slow, frustrating interface |

**Exam Tip:** Choosing the offline leaderboard winner without checking P95 latency under production load.

> **Accuracy, Latency, Cost, and User Experience** = Accuracy improves with model complexity but raises latency and cost per request.

---

## The Latency–Cost–UX Triangle — The Triangle Nobody Escapes

**The Story:** **Latency**, **cost**, and **UX** form a triangle: lower latency costs more; aggressive cost cuts raise latency. Use a four-question checklist (accuracy, latency, cost, UX) for every change; track avg *and* **P95**.

**Key mechanics:**
- Latency, cost, and UX form a triangle: lower latency usually costs more; aggressive cost cuts raise latency and hurt UX.
- Use a **four-question checklist** (accuracy, latency, cost, UX) for every production change.
- Always track both average and P95 latency.
- Inability to answer all four questions signals a blind spot in the change evaluation.

| Goal | Typical action | Effect on cost | Effect on UX |
|------|----------------|----------------|--------------|
| Reduce latency | Add replicas or upgrade to GPU/larger instances | Increases | Improves (if sized correctly) |
| Reduce cost | Shrink instances or reduce replica count | Decreases | Degrades if taken too far — jitter, timeouts, instability |

**Exam Tip:** Measuring only average latency — P95/P99 drive SLA violations and user frustration.

> **The Latency–Cost–UX Triangle** = Latency, cost, and UX form a triangle: lower latency usually costs more; aggressive cost cuts raise latency and hurt UX.

---

## Why ML Services Need to Scale — Holiday Rush Every Day

**The Story:** ML traffic is spiky; fixed capacity → rising latency, **SLO** violations. **Vertical scaling**: bigger machine — simple but limited. **Horizontal scaling**: more replicas + load balancer — standard at scale.

**Key mechanics:**
- ML traffic is spiky and grows over time; fixed capacity leads to rising latency and SLO violations.
- **Vertical scaling**: bigger machine — simple but limited.
- **Horizontal scaling**: more replicas + load balancer — standard at scale.
- **Autoscaling**: dynamically adjusts replica count based on metrics.
- Scaling keeps latency/UX stable under load; cost must still be managed deliberately.

| Pattern | Mechanism | Mental model |
|---------|-----------|--------------|
| **Vertical scaling** | Replace existing machine with a bigger one (more CPU, RAM, GPU) | One stronger box |
| **Horizontal scaling** | Run multiple copies of the service; load balancer distributes traffic | Many identical boxes |

**Exam Tip:** Assuming traffic is flat — ML services almost always have spikes and growth curves.

> **Why ML Services Need to Scale** = ML traffic is spiky and grows over time; fixed capacity leads to rising latency and SLO violations.

---

## Vertical Scaling, Horizontal Scaling, and Autoscaling — Bigger Truck vs More Trucks

**The Story:** **Vertical**: bigger box — quick win, single point of failure. **Horizontal**: replicas + LB — needs state coordination. **Autoscaling**: dynamic replicas from CPU, QPS, **P95** — with min/max and cooldowns.

**Key mechanics:**
- **Vertical scaling**: bigger box — simple, limited, single point of failure.
- **Horizontal scaling**: more replicas + load balancer — standard at scale, needs state and deploy coordination.
- **Autoscaling**: dynamic replica count from CPU, QPS, or P95 triggers — requires min/max bounds and cooldowns.
- **Flapping** = rapid scale in/out from over-sensitive rules — hurts cost and stability.
- Good monitoring is essential for sensible autoscaling policy design.

| Pros | Cons |
|------|------|
| Easy to implement | Hard upper limit on single-machine size |
| Manage one (or few) instances | Single point of failure — if the box dies, service is down |
| Fine for prototypes and low–medium traffic | Large instances often have **worse price/performance** per CPU/RAM unit |
| Quick latency win for small systems | Eventually impossible or not cost-effective to scale further |

**Exam Tip:** Using vertical scaling indefinitely — every machine has a size limit and diminishing returns.

> **Vertical Scaling, Horizontal Scaling, and Autoscaling** = Vertical scaling: bigger box — simple, limited, single point of failure.

---

## Scaling Patterns Compared: Latency, Cost, and Stability — Staffing the Rush Hour

**The Story:** Vertical: quick latency win for small systems; hits limits at scale. Horizontal + autoscaling: standard for spikes; stabilises **P95** with caps. Pattern depends on stage, traffic shape, budget.

**Key mechanics:**
- Vertical scaling: quick latency win for small systems; hits limits and cost inefficiency at scale.
- Horizontal + autoscaling: standard for spikes and high traffic; stabilises P95 with proper caps.
- Pattern choice depends on stage, traffic shape, and budget.
- Cost levers (spot, serverless, batching) complement scaling — they do not replace it.
- Scaling + cost optimisation + decision framework form the full production engineering toolkit.

| Pattern | Latency impact | Cost impact | Best stage / traffic |
|---------|----------------|-------------|----------------------|
| **Vertical scaling** | Quick improvement for small–medium systems | Large instances can be expensive per unit; ceiling exists | Early product, moderate traffic |
| **Horizontal + autoscaling** | Keeps P95 more stable as load grows | Grows with replica count — needs upper limits | Spikes, high sustained traffic |

**Exam Tip:** Jumping to horizontal scaling for a prototype with 10 RPS — vertical may suffice and be simpler.

> **Scaling Patterns Compared: Latency, Cost, and Stability** = Vertical scaling: quick latency win for small systems; hits limits and cost inefficiency at scale.

---

## Inference Cost and Spot / Preemptible Instances — Discount Trucks With Risk

**The Story:** **On-demand**: flexible, expensive. **Reserved**: cheaper for steady load. **Spot**: cheapest, interruptible — suits **batch**, offline scoring, training with checkpoints; not sole infra for critical online APIs.

**Key mechanics:**
- Inference cost is dominated by compute, idle capacity, network/storage, and engineering overhead.
- **On-demand**: flexible, most expensive; **reserved**: cheaper for steady load; **spot**: cheapest, interruptible.
- Spot suits batch, offline scoring, training with checkpoints — not sole infrastructure for critical online APIs.
- Hybrid pattern: on-demand core + spot for batch/overflow balances cost and reliability.
- Cost levers must be evaluated against latency and UX, not just monthly bills.

| Cost driver | Description |
|-------------|-------------|
| **Compute** | Number and type of machines (GPU vs CPU instances) — usually the largest line item |
| **Idle capacity** | Instances running but underutilised — paying for unused headroom |
| **Network & storage** | Data movement, model artefacts, logs |
| **Engineering time** | Maintenance, incident response, pipeline upkeep |

**Exam Tip:** Running latency-critical API entirely on spot — interruptions violate availability SLOs.

> **Inference Cost and Spot / Preemptible Instances** = Inference cost is dominated by compute, idle capacity, network/storage, and engineering overhead.

---

## Serverless Inference — Pay-Per-Prediction Booth

**The Story:** **Serverless inference**: model as function; platform scales and bills per use. Best for spiky, low-volume, prototypes. **Cold starts**, resource limits, vendor lock-in are main trade-offs.

**Key mechanics:**
- Serverless inference: model as a function; platform scales and bills per use.
- Best for spiky, low-volume, prototype, and internal workloads.
- **Cold starts**, resource limits, and vendor lock-in are the main trade-offs.
- Latency-critical online APIs need careful evaluation of cold-start impact on P95.
- At high sustained QPS, dedicated services with autoscaling often outperform serverless economically.

| Workload shape | Why serverless works |
|----------------|---------------------|
| **Spiky traffic** | Scales to zero between spikes — no idle cost |
| **Low average volume** | Cheaper than 24/7 dedicated instances |
| **Prototypes & internal tools** | No server management overhead |
| **Unpredictable demand** | Platform handles capacity planning |

**Exam Tip:** Using serverless for high-QPS GPU inference without checking limits — memory/time caps may block deployment.

> **Serverless Inference** = Serverless inference: model as a function; platform scales and bills per use.

---

## Batching and Micro-Batching for Cost Efficiency — Brief Queue at the Counter

**The Story:** **Batching** amortises forward-pass overhead. **Offline batch**: no user waiting — max batch size, spot instances. **Micro-batching**: brief online queue — tune max batch size and max wait against **SLA**.

**Key mechanics:**
- Batching amortises forward-pass overhead across many inputs — lower cost per request, higher throughput.
- **Offline batch**: no user waiting — maximise batch size and use spot instances.
- **Micro-batching**: brief queuing window online — tune max batch size and max wait time against SLA.
- GPU APIs benefit most; tuning must protect P95 latency.
- Cost levers (spot, serverless, batching) are often **combined** based on workload shape.


$N \times C \times H \times W$

| Mode | User waiting? | Latency tolerance | Typical use |
|------|---------------|-------------------|-------------|
| **Offline batch** | No | Hours acceptable | Nightly churn scoring, ETL pipelines |
| **Online micro-batching** | Yes — briefly | Milliseconds of queuing | High-QPS GPU APIs |

**Exam Tip:** Micro-batching without measuring P95 — average latency looks fine while tail blows SLA.

> **Batching and Micro-Batching for Cost Efficiency** = Batching amortises forward-pass overhead across many inputs — lower cost per request, higher throughput.

---

## Reading Constraints: A Decision Framework — Read the Contract First

**The Story:** First design step: **read constraints** — latency/UX, accuracy/risk, cost, traffic. Real-time user → online with strict **P95**; no one waiting → batch/async. High mistake cost → accuracy, monitoring, **canary**.

**Key mechanics:**
- First step in production design: **read constraints** — latency/UX, accuracy/risk, cost, traffic.
- Real-time user waiting → online with strict P95; no one waiting → batch/async OK.
- Higher mistake cost → accuracy, monitoring, canary deployment.
- Traffic shape and budget drive scaling pattern and cost lever selection.
- Constraints precede model format, compression, and infrastructure choices.

| Context | Inference mode | Latency priority |
|---------|----------------|------------------|
| User waiting in real time | **Online** request–response | Strict P95 targets (often 100–200 ms) |
| Monthly churn score, nightly backfill | **Batch / async** | Throughput and cost over per-row latency |

**Exam Tip:** Starting with infrastructure ("we'll use Kubernetes") before defining latency SLA and risk tier.

> **Reading Constraints: A Decision Framework** = First step in production design: read constraints — latency/UX, accuracy/risk, cost, traffic.

---

## Scenario-Based Deployment Decisions — Three Store Types

**The Story:** **Fraud**: online, high accuracy, horizontal autoscaling, premium HW, heavy monitoring. **Churn**: batch, spot, throughput-focused. **Mobile edge**: quantised/distilled, size/battery/latency per frame.

**Key mechanics:**
- **Fraud check**: online, high accuracy, horizontal autoscaling, premium hardware, heavy monitoring.
- **Churn prediction**: batch, spot instances, throughput-focused, hours-not-ms SLA.
- **Mobile edge**: quantised/distilled model, size/battery/latency per frame, cloud for training.
- Four-step flow: user waiting → mistake risk → traffic/budget → model fit.
- Architecture follows constraints — not the reverse.

| Dimension | Requirement |
|-----------|-------------|
| Accuracy | Very high — mistakes lose money or block legitimate users |
| Latency | Low — user waits for payment to complete |
| Availability | High — system should rarely be down |
| Stakes | Very high |

**Exam Tip:** Running churn scoring as online API — wastes money; batch + spot is appropriate.

> **Scenario-Based Deployment Decisions** = Fraud check: online, high accuracy, horizontal autoscaling, premium hardware, heavy monitoring.

---

## Dynamic Quantisation for Model Compression — Dynamic Shrink-Wrap

**The Story:** **Dynamic quantisation**: FP32 weights → INT8 — ~4× smaller, faster on CPU, possible small accuracy loss. Establish FP32 baseline size before optimising.

**Key mechanics:**
- Compression targets model size/speed when ONNX export alone is insufficient.
- **Dynamic quantisation**: FP32 weights → INT8 — ~4× smaller, faster on CPU, possible small accuracy loss.
- Always establish FP32 baseline size before optimising.
- ONNX Runtime `quantize_dynamic` with `QInt8` is a one-call compression path.
- Valid forward pass ≠ production-ready — benchmark size, latency, and accuracy next.


$-128$
$127$

| Effect | Mechanism |
|--------|-----------|
| ~**4× size reduction** | 32 bits → 8 bits per weight |
| **Faster CPU inference** | Integer arithmetic is typically faster than FP32 on CPUs |
| **Potential accuracy drop** | Less precise weights → small metric degradation (must be measured) |

**Exam Tip:** Skipping baseline measurement — cannot report improvement percentage.

> **Dynamic Quantisation for Model Compression** = Compression targets model size/speed when ONNX export alone is insufficient.

---

## Benchmarking Compression: Size, Latency, and Accuracy — Before and After Weigh-In

**The Story:** Benchmark FP32 vs compressed across **size**, **latency** (avg + **P95**), **accuracy**. Warm-up + repeated runs for stable numbers. INT8 wins size/latency on CPU; accuracy needs validation data.

**Key mechanics:**
- Benchmark FP32 vs compressed across **size, latency (avg + P95), and accuracy**.
- Use warm-up + repeated runs for stable latency numbers.
- Size and latency often show clear INT8 wins on CPU; accuracy requires validation data.
- The decision question: is small accuracy loss acceptable for size/speed gains in **your** use case?
- Production compression workflow always includes accuracy on a representative validation set.

| Dimension | Measurement | Production relevance |
|-----------|-------------|----------------------|
| **File size (MB)** | On-disk model artefact | Edge download, RAM, storage cost |
| **Inference latency** | Average and **P95** over N runs | UX, SLA compliance, fleet sizing |
| **Accuracy** | Validation set metrics | Product quality, risk tier acceptance |

**Exam Tip:** Benchmarking without warm-up — first-run load time skews averages.

> **Benchmarking Compression: Size, Latency, and Accuracy** = Benchmark FP32 vs compressed across size, latency (avg + P95), and accuracy.

---

## Deployment Fit: Edge vs Cloud for Compressed Models — Shelf vs Pocket

**The Story:** **FP32**: max precision — high-stakes, GPU cloud, unconstrained batch. **INT8**: 4× smaller, faster on CPU — edge/mobile, cost-sensitive cloud APIs. Align model profile with business goals.

**Key mechanics:**
- **FP32**: max precision — high-stakes domains, GPU cloud, unconstrained batch jobs.
- **INT8**: 4× smaller, much faster on CPU — edge/mobile, high-QPS cost-sensitive cloud APIs.
- Deployment aligns model profile with business goals — not benchmark wins alone.
- Always validate accuracy drop against risk tier before deploying compressed models.
- Full workflow: identify need → compress → benchmark → decide → justify trade-offs.

| Domain | Why FP32 may win |
|--------|------------------|
| Medical diagnosis | False negatives/positives have severe consequences |
| Financial fraud detection | Cost of mistake exceeds infrastructure cost |
| High-stakes automated decisions | Business value of precision outweighs cloud spend |

**Exam Tip:** Deploying INT8 to fraud/medical without measuring recall/precision drop — unacceptable risk.

> **Deployment Fit: Edge vs Cloud for Compressed Models** = FP32: max precision — high-stakes domains, GPU cloud, unconstrained batch jobs.

---

# PART 9: THE INGREDIENT WAREHOUSE (Week 9)
*Feature Stores and Single Sources of Truth*

---

## Training-Serving Skew: Definition, Causes, and Consequences — Same Label, Different Ingredient

**The Story:** **Training-serving skew**: model sees different **feature distributions** in training vs serving. Causes: different code, time windows, sources, filters. Classic trap: **30-day** feature in training, **7-day** in serving — same name, different semantics.

**Key mechanics:**
- Training-serving skew: model sees different feature distributions in training vs serving.
- Causes: different code, time windows, sources, filters, or unsynchronised ETL changes.
- Classic trap: 30-day feature in training, 7-day feature in serving — same name, different semantics.
- Consequences: silent production degradation; offline metrics remain misleadingly strong.
- Root cause: fragmented, ad hoc feature logic across teams and systems.


$\text{Skew exists when } P_{\text{train}}(\mathbf{x}) \neq P_{\text{serve}}(\mathbf{x})$
$170 total) | Inactive spender ($
$P_{\text{train}}$

| Cause | Training | Serving | Result |
|-------|----------|---------|--------|
| Time window mismatch | 30-day aggregation | 7-day aggregation | Different scale and variance |
| Code path divergence | SQL in warehouse | Reimplemented Python | Subtle filter differences |
| Data source split | Batch ETL table | Live API stream | Missing or extra events |
| Filter logic | Excludes refunds | Includes refunds | Systematic value shift |

**Exam Tip:** **Confusing skew with data drift** — Drift is natural distribution change over time; skew is a pipeline implementation mismatch from day one.

> **Training-Serving Skew: Definition, Causes, and Consequences** = Training-serving skew: model sees different feature distributions in training vs serving.

---

## Offline Features: Batch Computation for Training — Warehouse Pre-Prep

**The Story:** **Offline features**: batch-computed, stored in data lake/warehouse, used for training and batch scoring. Optimised for throughput; pipelines run minutes to hours. Feature tables: one row per entity per `as_of_date`.

**Key mechanics:**
- Offline features: batch-computed, stored in data lake/warehouse, used for training and batch scoring.
- Optimised for throughput; pipelines run minutes to hours on billions of rows.
- Feature tables: one row per entity per `as_of_date` with aggregated columns.
- `as_of_date` enables point-in-time correct joins with labels — critical for avoiding leakage.
- Same feature concept as online features, but different storage, latency, and compute patterns.


$\text{training\_set} = \text{features} \bowtie_{\text{customer\_id, as\_of\_date}} \text{labels}$
$t$

| Column | Description |
|--------|-------------|
| `customer_id` | Entity key |
| `timestamp` | Event time |
| `amount` | Transaction value |
| `category` | Optional segmentation |

**Exam Tip:** **Treating offline tables as always fresh** — Batch features reflect the last pipeline run, not live state.

> **Offline Features: Batch Computation for Training** = Offline features: batch-computed, stored in data lake/warehouse, used for training and batch scoring.

---

## Online Features: Low-Latency Serving — Counter-Ready Ingredients

**The Story:** **Online features**: precomputed values retrieved per entity at request time in milliseconds. Stored in low-latency KV (Redis, DynamoDB). Flow: request → lookup by key → optional transforms → inference.

**Key mechanics:**
- Online features: precomputed values retrieved per entity at request time in milliseconds.
- Stored in low-latency key-value systems (Redis, DynamoDB, Cassandra).
- Serving flow: request → feature lookup by key → optional transforms → model inference.
- **Materialisation** pushes computed values into the online store via batch or streaming jobs.
- Optimised for latency and freshness; no heavy per-request joins.

| Property | Requirement |
|----------|-------------|
| Latency | Few milliseconds per lookup (often 10–20 ms total for all features) |
| Availability | High uptime under heavy traffic |
| Freshness | Reflects recent events (minutes to hours, depending on use case) |
| Access pattern | Key-based lookup by entity ID |

**Exam Tip:** **Running batch aggregations per request** — Defeats the purpose of online features; use precomputation.

> **Online Features: Low-Latency Serving** = Online features: precomputed values retrieved per entity at request time in milliseconds.

---

## What a Feature Store Provides — Central Ingredient Catalogue

**The Story:** **Feature store**: define features once, serve offline and online. Four jobs: definition, offline materialisation, online materialisation, serving API + catalogue. Core promise: consistent features → eliminates skew.

**Key mechanics:**
- Feature store: central system to define features once and serve them offline and online.
- Four responsibilities: definition, offline materialisation, online materialisation, serving API + catalogue.
- Core promise: consistent features across training and serving → eliminates skew class.
- Offline store for training/batch scoring; online store for real-time prediction.
- Registry enables discovery, metadata, and reuse across teams and models.

| Element | Purpose |
|---------|---------|
| Entity key | Primary lookup key (e.g., `customer_id`) |
| Event timestamp | Column for point-in-time correctness |
| Transformation logic | Aggregation, window, filters |
| Feature name & schema | Type, description, units |

**Exam Tip:** **"Feature store = database"** — It is a system for definition, materialisation, serving, and governance — not just storage.

> **What a Feature Store Provides** = Feature store: central system to define features once and serve them offline and online.

---

## Feature Store Ecosystem: Common Building Blocks — Same Shelves, Different Brands

**The Story:** All feature stores share four blocks: definitions, offline store, online store, registry. **Feast** = open-source baseline; **Tecton** = managed enterprise; **Hopsworks** = broader ML platform. Concepts stay stable; vendor names change.

**Key mechanics:**
- All feature stores share four building blocks: definitions, offline store, online store, registry.
- Feast = open-source baseline; Tecton = managed enterprise; Hopsworks = broader ML platform.
- Vendor names change; core concepts (define once, materialise twice, serve via API) stay stable.
- Evaluate any feature store by asking about definitions, sync, registry, and safe feature addition.
- Use cases: skew prevention, feature reuse, online latency, governance.

| Tool | Type | Positioning |
|------|------|-------------|
| **Feast** | Open-source, self-hosted | Conceptual baseline; Python/YAML definitions |
| **Tecton** | Managed enterprise platform | Infrastructure + pipelines + governance UI |
| **Hopsworks** | ML platform with feature store | Feature store + notebooks + model registry |

**Exam Tip:** **Memorising vendor APIs instead of the pattern** — Exams test concepts (offline/online, registry, materialisation), not specific SDK calls.

> **Feature Store Ecosystem: Common Building Blocks** = All feature stores share four building blocks: definitions, offline store, online store, registry.

---

## Feast: Open-Source Feature Store Baseline — Feast as Reference Kitchen

**The Story:** **Feast**: entities, feature views, feature services, data sources, registry. Workflow: define → materialise offline → materialise online → serve via APIs — the mental baseline for all feature stores.

**Key mechanics:**
- Feast: open-source feature store; mental baseline for understanding all feature stores.
- Core concepts: entities, feature views, feature services, data sources, registry.
- Workflow: define → materialise offline → materialise online → serve via APIs.
- `get_historical_features()` for training; `get_online_features()` for serving.
- Same feature definition drives both materialisation paths → prevents skew.

| Concept | Description |
|---------|-------------|
| **Entity** | Key type for features (e.g., `customer_id`) |
| **Feature View** | A logical group of features derived from a source, with transformation logic |
| **Feature Service** | A curated bundle of features for a specific model or use case |
| **Data Source** | Upstream table, file, or stream reference |

**Exam Tip:** **Confusing Feast registry with offline store** — Registry holds metadata/definitions; offline store holds computed historical values.

> **Feast: Open-Source Feature Store Baseline** = Feast: open-source feature store; mental baseline for understanding all feature stores.

---

## Managed Feature Platforms: Tecton and Hopsworks — Fully Staffed Kitchen

**The Story:** **Tecton**: managed enterprise; runs pipelines, rich UI, streaming/warehouse integration. **Hopsworks**: ML platform with integrated feature store, notebooks, registry. Same four building blocks, more management.

**Key mechanics:**
- Tecton: managed enterprise feature platform; runs pipelines, rich UI, deep streaming/warehouse integration.
- Hopsworks: ML platform with integrated feature store, notebooks, model registry, orchestration.
- Both implement the same four building blocks as Feast with more management and governance.
- Differences: hosting model, UI depth, ecosystem integration, scope (feature-only vs full ML platform).
- Core pattern stable across all vendors: define → materialise offline + online → serve via API + registry.

| Capability | Tecton Approach |
|------------|-----------------|
| Pipeline management | Managed; teams define features, Tecton runs compute |
| UI | Rich feature discovery and management dashboard |
| Streaming | Deep integration with Kafka, Kinesis, etc. |
| Warehouse integration | Native connectors to Snowflake, BigQuery, Redshift |

**Exam Tip:** **"Tecton and Feast are completely different architectures"** — Same pattern; Tecton adds managed ops and enterprise UI.

> **Managed Feature Platforms: Tecton and Hopsworks** = Tecton: managed enterprise feature platform; runs pipelines, rich UI, deep streaming/warehouse integration.

---

## The Common Feature Store Pattern: Practical Takeaways — Define Once, Serve Twice

**The Story:** Universal pattern: define → offline materialise → online materialise → registry. Vendor differences: hosting, integrations, UI, governance — not core architecture. Ask four key questions before adopting.

**Key mechanics:**
- Universal pattern: define → offline materialise → online materialise → registry.
- Vendor differences: hosting, integrations, UI, governance — not core architecture.
- Model engineers should recognise when feature stores are needed and ask four key questions.
- Organisational benefits (reuse, metadata, lineage, governance) extend beyond technical consistency.
- Labs simulate the pattern with pandas + dict + shared function.

| Signal | Why a Feature Store Helps |
|--------|--------------------------|
| Repeated training-serving skew incidents | Enforces single definition across paths |
| Many teams reimplementing same features | Central registry + reuse eliminates duplication |
| Growing low-latency online feature demand | Built-in online materialisation and serving API |
| Multi-model feature sharing | One definition serves churn, fraud, recommendation models |

**Exam Tip:** **Treating vendor choice as the core learning objective** — Pattern recognition and good questions matter more.

> **The Common Feature Store Pattern: Practical Takeaways** = Universal pattern: define → offline materialise → online materialise → registry.

---

## Feature Reuse: Solving Duplication and Inconsistency — One Recipe, Many Counters

**The Story:** Without feature stores, same feature reimplemented 3–4 times with subtle differences — duplication, inconsistency, debugging nightmares. **Feature store**: define once, register, reuse across models and teams.

**Key mechanics:**
- Without feature stores: same feature reimplemented 3–4 times with subtle differences.
- Symptoms: duplication, inconsistency, debugging nightmares, slow onboarding.
- Feature store solution: define once, register, reuse across models and teams.
- Benefits: less duplicated ETL, fewer bugs, faster new use cases, consistent semantics.
- Reuse and training-serving consistency both stem from the single-definition principle.

| Symptom | Impact |
|---------|--------|
| 3–4 versions of "the same" feature | Inconsistent model inputs across teams |
| Copy-paste ETL code | Duplicated effort, divergent bug fixes |
| Same feature name, different semantics | Numbers don't match across dashboards and models |
| No single owner | Nobody responsible when values change unexpectedly |

**Exam Tip:** **"Reuse means all models share all features"** — Models select relevant subsets; the catalogue is shared, not monolithic.

> **Feature Reuse: Solving Duplication and Inconsistency** = Without feature stores: same feature reimplemented 3–4 times with subtle differences.

---

## Metadata and Lineage: Understanding and Tracing Features — Ingredient Provenance Labels

**The Story:** **Metadata**: name, description, units, owner, schema, freshness, quality. **Lineage**: upstream (sources, transforms) and downstream (models, APIs, dashboards) — trace any ingredient to its source.

**Key mechanics:**
- Metadata: name, description, units, owner, schema, freshness, quality, usage per feature.
- Enables discovery, trust, onboarding, and debugging.
- Lineage: upstream (sources, transformations) and downstream (models, APIs, dashboards).
- Lineage use cases: debugging breakage, impact analysis for schema changes, regulatory audits.
- Metadata answers "what is this?"; lineage answers "where from and where to?"

| Field | Description | Example |
|-------|-------------|---------|
| **Name** | Canonical identifier | `customer_30d_total_spend` |
| **Description** | Human-readable explanation | "Sum of completed transaction amounts in last 30 days" |
| **Units** | Measurement unit | USD, count, ratio, days |
| **Owner** | Responsible team or individual | Data Platform / Jane Smith |

**Exam Tip:** **Confusing metadata with lineage** — Metadata describes a feature; lineage describes its relationships in the data graph.

> **Metadata and Lineage: Understanding and Tracing Features** = Metadata: name, description, units, owner, schema, freshness, quality, usage per feature.

---

## Feature Governance and Lifecycle Management — Controlled Substances List

**The Story:** Sensitive features (PII, protected attributes) need access control, usage policies, audit logging. **Feature lifecycle**: experimental → active → deprecated → retired — like managing regulated inventory.

**Key mechanics:**
- Sensitive features: PII, protected attributes, financial, health data — require special handling.
- Governance: access control, usage policies, production blocks, audit logging.
- Feature lifecycle: experimental → active → deprecated → retired.
- Versioning enables safe rollout, dependency tracking, and gradual migration.
- Benefits span data scientists, ML engineers, platform teams, and business.

| Category | Examples | Risk |
|----------|----------|------|
| **PII** | Email, phone, home address, national ID | Privacy violations, GDPR/CCPA breaches |
| **Protected attributes** | Race, gender, religion, age | Discrimination, regulatory bans on use in scoring |
| **Financial data** | Credit scores, income, account balances | PCI/financial regulation, fair lending |
| **Health data** | Diagnosis codes, prescriptions | HIPAA and medical privacy rules |

**Exam Tip:** **"Governance = IT security only"** — Feature governance includes ML-specific policies (fairness, model-specific usage, lifecycle).

> **Feature Governance and Lifecycle Management** = Sensitive features: PII, protected attributes, financial, health data — require special handling.

---

## From Feature Governance to Hands-On Practice — Mini Warehouse Lab

**The Story:** Labs simulate a feature store: pandas offline table + Python dict online store + shared function. Build offline table with 30-day aggregations and `as_of_date`; encapsulate logic in one function for both paths.

**Key mechanics:**
- Labs simulate a feature store: pandas offline table + Python dict online store + shared function.
- Lab 1: build offline feature table with 30-day aggregations and `as_of_date`.
- Lab 2: encapsulate logic in `compute_30d_features()`, materialise to dict, serve via lookup.
- Lab 3: demonstrate skew (7-day bug) and fix (shared function) — core learning moment.
- Module theory: skew, offline/online, feature stores, ecosystem, governance.


$170 spend; online shows $

| Lab Component | Simulates | Production Equivalent |
|---------------|-----------|----------------------|
| `features.py` | Offline feature table build | Warehouse batch pipeline |
| `onlinestore.py` | Online feature store | Redis / DynamoDB |
| `skew.py` | Skew demonstration and fix | Feast / Tecton consistency |
| `compute_30d_features()` | Single source of truth | Feature view definition |

**Exam Tip:** **"The lab is trivial, so feature stores are trivial"** — The lab isolates the core pattern; production adds scale, streaming, governance, and multi-team coordination.

> **From Feature Governance to Hands-On Practice** = Labs simulate a feature store: pandas offline table + Python dict online store + shared function.

---

## Building an Offline Feature Table in Pandas — Rolling 30-Day Totals

**The Story:** Raw events → aggregated entity features. 30-day window: latest timestamp as `as_of_date`, lookback, filter, groupby, aggregate. Features: total spend (sum), txn count, avg ticket.

**Key mechanics:**
- Raw events (customer_id, timestamp, amount) → aggregated entity-level features.
- 30-day window: latest timestamp as `as_of_date`, lookback 30 days, filter, groupby, aggregate.
- Features: total spend (sum), txn count (count), avg ticket (spend/count).
- Output: one row per customer with `as_of_date` for traceability.
- Join with labels on `customer_id` for training.


$\text{training\_data} = \text{feature\_table} \bowtie_{\text{customer\_id}} \text{labels}$

| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | string | Entity key |
| `timestamp` | datetime | Event time |
| `amount` | float | Transaction value |
| `category` | string | Transaction category (optional) |

**Exam Tip:** **Forgetting the time window filter** — Aggregating all data without a window is not a "30-day" feature.

> **Building an Offline Feature Table in Pandas** = Raw events (customer_id, timestamp, amount) → aggregated entity-level features.

---

## Simulating an Online Feature Store with a Dict Cache — Dict as Counter Cache

**The Story:** Encapsulate logic in `compute_30d_features()` — single source of truth. Materialise: iterate customers, compute, store in dict keyed by `customer_id`. Retrieval in milliseconds.

**Key mechanics:**
- Online features: precomputed, retrieved by entity key in milliseconds.
- Step 1: encapsulate logic in `compute_30d_features()` — single source of truth.
- Step 2: materialise — iterate customers, compute, store in dict keyed by `customer_id`.
- Step 3: serve — `get_online_features(customer_id)` is O(1) dict lookup.
- Python dict simulates Redis/DynamoDB; materialisation simulates streaming/batch push.

| Lab Implementation | Production Equivalent |
|-------------------|----------------------|
| Python dictionary | Redis, DynamoDB, Cassandra |
| In-process loop | Distributed streaming/batch materialisation job |
| Single machine | Horizontally scaled cache cluster |

**Exam Tip:** **Reimplementing logic for online instead of reusing the function** — The most common source of skew.

> **Simulating an Online Feature Store with a Dict Cache** = Online features: precomputed, retrieved by entity key in milliseconds.

---

## Avoiding Training-Serving Skew with a Tiny Feature Store — 170 vs Zero

**The Story:** Skew demo: offline 30-day spend=170 vs buggy online 7-day spend=0. Customer appears active in training, inactive in serving. **No errors in logs** — skew is silent and devastating. Shared function fixes both paths.

**Key mechanics:**
- Skew demo: offline 30-day features (spend=170) vs buggy online 7-day features (spend=0).
- Customer appears active in training, inactive in serving — predictions unreliable.
- No errors in logs; skew is silent and dangerous.
- Fix: import and use `compute_30d_features()` — same function for both paths.
- Fixed values match offline perfectly; skew eliminated.

| Feature | Offline Value (30-day) |
|---------|----------------------|
| `customer_30d_total_spend` | 170.0 |
| `customer_30d_txn_count` | 4 |
| `customer_30d_avg_ticket` | 42.5 |

**Exam Tip:** **"The feature name is the same, so values should match"** — Names do not enforce semantics; only shared logic does.

> **Avoiding Training-Serving Skew with a Tiny Feature Store** = Skew demo: offline 30-day features (spend=170) vs buggy online 7-day features (spend=0).

---

# PART 10: THE SUPPLY CHAIN (Week 10)
*Data Pipelines and Fresh Ingredients*

---

## Why Machine Learning Needs Data Pipelines — Hand-Carrying vs Conveyor Belts

**The Story:** Notebooks are **exploratory and manual**; production **pipelines** are automated, scheduled, observable. Pipelines feed training, validation, inference — failures cascade. Late data delays retraining; wrong data makes validation metrics lie.

**Key mechanics:**
- Notebooks are **exploratory and manual**; production pipelines are **automated, scheduled, and observable**.
- Pipelines feed **training, validation, and inference** — failures cascade across the ML lifecycle.
- Late data delays retraining; wrong data makes **validation metrics lie** and breaks production decisions.
- "Run the notebook again" lacks **scheduling, idempotency, state, lineage, and alerting**.
- The notebook-to-pipeline shift is one of the **biggest transitions** in operationalising ML.

| Stage | What Pipelines Provide | Consequence of Pipeline Failure |
|-------|------------------------|--------------------------------|
| **Training** | Historical labelled data, feature tables | Model cannot be built or updated |
| **Validation** | Fresh or held-out evaluation data | Metrics become unreliable or stale |
| **Inference** | Live features and input schemas | Predictions wrong or unavailable |

**Exam Tip:** **Believing automation alone is enough** — a pipeline that runs daily but ingests wrong data is worse than a manual process that catches errors.

> **Why Machine Learning Needs Data Pipelines** = Notebooks are exploratory and manual; production pipelines are automated, scheduled, and observable.

---

## ETL and ELT: Foundations of ML Data Pipelines — Prep Outside vs Inside the Warehouse

**The Story:** **ETL**: extract → transform (external) → load curated tables. **ELT**: extract → load raw → transform inside warehouse (SQL/dbt). Both produce structured tables for feature engineering, training, scoring.

**Key mechanics:**
- **ETL**: extract → transform (external) → load curated tables into warehouse.
- **ELT**: extract → load raw → transform inside warehouse (SQL/dbt).
- Both patterns produce **structured tables** that feed ML feature engineering, training, and scoring.
- ETL suits **complex heterogeneous transforms**; ELT suits **SQL-first teams** with cheap warehouse storage.
- Raw data retention in ELT enables **cheap reprocessing** when transform logic changes.

| Dimension | ETL | ELT |
|-----------|-----|-----|
| Transform location | External engine (Spark, Python) | Inside warehouse (SQL, dbt) |
| Raw data retention | Often discarded post-transform | Typically retained in landing zone |
| Schema enforcement | At transform time | At query/model time |
| Flexibility for complex logic | High (arbitrary code) | Moderate (SQL + UDFs) |

**Exam Tip:** **Assuming ETL and ELT are mutually exclusive** — modern platforms combine both; the question is *where* each transform runs.

> **ETL and ELT: Foundations of ML Data Pipelines** = ETL: extract → transform (external) → load curated tables into warehouse.

---

## Pipeline Types: Batch, Micro-Batch, and Streaming — Daily Truck, Hourly Van, Live Belt

**The Story:** Three modes: **batch** (scheduled chunks), **micro-batch** (frequent small chunks), **streaming** (continuous per-event). Batch = workhorse for retraining; micro-batch = minute-level freshness; streaming = real-time.

**Key mechanics:**
- Three ingestion modes: **batch** (large scheduled chunks), **micro-batch** (frequent small chunks), **streaming** (continuous per-event).
- Batch is the **workhorse** for retraining, offline scoring, and heavy aggregations — simple but stale between runs.
- Micro-batch is the **middle ground** — minute-level freshness using familiar batch tools.
- Streaming uses **producers, topics, consumers, windows, and state** for sub-second ML use cases.
- Selection depends on **latency, complexity, budget, and volume** — not model architecture.

| Use Case | Example |
|----------|---------|
| Regular retraining | Weekly churn model update with new labelled data |
| Offline scoring | Nightly risk scores for all 10M users |
| Heavy aggregations | 30-day and 90-day rolling statistics |
| Feature table refresh | Daily `training_features_20240901` partition |

**Exam Tip:** **Jumping to streaming prematurely** — most ML systems operate fine on batch or micro-batch; streaming adds operational burden without proportional benefit.

> **Pipeline Types: Batch, Micro-Batch, and Streaming** = Three ingestion modes: batch (large scheduled chunks), micro-batch (frequent small chunks), streaming (continuous per-event).

---

## Batch Ingestion for Machine Learning — Midnight Ingredient Delivery

**The Story:** **Batch ingestion** on fixed schedule, specific time window. Ideal for retraining, offline scoring, heavy aggregations. Flow: read partitioned raw → clean → join → aggregate → write feature table → append to master training set.

**Key mechanics:**
- Batch ingestion runs on a **fixed schedule**, processing a **specific time window** per job.
- Ideal for **retraining, offline scoring, and heavy aggregations** where minute-level freshness is unnecessary.
- Typical flow: read partitioned raw data → clean → join → aggregate → write feature table → append to master training set.
- Jobs taking **minutes to hours** is normal for daily ML workflows.
- Each run produces a **versioned, lineage-friendly** artifact.


$\text{sum}(\text{spend})_{30d}$
$\text{count}(\text{clicks})_{7d}$

| Step | Action |
|------|--------|
| Schedule | Daily at 10:00 AM |
| Read | Yesterday's events from partition `events/2024/09/01` |
| Join | Reference tables: `users`, `products` |
| Compute | Feature columns: spend, click counts, tenure |

**Exam Tip:** **Full reprocess instead of incremental append** — re-reading years of partitions daily wastes compute; append new partitions to a master dataset.

> **Batch Ingestion for Machine Learning** = Batch ingestion runs on a fixed schedule, processing a specific time window per job.

---

## Micro-Batch Ingestion: Concept and Architecture — Every Five Minutes

**The Story:** **Micro-batch**: small batches every 1–5 minutes — compromise between batch and streaming. Via Spark Structured Streaming, Flink, Beam, or cron. Best for minute-level freshness without per-event complexity.

**Key mechanics:**
- Micro-batch = **small batches, frequent runs** (every 1–5 minutes) — a compromise between batch and streaming.
- Implemented via **Spark Structured Streaming, Flink, Beam, or simple cron scripts**.
- Best for features needing **minute-level freshness** but not per-event updates.
- Example: risk scores refreshed every 5 minutes from recent transactions.
- **Lower latency** than batch; **lower complexity** than true streaming.


$N$

| Property | Batch | Micro-Batch | Streaming |
|----------|-------|-------------|-----------|
| Window size | Hours to days | 1–5 minutes | Per event |
| Run frequency | Daily / hourly | Every 1–5 min | Continuous |
| Implementation | Cron + Spark/SQL job | Spark Structured Streaming, Flink micro-batch, cron script | Kafka + Flink/Beam |
| Latency | High | Medium (minutes) | Low (seconds) |

**Exam Tip:** **Calling micro-batch "streaming"** — it is batching with a short interval; exam questions may distinguish these explicitly.

> **Micro-Batch Ingestion: Concept and Architecture** = Micro-batch = small batches, frequent runs (every 1–5 minutes) — a compromise between batch and streaming.

---

## Comparing Batch and Micro-Batch Ingestion — Few Big vs Many Small

**The Story:** **Batch**: hours/day latency, lower complexity, retraining. **Micro-batch**: minutes latency, higher complexity, near-real-time features. Cost: batch = fewer big jobs; micro-batch = cumulative overhead.

**Key mechanics:**
- **Batch**: higher latency (hours/day), lower complexity, fewer large jobs, ideal for retraining and offline scoring.
- **Micro-batch**: lower latency (minutes), higher complexity, many small jobs, ideal for near-real-time features.
- **Cost**: batch = fewer big jobs; micro-batch = more runs with cumulative overhead.
- **Rule of thumb**: start with batch; escalate to micro-batch only when freshness requirements demand it.
- Batch excels at **heavy aggregations and score-all jobs**; micro-batch excels at **periodic feature refresh**.

| Dimension | Batch | Micro-Batch |
|-----------|-------|-------------|
| **Latency** | Hours to a full day | 1–5 minutes |
| **Complexity** | Simple — fewer moving parts | More complex — frequent runs, more monitoring |
| **Cost** | Fewer large jobs, lower overhead | Many smaller jobs, cumulative overhead |
| **Infrastructure** | Cron + nightly Spark/SQL | Cron every few min or streaming framework in micro-batch mode |

**Exam Tip:** **Escalating to micro-batch without a freshness requirement** — adds cost and operational burden with no business benefit.

> **Comparing Batch and Micro-Batch Ingestion** = Batch: higher latency (hours/day), lower complexity, fewer large jobs, ideal for retraining and offline scoring.

---

## Event Streams: Foundations of Streaming for ML — Continuous Ingredient Flow

**The Story:** **Streaming** processes continuous **event flows**. An **event** records what happened, when, who/what, details. **Topics** are channels; **producers** publish; **consumers** subscribe and process.

**Key mechanics:**
- Streaming processes **continuous event flows** rather than files or partitions.
- An **event** records what happened, when, who/what was involved, and details.
- **Topics** are named channels; **producers** publish; **consumers** subscribe and process.
- Architecture is **many-to-many** — multiple producers and consumers per topic.
- Streaming asks **"what is happening now?"** vs batch's **"what happened in this window?"**

| Field | Description | Example |
|-------|-------------|---------|
| **What** | Event type | `click`, `purchase`, `sensor_reading` |
| **When** | Timestamp | `2024-09-01T10:01:23Z` |
| **Who / What entity** | Actor or object | `user_id=123`, `sensor_id=45` |
| **Details** | Payload attributes | `amount=$52`, `url=/product/A`, `temp=25°C` |

**Exam Tip:** **Confusing event time with processing time** — a click at 10:00 AM may arrive at 10:05 AM; windowed features must specify which timestamp they use.

> **Event Streams: Foundations of Streaming for ML** = Streaming processes continuous event flows rather than files or partitions.

---

## Kafka, Spark, Flink, and Beam: Roles in Streaming ML — Highway and Vehicles

**The Story:** **Kafka** = event transport and durable log — the highway. **Spark, Flink, Beam** = processing engines — the vehicles. Key concepts: **windows** (tumbling, sliding, session), **aggregations**, **state**.

**Key mechanics:**
- **Kafka** = event transport and durable log (topics, partitions, offsets) — the highway.
- **Spark, Flink, Beam** = processing engines that transform events into features — the vehicles.
- Three key concepts: **windows** (tumbling, sliding, session), **aggregations** (per-key statistics), **state** (running values).
- Windows enable ML features like `clicks_last_10m` and `avg_spend_last_hour`.
- Spark suits **micro-batch and unified batch/stream**; Flink suits **low-latency true streaming**.


$\text{count}(\text{events})$
$\text{sum}(\text{amount})$
$\text{avg}(\text{transaction\_amount})$

| Responsibility | Description |
|----------------|-------------|
| **Topics** | Named channels partitioning the event space |
| **Partitions** | Parallelism units within a topic; ordering guaranteed per partition |
| **Offsets** | Position markers — consumers track how far they have read |
| **Durability** | Events persisted to disk; configurable retention (hours to forever) |

**Exam Tip:** **Using Kafka as a database** — it is a log with retention limits, not a query engine; use a processing engine or sink for reads.

> **Kafka, Spark, Flink, and Beam: Roles in Streaming ML** = Kafka = event transport and durable log (topics, partitions, offsets) — the highway.

---

## Streaming Machine Learning: Use Cases and Architecture — Live Price Tags

**The Story:** Streaming ML: **anomaly detection**, live recommendations, dynamic pricing, fraud, real-time monitoring. Two patterns: **online** (API per request) and **streaming** (event-driven). Touches features, serving, monitoring.

**Key mechanics:**
- Streaming ML excels at **anomaly detection, live recommendations, dynamic pricing, fraud, and real-time monitoring**.
- Two inference patterns: **online** (API per request) and **streaming** (event-driven, predict-on-stream).
- Streaming touches **features, serving, and monitoring** — not just one lifecycle stage.
- **Micro-batch** suffices for minute-level freshness; **full streaming** for sub-second requirements.
- Decision rule: **start simple** (batch/micro-batch), escalate to streaming only with clear latency or volume needs.

| Use Case | Why Streaming | Latency Requirement |
|----------|---------------|---------------------|
| **Real-time anomaly detection** | Unusual traffic, suspicious transactions, system failures | Seconds |
| **Live recommendations** | React to clicks and views in active session | Seconds to minutes |
| **Dynamic pricing / bidding** | Respond to market data and demand signals | Sub-second to seconds |
| **Real-time fraud checks** | Block fraudulent transactions before settlement | Sub-second |

**Exam Tip:** **Adopting streaming without a latency requirement** — operational cost and complexity rarely justify streaming for daily-retrained models.

> **Streaming Machine Learning: Use Cases and Architecture** = Streaming ML excels at anomaly detection, live recommendations, dynamic pricing, fraud, and real-time monitoring.

---

## Data Freshness and Latency in Real-Time ML — Two Clocks Ticking

**The Story:** **Inference latency** (request → prediction) and **data freshness latency** (event → feature) are **independent** — both must be managed. Real-time systems fail quietly with bad data. Define **freshness SLAs per feature category**.

**Key mechanics:**
- Real-time ML systems **fail quietly** with bad data — they do not crash, they make worse decisions.
- **Inference latency** (request → prediction) and **data freshness latency** (event → feature) are **independent** — both must be managed.
- Define **freshness SLAs per feature category**, not just prediction latency SLAs.
- Measure: **average event-to-feature lag** and **SLA compliance percentage**.
- Fresher data costs more — choose SLAs **per use case**, not one-size-fits-all.


$\text{freshness\_lag} = t_{\text{feature\_updated}} - t_{\text{event\_occurred}}$
$\text{SLA compliance} = \frac{\text{features meeting SLA}}{\text{total features evaluated}} \times 100\%$

| Type | Definition | Example |
|------|------------|---------|
| **Inference latency** | Time from receiving a request to returning a prediction | API responds in 50 ms |
| **Data freshness latency** | Time from a real-world event to that event appearing in features | Transaction at 10:00 AM visible in features at 10:05 AM (5-min micro-batch) |

**Exam Tip:** **Optimising inference latency while ignoring freshness** — a 10 ms API on 2-hour-old features is worse than a 100 ms API on 30-second-old features for fraud.

> **Data Freshness and Latency in Real-Time ML** = Real-time ML systems fail quietly with bad data — they do not crash, they make worse decisions.

---

## Data Completeness and Correctness for ML Pipelines — Missing Shipments

**The Story:** Three dimensions: **freshness**, **completeness**, **correctness**. Issues: missing events, duplicates (at-least-once), out-of-order arrivals, invalid values — cause **silent feature bias** without crashes.

**Key mechanics:**
- Data quality has three dimensions: **freshness**, **completeness**, and **correctness**.
- Common issues: **missing events**, **duplicates** (at-least-once delivery), **out-of-order arrivals**, **invalid values**.
- Issues cause **silent feature bias** — code does not crash, model performance degrades.
- Simple per-window checks: **event counts**, **field distributions**, **null/invalid rates**.
- Compare metrics against **historical baselines** and alert on significant deviation.


$\text{null\_rate} = \frac{\text{records with null/invalid value}}{\text{total records}}$

| Issue | Cause | Impact on ML |
|-------|-------|--------------|
| **Missing events** | Upstream system drops messages, pipeline failure, network partition | Features undercount activity; model sees inactive users as inactive |
| **Duplicates** | Retries, at-least-once delivery semantics | Features overcount; inflated spend, click counts |
| **Out-of-order events** | Network delays, distributed clocks, late arrivals | Windowed features miss or double-count events |
| **Invalid values** | Schema violations, upstream bugs | `NaN`, negative amounts, impossible categories poison training and inference |

**Exam Tip:** **Assuming pipeline success means data correctness** — a job completing without error does not guarantee all events were processed correctly.

> **Data Completeness and Correctness for ML Pipelines** = Data quality has three dimensions: freshness, completeness, and correctness.

---

## Schema Evolution and Data Contracts — Renamed Aisle Signs

**The Story:** **Schema evolution** is inevitable — fields added, removed, renamed, retyped. Unhandled changes cause crashes or **silent misinterpretation**. **Data contracts** define fields, types, allowed values, change policies.

**Key mechanics:**
- **Schema evolution** is inevitable — fields are added, removed, renamed, and retyped over time.
- Unhandled changes cause **runtime crashes** or **silent misinterpretation** — both harm ML systems.
- **Data contracts** define fields, types, allowed values, and change policies between producers and consumers.
- **Backward-compatible changes**: add optional fields with defaults; avoid breaking removals/renames without coordination.
- **Schema registries** enforce contracts at publish time, preventing bad data from entering the pipeline.

| Change Type | Example | Risk |
|-------------|---------|------|
| **Field added** | New `device_type` column in click events | Downstream may ignore it (low risk) or fail if strict |
| **Field removed** | `legacy_id` column deprecated | Downstream jobs break or see nulls |
| **Field renamed** | `user_id` → `customer_id` | Silent misinterpretation if not coordinated |
| **Type changed** | `amount` from `integer` to `float` | Coercion errors or precision loss |

**Exam Tip:** **Treating schema changes as backward-compatible by default** — adding a required field breaks all existing consumers.

> **Schema Evolution and Data Contracts** = Schema evolution is inevitable — fields are added, removed, renamed, and retyped over time.

---

## Applying Data Quality Concepts in Practice — Daily CSV Gate Check

**The Story:** Concrete batch pipeline: daily CSV → ingestion → master dataset → retrain trigger. **Freshness**: days behind? **Completeness/correctness** at ingestion: row counts, null checks, schema validation before append.

**Key mechanics:**
- Apply data quality concepts to a **concrete batch pipeline**: daily CSV → ingestion → master dataset → retrain trigger.
- **Freshness** in batch context: how many days behind is the training data?
- **Completeness/correctness** at ingestion: row counts, null checks, schema validation before append.
- **Log every ingestion** for lineage — which files, row counts, timestamps.
- **Schema contracts** apply even to CSV files — reject incompatible files, do not silently accept.


$N$
$< 0.5 \times$
$> 3 \times$

| Component | Purpose |
|-----------|---------|
| **Daily CSV simulator** | Mimics new data arriving each day (`day_1.csv`, `day_2.csv`, ...) |
| **Ingestion script** | Finds unprocessed day files, appends to master training dataset |
| **Retrain trigger** | Fires based on data volume threshold or days since last retrain |
| **Training function** | Consumes updated master dataset to produce a new model |

**Exam Tip:** **Skipping quality checks in "simple" lab pipelines** — bad habits in labs become production incidents; validate from day one.

> **Applying Data Quality Concepts in Practice** = Apply data quality concepts to a concrete batch pipeline: daily CSV → ingestion → master dataset → retrain trigger.

---

## Simulating Daily Data Arrival for Pipeline Development — Synthetic Daily Deliveries

**The Story:** Simulate daily arrival before building pipelines — predictable test data. Fixed random seed for reproducibility. Schema: `day`, `timestamp`, `customer_id`, `amount`, `label`.

**Key mechanics:**
- **Simulate daily data arrival** before building ingestion pipelines — predictable, repeatable test data.
- Generate base dataset with **fixed random seed** for reproducibility across runs.
- Schema: `day`, `timestamp`, `customer_id`, `amount`, `label` — mimics real event/training data.
- **Split by day** using `groupby` → one CSV per day in a landing zone.
- Realistic timestamps: base day + random minutes throughout the day.

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Days | 5 | Enough to test multi-day ingestion |
| Records per day | 10 | Small enough for inspection, large enough for aggregation |
| Total records | 50 | Manageable for lab exercises |

**Exam Tip:** **No fixed random seed** — non-reproducible data makes debugging ingestion failures nearly impossible.

> **Simulating Daily Data Arrival for Pipeline Development** = Simulate daily data arrival before building ingestion pipelines — predictable, repeatable test data.

---

## Incremental Ingestion: State Management and Idempotency — Append, Don't Rebuild

**The Story:** **Incremental ingestion** processes only new files — production standard. **Full reprocess** does not scale. **State management** via `ingest_state.json` tracking `last_ingested_day`; design for **idempotency**.

**Key mechanics:**
- **Incremental ingestion** processes only new files and appends to master dataset — the production standard.
- **Full reprocess** does not scale; avoid for any dataset beyond trivial size.
- **State management** via externalised state file (`ingest_state.json`) tracks `last_ingested_day`.
- Script is **stateless**; state lives in persistent artifact — survives restarts and machine changes.
- Flow: load state → scan for new files → filter by day > last ingested → append → save → update state.


$N > \text{last\_ingested\_day}$
$O(\text{all data})$
$O(\text{new data})$

| Approach | Description | Scalability |
|----------|-------------|-------------|
| **Full reprocess** | Delete master dataset; rebuild from all daily files | Poor — re-reads years of data for one new day |
| **Incremental ingestion** | Process only new files; append to master dataset | Good — scales linearly with new data volume |

**Exam Tip:** **Updating state before saving master dataset** — crash between state update and save causes permanent data loss.

> **Incremental Ingestion: State Management and Idempotency** = Incremental ingestion processes only new files and appends to master dataset — the production standard.

---

## Training-Serving Skew: Detection and the Feature Store Fix — Skew Caught at the Dock

**The Story:** **Training-serving skew** from two independent feature implementations (30-day vs 7-day). Model trains on one distribution; serving feeds another — no error thrown. **Feature store** with shared logic is the fix.

**Key mechanics:**
- **Training-serving skew**: features at training time differ from features at serving time — silent, devastating bug.
- Most common cause: **two independent implementations** of the same feature logic (e.g., 30-day vs 7-day window).
- Model trains on one distribution; serving feeds another — **no error thrown**, production performance collapses.
- Fix: **single source of truth** — one feature definition reused for offline and online materialisation.
- **Feature stores** (Feast, Tecton, Hopsworks) architecturally eliminate this bug class at scale.

| Path | Feature Function | Window |
|------|------------------|--------|
| Offline (training) | `compute_30day_features()` | 30 days |
| Online (serving) | `compute_7day_features_bug()` | 7 days (accidental) |

**Exam Tip:** **Assuming offline metrics validate serving correctness** — skew is invisible to offline evaluation by definition.

> **Training-Serving Skew: Detection and the Feature Store Fix** = Training-serving skew: features at training time differ from features at serving time — silent, devastating bug.

---

# PART 11: SAFETY LABELS AND COMPLIANCE (Week 11)
*Security, Privacy, and Fairness*

---

## Data and Input Threats in Machine Learning Systems — Poisoned Ingredients

**The Story:** ML security matters in high-stakes decision loops. **Data threats**: poisoning (deliberate), label noise (accidental), skew (structural). **Input threats**: OOD inputs, adversarial probing, API abuse — break reliability at serving time.

**Key mechanics:**
- ML security matters because models sit in high-stakes decision loops and are harder to reason about than rule engines.
- **Data threats:** poisoning (deliberate), label noise (accidental), skew (structural) — all corrupt learned behaviour.
- **Input threats:** OOD inputs, adversarial probing, and API abuse break reliability at serving time.
- Data quality is simultaneously a security, fairness, and accuracy concern.
- Defend inputs with validation, rate limiting, monitoring, and OOD detection.

| Threat type | Intent | Detection signal |
|-------------|--------|------------------|
| Poisoning | Deliberate | Sudden metric shifts; anomalous label clusters |
| Label noise | Accidental | Inter-annotator disagreement; temporal drift |
| Skew | Structural | Group-wise metric gaps; representation imbalance |

**Exam Tip:** Assuming offline metrics on a static test set catch poisoning — poisoned examples may be in the training set, not the holdout.

> **Data and Input Threats in Machine Learning Systems** = ML security matters because models sit in high-stakes decision loops and are harder to reason about than rule engines.

---

## Model and Privacy Threats: Extraction, Leakage, and Over-Exposure — Recipe Theft

**The Story:** Models are IP, information channel, and attack surface. **Model extraction**: query API at scale, train surrogate. **Information leakage**: overfitted outputs reveal training data patterns — limit output detail.

**Key mechanics:**
- Models are sensitive assets: IP, information channel, and attack surface simultaneously.
- **Model extraction:** query API at scale, train surrogate, analyse weaknesses offline.
- **Information leakage:** overfitted or overly detailed outputs reveal training data patterns.
- **Over-sharing:** weights, debug endpoints, verbose errors, and rich responses expand risk.
- Principle: expose only what is needed; prefer coarse outputs and strict access controls.


$(x, \hat{y})$

| Mitigation | Mechanism |
|------------|-----------|
| Rate limiting | Reduces query volume available for surrogate training |
| Output rounding / coarsening | Reduces fidelity of $(x, \hat{y})$ pairs |
| Query monitoring | Detect systematic probing patterns |
| Authentication and billing | Raises cost of large-scale querying |

**Exam Tip:** Equating "model leakage" only with **data leakage** (train-test contamination) — this topic covers **model extraction** and **output-side privacy leakage**.

> **Model and Privacy Threats: Extraction, Leakage, and Over-Exposure** = Models are sensitive assets: IP, information channel, and attack surface simultaneously.

---

## Why Machine Learning Systems Are Attractive Attack Targets — High-Stakes, Opaque Vault

**The Story:** ML controls high-stakes decisions with opaque behaviour. Attackers probe inputs, observe outputs — no architecture knowledge needed. Attack surface spans pipelines, feature stores, batch jobs, APIs, dashboards, logs.

**Key mechanics:**
- ML systems are attractive targets because they control high-stakes decisions with opaque behaviour.
- Attackers probe inputs and observe outputs — they do not need to understand your architecture upfront.
- Attack surface spans data pipelines, feature stores, batch jobs, APIs, dashboards, and logs.
- Immature deployment processes prolong exposure after vulnerabilities are found.
- First-line defences: input validation, rate limiting, least privilege, monitoring, secure defaults.

| Dimension | Rule-based system | ML system |
|-----------|-------------------|-----------|
| Behaviour predictability | High — logic is explicit | Low — learned boundaries |
| Attack surface | Application layer | Data + features + model + infra |
| Probe cost for attacker | Must understand business rules | Query API and observe outputs |
| Fix cycle | Change a rule | Retrain, redeploy, validate |

**Exam Tip:** Assuming security is "the infosec team's problem" after the model is trained.

> **Why Machine Learning Systems Are Attractive Attack Targets** = ML systems are attractive targets because they control high-stakes decisions with opaque behaviour.

---

## PII and Sensitive Attributes in Machine Learning — Customer ID Tags

**The Story:** **PII**: direct identifiers (name, email) and quasi-identifiers (DOB, ZIP, device ID). **Sensitive attributes** (health, financial, protected characteristics) need special handling as features or labels — privacy equals latency and uptime.

**Key mechanics:**
- Privacy is a non-functional requirement equal to latency and uptime in production ML.
- **PII** includes direct identifiers (name, email) and quasi-identifiers (DOB, ZIP, device ID).
- **Sensitive attributes** (health, financial, biometric, protected characteristics) need special handling as features or labels.
- PII hides inside features — user IDs, location traces, and transaction logs are highly identifying.
- Quasi-identifier combinations enable re-identification without any single direct identifier.

| Category | Examples | ML context |
|----------|----------|------------|
| Health | Diagnoses, prescriptions, vitals | Features or labels in triage models |
| Financial | Income, debt, transaction history | Credit and fraud scoring |
| Biometric | Fingerprints, facial geometry | Authentication models |
| Protected characteristics | Race, religion, political views, sexual orientation | Often legally protected; may appear as features or proxies |

**Exam Tip:** Assuming anonymisation of user IDs is sufficient — join keys in separate tables re-identify.

> **PII and Sensitive Attributes in Machine Learning** = Privacy is a non-functional requirement equal to latency and uptime in production ML.

---

## Data Minimisation and Anonymisation Techniques — Collect Less, Mask More

**The Story:** **Data minimisation**: collect only what the task requires. **Masking/redaction**: hide portions. **Aggregation/bucketing**: replace precise values with coarser groups — shrink the attack surface.

**Key mechanics:**
- **Data minimisation:** collect only what the task requires; reduces attack surface and compliance burden.
- **Masking/redaction:** hide portions of sensitive fields (last four digits).
- **Aggregation/bucketing:** replace precise values with coarser groups.
- **Pseudonymisation:** swap identifiers for internal IDs; mapping stored separately and restricted.
- Full anonymity is hard — ML needs detail; external linkage and model memorisation undermine guarantees.


$(lat, lon)$
$k = 5$

| Question | Alternative when answer is "no" |
|----------|--------------------------------|
| Do we need raw identifiers? | Internal surrogate ID |
| Can we use aggregated features? | Age band instead of exact age |
| Can we drop data after a window? | Archive or delete beyond retention period |
| Do we need full transaction history? | Rolling 90-day summary statistics |

**Exam Tip:** Treating pseudonymisation as equivalent to anonymisation — it is reversible with the mapping.

> **Data Minimisation and Anonymisation Techniques** = Data minimisation: collect only what the task requires; reduces attack surface and compliance burden.

---

## Role-Based Access Control and Data Governance for ML — Key Cards by Role

**The Story:** **RBAC**: least-privilege by role — data engineer, model engineer, analyst see different data. Separate dev/staging/production; avoid raw production data in dev. **Feature-level policies** restrict sensitive features per role.

**Key mechanics:**
- RBAC assigns least-privilege permissions by role — data engineer, model engineer, and analyst need different access.
- Separate dev, staging, and production environments; avoid raw production data in development.
- Enforce **feature-level policies** — some features restricted or aggregated per role and use case.
- **Audit logs** track data access, model deployments, and config changes.
- **Data lineage** documents feature provenance for debugging and privacy justification.

| Role | Typical needs | Raw PII access |
|------|---------------|----------------|
| Data engineer | Pipeline construction, ETL | Often yes — but scoped to pipeline stage |
| Model engineer | Feature experimentation, training | Prefer pseudonymised or sampled data |
| Business analyst | Dashboards, aggregate reports | Aggregated metrics only |
| Auditor / compliance | Investigation, policy verification | Read-only, time-bounded, fully logged |

**Exam Tip:** Granting all engineers production database access "for convenience."

> **Role-Based Access Control and Data Governance for ML** = RBAC assigns least-privilege permissions by role — data engineer, model engineer, and analyst need different access.

---

## Fairness and Bias: Evaluating Models Across Groups — Averages Hide Empty Shelves

**The Story:** High overall accuracy can mask systematic harm to specific groups. **Group comparison**: same model, same metrics, different slices — core fairness check. Slice, compute per group, compare.

**Key mechanics:**
- High overall accuracy can mask systematic harm to specific groups.
- **Group comparison:** same model, same metrics, different group slices — the core fairness check.
- Choose a group attribute, slice evaluation data, compute metrics per group, compare.
- **FP and FN rates** often matter more than accuracy; domain determines which error is costlier.
- Check calibration: does score 0.8 mean the same thing for every group?


$\text{FPR} = \frac{FP}{FP + TN} \quad \text{(false positive rate)}$
$\text{FNR} = \frac{FN}{FN + TP} \quad \text{(false negative rate)}$
$\text{Recall} = \frac{TP}{TP + FN} = 1 - \text{FNR}$

| Group | Accuracy | Population share |
|-------|----------|------------------|
| Group A | 92% | 70% |
| Group B | 83% | 30% |
| **Overall** | **~90%** | 100% |

**Exam Tip:** Reporting only overall accuracy in stakeholder presentations.

> **Fairness and Bias: Evaluating Models Across Groups** = High overall accuracy can mask systematic harm to specific groups.

---

## Practical Fairness Questions and Visualisation — Four Fairness Audits

**The Story:** Key questions: FN disparity, subpopulation drop, calibration consistency, threshold impact. **False negative disparity** = denied opportunities. **Calibration**: score 0.8 should mean ~80% positive rate in every group.

**Key mechanics:**
- Four key questions: FN disparity, subpopulation performance drop, calibration consistency, threshold impact.
- **False negative disparity** often maps to denied opportunities (lending, hiring, screening).
- **Calibration:** score 0.8 should mean ~80% positive rate in every group.
- Use bar charts, grouped error-rate bars, calibration plots, and delta tables.
- Highlight gaps exceeding chosen thresholds to focus attention.

| Question | Primary metric | Reveals |
|----------|----------------|---------|
| FN disparity | Recall, FNR | Denied opportunities, missed detections |
| Subpopulation drop | Accuracy, AUC per slice | Model simply works worse for some groups |
| Calibration | Reliability diagram, Brier score | Score interpretability across groups |
| Threshold impact | Outcome rates at fixed threshold | Policy-level disparate impact |

**Exam Tip:** Showing only accuracy bars without FP/FN breakdown — hides the direction of harm.

> **Practical Fairness Questions and Visualisation** = Four key questions: FN disparity, subpopulation performance drop, calibration consistency, threshold impact.

---

## Fairness Limitations, Trade-offs, and the Model Engineer's Role — No Universal Fairness Scale

**The Story:** No single fairness metric — equal accuracy, FPR, FNR, calibration can conflict. Improving one may cost accuracy, latency, complexity. Acceptability depends on domain, stakes, policy, regulation.

**Key mechanics:**
- No single universal fairness metric — equal accuracy, FPR, FNR, and calibration can conflict.
- Improving one fairness measure may cost accuracy, latency, or complexity.
- Whether a gap is acceptable depends on domain, stakes, policy, and regulation.
- Model engineer role: make metrics easy, flag gaps early, document decisions, collaborate.
- Fairness numbers are inputs to human decisions — not automated verdicts.

| Fairness criterion | What it demands | Example tension |
|--------------------|-----------------|-----------------|
| Equal accuracy | Same error rate across groups | May conflict with base-rate differences |
| Equal false positive rate | Same FP rate across groups | Conflicts with equal recall when base rates differ |
| Equal false negative rate | Same FN rate across groups | Conflicts with equal precision |
| Equal calibration | Same score-to-probability mapping | Conflicts with equal FPR and FNR simultaneously |

**Exam Tip:** Claiming a model is "fair" because one metric looks acceptable — other definitions may be violated.

> **Fairness Limitations, Trade-offs, and the Model Engineer's Role** = No single universal fairness metric — equal accuracy, FPR, FNR, and calibration can conflict.

---

## Explainability: What It Is, Why It Matters, and Its Limits — Why This Recommendation?

**The Story:** **Explainability**: local (one case — users, support, appeals) and global (population — review, risk, feature design). Makes model behaviour understandable; has limits with complex models.

**Key mechanics:**
- Explainability makes model behaviour understandable for humans — local (one case) and global (population).
- **Local:** why this prediction — for users, support, appeals.
- **Global:** what drives the model generally — for review, risk analysis, feature design.
- Invest in explainability for debugging, user trust, and regulatory review.
- Popular methods are **approximations** — they can oversimplify or mislead.

| Type | Question answered | Audience |
|------|-------------------|----------|
| **Local** | Why this prediction for this specific case? | End user, support, appeals |
| **Global** | What features drive behaviour in general? | Model reviewers, risk analysts, engineers |

**Exam Tip:** Treating SHAP values as ground truth rather than an approximation.

> **Explainability: What It Is, Why It Matters, and Its Limits** = Explainability makes model behaviour understandable for humans — local (one case) and global (population).

---

## Audit Trails Across the ML Pipeline — Paper Trail for Every Batch

**The Story:** **Audit trails** reconstruct lifecycle events. Per-prediction: model version, feature version, score, threshold, request ID. Training: data snapshot, hyperparameters, group-wise metrics.

**Key mechanics:**
- Audit trails reconstruct what happened across the ML lifecycle.
- Per-prediction logs: model version, feature version, score, threshold, request ID, optional explanation.
- Training logs: data snapshot, hyperparameters, metrics (including group-wise).
- Rollout logs: promotion approval, rollout/rollback events.
- Do not log raw PII — apply minimisation to audit records themselves.

| Field category | What to log | Example |
|----------------|-------------|---------|
| **Model metadata** | Name, version, hash, config flags | `credit-risk-v2.1`, `hash:abc123` |
| **Data / feature context** | Key input fields, feature store version, timestamp | `features_v3.2`, `2025-06-05T14:32:01Z` |
| **Decision details** | Prediction, score, threshold applied | `score: 0.73`, `threshold: 0.65`, `decision: deny` |
| **Explanation summary** | Optional short local explanation | `top drivers: income, delinquency` |

**Exam Tip:** Logging only predictions without model version — impossible to reproduce the decision later.

> **Audit Trails Across the ML Pipeline** = Audit trails reconstruct what happened across the ML lifecycle.

---

## Regulatory Expectations and Designing for Auditability — Compliance by Design

**The Story:** Regulated domains: purpose limitation, non-discrimination, explainability, record-keeping. Design for auditability at **design time** — versioning, structured logging, fairness records are core requirements.

**Key mechanics:**
- Regulated domains share expectations: purpose limitation, non-discrimination, explainability, record-keeping.
- Design for auditability at **design time** — not after incidents.
- Model versioning, structured logging, and fairness records are core requirements.
- System must answer: which model, what data, what checks passed, who approved.
- Write an **investigation playbook** before you need it.

| Expectation | What it means in practice |
|-------------|---------------------------|
| **Purpose limitation** | Use data only for declared, consented purposes |
| **Non-discrimination** | Avoid unjustified bias or harmful disparate impact |
| **Explainability** | Provide understandable reasons to non-technical people |
| **Record-keeping** | Maintain records of models used, evaluations performed, and approvals granted |

**Exam Tip:** Treating regulatory compliance as a legal-team-only concern — engineering design determines feasibility.

> **Regulatory Expectations and Designing for Auditability** = Regulated domains share expectations: purpose limitation, non-discrimination, explainability, record-keeping.

---

## Segmented Evaluation: Performance by Group — Slice the Receipts

**The Story:** **Segmented evaluation**: accuracy, precision, recall, AUC per group independently. Workflow: predict → overall baseline → loop groups → filter → compute → compare.

**Key mechanics:**
- High global accuracy can hide poor performance for specific groups.
- **Segmented evaluation:** compute accuracy, precision, recall, AUC per group independently.
- Workflow: predict → overall baseline → loop groups → filter → compute metrics → compare.
- Bar charts make disparities immediately visible.
- Recall gaps often indicate denied opportunities (lending) or missed detections (fraud).

| View | What you see | Risk |
|------|--------------|------|
| Global accuracy = 95% | One reassuring number | Hidden group disparities |
| Group A accuracy = 97% | Strong performance | — |
| Group B accuracy = 88% | Weaker performance | 9 pp gap invisible globally |

**Exam Tip:** Reporting only overall metrics to stakeholders for high-impact models.

> **Segmented Evaluation: Performance by Group** = High global accuracy can hide poor performance for specific groups.

---

## Automated Fairness Checks: Policy, Thresholds, and Pass/Fail Logic — Automated Policy Gate

**The Story:** Automate fairness: encode policy thresholds as pass/fail in **CI/CD**. Typical: max recall difference and max FPR difference between groups. **Recall** for opportunity models; **FPR** for punitive models (fraud).

**Key mechanics:**
- Automate fairness by encoding policy thresholds as pass/fail rules in CI/CD.
- Typical constraints: max recall difference and max FPR difference between groups.
- **Recall** critical for opportunity models (lending); **FPR** critical for punitive models (fraud).
- Compute confusion matrix per group → derive FPR, recall → compute absolute deltas.
- FAIL triggers human investigation — not automatic model rejection.


$1 - \text{FNR}$
$\text{FPR} = \frac{FP}{FP + TN}$
$\text{Recall} = \frac{TP}{TP + FN}$

| Domain | Example threshold | Rationale |
|--------|-------------------|-----------|
| High-stakes medical model | 1% max gap | Patient safety |
| Loan approval | 5–10% max gap | Regulatory scrutiny, opportunity impact |
| Movie recommendation | 10%+ may be acceptable | Low individual harm |

**Exam Tip:** Treating 10% as a universal threshold — always context-dependent.

> **Automated Fairness Checks: Policy, Thresholds, and Pass/Fail Logic** = Automate fairness by encoding policy thresholds as pass/fail rules in CI/CD.

---

## Logging Fairness Metrics for Audit and Monitoring — Permanent Fairness Ledger

**The Story:** Console pass/fail is ephemeral — governance needs persistent logs. Audit record: metadata, group metrics, deltas, thresholds, verdict. **JSONL**: one JSON object per line; append-only, streamable.

**Key mechanics:**
- Console pass/fail is ephemeral — governance requires persistent structured logs.
- A fairness audit record includes metadata, full group metrics, deltas, thresholds, and verdict.
- **JSONL format:** one JSON object per line; append-only, streamable, language-agnostic.
- Each model evaluation appends a line — building chronological fairness history.
- Enables trend analysis: is fairness improving or worsening over model versions?

| Field | Purpose |
|-------|---------|
| `model_version` | Which model was evaluated |
| `data_version` | Which dataset the evaluation ran against |
| `timestamp` | When the evaluation occurred |
| `group_metrics` | Full per-group breakdown (accuracy, recall, FPR, etc.) |

**Exam Tip:** Printing fairness results to stdout without persisting — no system of record.

> **Logging Fairness Metrics for Audit and Monitoring** = Console pass/fail is ephemeral — governance requires persistent structured logs.

---

# PART 12: MULTI-PRODUCT STORES (Week 12)
*Routing, Sharding, and Multi-Model Serving*

---

## Why Multi-Model Systems Exist — One Product vs Full Catalogue

**The Story:** Multi-model systems arise from localisation, versioning, task specialisation, scale. Production runs many models side by side. **Routing** = one model per request; **ensembles** = multiple models, combined output.

**Key mechanics:**
- Multi-model systems arise from localization, versioning, task specialisation, and scale
- Typical production platforms run many models side by side, not one
- **Routing** = one model per request; **ensembles** = multiple models, combined output
- Canary, A/B, and champion–challenger are key multi-version patterns
- Specialist models (fraud, credit, churn, recs) outperform generalists on narrow tasks

| Segment | Model strategy |
|---------|----------------|
| India users | Model trained on local transaction patterns |
| EU users | Model compliant with GDPR, trained on EU data |
| Enterprise tier | Higher-accuracy, higher-latency model |
| Free tier | Lightweight, cost-optimised model |

**Exam Tip:** Multi-model means you need a learned router from day one. **Reality**: Start with simple rule-based routing (country, language, product). Learned routing is an advanced optimisation.

> **Why Multi-Model Systems Exist** = Multi-model systems arise from localization, versioning, task specialisation, and scale

---

## Routing Strategies: Rule-Based and Learned Routers — Aisle Signs vs Smart Guide

**The Story:** **Rule-based routing**: explicit conditions (region, language, tier) → model endpoint — explainable but sprawl-prone. **Learned routing**: small model predicts best expert per input — captures patterns rules miss.

**Key mechanics:**
- **Rule-based routing** maps explicit conditions (region, language, tier) to model endpoints
- Rules are explainable and fast to build but suffer from sprawl and missed patterns
- **Learned routing** trains a small model to predict the best expert per input
- Learned routers appear in MoE architectures and cost-aware serving systems
- Start with rules; graduate to learned routing when complexity is justified

| Dimension | Example rule |
|-----------|-------------|
| Country / region | India → `model_IN`, Europe → `model_EU`, else → `model_global` |
| Language | `lang=hi` → Hindi model, `lang=en` → English model |
| Product / tenant | Product A → `model_a`, Product B → `model_b` |
| Risk band / tier | High-value customers → accurate (slow) model; low-risk segment → lightweight model |

**Exam Tip:** Learned routing is always better than rules. **Reality**: Rules are simpler, explainable, and sufficient for most early-stage systems. Learned routing adds complexity that must be justified.

> **Routing Strategies: Rule-Based and Learned Routers** = Rule-based routing maps explicit conditions (region, language, tier) to model endpoints

---

## Fallback Models, Ensembles, and the Accuracy–Cost Trade-Off — Backup Supplier and Blend

**The Story:** **Fallback routing**: uncertainty, OOD, service failures → safe alternative. **Ensembles**: multiple models combined via averaging, voting, stacking — accuracy and robustness when base models are diverse.

**Key mechanics:**
- **Fallback routing** handles uncertainty, OOD inputs, and service failures with safe alternatives
- **Ensembles** call multiple models and combine via averaging, voting, or stacking
- Ensembles improve accuracy and robustness when base models are diverse
- Trade-off: ensembles increase latency, cost, and operational complexity
- Start with rule-based routing; keep model count manageable; measure per-segment performance


$N$
$\hat{p} = \frac{1}{N} \sum_{i=1}^{N} p_i$
$N\times$

| Trigger | Example fallback |
|---------|-----------------|
| Low confidence / high uncertainty | Simpler, more conservative model |
| Out-of-distribution (OOD) input | Rule-based system or default deny |
| Primary service down / timeout | Backup model or cached response |
| Incident / degraded mode | Manual review queue or safe default |

**Exam Tip:** Fallback models should be more accurate than the primary. **Reality**: Fallbacks prioritise **safety and availability** — they may be simpler or more conservative, not more accurate.

> **Fallback Models, Ensembles, and the Accuracy–Cost Trade-Off** = Fallback routing handles uncertainty, OOD inputs, and service failures with safe alternatives

---

## Scaling Inference: Sharding and Replication — More Counters, More Aisles

**The Story:** Single instance hits latency, timeout, QPS ceilings. **Replication** = identical copies behind load balancer. **Sharding** = divide traffic/data into subsets with dedicated resources.

**Key mechanics:**
- Single-instance serving hits latency, timeout, and QPS ceilings
- **Replication** = multiple identical model copies behind a load balancer
- **Sharding** = divide traffic/data into subsets, each with dedicated resources
- Hash sharding: $\text{shard} = \text{hash}(\text{id}) \bmod N$ for even distribution
- Combine both: shards for partitioning, replicas within shards for throughput and fault tolerance


$N$
$N\times$
$\text{shard} = \text{hash}(\text{user\_id}) \bmod N$

| Primitive | What it does | Analogy |
|-----------|-------------|---------|
| **Replication** | Multiple copies of the **same** model | More checkout counters |
| **Sharding** | Divide traffic/data into **subsets**, each handled by a dedicated subset of servers | Separate departments per region |

**Exam Tip:** Replication and sharding are interchangeable. **Reality**: Replication spreads identical work; sharding partitions different work. They solve different problems and are often combined.

> **Scaling Inference: Sharding and Replication** = Single-instance serving hits latency, timeout, and QPS ceilings

---

## Caching Model Results and Embeddings — Memorised Answers

**The Story:** **Output caching** stores final predictions; **embedding caching** stores reusable vectors. Cache keys must include content/ID + **model version** + **preprocessing version** — stale cache is silent skew.

**Key mechanics:**
- Inference caching skips expensive model calls when recent results exist
- **Output caching** stores final predictions; **embedding caching** stores reusable vectors
- Cache keys must include content/ID + model version + preprocessing version
- Three invalidation strategies: TTL, version-based (new keys), event-based (data changes)
- Always trade off freshness vs performance per use case


$f(x)$
$x$
$\text{valid} \iff (t_{\text{now}} - t_{\text{cached}}) < \text{TTL}$

| Benefit | Impact |
|---------|--------|
| Latency | Cache reads are microseconds vs milliseconds for inference |
| Cost | Fewer GPU/CPU inference calls |
| Throughput | Frees model capacity for cache misses |

**Exam Tip:** Cache keys need only the input content. **Reality**: Must include **model version** and **preprocessing version** to avoid serving stale artefacts after upgrades.

> **Caching Model Results and Embeddings** = Inference caching skips expensive model calls when recent results exist

---

## Combining Routing, Sharding, and Caching at Scale — Front Desk Composition

**The Story:** Production stack: cache → router → shard → replicas → model. Cache serves repeats without inference. Router selects shard/model by region, language, tenant, experiment.

**Key mechanics:**
- Production inference stacks compose: cache → router → shard → replicas → model
- Cache sits in front to serve repeated requests without inference
- Router selects shard/model by region, language, tenant, or experiment
- Within each shard, replicas handle throughput and fault tolerance
- Total instances = shards $\times$ replicas per shard


$S$
$R$
$\text{total instances} = S \times R$

| Step | Component | Action |
|------|-----------|--------|
| 1 | Cache | Check for existing result; return on hit |
| 2 | Router | Select shard/model based on request attributes |
| 3 | Shard | Route to correct partition |
| 4 | Load balancer | Distribute across replicas within shard |

**Exam Tip:** Add caching last as an optimisation. **Reality**: Cache layer design (key schema, TTL) should be planned **with** routing and sharding, not bolted on.

> **Combining Routing, Sharding, and Caching at Scale** = Production inference stacks compose: cache → router → shard → replicas → model

---

## Integrated Architecture: Routing, Sharding, Replication, and Caching — Integrated Store Layout

**The Story:** Compose routing + sharding + replication + caching. Router selects shard/model; replicas handle load within shard. Cache in front with versioned keys for outputs and embeddings.

**Key mechanics:**
- Production ML serving composes routing + sharding + replication + caching
- Router selects shard/model; replicas handle load within each shard
- Cache sits in front with versioned keys for outputs and embeddings
- Together: low latency, high throughput, predictable SLOs, controlled cost
- Same pattern extends to multi-tenant platforms and RAG systems

| Component | Responsibility |
|-----------|---------------|
| **Router** | Decide which shard or model variant handles this request |
| **Shard** | Partition traffic/data; may host specialised models |
| **Replicas** | Multiple instances within a shard for throughput and reliability |
| **Cache** | Store outputs and embeddings with versioned keys for fast reuse |

**Exam Tip:** Caching replaces the need for replicas. **Reality**: Cache helps on hits; misses still need replica capacity. Both are necessary.

> **Integrated Architecture: Routing, Sharding, Replication, and Caching** = Production ML serving composes routing + sharding + replication + caching

---

## Multi-Tenant ML Platforms and the Noisy Neighbour Problem — Shared Mall, Loud Tenant

**The Story:** A **tenant** is a logical customer (team, BU, external client). Multi-tenancy shares infra for efficiency but needs isolation. **Noisy neighbour**: one tenant over-consumes shared resources, degrading others.

**Key mechanics:**
- A **tenant** is a logical customer of the ML platform (team, business unit, external client)
- Multi-tenancy shares infrastructure for efficiency but requires isolation for safety
- The **noisy neighbour problem**: one tenant over-consumes shared resources, degrading others
- Symptoms: latency spikes, queue buildup, timeouts, broken SLOs for unrelated tenants
- Isolation strategies span logical, resource, data, and observability layers

| Tenant type | Example |
|-------------|---------|
| Internal product team | Search, recommendations, fraud detection |
| Business unit | Retail, enterprise, small business |
| External customer | SaaS ML platform subscriber |

**Exam Tip:** Multi-tenancy only applies to external SaaS products. **Reality**: Internal platforms with multiple product teams are multi-tenant too.

> **Multi-Tenant ML Platforms and the Noisy Neighbour Problem** = A tenant is a logical customer of the ML platform (team, business unit, external client)

---

## Per-Tenant SLOs and Isolation Strategy Overview — VIP vs Standard Service

**The Story:** **SLOs** per tenant: latency, availability, error rate. Not all tenants equal — VIP vs internal vs experimental tiers. SLOs drive capacity, isolation design, incident prioritisation.

**Key mechanics:**
- **SLOs** are measurable targets (latency, availability, error rate) per tenant
- Not all tenants get the same SLOs — VIP vs internal vs experimental tiers
- SLOs drive capacity planning, isolation design, and incident prioritisation
- Three isolation layers: logical (namespaces), resource (quotas), data (access controls)
- Principle: shared platform with clear per-tenant boundaries

| Metric type | Example SLO |
|-------------|------------|
| Latency | P95 inference latency < 150 ms |
| Availability | 99.9% uptime over 30 days |
| Error rate | < 0.1% of requests return 5xx |

**Exam Tip:** One global SLO covers all tenants. **Reality**: Different tenants have different business criticality. Per-tenant SLOs enable fair prioritisation.

> **Per-Tenant SLOs and Isolation Strategy Overview** = SLOs are measurable targets (latency, availability, error rate) per tenant

---

## Blast Radius, Resource Quotas, and Data Isolation — Firewalls Between Tenants

**The Story:** **Blast radius** limited via namespaces and separate clusters. **Resource quotas** cap CPU, GPU, memory, concurrency per tenant. **Priority classes** ensure high-priority tenants get resources under pressure.

**Key mechanics:**
- **Blast radius** = how far an incident spreads; limit it via namespaces and separate clusters
- **Resource quotas** cap CPU, GPU, memory, and concurrency per tenant
- **Priority classes** ensure high-priority tenants get resources first under pressure
- **Data isolation**: separate storage + RBAC/IAM per tenant
- **Logging isolation**: per-tenant log streams and metric namespaces

| Mechanism | What it isolates |
|-----------|-----------------|
| Kubernetes namespace | Deployments, services, config maps, secrets |
| Cloud project/account | IAM, billing, resource quotas |
| Separate deployment pipeline | CI/CD scope per tenant |

**Exam Tip:** Namespaces alone prevent noisy neighbours. **Reality**: Namespaces isolate configuration, not resource consumption. **Quotas** are required.

> **Blast Radius, Resource Quotas, and Data Isolation** = Blast radius = how far an incident spreads; limit it via namespaces and separate clusters

---

## Embeddings, Vector Similarity, and Vector Databases — Semantic Shelf Tags

**The Story:** An **embedding** is a dense vector capturing semantic meaning; similar items are nearby. **Vector similarity search**: embed query → top-$K$ neighbours via cosine/dot/Euclidean. Use cases: semantic search, recommendations, dedup.

**Key mechanics:**
- An **embedding** is a dense vector capturing semantic meaning; similar items are nearby in vector space
- **Vector similarity search**: embed query → find top-$K$ nearest neighbours via cosine, dot product, or Euclidean distance
- Use cases: semantic search, recommendations, deduplication, clustering, anomaly detection
- A **vector database** stores (vector, metadata) pairs and provides fast similarity search APIs
- Vector DBs use specialised indexes (ANN) to scale to millions/billions of vectors


$K$
$\cos(\theta) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}$
$\mathbf{a} \cdot \mathbf{b} = \sum_i a_i b_i$

| Metric | Formula (intuition) | Best for |
|--------|-------------------|----------|
| **Cosine similarity** | $\cos(\theta) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}$ | Normalised vectors; direction matters, not magnitude |
| **Dot product** | $\mathbf{a} \cdot \mathbf{b} = \sum_i a_i b_i$ | When magnitude carries information (e.g., relevance score) |
| **Euclidean distance** | $\|\mathbf{a} - \mathbf{b}\|_2$ | Absolute distance in space; smaller = more similar |

**Exam Tip:** Embeddings are just feature vectors from tabular ML. **Reality**: Embeddings are **dense semantic representations** learned by neural models. Their geometry encodes meaning, not just raw features.

> **Embeddings, Vector Similarity, and Vector Databases** = An embedding is a dense vector capturing semantic meaning; similar items are nearby in vector space

---

## Approximate Nearest Neighbour (ANN) Search — Good Enough, Fast Enough

**The Story:** Exact NN search does not scale to billions. **ANN** trades slight accuracy for dramatic speed — core trade-off: **latency vs recall@K**. HNSW, IVF, LSH are common index structures.

**Key mechanics:**
- **Exact NN search** does not scale to millions/billions of vectors
- **ANN** trades slight accuracy loss for dramatic speed improvement
- Core trade-off: **latency vs recall@K** (how many true neighbours are recovered)
- ANN indexes (HNSW, IVF, LSH, PQ) use pre-computed structures to avoid brute force
- Tunable knobs: index type, probes, search depth — adjust per quality/latency requirements


$K$
$\text{ANN: } \text{speed} \uparrow, \quad \text{exactness} \downarrow \text{ (slightly)}$
$\text{Higher recall} \iff \text{more probes/deeper search} \iff \text{higher latency}$

| Collection size | Exact search latency | Production viable? |
|----------------|---------------------|-------------------|
| 10,000 vectors | ~10 ms | Yes |
| 1 million vectors | ~1–5 seconds | Borderline |
| 100 million+ vectors | Minutes | No |

**Exam Tip:** ANN always returns wrong results. **Reality**: ANN returns **approximately correct** results. At 95% recall@10, you miss 0.5 of the true top-10 on average — often acceptable.

> **Approximate Nearest Neighbour (ANN) Search** = Exact NN search does not scale to millions/billions of vectors

---

## RAG Pipelines as Multi-Model Systems — Ask the Warehouse, Then Answer

**The Story:** **RAG**: embed query → retrieve top-$K$ docs → optional rerank → generate with context. Multi-model by design: embedding model + vector DB + reranker + generator. Apply sharding, caching, routing.

**Key mechanics:**
- **RAG** = embed query → retrieve top-$K$ docs → optional rerank → generate answer with context
- RAG is **multi-model by design**: embedding model + vector DB + reranker + generator
- Apply sharding (per domain/tenant), caching (embeddings, retrieval, answers), and routing
- Production RAG is a multi-model, multi-tenant, sharded, cached system
- Real-world uses: Q&A, support bots, recommendations, code search, enterprise knowledge


$K$
$\text{Production ML} = \text{Models} + \text{Data} + \text{Retrieval Infrastructure}$

| Model role | Function | Example |
|-----------|----------|---------|
| Embedding model | Text → vector | `text-embedding-3-small`, BGE, E5 |
| Vector database | Store + search vectors | Pinecone, Milvus, pgvector |
| Reranker model | Refine retrieval order | Cross-encoder, Cohere Rerank |
| Generator model | Produce final text | GPT-4, Llama, Mistral |

**Exam Tip:** RAG replaces the need for a good LLM. **Reality**: RAG **augments** the LLM with external knowledge. A weak generator still produces poor answers even with perfect retrieval.

> **RAG Pipelines as Multi-Model Systems** = RAG = embed query → retrieve top-$K$ docs → optional rerank → generate answer with context

---

## Building a File-Based Model Registry — Versioned Stock Room

**The Story:** **Model registry**: single source of truth for all versions. Convention: each version in own folder with `model.pkl` + `metrics.json` — self-describing artefacts.

**Key mechanics:**
- A **model registry** is the single source of truth for all trained model versions
- Convention: each version in its own folder with `model.pkl` + `metrics.json`
- Self-describing artefacts: metrics stored alongside the model file
- Registration agent scans version folders and writes `registry.json` catalogue
- Registry decouples model knowledge from training, promotion, and serving

| File | Purpose |
|------|---------|
| `model.pkl` (or `.onnx`, `.pt`, etc.) | The serialised model artefact |
| `metrics.json` | Key performance indicators from evaluation |

**Exam Tip:** A registry stores model files itself. **Reality**: The registry stores **metadata and paths** to artefacts. Model files live in versioned folders.

> **Building a File-Based Model Registry** = A model registry is the single source of truth for all trained model versions

---

## Model Promotion and `current_best.json` — The Champion Pointer

**The Story:** **Promotion** picks current best for production via centralised policy (e.g., highest accuracy). **`current_best.json`** is the single file serving reads — rich metadata for audit.

**Key mechanics:**
- **Promotion** decides which registry candidate is the current best for production
- Promotion policy is centralised in one function (e.g., highest accuracy wins)
- **`current_best.json`** is the single file the serving layer reads — rich metadata for audit
- Decoupling: registry (catalogue) → promotion (decision) → serving (execution)
- Rollback = edit `current_best.json` to previous version + restart service


$0.7 \times \text{accuracy} + 0.3 \times (1 - \text{log\_loss})$

| Component | Knows about | Does NOT know about |
|-----------|------------|-------------------|
| Registry | All versions, all metrics | Which is "best" |
| Promotion script | Registry + policy rules | How to serve predictions |
| Serving layer | `current_best.json` only | Training, registry, promotion logic |

**Exam Tip:** Promotion and deployment are the same thing. **Reality**: Promotion selects the best model; deployment loads it into the serving environment. They are sequential but distinct steps.

> **Model Promotion and `current_best.json`** = Promotion decides which registry candidate is the current best for production

---

## Dynamic Model Serving with `current_best.json` — Pointer, Not Path

**The Story:** Serving reads **only** `current_best.json` — decoupled from training/promotion. Load once at startup via FastAPI lifespan. Endpoints: metadata (`GET /`) and predict (`POST /predict`).

**Key mechanics:**
- Serving service reads **only** `current_best.json` — decoupled from training and promotion
- Load model once at startup via FastAPI lifespan events
- Two endpoints: metadata (`GET /`) and predict (`POST /predict`)
- Every prediction response includes `model_version` for traceability
- Rollback = edit `current_best.json` + restart — no code changes

| Extension | How |
|-----------|-----|
| Multiple models per service | `current_best.json` lists models by task: `{ "fraud": "v3", "credit": "v1" }` |
| Per-tenant models | Router reads tenant-specific `current_best` file |
| Hot reload | Watch `current_best.json` for changes; reload without restart |
| A/B testing | Router reads experiment config; serving layer loads multiple models |

**Exam Tip:** Load the model on every request for freshness. **Reality**: Model loading takes seconds. Load once at startup via lifespan events; restart to pick up new versions.

> **Dynamic Model Serving with `current_best.json`** = Serving service reads only current_best.json — decoupled from training and promotion

---

# PART 13: THE FULL RETAIL CHAIN (Week 13)
*System Design from Factory to Shelf*

---

## Recommendation System: Problem Definition and Requirements — Ten Items, 200 Milliseconds

**The Story:** Carousel shows ~10 personalised products within **100–200 ms**. Requirements: personalisation, freshness, low latency, business constraints, diversity. **Data layer**: click streams → data lake via **streaming pipelines**.

**Key mechanics:**
- Carousel shows ~10 personalised products within **100–200 ms**
- Requirements: personalisation, freshness, low latency, business constraints, diversity
- **Data layer**: click streams and transactions → data lake via streaming pipelines
- **Feature layer**: user/item features via feature store (offline training + online serving)
- **Two-stage model**: candidate generation (recall, scale) → ranking (precision, business trade-offs)


$N$
$\text{Total latency} \approx T_{\text{feature lookup}} + T_{\text{candidate gen}} + T_{\text{ranking}} + T_{\text{post-processing}}$

| Requirement | Description | Example |
|-------------|-------------|---------|
| **Personalisation** | Use individual behaviour history | Past views, clicks, purchases shape recommendations |
| **Freshness** | React quickly to recent activity | User clicks a new category → carousel updates within minutes |
| **Low latency** | No perceptible delay | Entire recommendation call completes in **100–200 ms** |
| **Business constraints** | Honour inventory and marketing rules | Only in-stock items; highlight promotions; avoid 10 near-identical products |

**Exam Tip:** **Optimising ranking without candidate generation** — you cannot score 10M items per request; two-stage architecture is mandatory at scale.

> **Recommendation System: Problem Definition and Requirements** = Carousel shows ~10 personalised products within 100–200 ms

---

## Recommendation Systems: The Data Layer — Behavioural and Transactional Streams

**The Story:** Data layer ingests **behavioural events** (views, clicks) and **transactional events** (cart, purchases, returns) via **Kafka/Kinesis** into **data lakes** (Parquet/ORC). **Aggregated tables** feed feature pipelines and training.

**Key mechanics:**
- Data layer ingests **behavioural events** (views, clicks) and **transactional events** (cart, purchases, returns)
- Events flow through **streaming pipelines** (Kafka/Kinesis) into **data lakes/warehouses** (Parquet/ORC)
- **Aggregated tables** (daily user/item summaries) feed feature pipelines and training jobs
- Data layer owns **freshness, completeness, and schema** quality contracts
- Everything upstream — features, models, serving — depends on reliable data ingestion

| Event Type | Signal Captured | Use in Recommendations |
|------------|-----------------|------------------------|
| Page views | Browsing intent, category interest | Category affinity features |
| Clicks | Active engagement | Short-term preference signals |
| Scrolls | Attention depth | Engagement quality metrics |
| Search queries | Explicit intent | Query-document matching |

**Exam Tip:** **Skipping aggregation** — models cannot train on raw click-stream events at scale; aggregated entity-time tables are required.

> **Recommendation Systems: The Data Layer** = Data layer ingests behavioural events (views, clicks) and transactional events (cart, purchases, returns)

---

## Recommendation Systems: Feature Store, Candidate Generation, and Ranking — Candidates Then Rank

**The Story:** Features span **user**, **item**, **context**. **Feature store** defines once for offline/online — prevents skew. **Candidate generation**: millions → hundreds via heuristics, embeddings, or two-tower **ANN** (recall-focused).

**Key mechanics:**
- Features span **user** (affinity, recency, spend), **item** (attributes, content, popularity), and **context** (time, device, page)
- **Feature store** defines features once for offline training and online serving — prevents training-serving skew
- **Candidate generation**: millions → hundreds via heuristics, embeddings, or two-tower ANN search (recall-focused)
- **Ranking model**: hundreds → top $N$ via GBDT/neural ranker + business rules (precision-focused)
- **Online path**: gateway → feature lookup → candidate gen → ranking → post-processing → UI (all under 200 ms)


$\mathbf{x} = [x_{\text{user}}, x_{\text{item}}, x_{\text{context}}]$
$f_u$
$f_i$

| Category | Examples | Computation |
|----------|----------|-------------|
| Recency / frequency | Clicks in last 7 days, days since last purchase | Sliding window aggregation |
| Category affinity | P(electronics), P(fashion) from browse history | Normalised click distribution |
| Spend patterns | Average order value, discount sensitivity | Transaction aggregations |

**Exam Tip:** **Single-stage scoring at scale** — scoring millions of items per request is infeasible; always use candidate generation first.

> **Recommendation Systems: Feature Store, Candidate Generation, and Ranking** = Features span user (affinity, recency, spend), item (attributes, content, popularity), and context (time, device, page)

---

## Architectures for Search Ranking and Fraud Detection — Rank vs Block

**The Story:** **Ranking**: retrieve 100–1000 → enrich → ML ranker → post-process → top N; latency 50–150 ms; success = CTR, conversion. **Fraud**: one-shot real-time (tens of ms); approve/decline/step-up.

**Key mechanics:**
- **Ranking**: retrieve 100–1000 candidates → enrich with query/doc/user features → ML ranker → post-process → top N
- Ranking optimises **order and relevance**; success = CTR, conversion, dwell time; latency 50–150 ms
- Ranking feedback loop: log queries/clicks → train → A/B test → promote
- **Fraud**: assemble real-time features → risk score → threshold decision (approve/decline/step-up)
- Fraud optimises **risk and correctness**; errors are expensive; latency tens of ms


$\text{decision}(s) = \begin{cases} \text{approve} & \text{if } s < \tau_{\text{low}} \\ \text{step-up} & \text{if } \tau_{\text{low}} \leq s < \tau_{\text{high}} \\ \text{decline} & \text{if } s \geq \tau_{\text{high}} \end{cases}$

| Component | Purpose |
|-----------|---------|
| Document store | Products, articles, or videos with metadata and precomputed embeddings |
| Lexical index | BM25, inverted indexes for keyword matching |
| Vector index | Semantic search via embedding similarity |
| Feature pipeline | Precompute popularity (CTR), quality signals, business scores |

**Exam Tip:** **Applying ranking latency budgets to fraud** — fraud decisions need sub-50 ms; ranking can tolerate 150 ms for the ranker step alone.

> **Architectures for Search Ranking and Fraud Detection** = Ranking: retrieve 100–1000 candidates → enrich with query/doc/user features → ML ranker → post-process → top N

---

## Fraud Detection: Online Decisions and Delayed Labels — Instant Block, Delayed Verdict

**The Story:** Fraud decisions are one-shot, real-time with approve/decline/step-up. Real-time features: **velocity**, device familiarity, IP risk, amount anomaly. Thresholds $\tau_{\text{low}}$ and $\tau_{\text{high}}$ are **segment-specific**.

**Key mechanics:**
- Fraud decisions are **one-shot, real-time** (tens of ms) with approve / decline / step-up outcomes
- Real-time features: **velocity, device familiarity, IP risk, amount anomaly**
- Thresholds $\tau_{\text{low}}$ and $\tau_{\text{high}}$ are **segment-specific**, not global
- Every decision is **audited** with model version, features, score, and action
- Labels arrive **30–90 days late** via chargebacks and investigations


$s < \tau_{\text{low}}$
$\tau_{\text{low}} \leq s < \tau_{\text{high}}$
$s \geq \tau_{\text{high}}$

| Field | Use in Feature Assembly |
|-------|------------------------|
| Card details (tokenised) | Velocity checks, historical pattern |
| Transaction amount | Anomaly detection vs user baseline |
| Merchant ID / category | Merchant risk scoring |
| Device fingerprint | New vs known device |

**Exam Tip:** **Training on future information** — using post-chargeback features as inputs creates leakage; always reconstruct point-in-time feature snapshots.

> **Fraud Detection: Online Decisions and Delayed Labels** = Fraud decisions are one-shot, real-time (tens of ms) with approve / decline / step-up outcomes

---

## Ranking vs Fraud Systems: Shared Platform, Different Priorities — Same Platform, Different Stakes

**The Story:** Ranking and fraud share pipelines, feature stores, online scoring, monitoring/retraining. **Ranking** bad results are annoying; **fraud** mistakes are catastrophic — different accuracy/latency trade-offs on shared infra.

**Key mechanics:**
- Ranking and fraud share: **data pipelines, feature stores, online scoring, monitoring/retraining**
- Both track metric drift, data drift, and model performance over time
- **Ranking** optimises order/relevance (CTR, conversion); bad results are annoying, not catastrophic
- **Fraud** optimises risk/correctness; bad decisions mean financial loss or unfair treatment
- Ranking experiments aggressively with A/B tests; fraud deploys conservatively with audit trails

| Primitive | Function | Shared Implementation |
|-----------|----------|----------------------|
| **Data pipeline** | Ingest raw events into usable tables | Kafka → data lake → aggregated tables |
| **Feature layer** | Consistent features for training and serving | Feature store with offline + online paths |
| **Online scoring** | Low-latency model inference | FastAPI/gRPC service with model registry |
| **Monitoring** | Track drift, performance, system health | Prometheus + alerting + dashboards |

**Exam Tip:** **Assuming ranking and fraud need different platforms** — they share 80% of infrastructure; only priorities and risk profiles differ.

> **Ranking vs Fraud Systems: Shared Platform, Different Priorities** = Ranking and fraud share: data pipelines, feature stores, online scoring, monitoring/retraining

---

## The Layered ML Platform: Five-Layer Architecture — Five-Layer Platform

**The Story:** ML platform = **5 layers**: Data → Features → Training → Serving → Monitoring. Each depends on the one below. **Data layer**: ingestion, storage, quality contracts (freshness, completeness, schema).

**Key mechanics:**
- ML platform = **5 layers**: Data → Features → Training → Serving → Monitoring
- Each layer depends on the one below; interfaces must stay clear
- **Data layer**: ingestion, storage, quality contracts (freshness, completeness, schema)
- **Feature layer**: define once, materialise offline + online; feature store lives here
- **Training layer**: pipelines, experiment tracking, model registry, promotion logic

| Layer | Core Responsibility | Key Question |
|-------|----------------------|--------------|
| **Data** | Ingest, store, validate raw data | Where does data come from? Is it on time and complete? |
| **Features** | Transform raw data into reusable features | Which features matter? Are they consistent in training and serving? |
| **Training & Experiments** | Train, evaluate, track, promote models | How do we choose which model goes to production? |
| **Serving & Infrastructure** | Deploy, scale, route inference requests | How do we meet latency, reliability, and cost constraints? |

**Exam Tip:** **Treating the platform as a monolith** — layers must have clear interfaces so they can evolve independently.

> **The Layered ML Platform: Five-Layer Architecture** = ML platform = 5 layers: Data → Features → Training → Serving → Monitoring

---

## ML Platform Layers: Serving, Monitoring, and the Closed Loop — Closed Loop on the Floor

**The Story:** **Serving**: FastAPI/gRPC, Docker/K8s, blue-green/canary, autoscaling. Model from **registry config** (`current_best.json`). Runtime optimisation: ONNX, quantisation. **Monitoring** closes loop to retraining.

**Key mechanics:**
- **Serving layer**: FastAPI/gRPC APIs, Docker/Kubernetes deployment, blue-green/canary rollouts, auto-scaling
- Model loaded from **registry config** (`current_best.json`) — swap versions without code changes
- Runtime optimisation: ONNX, quantisation, pruning for latency/cost targets
- **Monitoring layer**: system metrics (latency, errors), data metrics (drift, freshness), model metrics (CTR, fairness)
- Alerts trigger: auto-scale, rollback, retrain, or block promotion

| Interface Type | Pattern | Latency | Example |
|----------------|---------|---------|---------|
| **Online (sync)** | Request-response per prediction | Milliseconds | Fraud scoring, recommendation ranking |
| **Batch** | Score large datasets offline | Minutes–hours | Nightly churn prediction for all users |
| **Streaming** | Process event stream continuously | Seconds | Real-time feature updates, anomaly detection |

**Exam Tip:** **Monitoring only system metrics** — data drift and model performance degradation cause silent quality loss without any 5xx errors.

> **ML Platform Layers: Serving, Monitoring, and the Closed Loop** = Serving layer: FastAPI/gRPC APIs, Docker/Kubernetes deployment, blue-green/canary rollouts, auto-scaling

---

## ML Platform: Module Mapping and System Design Framework — Module Map for Design

**The Story:** Every course topic maps to one of **5 platform layers**. System design = answer 5 questions (data, features, training, serving, monitoring). Three examples: recommendation, ranking, fraud — same layers, different priorities.

**Key mechanics:**
- Every course topic maps to one of **5 platform layers** — use this as a mental index
- System design = answer **5 questions** (data, features, training, serving, monitoring) for any ML problem
- Three worked examples: recommendation, ranking, fraud — same layers, different priorities
- Paradigm shift: from **single model** to **whole system** thinking
- Governance hooks exist in **every layer** — not a separate concern

| Layer | Course Topics Covered |
|-------|----------------------|
| **Data** | Ingestion patterns (batch, micro-batch, streaming); data quality monitoring; pipeline orchestration; schema contracts |
| **Features** | Feature store architecture; offline vs online materialisation; training-serving skew; feature reuse, metadata, lineage |
| **Training & Experiments** | Training pipelines; experiment tracking (MLflow); model registry and versioning; promotion logic; fairness thresholds; model optimisation trade-offs |
| **Serving & Infrastructure** | Serving patterns (REST, gRPC, batch, streaming); Docker containerisation; Kubernetes deployment; blue-green and canary rollouts; multi-model routing; ONNX/quantisation |

**Exam Tip:** **Jumping to architecture diagrams without clarifying requirements** — always start with the five questions, not boxes and arrows.

> **ML Platform: Module Mapping and System Design Framework** = Every course topic maps to one of 5 platform layers — use this as a mental index

---

## ML System Design: Clarifying Requirements and SLAs — Questions Before Boxes

**The Story:** Never start with architecture diagrams — clarify requirements, **SLAs**, failure impact. Key questions: what product, who uses it, success definition, failure cost. **Latency SLAs**: specify percentile (**P95/P99**) and measurement point.

**Key mechanics:**
- **Never start with boxes** — clarify requirements, SLAs, and failure impact first
- Key questions: what product, who uses it, what does success mean, what if it fails?
- **Latency SLAs**: specify percentile (P95/P99) and measurement point (end-to-end vs service)
- **Availability**: 99% = 3.5 days downtime/yr; 99.9% = 9 hrs; 99.99% = 1 hr
- **Graceful degradation**: fallback models, cached results, non-personalised defaults

| Question | Why It Matters | Example Answers |
|----------|----------------|-----------------|
| What is the product? | Determines architecture pattern | Recommendation carousel, fraud detector, search ranker |
| Who uses it? | Determines interface and SLA | UI-facing API, backend service, batch pipeline |
| UI-facing or backend? | Determines latency sensitivity | Homepage carousel (tight) vs nightly batch scoring (loose) |
| Batch or real-time? | Determines infrastructure | Real-time fraud (streaming) vs weekly churn (batch) |

**Exam Tip:** **Starting with architecture diagrams** — always clarify requirements and SLAs first; diagrams come after.

> **ML System Design: Clarifying Requirements and SLAs** = Never start with boxes — clarify requirements, SLAs, and failure impact first

---

## ML System Design: Traffic Estimation and Capacity Planning — How Many Counters?

**The Story:** Capacity planning translates SLAs to **instance counts**, storage, batch windows. Ask: average QPS, **peak QPS**, events/day, training data window. $\text{instances} = (\text{peak QPS} / \text{QPS per instance}) \times \text{headroom}$.

**Key mechanics:**
- Capacity planning = translate SLAs into **instance counts, storage, and batch windows**
- Ask: average QPS, **peak QPS**, events/day, training data window
- Instance formula: $\text{instances} = (\text{peak QPS} / \text{QPS per instance}) \times \text{headroom}$
- Headroom multiplier typically **2x** for bursts and failover
- Storage: events/day × bytes/event × retention days ÷ compression ratio


$\text{daily storage} = 50 \times 10^6 \times 500 \text{ bytes} \approx 25 \text{ GB/day}$
$\text{6-month storage} = 25 \text{ GB} \times 180 \text{ days} \approx 4.5 \text{ TB}$
$\text{instances} = \frac{\text{peak QPS}}{\text{QPS per instance}} \times \text{headroom} = \frac{1000}{100} \times 2 = 20 \text{ instances}$

| Question | Why It Matters |
|----------|----------------|
| Average QPS? | Baseline instance count |
| Peak QPS? | Burst capacity and headroom |
| When do peaks occur? | Sale events, evenings, product launches |
| Geographic distribution? | Multi-region requirements |

**Exam Tip:** **Planning for average QPS only** — peak traffic (4–10x average) causes outages during sales events.

> **ML System Design: Traffic Estimation and Capacity Planning** = Capacity planning = translate SLAs into instance counts, storage, and batch windows

---

## ML System Design: Failure Scenarios and Resilience Strategies — Disaster Drills

**The Story:** **Data failures**: pipeline stall, partial batches, schema changes → fallback snapshots, quality alerts, versioned features. **Model failures**: outage, overload, bad deploy → cached fallback, baseline model, **canary**, fast rollback. Ramp canary 5% → 25% → 100%.

**Key mechanics:**
- **Data failures**: pipeline stall, partial batches, schema changes → fallback snapshots, quality alerts, versioned features
- **Model service failures**: outage, overload, bad deployment → cached fallback, baseline model, canary, fast rollback
- **Deployment safety**: canary (5% → 25% → 100%) with defined success criteria; instant rollback via config
- **Infrastructure failures**: auto-scaling, multi-AZ, circuit breakers, rate limiting
- Interview structure: requirements → architecture → capacity → failures → trade-offs

| Failure | Symptom | Downstream Impact |
|---------|---------|-------------------|
| Pipeline stall | No new events ingested for hours | Stale features, outdated training data |
| Partial batch | Only 60% of expected events arrive | Biased aggregations, incorrect features |
| Schema change | New column added, old column removed | Downstream SQL/feature jobs crash |
| Feature job failure | Aggregation pipeline fails overnight | Offline features stale; online cache expires |

**Exam Tip:** **Only discussing model accuracy failures** — infrastructure and data failures are more common and more impactful.

> **ML System Design: Failure Scenarios and Resilience Strategies** = Data failures: pipeline stall, partial batches, schema changes → fallback snapshots, quality alerts, versioned features

---

## From Components to Complete System — Capstone Blueprint

**The Story:** Capstone integrates all course components into one production-grade system. Repository mirrors **five-layer architecture**. System story: what it does, how it scales, how it fails, how it improves.

**Key mechanics:**
- Capstone integrates **all course components** into one production-grade system
- Repository structure mirrors the **five-layer architecture**
- System story: **what it does, how it scales, how it fails, how it improves**
- Key integration: shared features, registry → serving, monitoring → retrain, CI/CD → deploy
- Rollback = edit `current_best.json` + restart — decoupled model management

| Skill | How It Is Demonstrated |
|-------|------------------------|
| **End-to-end architecture** | Complete diagram from raw data to monitored production model |
| **Component integration** | Each module's artefact has a home in the repository |
| **Operational narrative** | Explain what the system does, how it scales, how it fails |
| **Hands-on execution** | Train models, promote champions, serve predictions, roll back |

**Exam Tip:** **Treating the capstone as a coding exercise** — it tests system thinking and integration, not just script execution.

> **From Components to Complete System** = Capstone integrates all course components into one production-grade system

---

## Complete System Walkthrough — Full Loop Walkthrough

**The Story:** Capstone implements full **MLOps loop**: data → features → train → register → promote → serve → monitor → retrain. **Offline**: ingest → features → training → MLflow → registry. **Online**: `current_best.json` → FastAPI → predictions with online features.

**Key mechanics:**
- Capstone implements the **full MLOps loop**: data → features → train → register → promote → serve → monitor → retrain
- **Offline path**: ingest → feature pipeline → training → MLflow logging → registry.json
- **Online path**: current_best.json → FastAPI loads champion → predictions with online features
- **Closed loop**: monitoring detects drift → retrain trigger → new candidate → promote or discard
- **Rollback**: edit current_best.json + restart — seconds, no code changes

| Action | Detail |
|--------|--------|
| Input | New CSV/Parquet files in `data/raw/` |
| Validation | Schema check, null rate, volume sanity |
| Output | Appended rows in `data/processed/train.parquet` |
| Failure handling | Reject bad files; alert on validation failure |

**Exam Tip:** **Training without registration** — a model file without registry metadata cannot be promoted or rolled back.

> **Complete System Walkthrough** = Capstone implements the full MLOps loop: data → features → train → register → promote → serve → monitor → retrain

---

# ONE-LINE SUMMARIES — The Complete Set

> **Why Models Die in the Notebook: The Integration Gap** = High notebook metrics often lead nowhere without engineering around the model
> **Defining Model Engineering: From Artifact to Production Service** = Model engineering = making models usable, reliable, and scalable in production
> **Four Core Responsibilities of Model Engineering** = Four responsibilities: services, constraints, change management, collaboration
> **The Seven-Stage ML Lifecycle** = Seven stages: framing → data → features → training → deployment → monitoring → retraining
> **Deployment, Monitoring, and Retraining: The Production Loop** = Deployment: expose model via API or batch; integrate into product; balance latency, uptime, cost, security
> **Where This Course Fits in the ML Lifecycle** = Course focuses on deployment, monitoring, and retraining — not primary training/research
> **Production Constraints: Latency, Throughput, Cost, and Reliability** = Offline metrics necessary but not sufficient for production
> **Common Production Failure Modes** = Four recurring failure modes: training-serving skew, data drift/staleness, silent failures, infra/dependency issues
> **Why ML Needs Engineering and Operations** = Constraints + failure modes = why ML needs engineering and operations
> **MLOps: The Operating System for Production ML** = MLOps = DevOps practices adapted for ML systems
> **MLOps Core Practices: Versioning, Pipelines, and CI/CD** = Version data, model artifacts, and config — for reproducibility, auditability, rollback
> **The ML Model Engineer Role** = Model engineer: intersection of research, infra, and product
> **Building an ML Project from Scratch** = Lab flow: environment → project → notebook → Hugging Face → prediction → package
> **Virtual Environments, Jupyter, and Hugging Face Setup** = Activate venv before any installs: source .venv/bin/activate (Mac/Linux)
> **Hugging Face Ecosystem and Text Generation Pipeline** = Hugging Face = model hub + datasets + libraries + community ecosystem
> **Definition of Model Inference** = Training learns $f$ from historical data; inference calls $f$ on new data continuously
> **Latency, Throughput, and Cost: The Inference Metrics Triangle** = Three core inference metrics: latency, throughput, cost — they drive all serving design
> **Inference Patterns: Setup and Mental Model** = Model inference is $\text{prediction} = f(\text{input features})$ — the function stays constant
> **Batch Inference: Definition and Architecture** = Batch inference scores many items at once on a schedule; nobody waits per row
> **Batch Inference: Offline Use Cases and Trade-offs** = Classic batch use cases: churn scoring, credit risk, offline recommendations, marketing lists, compliance reports
> **Batch Inference: Metrics, Pros, Cons, and Architecture** = Batch optimizes throughput and total job time; per-row latency is low priority
> **Online Inference: The Request-Response Pattern** = Online inference = one request in, one response out; caller is blocked until prediction arrives
> **Online Inference: Interactive Use Cases and Metrics** = Online inference is required when a live interaction blocks on the prediction
> **Online Inference: Latency, Reliability, and Production Techniques** = Online advantages: fresh context, per-request personalization, faster training feedback
> **Streaming Inference: Architecture and Pattern Comparison** = Streaming inference processes continuous event flows through a long-running pipeline
> **Streaming Inference: Use Cases, Metrics, and Trade-offs** = Streaming use cases: fraud detection, clickstream analytics, IoT sensors, log/security analytics
> **Choosing the Right Inference Pattern: Decision Guide** = Three decision questions: sub-second user response? scheduled bulk? continuous event stream?
> **Inference Patterns: Metrics Mapping and Scenario Guide** = Each pattern optimizes different metrics: batch (throughput/job time), online (P95/P99), streaming (event-to-action/lag)
> **Model Selection and Single-Request Inference** = Model selection must balance capability with hardware constraints (Flan-T5 Small: 77M params, runs on CPU)
> **Sequential vs Batch Inference Performance** = Sequential baseline: 1,000 inputs in ~61 sec, ~16.25 inputs/sec on CPU
> **Summary: Interpreting Inference Metrics and Trade-offs** = Batching trade-off: parallelism benefit vs padding cost
> **Defining Model Serving: Artefact vs Service** = Model serving = long-lived service that loads a model, handles requests, and returns predictions.
> **Core Responsibilities of the Model Serving Layer** = Five responsibility domains: model lifecycle, input validation, efficient inference, response formatting, operations.
> **Monolithic Model Serving Architecture** = Monolith = model embedded inside the main application, same process, no separate service.
> **Microservice Model Serving Architecture** = Model microservice = separate process/container with its own POST /predict API.
> **Serverless Model Serving Architecture** = Serverless = model packaged as a cloud-managed function (Lambda, Cloud Functions).
> **Design Decisions in Model Serving Systems** = Three architectures: monolith (simple, coupled), microservice (independent, complex), serverless (auto-scale, constrained).
> **REST APIs for Machine Learning Serving** = REST = HTTP verbs + JSON payloads; the default ML serving API style.
> **gRPC for Machine Learning Serving** = gRPC = high-performance, contract-first RPC using Protocol Buffers (binary, not JSON).
> **Synchronous vs Asynchronous API Calls for ML Serving** = Sync = client blocks until prediction arrives; async = client submits job and moves on.
> **Single-Instance Deployment of Model Services** = Simplest deployment: one VM or container running the model API on a single port.
> **Blue-Green and Canary Deployment for Model Services** = Blue-green: two environments side by side; switch all traffic at once; instant rollback.
> **Autoscaling for Model Services** = Autoscaling adjusts instance count based on load signals to balance SLOs and cost.
> **Building a FastAPI Model Service** = FastAPI app with Pydantic models = schema-enforced ML API with auto-generated docs.
> **Containerizing the ML Service with Docker** = Docker image = portable unit bundling code, model, and dependencies.
> **Testing the Containerized Model Service Locally** = Test containerised service at localhost:8000 (mapped from container port 80).
> **Manual Workflow Pain, Pipeline Definition, and Benefits** = Manual notebook workflows hide steps in one person's head and break under team scale.
> **Classic CI/CD in Software Engineering** = CI: frequent commits + automated build/test on every change; catch problems early.
> **ML-Specific Differences from Classic CI/CD** = ML behaviour depends on code, data/labels, and model parameters — not code alone.
> **The Hybrid Picture: Code CI/CD + ML Pipeline** = Production MLOps uses a hybrid: code CI/CD + ML pipeline, orchestrated together.
> **ML Artefacts: What Pipelines Move and Track** = ML artefacts include code, configs, data snapshots, models, metrics, and reports — not just code.
> **Lineage and Traceability in ML Systems** = Lineage answers: which data/code/config produced which model, and what is in production.
> **Reproducibility in Machine Learning Systems** = Reproducibility: same code + config + data snapshot → equivalent model (within tolerance).
> **CI/CD for Machine Learning** = CI/CD for ML turns abstract pipeline concepts into concrete verification and promotion workflows.
> **CI for Machine Learning** = ML CI starts with standard software CI: lint, unit tests, integration tests.
> **CD for Machine Learning** = ML CD promotes a specific model version + metrics + code + config — not just latest image.
> **Repository Structure for MLOps Pipelines** = MLOps repo layout: .github/, configs/, data/, models/, scripts/, src/, README.md.
> **MLflow Experiment Tracking** = MLflow pattern: start_run → log_params → train → log_metrics → log_model.
> **CI Workflow for ML Repositories** = CI YAML in .github/workflows/ defines automated jobs on push/PR to main.
> **Why Monitoring ML Models Is Different** = ML services need traditional monitoring and data/prediction monitoring.
> **What to Monitor: The Three-Layer Framework** = ML monitoring uses three layers: system health, data health, prediction/business health.
> **System, Data, and Feature Metrics in Depth** = System metrics: P95/P99 latency, 4xx/5xx errors, RPS, CPU/memory, restarts.
> **Model Performance Metrics and Production Logging** = All monitoring metrics depend on structured per-prediction logging.
> **Types of Drift in Production ML Systems** = Drift = world changes, model does not; primary cause of silent production degradation.
> **Drift Detection Methods and Alert Design** = Start drift detection with mean, std, min/max, missing rates, and histograms.
> **Responding to Drift: Detection, Investigation, and Action** = Drift response: detect → investigate → decide (threshold, data fix, or retrain).
> **From Metrics to Action: Designing an ML Monitoring Workflow** = Observability pillars: logs (events), metrics (time-series), traces (request paths) — all needed for ML.
> **Dashboards, Alerts, and the Typical ML Monitoring Stack** = One primary dashboard per model: system + data + prediction zones; 30-second scan.
> **Four Production Failure Scenarios** = Lab uses simulated scenarios for reproducibility; patterns scale to production.
> **Instrumenting Model Services: Metrics, PSI, and Automated Alerting** = Production monitoring starts with structured logs + stored training baselines.
> **Static Models and the Retraining Loop** = Static models degrade silently as the world changes; monitoring exposes this, retraining addresses it.
> **Retraining Triggers: Drift, Performance, and Policy** = Three major retraining triggers: data drift/quality, performance degradation, policy/product changes.
> **Continuous Training: Scheduled vs Event-Driven Retraining** = Continuous training keeps models fresh via scheduled, event-driven, or hybrid retraining patterns.
> **Designing a Retraining and Promotion Pipeline** = Retraining pipeline: snapshot data → build features → train candidates → evaluate → register → promote.
> **Evaluating and Selecting the Right Model: Champion vs Challenger** = Stage 3 compares challengers to champion on held-out data, multiple time slices, ML metrics, business KPIs, and segment fairness.
> **Promotion, Deployment, and the Continuous Retraining Loop** = Stage 5 promotes models through staging → canary/shadow → full production, keeping old champion for rollback.
> **Offline Evaluation and Backtesting** = Offline evaluation: train/val/test splits, time-based splits, cross-validation — fast, cheap, zero user risk.
> **Live Environment Validation: Shadow Testing and A/B Testing** = Shadow testing: both models see same input; only champion output served; challenger logged for analysis.
> **Choosing Evaluation Methods and Connecting Them to Promotion** = Match evaluation depth to model impact: backtest (cheap) → shadow (live inputs) → A/B (real users).
> **Governance and Safety: Why Approvals Matter** = Governance provides accountability (owners, approvers), traceability (lineage, audit trail), and controlled risk.
> **Traceability, Audit Trails, and Rollback Mechanisms** = Audit trail: registry entry with version, owner, stage, training lineage, deployment history, approvers.
> **Guardrails and the Governed Promotion Workflow** = Guardrails: output sanity checks, rate limiting, kill switches, policy constraints, input validation, fallbacks.
> **Config-Driven Retraining Pipeline: Training Script and MLflow Integration** = Retraining pipeline is config-driven: same train.py, different config files for data/hyperparameters.
> **Champion vs Challenger Evaluation and Automated Promotion** = Champion loaded by Production stage; challenger by explicit version number.
> **Registry-Driven Serving, Promotion Updates, and Rollback** = Serving service loads model from MLflow registry by name + stage (via environment variables).
> **The Research–Production Deployment Gap** = Production constraints: P95/P99 latency, throughput, cost-per-prediction, diverse hardware
> **Production Optimisation Goals: Portability, Speed, and Footprint** = Portability: train in any framework, deploy on any hardware via standard formats
> **Three Levers for Production Model Optimisation** = Three levers: standard formats, compression, optimised runtimes
> **Standard Model Formats: Foundations and ONNX** = Model format = graph + parameters + metadata (blueprint + numbers)
> **TensorFlow Lite: Mobile and Edge Deployment** = TF Lite = format + runtime for mobile and embedded deployment
> **OpenVINO and the Standard Format Pipeline** = OpenVINO optimises for Intel CPUs, iGPUs, and accelerators
> **Why Model Compression Matters in Production** = Compression makes accurate models practical for production constraints
> **Quantisation and Pruning** = Quantisation: FP32 → FP16/INT8; ~4× size reduction at INT8; faster memory-bound inference
> **Knowledge Distillation** = Distillation: train a small student to mimic a large teacher
> **Compression Trade-offs and the MLOps Pipeline** = Quantisation: best first step; easy PTQ, big INT8 gains
> **Optimised Runtimes: Foundations** = Optimised runtimes execute standard-format graphs with maximum hardware efficiency
> **ONNX Runtime, TensorRT, and XLA** = ONNX Runtime: portable, ONNX-native, execution providers for CPU/GPU/TensorRT
> **Runtime Trade-offs and Deployment Fit** = Portable: ONNX + ORT — one format, many platforms; may sacrifice peak perf
> **Establishing a Baseline: Model Size and Latency** = Baseline = disk size + avg/P95 latency before any optimisation
> **Exporting a CNN to ONNX Format** = torch.onnx.export traces graph with dummy input; names define runtime API
> **ONNX Runtime Benchmarking and Interpreting Results** = ORT inference: InferenceSession + session.run with numpy arrays and named inputs
> **The Four-Way Tug-of-War Mental Model** = Production ML sits at the centre of a four-way tug-of-war: accuracy, latency, cost, UX.
> **Accuracy, Latency, Cost, and User Experience** = Accuracy improves with model complexity but raises latency and cost per request.
> **The Latency–Cost–UX Triangle** = Latency, cost, and UX form a triangle: lower latency usually costs more; aggressive cost cuts raise latency and hurt UX.
> **Why ML Services Need to Scale** = ML traffic is spiky and grows over time; fixed capacity leads to rising latency and SLO violations.
> **Vertical Scaling, Horizontal Scaling, and Autoscaling** = Vertical scaling: bigger box — simple, limited, single point of failure.
> **Scaling Patterns Compared: Latency, Cost, and Stability** = Vertical scaling: quick latency win for small systems; hits limits and cost inefficiency at scale.
> **Inference Cost and Spot / Preemptible Instances** = Inference cost is dominated by compute, idle capacity, network/storage, and engineering overhead.
> **Serverless Inference** = Serverless inference: model as a function; platform scales and bills per use.
> **Batching and Micro-Batching for Cost Efficiency** = Batching amortises forward-pass overhead across many inputs — lower cost per request, higher throughput.
> **Reading Constraints: A Decision Framework** = First step in production design: read constraints — latency/UX, accuracy/risk, cost, traffic.
> **Scenario-Based Deployment Decisions** = Fraud check: online, high accuracy, horizontal autoscaling, premium hardware, heavy monitoring.
> **Dynamic Quantisation for Model Compression** = Compression targets model size/speed when ONNX export alone is insufficient.
> **Benchmarking Compression: Size, Latency, and Accuracy** = Benchmark FP32 vs compressed across size, latency (avg + P95), and accuracy.
> **Deployment Fit: Edge vs Cloud for Compressed Models** = FP32: max precision — high-stakes domains, GPU cloud, unconstrained batch jobs.
> **Training-Serving Skew: Definition, Causes, and Consequences** = Training-serving skew: model sees different feature distributions in training vs serving.
> **Offline Features: Batch Computation for Training** = Offline features: batch-computed, stored in data lake/warehouse, used for training and batch scoring.
> **Online Features: Low-Latency Serving** = Online features: precomputed values retrieved per entity at request time in milliseconds.
> **What a Feature Store Provides** = Feature store: central system to define features once and serve them offline and online.
> **Feature Store Ecosystem: Common Building Blocks** = All feature stores share four building blocks: definitions, offline store, online store, registry.
> **Feast: Open-Source Feature Store Baseline** = Feast: open-source feature store; mental baseline for understanding all feature stores.
> **Managed Feature Platforms: Tecton and Hopsworks** = Tecton: managed enterprise feature platform; runs pipelines, rich UI, deep streaming/warehouse integration.
> **The Common Feature Store Pattern: Practical Takeaways** = Universal pattern: define → offline materialise → online materialise → registry.
> **Feature Reuse: Solving Duplication and Inconsistency** = Without feature stores: same feature reimplemented 3–4 times with subtle differences.
> **Metadata and Lineage: Understanding and Tracing Features** = Metadata: name, description, units, owner, schema, freshness, quality, usage per feature.
> **Feature Governance and Lifecycle Management** = Sensitive features: PII, protected attributes, financial, health data — require special handling.
> **From Feature Governance to Hands-On Practice** = Labs simulate a feature store: pandas offline table + Python dict online store + shared function.
> **Building an Offline Feature Table in Pandas** = Raw events (customer_id, timestamp, amount) → aggregated entity-level features.
> **Simulating an Online Feature Store with a Dict Cache** = Online features: precomputed, retrieved by entity key in milliseconds.
> **Avoiding Training-Serving Skew with a Tiny Feature Store** = Skew demo: offline 30-day features (spend=170) vs buggy online 7-day features (spend=0).
> **Why Machine Learning Needs Data Pipelines** = Notebooks are exploratory and manual; production pipelines are automated, scheduled, and observable.
> **ETL and ELT: Foundations of ML Data Pipelines** = ETL: extract → transform (external) → load curated tables into warehouse.
> **Pipeline Types: Batch, Micro-Batch, and Streaming** = Three ingestion modes: batch (large scheduled chunks), micro-batch (frequent small chunks), streaming (continuous per-event).
> **Batch Ingestion for Machine Learning** = Batch ingestion runs on a fixed schedule, processing a specific time window per job.
> **Micro-Batch Ingestion: Concept and Architecture** = Micro-batch = small batches, frequent runs (every 1–5 minutes) — a compromise between batch and streaming.
> **Comparing Batch and Micro-Batch Ingestion** = Batch: higher latency (hours/day), lower complexity, fewer large jobs, ideal for retraining and offline scoring.
> **Event Streams: Foundations of Streaming for ML** = Streaming processes continuous event flows rather than files or partitions.
> **Kafka, Spark, Flink, and Beam: Roles in Streaming ML** = Kafka = event transport and durable log (topics, partitions, offsets) — the highway.
> **Streaming Machine Learning: Use Cases and Architecture** = Streaming ML excels at anomaly detection, live recommendations, dynamic pricing, fraud, and real-time monitoring.
> **Data Freshness and Latency in Real-Time ML** = Real-time ML systems fail quietly with bad data — they do not crash, they make worse decisions.
> **Data Completeness and Correctness for ML Pipelines** = Data quality has three dimensions: freshness, completeness, and correctness.
> **Schema Evolution and Data Contracts** = Schema evolution is inevitable — fields are added, removed, renamed, and retyped over time.
> **Applying Data Quality Concepts in Practice** = Apply data quality concepts to a concrete batch pipeline: daily CSV → ingestion → master dataset → retrain trigger.
> **Simulating Daily Data Arrival for Pipeline Development** = Simulate daily data arrival before building ingestion pipelines — predictable, repeatable test data.
> **Incremental Ingestion: State Management and Idempotency** = Incremental ingestion processes only new files and appends to master dataset — the production standard.
> **Training-Serving Skew: Detection and the Feature Store Fix** = Training-serving skew: features at training time differ from features at serving time — silent, devastating bug.
> **Data and Input Threats in Machine Learning Systems** = ML security matters because models sit in high-stakes decision loops and are harder to reason about than rule engines.
> **Model and Privacy Threats: Extraction, Leakage, and Over-Exposure** = Models are sensitive assets: IP, information channel, and attack surface simultaneously.
> **Why Machine Learning Systems Are Attractive Attack Targets** = ML systems are attractive targets because they control high-stakes decisions with opaque behaviour.
> **PII and Sensitive Attributes in Machine Learning** = Privacy is a non-functional requirement equal to latency and uptime in production ML.
> **Data Minimisation and Anonymisation Techniques** = Data minimisation: collect only what the task requires; reduces attack surface and compliance burden.
> **Role-Based Access Control and Data Governance for ML** = RBAC assigns least-privilege permissions by role — data engineer, model engineer, and analyst need different access.
> **Fairness and Bias: Evaluating Models Across Groups** = High overall accuracy can mask systematic harm to specific groups.
> **Practical Fairness Questions and Visualisation** = Four key questions: FN disparity, subpopulation performance drop, calibration consistency, threshold impact.
> **Fairness Limitations, Trade-offs, and the Model Engineer's Role** = No single universal fairness metric — equal accuracy, FPR, FNR, and calibration can conflict.
> **Explainability: What It Is, Why It Matters, and Its Limits** = Explainability makes model behaviour understandable for humans — local (one case) and global (population).
> **Audit Trails Across the ML Pipeline** = Audit trails reconstruct what happened across the ML lifecycle.
> **Regulatory Expectations and Designing for Auditability** = Regulated domains share expectations: purpose limitation, non-discrimination, explainability, record-keeping.
> **Segmented Evaluation: Performance by Group** = High global accuracy can hide poor performance for specific groups.
> **Automated Fairness Checks: Policy, Thresholds, and Pass/Fail Logic** = Automate fairness by encoding policy thresholds as pass/fail rules in CI/CD.
> **Logging Fairness Metrics for Audit and Monitoring** = Console pass/fail is ephemeral — governance requires persistent structured logs.
> **Why Multi-Model Systems Exist** = Multi-model systems arise from localization, versioning, task specialisation, and scale
> **Routing Strategies: Rule-Based and Learned Routers** = Rule-based routing maps explicit conditions (region, language, tier) to model endpoints
> **Fallback Models, Ensembles, and the Accuracy–Cost Trade-Off** = Fallback routing handles uncertainty, OOD inputs, and service failures with safe alternatives
> **Scaling Inference: Sharding and Replication** = Single-instance serving hits latency, timeout, and QPS ceilings
> **Caching Model Results and Embeddings** = Inference caching skips expensive model calls when recent results exist
> **Combining Routing, Sharding, and Caching at Scale** = Production inference stacks compose: cache → router → shard → replicas → model
> **Integrated Architecture: Routing, Sharding, Replication, and Caching** = Production ML serving composes routing + sharding + replication + caching
> **Multi-Tenant ML Platforms and the Noisy Neighbour Problem** = A tenant is a logical customer of the ML platform (team, business unit, external client)
> **Per-Tenant SLOs and Isolation Strategy Overview** = SLOs are measurable targets (latency, availability, error rate) per tenant
> **Blast Radius, Resource Quotas, and Data Isolation** = Blast radius = how far an incident spreads; limit it via namespaces and separate clusters
> **Embeddings, Vector Similarity, and Vector Databases** = An embedding is a dense vector capturing semantic meaning; similar items are nearby in vector space
> **Approximate Nearest Neighbour (ANN) Search** = Exact NN search does not scale to millions/billions of vectors
> **RAG Pipelines as Multi-Model Systems** = RAG = embed query → retrieve top-$K$ docs → optional rerank → generate answer with context
> **Building a File-Based Model Registry** = A model registry is the single source of truth for all trained model versions
> **Model Promotion and `current_best.json`** = Promotion decides which registry candidate is the current best for production
> **Dynamic Model Serving with `current_best.json`** = Serving service reads only current_best.json — decoupled from training and promotion
> **Recommendation System: Problem Definition and Requirements** = Carousel shows ~10 personalised products within 100–200 ms
> **Recommendation Systems: The Data Layer** = Data layer ingests behavioural events (views, clicks) and transactional events (cart, purchases, returns)
> **Recommendation Systems: Feature Store, Candidate Generation, and Ranking** = Features span user (affinity, recency, spend), item (attributes, content, popularity), and context (time, device, page)
> **Architectures for Search Ranking and Fraud Detection** = Ranking: retrieve 100–1000 candidates → enrich with query/doc/user features → ML ranker → post-process → top N
> **Fraud Detection: Online Decisions and Delayed Labels** = Fraud decisions are one-shot, real-time (tens of ms) with approve / decline / step-up outcomes
> **Ranking vs Fraud Systems: Shared Platform, Different Priorities** = Ranking and fraud share: data pipelines, feature stores, online scoring, monitoring/retraining
> **The Layered ML Platform: Five-Layer Architecture** = ML platform = 5 layers: Data → Features → Training → Serving → Monitoring
> **ML Platform Layers: Serving, Monitoring, and the Closed Loop** = Serving layer: FastAPI/gRPC APIs, Docker/Kubernetes deployment, blue-green/canary rollouts, auto-scaling
> **ML Platform: Module Mapping and System Design Framework** = Every course topic maps to one of 5 platform layers — use this as a mental index
> **ML System Design: Clarifying Requirements and SLAs** = Never start with boxes — clarify requirements, SLAs, and failure impact first
> **ML System Design: Traffic Estimation and Capacity Planning** = Capacity planning = translate SLAs into instance counts, storage, and batch windows
> **ML System Design: Failure Scenarios and Resilience Strategies** = Data failures: pipeline stall, partial batches, schema changes → fallback snapshots, quality alerts, versioned features
> **From Components to Complete System** = Capstone integrates all course components into one production-grade system
> **Complete System Walkthrough** = Capstone implements the full MLOps loop: data → features → train → register → promote → serve → monitor → retrain

---



*Last compiled: 2026-08-01 | BITS Pilani — Machine Learning Model Engineering*
