"""
Visualization script for seller recommendations CSV output.

STORY: "Your job is to analyze internal sales and competitor data and recommend
top 10 selling items that each seller currently does not have. This will help
sellers increase revenue and profit by onboarding these items."

This script creates visualizations that tell the story of:
- Missing opportunities: Items sellers don't currently have
- Revenue potential: Expected revenue from onboarding recommended items
- Business impact: How these recommendations can drive growth
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
    Plot top N missing items by expected revenue opportunity.
    These are items that sellers don't currently have but should consider adding.

    Args:
        df: DataFrame with recommendations
        top_n: Number of top items to show
        save_path: Optional path to save the figure
    """
    # Aggregate by item_id to get total expected revenue per item across all sellers
    item_revenue = df.groupby(['item_id', 'item_name'])['expected_revenue'].sum().reset_index()
    item_revenue = item_revenue.sort_values('expected_revenue', ascending=False).head(top_n)

    # Count how many sellers are missing each item
    seller_counts = df.groupby('item_id')['seller_id'].nunique().reset_index()
    seller_counts.columns = ['item_id', 'sellers_missing']
    item_revenue = item_revenue.merge(seller_counts, on='item_id')

    fig, ax = plt.subplots(figsize=(14, 8))
    bars = ax.barh(range(len(item_revenue)), item_revenue['expected_revenue'] / 1e8,
                   color='#2E86AB', edgecolor='#1B4965', linewidth=2)

    ax.set_yticks(range(len(item_revenue)))
    ax.set_yticklabels([f"{row['item_id']}\n{row['item_name'][:35]}..."
                        if len(row['item_name']) > 35 else f"{row['item_id']}\n{row['item_name']}"
                        for _, row in item_revenue.iterrows()], fontsize=9)
    ax.set_xlabel('Total Expected Revenue Opportunity (×100 Million)', fontsize=12, fontweight='bold')
    ax.set_title(f'Top {top_n} Missing Items: Highest Revenue Opportunities\n'
                 f'(Items sellers don\'t have but should consider adding)',
                 fontsize=15, fontweight='bold', pad=20, color='#1B4965')
    ax.grid(axis='x', alpha=0.3, linestyle='--', color='gray')

    # Add value labels on bars with seller count
    for i, (idx, row) in enumerate(item_revenue.iterrows()):
        value = row['expected_revenue'] / 1e8
        sellers = row['sellers_missing']
        ax.text(value, i, f' {value:.2f}\n({sellers} sellers)', va='center',
                fontsize=9, fontweight='bold', color='white')

    # Add annotation
    total_revenue = item_revenue['expected_revenue'].sum() / 1e8
    ax.text(0.98, 0.02, f'Total Opportunity: {total_revenue:.2f} ×100M\n'
            f'These items are missing from seller catalogs',
            transform=ax.transAxes, fontsize=10, verticalalignment='bottom',
            horizontalalignment='right', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {save_path}")
    plt.close()


def plot_category_analysis(df: pd.DataFrame, save_path: str = "data/2025em1100506/processed/recommendations_visualization/category_analysis.png"):
    """
    Plot category-wise analysis showing revenue opportunities by category.
    Highlights which categories have the most missing items with high revenue potential.

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

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # Plot 1: Total revenue opportunity by category
    bars1 = ax1.bar(range(len(category_stats)), category_stats['total_revenue'] / 1e8,
                    color='#FF6B6B', edgecolor='#C92A2A', linewidth=2)
    ax1.set_xticks(range(len(category_stats)))
    ax1.set_xticklabels(category_stats['category'], rotation=45, ha='right', fontsize=10)
    ax1.set_ylabel('Total Revenue Opportunity (×100 Million)', fontsize=11, fontweight='bold')
    ax1.set_title('Revenue Opportunity by Category\n(Missing items with highest potential)',
                  fontsize=13, fontweight='bold', color='#C92A2A')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels
    for i, val in enumerate(category_stats['total_revenue'] / 1e8):
        ax1.text(i, val, f' {val:.2f}', va='bottom', fontsize=9, fontweight='bold')

    # Plot 2: Missing items and affected sellers by category
    x = range(len(category_stats))
    width = 0.35
    ax2.bar([i - width/2 for i in x], category_stats['unique_items'], width,
            label='Missing Items', color='#4ECDC4', edgecolor='#0E7C7B', linewidth=1.5)
    ax2.bar([i + width/2 for i in x], category_stats['unique_sellers'], width,
            label='Sellers Affected', color='#95E1D3', edgecolor='#2D7A6B', linewidth=1.5)

    ax2.set_xticks(x)
    ax2.set_xticklabels(category_stats['category'], rotation=45, ha='right', fontsize=10)
    ax2.set_ylabel('Count', fontsize=11, fontweight='bold')
    ax2.set_title('Missing Items & Affected Sellers by Category\n(Items sellers don\'t have)',
                  fontsize=13, fontweight='bold', color='#0E7C7B')
    ax2.legend(fontsize=10, loc='upper right')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {save_path}")
    plt.close()


def plot_revenue_distribution(df: pd.DataFrame, save_path: str = "data/2025em1100506/processed/recommendations_visualization/revenue_distribution.png"):
    """
    Plot distribution of expected revenue opportunities from missing items.
    Shows the spread of revenue potential across all recommendations.

    Args:
        df: DataFrame with recommendations
        save_path: Optional path to save the figure
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # Histogram
    ax1.hist(df['expected_revenue'] / 1e8, bins=50, color='#6C5CE7',
             edgecolor='#4834D4', alpha=0.7, linewidth=1.5)
    ax1.set_xlabel('Expected Revenue Opportunity (×100 Million)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Number of Recommendations', fontsize=11, fontweight='bold')
    ax1.set_title('Distribution of Revenue Opportunities\n'
                 f'(From {len(df):,} missing item recommendations)',
                 fontsize=13, fontweight='bold', color='#4834D4')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # Add vertical line for mean
    mean_rev = df['expected_revenue'].mean() / 1e8
    ax1.axvline(mean_rev, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_rev:.2f}')
    ax1.legend(fontsize=10)

    # Box plot
    bp = ax2.boxplot(df['expected_revenue'] / 1e8, vert=True, patch_artist=True,
                     boxprops=dict(facecolor='#FF6B6B', alpha=0.7),
                     medianprops=dict(color='#C92A2A', linewidth=2),
                     whiskerprops=dict(color='black', linewidth=1.5),
                     capprops=dict(color='black', linewidth=1.5))
    ax2.set_ylabel('Expected Revenue Opportunity (×100 Million)', fontsize=11, fontweight='bold')
    ax2.set_title('Revenue Opportunity Statistics\n'
                 f'(Per missing item recommendation)',
                 fontsize=13, fontweight='bold', color='#C92A2A')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')

    # Add statistics text with business context
    stats_text = f"Mean Opportunity: {df['expected_revenue'].mean() / 1e8:.2f}\n"
    stats_text += f"Median Opportunity: {df['expected_revenue'].median() / 1e8:.2f}\n"
    stats_text += f"Std Dev: {df['expected_revenue'].std() / 1e8:.2f}\n\n"
    stats_text += f"Total Opportunity:\n{df['expected_revenue'].sum() / 1e9:.2f} Billion"
    ax2.text(1.15, df['expected_revenue'].max() / 1e8 * 0.95, stats_text,
             fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round',
             facecolor='lightyellow', alpha=0.9, edgecolor='orange', linewidth=2))

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {save_path}")
    plt.close()


def plot_top_sellers(df: pd.DataFrame, top_n: int = 15, save_path: str = "data/2025em1100506/processed/recommendations_visualization/top_sellers.png"):
    """
    Plot sellers with highest revenue opportunities from missing items.
    Shows which sellers have the most to gain by adding recommended items.

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

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # Plot 1: Top sellers by revenue opportunity
    bars1 = ax1.bar(range(len(seller_stats)), seller_stats['total_revenue'] / 1e8,
                    color='#FFD93D', edgecolor='#F6AE2D', linewidth=2)
    ax1.set_xticks(range(len(seller_stats)))
    ax1.set_xticklabels(seller_stats['seller_id'], rotation=45, ha='right', fontsize=9)
    ax1.set_ylabel('Revenue Opportunity (×100 Million)', fontsize=11, fontweight='bold')
    ax1.set_title(f'Top {top_n} Sellers: Highest Revenue Opportunities\n'
                 f'(Potential revenue from adding missing items)',
                 fontsize=13, fontweight='bold', color='#F6AE2D')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels
    for i, val in enumerate(seller_stats['total_revenue'] / 1e8):
        ax1.text(i, val, f' {val:.2f}', va='bottom', fontsize=8, fontweight='bold', rotation=90)

    # Plot 2: Top 10 missing items per seller (showing count)
    seller_counts = df['seller_id'].value_counts().head(top_n).sort_values(ascending=True)
    bars2 = ax2.barh(range(len(seller_counts)), seller_counts.values,
                     color='#A8E6CF', edgecolor='#4ECDC4', linewidth=2)
    ax2.set_yticks(range(len(seller_counts)))
    ax2.set_yticklabels(seller_counts.index, fontsize=9)
    ax2.set_xlabel('Number of Missing Items Recommended', fontsize=11, fontweight='bold')
    ax2.set_title(f'Top {top_n} Sellers: Missing Items Count\n'
                 f'(Each seller gets top 10 recommendations)',
                 fontsize=13, fontweight='bold', color='#4ECDC4')
    ax2.grid(axis='x', alpha=0.3, linestyle='--')

    # Add value labels
    for i, val in enumerate(seller_counts.values):
        ax2.text(val, i, f' {val} items', va='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {save_path}")
    plt.close()


def plot_price_vs_units_analysis(df: pd.DataFrame, save_path: str = "data/2025em1100506/processed/recommendations_visualization/price_vs_units.png"):
    """
    Plot market price vs expected units sold for recommended missing items.
    Shows the relationship between pricing and demand for items sellers should add.

    Args:
        df: DataFrame with recommendations
        save_path: Optional path to save the figure
    """
    fig, ax = plt.subplots(figsize=(14, 8))

    # Create scatter plot colored by category, sized by expected revenue
    categories = df['category'].unique()
    colors = plt.cm.Set3(range(len(categories)))
    color_map = dict(zip(categories, colors))

    for category in categories:
        category_data = df[df['category'] == category]
        # Size points by expected revenue (normalized)
        sizes = (category_data['expected_revenue'] / category_data['expected_revenue'].max() * 300) + 50
        ax.scatter(category_data['market_price'] / 1000,
                  category_data['expected_units_sold'],
                  label=category, alpha=0.7, s=sizes, edgecolors='black', linewidth=0.8)

    ax.set_xlabel('Market Price (×1000)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Expected Units Sold', fontsize=12, fontweight='bold')
    ax.set_title('Market Price vs Expected Units Sold for Missing Items\n'
                f'(Point size = Revenue Opportunity; {len(df)} recommendations across {df["seller_id"].nunique()} sellers)',
                fontsize=14, fontweight='bold', pad=20, color='#2C3E50')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9, title='Category')
    ax.grid(alpha=0.3, linestyle='--')

    # Add annotation about the opportunity
    total_revenue = df['expected_revenue'].sum() / 1e9
    ax.text(0.02, 0.98, f'Total Revenue Opportunity:\n{total_revenue:.2f} Billion\n\n'
            f'These are items sellers don\'t have\nbut should consider adding',
            transform=ax.transAxes, fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9, edgecolor='orange', linewidth=2))

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {save_path}")
    plt.close()


def plot_top_items_per_seller(df: pd.DataFrame, num_sellers: int = 5, save_path: str = "data/2025em1100506/processed/recommendations_visualization/top_items_per_seller.png"):
    """
    Plot top 10 missing items for selected sellers.
    This visualization emphasizes the "top 10 per seller" aspect of the story.

    Args:
        df: DataFrame with recommendations
        num_sellers: Number of sellers to showcase
        save_path: Optional path to save the figure
    """
    # Get top sellers by total revenue opportunity
    seller_revenue = df.groupby('seller_id')['expected_revenue'].sum().reset_index()
    top_sellers = seller_revenue.nlargest(num_sellers, 'expected_revenue')['seller_id'].tolist()

    # Create subplots for each seller
    fig, axes = plt.subplots(num_sellers, 1, figsize=(14, 4 * num_sellers))
    if num_sellers == 1:
        axes = [axes]

    fig.suptitle('Top 10 Missing Items Per Seller: Revenue Opportunities\n'
                 'These items are NOT in seller catalogs but should be added',
                 fontsize=16, fontweight='bold', color='#2C3E50', y=0.995)

    for idx, seller_id in enumerate(top_sellers):
        seller_data = df[df['seller_id'] == seller_id].nlargest(10, 'expected_revenue')

        ax = axes[idx]
        bars = ax.barh(range(len(seller_data)), seller_data['expected_revenue'] / 1e6,
                      color='#3498DB', edgecolor='#2980B9', linewidth=1.5)

        ax.set_yticks(range(len(seller_data)))
        ax.set_yticklabels([f"{row['item_id']}\n{row['item_name'][:25]}..."
                            if len(row['item_name']) > 25 else f"{row['item_id']}\n{row['item_name']}"
                            for _, row in seller_data.iterrows()], fontsize=8)
        ax.set_xlabel('Expected Revenue Opportunity (Million)', fontsize=10, fontweight='bold')
        ax.set_title(f'Seller {seller_id}: Top 10 Missing Items\n'
                    f'Total Opportunity: {seller_data["expected_revenue"].sum() / 1e8:.2f} ×100 Million',
                    fontsize=12, fontweight='bold', color='#2980B9')
        ax.grid(axis='x', alpha=0.3, linestyle='--')

        # Add value labels
        for i, (_, row) in enumerate(seller_data.iterrows()):
            value = row['expected_revenue'] / 1e6
            ax.text(value, i, f' {value:.2f}M', va='center', fontsize=8, fontweight='bold')

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {save_path}")
    plt.close()


def plot_summary_statistics(df: pd.DataFrame, save_path: str = "data/2025em1100506/processed/recommendations_visualization/summary_statistics.png"):
    """
    Create a comprehensive summary visualization showing key insights about missing items.
    Tells the story of revenue opportunities from items sellers don't have.

    Args:
        df: DataFrame with recommendations
        save_path: Optional path to save the figure
    """
    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

    # Add main title
    fig.suptitle('Seller Recommendations: Missing Items Analysis\n'
                 'Top 10 items per seller that can drive revenue growth',
                 fontsize=16, fontweight='bold', color='#2C3E50', y=0.98)

    # 1. Market Price Distribution for Missing Items
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.hist(df['market_price'] / 1000, bins=30, color='#00D2D3',
             edgecolor='#01A3A4', linewidth=1.5, alpha=0.7)
    ax1.set_xlabel('Market Price (×1000)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Number of Recommendations', fontsize=11, fontweight='bold')
    ax1.set_title('Market Price Distribution\n(For recommended missing items)',
                  fontsize=12, fontweight='bold', color='#01A3A4')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # 2. Expected Units Sold Distribution
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.hist(df['expected_units_sold'], bins=30, color='#FF6348',
             edgecolor='#C44536', linewidth=1.5, alpha=0.7)
    ax2.set_xlabel('Expected Units Sold', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Number of Recommendations', fontsize=11, fontweight='bold')
    ax2.set_title('Expected Units Sold Distribution\n(Demand forecast for missing items)',
                  fontsize=12, fontweight='bold', color='#C44536')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')

    # 3. Top 10 Categories by Average Revenue Opportunity
    ax3 = fig.add_subplot(gs[1, 0])
    category_avg_revenue = df.groupby('category')['expected_revenue'].mean().sort_values(ascending=False).head(10)
    ax3.barh(range(len(category_avg_revenue)), category_avg_revenue.values / 1e8,
             color='#A29BFE', edgecolor='#6C5CE7', linewidth=1.5)
    ax3.set_yticks(range(len(category_avg_revenue)))
    ax3.set_yticklabels(category_avg_revenue.index, fontsize=9)
    ax3.set_xlabel('Average Revenue Opportunity (×100 Million)', fontsize=11, fontweight='bold')
    ax3.set_title('Top 10 Categories: Highest Avg Revenue\n(Per missing item recommendation)',
                  fontsize=12, fontweight='bold', color='#6C5CE7')
    ax3.grid(axis='x', alpha=0.3, linestyle='--')

    # 4. Revenue vs Units Sold (scatter) - Opportunity Analysis
    ax4 = fig.add_subplot(gs[1, 1])
    scatter = ax4.scatter(df['expected_units_sold'], df['expected_revenue'] / 1e8,
                         c=df['market_price'] / 1000, cmap='viridis',
                         alpha=0.7, s=120, edgecolors='black', linewidth=0.8)
    ax4.set_xlabel('Expected Units Sold', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Expected Revenue Opportunity (×100 Million)', fontsize=11, fontweight='bold')
    ax4.set_title('Revenue Opportunity vs Demand\n(Color = Market Price)',
                  fontsize=12, fontweight='bold', color='#2C3E50')
    ax4.grid(alpha=0.3, linestyle='--')
    cbar = plt.colorbar(scatter, ax=ax4)
    cbar.set_label('Market Price (×1000)', fontsize=10, fontweight='bold')

    # 5. Business Impact Summary (new panel)
    ax5 = fig.add_subplot(gs[2, :])
    ax5.axis('off')

    # Calculate key metrics
    total_revenue = df['expected_revenue'].sum() / 1e9
    avg_revenue_per_seller = df.groupby('seller_id')['expected_revenue'].sum().mean() / 1e8
    total_sellers = df['seller_id'].nunique()
    total_items = df['item_id'].nunique()
    total_recommendations = len(df)

    # Create summary text box
    summary_text = f"""
    BUSINESS IMPACT SUMMARY: Missing Items Recommendations

    📊 Total Revenue Opportunity: {total_revenue:.2f} Billion
    👥 Sellers Affected: {total_sellers:,} sellers
    📦 Unique Missing Items: {total_items:,} items
    🎯 Total Recommendations: {total_recommendations:,} (Top 10 per seller)
    💰 Average Revenue Opportunity per Seller: {avg_revenue_per_seller:.2f} ×100 Million

    These recommendations identify top-selling items that sellers currently don't have in their catalogs.
    By onboarding these items, sellers can tap into proven market demand and increase revenue.
    """

    ax5.text(0.5, 0.5, summary_text, transform=ax5.transAxes,
             fontsize=13, verticalalignment='center', horizontalalignment='center',
             bbox=dict(boxstyle='round,pad=1.5', facecolor='#E8F8F5',
                      alpha=0.9, edgecolor='#1ABC9C', linewidth=3),
             family='monospace')

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

        # Print basic statistics with story context
        print("\n" + "=" * 60)
        print("RECOMMENDATION ANALYSIS: Missing Items Opportunities")
        print("=" * 60)
        print("\nSTORY: These are top 10 selling items that each seller currently does NOT have.")
        print("       By onboarding these items, sellers can increase revenue and profit.\n")
        print("-" * 60)
        print(f"Total Recommendations: {len(df):,} (Top 10 per seller)")
        print(f"Unique Sellers: {df['seller_id'].nunique():,} sellers")
        print(f"Unique Missing Items: {df['item_id'].nunique():,} items")
        print(f"Unique Categories: {df['category'].nunique():,} categories")
        print(f"\n💰 Total Revenue Opportunity: {df['expected_revenue'].sum() / 1e9:.2f} Billion")
        print(f"💰 Average Revenue per Recommendation: {df['expected_revenue'].mean() / 1e6:.2f} Million")
        print(f"💰 Average Revenue per Seller: {df.groupby('seller_id')['expected_revenue'].sum().mean() / 1e8:.2f} ×100 Million")

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

        # 6. Top items per seller (emphasizing "top 10 per seller")
        print("\n6. Plotting top 10 missing items per seller...")
        plot_top_items_per_seller(df, num_sellers=5)

        # 7. Summary statistics
        print("\n7. Plotting summary statistics...")
        plot_summary_statistics(df)

        print("\n" + "=" * 60)
        print("Visualization Complete!")
        print("=" * 60)
        print("\nSTORY SUMMARY:")
        print("These visualizations show top 10 selling items that each seller")
        print("currently does NOT have. By onboarding these items, sellers can")
        print("increase revenue and profit.")
        print("=" * 60)

    except Exception as e:
        print(f"Error generating visualizations: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

