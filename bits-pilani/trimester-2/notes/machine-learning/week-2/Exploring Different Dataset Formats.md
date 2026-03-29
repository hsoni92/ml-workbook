# Exploring Different Dataset Formats – Machine Learning (Module 2)

## Learning Objectives

By the end of this video you will:

1. **Distinguish** three main **data organization** types: **record**, **graph**, and **ordered** data.
2. **Describe** **record data** and its sub-types: **data matrix**, **document data**, **transactional data**.
3. **Describe** **graph data** (nodes, edges) and give examples (e.g. web, molecules).
4. **Describe** **ordered/sequence** data (order matters) and **spatio-temporal** data.
5. **Explain** why **structure** determines which **questions** and **analysis tools** we can use.

---

## Three Main Ways to Organize Data

After we **structure** raw information for storage and analysis, we get different **dataset formats**:

| Type | Organization | Typical use |
|------|--------------|------------|
| **Record data** | Table-like: rows = objects, columns = attributes | Most common; many ML algorithms |
| **Graph data** | Nodes + edges (relationships) | Networks, links, dependencies |
| **Ordered data** | Sequence where **order matters** | Time series, genomes, events |

---

## 1. Record Data

- **Definition:** A **collection of records** (data objects), each with a **fixed set of attributes**.
- **Tabular data** is the standard example: rows = records, columns = attributes.

Record data can be further categorized:

### Data Matrix

- **All attributes are numerical.**
- Can be thought of as an **m × n matrix**; each object is a point in an **n-dimensional** space.
- Used when we have only numeric features (e.g. for distance-based or linear algebra methods).

### Document Data

- **Objects = text documents** (e.g. news articles).
- Each document is often represented as a **term vector**: **attributes = distinct terms (words)** in the collection; value = count (or weight) of that term in the document.
- **Result:** Often a **sparse** matrix (most documents do not contain most terms).

### Transactional Data

- Each **record = one transaction** (e.g. one market basket).
- **Attributes are not fixed** in the same way: each record is a **set of items** that appear together (e.g. {bread, milk, coke}).
- **Example:** Supermarket: TID (transaction ID) + list of items bought. Used for **association rule mining** (e.g. “if bread and butter, then milk”).

---

## 2. Graph Data

- **When to use:** When **relationships between objects** are central; information is not only in the attributes of single objects but in **links** between them.
- **Structure:** **Nodes** = objects; **edges** = connections/relationships.
- **Examples:**
  - **World Wide Web:** Nodes = web pages, edges = hyperlinks. Used in **PageRank** and crawling.
  - **Molecules:** Nodes = atoms, edges = chemical bonds.
- **Analysis:** Graph algorithms (e.g. centrality, community detection, path finding).

---

## 3. Ordered Data

- **Definition:** Data where **order** of objects **matters** (e.g. first event, second event, …).
- **Examples:**
  - **Genome sequence** — sequence of bases (A, T, G, C).
  - **Time series** — values ordered by time.
  - **Spatio-temporal** — data with both **space** and **time** (e.g. location at each timestamp).

---

## Why Structure Matters

- The **structure** of the dataset determines:
  - **What questions** we can ask (e.g. “which items are bought together?” → transactional; “which pages link to this?” → graph).
  - **What analysis tools** we can apply (e.g. clustering on data matrix vs graph algorithms on graph data).
- **Choosing the right representation** is a **critical step** in a data pre-processing / ML project.

---

## Summary Table

| Format | Main idea | Sub-types / examples |
|--------|-----------|-----------------------|
| **Record** | Table: rows = objects, columns = attributes | Data matrix (all numeric), document (term vectors), transactional (item sets) |
| **Graph** | Nodes + edges | Web (pages + links), molecules (atoms + bonds) |
| **Ordered** | Order matters | Sequences, time series, spatio-temporal |

---

## Exam-Oriented Points

- **Record:** Tabular; data matrix (numerical), document (terms as attributes, sparse), transactional (sets of items).
- **Graph:** Nodes and edges; relationships are first-class (e.g. web, social network, molecules).
- **Ordered:** Sequence or time order matters (genome, time series, spatio-temporal).
- **Structure** drives **questions** and **tools** we can use.

Use this note for questions on “types of dataset formats” and “when to use record vs graph vs ordered data.”
