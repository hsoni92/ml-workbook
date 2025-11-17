"""
Visualization script for seller recommendations CSV output.
This script reads the recommendations CSV and creates various visualizations
using matplotlib to analyze the recommendation data.
"""

import sys
import os
import argparse
import glob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path


def find_csv_file(csv_path: str) -> str:
    """
    Find the actual CSV file in the directory structure.
    Spark writes CSV files with partitions, so we need to find the actual file.

    Args:
        csv_path: Path to CSV directory or file

    Returns:
        Path to the actual CSV file
    """
    # If it's a directory, look for CSV files inside
    if os.path.isdir(csv_path):
        # Look for CSV files in subdirectories
        csv_files = glob.glob(os.path.join(csv_path, "**/*.csv"), recursive=True)
        if csv_files:
            return csv_files[0]
        # Also check for files directly in the directory
        csv_files = glob.glob(os.path.join(csv_path, "*.csv"))
        if csv_files:
            return csv_files[0]
        raise FileNotFoundError(f"No CSV file found in directory: {csv_path}")
    elif os.path.isfile(csv_path):
        return csv_path
    else:
        raise FileNotFoundError(f"CSV path not found: {csv_path}")


def load_recommendations(csv_path: str) -> pd.DataFrame:
    """
    Load recommendations CSV file into a pandas DataFrame.

    Args:
        csv_path: Path to CSV file or directory

    Returns:
        DataFrame containing recommendations data
    """
    print(f"Loading recommendations from: {csv_path}")

    # Find the actual CSV file
    actual_csv_path = find_csv_file(csv_path)
    print(f"Found CSV file: {actual_csv_path}")

    # Read CSV
    df = pd.read_csv(actual_csv_path)

    print(f"Loaded {len(df)} recommendations")
    print(f"Columns: {df.columns.tolist()}")
    print(f"\nData Summary:")
    print(df.describe())

    return df


def plot_top_items_by_revenue(df: pd.DataFrame, top_n: int = 10, save_path: str = "data/2025em1100506/processed/recommendations_visualization/top_items_by_revenue.png"):
    """
    Plot top N items by expected revenue.

    Args:
        df: DataFrame with recommendations
        top_n: Number of top items to show
        save_path: Optional path to save the figure
    """
    # Aggregate by item_id to get total expected revenue per item
    item_revenue = df.groupby(['item_id', 'item_name'])['expected_revenue'].sum().reset_index()
    item_revenue = item_revenue.sort_values('expected_revenue', ascending=False).head(top_n)

    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(range(len(item_revenue)), item_revenue['expected_revenue'] / 1e8,
                   color='steelblue', edgecolor='navy', linewidth=1.5)

    ax.set_yticks(range(len(item_revenue)))
    ax.set_yticklabels([f"{row['item_id']}\n{row['item_name'][:30]}..."
                        if len(row['item_name']) > 30 else f"{row['item_id']}\n{row['item_name']}"
                        for _, row in item_revenue.iterrows()], fontsize=9)
    ax.set_xlabel('Expected Revenue (×100 Million)', fontsize=12, fontweight='bold')
    ax.set_title(f'Top {top_n} Items by Expected Revenue', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')

    # Add value labels on bars
    for i, (idx, row) in enumerate(item_revenue.iterrows()):
        value = row['expected_revenue'] / 1e8
        ax.text(value, i, f' {value:.2f}', va='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {save_path}")
    plt.close()


def plot_category_analysis(df: pd.DataFrame, save_path: str = "data/2025em1100506/processed/recommendations_visualization/category_analysis.png"):
    """
    Plot category-wise analysis including revenue and item counts.

    Args:
        df: DataFrame with recommendations
        save_path: Optional path to save the figure
    """
    category_stats = df.groupby('category').agg({
        'expected_revenue': 'sum',
        'item_id': 'nunique',
        'seller_id': 'nunique'
    }).reset_index()
    category_stats.columns = ['category', 'total_revenue', 'unique_items', 'unique_sellers']
    category_stats = category_stats.sort_values('total_revenue', ascending=False)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Plot 1: Total revenue by category
    bars1 = ax1.bar(range(len(category_stats)), category_stats['total_revenue'] / 1e8,
                    color='coral', edgecolor='darkred', linewidth=1.5)
    ax1.set_xticks(range(len(category_stats)))
    ax1.set_xticklabels(category_stats['category'], rotation=45, ha='right', fontsize=10)
    ax1.set_ylabel('Total Expected Revenue (×100 Million)', fontsize=11, fontweight='bold')
    ax1.set_title('Total Expected Revenue by Category', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels
    for i, val in enumerate(category_stats['total_revenue'] / 1e8):
        ax1.text(i, val, f' {val:.2f}', va='bottom', fontsize=9, fontweight='bold')

    # Plot 2: Unique items and sellers by category
    x = range(len(category_stats))
    width = 0.35
    ax2.bar([i - width/2 for i in x], category_stats['unique_items'], width,
            label='Unique Items', color='lightblue', edgecolor='navy', linewidth=1.5)
    ax2.bar([i + width/2 for i in x], category_stats['unique_sellers'], width,
            label='Unique Sellers', color='lightgreen', edgecolor='darkgreen', linewidth=1.5)

    ax2.set_xticks(x)
    ax2.set_xticklabels(category_stats['category'], rotation=45, ha='right', fontsize=10)
    ax2.set_ylabel('Count', fontsize=11, fontweight='bold')
    ax2.set_title('Unique Items and Sellers by Category', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {save_path}")
    plt.close()


def plot_revenue_distribution(df: pd.DataFrame, save_path: str = "data/2025em1100506/processed/recommendations_visualization/revenue_distribution.png"):
    """
    Plot distribution of expected revenue.

    Args:
        df: DataFrame with recommendations
        save_path: Optional path to save the figure
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Histogram
    ax1.hist(df['expected_revenue'] / 1e8, bins=50, color='skyblue',
             edgecolor='navy', alpha=0.7, linewidth=1.5)
    ax1.set_xlabel('Expected Revenue (×100 Million)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Frequency', fontsize=11, fontweight='bold')
    ax1.set_title('Distribution of Expected Revenue', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # Box plot
    bp = ax2.boxplot(df['expected_revenue'] / 1e8, vert=True, patch_artist=True,
                     boxprops=dict(facecolor='lightcoral', alpha=0.7),
                     medianprops=dict(color='darkred', linewidth=2),
                     whiskerprops=dict(color='black', linewidth=1.5),
                     capprops=dict(color='black', linewidth=1.5))
    ax2.set_ylabel('Expected Revenue (×100 Million)', fontsize=11, fontweight='bold')
    ax2.set_title('Box Plot of Expected Revenue', fontsize=12, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')

    # Add statistics text
    stats_text = f"Mean: {df['expected_revenue'].mean() / 1e8:.2f}\n"
    stats_text += f"Median: {df['expected_revenue'].median() / 1e8:.2f}\n"
    stats_text += f"Std Dev: {df['expected_revenue'].std() / 1e8:.2f}"
    ax2.text(1.1, df['expected_revenue'].max() / 1e8 * 0.9, stats_text,
             fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round',
             facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {save_path}")
    plt.close()


def plot_top_sellers(df: pd.DataFrame, top_n: int = 15, save_path: str = "data/2025em1100506/processed/recommendations_visualization/top_sellers.png"):
    """
    Plot top sellers by total expected revenue and number of recommendations.

    Args:
        df: DataFrame with recommendations
        top_n: Number of top sellers to show
        save_path: Optional path to save the figure
    """
    seller_stats = df.groupby('seller_id').agg({
        'expected_revenue': 'sum',
        'item_id': 'count'
    }).reset_index()
    seller_stats.columns = ['seller_id', 'total_revenue', 'num_recommendations']
    seller_stats = seller_stats.sort_values('total_revenue', ascending=False).head(top_n)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Plot 1: Top sellers by total revenue
    bars1 = ax1.bar(range(len(seller_stats)), seller_stats['total_revenue'] / 1e8,
                    color='gold', edgecolor='darkorange', linewidth=1.5)
    ax1.set_xticks(range(len(seller_stats)))
    ax1.set_xticklabels(seller_stats['seller_id'], rotation=45, ha='right', fontsize=9)
    ax1.set_ylabel('Total Expected Revenue (×100 Million)', fontsize=11, fontweight='bold')
    ax1.set_title(f'Top {top_n} Sellers by Total Expected Revenue', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels
    for i, val in enumerate(seller_stats['total_revenue'] / 1e8):
        ax1.text(i, val, f' {val:.2f}', va='bottom', fontsize=8, fontweight='bold', rotation=90)

    # Plot 2: Number of recommendations per seller
    seller_counts = df['seller_id'].value_counts().head(top_n).sort_values(ascending=True)
    bars2 = ax2.barh(range(len(seller_counts)), seller_counts.values,
                     color='mediumpurple', edgecolor='darkviolet', linewidth=1.5)
    ax2.set_yticks(range(len(seller_counts)))
    ax2.set_yticklabels(seller_counts.index, fontsize=9)
    ax2.set_xlabel('Number of Recommendations', fontsize=11, fontweight='bold')
    ax2.set_title(f'Top {top_n} Sellers by Number of Recommendations', fontsize=12, fontweight='bold')
    ax2.grid(axis='x', alpha=0.3, linestyle='--')

    # Add value labels
    for i, val in enumerate(seller_counts.values):
        ax2.text(val, i, f' {val}', va='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {save_path}")
    plt.close()


def plot_price_vs_units_analysis(df: pd.DataFrame, save_path: str = "data/2025em1100506/processed/recommendations_visualization/price_vs_units.png"):
    """
    Plot scatter plot of market price vs expected units sold.

    Args:
        df: DataFrame with recommendations
        save_path: Optional path to save the figure
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    # Create scatter plot colored by category
    categories = df['category'].unique()
    colors = plt.cm.tab10(range(len(categories)))
    color_map = dict(zip(categories, colors))

    for category in categories:
        category_data = df[df['category'] == category]
        ax.scatter(category_data['market_price'] / 1000,
                  category_data['expected_units_sold'],
                  label=category, alpha=0.6, s=100, edgecolors='black', linewidth=0.5)

    ax.set_xlabel('Market Price (×1000)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Expected Units Sold', fontsize=12, fontweight='bold')
    ax.set_title('Market Price vs Expected Units Sold (by Category)',
                fontsize=14, fontweight='bold', pad=20)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
    ax.grid(alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {save_path}")
    plt.close()


def plot_summary_statistics(df: pd.DataFrame, save_path: str = "data/2025em1100506/processed/recommendations_visualization/summary_statistics.png"):
    """
    Create a summary statistics visualization.

    Args:
        df: DataFrame with recommendations
        save_path: Optional path to save the figure
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # 1. Market Price Distribution
    axes[0, 0].hist(df['market_price'] / 1000, bins=30, color='lightseagreen',
                    edgecolor='teal', linewidth=1.5, alpha=0.7)
    axes[0, 0].set_xlabel('Market Price (×1000)', fontsize=11, fontweight='bold')
    axes[0, 0].set_ylabel('Frequency', fontsize=11, fontweight='bold')
    axes[0, 0].set_title('Market Price Distribution', fontsize=12, fontweight='bold')
    axes[0, 0].grid(axis='y', alpha=0.3, linestyle='--')

    # 2. Expected Units Sold Distribution
    axes[0, 1].hist(df['expected_units_sold'], bins=30, color='salmon',
                    edgecolor='crimson', linewidth=1.5, alpha=0.7)
    axes[0, 1].set_xlabel('Expected Units Sold', fontsize=11, fontweight='bold')
    axes[0, 1].set_ylabel('Frequency', fontsize=11, fontweight='bold')
    axes[0, 1].set_title('Expected Units Sold Distribution', fontsize=12, fontweight='bold')
    axes[0, 1].grid(axis='y', alpha=0.3, linestyle='--')

    # 3. Top 10 Categories by Average Revenue
    category_avg_revenue = df.groupby('category')['expected_revenue'].mean().sort_values(ascending=False).head(10)
    axes[1, 0].barh(range(len(category_avg_revenue)), category_avg_revenue.values / 1e8,
                    color='plum', edgecolor='purple', linewidth=1.5)
    axes[1, 0].set_yticks(range(len(category_avg_revenue)))
    axes[1, 0].set_yticklabels(category_avg_revenue.index, fontsize=9)
    axes[1, 0].set_xlabel('Average Expected Revenue (×100 Million)', fontsize=11, fontweight='bold')
    axes[1, 0].set_title('Top 10 Categories by Average Revenue', fontsize=12, fontweight='bold')
    axes[1, 0].grid(axis='x', alpha=0.3, linestyle='--')

    # 4. Revenue vs Units Sold (scatter)
    scatter = axes[1, 1].scatter(df['expected_units_sold'], df['expected_revenue'] / 1e8,
                                c=df['market_price'] / 1000, cmap='viridis',
                                alpha=0.6, s=100, edgecolors='black', linewidth=0.5)
    axes[1, 1].set_xlabel('Expected Units Sold', fontsize=11, fontweight='bold')
    axes[1, 1].set_ylabel('Expected Revenue (×100 Million)', fontsize=11, fontweight='bold')
    axes[1, 1].set_title('Revenue vs Units Sold (colored by Market Price)', fontsize=12, fontweight='bold')
    axes[1, 1].grid(alpha=0.3, linestyle='--')
    cbar = plt.colorbar(scatter, ax=axes[1, 1])
    cbar.set_label('Market Price (×1000)', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {save_path}")
    plt.close()


def main():
    """Main function to run all visualizations."""
    parser = argparse.ArgumentParser(
        description='Visualize seller recommendations CSV output'
    )
    parser.add_argument(
        '--csv-path',
        type=str,
        default='data/2025em1100506/processed/recommendations_csv/seller_recommend_data.csv',
        help='Path to the recommendations CSV file or directory'
    )
    args = parser.parse_args()

    # Create visualizations directory
    os.makedirs('data/2025em1100506/processed/recommendations_visualization', exist_ok=True)
    print(f"Plots will be saved to: data/2025em1100506/processed/recommendations_visualization/")

    try:
        # Load data
        print("=" * 60)
        print("Loading Recommendations Data")
        print("=" * 60)
        df = load_recommendations(args.csv_path)

        # Print basic statistics
        print("\n" + "=" * 60)
        print("Data Overview")
        print("=" * 60)
        print(f"Total Recommendations: {len(df):,}")
        print(f"Unique Sellers: {df['seller_id'].nunique()}")
        print(f"Unique Items: {df['item_id'].nunique()}")
        print(f"Unique Categories: {df['category'].nunique()}")
        print(f"\nTotal Expected Revenue: {df['expected_revenue'].sum() / 1e9:.2f} Billion")
        print(f"Average Expected Revenue per Recommendation: {df['expected_revenue'].mean() / 1e6:.2f} Million")

        # Generate visualizations
        print("\n" + "=" * 60)
        print("Generating Visualizations")
        print("=" * 60)

        # 1. Top items by revenue
        print("\n1. Plotting top items by expected revenue...")
        plot_top_items_by_revenue(df, top_n=10)

        # 2. Category analysis
        print("\n2. Plotting category analysis...")
        plot_category_analysis(df)

        # 3. Revenue distribution
        print("\n3. Plotting revenue distribution...")
        plot_revenue_distribution(df)

        # 4. Top sellers
        print("\n4. Plotting top sellers analysis...")
        plot_top_sellers(df, top_n=15)

        # 5. Price vs units analysis
        print("\n5. Plotting price vs units sold analysis...")
        plot_price_vs_units_analysis(df)

        # 6. Summary statistics
        print("\n6. Plotting summary statistics...")
        plot_summary_statistics(df)

        print("\n" + "=" * 60)
        print("Visualization Complete!")
        print("=" * 60)

    except Exception as e:
        print(f"Error generating visualizations: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

