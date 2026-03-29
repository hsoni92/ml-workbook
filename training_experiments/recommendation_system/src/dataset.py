"""
PyTorch Dataset for (user, item) pairs.

Loads a CSV with configurable user/item column names. Builds contiguous indices
for users and items so the model can use Embedding layers. Yields (user_idx, item_idx)
for each positive interaction.
"""

import csv
from pathlib import Path
from typing import Dict, Optional, Tuple

import torch
from torch.utils.data import Dataset


class RecommendationDataset(Dataset):
    """
    Dataset of positive (user, item) pairs. Each row is one interaction.
    User and item IDs from CSV are mapped to contiguous indices 0..num_users-1
    and 0..num_items-1.
    """

    def __init__(
        self,
        path: str,
        user2idx: Optional[Dict[str, int]] = None,
        item2idx: Optional[Dict[str, int]] = None,
        user_id_column: str = "user_id",
        item_id_column: str = "item_id",
    ):
        """
        Args:
            path: Path to CSV.
            user2idx: If provided, use this mapping; else build from this file.
            item2idx: If provided, use this mapping; else build from this file.
            user_id_column: CSV column name for user identifier (e.g. user_id, userId).
            item_id_column: CSV column name for item identifier (e.g. item_id, movieId).
        """
        self.path = Path(path)
        self.pairs: list[Tuple[int, int]] = []
        self.user_id_column = user_id_column
        self.item_id_column = item_id_column

        if user2idx is None:
            user2idx = {}
        if item2idx is None:
            item2idx = {}

        with open(self.path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if user_id_column not in reader.fieldnames or item_id_column not in reader.fieldnames:
                raise ValueError(
                    f"CSV must have '{user_id_column}' and '{item_id_column}' columns. Got: {reader.fieldnames}"
                )
            for row in reader:
                uid = str(row[user_id_column]).strip()
                iid = str(row[item_id_column]).strip()
                if uid not in user2idx:
                    user2idx[uid] = len(user2idx)
                if iid not in item2idx:
                    item2idx[iid] = len(item2idx)
                self.pairs.append((user2idx[uid], item2idx[iid]))

        self.user2idx = user2idx
        self.item2idx = item2idx
        self.num_users = len(user2idx)
        self.num_items = len(item2idx)

    def __len__(self) -> int:
        return len(self.pairs)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        u, i = self.pairs[idx]
        return torch.tensor(u, dtype=torch.long), torch.tensor(i, dtype=torch.long)


def load_vocab_from_csv(
    path: str,
    user_id_column: str = "user_id",
    item_id_column: str = "item_id",
) -> Tuple[Dict[str, int], Dict[str, int]]:
    """
    Build user2idx and item2idx from a CSV without loading full pairs.
    Useful to build eval dataset with same vocab as train.
    """
    user2idx: Dict[str, int] = {}
    item2idx: Dict[str, int] = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            uid = str(row[user_id_column]).strip()
            iid = str(row[item_id_column]).strip()
            if uid not in user2idx:
                user2idx[uid] = len(user2idx)
            if iid not in item2idx:
                item2idx[iid] = len(item2idx)
    return user2idx, item2idx
