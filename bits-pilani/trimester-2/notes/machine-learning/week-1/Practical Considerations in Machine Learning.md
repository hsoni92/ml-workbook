# Practical Considerations in Machine Learning – Machine Learning (Module 1)

## Learning Objectives

By the end of this video you will:

1. **List** real-world challenges when building ML systems.
2. **Explain** why **scalability**, **dimensionality**, **data quality**, **heterogeneity**, **ownership**, **privacy**, and **streaming** matter.
3. **Connect** these issues to building **effective and efficient** ML pipelines.

---

## Building an Effective ML System: What to Consider

An ML system (classification, regression, clustering, association rules, etc.) should be:

- **Scalable**
- Able to handle **complex and heterogeneous** data
- Aware of **data ownership and distribution**
- Able to deal with **high-dimensional** data
- Robust to **poor data quality**
- **Privacy-preserving** and compliant

Below are the main **practical challenges** and why they matter.

---

## 1. Scalability

- **Meaning:** The algorithm and pipeline should work when data **grows** (e.g. from 100 to 100,000 or 1 billion records).
- **Requirement:** Performance (time, memory) should remain acceptable as data size increases. The system must **scale** with data volume.
- **Why it matters:** In production, data often grows; a solution that only works on small samples is not useful.

---

## 2. Dimensionality (High-Dimensional Data)

- **Meaning:** **Dimensionality** = number of **features/attributes** (e.g. number of columns in a table).
- **Problem:** Many ML algorithms perform **poorly** or become **slow** when the number of dimensions is large. The amount of data needed to support reliable results often grows with dimensions.
- **Sparsity:** In high dimensions, data can become **sparse** (few points per region). That makes learning harder.
- **Requirement:** The pipeline should handle high-dimensional and possibly sparse data (e.g. via feature selection, dimensionality reduction, or algorithms suited to high dimensions).

---

## 3. Heterogeneous and Complex Data

- **Meaning:** Data comes from **many sources** and in **many forms**: audio, video, text, sensors, databases.
- **Challenge:** We must **aggregate and integrate** these sources into a form suitable for modeling. Data can also be **complex** in structure (e.g. nested, graph, time series).
- **Requirement:** The ML pipeline must **integrate and handle** heterogeneous and complex data effectively.

---

## 4. Data Quality

- **Reality:** Real-world data is often **poor quality**: noisy, incomplete, inconsistent, with outliers and missing values.
- **Principle:** **Garbage in, garbage out.** Model quality depends heavily on input data quality.
- **Practice:** A large part of an ML project (often quoted ~80%) is **data cleaning and preparation**.
- **Requirement:** The pipeline must handle **noise**, **missing values**, **outliers**, **inconsistencies** (e.g. through data cleaning, imputation, robust methods).

---

## 5. Data Ownership and Distribution

- **Meaning:** In large organizations, data lives in **different departments/silos**. Ownership and sharing can be unclear or politically sensitive.
- **Challenge:** Building a **unified view** for ML may require integrating data across owners; this can create ownership and governance issues.
- **Requirement:** Data integration and access must respect **ownership** and **distribution** so that the project is technically and politically feasible.

---

## 6. Privacy

- **Problem:** Many datasets contain **sensitive or personal** information. Leaks or misuse cause harm and **legal** issues (e.g. GDPR).
- **Requirement:** Data must be **stored and processed** in an **ethical and legally compliant** way. The pipeline should support **privacy preservation** (e.g. anonymization, access control, secure processing).

---

## 7. Streaming and Diverse Data Types

- **Reality:** Data may arrive as **streams** (e.g. sensors, social media, finance) rather than as a single static batch.
- **Challenge:** Traditional batch-only systems may not handle **real-time** or **continuously flowing** data.
- **Requirement:** The pipeline should be able to handle **streaming data**, as well as **static**, **dynamic**, **image**, **video**, etc., as needed by the application.

---

## Module 1 Recap (Four Videos)

| Video | Focus |
|-------|--------|
| 1 | **Foundations:** What is ML, why ML, pipeline, workflows, data types. |
| 2 | **Supervised learning:** Classification and regression; training and testing. |
| 3 | **Unsupervised learning:** Clustering and association rule mining; finding patterns. |
| 4 | **Practical considerations:** Scalability, dimensionality, quality, heterogeneity, ownership, privacy, streaming. |

---

## Summary

- **Scalability:** System must handle growing data.
- **Dimensionality:** High dimensions and sparsity make learning harder; pipeline must account for this.
- **Heterogeneous/complex data:** Multiple sources and formats require integration and appropriate handling.
- **Data quality:** Poor quality → poor models; invest in cleaning and preparation.
- **Ownership & distribution:** Integration must respect organizational and data ownership.
- **Privacy:** Ethical and legal handling of sensitive data.
- **Streaming:** Support for real-time and varied data types when required.

Use this note for exam questions on “challenges in ML projects” and “what to consider when building an ML system.”
