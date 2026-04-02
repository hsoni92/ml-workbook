# Where ANNs are Used – Artificial Neural Networks (Module 1)

## Learning Objectives

By the end of this video you will:

1. **Identify** the major real-world domains where Artificial Neural Networks are widely used.
2. **Explain** how neural networks operate on different types of data.
3. **Recognize** why ANNs are the default choice for modern AI systems.

---

## Prerequisite: Connecting Theory to the Real World

So far in this module we have studied **what neural networks are**, **how single neurons work**, and **how feed-forward networks are structured**. Now it is important to connect these ideas to the real world.

Neural networks are **not just academic models**. They are the **core engines** behind most modern AI systems that we interact with every day. By looking at these applications, you will understand **what types of problems** neural networks are especially good at and **why they have become the dominant approach** in artificial intelligence. In this video we survey the major domains where artificial neural networks are the **default modeling choice**.

---

## Computer Vision

### Input and Output

In **computer vision**, the **input** to the model is **raw pixel data** and the **output** can be:

- An **object label** (e.g. “cat”, “car”),
- A **bounding box** (location of an object in the image), or
- A **segmentation map** (pixel-level labeling of the image).

### Automatic Feature Learning

Neural networks **automatically learn visual features** directly from the pixels. They do not rely on hand-designed features:

- **Early layers** learn simple structures: **edges** and **textures**.
- **Deeper layers** learn **shapes**, **objects**, and **full scenes**.

This ability to automatically learn visual representations from raw pixels is why **convolutional neural networks (CNNs)** have become the **backbone** of computer vision.

### Applications

| Application | Role of neural networks |
|-------------|-------------------------|
| **Face recognition** | Learn identity from face images. |
| **Medical image diagnosis** | Detect anomalies, lesions, or conditions from X-rays, MRI, etc. |
| **Autonomous driving perception** | Recognize lanes, vehicles, pedestrians, and obstacles from camera/sensor data. |

> **Exam tip:** In vision, think **raw pixels → automatic feature learning**. Link “edges → textures → shapes → objects → scenes” to **CNNs** and to the **hierarchical** nature of visual representation.

---

## Speech and Natural Language Processing

### Speech Systems

In **speech**, neural networks are used for:

- **Speech-to-text** (transcription),
- **Voice assistants** (e.g. wake word, intent, dialogue),
- **Speaker identification** (who is speaking).

### Natural Language Processing

In **NLP**, they power:

- **Chatbots**,
- **Machine translation**,
- **Text summarization**,
- **Large language models (LLMs)**.

### Why Neural Networks Fit Language and Speech

Language and speech data are **sequential** and **highly contextual**. The meaning of a word or sound often depends on what came before and after. Neural networks—especially **recurrent networks** and **transformers**—are very effective at modeling:

- **Temporal structure** (order of elements in time),
- **Long-range dependencies** (relationships between distant parts of the sequence).

This is what enables machines to **understand and generate human language at scale**.

### Domain vs Tasks vs Architecture

| Domain | Example tasks | Typical architecture |
|--------|----------------|----------------------|
| **Speech** | Speech-to-text, voice assistants, speaker ID | RNNs, transformers |
| **NLP** | Chatbots, translation, summarization, LLMs | RNNs, transformers |

> **Exam tip:** **Sequential + contextual data** → use **RNNs or transformers**. Key idea: **long-range dependencies** in time or text.

---

## Recommendation and Personalization

Whenever you watch a movie on **Netflix**, a video on **YouTube**, or browse products on **Amazon**, neural networks are working in the background to **predict what you are most likely to engage with next**.

### What the Systems Learn

These systems learn:

- **Representations of users** (preferences, behavior patterns),
- **Representations of items** (movies, videos, products),
- **Complex interaction patterns** between users and items.

### Business Impact

The business impact is large: even **small improvements** in recommendation quality can lead to **large gains** in:

- User **engagement**,
- **Retention**,
- **Revenue** for these companies.

> **Exam tip:** **Recommendation systems** = learning **user representations** + **item representations** + **interaction patterns**; NNs excel at this.

---

## Industrial and Critical Domains

Beyond consumer applications, neural networks are widely used in **critical industrial domains**. In all of them, they learn from **large volumes of complex, high-dimensional data** where **traditional models struggle**.

### Domain Overview

| Domain | Applications | Data type |
|--------|--------------|-----------|
| **Finance** | Fraud detection, credit scoring, algorithmic trading | Transactions, time series, market data |
| **Healthcare** | Medical image analysis, disease risk prediction, clinical decision support | Images, EHR, time series |
| **Autonomous systems and robotics** | Perception, control, navigation | Images, LiDAR, sensor streams |
| **Manufacturing** | Predictive maintenance, defect detection | Sensor data, images |

### Summary by Domain

- **Finance:** Fraud detection, credit scoring, algorithmic trading.
- **Healthcare:** Medical image analysis, disease risk prediction, clinical decision support.
- **Autonomous systems and robotics:** Perception, control, navigation.
- **Manufacturing:** Predictive maintenance and defect detection from **sensor and image data**.

---

## Data Types and Architectures (How NNs Operate on Different Data)

Neural networks operate on **different types of data** by using **architectures** suited to the structure of the data:

| Data type | Example | Typical architecture |
|-----------|---------|----------------------|
| **Images / spatial** | Pixels, medical scans | **CNNs** (convolutional neural networks) |
| **Sequences** (speech, text) | Audio waveform, sentences | **RNNs**, **transformers** |
| **Tabular / vectors** | User features, sensor summaries | **Feed-forward** networks |

This is how NNs “operate on different types of data”: the **architecture** is chosen to match **spatial**, **temporal**, or **flat** structure.

---

## Why ANNs Dominate: Four Fundamental Reasons

Neural networks dominate these application areas for a few **fundamental reasons**:

1. **Learn directly from raw, high-dimensional data** — e.g. images, audio, text, and sensor signals; no need to manually reduce dimensionality first.
2. **Automatic feature learning** — they learn useful representations from data instead of relying on **handcrafted features**.
3. **Scale with data and compute** — performance generally improves with more data and more computational power.
4. **End-to-end optimization** — the **entire system** can be **trained jointly** for the **final objective**; no need to optimize each stage separately.

**End-to-end optimization** means: from raw input to final output, one differentiable pipeline is trained together, so the model can learn the best internal representations for the task.

> **Exam tip:** “Default choice for modern AI” → **scalability** + **end-to-end optimization** + **automatic feature learning**. Contrast with handcrafted features and multi-stage non-joint systems.

---

## Module Summary and Next Video

### Summary of This Video

- Neural networks are the **core engines** of modern AI systems.
- They power real-world applications ranging from **finance** to **autonomous vehicles** (vision, speech, NLP, recommendation, and industry).
- **Scalability** and **end-to-end optimization** are what make them the **default choice** for so many applications.

### Next Video

In the next video we will look at the **current limitations** of neural networks and why those limitations **motivated the development of deeper and more advanced models**.
