#!/usr/bin/env bash
# Train the two-tower model. Run from recommendation_system/ project root.
set -e
cd "$(dirname "$0")/.."
python -m src.train --config config/config.yaml
