"""
Script to create the curated dataset for 10 selected constituencies.
"""

import pandas as pd
import os
try:
    from .data_loader import load_all_data
    from .data_processor import create_standardized_dataset, find_common_constituencies
except ImportError:
    from data_loader import load_all_data
    from data_processor import create_standardized_dataset, find_common_constituencies


def select_constituencies(common_constituencies, n=10):
    """
    Select n constituencies with diversity in states and regions.

    Selection criteria:
    - Geographic diversity (different states)
    - Mix of constituencies from different regions
    """
    # Select diverse constituencies
    # Prioritize different states
    selected_indices = []

    # Select 2-3 constituencies from different major states
    # This ensures geographic diversity
    state_counts = common_constituencies.groupby('State').size().sort_values(ascending=False)

    # Select from top states with most constituencies
    top_states = state_counts.head(5).index.tolist()

    # Track selected constituency keys to avoid duplicates
    selected_keys = set()

    for state in top_states[:4]:  # Take from 4 different states
        state_constituencies = common_constituencies[common_constituencies['State'] == state]
        if len(state_constituencies) > 0:
            idx = state_constituencies.index[0]
            row = state_constituencies.iloc[0]
            key = (row['State'], row['PC_NAME'])
            if key not in selected_keys:
                selected_indices.append(idx)
                selected_keys.add(key)
        if len(selected_indices) >= n:
            break

    # Fill remaining slots from any state
    remaining = n - len(selected_indices)
    if remaining > 0:
        # Filter out already selected constituencies
        mask = common_constituencies.apply(
            lambda x: (x['State'], x['PC_NAME']) not in selected_keys,
            axis=1
        )
        remaining_constituencies = common_constituencies[mask]

        if len(remaining_constituencies) >= remaining:
            additional_indices = remaining_constituencies.head(remaining).index.tolist()
            selected_indices.extend(additional_indices)

    # Select rows by index
    selected_df = common_constituencies.loc[selected_indices[:n]].copy().reset_index(drop=True)

    return selected_df


def create_dataset():
    """Main function to create the curated dataset."""

    print("Loading data files...")
    data = load_all_data()

    print("Finding common constituencies...")
    common = find_common_constituencies(data, min_years=3)

    print(f"Found {len(common)} constituencies present in all 3 years")

    # Select 10 constituencies
    print("\nSelecting 10 constituencies...")
    selected = select_constituencies(common, n=10)

    print("\nSelected constituencies:")
    for idx, row in selected.iterrows():
        print(f"  {idx+1}. {row['PC_NAME']}, {row['State']}")

    # Create standardized dataset
    print("\nCreating standardized dataset...")
    dataset = create_standardized_dataset(data, selected)

    print(f"\nDataset created with {len(dataset)} rows")
    print(f"Columns: {list(dataset.columns)}")

    # Save to CSV and Excel
    output_dir = 'data'
    os.makedirs(output_dir, exist_ok=True)

    csv_path = os.path.join(output_dir, 'voter_turnout_dataset.csv')
    excel_path = os.path.join(output_dir, 'voter_turnout_dataset.xlsx')

    dataset.to_csv(csv_path, index=False)
    dataset.to_excel(excel_path, index=False)

    print(f"\nDataset saved to:")
    print(f"  CSV: {csv_path}")
    print(f"  Excel: {excel_path}")

    # Save selected constituencies list
    selected.to_csv(os.path.join(output_dir, 'selected_constituencies.csv'), index=False)

    return dataset, selected


if __name__ == '__main__':
    dataset, selected = create_dataset()

    print("\nDataset summary:")
    print(dataset.groupby('Year').agg({
        'Total_Electors': 'sum',
        'Total_Votes': 'sum',
        'Overall_Turnout': 'mean'
    }))

