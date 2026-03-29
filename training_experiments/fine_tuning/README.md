# Fine-tuning

Simple LLM fine-tuning on instruction/response JSONL using YAML configs.

## Project layout

```
llm-finetune/
│
├── configs/
│   ├── smollm2.yaml
│   ├── qwen2.yaml
│
├── data/
│   ├── support.jsonl
│   ├── docs.jsonl
│
├── train.py
├── dataset.py
├── model.py
└── utils.py
```

## How to run

1. **Install dependencies** (from this repo root or from `fine_tuning/`):

   ```bash
   cd training_experiments/fine_tuning/llm-finetune
   pip install -r requirements.txt
   ```

2. **Train with a config** (pick one):

   ```bash
   python train.py configs/smollm2.yaml
   ```

   or:

   ```bash
   python train.py configs/qwen2.yaml
   ```

   Outputs are written to `llm-finetune/outputs/<smollm2|qwen2>/`.

3. **Use your own data**: put JSONL files in `data/` (or elsewhere) and set the `dataset` path in the config. Each line must be JSON with `"instruction"` and `"response"` keys.
