#!/usr/bin/env bash
# Embed all items and save to output/ (for building ANN index later).
# Run after training. Run from recommendation_system/ project root.
set -e
cd "$(dirname "$0")/.."
python -m src.embed items --checkpoint checkpoints/best.pt --batch-size 1024
