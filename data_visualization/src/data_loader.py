"""
Data loading and cleaning module for CSV files.
"""
import pandas as pd
from pathlib import Path
from typing import Dict, Optional, Any
import re


class DataLoader:
    """Loads and cleans CSV data files."""

    def __init__(self, file_paths: Dict[int, Path]):
        """
        Initialize with file paths dictionary.

        Args:
            file_paths: Dictionary mapping year to file path {year: path}
        """
        self.file_paths = file_paths
        self.loaded_data = {}
        self.standardized_columns = {}

    def load_file(self, file_path: Path, year: int) -> Optional[pd.DataFrame]:
        """
        Load CSV file.

        Args:
            file_path: Path to CSV file
            year: Year of the election

        Returns:
            Loaded DataFrame or None if error
        """
        try:
            # Load CSV file (header is in first row, already cleaned)
            df = pd.read_csv(file_path)
            print(f"Successfully loaded {year} data from CSV file")

            # Clean up: remove rows that are all NaN
            df = df.dropna(how='all')

            # Remove rows where first column is NaN (usually header/metadata rows)
            first_col = df.columns[0]
            df = df[df[first_col].notna()]

            print(f"Loaded {year} data: {df.shape[0]} rows, {df.shape[1]} columns")
            return df

        except Exception as e:
            print(f"Error loading file {file_path} for year {year}: {e}")
            import traceback
            traceback.print_exc()
            return None

    def preprocess_dataframe(self, df: pd.DataFrame, year: int) -> pd.DataFrame:
        """
        Comprehensive preprocessing pipeline for raw DataFrame.

        Args:
            df: Raw DataFrame from CSV
            year: Year of the data

        Returns:
            Preprocessed DataFrame
        """
        if df is None or df.empty:
            return df

        df_clean = df.copy()
        initial_shape = df_clean.shape

        # a. Remove empty columns (all NaN or empty strings)
        empty_cols = []
        for col in df_clean.columns:
            # Check if column is all NaN or all empty strings
            if df_clean[col].isna().all():
                empty_cols.append(col)
            elif df_clean[col].dtype == 'object':
                # Check if all values are empty strings or whitespace
                if df_clean[col].astype(str).str.strip().eq('').all() or \
                   df_clean[col].astype(str).str.strip().eq('nan').all():
                    empty_cols.append(col)

        if empty_cols:
            df_clean = df_clean.drop(columns=empty_cols)
            print(f"  Removed {len(empty_cols)} empty columns: {empty_cols[:5]}{'...' if len(empty_cols) > 5 else ''}")

        # b. Remove duplicate rows
        initial_rows = len(df_clean)
        df_clean = df_clean.drop_duplicates()
        duplicates_removed = initial_rows - len(df_clean)
        if duplicates_removed > 0:
            print(f"  Removed {duplicates_removed} duplicate rows")

        # c. Remove rows with all NaN values
        initial_rows = len(df_clean)
        df_clean = df_clean.dropna(how='all')
        empty_rows_removed = initial_rows - len(df_clean)
        if empty_rows_removed > 0:
            print(f"  Removed {empty_rows_removed} completely empty rows")

        # d. Clean column names (strip spaces, normalize)
        df_clean.columns = [str(col).strip() for col in df_clean.columns]

        # Remove rows where first column is NaN (usually header/metadata rows)
        if len(df_clean) > 0:
            first_col = df_clean.columns[0]
            initial_rows = len(df_clean)
            df_clean = df_clean[df_clean[first_col].notna()]
            metadata_rows_removed = initial_rows - len(df_clean)
            if metadata_rows_removed > 0:
                print(f"  Removed {metadata_rows_removed} rows with missing first column")

        final_shape = df_clean.shape
        print(f"  Preprocessing: {initial_shape} → {final_shape} (removed {initial_shape[0] - final_shape[0]} rows, {initial_shape[1] - final_shape[1]} columns)")

        return df_clean

    def standardize_columns(self, df: pd.DataFrame, year: int) -> pd.DataFrame:
        """
        Standardize column names across years with year-specific mapping logic.

        Args:
            df: DataFrame to standardize
            year: Year of the data

        Returns:
            DataFrame with standardized column names (no duplicates)
        """
        if df is None or df.empty:
            return df

        df_std = df.copy()
        original_columns = list(df_std.columns)
        standardized_cols = {}  # Maps original column name -> standardized name

        # Normalize column names for matching
        normalized_columns = [str(col).lower().strip().replace(' ', '_').replace('-', '_')
                            for col in original_columns]

        # Year-specific column mapping
        if year == 2024:
            # 2024 structure: State Name, PC NO., PC NAME, Polling Stations,
            # Male, Female, TG, TOTAL, (empty), Male, Female, TG, TOTAL, NRI, (empty),
            # TOTAL VOTERS, VOTER TURN OUT (%), Male, Female, TG
            for i, (orig_col, norm_col) in enumerate(zip(original_columns, normalized_columns)):
                col_clean = norm_col.replace('_', '').replace('.', '')

                # Basic identifiers
                if 'statename' in col_clean or (col_clean == 'state' and i == 0):
                    standardized_cols[orig_col] = 'state'
                elif 'pcname' in col_clean or 'pc_name' in col_clean:
                    standardized_cols[orig_col] = 'constituency'
                elif 'pcno' in col_clean or 'pc_no' in col_clean:
                    standardized_cols[orig_col] = 'pc_no'
                elif 'pollingstations' in col_clean:
                    standardized_cols[orig_col] = 'polling_stations'

                # First group (voters): Male, Female, TG, TOTAL (positions 4-7)
                elif i == 4 and 'male' in col_clean:
                    standardized_cols[orig_col] = 'male_voters'
                elif i == 5 and 'female' in col_clean:
                    standardized_cols[orig_col] = 'female_voters'
                elif i == 6 and ('tg' in col_clean or 'third' in col_clean):
                    standardized_cols[orig_col] = 'tg_voters'
                elif i == 7 and 'total' in col_clean and 'voters' not in col_clean and 'votes' not in col_clean:
                    standardized_cols[orig_col] = 'total_voters_group1'

                # Second group (votes): Male, Female, TG, TOTAL (positions 9-12)
                elif i == 9 and 'male' in col_clean:
                    standardized_cols[orig_col] = 'male_votes_polled'
                elif i == 10 and 'female' in col_clean:
                    standardized_cols[orig_col] = 'female_votes_polled'
                elif i == 11 and ('tg' in col_clean or 'third' in col_clean):
                    standardized_cols[orig_col] = 'tg_votes_polled'
                elif i == 12 and 'total' in col_clean and 'voters' not in col_clean and 'votes' not in col_clean:
                    standardized_cols[orig_col] = 'total_votes_polled'
                elif i == 13 and 'nri' in col_clean:
                    standardized_cols[orig_col] = 'nri_votes'

                # Total voters (position 15)
                elif i == 15 and 'totalvoters' in col_clean:
                    standardized_cols[orig_col] = 'total_voters'
                elif i == 16 and 'turnout' in col_clean:
                    standardized_cols[orig_col] = 'turnout_overall_reported'
                # Last group (turnout %): Male, Female, TG (positions 17-19) - skip these

        elif year == 2019:
            # 2019 structure: State Name, PC NO., PC NAME, ELECTORS,
            # MALE, FEMALE, THIRD GENDER, TOTAL, NRI, (empty), TOTAL VOTERS,
            # VOTER TURN OUT (%), MALE, FEMALE, THIRD GENDER
            for i, (orig_col, norm_col) in enumerate(zip(original_columns, normalized_columns)):
                col_clean = norm_col.replace('_', '').replace('.', '')

                # Basic identifiers
                if 'statename' in col_clean or (col_clean == 'state' and i == 0):
                    standardized_cols[orig_col] = 'state'
                elif 'pcname' in col_clean or 'pc_name' in col_clean:
                    standardized_cols[orig_col] = 'constituency'
                elif 'pcno' in col_clean or 'pc_no' in col_clean:
                    standardized_cols[orig_col] = 'pc_no'
                elif i == 3 and 'electors' in col_clean:
                    standardized_cols[orig_col] = 'total_voters'

                # Voters group: MALE, FEMALE, THIRD GENDER, TOTAL (positions 4-7)
                elif i == 4 and 'male' in col_clean:
                    standardized_cols[orig_col] = 'male_voters'
                elif i == 5 and 'female' in col_clean:
                    standardized_cols[orig_col] = 'female_voters'
                elif i == 6 and ('thirdgender' in col_clean or 'tg' in col_clean):
                    standardized_cols[orig_col] = 'tg_voters'
                elif i == 7 and 'total' in col_clean and 'voters' not in col_clean and 'votes' not in col_clean:
                    # For 2019, this TOTAL column contains votes data
                    standardized_cols[orig_col] = 'total_votes_polled'
                elif i == 8 and 'nri' in col_clean:
                    standardized_cols[orig_col] = 'nri_votes'

                # Total voters (position 10) - this is a duplicate/redundant column
                elif i == 10 and 'totalvoters' in col_clean:
                    # Skip if we already have total_voters from ELECTORS
                    pass
                elif i == 11 and 'turnout' in col_clean:
                    standardized_cols[orig_col] = 'turnout_overall_reported'
                # Last group (turnout %): MALE, FEMALE, THIRD GENDER (positions 12-14) - skip

        elif year == 2014:
            # 2014 structure: State Name, PC NO., PC NAME, ELECTORS,
            # MALE, FEMALE, OTHERS, TOTAL, NRI, (empty), TOTAL VOTES,
            # VOTER TURN OUT(%), MALE, FEMALE, OTHERS
            for i, (orig_col, norm_col) in enumerate(zip(original_columns, normalized_columns)):
                col_clean = norm_col.replace('_', '').replace('.', '')

                # Basic identifiers
                if 'statename' in col_clean or (col_clean == 'state' and i == 0):
                    standardized_cols[orig_col] = 'state'
                elif 'pcname' in col_clean or 'pc_name' in col_clean:
                    standardized_cols[orig_col] = 'constituency'
                elif 'pcno' in col_clean or 'pc_no' in col_clean:
                    standardized_cols[orig_col] = 'pc_no'
                elif i == 3 and 'electors' in col_clean:
                    standardized_cols[orig_col] = 'total_voters'

                # Voters group: MALE, FEMALE, OTHERS, TOTAL (positions 4-7)
                elif i == 4 and 'male' in col_clean:
                    standardized_cols[orig_col] = 'male_voters'
                elif i == 5 and 'female' in col_clean:
                    standardized_cols[orig_col] = 'female_voters'
                elif i == 6 and ('others' in col_clean or 'tg' in col_clean):
                    standardized_cols[orig_col] = 'tg_voters'
                elif i == 7 and 'total' in col_clean and 'voters' not in col_clean and 'votes' not in col_clean:
                    standardized_cols[orig_col] = 'total_voters_group1'
                elif i == 8 and 'nri' in col_clean:
                    standardized_cols[orig_col] = 'nri_votes'

                # Total votes (position 10)
                elif i == 10 and 'totalvotes' in col_clean:
                    standardized_cols[orig_col] = 'total_votes_polled'
                elif i == 11 and 'turnout' in col_clean:
                    standardized_cols[orig_col] = 'turnout_overall_reported'
                # Last group (turnout %): MALE, FEMALE, OTHERS (positions 12-14) - skip

        # Fallback: if position-based mapping didn't work, try name-based matching
        # This handles cases where column order might vary
        for i, (orig_col, norm_col) in enumerate(zip(original_columns, normalized_columns)):
            if orig_col in standardized_cols:
                continue  # Already mapped

            col_clean = norm_col.replace('_', '').replace('.', '')

            # Try to match by name patterns
            if 'statename' in col_clean and 'state' not in standardized_cols.values():
                standardized_cols[orig_col] = 'state'
            elif ('pcname' in col_clean or 'constituency' in col_clean) and 'constituency' not in standardized_cols.values():
                standardized_cols[orig_col] = 'constituency'
            elif 'electors' in col_clean and 'total_voters' not in standardized_cols.values():
                standardized_cols[orig_col] = 'total_voters'
            elif 'totalvoters' in col_clean and 'total_voters' not in standardized_cols.values():
                standardized_cols[orig_col] = 'total_voters'
            elif 'totalvotes' in col_clean and 'turnout' not in col_clean and 'total_votes_polled' not in standardized_cols.values():
                standardized_cols[orig_col] = 'total_votes_polled'

        # Apply renaming (only rename mapped columns to avoid duplicates)
        df_std.rename(columns=standardized_cols, inplace=True)

        # Ensure no duplicate column names exist
        if df_std.columns.duplicated().any():
            # Handle duplicates by keeping first occurrence and renaming others
            cols = list(df_std.columns)
            seen = {}
            new_cols = []
            for col in cols:
                if col in seen:
                    seen[col] += 1
                    new_cols.append(f"{col}_dup{seen[col]}")
                else:
                    seen[col] = 0
                    new_cols.append(col)
            df_std.columns = new_cols

        self.standardized_columns[year] = list(df_std.columns)

        return df_std

    def normalize_text_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Normalize constituency and state names for consistent matching across years.

        Args:
            df: DataFrame with standardized columns

        Returns:
            DataFrame with normalized text columns
        """
        if df is None or df.empty:
            return df

        df_norm = df.copy()

        # Normalize constituency column
        if 'constituency' in df_norm.columns:
            df_norm['constituency'] = (
                df_norm['constituency']
                .astype(str)
                .str.strip()
                .str.title()  # Title case for consistency
                .str.replace(r'\s+', ' ', regex=True)  # Remove extra spaces
                .str.replace(r'\(', ' (', regex=True)  # Normalize parentheses spacing
                .str.replace(r'\)', ') ', regex=True)
                .str.replace(r'\s+', ' ', regex=True)  # Remove extra spaces again
                .str.strip()
            )
            # Create normalized version for matching (lowercase, no special chars)
            df_norm['constituency_normalized'] = (
                df_norm['constituency']
                .str.lower()
                .str.replace(r'[^a-z0-9\s]', '', regex=True)
                .str.replace(r'\s+', ' ', regex=True)
                .str.strip()
            )

        # Normalize state column
        if 'state' in df_norm.columns:
            df_norm['state'] = (
                df_norm['state']
                .astype(str)
                .str.strip()
                .str.title()  # Title case for consistency
                .str.replace(r'\s+', ' ', regex=True)  # Remove extra spaces
                .str.strip()
            )
            # Create normalized version for matching
            df_norm['state_normalized'] = (
                df_norm['state']
                .str.lower()
                .str.replace(r'[^a-z0-9\s]', '', regex=True)
                .str.replace(r'\s+', ' ', regex=True)
                .str.strip()
            )

        return df_norm

    def extract_variables(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Extract required variables with improved column detection and error handling.

        Args:
            df: DataFrame with standardized columns

        Returns:
            DataFrame with extracted and validated variables
        """
        if df is None or df.empty:
            return df

        extracted_df = df.copy()
        col_list = [str(col).lower() for col in extracted_df.columns]

        # Strategy 1: Use already standardized columns if they exist
        # Strategy 2: Find columns by name patterns
        # Strategy 3: Use position-based detection as fallback

        # Map of required columns to possible patterns
        column_patterns = {
            'total_voters': ['total_voters', 'electors', 'totalvoters'],
            'male_voters': ['male_voters', 'male'],
            'female_voters': ['female_voters', 'female'],
            'tg_voters': ['tg_voters', 'thirdgender', 'others'],
            'total_votes_polled': ['total_votes_polled', 'totalvotes', 'total_votes'],
            'male_votes_polled': ['male_votes_polled', 'male.1'],
            'female_votes_polled': ['female_votes_polled', 'female.1'],
            'tg_votes_polled': ['tg_votes_polled', 'tg.1', 'thirdgender.1', 'others.1'],
            'nri_votes': ['nri_votes', 'nri'],
            'postal_votes': ['postal_votes', 'postal']
        }

        # Find and map columns using multiple strategies
        found_columns = {}

        for std_name, patterns in column_patterns.items():
            if std_name in extracted_df.columns:
                # Already exists with correct name
                found_columns[std_name] = std_name
                continue

            # Try to find by pattern matching
            for pattern in patterns:
                for i, col in enumerate(col_list):
                    col_clean = col.replace('_', '').replace('.', '').replace(' ', '')
                    pattern_clean = pattern.replace('_', '').replace('.', '').replace(' ', '')

                    # Exact match or contains pattern
                    if pattern_clean in col_clean or col_clean == pattern_clean:
                        orig_col = extracted_df.columns[i]
                        # Avoid mapping turnout percentage columns
                        if 'turnout' not in col and orig_col not in found_columns.values():
                            found_columns[std_name] = orig_col
                            break

                if std_name in found_columns:
                    break

        # Rename found columns to standard names
        rename_map = {v: k for k, v in found_columns.items() if k != v}
        if rename_map:
            extracted_df.rename(columns=rename_map, inplace=True)

        # For 2019 and 2014, we may need to extract votes from TOTAL column
        # Check if we have total_voters_group1 but not total_votes_polled
        if 'total_voters_group1' in extracted_df.columns and 'total_votes_polled' not in extracted_df.columns:
            # The TOTAL column might contain votes data
            # Try to find it in a different column
            for col in extracted_df.columns:
                col_lower = str(col).lower()
                if 'total' in col_lower and 'voters' not in col_lower and 'votes' not in col_lower:
                    # This might be the votes column
                    if 'total_votes_polled' not in extracted_df.columns:
                        extracted_df.rename(columns={col: 'total_votes_polled'}, inplace=True)
                        break

        # Convert numeric columns
        numeric_cols = ['total_voters', 'male_voters', 'female_voters', 'tg_voters',
                       'total_votes_polled', 'male_votes_polled', 'female_votes_polled',
                       'tg_votes_polled', 'nri_votes', 'postal_votes', 'pc_no', 'polling_stations']

        for col in numeric_cols:
            if col in extracted_df.columns:
                try:
                    # Ensure it's a Series before converting
                    if isinstance(extracted_df[col], pd.Series):
                        extracted_df[col] = pd.to_numeric(extracted_df[col], errors='coerce')
                    else:
                        print(f"Warning: Column '{col}' is not a Series, skipping conversion")
                except Exception as e:
                    print(f"Warning: Could not convert column '{col}' to numeric: {e}")
            else:
                # Create column with NaN if it doesn't exist (for optional columns)
                if col in ['tg_voters', 'tg_votes_polled', 'nri_votes', 'postal_votes']:
                    extracted_df[col] = pd.NA

        # Validate required columns exist
        required_cols = ['state', 'constituency', 'total_voters']
        missing_required = [col for col in required_cols if col not in extracted_df.columns]
        if missing_required:
            print(f"Warning: Missing required columns after extraction: {missing_required}")

        return extracted_df

    def clean_missing_values(self, df: pd.DataFrame, year: int) -> pd.DataFrame:
        """
        Handle missing values strategically based on column type and importance.

        Args:
            df: DataFrame with extracted variables
            year: Year of the data

        Returns:
            DataFrame with cleaned missing values
        """
        if df is None or df.empty:
            return df

        df_clean = df.copy()
        missing_report = {}

        # Critical columns: drop rows with missing values
        critical_cols = ['state', 'constituency']
        for col in critical_cols:
            if col in df_clean.columns:
                initial_count = len(df_clean)
                df_clean = df_clean[df_clean[col].notna()]
                missing_count = initial_count - len(df_clean)
                if missing_count > 0:
                    missing_report[col] = f"Dropped {missing_count} rows with missing {col}"
                    print(f"  Dropped {missing_count} rows with missing {col}")

        # Numeric voter/vote columns: fill with 0 (assume no data = 0)
        numeric_fill_zero = ['total_voters', 'male_voters', 'female_voters', 'tg_voters',
                            'total_votes_polled', 'male_votes_polled', 'female_votes_polled',
                            'tg_votes_polled', 'nri_votes', 'postal_votes', 'pc_no', 'polling_stations']

        for col in numeric_fill_zero:
            if col in df_clean.columns:
                missing_before = df_clean[col].isna().sum()
                if missing_before > 0:
                    df_clean[col] = df_clean[col].fillna(0).infer_objects(copy=False)
                    missing_report[col] = f"Filled {missing_before} missing values with 0"
                    if missing_before > len(df_clean) * 0.1:  # More than 10% missing
                        print(f"  Warning: {missing_before} missing values in '{col}' ({missing_before/len(df_clean)*100:.1f}%)")

        # Optional columns: fill with 0 or median based on type
        optional_cols = ['tg_voters', 'tg_votes_polled', 'nri_votes', 'postal_votes']
        for col in optional_cols:
            if col in df_clean.columns:
                missing_count = df_clean[col].isna().sum()
                if missing_count > 0:
                    df_clean[col] = df_clean[col].fillna(0)

        # Text columns: fill with 'Unknown' if needed (but we already dropped rows with missing critical text)
        text_cols = ['state', 'constituency']
        for col in text_cols:
            if col in df_clean.columns:
                # Convert any remaining NaN to string 'Unknown'
                df_clean[col] = df_clean[col].fillna('Unknown')

        return df_clean

    def validate_dataframe(self, df: pd.DataFrame, year: int) -> Dict[str, Any]:
        """
        Validate data integrity and consistency after preprocessing.

        Args:
            df: DataFrame to validate
            year: Year of the data

        Returns:
            Dictionary with validation results and report
        """
        validation_report = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'stats': {}
        }

        if df is None or df.empty:
            validation_report['is_valid'] = False
            validation_report['errors'].append("DataFrame is None or empty")
            return validation_report

        # Check required columns exist
        required_cols = ['state', 'constituency', 'total_voters']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            validation_report['is_valid'] = False
            validation_report['errors'].append(f"Missing required columns: {missing_cols}")

        # Check numeric columns are actually numeric
        numeric_cols = ['total_voters', 'male_voters', 'female_voters', 'total_votes_polled',
                       'male_votes_polled', 'female_votes_polled']
        for col in numeric_cols:
            if col in df.columns:
                if not pd.api.types.is_numeric_dtype(df[col]):
                    validation_report['warnings'].append(f"Column '{col}' is not numeric type")
                else:
                    # Check for negative values (counts should be non-negative)
                    negative_count = (df[col] < 0).sum()
                    if negative_count > 0:
                        validation_report['warnings'].append(
                            f"Column '{col}' has {negative_count} negative values"
                        )

        # Check turnout percentages are between 0-100 (if present)
        turnout_cols = [col for col in df.columns if 'turnout' in col.lower() and 'reported' not in col.lower()]
        for col in turnout_cols:
            if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
                invalid_turnout = ((df[col] < 0) | (df[col] > 100)).sum()
                if invalid_turnout > 0:
                    validation_report['warnings'].append(
                        f"Column '{col}' has {invalid_turnout} values outside 0-100 range"
                    )

        # Check data consistency: votes should be <= voters
        if 'total_voters' in df.columns and 'total_votes_polled' in df.columns:
            inconsistent = (df['total_votes_polled'] > df['total_voters'] * 1.1).sum()  # Allow 10% tolerance
            if inconsistent > 0:
                validation_report['warnings'].append(
                    f"{inconsistent} rows where total_votes_polled > total_voters (with 10% tolerance)"
                )

        if 'male_voters' in df.columns and 'male_votes_polled' in df.columns:
            inconsistent = (df['male_votes_polled'] > df['male_voters'] * 1.1).sum()
            if inconsistent > 0:
                validation_report['warnings'].append(
                    f"{inconsistent} rows where male_votes_polled > male_voters (with 10% tolerance)"
                )

        if 'female_voters' in df.columns and 'female_votes_polled' in df.columns:
            inconsistent = (df['female_votes_polled'] > df['female_voters'] * 1.1).sum()
            if inconsistent > 0:
                validation_report['warnings'].append(
                    f"{inconsistent} rows where female_votes_polled > female_voters (with 10% tolerance)"
                )

        # Check for duplicate constituency names (might indicate data issues)
        if 'constituency' in df.columns:
            duplicates = df['constituency'].duplicated().sum()
            if duplicates > 0:
                validation_report['warnings'].append(
                    f"{duplicates} duplicate constituency names found (may be expected)"
                )

        # Statistics
        validation_report['stats'] = {
            'total_rows': len(df),
            'total_columns': len(df.columns),
            'required_columns_present': len([c for c in required_cols if c in df.columns]),
            'numeric_columns': len([c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])])
        }

        # Print validation summary
        if validation_report['errors']:
            print(f"  Validation errors for {year}:")
            for error in validation_report['errors']:
                print(f"    - {error}")

        if validation_report['warnings']:
            print(f"  Validation warnings for {year}:")
            for warning in validation_report['warnings'][:5]:  # Show first 5 warnings
                print(f"    - {warning}")
            if len(validation_report['warnings']) > 5:
                print(f"    ... and {len(validation_report['warnings']) - 5} more warnings")

        if validation_report['is_valid'] and not validation_report['warnings']:
            print(f"  Validation passed for {year}: {validation_report['stats']['total_rows']} rows, "
                  f"{validation_report['stats']['total_columns']} columns")

        return validation_report

    def calculate_turnout_ratios(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate voter turnout ratios (overall, male, female, postal).

        Args:
            df: DataFrame with voter and vote data

        Returns:
            DataFrame with added turnout ratio columns
        """
        if df is None or df.empty:
            return df

        df_ratios = df.copy()

        # Calculate overall turnout ratio
        if 'total_voters' in df_ratios.columns and 'total_votes_polled' in df_ratios.columns:
            df_ratios['turnout_overall'] = (
                df_ratios['total_votes_polled'] / df_ratios['total_voters'] * 100
            )

        # Calculate male turnout ratio
        if 'male_voters' in df_ratios.columns and 'male_votes_polled' in df_ratios.columns:
            df_ratios['turnout_male'] = (
                df_ratios['male_votes_polled'] / df_ratios['male_voters'] * 100
            )

        # Calculate female turnout ratio
        if 'female_voters' in df_ratios.columns and 'female_votes_polled' in df_ratios.columns:
            df_ratios['turnout_female'] = (
                df_ratios['female_votes_polled'] / df_ratios['female_voters'] * 100
            )

        # Calculate postal turnout ratio (if postal votes data available)
        if 'postal_votes' in df_ratios.columns and 'total_voters' in df_ratios.columns:
            df_ratios['turnout_postal'] = (
                df_ratios['postal_votes'] / df_ratios['total_voters'] * 100
            )

        # Replace inf and NaN values with 0
        ratio_cols = [col for col in df_ratios.columns if col.startswith('turnout')]
        for col in ratio_cols:
            df_ratios[col] = df_ratios[col].replace([float('inf'), float('-inf')], 0)
            df_ratios[col] = df_ratios[col].fillna(0)

        return df_ratios

    def load_all_years(self) -> Dict[int, pd.DataFrame]:
        """
        Load and process all three years with comprehensive preprocessing pipeline.

        Returns:
            Dictionary of processed DataFrames {year: DataFrame}
        """
        self.loaded_data = {}

        for year, file_path in self.file_paths.items():
            print(f"\nProcessing {year} data...")

            try:
                # Step 1: Load file
                df = self.load_file(file_path, year)
                if df is None:
                    print(f"  Error: Failed to load {year} data")
                    continue

                # Step 2: Preprocess dataframe (remove empty cols, duplicates, etc.)
                df = self.preprocess_dataframe(df, year)
                if df is None or df.empty:
                    print(f"  Error: DataFrame is empty after preprocessing for {year}")
                    continue

                # Step 3: Standardize columns (year-specific mapping)
                df = self.standardize_columns(df, year)
                if df is None or df.empty:
                    print(f"  Error: DataFrame is empty after column standardization for {year}")
                    continue

                # Step 4: Normalize text columns (constituency, state names)
                df = self.normalize_text_columns(df)

                # Step 5: Extract variables (with improved column detection)
                df = self.extract_variables(df)
                if df is None or df.empty:
                    print(f"  Error: DataFrame is empty after variable extraction for {year}")
                    continue

                # Step 6: Clean missing values (strategic filling)
                df = self.clean_missing_values(df, year)

                # Step 7: Validate dataframe (check integrity and consistency)
                validation_result = self.validate_dataframe(df, year)
                if not validation_result['is_valid']:
                    print(f"  Warning: Validation failed for {year}, but continuing...")

                # Step 8: Calculate turnout ratios
                df = self.calculate_turnout_ratios(df)

                # Store processed data
                self.loaded_data[year] = df
                print(f"  Successfully processed {year} data: {df.shape[0]} rows, {df.shape[1]} columns")

            except Exception as e:
                print(f"  Error processing {year} data: {e}")
                import traceback
                traceback.print_exc()
                continue

        return self.loaded_data

    def get_loaded_data(self) -> Dict[int, pd.DataFrame]:
        """
        Return processed dataframes.

        Returns:
            Dictionary of processed DataFrames
        """
        return self.loaded_data

