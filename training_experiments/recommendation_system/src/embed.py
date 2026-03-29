"""
Embedding scripts for serving.

Mode 1: Embed all items -> save item embeddings and item IDs (for ANN index).
Mode 2: Embed one user -> return user embedding (for online lookup).
"""

import argparse
import sys
from pathlib import Path

import torch

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.model import TwoTower


def load_checkpoint(ckpt_path: str, device: torch.device):
    """Load model and metadata from checkpoint."""
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


def run_embed_items(args):
    """
    Run all item IDs through the item tower; save embeddings and item IDs.
    Used offline to build an ANN index (e.g. FAISS).
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    ckpt_path = Path(args.checkpoint)
    if not ckpt_path.is_absolute():
        ckpt_path = PROJECT_ROOT / ckpt_path
    model, ckpt = load_checkpoint(str(ckpt_path), device)
    model = model.to(device)

    num_items = ckpt["num_items"]
    embed_cfg = ckpt["config"].get("embed", {})
    out_emb_path = Path(embed_cfg.get("item_embeddings_path", "output/item_embeddings.pt"))
    out_ids_path = Path(embed_cfg.get("item_ids_path", "output/item_ids.pt"))
    if not out_emb_path.is_absolute():
        out_emb_path = PROJECT_ROOT / out_emb_path
    if not out_ids_path.is_absolute():
        out_ids_path = PROJECT_ROOT / out_ids_path
    out_emb_path.parent.mkdir(parents=True, exist_ok=True)

    batch_size = args.batch_size
    all_embeddings = []
    with torch.no_grad():
        for start in range(0, num_items, batch_size):
            end = min(start + batch_size, num_items)
            item_ids = torch.arange(start, end, device=device, dtype=torch.long)
            item_emb = model.item_tower(item_ids)
            all_embeddings.append(item_emb.cpu())
    item_embeddings = torch.cat(all_embeddings, dim=0)
    item_ids_tensor = torch.arange(num_items, dtype=torch.long)

    torch.save(item_embeddings, out_emb_path)
    torch.save(item_ids_tensor, out_ids_path)
    print(f"Saved item embeddings {item_embeddings.shape} to {out_emb_path}")
    print(f"Saved item IDs to {out_ids_path}")


def run_embed_user(args):
    """
    Compute user embedding for one user (by index or by raw ID if vocab in checkpoint).
    For online serving: one user -> one vector -> ANN lookup.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    ckpt_path = Path(args.checkpoint)
    if not ckpt_path.is_absolute():
        ckpt_path = PROJECT_ROOT / ckpt_path
    model, ckpt = load_checkpoint(str(ckpt_path), device)
    model = model.to(device)

    user2idx = ckpt.get("user2idx")
    if args.user_id is not None:
        # Raw ID (string)
        if user2idx is None:
            raise ValueError("Checkpoint has no user2idx; cannot map user_id to index.")
        user_idx = user2idx.get(str(args.user_id))
        if user_idx is None:
            raise ValueError(f"user_id '{args.user_id}' not in vocab.")
    else:
        user_idx = args.user_idx

    with torch.no_grad():
        user_tensor = torch.tensor([[user_idx]], device=device, dtype=torch.long)
        user_emb = model.user_tower(user_tensor).squeeze(0).cpu()
    print(f"User embedding shape: {user_emb.shape}")
    if args.output:
        torch.save(user_emb, args.output)
        print(f"Saved to {args.output}")
    else:
        print(user_emb.numpy().tolist())


def main():
    parser = argparse.ArgumentParser(description="Compute embeddings for items or user")
    sub = parser.add_subparsers(dest="mode", required=True)

    # Mode: embed all items
    p_items = sub.add_parser("items", help="Embed all items; save to output/")
    p_items.add_argument("--checkpoint", type=str, default="checkpoints/best.pt")
    p_items.add_argument("--batch-size", type=int, default=1024)
    p_items.set_defaults(func=run_embed_items)

    # Mode: embed one user
    p_user = sub.add_parser("user", help="Embed one user (for serving)")
    p_user.add_argument("--checkpoint", type=str, default="checkpoints/best.pt")
    p_user.add_argument("--user-idx", type=int, default=None, help="User index (0..num_users-1)")
    p_user.add_argument("--user-id", type=str, default=None, help="Raw user ID (uses vocab in ckpt)")
    p_user.add_argument("--output", type=str, default=None, help="Optional path to save embedding")
    p_user.set_defaults(func=run_embed_user)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
