"""
Simple visualization script for seller recommendations CSV output.
Shows top selling products per seller as ranked items in a bar chart.
"""

import sys
import os
import argparse
import glob
import pandas as pd
import matplotlib.pyplot as plt


def find_csv_file(csv_path: str) -> str:
    """Find the actual CSV file in the directory structure."""
    if os.path.isdir(csv_path):
        csv_files = glob.glob(os.path.join(csv_path, "**/*.csv"), recursive=True)
        if csv_files:
            return csv_files[0]
        csv_files = glob.glob(os.path.join(csv_path, "*.csv"))
        if csv_files:
            return csv_files[0]
        raise FileNotFoundError(f"No CSV file found in directory: {csv_path}")
    elif os.path.isfile(csv_path):
        return csv_path
    else:
        raise FileNotFoundError(f"CSV path not found: {csv_path}")


def load_recommendations(csv_path: str) -> pd.DataFrame:
    """Load recommendations CSV file into a pandas DataFrame."""
    print(f"Loading recommendations from: {csv_path}")
    actual_csv_path = find_csv_file(csv_path)
    print(f"Found CSV file: {actual_csv_path}")
    df = pd.read_csv(actual_csv_path)
    print(f"Loaded {len(df)} recommendations")
    return df


def plot_top_products_per_seller(df: pd.DataFrame, output_dir: str = "data/2025em1100506/processed/recommendations_visualization"):
    """
    Plot top selling products per seller as ranked items in separate bar charts.
    Creates one chart per seller.

    Args:
        df: DataFrame with recommendations
        output_dir: Directory to save the figures
    """
    # Get unique sellers
    sellers = df['seller_id'].unique()

    # Create a chart for each seller
    for seller_id in sellers:
        # Get top products for this seller, ranked by expected revenue
        seller_data = df[df['seller_id'] == seller_id].copy()
        seller_data = seller_data.sort_values('expected_revenue', ascending=False).head(10)

        # Sort for display (lowest to highest for horizontal bar chart)
        seller_data = seller_data.sort_values('expected_revenue', ascending=True)

        # Create bar chart
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create labels
        labels = [f"{row['item_id']} - {row['item_name'][:40]}"
                 if len(row['item_name']) > 40 else f"{row['item_id']} - {row['item_name']}"
                 for _, row in seller_data.iterrows()]

        # Plot horizontal bar chart
        bars = ax.barh(range(len(seller_data)),
                      seller_data['expected_revenue'] / 1e6,
                      color='steelblue', edgecolor='navy', linewidth=0.5)

        ax.set_yticks(range(len(seller_data)))
        ax.set_yticklabels(labels, fontsize=9)
        ax.set_xlabel('Expected Revenue (Million)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Products (Ranked)', fontsize=12, fontweight='bold')
        ax.set_title(f'Top Selling Products - Seller {seller_id}', fontsize=14, fontweight='bold')
        ax.grid(axis='x', alpha=0.3, linestyle='--')

        # Save chart
        save_path = os.path.join(output_dir, f'top_products_seller_{seller_id}.png')
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved plot for seller {seller_id} to: {save_path}")
        plt.close()


def main():
    """Main function to run visualization."""
    parser = argparse.ArgumentParser(description='Visualize top selling products per seller')
    parser.add_argument(
        '--csv-path',
        type=str,
        default='data/2025em1100506/processed/recommendations_csv/seller_recommend_data.csv',
        help='Path to the recommendations CSV file or directory'
    )
    args = parser.parse_args()

    # Create visualizations directory
    os.makedirs('data/2025em1100506/processed/recommendations_visualization', exist_ok=True)

    try:
        # Load data
        df = load_recommendations(args.csv_path)

        # Generate visualizations (one per seller)
        print("Generating bar charts (one per seller)...")
        plot_top_products_per_seller(df)

        print(f"Visualization complete! Generated charts for {df['seller_id'].nunique()} sellers.")

    except Exception as e:
        print(f"Error generating visualization: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
