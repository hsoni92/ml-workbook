# AI Chatbot Evaluation Cheat Sheet

## 1. Classical NLP Evaluation Metrics

- **Precision / Recall / F1**
- **Accuracy** (low value for imbalanced data)
- **Confusion Matrix**
- **BLEU** → n-gram precision
- **ROUGE** → recall-oriented (ROUGE-1/2/L)
- **METEOR** → synonyms + stemming + better human alignment
- **Perplexity** → LM fluency
- **WER** → speech errors

---

## 2. LLM / GenAI Evaluation Techniques

### Reference-based
- BLEU, ROUGE, METEOR

### Embedding-based similarity
- Cosine similarity
- SBERT, BGE, MiniLM

### LLM-as-a-Judge
- Rubric scoring (accuracy, coherence, relevance, completeness)
- Rubrics: structured scoring criteria (1–5/1–10 per dimension)

### Reference-free eval
- LLM rubric scoring
- Toxicity/safety checks

### Hallucination detection
- Self-check prompts
- Retrieval grounding

---

## 3. RAG Evaluation

### Retrieval
- **Precision** = relevant retrieved / all retrieved
- **Recall** = relevant retrieved / total relevant
- Evaluate using: embeddings, recall@k, precision@k

### Answer Generation
- Semantic correctness: embeddings + LLM judge
- Label outputs as: **correct / partial / incorrect** → compute F1

---

## 4. Combining BLEU + ROUGE + Embedding + LLM Judge

- **BLEU** → phrase-level precision
- **ROUGE** → recall & structure
- **Embedding similarity** → semantic closeness
- **LLM judge** → factuality, reasoning, completeness
- **Weighted average** → final score

---

## 5. Prompt Injection Categories

### Direct
- Ignore instructions
- Command override
- Role confusion
- System prompt reveal

### Indirect
- Hidden malicious text in content (email, website, PDFs)
- RAG poisoning
- Upstream data attacks

### Jailbreak Attacks
- DAN prompts
- Role-play jailbreak
- Persona hijacking
- Multi-step deception

### Adversarial Attacks
- Unicode
- Typos
- Token boundary tricks

### Prompt Leakage
- Extract system prompts
- Chain-of-thought leakage

### Memory Manipulation
- "From now on remember X"

---

## 6. Chatbot Evaluation Dimensions

- Intent accuracy
- Entity extraction accuracy
- Context retention
- Coherence
- Relevance
- Safety
- Tone
- Latency

---

## 7. Adversarial / Negative Testing

- Paraphrase attacks
- Noise/typo attacks
- Distraction / long prompt overload
- Ambiguous inputs
- Out-of-scope detection
- Jailbreak scenarios

---

## 8. Test Plan for Chatbots

- Define expected flows
- Generate test utterances
- Regression tests
- Multilingual tests
- Negative tests
- Coverage evaluation (intents/entities/domain)
- LLM-judge scoring
- Load/performance testing

---

## 9. Platform Overviews

### Dialogflow
- Google's conversational AI platform
- Intent + entity models
- CX visual flow builder
- Used for web chat, voice bots, IVR
- **Peers**: Amazon Lex, Microsoft LUIS/Copilot Studio, IBM Watson, Rasa, Cognigy.ai, Kore.ai

### Rasa
- Open-source conversational AI framework
- Components: Rasa NLU + Rasa Core
- Full control, on-premise, custom ML pipelines
- Ideal for regulated industries and high customization

### Cyara
- Product-based SaaS
- CX assurance: IVR, voice, chatbots, digital channels
- Automated testing, regression, load, monitoring
- Botium → chatbot/LLM evaluation automation
- Used by enterprises for reliable customer experience

---

## 10. LLM Chatbot Drift

### What is LLM Chatbot Drift?

**Definition**: The phenomenon where a chatbot's behavior changes over time, even though developers did not change the model, prompts, or code.

**Symptoms**:
- Giving different answers
- Showing degraded accuracy
- Deviating from expected behaviors
- Losing consistency
- Violating tone or safety rules

**In short**: The bot "drifts" away from how it originally performed.

### Why Drift Happens in LLMs

1. **Model Updates** (External LLM providers)
   - OpenAI, Google, Anthropic silently upgrade or tweak models
   - Your prompts stay the same; model output changes → drift

2. **Retrieval Drift** (in RAG systems)
   - KB content changes
   - Embeddings updated
   - Chunking changes
   - Vector DB parameters change
   - → Retrieved documents differ → chatbot behaves differently

3. **Prompt or System Context Overload**
   - Long-term chat history changes meaning → bot responds differently

4. **Dependency Drift**
   - Changes in: tokenizers, temperature parameters, external APIs, grounding tools
   - → Shift outputs

5. **Pattern Drift Due to LLM Nondeterminism**
   - Even small randomness can accumulate across versions or multi-turn sessions

6. **Fine-tuning or System Policy Updates**
   - If the provider updates safety layers → style or depth changes

### Why Drift Is a Big Problem for Enterprises

- Breaks compliance
- Breaks customer support workflows
- Causes inconsistent quality
- Makes automated scripts or IVR/chat testing fail
- Leads to hallucinations or unexpected behaviors
- Cyara/Botium specifically tries to detect and block drift

### How to Test or Detect Chatbot Drift

1. **Regression Testing with Frozen Test Suites**
   - Run the same test questions daily/weekly → compare outputs

2. **Semantic Difference Analysis**
   - Use embedding similarity to detect output meaning shifts

3. **LLM Judge Comparison**
   - Judge new output vs baseline → score drop = drift

4. **Prompt Stability Tests**
   - Send paraphrases and variants → check consistency

5. **RAG Retrieval Monitoring**
   - Detect if retrieved documents changed (recall@k drift)

6. **Hallucination Tracking**
   - Monitor factual correctness over time

7. **User Behavior Telemetry**
   - Real-user interaction degradation signals drift

### Short One-Line Definition (Interview)

> "LLM Chatbot Drift is when a chatbot's responses change unexpectedly over time due to model updates, retrieval changes, or context effects—even though nothing in the bot's logic has changed."

---

## 11. LLM Chatbot Drift Detection Test Plan

### Objective
Detect behavioral changes in the chatbot over time by comparing current outputs with a validated baseline using lexical, semantic, and rubric-based evaluation.

### Scope
Drift detection covers:
- Intent detection
- Entity extraction
- RAG retrieval quality
- Response correctness
- Tone & style consistency
- Safety / policy alignment
- Multi-turn behavior
- Latency & stability

### Inputs
- **Baseline Dataset**: Frozen reference Q&A pairs from the bot's expected domain
- **Drift Test Suite**: canonical questions, paraphrases, adversarial variants, multi-turn flows
- **Baseline Responses**: Stored outputs from earlier stable version
- **Current Responses**: Latest outputs after model/provider changes

### Test Steps (Core Plan)

#### Step 1 — Run Regression Evaluation
- Run the entire test suite and compare: baseline_output vs current_output
- **Threshold**: semantic similarity drop > X% → drift

#### Step 2 — Semantics Drift Check
- Use embedding similarity: cosine(baseline, current)
- **If similarity < 0.85** → semantic drift

#### Step 3 — LLM-as-a-Judge Comparison
- Provide LLM with: question, baseline answer, new answer
- Ask: "Is the new answer worse, better or same?"
- **If judge score drops** → quality drift

#### Step 4 — Retrieval Drift (RAG Only)
- Measure: recall@k, precision@k, change in retrieved documents (ID diff)
- **If top-k retrieved chunks differ > 30%** → retrieval drift

#### Step 5 — Prompt Robustness Testing
- Send: paraphrase queries, noisy inputs, long queries, contradictory cues
- **If output variance increases** → robustness drift

#### Step 6 — Multi-turn Drift
- Replay multi-turn flows: Q1 → Q2 → Q3 → …
- Compare dialog state transitions against baseline
- **If the bot takes a different path** → dialog drift

#### Step 7 — Safety / Guardrail Drift
- Check: unwanted disclosures, refusal consistency, policy compliance
- **If safety behavior differs** → safety drift

#### Step 8 — Tone/Style Drift
- Check: politeness, professional tone, formatting consistency
- Use embedding + rule-based checks

#### Step 9 — Statistical Drift Trigger
- Track: F1 changes, intent accuracy drop, entity extraction drop, latency rose > threshold
- Triggers automated alert

### Metrics
- Embedding similarity (cosine)
- BLEU / ROUGE / METEOR (optional lexical checks)
- LLM Judge score
- Precision@k, recall@k for RAG
- Intent F1
- Entity F1
- Safety score
- Tone score
- Latency P95 / P99

### Pass/Fail Criteria
- Semantic similarity < 0.85 → **FAIL**
- LLM Judge rating drops > 20% → **FAIL**
- Retrieval recall drops > 15% → **FAIL**
- Intent F1 drops > 5% → **FAIL**
- Safety non-compliance → **FAIL**
- Tone inconsistency → Warning / FAIL depending on severity

### Reporting
Generate:
- Drift diff summary
- Per-test semantic shifts
- Per-turn dialog deviations
- Retrieval shifts
- Safety deviations
- Trend lines over time

### Automation
Schedule daily/weekly:
- Run drift test suite
- Compute trends
- Alert if thresholds crossed

Integrate with:
- Cyara/Botium test harness
- Dashboards
- Monitoring pipelines

### Short Interview Answer

> "Our drift detection test plan runs a frozen regression suite, compares baseline vs current outputs using semantic similarity, rubric scoring, and retrieval checks. We detect changes in intent accuracy, retrieval quality, safety behavior, tone, and multi-turn flows. Any significant drop in similarity or evaluation score signals drift."

---

## 12. Black-Box Chatbot Drift Detection

When you have zero internal access, you only test from the outside, using controlled inputs and analyzing outputs.

You treat the chatbot like: **Input → Output mapping** and detect if this mapping changes.

### Techniques

#### 1. Frozen Test Suite Regression (Core Method)
- Maintain a fixed set of test prompts
- Every day/week, send the exact same inputs to the chatbot
- If new outputs differ from previously stored baseline outputs → drift
- Detect differences via: exact match, lexical similarity (BLEU/ROUGE/METEOR), semantic similarity (embeddings), LLM-judge evaluation
- **This is the #1 method used in black-box testing**

#### 2. Semantic Drift Detection
- Even if wording changes, detect meaning changes using embedding similarity: cosine(baseline_output, new_output)
- **If similarity < threshold** → semantic drift
- Powerful because even "rephrased answers" can be drift

#### 3. Behavioral Drift via Multi-Turn Replay
- Replay recorded user journeys
- Example: User: "What is your refund policy?" → Bot: A → User: "How many days?" → Bot: B
- Store baseline sequence (A, B). Re-run the same conversation later
- **If the sequence deviates** → dialog drift
- Works without knowing internal logic

#### 4. Intent and Output Classification Drift
- Categorize outputs using your own classifier (not the bot's)
- Example classes: Correct, Irrelevant, Partial, Refusal, Fallback, Safety violation
- Compare classification accuracy over time
- **Changes → drift**
- You don't need access to the bot's internal intent system

#### 5. RAG Retrieval Drift (Black-Box Version)
- You cannot see the retrieved docs, but you can infer retrieval changes
- **Signs**: factual details change, examples provided change, domain knowledge fluctuates, specificity varies
- Example: "Explain Kafka retention policy." Week 1 answer → detailed, Week 3 answer → vague or missing key parts
- This indicates RAG drift even if you cannot see retrieval

#### 6. Safety/Tone Drift Monitoring
- Check if the bot: becomes more/less polite, refuses more/less questions, starts leaking information, becomes more/less compliant
- These are classification tasks on output text → compare across time
- Black-box friendly

#### 7. Latency Drift
- Measure: response times, P95/P99 latency, spike anomalies
- Higher latency → model/infra drift
- No internal access needed

#### 8. Statistical Drift Detection
- Track: F1 of your tests, embedding similarity mean, response length, refusal frequency, hallucination count, fallback rate
- Sudden shifts → drift
- All measurable from outputs only

### Short Interview Summary (Perfect Answer)

> "For a black-box chatbot, drift detection relies entirely on external behavior. We run a frozen regression test suite regularly, measure semantic differences between baseline and current outputs, replay multi-turn flows, classify outputs into correctness/safety categories, track refusal/fallback patterns, and monitor latency. Any change in behavior, semantics, or output quality across time signals drift—even without internal model access."

---

## 13. Interview Q&A Format

### 1. Drift, Robustness & Black-Box Testing

**Q: How would you evaluate a black-box chatbot?**
→ Treat it as I/O only; run frozen test sets, compare outputs using semantic + rubric scoring.

**Q: How do you detect drift without internals?**
→ Compare baseline vs current responses using embeddings + LLM judge + multi-turn replay.

**Q: How do you detect RAG failures without access?**
→ Look for changes in factuality, specificity, and domain grounding across regression runs.

**Q: How to design robustness tests for chatbots?**
→ Attack with paraphrases, noise, adversarial inputs, edge cases, and multi-turn variations.

**Q: How measure consistency across paraphrased queries?**
→ Compare answer embeddings and rubric scores across semantically equivalent prompts.

**Q: How evaluate multi-turn consistency?**
→ Replay conversation flows and ensure the state transitions match a baseline dialogue graph.

**Q: How detect hallucinations without ground truth?**
→ Use retrieval evidence, self-consistency checks, and LLM-as-a-judge factuality scoring.

### 2. Testing & Evaluation Automation

**Q: How to automate chatbot evaluation at scale?**
→ Create scheduled test pipelines that run regression suites and auto-score outputs.

**Q: How to combine BLEU/ROUGE/Embeddings/LLM Judge?**
→ Normalize all metrics to 0–1 and compute a weighted composite score.

**Q: How detect when bot gives inconsistent answers over time?**
→ Store baseline outputs and detect semantic similarity drift.

**Q: How to evaluate NLU without labeled data?**
→ Cluster outputs semantically and manually validate representative samples.

**Q: How evaluate LLM agent workflows?**
→ Test tool-calling accuracy, action grounding, and reasoning steps via scripted tasks.

**Q: How design a safety evaluation framework?**
→ Use a rubric scoring system + adversarial prompts + refusal consistency checks.

### 3. Prompt Injection / Jailbreak / Adversarial Attacks

**Q: Categories of prompt injection?**
→ Direct overrides, indirect injections, jailbreaks, adversarial perturbations, leakage.

**Q: How detect jailbreak attempts automatically?**
→ Classify outputs for role-switching, safety-bypass patterns, or DAN-style behavior.

**Q: How quantify risk if bot has no guardrails?**
→ Use red-team prompts and score outputs on safety, harmfulness, and policy violations.

**Q: How adversarial-test a black-box chatbot?**
→ Feed noise, obfuscation, paraphrases, unicode, trick prompts, role-play attacks.

**Q: How design fuzzing tests for LLMs?**
→ Auto-generate thousands of mutated queries and detect failure patterns statistically.

### 4. RAG Evaluation & Failures

**Q: How evaluate retrieval quality?**
→ Compute precision@k, recall@k, and embedding-based relevance scoring.

**Q: How measure hallucination severity in RAG?**
→ Compare answer facts vs retrieved evidence using LLM judge.

**Q: How detect vector DB drift without access?**
→ Watch for changing factuality or answer specificity across regressions.

**Q: How evaluate grounding correctness?**
→ Use citation consistency + evidence alignment scoring.

**Q: How measure RAG relevance vs completeness?**
→ Score which essential facts are included vs missing using LLM rubrics.

### 5. Chatbot Behavior & Product-Oriented Evaluation

**Q: How test on-brand tone/style?**
→ Use LLM judge rubric for tone similarity and persona consistency.

**Q: How verify compliance rules?**
→ Provide compliance test cases and detect deviations via rule-based scoring.

**Q: How evaluate fallback behavior?**
→ Trigger unknown/ambiguous inputs and measure fallback correctness and frequency.

**Q: How evaluate multilingual bots?**
→ Test parallel prompts and compare semantic parity across languages.

**Q: How evaluate bot performance under load?**
→ Run concurrent calls + track latency, timeout rate, and answer degradation.

### 6. Rubrics, Judges & Scoring Systems

**Q: How design a rubric?**
→ Choose criteria (accuracy, relevance, completeness) + scoring scale + weights.

**Q: How detect drift in LLM judges?**
→ Keep a control set of judge prompts and analyze score variance over time.

**Q: How calibrate multiple LLM judges?**
→ Evaluate same samples across judges and normalize via score alignment.

**Q: When trust vs not trust LLM-as-a-judge?**
→ Trust for qualitative tasks; don't trust for strict factual accuracy without grounding.

**Q: How combine multiple metrics into one score?**
→ Normalize → weight → aggregate via mean or weighted harmonic mean.

### 7. Edge Cases & Real-World Failures

**Q: Bot fails only on a tiny subset — what do you do?**
→ Cluster failure cases, identify patterns, expand tests around them.

**Q: How test bots dependent on APIs/tools?**
→ Validate tool call correctness, error recovery, and fallback paths.

**Q: How evaluate bot using private embeddings you can't see?**
→ Compare answers for consistency and completeness across known factual prompts.

**Q: How detect tone/personality drift?**
→ Track tone embeddings + rubric scoring across time.

**Q: How evaluate ambiguity handling?**
→ Provide ambiguous prompts and ensure the bot asks clarifying questions.

---

## 14. Testing Domain Knowledge

### 1. Regression Testing
**Link to chatbots**: "We run regression suites to detect behavioral drift across LLM versions."

### 2. Black-Box Testing
**Link**: "We treat external chatbots as black boxes and use input–output differential testing."
This shows Cyara-style thinking.

### 3. Differential Testing
Compare baseline vs current outputs.
**Line**: "Differential testing helps detect semantic drift without internal access."

### 4. Functional Testing
**Link**: "We validate the bot's functional correctness — does it answer the question, extract entities, follow flows."

### 5. Non-Functional Testing
Cyara cares heavily about this.
**Includes**: Performance testing, Load testing, Latency/P95/P99, Stress testing, Stability testing
**Line**: "To detect non-functional drift, we monitor latency variation and response-time degradation under load."

### 6. Behavior-Driven Testing (BDD)
You can simulate conversational flows as: Given → When → Then
**Line**: "We design multi-turn conversational tests using BDD-style scenarios to ensure dialog integrity."

### 7. Negative Testing
Feed invalid, noisy, adversarial prompts.
**Line**: "Negative tests help detect robustness drift — especially for safety and fallback behavior."

### 8. Exploratory Testing (AI-Assisted)
LLMs generate edge cases → you test them.
**Line**: "We use AI-driven exploratory testing to uncover novel failure modes that weren't part of the test plan."

### 9. Fuzz Testing
Random/mutated prompts.
**Line**: "Fuzz testing exposes hidden prompt-injection vulnerabilities and semantic instability."

### 10. Mutation Testing
Intentionally modify prompts to ensure model stability.
**Line**: "Mutation testing helps evaluate if small paraphrase changes break the bot's output."

### 11. Canary Testing
Roll out model changes to a small traffic slice.
**Line**: "We catch early drift using canary testing before full rollout."

### 12. A/B Testing
Compare two LLM versions live.
**Line**: "A/B evaluations detect preference drift between model versions."

### 13. Test Coverage Analysis
Intent coverage, entity coverage, scenario coverage.
**Line**: "We measure NLU coverage to ensure every intent/entity combination is robust across variants."

### 14. Root Cause Analysis (RCA)
For regressions or drifts.
**Line**: "Post-drift RCA helps determine whether the cause is model updates, retrieval changes, or safety layer shifts."

### 15. SLA/SLO Testing
Reliability metrics: uptime, latency, response success
**Line**: "We test SLO compliance such as bot answer accuracy threshold (≥90%) and latency (P95 < 1.5s)."

---

## 15. How to Combine These Into SUPER Answers

### Example 1 — Drift Detection

**Vanilla answer**: "We test outputs for drift using embeddings."

**Super upgraded answer**: "We apply black-box differential regression testing, compare baseline vs current outputs using semantic similarity, and run non-functional tests like latency drift. We also maintain canary tests and mutation testing to evaluate paraphrase robustness."

### Example 2 — Testing RAG Bots

**Vanilla**: "We check retrieval precision."

**Super upgraded**: "RAG evaluation uses retrieval precision@k, functional correctness on answers, evidence-grounding checks, and negative testing for OOD prompts. We measure coverage across document clusters and run exploratory fuzzing to detect injection vulnerabilities."

### Example 3 — Prompt Injection Mitigation

**Vanilla**: "I validate the bot using adversarial prompts."

**Super upgraded**: "We perform security-focused negative testing, adversarial fuzzing, role-play mutation tests, and run a safety SLO validation suite to ensure the bot rejects jailbreak attempts consistently."

---

## 16. Final One-Liner (MUST USE)

> "I combine classical QA methods (regression, fuzzing, black-box differential testing) with NLP evaluation (semantic similarity, LLM judges, retrieval metrics) to create an end-to-end chatbot assurance framework."

---

## Quick Reference: Key Metrics & Thresholds

| Metric | Threshold | Use Case |
|--------|-----------|----------|
| Semantic Similarity (cosine) | < 0.85 = FAIL | Drift detection |
| LLM Judge rating drop | > 20% = FAIL | Quality drift |
| Retrieval recall drop | > 15% = FAIL | RAG drift |
| Intent F1 drop | > 5% = FAIL | NLU drift |
| Top-k retrieved chunks differ | > 30% = retrieval drift | RAG drift |
| Latency P95 | < 1.5s (SLO) | Performance |
| Answer accuracy | ≥ 90% (SLO) | Quality |

---

## Quick Reference: Evaluation Stack

```
Input → Chatbot → Output
         ↓
    [Evaluation Layer]
         ↓
┌────────────────────────┐
│ Lexical Metrics        │
│ • BLEU                 │
│ • ROUGE                │
│ • METEOR               │
└────────────────────────┘
┌────────────────────────┐
│ Semantic Metrics       │
│ • Embedding similarity │
│ • SBERT/BGE/MiniLM     │
└────────────────────────┘
┌────────────────────────┐
│ LLM-as-a-Judge         │
│ • Rubric scoring       │
│ • Factuality checks    │
└────────────────────────┘
┌────────────────────────┐
│ RAG Metrics            │
│ • Precision@k          │
│ • Recall@k             │
│ • Grounding checks     │
└────────────────────────┘
         ↓
    [Weighted Composite Score]
```

