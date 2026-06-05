# Where This Course Fits in the ML Lifecycle

## Course Focus: Production Stages

This course primarily operates in the **later stages** of the seven-stage ML lifecycle:

```mermaid
flowchart LR
    S1[Problem Framing] --> S2[Data Collection]
    S2 --> S3[Feature Engineering]
    S3 --> S4[Training & Evaluation]
    S4 --> S5[Deployment]
    S5 --> S6[Monitoring]
    S6 --> S7[Retraining]
    style S5 fill:#e8f4e8
    style S6 fill:#e8f4e8
    style S7 fill:#e8f4e8
```

| Stage | Course Coverage |
|-------|-----------------|
| Problem framing, data, features | Discussed as **context** for building production systems |
| **Deployment** | **Core focus** — turning models into services |
| **Monitoring** | **Core focus** — observing real-world behavior |
| **Retraining / deprecation** | **Core focus** — evolving models over time |

When encountering architecture diagrams later in the course, mentally place concepts into these three production stages.

---

## Mental Roadmap

Each module is a deep dive into one or more parts of the lifecycle, especially the production-focused stages:

| Connection | Example |
|------------|---------|
| Monitoring → Retraining | Drift alerts trigger retraining pipelines |
| Deployment → Monitoring | Cannot monitor what is not deployed |
| Feature engineering → Deployment | Training-serving consistency prevents skew |

---

## The Big Takeaway

ML in the real world is **not** about training a model once. It is about **running a system over time** with:

- Feedback loops
- Continuous updates
- Careful engineering discipline

The next modules build the concrete skills and tools needed to operate in these later lifecycle stages as a model engineer.

---

## Common Pitfalls / Exam Traps

- Assuming this course teaches algorithm design — it teaches production operations
- Ignoring earlier lifecycle stages entirely — problem framing and features matter as context for serving
- Thinking deployment is the finish line — monitoring and retraining are equally essential

---

## Quick Revision Summary

- Course focuses on deployment, monitoring, and retraining — not primary training/research
- Earlier stages (framing, data, features) appear as production context
- Use the lifecycle diagram as a mental map for every module
- Real-world ML = systems over time with feedback loops, not one-time training
- Each module deep-dives into production-focused lifecycle stages
