"""
Dataset creation module for merging and consolidating election data.
"""
import pandas as pd
from pathlib import Path
from typing import Dict, List


class DatasetCreator:
    """Creates consolidated dataset from multiple years of election data."""

    def __init__(self, dataframes_dict: Dict[int, pd.DataFrame], selected_constituencies: List[str]):
        """
        Initialize with data and selections.

        Args:
            dataframes_dict: Dictionary mapping year to DataFrame
            selected_constituencies: List of selected constituency names (normalized)
        """
        self.dataframes_dict = dataframes_dict
        self.selected_constituencies = selected_constituencies
        self.filtered_data = {}
        self.consolidated_dataset = None

    def filter_by_constituencies(self) -> Dict[int, pd.DataFrame]:
        """
        Filter dataframes to include only selected constituencies.

        Returns:
            Dictionary of filtered DataFrames
        """
        self.filtered_data = {}

        for year, df in self.dataframes_dict.items():
            if df is None or df.empty:
                continue

            # Find constituency column
            constituency_col = None
            for col in df.columns:
                if 'constituency' in col.lower() or 'pc' in col.lower():
                    constituency_col = col
                    break

            if constituency_col:
                # Normalize constituency names for comparison
                df_filtered = df.copy()
                df_filtered['_const_normalized'] = (
                    df_filtered[constituency_col].astype(str).str.strip().str.lower()
                )

                # Filter by selected constituencies
                df_filtered = df_filtered[
                    df_filtered['_const_normalized'].isin(self.selected_constituencies)
                ].copy()

                # Drop temporary column
                df_filtered.drop('_const_normalized', axis=1, inplace=True)

                self.filtered_data[year] = df_filtered
                print(f"Filtered {year} data: {df_filtered.shape[0]} rows")

        return self.filtered_data

    def merge_data(self) -> pd.DataFrame:
        """
        Merge data from all three years for selected constituencies.

        Returns:
            Consolidated DataFrame
        """
        if not self.filtered_data:
            self.filter_by_constituencies()

        merged_dfs = []

        for year, df in self.filtered_data.items():
            if df is not None and not df.empty:
                df_with_year = df.copy()
                df_with_year['year'] = year
                merged_dfs.append(df_with_year)

        if not merged_dfs:
            print("No data to merge")
            return pd.DataFrame()

        # Concatenate all dataframes
        self.consolidated_dataset = pd.concat(merged_dfs, ignore_index=True)

        print(f"Merged dataset: {self.consolidated_dataset.shape[0]} rows, "
              f"{self.consolidated_dataset.shape[1]} columns")

        return self.consolidated_dataset

    def add_year_column(self) -> pd.DataFrame:
        """
        Add year column for time-based analysis.

        Returns:
            DataFrame with year column
        """
        if self.consolidated_dataset is None:
            self.merge_data()

        # Year column should already be added in merge_data
        if 'year' not in self.consolidated_dataset.columns:
            # Extract year from data if not present
            print("Warning: Year column not found, attempting to extract from data")

        return self.consolidated_dataset

    def calculate_aggregates(self) -> pd.DataFrame:
        """
        Calculate aggregate statistics (sums, averages) for the 10 constituencies.

        Returns:
            DataFrame with aggregate statistics
        """
        if self.consolidated_dataset is None:
            self.add_year_column()

        # Ensure we have the required columns
        numeric_cols = ['total_voters', 'male_voters', 'female_voters',
                       'total_votes_polled', 'male_votes_polled',
                       'female_votes_polled', 'postal_votes',
                       'turnout_overall', 'turnout_male', 'turnout_female', 'turnout_postal']

        available_numeric_cols = [col for col in numeric_cols
                                 if col in self.consolidated_dataset.columns]

        # Add aggregate columns
        if 'year' in self.consolidated_dataset.columns:
            # Group by year and calculate aggregates
            agg_dict = {}
            for col in available_numeric_cols:
                if col.startswith('turnout'):
                    agg_dict[col] = 'mean'  # Average for ratios
                else:
                    agg_dict[col] = 'sum'  # Sum for counts

            aggregates = self.consolidated_dataset.groupby('year')[available_numeric_cols].agg(agg_dict)
            aggregates.reset_index(inplace=True)

            print("\nAggregate statistics by year:")
            print(aggregates)

        return self.consolidated_dataset

    def validate_dataset(self) -> bool:
        """
        Check data consistency and completeness.

        Returns:
            True if dataset is valid
        """
        if self.consolidated_dataset is None or self.consolidated_dataset.empty:
            print("Dataset is empty")
            return False

        # Check for required columns
        required_cols = ['constituency', 'state', 'year']
        missing_cols = [col for col in required_cols
                       if col not in self.consolidated_dataset.columns]

        if missing_cols:
            print(f"Missing required columns: {missing_cols}")
            return False

        # Check for missing values in key columns
        key_cols = ['constituency', 'state', 'year']
        for col in key_cols:
            if col in self.consolidated_dataset.columns:
                missing = self.consolidated_dataset[col].isnull().sum()
                if missing > 0:
                    print(f"Warning: {missing} missing values in {col}")

        # Check that we have data for all selected constituencies
        if 'constituency' in self.consolidated_dataset.columns:
            const_normalized = (
                self.consolidated_dataset['constituency']
                .astype(str).str.strip().str.lower()
            )
            found_constituencies = set(const_normalized.unique())
            selected_set = set(self.selected_constituencies)

            missing = selected_set - found_constituencies
            if missing:
                print(f"Warning: Missing data for constituencies: {missing}")

        # Check that we have data for all years
        if 'year' in self.consolidated_dataset.columns:
            years = set(self.consolidated_dataset['year'].unique())
            expected_years = set(self.dataframes_dict.keys())
            missing_years = expected_years - years
            if missing_years:
                print(f"Warning: Missing data for years: {missing_years}")

        print("Dataset validation completed")
        return True

    def export_to_excel(self, filepath: Path) -> bool:
        """
        Export consolidated dataset to Excel.

        Args:
            filepath: Path to save Excel file

        Returns:
            True if export successful
        """
        if self.consolidated_dataset is None:
            print("No dataset to export")
            return False

        try:
            # Ensure output directory exists
            filepath.parent.mkdir(parents=True, exist_ok=True)

            # Export to Excel
            self.consolidated_dataset.to_excel(filepath, index=False)
            print(f"Dataset exported to {filepath}")
            return True

        except Exception as e:
            print(f"Error exporting dataset: {e}")
            return False

    def export_to_csv(self, filepath: Path) -> bool:
        """
        Export consolidated dataset to CSV.

        Args:
            filepath: Path to save CSV file

        Returns:
            True if export successful
        """
        if self.consolidated_dataset is None:
            print("No dataset to export")
            return False

        try:
            # Ensure output directory exists
            filepath.parent.mkdir(parents=True, exist_ok=True)

            # Export to CSV
            self.consolidated_dataset.to_csv(filepath, index=False)
            print(f"Dataset exported to {filepath}")
            return True

        except Exception as e:
            print(f"Error exporting dataset: {e}")
            return False

    def get_dataset(self) -> pd.DataFrame:
        """
        Return the consolidated DataFrame.

        Returns:
            Consolidated DataFrame
        """
        return self.consolidated_dataset

