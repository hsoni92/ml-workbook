# Natural Language Processing — Revision Mind Map

> Everything important, in acronyms and one-liners. Pair with `sample-paper-01.md` and the speculative papers for exam patterns.

## Core Concepts

```
NLP = computers process/analyse natural language
NLU = understand (meaning)  ·  NLG = generate (text)
```

- **Morphology** — words = **stems + affixes** (prefixes, suffixes); morphology studies word formation
- **Ambiguity** — **polysemy** (one word, many senses: *bank*) vs **synonymy** (many words, one sense: *car/automobile*)
- **Pipeline order matters** — tokenisation → noise removal (regex) → stopword removal → stemming/lemmatisation → vectorise

## Preprocessing

| Step | What it does | Trap |
|------|-------------|------|
| **Tokenisation** | Split text into units (words, subwords, chars) | Wrong tokenisation poisons every downstream step |
| **Noise removal** | Regex to strip URLs, HTML, numbers, punctuation | Over-cleaning destroys meaning |
| **Stopword removal** | Drop function words (*the, is, at*) | **Never remove negation words** (*not, never*) — flips sentiment |
| **Stemming** | Rule-based chop: *running → run* | Over-stemming → non-words (*studies → studi*) |
| **Lemmatisation** | Dictionary-based: *running → run* (valid word) | Slower than stemming, needs POS context |

- **OOV (out-of-vocabulary)** — word not in vocabulary; fixed by **sub-word tokenisation** (BPE: byte-pair encoding)

## Vectorisation & Embeddings

| Method | Type | Answers | Limits |
|--------|------|---------|--------|
| **One-hot** | Sparse, vocabulary-sized | Does the word appear? | No frequency, no semantics, huge dims |
| **BoW** (Bag-of-Words) | Sparse counts | How many times? | Loses order → *not good* ≈ *good* |
| **TF-IDF** | Sparse weighted counts | How often here + how rare globally? | Still no semantics; corpus-dependent |

$$\text{TF-IDF}(x,d) = \text{TF}(x,d) \times \log\frac{N}{\text{DF}(x)}$$

- **Word2Vec** (dense, learned) — **CBOW** (predict word from context) vs **Skip-gram** (predict context from word); analogy: $king - man + woman \approx queen$
- **GloVe** — global co-occurrence matrix factorisation
- **Static vs Contextual** — static = one vector per word (polysemy fails); contextual = one vector per occurrence via attention (BERT)

## Sequential Models

- **Seq2Seq** — encoder compresses input → **information bottleneck** (fixed vector for variable-length input); fix = **attention**
- **RNN** — hidden state carries context; problem = **vanishing/exploding gradients** (early context forgotten)
- **LSTM** — **cell state highway** + 3 gates (forget/input/output) solves vanishing gradient
- **GRU** — cheaper sibling (2 gates, no separate cell state)
- **Architecture patterns** — many-to-one (sentiment), one-to-many (caption), many-to-many (translation)

## Transformers & Attention

$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

- **Q**uery = what am I looking for · **K**ey = what do I contain · **V**alue = what do I pass
- **Self-attention** — every token attends to every token, **fully bidirectional** in encoder; enables **coreference** (*it → animal*)
- **Multi-head** — heads run in parallel; each learns a pattern (syntax, coreference, collocation)
- **Positional encoding** — injects order (self-attention has no inherent order)
- **Decoder** — **masked/causal** attention (only past tokens) for autoregressive generation
- **Families** — encoder (BERT), decoder (GPT), encoder-decoder (T5)

## BERT & Sentiment

- **BERT** — bidirectional encoder; pre-training tasks = **MLM** (masked language model) + **NSP** (next sentence prediction); fine-tune `[CLS]` → softmax
- **Variants** — RoBERTa (more data, no NSP), ALBERT (parameter sharing), DistilBERT (distilled, faster)
- **Sentiment levels** — document, sentence, aspect-based
- **VADER** — rule-based lexicon (fast, no training, handles social media slang)
- **BERT sentiment** — full-sentence bidirectional attention
- **Challenges** — **negation** (*not good*), **sarcasm** (positive words, negative intent → needs full context)

## Topic Modelling

| Method | Approach | Best for |
|--------|----------|----------|
| **LDA** | Probabilistic mixtures (words ↔ topics ↔ docs) | Long documents |
| **GSDMM** | One-topic-per-doc (Dirichlet multinomial mixture) | Short text (tweets) |
| **BERTopic** | Embed → **UMAP** → **HDBSCAN** → **c-TF-IDF** → optional **MMR** | Semantic, handles outliers |

- BERTopic trap: it is not "BERT + LDA" — the pipeline is fundamentally different; c-TF-IDF computes IDF **per cluster**

## LLMs & Decoding

- **Decoder-only dominance** — GPT-style causal LMs excel at NLG (next-token prediction)
- **Sampling strategies** — **greedy** (always max prob, deterministic), **beam search** (keep top-B paths)
- **Temperature** $T$ — scales logits before softmax: low $T$ = sharp/deterministic, high $T$ = flat/creative; keep in 0–1 for production
- **Top-K** — restrict to K most-likely tokens (fixed count)
- **Top-P** — cumulative probability mass (dynamic count; default ≈ 0.9)
- **Guideline** — low $T$ for coding/extraction; high $T$ for creative; never high $T$ for JSON/structured output

## Prompting

- **Prompt components** — role/instruction, context, task, examples, output format
- **Zero-shot** — no examples · **One-shot** — 1 example · **Few-shot** — 2+ examples (best for format anchoring)
- **Guidelines** — be specific, constrain format, give examples matching the schema, test after parameter changes

## Formula Cheat Sheet

| Formula | Expression |
|---------|-----------|
| TF-IDF | $\text{TF}(x,d) \times \log\frac{N}{\text{DF}(x)}$ |
| Attention | $\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$ |
| Temperature | softmax over logits $\div T$ |
| Word2Vec analogy | $king - man + woman \approx queen$ |
