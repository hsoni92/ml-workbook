# Building Blocks of Data – Objects, Attributes and Types – Machine Learning (Module 2)

## Learning Objectives

By the end of this video you will:

1. **Define** dataset, data objects, and the role of **attributes**.
2. **Distinguish** rows (tuples/records) vs columns (attributes/features).
3. **Classify** attributes as **nominal**, **ordinal**, **interval**, and **ratio**.
4. **State** which **mathematical operations** are valid for each attribute type.
5. **Define** **discrete** vs **continuous** attributes.

---

## Dataset and Data Objects

- **Dataset:** A **collection of data objects** stored in a **structured** way (e.g. table).
- **Why structure?** Large data (e.g. millions of transactions) must be stored and retrieved efficiently; structure enables that.
- **Examples:** Bank passbook (date, transaction ID, credit, debit, balance), sales DB, medical DB, university DB.

In a **table**:

- **Rows** = data points = **records / tuples / cases / samples / entities / instances**.
- **Columns** = **attributes** (or **features**). Each attribute describes a **property or characteristic** of the data object.
- A **single object** is described by the **collection of attribute values** in one row.

---

## Attributes and Attribute Values

- **Attribute:** A property or characteristic of a data object. Synonyms: attribute, feature.
- **Attribute value:** The specific number or symbol assigned to that attribute for a given object (e.g. Refund = Yes, Marital status = Single, Taxable income = 125).
- Different attributes can have different **numbers of unique values** (e.g. Refund: 2; Marital status: 3; Taxable income: many/numerical).

---

## Two Broad Categories of Attributes

| Category | Also known as | Measures | Sub-types |
|----------|----------------|----------|-----------|
| **Qualitative** | Categorical | Quality / category | Nominal, Ordinal |
| **Quantitative** | Numerical | Quantity / amount | Interval, Ratio |

---

## The Four Attribute Types (Detail)

### 1. Nominal

- **Meaning:** Values are **labels or names** used only to **distinguish** one object from another. No order, no magnitude.
- **Operations:** **Equality only** — equal to (＝) and not equal to (≠).
- **Examples:** ID number, colour (blue, green), zip code. We can only say two values are same or different.

### 2. Ordinal

- **Meaning:** Values can be **ranked or ordered** (ascending/descending). **Distance between values has no meaning** (e.g. “how much better” is not defined).
- **Operations:** **Equality + order** — ＝, ≠, &lt;, &gt;, ≤, ≥.
- **Examples:** Grade (A, B, C, D, F), rank (1, 2, 3), height (tall, medium, short).

### 3. Interval

- **Meaning:** **Differences** between values **have meaning** and can be measured in a **fixed unit**. No true zero for ratios (e.g. 0°C is not “no temperature”).
- **Operations:** **Equality + order + addition/subtraction** — ＝, ≠, &lt;, &gt;, ＋, －.
- **Examples:** Calendar date, temperature (Celsius/Fahrenheit). e.g. “Date 2 − Date 1 = 1 day” is meaningful.

### 4. Ratio

- **Meaning:** Has all properties of **interval** plus a **true zero**; **ratios** of values are meaningful (e.g. “twice as long”).
- **Operations:** **Equality + order + addition/subtraction + multiplication/division** — ＝, ≠, &lt;, &gt;, ＋, －, ×, ÷.
- **Examples:** Length, time, count, distance (e.g. 1000 km × 10 = 10,000 km total).

---

## Summary: Operations by Type

| Type | Distinctness (＝, ≠) | Order (&lt;, &gt;) | Addition/subtraction | Multiplication/division |
|------|------------------------|---------------------|------------------------|--------------------------|
| **Nominal** | ✓ | ✗ | ✗ | ✗ |
| **Ordinal** | ✓ | ✓ | ✗ | ✗ |
| **Interval** | ✓ | ✓ | ✓ | ✗ |
| **Ratio** | ✓ | ✓ | ✓ | ✓ |

---

## Discrete vs Continuous Attributes

| Type | Meaning | Example |
|------|---------|---------|
| **Discrete** | **Finite or countable** number of distinct values | Zip code, binary (0/1), grade (A–F) |
| **Continuous** | **Infinite** possible values (e.g. real numbers) | Temperature (10, 10.1, 10.11, …), age, weight |

- **Discrete:** Cardinality is finite or countable.
- **Continuous:** Values can be arbitrarily fine (e.g. 10.111…).

---

## Exam-Oriented Points

- **Rows** = tuples/records; **columns** = attributes/features.
- **Nominal:** only same/different; **ordinal:** + order; **interval:** + difference; **ratio:** + ratio and true zero.
- **Discrete** = finite/countable values; **continuous** = infinite possible values.
- Always ask: “Which operations are valid?” for a given attribute type.

Use this note for definitions and for choosing correct operations and attribute types in exam questions.
