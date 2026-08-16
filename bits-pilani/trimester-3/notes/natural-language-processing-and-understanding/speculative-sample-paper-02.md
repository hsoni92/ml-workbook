# Sample Question Paper (Speculative — 2 of 2)

## BITS Digital Comprehensive Test

> **Note:** This is a speculative paper, constructed from the breadth of the course notes to help you practise patterns that did not appear in `sample-paper-01.md`. Question numbering and marks are indicative.

| Field | Value |
|-------|-------|
| Course No. | |
| Course Title | Natural Language Processing (NLP) |
| Nature of Exam | Closed Book (No Internet) |
| Weightage | 40% |
| Duration | 2.5 Hours |
| Date of Exam | |

### Note to Students

1. Please follow all the Instructions to Candidates given on the cover page of the answer book.
2. Read each question carefully and write to-the-point answer.
3. All parts of a question should be answered consecutively. Each answer should start from a fresh page.
4. Assumptions made if any, should be stated clearly at the beginning of your answer.
5. Show all the calculations/derivations in fair and box/highlight the final answer.

---

## Q.1

### Q.1.1 — One-Hot Encoding, BoW, and TF-IDF Compared (5 Marks)

Compare **one-hot encoding**, **Bag-of-Words**, and **TF-IDF** as sparse text vectorization methods. For a spam-classification task, recommend which to use and justify your choice.

#### Answer

| Aspect | One-Hot | Bag-of-Words | TF-IDF |
|--------|---------|--------------|--------|
| Values | 0 or 1 (presence) | Non-negative integers (counts) | Floats (count × rarity weight) |
| Frequency captured | No | Yes | Yes (weighted) |
| Common-word handling | Manual stopword removal | Manual stopword removal | Automatic downweighting (IDF → ~0) |
| Word order / semantics | Lost | Lost | Lost |
| Feature dimension | Vocabulary size | Vocabulary size | Vocabulary size |

One-hot answers *"does the word appear?"*; BoW answers *"how many times?"*; TF-IDF answers *"how often here, and how rare globally?"* — $\text{TF-IDF}(x,d) = \text{TF}(x,d) \times \log\frac{N}{\text{DF}(x)}$, so a word in every document (IDF → 0) is downweighted while a rare, distinctive term is boosted.

**Recommendation for spam classification: TF-IDF** (optionally with unigram+bigram features). Spam detection is a **keyword-driven task**, and TF-IDF's strength is exactly this: it automatically downweights generic words (`the`, `is`) and boosts spam-signalling terms (`lottery`, `OTP`, `urgent`, `click`) that are rare in normal mail but concentrated in spam. Compared to BoW, it needs less manual stopword tuning; compared to one-hot, it captures frequency. A TF-IDF + linear model remains a strong, interpretable production baseline for keyword tasks.

**Pro tip:** The comparison table + "which and why" is the classic paper-1-complement question. The *why* must be task-matched: spam is keyword-driven, so TF-IDF's rare-term boosting wins. One sentence on the limitation (still no semantics — "car"/"automobile" stay orthogonal) shows you know where it stops, which is often worth the last mark.

---

### Q.1.2 — The Preprocessing Pipeline: Ordering, Stemming vs Lemmatization (5 Marks)

(a) Give the recommended **order** of steps in a text preprocessing pipeline, and explain why stopword removal must come after tokenisation. `[2 Marks]`

(b) Contrast **stemming** with **lemmatization**, and state which you would use for a sentiment-analysis model, with justification. `[3 Marks]`

#### Answer

**(a) Recommended order:**

Raw text → **normalise case** (lowercase) → **noise removal** (regex) → **tokenise** → **remove stopwords** → **stem/lemmatise** → (optional) phrase handling → processed tokens.

**Why stopwords after tokenisation:** stopword lists operate on **tokens**, not raw text. `stopwords.words('english')` contains word forms (`the`, `is`, `and`); you can only filter tokens once the text has been split into them. Also, normalising and cleaning before tokenisation prevents HTML fragments or punctuation becoming tokens, and lemmatising after stopwords is more efficient (fewer tokens to lemmatise).

**(b)** **Stemming** is a fast **heuristic chop** (Porter, Snowball) that removes affixes by rules — `computing` → `comput`; it can produce non-words (`studies` → `studi`). **Lemmatization** uses a **dictionary + POS** to return the true base form — `running` (verb) → `run`, `studies` → `study`.

| | Stemming | Lemmatization |
|---|---|---|
| Method | Rule-based truncation | Dictionary + POS lookup |
| Speed | Fast | Slower |
| Output | Possibly non-words | Valid dictionary words |
| Accuracy | Can over-merge (`university`/`universe`) | Linguistically correct |

**For sentiment analysis: lemmatization** (or careful stemming). Sentiment features benefit from valid, consistent word forms, and over-stemming can merge words with different polarities into one feature. But note the practical trap: for sentiment, **negation words must be preserved** (do not stem/remove `not`), which matters more than the stem-vs-lemma choice.

**Pro tip:** The pipeline-order question is scored on *why*, not just the sequence — give one rationale per step boundary (clean-before-tokenise prevents HTML tokens; stopwords-after-tokenise because lists are token-level; lemmatise-after-stopwords for efficiency). The stem-vs-lemma contrast is a table + a task-matched choice; naming the over-stemming failure (`university`/`universe`) is the expert mark.

---

## Q.2

### Q.2.1 — Word2Vec: CBOW vs Skip-gram and Embedding Arithmetic (6 Marks)

(a) Contrast the **CBOW** and **Skip-gram** architectures of Word2Vec, including their training direction and which handles rare words better. `[3 Marks]`

(b) Explain how the learned vectors support analogies such as *king − man + woman ≈ queen*. `[3 Marks]`

#### Answer

**(a)** Word2Vec is a **shallow** neural network (single hidden layer) trained on a prediction task; the hidden-layer weight rows become the embeddings.

- **CBOW** (Continuous Bag of Words): input = **context words**, output = **target word**. It averages the context vectors and predicts the centre word — "fill in the blank" (`the cat __ on the mat` → `sat`). Faster to train, but weaker on rare words.
- **Skip-gram**: input = **target word**, output = **context words**. Given `sat`, predict `the`, `cat`, `on`, `mat`. Slower, but generates more training examples per word and handles **rare words better**.

| | CBOW | Skip-gram |
|---|---|---|
| Direction | Context → target | Target → context |
| Speed | Faster | Slower |
| Rare words | Less effective | Better |
| Best for | Large clean corpora | Smaller corpora, rare terms |

**(b)** Words appearing in similar contexts get similar vectors, so directions in vector space encode **relationships**. The difference vector $r = \mathbf{v}_{\text{man}} - \mathbf{v}_{\text{woman}}$ (or the reverse) encodes the "gender" relationship; the same relationship transposes across pairs:

$$\mathbf{v}_{\text{king}} - \mathbf{v}_{\text{man}} + \mathbf{v}_{\text{woman}} \approx \mathbf{v}_{\text{queen}}$$

Similarly, $\mathbf{v}_{\text{Delhi}} - \mathbf{v}_{\text{India}}$ encodes a "capital city" relationship that transposes to $\mathbf{v}_{\text{Moscow}} - \mathbf{v}_{\text{Russia}}$. The analogy works because the training objective pushed words with similar co-occurrence patterns to arrange into parallel offset structures in the embedding space.

**Pro tip:** The direction flip (CBOW: many→one, Skip-gram: one→many) is the most common trap — state it explicitly. For the analogy, show the equation and the "relationship transposes across pairs" insight; adding the capital-city example (Delhi − India + Russia ≈ Moscow) demonstrates understanding beyond memorising one equation.

---

### Q.2.2 — Static vs Contextual Embeddings and Polysemy (4 Marks)

The word *"bank"* appears in *"the bank of the river"* and *"the bank approved my loan"*. Explain why a **static embedding** (Word2Vec/GloVe) cannot distinguish these, and how a **contextual embedding** (BERT/GPT) resolves the ambiguity.

#### Answer

**Static embeddings (Word2Vec, GloVe)** assign **one fixed vector per word** regardless of context. Whether *bank* means the river edge or a financial institution, the model returns the *same* vector — the polysemy is crushed into a single averaged meaning. Static embeddings therefore cannot resolve homonyms; they reflect corpus-wide co-occurrence, not sentence meaning.

**Contextual embeddings (BERT, GPT)** produce a **different vector for each occurrence**, computed from the surrounding context. The representation of *bank* in *"bank of the river"* is pushed toward water/river-related semantics; in *"approved my loan"* it is pushed toward financial semantics. The notes' canonical example is *dish*: alone it is ambiguous (food or utensil), but `Indian rice dish with spices and meat` shifts the embedding near biryani. Every additional context word shifts the embedding via relationship-vector steps.

| | Static | Contextual |
|---|---|---|
| Vectors per word | 1 (fixed) | One per occurrence |
| Polysemy handling | Poor | Excellent |
| Mechanism | Lookup table | Full-sentence forward pass (attention) |

**Pro tip:** Polysemy questions reward the *one-vector-per-word vs one-vector-per-occurrence* contrast. Give a second example (the *dish* → biryani progression) to show depth. One sentence on *why* — static reflects global co-occurrence, contextual uses bidirectional attention — is the differentiating mark.

---

## Q.3

### Q.3.1 — Vanishing Gradients and How LSTMs Solve Them (6 Marks)

(a) Explain the **vanishing gradient problem** in vanilla RNNs and its practical effect on long sequences. `[3 Marks]`

(b) Explain how the LSTM architecture's **gates** and **cell state** address this problem. `[3 Marks]`

#### Answer

**(a)** During training, the error must be propagated **backward through time** (BPTT) from the last timestep to the first. By the chain rule, the gradient at an early step is a **product of many per-step gradient factors**, each potentially $< 1$. Multiplying many small numbers drives the gradient toward zero — it **vanishes**. Practical effect: the RNN cannot learn long-range dependencies and effectively has **short-term memory**. It can predict *"the clouds are in the ___"* → `sky`, but fails to connect *"I grew up in France"* (word 1) to *"I speak fluent ___"* → `French` (word 100). The model is effectively amnesic beyond a few tokens.

**(b)** The LSTM separates **long-term storage (cell state $C_t$)** from **short-term output (hidden state $H_t$)**. The cell state is a **"highway"** that runs through the entire chain with minimal transformation, so gradients flow backward through it **largely unchanged** — this is the mechanism that avoids vanishing.

Three gates control the flow:

- **Forget gate** — what to discard from $C_t$ (sigmoid, 0 = forget, 1 = keep).
- **Input gate** — what new information to write into $C_t$ (sigmoid gates values, tanh proposes candidates).
- **Output gate** — what to reveal from $C_t$ into $H_t$.

Because information can be *added* and *removed* by gates instead of being repeatedly multiplied, long-range context can survive the sequence — LSTM handles long paragraphs and translation inputs that defeat vanilla RNNs. (Caveat from the notes: the cell state *mitigates* the problem; extreme cases can still struggle.)

**Pro tip:** The mechanism is the *multiplicative chain* — a product of many $<1$ gradients → zero. The LSTM answer hinges on the **cell-state highway with gates that add/remove, not just multiply**. Never say "LSTM has three gates: forget, input, cell" — the cell state is the highway, not a gate (course trap). Use the France→French example to make the consequence concrete.

---

### Q.3.2 — GRU vs LSTM (4 Marks)

Compare the **GRU** with the **LSTM**. Given a compute-constrained deployment, which would you prefer and why?

#### Answer

**GRU is LSTM's leaner sibling.** It merges the LSTM's cell state and hidden state into a **single hidden state** and reduces the three LSTM gates to **two gates**:

- **Update gate** — a combined forget + input decision ("how much of the past to keep and how much new information to let in").
- **Reset gate** — how much of the past to ignore when computing the candidate state.

| Component | LSTM | GRU |
|-----------|------|-----|
| Memory stores | Cell state + hidden state | Hidden state only (merged) |
| Gates | 3 (forget, input, output) | 2 (update, reset) |
| Parameters | More | Fewer |
| Training speed | Slower | Faster |
| Long-sequence performance | Slightly better | Comparable |

**Recommendation for compute-constrained deployment: GRU.** It delivers **comparable** long-sequence performance with fewer parameters and faster training/inference, which matters when memory or latency is limited. Prefer LSTM when you need the marginal extra capacity on very long sequences and can afford the compute. In practice the difference is often small, so the cheaper model wins unless evidence shows otherwise.

**Pro tip:** The table is the answer — 2 gates vs 3, one memory vs two, comparable accuracy at lower cost. The *why* must be compute-matched: fewer parameters → faster, and comparable accuracy means the cheaper option is usually the right default. One line on when to choose LSTM anyway (slightly better on very long sequences) shows balanced judgment.

---

## Q.4

### Q.4.1 — BERT: Pre-training, Bidirectionality, and Fine-Tuning (6 Marks)

(a) Describe BERT's two pre-training objectives, **Masked Language Modeling (MLM)** and **Next Sentence Prediction (NSP)**, and explain why MLM makes BERT **bidirectional**. `[3 Marks]`

(b) Explain how BERT is **fine-tuned** for a downstream task such as sentiment classification or NER, and why fine-tuning requires far less data than training from scratch. `[3 Marks]`

#### Answer

**(a)** BERT is a **stack of Transformer encoder blocks** (encoder-only). It is pre-trained with two **self-supervised** objectives on raw text (Wikipedia + BooksCorpus):

- **MLM:** randomly mask ~15% of tokens and predict them from **both left and right context**. For "The cat [MASK] on the mat", the label `sat` depends on `cat`, `on`, and `mat` simultaneously. This is what makes BERT **bidirectional** — unlike GPT's strictly left-to-right decoder. (Detail: of selected tokens, 80% are replaced with `[MASK]`, 10% with a random word, 10% unchanged — reducing train/serve mismatch.)
- **NSP:** given a sentence pair, predict whether the second sentence follows the first. This teaches **inter-sentence relationships**, critical for QA, NLI, and summarisation.

**(b)** **Fine-tuning** adds a small **task-specific head** on top of the pre-trained encoder (a classification layer for sentiment on the `[CLS]` token, a token-level classifier for NER) and trains it on labelled data. Because the encoder already contains **rich linguistic knowledge** learned from billions of tokens, fine-tuning only adapts the final layers to the task — so it needs **far fewer labels** than training from scratch, where the model would have to rediscover language structure before it can learn the task. The notes cite a typical pattern: fine-tuning on ~50k labelled reviews beats a BoW classifier trained from scratch.

**Pro tip:** MLM + bidirectional is the top BERT fact — state it as *"predict masked words from both sides → bidirectional; GPT is causal/left-to-right."* The fine-tuning answer hinges on **transfer learning**: pre-train once (self-supervised, cheap labels), fine-tune for tasks (small labelled data) — mention the `[CLS]`/token-level head to show you know how the head connects to the task.

---

### Q.4.2 — Sentiment Analysis: Granularity and Challenges (4 Marks)

(a) Distinguish **document-level**, **sentence-level**, and **aspect-based** sentiment analysis (ABSA), with an example. `[2 Marks]`

(b) Describe two challenges (e.g. negation, sarcasm) that break naive lexicon-based sentiment systems, and how a model-based approach addresses them. `[2 Marks]`

#### Answer

**(a)** Granularity levels:

| Level | What gets labelled | Example |
|-------|--------------------|---------|
| **Document-level** | One label for the whole text | Movie review → positive/negative/neutral |
| **Sentence-level** | Each sentence gets its own label | Multi-sentence review: sentence 1 positive, sentence 2 negative |
| **Aspect-based (ABSA)** | Per-aspect labels within a sentence | *"The food was great, but the service was slow"* → food: positive, service: negative |

Use cases: document-level for rating dashboards; sentence-level for fine-grained long-form feedback; ABSA for restaurants/e-commerce tracking sentiment per feature (battery, camera, delivery).

**(b)** Two challenges that break naive lexicon systems:

- **Negation:** *"This movie is not good"* — a lexicon scores `good` as positive, inverting the meaning. Fix: preserve negation words and/or use bigrams (`not_good`), which contextual models learn automatically.
- **Sarcasm:** surface words are positive while intent is negative (*"Great, another silent upgrade"*). Fix: full-sentence context is required — a model that reads the whole sentence (especially bidirectional attention, e.g. BERT) can weigh contradictory cues.

The shift is from **word-level rules** to **context-aware models**: lexicon methods treat words independently, while model-based approaches (n-gram features or contextual encoders) capture composition — the interaction of words — which is exactly where negation and sarcasm live.

**Pro tip:** Part (a) is a three-row table with a concrete example — the food/service ABSA example is the canonical one. Part (b) rewards *mechanism*: negation breaks independence (word-level scoring), sarcasm breaks surface polarity — both are fixed by *compositional context*. Mention the bigram fix (ties back to Q.1.1 in paper 1) for an integrated answer.
