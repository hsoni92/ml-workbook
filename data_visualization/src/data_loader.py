"""
Data loader module for loading and parsing CSV files from different election years.
Handles variations in column names and data formats across 2014, 2019, and 2024.
"""

import pandas as pd
import os


def load_2014_data(filepath):
    """
    Load 2014 election data.

    Columns: State Name, PC NO., PC NAME, ELECTORS, MALE, FEMALE, OTHERS,
             TOTAL, NRI, Unnamed: 9, TOTAL VOTES, VOTER TURN OUT(%), MALE.1, FEMALE.1, OTHERS.1
    """
    df = pd.read_csv(filepath)

    # Standardize column names
    df.columns = df.columns.str.strip()

    # Rename columns to standard format
    df = df.rename(columns={
        'PC NO.': 'PC_NO',
        'PC NAME': 'PC_NAME',
        'State Name': 'State',
        'ELECTORS': 'Total_Electors',
        'MALE': 'Male_Electors',
        'FEMALE': 'Female_Electors',
        'OTHERS': 'Others_Electors',
        'TOTAL': 'Total_Electors_Sum',
        'TOTAL VOTES': 'Total_Votes',
        'VOTER TURN OUT(%)': 'Overall_Turnout',
        'MALE.1': 'Male_Turnout',
        'FEMALE.1': 'Female_Turnout',
        'OTHERS.1': 'Others_Turnout'
    })

    # Fill missing values
    df['Male_Turnout'] = pd.to_numeric(df['Male_Turnout'], errors='coerce').fillna(0)
    df['Female_Turnout'] = pd.to_numeric(df['Female_Turnout'], errors='coerce').fillna(0)
    df['Male_Electors'] = pd.to_numeric(df['Male_Electors'], errors='coerce').fillna(0)
    df['Female_Electors'] = pd.to_numeric(df['Female_Electors'], errors='coerce').fillna(0)
    df['Total_Votes'] = pd.to_numeric(df['Total_Votes'], errors='coerce').fillna(0)

    # Calculate votes polled by gender (from turnout percentages)
    df['Male_Votes'] = (df['Male_Electors'] * df['Male_Turnout'] / 100).round().fillna(0).astype(int)
    df['Female_Votes'] = (df['Female_Electors'] * df['Female_Turnout'] / 100).round().fillna(0).astype(int)

    # Postal votes = Total votes - (Male votes + Female votes)
    df['Postal_Votes'] = (df['Total_Votes'] - df['Male_Votes'] - df['Female_Votes']).clip(lower=0).astype(int)

    df['Year'] = 2014
    df['PC_NAME'] = df['PC_NAME'].str.strip()
    df['State'] = df['State'].str.strip()

    return df


def load_2019_data(filepath):
    """
    Load 2019 election data.

    Columns: State Name, PC NO., PC NAME, ELECTORS, MALE, FEMALE, THIRD GENDER,
             TOTAL, NRI, Unnamed: 9, TOTAL VOTERS, VOTER TURN OUT (%), MALE .1, FEMALE .1, THIRD GENDER
    Note: There are two 'THIRD GENDER' columns - one for electors, one for turnout
    """
    df = pd.read_csv(filepath)

    # Standardize column names - strip spaces first
    df.columns = df.columns.str.strip()

    # Get column list to handle duplicate 'THIRD GENDER' names
    cols = list(df.columns)

    # Find indices of THIRD GENDER columns
    third_gender_indices = [i for i, col in enumerate(cols) if col == 'THIRD GENDER']

    # Rename columns to standard format
    rename_dict = {
        'PC NO.': 'PC_NO',
        'PC NAME': 'PC_NAME',
        'State Name': 'State',
        'ELECTORS': 'Total_Electors',
        'MALE': 'Male_Electors',
        'FEMALE': 'Female_Electors',
        'TOTAL': 'Total_Electors_Sum',
        'TOTAL VOTERS': 'Total_Votes',
        'VOTER TURN OUT (%)': 'Overall_Turnout',
        'MALE .1': 'Male_Turnout',
        'FEMALE .1': 'Female_Turnout'
    }

    # Handle THIRD GENDER columns - first one is electors, last one is turnout
    if len(third_gender_indices) >= 1:
        # First THIRD GENDER is electors
        df.columns.values[third_gender_indices[0]] = 'Others_Electors'
    if len(third_gender_indices) >= 2:
        # Last THIRD GENDER is turnout
        df.columns.values[third_gender_indices[-1]] = 'Others_Turnout'
    elif len(third_gender_indices) == 1:
        # Only one THIRD GENDER - check if it's electors or turnout based on position
        # If it's before TOTAL VOTERS, it's electors; otherwise it might be turnout
        if third_gender_indices[0] < cols.index('TOTAL VOTERS'):
            df.columns.values[third_gender_indices[0]] = 'Others_Electors'
            # Others_Turnout might be missing or in a different column

    # Apply rename dictionary
    df = df.rename(columns=rename_dict)

    # Ensure Others_Turnout exists - if not, set to 0 or calculate
    if 'Others_Turnout' not in df.columns:
        df['Others_Turnout'] = 0

    # Fill missing values with 0 before calculations
    df['Male_Turnout'] = pd.to_numeric(df['Male_Turnout'], errors='coerce').fillna(0)
    df['Female_Turnout'] = pd.to_numeric(df['Female_Turnout'], errors='coerce').fillna(0)
    df['Male_Electors'] = pd.to_numeric(df['Male_Electors'], errors='coerce').fillna(0)
    df['Female_Electors'] = pd.to_numeric(df['Female_Electors'], errors='coerce').fillna(0)
    df['Total_Votes'] = pd.to_numeric(df['Total_Votes'], errors='coerce').fillna(0)

    # Calculate votes polled by gender
    df['Male_Votes'] = (df['Male_Electors'] * df['Male_Turnout'] / 100).round().fillna(0).astype(int)
    df['Female_Votes'] = (df['Female_Electors'] * df['Female_Turnout'] / 100).round().fillna(0).astype(int)

    # Postal votes = Total votes - (Male votes + Female votes)
    df['Postal_Votes'] = (df['Total_Votes'] - df['Male_Votes'] - df['Female_Votes']).clip(lower=0).astype(int)

    df['Year'] = 2019
    df['PC_NAME'] = df['PC_NAME'].str.strip()
    df['State'] = df['State'].str.strip()

    return df


def load_2024_data(filepath):
    """
    Load 2024 election data.

    Columns: State Name, PC NO., PC NAME, Polling Stations, Male, Female, TG, TOTAL,
             Unnamed: 8, Male.1, Female.1, TG.1, TOTAL.1, NRI, Unnamed: 14, TOTAL VOTERS,
             VOTER TURN OUT (%), Male.2, Female.2, TG.2
    First set (Male, Female, TG, TOTAL): Electors
    Second set (Male.1, Female.1, TG.1, TOTAL.1): Votes polled
    Third set (Male.2, Female.2, TG.2): Turnout percentages
    """
    df = pd.read_csv(filepath)

    # Standardize column names
    df.columns = df.columns.str.strip()

    # Rename columns to standard format
    df = df.rename(columns={
        'PC NO.': 'PC_NO',
        'PC NAME': 'PC_NAME',
        'State Name': 'State',
        'Male': 'Male_Electors',
        'Female': 'Female_Electors',
        'TG': 'Others_Electors',
        'TOTAL': 'Total_Electors',
        'TOTAL VOTERS': 'Total_Votes',
        'VOTER TURN OUT (%)': 'Overall_Turnout',
        'Male.1': 'Male_Votes',
        'Female.1': 'Female_Votes',
        'Male.2': 'Male_Turnout',
        'Female.2': 'Female_Turnout',
        'TG.2': 'Others_Turnout'
    })

    # Fill missing values
    df['Male_Votes'] = pd.to_numeric(df['Male_Votes'], errors='coerce').fillna(0)
    df['Female_Votes'] = pd.to_numeric(df['Female_Votes'], errors='coerce').fillna(0)
    df['Total_Votes'] = pd.to_numeric(df['Total_Votes'], errors='coerce').fillna(0)
    df['Male_Electors'] = pd.to_numeric(df['Male_Electors'], errors='coerce').fillna(0)
    df['Female_Electors'] = pd.to_numeric(df['Female_Electors'], errors='coerce').fillna(0)
    df['Male_Turnout'] = pd.to_numeric(df['Male_Turnout'], errors='coerce').fillna(0)
    df['Female_Turnout'] = pd.to_numeric(df['Female_Turnout'], errors='coerce').fillna(0)

    # Postal votes = Total votes - (Male votes + Female votes)
    df['Postal_Votes'] = (df['Total_Votes'] - df['Male_Votes'] - df['Female_Votes']).clip(lower=0).astype(int)

    df['Year'] = 2024
    df['PC_NAME'] = df['PC_NAME'].str.strip()
    df['State'] = df['State'].str.strip()

    return df


def load_all_data(data_dir='data'):
    """
    Load all election data files and return as dictionary.

    Returns:
        dict: Dictionary with keys '2014', '2019', '2024' containing DataFrames
    """
    data = {}

    file_2014 = os.path.join(data_dir, '2014-PC wise Voters Turn Out.csv')
    file_2019 = os.path.join(data_dir, '2019-PC Wise Voters Turn Out.csv')
    file_2024 = os.path.join(data_dir, '2024-PC-Wise-Voters-Turn-Out.csv')

    if os.path.exists(file_2014):
        data[2014] = load_2014_data(file_2014)

    if os.path.exists(file_2019):
        data[2019] = load_2019_data(file_2019)

    if os.path.exists(file_2024):
        data[2024] = load_2024_data(file_2024)

    return data

    return data


if __name__ == '__main__':
    # Test loading
    data = load_all_data()
    for year, df in data.items():
        print(f"\n{year} Data Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print(f"Sample:\n{df.head()}")

