"""
Configuration manager for the voter turnout dashboard application.
"""
import os
from pathlib import Path


class Config:
    """Manages configuration settings for the dashboard application."""

    def __init__(self):
        """Initialize with default configuration."""
        # Base directory
        self.base_dir = Path(__file__).parent

        # Data file paths
        self.data_dir = self.base_dir / "data"
        self.file_paths = {
            2024: self.data_dir / "2024-PC-Wise-Voters-Turn-Out.csv",
            2019: self.data_dir / "2019-PC Wise Voters Turn Out.csv",
            2014: self.data_dir / "2014-PC wise Voters Turn Out.csv"
        }

        # Output paths
        self.output_dir = self.base_dir / "output"
        self.output_dir.mkdir(exist_ok=True)
        self.output_paths = {
            'dataset': self.output_dir / "voter_turnout_dataset.csv",
            'dashboard': self.output_dir / "voter_turnout_dashboard.html",
            'notebook': self.base_dir / "dashboard.ipynb"
        }

        # Visualization settings
        self.visualization_settings = {
            'figure_width': 800,
            'figure_height': 500,
            'color_scheme': 'colorblind_safe',
            'font_size': '12pt',
            'title_font_size': '16pt'
        }

        # Number of constituencies to select
        self.num_constituencies = 10

    def load_from_file(self, filepath):
        """Load configuration from file (future enhancement)."""
        # Placeholder for loading from JSON/YAML file
        pass

    def get_file_paths(self):
        """Return file paths for data files."""
        return self.file_paths

    def get_output_paths(self):
        """Return output file paths."""
        return self.output_paths

    def get_visualization_settings(self):
        """Return visualization settings (colors, sizes, etc.)."""
        return self.visualization_settings

