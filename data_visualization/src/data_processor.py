"""
Data processing module for preparing visualization data.
"""
import pandas as pd
from typing import Dict, List, Optional


class DataProcessor:
    """Processes data for different visualization types."""

    def __init__(self, dataset: pd.DataFrame):
        """
        Initialize with consolidated dataset DataFrame.

        Args:
            dataset: Consolidated DataFrame with all years and constituencies
        """
        self.dataset = dataset
        self.processed_data = {}

    def prepare_time_series_data(self) -> pd.DataFrame:
        """
        Create time series data (aggregate turnout by year).

        Returns:
            DataFrame with year and aggregate turnout ratios
        """
        if self.dataset is None or self.dataset.empty:
            return pd.DataFrame()

        # Group by year and calculate aggregate turnout
        if 'year' not in self.dataset.columns:
            print("Warning: Year column not found")
            return pd.DataFrame()

        # Calculate aggregate turnout (average across all constituencies)
        turnout_cols = [col for col in self.dataset.columns if col.startswith('turnout')]

        if not turnout_cols:
            print("Warning: No turnout columns found")
            return pd.DataFrame()

        # Aggregate by year
        agg_data = self.dataset.groupby('year')[turnout_cols].mean().reset_index()

        self.processed_data['time_series'] = agg_data

        return agg_data

    def prepare_gender_comparison_data(self) -> pd.DataFrame:
        """
        Create gender comparison data (aggregate by year and gender).

        Returns:
            DataFrame with year, gender, and turnout ratios
        """
        if self.dataset is None or self.dataset.empty:
            return pd.DataFrame()

        if 'year' not in self.dataset.columns:
            print("Warning: Year column not found")
            return pd.DataFrame()

        # Prepare data for gender comparison
        gender_data = []

        years = sorted(self.dataset['year'].unique())

        for year in years:
            year_data = self.dataset[self.dataset['year'] == year]

            # Overall turnout
            if 'turnout_overall' in year_data.columns:
                overall = year_data['turnout_overall'].mean()
                gender_data.append({
                    'year': year,
                    'gender': 'Overall',
                    'turnout': overall
                })

            # Male turnout
            if 'turnout_male' in year_data.columns:
                male = year_data['turnout_male'].mean()
                gender_data.append({
                    'year': year,
                    'gender': 'Male',
                    'turnout': male
                })

            # Female turnout
            if 'turnout_female' in year_data.columns:
                female = year_data['turnout_female'].mean()
                gender_data.append({
                    'year': year,
                    'gender': 'Female',
                    'turnout': female
                })

        gender_df = pd.DataFrame(gender_data)
        self.processed_data['gender_comparison'] = gender_df

        return gender_df

    def prepare_constituency_time_data(self) -> pd.DataFrame:
        """
        Create constituency-time distribution data.

        Returns:
            DataFrame with constituency, year, and turnout
        """
        if self.dataset is None or self.dataset.empty:
            return pd.DataFrame()

        # Find constituency column
        constituency_col = None
        for col in self.dataset.columns:
            if 'constituency' in col.lower() or 'pc' in col.lower():
                constituency_col = col
                break

        if not constituency_col or 'year' not in self.dataset.columns:
            print("Warning: Required columns not found")
            return pd.DataFrame()

        # Select relevant columns
        cols = [constituency_col, 'year']
        if 'turnout_overall' in self.dataset.columns:
            cols.append('turnout_overall')

        dist_data = self.dataset[cols].copy()
        dist_data.rename(columns={constituency_col: 'constituency',
                                 'turnout_overall': 'turnout'}, inplace=True)

        # Normalize constituency names for consistency
        dist_data['constituency'] = dist_data['constituency'].astype(str).str.strip()

        self.processed_data['constituency_time'] = dist_data

        return dist_data

    def prepare_constituency_gender_data(self) -> pd.DataFrame:
        """
        Create constituency-gender distribution data.

        Returns:
            DataFrame with constituency, gender, and turnout
        """
        if self.dataset is None or self.dataset.empty:
            return pd.DataFrame()

        # Find constituency column
        constituency_col = None
        for col in self.dataset.columns:
            if 'constituency' in col.lower() or 'pc' in col.lower():
                constituency_col = col
                break

        if not constituency_col:
            print("Warning: Constituency column not found")
            return pd.DataFrame()

        # Prepare data for constituency-gender comparison
        gender_dist_data = []

        constituencies = self.dataset[constituency_col].unique()

        for const in constituencies:
            const_data = self.dataset[self.dataset[constituency_col] == const]

            # Average across all years for each gender
            if 'turnout_overall' in const_data.columns:
                overall = const_data['turnout_overall'].mean()
                gender_dist_data.append({
                    'constituency': str(const).strip(),
                    'gender': 'Overall',
                    'turnout': overall
                })

            if 'turnout_male' in const_data.columns:
                male = const_data['turnout_male'].mean()
                gender_dist_data.append({
                    'constituency': str(const).strip(),
                    'gender': 'Male',
                    'turnout': male
                })

            if 'turnout_female' in const_data.columns:
                female = const_data['turnout_female'].mean()
                gender_dist_data.append({
                    'constituency': str(const).strip(),
                    'gender': 'Female',
                    'turnout': female
                })

        gender_dist_df = pd.DataFrame(gender_dist_data)
        self.processed_data['constituency_gender'] = gender_dist_df

        return gender_dist_df

    def get_aggregated_data(self, viz_type: str) -> Optional[pd.DataFrame]:
        """
        Return processed data for specific visualization type.

        Args:
            viz_type: Type of visualization ('time_series', 'gender_comparison',
                     'constituency_time', 'constituency_gender')

        Returns:
            Processed DataFrame or None
        """
        if viz_type in self.processed_data:
            return self.processed_data[viz_type]

        # Generate data if not already processed
        if viz_type == 'time_series':
            return self.prepare_time_series_data()
        elif viz_type == 'gender_comparison':
            return self.prepare_gender_comparison_data()
        elif viz_type == 'constituency_time':
            return self.prepare_constituency_time_data()
        elif viz_type == 'constituency_gender':
            return self.prepare_constituency_gender_data()
        else:
            print(f"Unknown visualization type: {viz_type}")
            return None

    def filter_by_constituencies(self, constituency_list: List[str]) -> pd.DataFrame:
        """
        Filter data for selected constituencies.

        Args:
            constituency_list: List of constituency names to filter

        Returns:
            Filtered DataFrame
        """
        if self.dataset is None or self.dataset.empty:
            return pd.DataFrame()

        # Find constituency column
        constituency_col = None
        for col in self.dataset.columns:
            if 'constituency' in col.lower() or 'pc' in col.lower():
                constituency_col = col
                break

        if not constituency_col:
            return self.dataset

        # Normalize constituency names for comparison
        normalized_list = [str(c).strip().lower() for c in constituency_list]
        dataset_normalized = (
            self.dataset[constituency_col].astype(str).str.strip().str.lower()
        )

        filtered = self.dataset[dataset_normalized.isin(normalized_list)].copy()

        return filtered

