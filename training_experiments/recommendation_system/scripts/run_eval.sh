#!/usr/bin/env bash
# Run offline evaluation: Recall@K, MRR, NDCG@K on holdout set.
# Run from recommendation_system/ project root.
set -e
cd "$(dirname "$0")/.."
python -m src.evaluate --config config/config.yaml --checkpoint checkpoints/best.pt
