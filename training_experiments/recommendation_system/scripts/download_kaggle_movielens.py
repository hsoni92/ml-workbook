"""
Download a real MovieLens dataset from Kaggle and prepare train/eval CSVs.

Requires Kaggle API credentials: place kaggle.json in ~/.kaggle/ (see
https://www.kaggle.com/settings/account -> "Create New Token").

Usage:
  python scripts/download_kaggle_movielens.py
  python scripts/download_kaggle_movielens.py --dataset grouplens/movielens-20m-dataset --max-rows 500000

Then run training as usual; config already points at data/train.csv and data/eval.csv.
"""

import argparse
import csv
import random
import subprocess
import sys
import zipfile
from pathlib import Path

# Project root (recommendation_system/)
ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
DATA_DIR = ROOT / "data"

# Default: small dataset for quick runs (~100k ratings)
DEFAULT_DATASET = "grouplens/movielens-latest-small"
# Alternative: "grouplens/movielens-20m-dataset" (use --max-rows to subsample)


def run_cmd(cmd: list[str], cwd: Path) -> None:
    """Run a command; raise on failure."""
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{result.stderr}")


def download_from_kaggle(dataset_slug: str, dest: Path) -> Path:
    """Download dataset via Kaggle API; return path to the downloaded zip."""
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError:
        print("Kaggle API not installed. Run: pip install kaggle", file=sys.stderr)
        sys.exit(1)

    dest.mkdir(parents=True, exist_ok=True)
    api = KaggleApi()
    api.authenticate()
    # Download into dest; creates dest/<dataset_name>.zip
    api.dataset_download_files(dataset_slug, path=str(dest))
    # Zip name is typically the last part of the slug
    zip_name = dataset_slug.split("/")[-1] + ".zip"
    zip_path = dest / zip_name
    if not zip_path.exists():
        # Sometimes the zip has a different name; find it
        zips = list(dest.glob("*.zip"))
        if not zips:
            raise FileNotFoundError(f"No zip found in {dest}")
        zip_path = zips[0]
    return zip_path


def find_ratings_file(top_dir: Path) -> Path:
    """Locate ratings CSV (rating.csv or ratings.csv) in top_dir or one level down."""
    for name in ("ratings.csv", "rating.csv"):
        p = top_dir / name
        if p.exists():
            return p
    for sub in top_dir.iterdir():
        if sub.is_dir():
            for name in ("ratings.csv", "rating.csv"):
                p = sub / name
                if p.exists():
                    return p
    raise FileNotFoundError(
        f"No ratings.csv or rating.csv under {top_dir}. Contents: {list(top_dir.iterdir())}"
    )


def main():
    parser = argparse.ArgumentParser(description="Download MovieLens from Kaggle and prepare train/eval CSVs")
    parser.add_argument(
        "--dataset",
        type=str,
        default=DEFAULT_DATASET,
        help=f"Kaggle dataset slug (default: {DEFAULT_DATASET})",
    )
    parser.add_argument(
        "--max-rows",
        type=int,
        default=None,
        help="Max rows to use (for large datasets; subsample for faster runs)",
    )
    parser.add_argument(
        "--min-rating",
        type=float,
        default=4.0,
        help="Keep only ratings >= this (default 4 = positive only)",
    )
    parser.add_argument(
        "--eval-frac",
        type=float,
        default=0.1,
        help="Fraction of data for eval (default 0.1)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for train/eval split",
    )
    args = parser.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # 1) Download from Kaggle
    print(f"Downloading Kaggle dataset: {args.dataset}")
    zip_path = download_from_kaggle(args.dataset, RAW_DIR)
    print(f"Downloaded {zip_path}")

    # 2) Unzip and find ratings file
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(RAW_DIR)
    # Zip may contain a single folder (e.g. ml-latest-small) or files at root
    top = RAW_DIR
    if not (top / "ratings.csv").exists() and not (top / "rating.csv").exists():
        subs = [s for s in top.iterdir() if s.is_dir()]
        if len(subs) == 1:
            top = subs[0]
    ratings_path = find_ratings_file(top)
    print(f"Using ratings file: {ratings_path}")

    # 3) Read ratings; expect userId, movieId, rating [, timestamp]
    rows = []
    with open(ratings_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # Normalize column names (MovieLens uses userId, movieId)
        fieldnames = [c.strip() for c in reader.fieldnames or []]
        user_col = "userId" if "userId" in fieldnames else "user_id"
        item_col = "movieId" if "movieId" in fieldnames else "item_id"
        rating_col = "rating" if "rating" in fieldnames else None
        for row in reader:
            uid = str(row.get(user_col, row.get("user_id", ""))).strip()
            iid = str(row.get(item_col, row.get("item_id", ""))).strip()
            if not uid or not iid:
                continue
            if rating_col and args.min_rating > 0:
                try:
                    r = float(row.get(rating_col, 0))
                except (ValueError, TypeError):
                    continue
                if r < args.min_rating:
                    continue
            rows.append((uid, iid))

    if args.max_rows and len(rows) > args.max_rows:
        random.seed(args.seed)
        rows = random.sample(rows, args.max_rows)
    print(f"Kept {len(rows)} interactions")

    # 4) Train/eval split (random)
    random.seed(args.seed)
    random.shuffle(rows)
    n_eval = max(1, int(len(rows) * args.eval_frac))
    train_rows = rows[:-n_eval]
    eval_rows = rows[-n_eval:]

    # 5) Write CSVs with columns user_id, item_id (pipeline default)
    train_path = DATA_DIR / "train.csv"
    eval_path = DATA_DIR / "eval.csv"
    with open(train_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["user_id", "item_id"])
        w.writerows(train_rows)
    with open(eval_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["user_id", "item_id"])
        w.writerows(eval_rows)

    print(f"Wrote {train_path} ({len(train_rows)} rows)")
    print(f"Wrote {eval_path} ({len(eval_rows)} rows)")
    print("Run training: python -m src.train --config config/config.yaml")


if __name__ == "__main__":
    main()
