"""
Script to explore data structure and identify available constituencies.
"""

import pandas as pd
try:
    from .data_loader import load_all_data
    from .data_processor import find_common_constituencies, standardize_constituency_names
except ImportError:
    from data_loader import load_all_data
    from data_processor import find_common_constituencies, standardize_constituency_names


def explore_data():
    """Explore the data structure and find common constituencies."""

    print("Loading data files...")
    data = load_all_data()

    print(f"\nLoaded data for years: {sorted(data.keys())}")

    # Show data structure for each year
    for year in sorted(data.keys()):
        df = data[year]
        print(f"\n{year} Data:")
        print(f"  Shape: {df.shape}")
        print(f"  Columns: {list(df.columns)}")
        print(f"  States: {df['State'].nunique()}")
        print(f"  Constituencies: {df['PC_NAME'].nunique()}")

    # Find common constituencies
    print("\n" + "="*60)
    print("Finding constituencies common across all years...")
    common = find_common_constituencies(data, min_years=3)

    print(f"\nFound {len(common)} constituencies present in all 3 years")
    print("\nSample constituencies:")
    print(common.head(20))

    # Show distribution by state
    print("\n" + "="*60)
    print("Distribution by State:")
    state_counts = common.groupby('State').size().sort_values(ascending=False)
    print(state_counts.head(20))

    return data, common


if __name__ == '__main__':
    data, common_constituencies = explore_data()

    # Save common constituencies list
    common_constituencies.to_csv('data/common_constituencies.csv', index=False)
    print(f"\nSaved common constituencies to data/common_constituencies.csv")
