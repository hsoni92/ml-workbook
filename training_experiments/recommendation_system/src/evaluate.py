"""
Offline evaluation: Recall@K, MRR, NDCG@K on a holdout set.

For each (user, item) pair in the eval set we compute user and item embeddings,
score all items for that user, and measure whether the positive item is in top-K.
"""

import argparse
import csv
import sys
from pathlib import Path

import torch
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.dataset import load_vocab_from_csv
from src.model import TwoTower


def load_config(config_path: str) -> dict:
    path = Path(config_path)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_model_from_checkpoint(ckpt_path: str, device: torch.device):
    """Load model from checkpoint (same as embed.py)."""
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    cfg = ckpt["config"]
    model = TwoTower(
        num_users=ckpt["num_users"],
        num_items=ckpt["num_items"],
        user_id_embed_dim=cfg["user_tower"]["input_dim"],
        user_hidden_dims=cfg["user_tower"]["hidden_dims"],
        item_id_embed_dim=cfg["item_tower"]["input_dim"],
        item_hidden_dims=cfg["item_tower"]["hidden_dims"],
        embedding_dim=cfg["embedding_dim"],
    )
    model.load_state_dict(ckpt["model_state_dict"])
    model.eval()
    return model, ckpt


def recall_at_k(scores: torch.Tensor, positive_idx: int, k: int) -> float:
    """1 if positive is in top-k, else 0. scores: (num_items,)."""
    _, topk = torch.topk(scores, min(k, scores.size(0)))
    return 1.0 if positive_idx in topk.tolist() else 0.0


def mrr(scores: torch.Tensor, positive_idx: int) -> float:
    """1 / (1-based rank)."""
    rank = (scores > scores[positive_idx]).sum().item() + 1
    return 1.0 / rank if rank > 0 else 0.0


def ndcg_at_k(scores: torch.Tensor, positive_idx: int, k: int) -> float:
    """DCG@K for single relevant item: 1/log2(rank+1) if rank <= K else 0."""
    rank = (scores > scores[positive_idx]).sum().item() + 1
    if rank > k:
        return 0.0
    return 1.0 / (torch.log2(torch.tensor(rank, dtype=torch.float)) + 1.0).item()


def main():
    parser = argparse.ArgumentParser(description="Evaluate two-tower model on holdout set")
    parser.add_argument("--config", type=str, default="config/config.yaml")
    parser.add_argument("--checkpoint", type=str, default="checkpoints/best.pt")
    parser.add_argument("--eval-path", type=str, default=None, help="Override eval CSV path")
    args = parser.parse_args()

    cfg = load_config(args.config)
    eval_cfg = cfg.get("evaluate", {})
    k_values = eval_cfg.get("k_values", [1, 5, 10, 20])

    eval_path = args.eval_path or cfg["data"].get("eval_path", "data/eval.csv")
    eval_path = Path(eval_path)
    if not eval_path.is_absolute():
        eval_path = PROJECT_ROOT / eval_path
    if not eval_path.exists():
        raise FileNotFoundError(f"Eval data not found at {eval_path}")

    ckpt_path = Path(args.checkpoint)
    if not ckpt_path.is_absolute():
        ckpt_path = PROJECT_ROOT / ckpt_path
    if not ckpt_path.exists():
        raise FileNotFoundError(f"Checkpoint not found at {ckpt_path}")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model, ckpt = load_model_from_checkpoint(str(ckpt_path), device)
    model = model.to(device)

    data_cfg = cfg.get("data", {})
    user_col = data_cfg.get("user_id_column", "user_id")
    item_col = data_cfg.get("item_id_column", "item_id")

    # Eval must use train vocab only (model was trained with fixed num_users, num_items)
    user2idx = ckpt.get("user2idx")
    item2idx = ckpt.get("item2idx")
    if user2idx is None or item2idx is None:
        train_path = Path(cfg["data"]["train_path"])
        if not train_path.is_absolute():
            train_path = PROJECT_ROOT / train_path
        user2idx, item2idx = load_vocab_from_csv(
            str(train_path),
            user_id_column=user_col,
            item_id_column=item_col,
        )

    # Load eval pairs; keep only those with user and item in train vocab
    eval_pairs = []
    with open(eval_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            u = str(row[user_col]).strip()
            i = str(row[item_col]).strip()
            if u in user2idx and i in item2idx:
                eval_pairs.append((user2idx[u], item2idx[i]))
    if not eval_pairs:
        raise ValueError("No eval pairs found with user and item in train vocab.")

    # Precompute all item embeddings once
    num_items = ckpt["num_items"]
    with torch.no_grad():
        item_ids = torch.arange(num_items, device=device, dtype=torch.long)
        item_embeddings = model.item_tower(item_ids)  # (num_items, emb_dim)

    recall_sums = {k: 0.0 for k in k_values}
    mrr_sum = 0.0
    ndcg_sums = {k: 0.0 for k in k_values}
    n = 0

    with torch.no_grad():
        for user_idx, item_idx in eval_pairs:
            user_t = torch.tensor([[user_idx]], device=device, dtype=torch.long)
            user_emb = model.user_tower(user_t).squeeze(0)  # (emb_dim,)
            scores = torch.matmul(user_emb.unsqueeze(0), item_embeddings.T).squeeze(0)

            for k in k_values:
                recall_sums[k] += recall_at_k(scores.cpu(), item_idx, k)
            mrr_sum += mrr(scores.cpu(), item_idx)
            for k in k_values:
                ndcg_sums[k] += ndcg_at_k(scores.cpu(), item_idx, k)
            n += 1

    print(f"Evaluated on {n} pairs")
    print("Recall@K:")
    for k in k_values:
        print(f"  Recall@{k}: {recall_sums[k] / max(n, 1):.4f}")
    print(f"MRR: {mrr_sum / max(n, 1):.4f}")
    print("NDCG@K:")
    for k in k_values:
        print(f"  NDCG@{k}: {ndcg_sums[k] / max(n, 1):.4f}")


if __name__ == "__main__":
    main()
