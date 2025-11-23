"""
Data exploration module for examining CSV file structures and data quality.
"""
import pandas as pd
from pathlib import Path
from typing import Dict, List


class DataExplorer:
    """Explores data structure and quality of CSV files."""

    def __init__(self, file_paths: Dict[int, Path]):
        """
        Initialize with list of CSV file paths.

        Args:
            file_paths: Dictionary mapping year to file path
        """
        self.file_paths = file_paths
        self.samples = {}
        self.structures = {}
        self.quality_issues = {}

    def load_sample(self, n_rows: int = 5) -> Dict[int, pd.DataFrame]:
        """
        Load first few rows from each file.

        Args:
            n_rows: Number of rows to load

        Returns:
            Dictionary of sample dataframes
        """
        self.samples = {}
        for year, file_path in self.file_paths.items():
            try:
                df = pd.read_csv(file_path, nrows=n_rows)
                self.samples[year] = df
                print(f"\n=== Sample data for {year} ===")
                print(df.head())
            except Exception as e:
                print(f"Error loading {year} data: {e}")
                self.samples[year] = None

        return self.samples

    def examine_structure(self) -> Dict[int, Dict]:
        """
        Display column names, data types, and sample data.

        Returns:
            Dictionary containing structure information for each year
        """
        self.structures = {}

        for year, file_path in self.file_paths.items():
            try:
                df = pd.read_csv(file_path, nrows=100)

                structure = {
                    'columns': list(df.columns),
                    'dtypes': df.dtypes.to_dict(),
                    'shape': df.shape,
                    'sample': df.head(3)
                }

                self.structures[year] = structure

                print(f"\n=== Structure for {year} ===")
                print(f"Shape: {structure['shape']}")
                print(f"Columns: {structure['columns']}")
                print(f"\nData types:")
                for col, dtype in structure['dtypes'].items():
                    print(f"  {col}: {dtype}")
                print(f"\nSample data:")
                print(structure['sample'])

            except Exception as e:
                print(f"Error examining structure for {year}: {e}")
                self.structures[year] = None

        return self.structures

    def check_data_quality(self) -> Dict[int, Dict]:
        """
        Identify missing values, inconsistencies, format issues.

        Returns:
            Dictionary of quality issues for each year
        """
        self.quality_issues = {}

        for year, file_path in self.file_paths.items():
            try:
                df = pd.read_csv(file_path)

                issues = {
                    'missing_values': df.isnull().sum().to_dict(),
                    'total_missing': df.isnull().sum().sum(),
                    'duplicate_rows': df.duplicated().sum(),
                    'empty_rows': df.isnull().all(axis=1).sum(),
                    'data_types': df.dtypes.to_dict()
                }

                self.quality_issues[year] = issues

                print(f"\n=== Data Quality for {year} ===")
                print(f"Total missing values: {issues['total_missing']}")
                print(f"Duplicate rows: {issues['duplicate_rows']}")
                print(f"Empty rows: {issues['empty_rows']}")

                if issues['total_missing'] > 0:
                    print("\nMissing values by column:")
                    for col, count in issues['missing_values'].items():
                        if count > 0:
                            print(f"  {col}: {count}")

            except Exception as e:
                print(f"Error checking quality for {year}: {e}")
                self.quality_issues[year] = None

        return self.quality_issues

    def generate_report(self) -> str:
        """
        Create summary report of findings.

        Returns:
            Summary report as string
        """
        report = "=" * 80 + "\n"
        report += "DATA EXPLORATION REPORT\n"
        report += "=" * 80 + "\n\n"

        for year in sorted(self.file_paths.keys()):
            report += f"Year: {year}\n"
            report += "-" * 80 + "\n"

            if year in self.structures and self.structures[year]:
                structure = self.structures[year]
                report += f"Shape: {structure['shape']}\n"
                report += f"Columns: {len(structure['columns'])}\n"

            if year in self.quality_issues and self.quality_issues[year]:
                issues = self.quality_issues[year]
                report += f"Missing values: {issues['total_missing']}\n"
                report += f"Duplicate rows: {issues['duplicate_rows']}\n"

            report += "\n"

        return report

