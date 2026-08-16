# Sample Question Paper (Speculative — 3 of 2)

## BITS Digital Comprehensive Test

> **Note:** This is a speculative paper, constructed from the breadth of the course notes to help you practise patterns that did not appear in `sample-paper-01.md` or `sample-paper-02.md`. Question numbering and marks are indicative.

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

### Q.1.1 — Ambiguity in Language: Polysemy, Synonymy, and Why It Matters (5 Marks)

(a) Define **polysemy** and **synonymy**, each with an example. `[2 Marks]`

(b) Explain why these forms of ambiguity break a naive **word-lookup** NLP system, and how modern approaches handle them. `[3 Marks]`

#### Answer

**(a)**

- **Polysemy** — one word with **multiple related meanings**. Example: *bank* (river edge vs financial institution), or *dish* (food vs utensil).
- **Synonymy** — different words with **similar meanings**. Example: *happy* and *joyful*; *car* and *automobile*.

Both are properties of real language: meanings are fuzzy, overlapping, and context-dependent — not one-to-one word→concept mappings.

**(b)** A naive **word-lookup** system maps each surface form to one fixed entry (one vector, one dictionary meaning, one bag-of-words dimension). Polysemy breaks it because the same token needs *different* meanings in different contexts — a single representation must serve all senses, so it becomes a blurry average. Synonymy breaks it because *different* tokens share a meaning but get *separate* entries — the system cannot see that *car* and *automobile* are the same concept, so related text appears unrelated.

Modern approaches handle both with **context**:

- **Distributional/contextual embeddings** — Word2Vec puts synonyms near each other (shared contexts → similar vectors); BERT/GPT produce a *different vector per occurrence*, so polysemy is resolved per sentence.
- **N-grams and phrase handling** — bind words to their local context (e.g. `bank_of_river` vs `bank_loan`).

The unifying idea: meaning is determined by **context**, so representations that incorporate context resolve both ambiguity types.

**Pro tip:** Definition questions reward a crisp *one-liner + example* per term. Part (b) wants the *failure mechanism*: polysemy = one form, many meanings (representation overload); synonymy = many forms, one meaning (representation fragmentation). Then the modern fix is one word: **context**. Mentioning contextual embeddings resolves both in one move is the integrated answer.

---

### Q.1.2 — Corpus Bias and Representation (5 Marks)

(a) Describe two **types of corpus bias** with examples. `[2 Marks]`

(b) Explain how corpus bias manifests in trained NLP models, and give one pre-deployment mitigation. `[3 Marks]`

#### Answer

**(a)** Corpora are not neutral — they are written, selected, and labelled by humans. Two types:

- **Representation bias** — who appears, and how often, in the corpus. Example: under-represented demographics or dialects absent from training text.
- **Historical bias** — old texts reflect past norms. Example: stereotypical role language ("doctor is a man, nurse is a woman") baked into news from previous decades.
- (Also common: **source bias** — news vs social media vs academic text each have their own lens; **annotation bias** — human labelers inject subjectivity.)

**(b)** Models **absorb** corpus patterns rather than inventing them — *model bias ← corpus bias* (it is a **data problem before it is a model problem**). Manifestations:

- **Skewed predictions** — worse performance on under-represented groups.
- **Stereotypes in embeddings** — *doctor* closer to *man*, *nurse* closer to *woman*, because that is the co-occurrence pattern the corpus taught.
- **Unequal performance** — higher error rates on dialects that never appeared in training.

**Pre-deployment mitigation:** run a **bias audit before deployment** — evaluate metrics per demographic segment, check embedding fairness (e.g. bias probes), and document the corpus composition. Then fix the *data*: rebalance the corpus, add representative sources, or apply debiasing (e.g. projection-based embedding debiasing). Since the bias enters via data, the primary lever is data curation, not model tweaks.

**Pro tip:** The chain — *source → corpus → model → skewed predictions* — is the marks' skeleton. Part (b) needs (1) the absorbtion statement (bias is a data problem first), (2) two concrete manifestations (skewed predictions + stereotype embeddings), (3) a data-side mitigation. The doctor/nurse example is the canonical embedding-bias illustration.

---

## Q.2

### Q.2.1 — POS Tagging vs NER (6 Marks)

(a) Distinguish **Part-of-Speech (POS) tagging** from **Named Entity Recognition (NER)** in terms of the layer of language they analyse and their outputs. `[3 Marks]`

(b) Give two real-world applications of NER and explain the role of **context** in resolving entity spans (e.g. "Apple" the company vs "apple" the fruit). `[3 Marks]`

#### Answer

**(a)** POS tagging operates at the **syntactic/grammatical** layer — it assigns each token a part of speech (noun, verb, adjective). NER operates at the **semantic/real-world** layer — it identifies spans of tokens and classifies them as **entities** (PERSON, ORG, GPE/LOCATION, DATE, MONEY).

| | POS Tagging | NER |
|---|---|---|
| Layer | Syntactic / grammatical | Semantic / real-world |
| Output | Noun, verb, adjective, ... | PERSON, ORG, GPE, DATE, MONEY |
| Unit | Single token | Multi-token spans |
| Example | `Sundar`/`Prabhu` nouns, `is` verb | `Sundar Pichai` → PERSON, `Google` → ORG |

Example sentence *"Sundar Pichai is the CEO of Google"*: POS tags every token; NER labels `Sundar Pichai` as PERSON and `Google` as ORG.

**(b) Applications of NER:** information extraction (who did what, where, when), search & indexing, knowledge-graph construction, question answering, document analysis (resume parsing).

**Role of context in entity spans:** NER must decide whether a surface form is an entity and *which type*. `Apple` needs context — *"Apple released a new iPhone"* (ORG, capitalised, verb collocation) vs *"she ate an apple"* (common noun). Resolving this requires the **surrounding words**: capitalisation, verb agreement (`released`), and neighbouring tokens (`iPhone`, `ate`) — exactly why modern NER uses **contextual models (BiLSTM-CRF or BERT)** whose token representations incorporate the full sentence, rather than a lookup of "Apple → ORG".

**Pro tip:** The POS-vs-NER distinction is a *syntax vs semantics* one — state those two words and the table falls out. The Apple example carries part (b): the lesson is that NER is *context-dependent classification of spans*, not a gazetteer lookup. Mention the BiLSTM-CRF/BERT link to connect to paper 1's BiLSTM question.

---

### Q.2.2 — Tokenisation Challenges and Granularity (4 Marks)

(a) Explain why naive whitespace splitting is insufficient for tokenisation, with two examples. `[2 Marks]`

(b) Contrast **word-level** and **subword-level** tokenisation, and explain why transformer models (BERT/GPT) use subword tokenisers. `[2 Marks]`

#### Answer

**(a)** Whitespace splitting fails on:

- **Punctuation/contractions** — `"U.S.A."` vs `USA`; `don't` should split into `do` and `n't`; `state-of-the-art` is one concept but four hyphen-pieces.
- **Numbers, symbols, and Unicode** — `$1.2B`, version strings `v2.3`, URLs, emojis (multi-codepoint), and languages without spaces (Chinese) all resist naive splitting.

The choice of tokeniser is therefore **task- and language-dependent** — there is no single correct tokenisation.

**(b)** **Word-level** tokenisation splits on word boundaries and keeps whole words as tokens — simple, interpretable, but a **closed vocabulary**: new words, typos, and rare forms are out-of-vocabulary (OOV). **Subword-level** tokenisation (BPE, WordPiece) splits words into frequent **morpheme-like pieces** — `unhappiness` → `un`, `happi`, `ness`. Any word, seen or unseen, can be decomposed into in-vocabulary pieces, so **OOV largely disappears** and rare words are handled compositionally.

Transformers use subword tokenisers because they need a **fixed, manageable vocabulary** (a full word vocabulary would be huge and leaky), while still representing arbitrary text — including morphology and rare/compound words — through subword pieces. It also keeps the embedding matrix a reasonable size.

**Pro tip:** The examples carry the marks — `don't`, `U.S.A.`, `$1.2B` are the course's canonical whitespace-splitting failures. The word-vs-subword contrast is the *closed vs compositional* vocabulary idea; name BPE/WordPiece and one decomposition (`unhappiness` → `un`+`happi`+`ness`). This connects directly to paper 1's OOV question — reuse that knowledge.

---

## Q.3

### Q.3.1 — LDA Topic Modelling: Assumptions and Mechanics (6 Marks)

(a) State the **two core assumptions** of Latent Dirichlet Allocation (LDA) and illustrate them with an example. `[3 Marks]`

(b) Describe the **output** of LDA (topic proportions and topic–word distributions) and give two applications of topic modelling. `[3 Marks]`

#### Answer

**(a)** LDA's two core assumptions:

1. **Documents are mixtures of topics** — a document discusses several subjects in different proportions. Example: a tech-health article is 70% technology and 30% healthcare — LDA assigns *topic proportions*, not a single label.
2. **Topics are distributions over words** — each topic is defined by a probability distribution across the vocabulary. The technology topic weights `software`, `system`, `data`, `algorithm` highly; the healthcare topic weights `patient`, `treatment`, `hospital`, `care`.

LDA is **probabilistic** (outputs interpretable probability distributions), **interpretable** (topics described by top-weighted words), and **scalable** to large collections — which is why it dominates classical topic modelling.

**(b) Output of LDA** — for each document: a **topic-mixing vector** (e.g. doc = 70% tech + 30% healthcare); for each topic: a **word distribution** (top-weighted words that name the topic). You can inspect both: "what topics exist?" and "how is this document composed of topics?"

**Applications:** document **clustering/organisation** (grouping news or support tickets by theme), **corpus exploration** (discovering themes in a large collection), **information retrieval** (topic-based features for search), and **content recommendation** (matching documents on topic vectors).

**Pro tip:** The two assumptions are the answer's spine — restate them in exactly the course's phrasing ("documents are mixtures of topics; topics are distributions over words") and attach a concrete example. For part (b), the *two outputs* (document→topic proportions, topic→word distribution) map one-to-one to the two assumptions — noticing that symmetry is the expert move.

---

### Q.3.2 — LDA vs GSDMM vs BERTopic: Choosing a Topic Model (4 Marks)

A social-media analytics team must discover topics in a stream of short tweets. Compare **LDA**, **GSDMM**, and **BERTopic**, and recommend which to use for this corpus, with justification.

#### Answer

| | LDA | GSDMM | BERTopic |
|---|---|---|---|
| Assumption | Document = mixture of topics | One topic per document | Documents cluster by semantic embedding |
| Best for | Long documents, articles (hundreds+ words) | **Short text** (tweets, reviews, < 50 words) | Short or long text, semantic/synonym-aware |
| Method | Variational inference over word counts | Gibbs sampling (Dirichlet multinomial mixture) | BERT embeddings → UMAP → HDBSCAN → c-TF-IDF |
| Language dependence | Exact-word co-occurrence | Exact-word co-occurrence | Semantic (synonyms/paraphrases land together) |

**Why not LDA:** short tweets violate LDA's mixture assumption — a tweet typically expresses **one** theme, and with < 50 words there is insufficient co-occurrence signal for topic mixtures. **GSDMM** was designed for exactly this: one-topic-per-document over short text. **BERTopic** is the modern alternative — it embeds documents with a sentence transformer (so synonyms and paraphrases cluster together), reduces dimensionality with UMAP, clusters with HDBSCAN (which also flags outliers), and names topics with c-TF-IDF.

**Recommendation:** for tweets, either GSDMM or BERTopic beats LDA. Choose **GSDMM** for a simple, fast, interpretable baseline over exact words; choose **BERTopic** when semantic grouping matters (tweets about "Kubernetes scaling" and "container autoscaling" should land in one topic even with zero shared words) and you can afford the compute. If the team needs outlier handling and no fixed topic count, BERTopic's HDBSCAN is a further advantage.

**Pro tip:** The recommendation is *task-matched to text length and semantics*. The key sentence: "LDA assumes mixture + long text; GSDMM assumes one-topic-per-document for short text; BERTopic uses semantic embeddings so synonyms cluster." Mention that tweets violate the LDA mixture assumption — that is the reasoning examiners want, not just tool names.

---

## Q.4

### Q.4.1 — Decoding Strategies: Top-K, Top-P, and Temperature (6 Marks)

(a) Explain **temperature** and how it controls randomness at generation time. `[2 Marks]`

(b) Contrast **Top-K** and **Top-P (nucleus) sampling**, including the key advantage of Top-P. `[2 Marks]`

(c) A product needs **deterministic, format-consistent output** for a data-extraction task. Recommend decoding settings and justify them. `[2 Marks]`

#### Answer

**(a)** The LLM produces a probability distribution over the vocabulary at each step. **Temperature** scales the logits before softmax:

$$P(token_i) = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}$$

Low temperature ($T \to 0$) sharpens the distribution — the highest-probability token dominates → **deterministic, focused** output. High temperature flattens it → more **random, creative** output. Recommended: low (0.0–0.3) for coding/data extraction; higher for brainstorming/creative writing.

**(b)** **Top-K** restricts candidates to the **K most probable** tokens (fixed count), renormalises, and samples. K=1 = greedy decoding. **Top-P (nucleus)** selects the **smallest set of tokens whose cumulative probability reaches $p$** and samples from that — the candidate set **adapts dynamically** to the distribution shape. If the distribution is flat, Top-P keeps many tokens; if peaked, few. This adaptivity (Top-P keeps a sensible number of options regardless of K) is why **Top-P is the preferred strategy in industrial NLG**.

**(c)** For deterministic, format-consistent data extraction: use **greedy decoding or very low temperature** (e.g. $T \approx 0$–0.1) to make output reproducible, combined with **low Top-P** (e.g. 0.7) or small Top-K to suppress unlikely tokens. For *format consistency* specifically, also use **few-shot prompting** with examples matching the exact output schema — the course notes warn that sampling settings improve determinism but do not guarantee format, so a few well-chosen examples anchor the structure. And state the trade-off: deterministic settings reduce creativity/diversity, which is exactly what extraction wants.

**Pro tip:** The formula + the "sharpens vs flattens" intuition carries (a). The Top-P advantage is *dynamic candidate size* — state it as "Top-K fixes the count; Top-P adapts to the distribution." Part (c) rewards the *combined* answer: low temperature for determinism + few-shot examples for format (connecting to prompt engineering). Never claim greedy output is "guaranteed correct" — the course explicitly separates format consistency from correctness.

---

### Q.4.2 — Prompt Engineering: Zero-Shot, Few-Shot, and LLM Applications (4 Marks)

(a) Define **zero-shot** and **few-shot** prompting, and give one advantage and one limitation of each. `[2 Marks]`

(b) A legal team wants to summarise contracts with an LLM but is worried about hallucination. Briefly explain how **Retrieval-Augmented Generation (RAG)** or a similar grounding approach addresses this. `[2 Marks]`

#### Answer

**(a)** In prompting, a **"shot"** is an example in the prompt. **Zero-shot** = no examples, only instructions. **Few-shot** = 2–5 examples demonstrating the input–output pattern.

| | Zero-shot | Few-shot |
|---|---|---|
| Definition | Instructions only | 2–5 worked examples + instruction |
| Advantage | Simple, fast, low token cost | Strong format guidance, more consistent structure |
| Limitation | Output format may vary; inconsistent for structured tasks | Higher token cost; examples need to match the exact expected format |
| Best for | Open-ended tasks, brainstorming | Production classification, structured extraction, consistent formatting |

Key caveat from the notes: more shots improve **format consistency**, not guaranteed **correctness**.

**(b)** **RAG** grounds generation in external retrieval. Instead of the LLM answering purely from memorised weights (the source of hallucinated or stale facts), the system **retrieves relevant contract passages** from an indexed knowledge base and feeds them to the generator as context. The summary is then **anchored to the retrieved clauses**, and sources can be cited — an "open-book exam" rather than a "closed-book" one. This dramatically reduces (though does not fully eliminate) hallucination: the model is less likely to invent clause obligations when the actual clause text is in the prompt. It also means knowledge updates happen in the knowledge base, not by retraining the model.

**Pro tip:** The shot question is a table of *examples / advantage / limitation* — and always include the caveat "shots improve format consistency, not correctness" (a course trap). The hallucination answer keys on *open-book vs closed-book* and the phrase "anchors generation to retrieved evidence" — name retrieval + context + citation, not "it makes the model smarter."

---

## Closing Pro-Tip Recap

Across all three papers, the reusable exam patterns are:

- **Text representation** → compare methods on *what they capture* (presence/frequency/rarity/semantics), then match to the task.
- **Ambiguity & embeddings** → "context resolves ambiguity"; static = one vector, contextual = one per occurrence.
- **Sequences** → vanishing gradients → LSTM cell-state highway → GRU cheaper sibling → attention/transformers remove recurrence.
- **LLMs** → decoding settings control *randomness*, prompts control *format*, fine-tuning/RAG control *domain fit and grounding* — keep the three separate and you can answer any LLM question.
