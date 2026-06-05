# Lab 1: Hugging Face Ecosystem and Text Generation Pipeline

## Why Hugging Face Matters

Hugging Face democratized AI development. Before centralized model hubs, building language models required massive in-house resources — data preparation, training pipelines, GPU infrastructure. Today, a few lines of code lets anyone download, experiment with, and deploy state-of-the-art models.

| Role | What Hugging Face Provides |
|------|---------------------------|
| **Model hub** | Thousands of community and enterprise models |
| **Dataset hub** | Real-world data for fine-tuning |
| **Open-source libraries** | Transformers, Datasets, Accelerate |
| **Community** | Continuous model improvements and sharing |

Mastering this ecosystem means learning how modern AI is actually built in industry — not reinventing models from scratch.

---

## Model Selection: DistilGPT-2

For the first lab, **DistilGPT-2** is the recommended starting model:

| Property | Value |
|----------|-------|
| Type | Compressed GPT-2 (distilled) |
| Size | Small, fast download |
| Hardware | Runs on CPU — no GPU required |
| Quality | Simple/imperfect text — ideal for learning |

**Selection principle:** Pick a model you can run easily, not the best model in the world. Validate the pipeline first; improve the model later.

---

## End-to-End Inference Pipeline

```mermaid
flowchart LR
    HF[Hugging Face Hub] --> DL[Download tokenizer + model]
    DL --> LOAD[Load into memory]
    LOAD --> TOK[Tokenize prompt]
    TOK --> GEN[model.generate]
    GEN --> DEC[tokenizer.decode]
    DEC --> OUT[Generated text]
```

### Step 1: Install Dependencies

```bash
# requirements.txt: transformers, torch
uv pip install -r requirements.txt
```

### Step 2: Download Model and Tokenizer

Two artifacts are downloaded:

| Artifact | Purpose |
|----------|---------|
| **Tokenizer** | Converts text ↔ token IDs the model understands |
| **Model weights** | The neural network parameters |

Both are saved to a local `models/` directory for offline use.

### Step 3: Load Model

Load tokenizer and model from the local directory. The model reports its parameter count — useful for understanding memory requirements.

### Step 4: Generate Text

```python
prompt = "Machine learning is"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs)
generated_text = tokenizer.decode(outputs[0])
```

| Step | What Happens |
|------|--------------|
| Tokenize | Text → token IDs |
| Generate | Model predicts next tokens autoregressively |
| Decode | Token IDs → human-readable text |

---

## Interpreting Output

DistilGPT-2 with short prompts produces simple or imperfect sentences. **This is expected and correct.**

| What to validate | What NOT to judge yet |
|------------------|----------------------|
| Model loads successfully | Sentence coherence |
| Prompt is tokenized | Factual accuracy |
| Text is generated | Response depth |
| Pipeline runs end-to-end | Production readiness |

A working pipeline with mediocre output is a **success** at this stage. Later modules improve prompts, models, and output control.

---

## Learning Approach

Hugging Face will be revisited throughout the curriculum. Each exposure focuses on one component:

- Model cards and selection
- Tokenization mechanics
- Inference patterns
- Fine-tuning workflows

Step-by-step repetition builds familiarity — not mastery in a single session.

---

## Common Pitfalls / Exam Traps

- Judging lab success by output quality instead of pipeline correctness
- Skipping local model save — re-downloads on every run waste time and bandwidth
- Confusing tokenizer and model — both are required; tokenizer handles text encoding, model handles prediction
- Choosing oversized models for local CPU execution — pipeline debugging becomes painfully slow

---

## Quick Revision Summary

- Hugging Face = model hub + datasets + libraries + community ecosystem
- DistilGPT-2: lightweight CPU-friendly model for pipeline learning
- Pipeline: download → load → tokenize → generate → decode
- Two artifacts: tokenizer (text↔tokens) and model (weights)
- Imperfect output is fine — validate that the pipeline works end-to-end
- Ecosystem mastery builds incrementally across the course
