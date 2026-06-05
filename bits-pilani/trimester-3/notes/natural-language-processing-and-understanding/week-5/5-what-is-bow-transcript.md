# Bag of Words (BoW)

## Intuition: A Multisets of Words

Bag of Words treats a document as a **multiset** (bag) of its words — like shaking a Scrabble tile bag and counting what fell out. Grammar, syntax, and word order are discarded entirely. What remains is **how many times** each word appears.

The name captures the metaphor: tip a document into a bag, shake it, and count the tiles. "The cat sat on the mat" and "mat the on sat cat the" produce identical bags.

---

## What BoW Answers

BoW answers two questions for each word in the vocabulary:

1. **Does this word appear in the document?**
2. **How many times?**

This is a step beyond one-hot encoding, which only answers the first question.

---

## Worked Example

**Corpus:**

| Document |
|----------|
| The cat sat on the mat |
| The dog sat on the log |
| Cats and dogs are enemies |

**Vocabulary (sample):** `the`, `cat`, `sat`, `on`, `mat`, `dog`, `log`, `cats`, `and`, `dogs`, `are`, `enemies`

**BoW vector for "The cat sat on the mat":**

| Word | Count |
|------|-------|
| the | 2 |
| cat | 1 |
| sat | 1 |
| on | 1 |
| mat | 1 |
| all others | 0 |

The word `the` appears twice — BoW records `2`, whereas one-hot encoding would record `1`.

```mermaid
flowchart LR
    D[Document] --> T[Tokenize]
    T --> C[Count Word Frequencies]
    C --> V[Align to Vocabulary]
    V --> B[BoW Vector]
```

---

## BoW vs One-Hot Encoding

| Aspect | One-Hot | Bag of Words |
|--------|---------|--------------|
| Values | 0 or 1 | Non-negative integers |
| Repeated words | Counted once | Counted each time |
| Information captured | Presence | Frequency |
| Word order | Lost | Lost |
| Semantics | None | None |

---

## Why BoW Persists in Production

Despite its simplicity, BoW remains useful in cloud ML pipelines for:

- **Spam detection** — keywords like "OTP", "lottery", "urgent" appear with characteristic frequencies
- **Topic routing** — support tickets classified by dominant term counts
- **Baseline models** — fast to build, easy to benchmark before investing in embeddings

BoW is a strong baseline: if a complex model cannot beat BoW on a keyword-driven task, the added complexity is not justified.

---

## Common Pitfalls / Exam Traps

- **"Bag of words preserves multiplicity but not order"** — a classic exam phrasing; multiplicity means repeat counts are kept.
- **Confusing BoW with TF-IDF** — BoW uses raw counts; TF-IDF scales counts by inverse document frequency.
- **Case and stemming matter** — `"Cat"` and `"cats"` are different dimensions unless normalized.
- **Identical BoW for different sentences** — "the man bit the dog" and "the dog bit the man" produce the same vector.

---

## Quick Revision Summary

- Bag of Words represents a document as word frequency counts over a fixed vocabulary.
- Word order and grammar are completely ignored; only multiplicity (count) is preserved.
- BoW extends one-hot encoding by recording frequency, not just presence.
- Effective for keyword-driven tasks like spam detection and simple classification.
- Does not capture semantics — related words remain unrelated in vector space.
- Serves as a fast, interpretable baseline in production ML pipelines.
