"""
Data processor module for standardizing and transforming election data.
"""

import pandas as pd
try:
    from .data_loader import load_all_data
except ImportError:
    from data_loader import load_all_data


def standardize_constituency_names(df):
    """
    Standardize constituency names across different years.
    Handles variations like 'Araku' vs 'Aruku', extra spaces, etc.
    """
    df = df.copy()
    df['PC_NAME'] = df['PC_NAME'].str.strip()
    df['PC_NAME'] = df['PC_NAME'].str.replace(r'\s+', ' ', regex=True)

    # Common name variations
    name_mapping = {
        'Aruku': 'Araku',
        'Araku (ST)': 'Araku',
        'Araku (ST) ': 'Araku',
    }

    df['PC_NAME'] = df['PC_NAME'].replace(name_mapping)

    return df


def find_common_constituencies(data_dict, min_years=3):
    """
    Find constituencies that appear in all specified years.

    Args:
        data_dict: Dictionary with year as key and DataFrame as value
        min_years: Minimum number of years a constituency should appear in

    Returns:
        DataFrame with constituency names and their states
    """
    all_constituencies = []

    for year, df in data_dict.items():
        df_std = standardize_constituency_names(df)
        constituencies = df_std[['State', 'PC_NAME']].drop_duplicates()
        constituencies['Year'] = year
        all_constituencies.append(constituencies)

    # Combine all years
    combined = pd.concat(all_constituencies, ignore_index=True)

    # Count occurrences of each constituency
    constituency_counts = combined.groupby(['State', 'PC_NAME']).size().reset_index(name='Count')

    # Filter constituencies that appear in all years
    common = constituency_counts[constituency_counts['Count'] >= min_years]

    return common[['State', 'PC_NAME']].sort_values(['State', 'PC_NAME'])


def create_standardized_dataset(data_dict, selected_constituencies):
    """
    Create a standardized dataset for selected constituencies.

    Args:
        data_dict: Dictionary with year as key and DataFrame as value
        selected_constituencies: List of tuples (State, PC_NAME) or DataFrame

    Returns:
        DataFrame with standardized columns
    """
    all_data = []

    for year, df in data_dict.items():
        df_std = standardize_constituency_names(df)

        # Filter selected constituencies
        if isinstance(selected_constituencies, pd.DataFrame):
            merged = df_std.merge(
                selected_constituencies[['State', 'PC_NAME']],
                on=['State', 'PC_NAME'],
                how='inner'
            )
        else:
            # If list of tuples, filter manually
            mask = df_std.apply(
                lambda row: (row['State'], row['PC_NAME']) in selected_constituencies,
                axis=1
            )
            merged = df_std[mask]

        all_data.append(merged)

    # Combine all years
    combined = pd.concat(all_data, ignore_index=True)

    # Select and rename columns to final format
    final_columns = [
        'Year', 'State', 'PC_NAME', 'PC_NO',
        'Total_Electors', 'Male_Electors', 'Female_Electors', 'Others_Electors',
        'Total_Votes', 'Male_Votes', 'Female_Votes', 'Postal_Votes',
        'Overall_Turnout', 'Male_Turnout', 'Female_Turnout', 'Others_Turnout'
    ]

    # Ensure all columns exist, fill missing with 0
    for col in final_columns:
        if col not in combined.columns:
            combined[col] = 0

    result = combined[final_columns].copy()

    # Calculate postal votes turnout if not already calculated
    result['Postal_Turnout'] = (result['Postal_Votes'] / result['Total_Electors'] * 100).round(2)
    result['Postal_Turnout'] = result['Postal_Turnout'].fillna(0)

    # Ensure numeric columns are numeric
    numeric_cols = ['Total_Electors', 'Male_Electors', 'Female_Electors', 'Others_Electors',
                    'Total_Votes', 'Male_Votes', 'Female_Votes', 'Postal_Votes',
                    'Overall_Turnout', 'Male_Turnout', 'Female_Turnout', 'Others_Turnout', 'Postal_Turnout']

    for col in numeric_cols:
        result[col] = pd.to_numeric(result[col], errors='coerce').fillna(0)

    # Sort by State, Constituency, Year
    result = result.sort_values(['State', 'PC_NAME', 'Year']).reset_index(drop=True)

    return result


def aggregate_data(df, group_by=['Year']):
    """
    Aggregate data by specified columns.

    Args:
        df: DataFrame with constituency-level data
        group_by: List of columns to group by

    Returns:
        Aggregated DataFrame
    """
    agg_dict = {
        'Total_Electors': 'sum',
        'Male_Electors': 'sum',
        'Female_Electors': 'sum',
        'Others_Electors': 'sum',
        'Total_Votes': 'sum',
        'Male_Votes': 'sum',
        'Female_Votes': 'sum',
        'Postal_Votes': 'sum'
    }

    aggregated = df.groupby(group_by).agg(agg_dict).reset_index()

    # Recalculate turnout ratios from aggregated data
    aggregated['Overall_Turnout'] = (aggregated['Total_Votes'] / aggregated['Total_Electors'] * 100).round(2)
    aggregated['Male_Turnout'] = (aggregated['Male_Votes'] / aggregated['Male_Electors'] * 100).round(2)
    aggregated['Female_Turnout'] = (aggregated['Female_Votes'] / aggregated['Female_Electors'] * 100).round(2)
    aggregated['Postal_Turnout'] = (aggregated['Postal_Votes'] / aggregated['Total_Electors'] * 100).round(2)

    # Handle division by zero
    aggregated = aggregated.replace([float('inf'), float('-inf')], 0)

    return aggregated

