# Two-Tower Recommendation System

A minimal two-tower model for scalable retrieval: user and item towers output embeddings of the same dimension; relevance is the dot product. See [HLD.md](HLD.md) for design.

## Setup

```bash
cd training_experiments/recommendation_system
pip install -r requirements.txt
```

## Data

CSV format: `user_id,item_id` (one interaction per row).

**Option A – sample data (no download):**

```bash
python scripts/generate_sample_data.py
```

Creates `data/train.csv` and `data/eval.csv` with random pairs (for pipeline testing).

**Option B – real dataset from Kaggle (MovieLens):**

1. Install the Kaggle CLI and add your API key: [Kaggle API](https://www.kaggle.com/settings/account) → “Create New Token”, then place `kaggle.json` in `~/.kaggle/`.
2. Run the download script (uses MovieLens “latest small” by default):

```bash
pip install kaggle
python scripts/download_kaggle_movielens.py
```

This downloads the dataset from Kaggle, keeps ratings ≥ 4, splits into train/eval, and writes `data/train.csv` and `data/eval.csv`. For a larger dataset or subsampling:

```bash
python scripts/download_kaggle_movielens.py --dataset grouplens/movielens-20m-dataset --max-rows 500000
```

## Train

```bash
python -m src.train --config config/config.yaml
# or
./scripts/run_train.sh
```

Checkpoints go to `checkpoints/` (best model: `checkpoints/best.pt`).

## Embed (for serving)

**All items** (offline, to build an ANN index):

```bash
python -m src.embed items --checkpoint checkpoints/best.pt
# or
./scripts/run_build_index.sh
```

Saves `output/item_embeddings.pt` and `output/item_ids.pt`.

**One user** (online):

```bash
python -m src.embed user --checkpoint checkpoints/best.pt --user-idx 0
# or by raw ID (if vocab in checkpoint):
python -m src.embed user --checkpoint checkpoints/best.pt --user-id u42
```

## Evaluate

```bash
python -m src.evaluate --config config/config.yaml --checkpoint checkpoints/best.pt
# or
./scripts/run_eval.sh
```

Reports Recall@K, MRR, NDCG@K (K from `config.yaml` → `evaluate.k_values`).

## Config

Edit `config/config.yaml` for:

- `embedding_dim`, tower `hidden_dims`, `input_dim`
- `data.train_path`, `data.eval_path`
- `train.batch_size`, `epochs`, `learning_rate`
- `evaluate.k_values`

## Project layout

```
recommendation_system/
├── HLD.md
├── config/config.yaml
├── src/
│   ├── model.py      # Two-tower (user + item) model
│   ├── dataset.py    # (user_id, item_id) dataset
│   ├── train.py      # Training loop, in-batch negatives
│   ├── embed.py      # Embed items or one user
│   └── evaluate.py   # Recall@K, MRR, NDCG@K
├── scripts/
│   ├── run_train.sh
│   ├── run_build_index.sh
│   ├── run_eval.sh
│   ├── generate_sample_data.py
│   └── download_kaggle_movielens.py   # pull real MovieLens from Kaggle
├── data/             # train.csv, eval.csv (and data/raw/ after Kaggle download)
├── checkpoints/      # best.pt, epoch_*.pt
├── output/           # item_embeddings.pt, item_ids.pt
└── requirements.txt
```
