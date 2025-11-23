"""
Constituency selection module for choosing diverse constituencies.
"""
import pandas as pd
from typing import Dict, List, Set
from collections import Counter


class ConstituencySelector:
    """Selects diverse constituencies from election data."""

    def __init__(self, dataframes_dict: Dict[int, pd.DataFrame]):
        """
        Initialize with loaded dataframes.

        Args:
            dataframes_dict: Dictionary mapping year to DataFrame {year: DataFrame}
        """
        self.dataframes_dict = dataframes_dict
        self.common_constituencies = []
        self.selected_constituencies = []
        self.name_mapping = {}

    def find_common_constituencies(self) -> List[str]:
        """
        Find constituencies present in all three years.

        Returns:
            List of constituency names present in all years
        """
        if not self.dataframes_dict:
            return []

        # Get constituency names from each year
        constituency_sets = {}
        for year, df in self.dataframes_dict.items():
            if df is not None and not df.empty:
                # Try different possible column names
                constituency_col = None
                for col in df.columns:
                    if 'constituency' in col.lower() or 'pc' in col.lower():
                        constituency_col = col
                        break

                if constituency_col:
                    # Normalize constituency names
                    constituencies = df[constituency_col].astype(str).str.strip().str.lower()
                    constituency_sets[year] = set(constituencies.unique())

        if len(constituency_sets) < 3:
            print("Warning: Not all years have data")
            return []

        # Find intersection of all years
        common = set.intersection(*constituency_sets.values())
        self.common_constituencies = sorted(list(common))

        print(f"Found {len(self.common_constituencies)} common constituencies across all years")

        return self.common_constituencies

    def analyze_geographic_distribution(self) -> Dict[str, int]:
        """
        Analyze state-wise distribution of constituencies.

        Returns:
            Dictionary mapping state to count of constituencies
        """
        if not self.dataframes_dict:
            return {}

        state_distribution = Counter()

        for year, df in self.dataframes_dict.items():
            if df is not None and not df.empty:
                # Find state column
                state_col = None
                for col in df.columns:
                    if 'state' in col.lower():
                        state_col = col
                        break

                if state_col:
                    states = df[state_col].astype(str).str.strip()
                    state_distribution.update(states.unique())

        distribution_dict = dict(state_distribution)
        print("\nState-wise distribution of constituencies:")
        for state, count in sorted(distribution_dict.items(), key=lambda x: x[1], reverse=True):
            print(f"  {state}: {count}")

        return distribution_dict

    def select_diverse_constituencies(self, n: int = 10) -> List[str]:
        """
        Select diverse constituencies (geographic diversity, different states).

        Args:
            n: Number of constituencies to select

        Returns:
            List of selected constituency names
        """
        if not self.common_constituencies:
            self.find_common_constituencies()

        if not self.common_constituencies:
            print("No common constituencies found")
            return []

        # Get state information for each constituency
        constituency_states = {}

        for year, df in self.dataframes_dict.items():
            if df is not None and not df.empty:
                constituency_col = None
                state_col = None

                for col in df.columns:
                    if 'constituency' in col.lower() or 'pc' in col.lower():
                        constituency_col = col
                    if 'state' in col.lower():
                        state_col = col

                if constituency_col and state_col:
                    for _, row in df.iterrows():
                        const_name = str(row[constituency_col]).strip().lower()
                        state_name = str(row[state_col]).strip()
                        if const_name in self.common_constituencies:
                            if const_name not in constituency_states:
                                constituency_states[const_name] = state_name

        # Group constituencies by state
        state_groups = {}
        for const, state in constituency_states.items():
            if state not in state_groups:
                state_groups[state] = []
            state_groups[state].append(const)

        # Select diverse constituencies
        selected = []
        states_used = set()

        # First, try to get at least one from each state
        for state, constituencies in state_groups.items():
            if len(selected) < n and constituencies:
                selected.append(constituencies[0])
                states_used.add(state)

        # Fill remaining slots with diverse selection
        remaining = n - len(selected)
        if remaining > 0:
            # Get constituencies from states not yet represented
            for state, constituencies in state_groups.items():
                if len(selected) >= n:
                    break
                for const in constituencies:
                    if const not in selected and len(selected) < n:
                        selected.append(const)
                        states_used.add(state)
                        break

        # If still need more, fill from any state
        if len(selected) < n:
            for const in self.common_constituencies:
                if const not in selected and len(selected) < n:
                    selected.append(const)

        self.selected_constituencies = selected[:n]

        print(f"\nSelected {len(self.selected_constituencies)} constituencies:")
        for i, const in enumerate(self.selected_constituencies, 1):
            state = constituency_states.get(const, "Unknown")
            print(f"  {i}. {const.title()} ({state})")

        return self.selected_constituencies

    def standardize_names(self) -> Dict[str, str]:
        """
        Create mapping for constituency name standardization across years.

        Returns:
            Dictionary mapping normalized name to original names by year
        """
        self.name_mapping = {}

        for year, df in self.dataframes_dict.items():
            if df is not None and not df.empty:
                constituency_col = None
                for col in df.columns:
                    if 'constituency' in col.lower() or 'pc' in col.lower():
                        constituency_col = col
                        break

                if constituency_col:
                    for _, row in df.iterrows():
                        const_name = str(row[constituency_col]).strip()
                        const_normalized = const_name.lower().strip()

                        if const_normalized not in self.name_mapping:
                            self.name_mapping[const_normalized] = {}
                        self.name_mapping[const_normalized][year] = const_name

        return self.name_mapping

    def get_selected_constituencies(self) -> List[str]:
        """
        Return list of selected constituency names.

        Returns:
            List of selected constituency names
        """
        return self.selected_constituencies

    def validate_selection(self) -> bool:
        """
        Ensure selected constituencies have complete data.

        Returns:
            True if all selected constituencies have complete data
        """
        if not self.selected_constituencies:
            print("No constituencies selected")
            return False

        all_valid = True

        for year, df in self.dataframes_dict.items():
            if df is not None and not df.empty:
                constituency_col = None
                for col in df.columns:
                    if 'constituency' in col.lower() or 'pc' in col.lower():
                        constituency_col = col
                        break

                if constituency_col:
                    df_constituencies = df[constituency_col].astype(str).str.strip().str.lower()
                    missing = []

                    for const in self.selected_constituencies:
                        if const not in df_constituencies.values:
                            missing.append(const)

                    if missing:
                        print(f"Warning: {year} data missing for: {missing}")
                        all_valid = False

        if all_valid:
            print("All selected constituencies have complete data across all years")

        return all_valid

