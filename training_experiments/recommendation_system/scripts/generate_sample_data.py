"""
Generate sample train/eval CSV so you can run training without real data.
CSV format: user_id,item_id (one interaction per row).
"""

import csv
import random
from pathlib import Path

# Run from recommendation_system/
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

NUM_USERS = 200
NUM_ITEMS = 500
TRAIN_PAIRS = 5000
EVAL_PAIRS = 500

random.seed(42)


def main():
    train_path = DATA_DIR / "train.csv"
    eval_path = DATA_DIR / "eval.csv"

    # Generate random (user, item) pairs; allow duplicates for train
    train_rows = [
        (f"u{random.randint(0, NUM_USERS - 1)}", f"i{random.randint(0, NUM_ITEMS - 1)}")
        for _ in range(TRAIN_PAIRS)
    ]
    eval_rows = [
        (f"u{random.randint(0, NUM_USERS - 1)}", f"i{random.randint(0, NUM_ITEMS - 1)}")
        for _ in range(EVAL_PAIRS)
    ]

    with open(train_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["user_id", "item_id"])
        w.writerows(train_rows)
    with open(eval_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["user_id", "item_id"])
        w.writerows(eval_rows)

    print(f"Wrote {train_path} ({TRAIN_PAIRS} rows)")
    print(f"Wrote {eval_path} ({EVAL_PAIRS} rows)")


if __name__ == "__main__":
    main()
