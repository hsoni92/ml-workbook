"""
Training loop for the two-tower model.

Uses in-batch negatives: for a batch of B (user, item) pairs, we get B user
embeddings and B item embeddings. The similarity matrix is BxB; diagonal
entries are positives. We apply cross-entropy loss (each row: softmax over
scores, target = diagonal index).
"""

import argparse
import sys
from pathlib import Path

import torch
import torch.nn.functional as F
import yaml
from torch.utils.data import DataLoader

# Add project root so we can run as: python -m src.train
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.dataset import RecommendationDataset
from src.model import TwoTower


def load_config(config_path: str) -> dict:
    """Load YAML config; paths can be relative to project root."""
    path = Path(config_path)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    with open(path, "r") as f:
        cfg = yaml.safe_load(f)
    return cfg


def in_batch_negative_loss(
    user_emb: torch.Tensor, item_emb: torch.Tensor
) -> torch.Tensor:
    """
    For batch of B pairs: logits = user_emb @ item_emb.T (B x B).
    Positive for row i is column i. Cross-entropy with targets = [0,1,...,B-1].
    """
    logits = torch.matmul(user_emb, item_emb.T)
    # Scale down logits for stable softmax (temperature)
    logits = logits / max(user_emb.size(-1) ** 0.5, 1e-6)
    batch_size = user_emb.size(0)
    targets = torch.arange(batch_size, device=logits.device, dtype=torch.long)
    return F.cross_entropy(logits, targets)


def main():
    parser = argparse.ArgumentParser(description="Train two-tower recommendation model")
    parser.add_argument(
        "--config",
        type=str,
        default="config/config.yaml",
        help="Path to config YAML",
    )
    args = parser.parse_args()

    cfg = load_config(args.config)
    train_cfg = cfg["train"]
    data_cfg = cfg["data"]
    model_cfg = cfg

    # Resolve data paths
    train_path = Path(data_cfg["train_path"])
    if not train_path.is_absolute():
        train_path = PROJECT_ROOT / train_path
    if not train_path.exists():
        raise FileNotFoundError(
            f"Train data not found at {train_path}. Create data/train.csv with user_id,item_id columns."
        )

    user_col = data_cfg.get("user_id_column", "user_id")
    item_col = data_cfg.get("item_id_column", "item_id")

    # Dataset and vocab
    train_ds = RecommendationDataset(
        str(train_path),
        user_id_column=user_col,
        item_id_column=item_col,
    )
    num_users = train_ds.num_users
    num_items = train_ds.num_items

    train_loader = DataLoader(
        train_ds,
        batch_size=train_cfg["batch_size"],
        shuffle=True,
        num_workers=0,
        pin_memory=True,
    )

    # Model
    model = TwoTower(
        num_users=num_users,
        num_items=num_items,
        user_id_embed_dim=model_cfg["user_tower"]["input_dim"],
        user_hidden_dims=model_cfg["user_tower"]["hidden_dims"],
        item_id_embed_dim=model_cfg["item_tower"]["input_dim"],
        item_hidden_dims=model_cfg["item_tower"]["hidden_dims"],
        embedding_dim=model_cfg["embedding_dim"],
    )
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=train_cfg["learning_rate"])

    # Checkpoint dir
    ckpt_dir = Path(train_cfg["checkpoint_dir"])
    if not ckpt_dir.is_absolute():
        ckpt_dir = PROJECT_ROOT / ckpt_dir
    ckpt_dir.mkdir(parents=True, exist_ok=True)

    # Training loop
    best_loss = float("inf")
    for epoch in range(train_cfg["epochs"]):
        model.train()
        total_loss = 0.0
        num_batches = 0
        for user_ids, item_ids in train_loader:
            user_ids = user_ids.to(device)
            item_ids = item_ids.to(device)
            optimizer.zero_grad()
            user_emb, item_emb = model(user_ids, item_ids)
            loss = in_batch_negative_loss(user_emb, item_emb)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            num_batches += 1

        avg_loss = total_loss / max(num_batches, 1)
        print(f"Epoch {epoch + 1}/{train_cfg['epochs']}  loss={avg_loss:.4f}")

        if avg_loss < best_loss:
            best_loss = avg_loss
            save_path = ckpt_dir / "best.pt"
            torch.save(
                {
                    "model_state_dict": model.state_dict(),
                    "config": cfg,
                    "num_users": num_users,
                    "num_items": num_items,
                    "user2idx": train_ds.user2idx,
                    "item2idx": train_ds.item2idx,
                    "epoch": epoch + 1,
                },
                save_path,
            )
            print(f"  Saved best checkpoint to {save_path}")

        if (epoch + 1) % train_cfg.get("save_every_n_epochs", 1) == 0:
            torch.save(
                {
                    "model_state_dict": model.state_dict(),
                    "config": cfg,
                    "num_users": num_users,
                    "num_items": num_items,
                    "user2idx": train_ds.user2idx,
                    "item2idx": train_ds.item2idx,
                    "epoch": epoch + 1,
                },
                ckpt_dir / f"epoch_{epoch + 1}.pt",
            )

    print("Training done.")


if __name__ == "__main__":
    main()
