"""
Two-tower model: User Tower and Item Tower.

Each tower embeds IDs (user_id, item_id) then passes through an MLP to a
fixed-size embedding. Relevance score = dot product of user_embed and item_embed.
"""

import torch
import torch.nn as nn
from typing import List


class Tower(nn.Module):
    """
    Single tower: Embedding lookup for IDs, then MLP to embedding_dim.
    """

    def __init__(
        self,
        num_entities: int,
        id_embed_dim: int,
        hidden_dims: List[int],
        embedding_dim: int,
    ):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.id_embed = nn.Embedding(num_entities, id_embed_dim)

        layers = []
        prev = id_embed_dim
        for h in hidden_dims:
            layers.append(nn.Linear(prev, h))
            layers.append(nn.ReLU())
            layers.append(nn.BatchNorm1d(h))
            prev = h
        layers.append(nn.Linear(prev, embedding_dim))
        self.mlp = nn.Sequential(*layers)

    def forward(self, ids: torch.Tensor) -> torch.Tensor:
        # ids: (batch_size,) or (batch_size, 1) -> (batch_size, embedding_dim)
        x = self.id_embed(ids)
        # Flatten so MLP always gets (batch_size, id_embed_dim); avoid (B, 1, D) -> BatchNorm error
        x = x.view(x.size(0), -1)
        return self.mlp(x)


class TwoTower(nn.Module):
    """
    User tower + Item tower. Both output same embedding_dim so we can score
    with dot product: score(u, i) = user_embed @ item_embed.T
    """

    def __init__(
        self,
        num_users: int,
        num_items: int,
        user_id_embed_dim: int,
        user_hidden_dims: List[int],
        item_id_embed_dim: int,
        item_hidden_dims: List[int],
        embedding_dim: int,
    ):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.num_users = num_users
        self.num_items = num_items

        self.user_tower = Tower(
            num_entities=num_users,
            id_embed_dim=user_id_embed_dim,
            hidden_dims=user_hidden_dims,
            embedding_dim=embedding_dim,
        )
        self.item_tower = Tower(
            num_entities=num_items,
            id_embed_dim=item_id_embed_dim,
            hidden_dims=item_hidden_dims,
            embedding_dim=embedding_dim,
        )

    def forward(
        self,
        user_ids: torch.Tensor,
        item_ids: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """
        Args:
            user_ids: (batch_size,) long tensor, indices in [0, num_users)
            item_ids: (batch_size,) long tensor, indices in [0, num_items)

        Returns:
            user_emb: (batch_size, embedding_dim)
            item_emb: (batch_size, embedding_dim)
        """
        user_emb = self.user_tower(user_ids)
        item_emb = self.item_tower(item_ids)
        return user_emb, item_emb

    def score(self, user_emb: torch.Tensor, item_emb: torch.Tensor) -> torch.Tensor:
        """
        Dot-product scores. user_emb (B, D) @ item_emb.T (D, N) -> (B, N).
        """
        return torch.matmul(user_emb, item_emb.T)
