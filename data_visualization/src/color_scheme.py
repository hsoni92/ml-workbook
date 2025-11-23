"""
Color scheme manager for consistent visualization styling.
"""
from typing import Dict, List
from bokeh.palettes import Category10, Category20, Viridis, Plasma


class ColorScheme:
    """Manages color schemes for visualizations."""

    def __init__(self, scheme_name: str = 'default'):
        """
        Initialize with color scheme name.

        Args:
            scheme_name: Name of color scheme ('default', 'colorblind_safe', 'viridis', 'plasma')
        """
        self.scheme_name = scheme_name
        self._setup_schemes()

    def _setup_schemes(self):
        """Setup color schemes."""
        # Colorblind-safe palette (based on ColorBrewer)
        self.colorblind_safe = {
            'primary': '#1f77b4',      # Blue
            'secondary': '#ff7f0e',   # Orange
            'tertiary': '#2ca02c',     # Green
            'quaternary': '#d62728',   # Red
            'quinary': '#9467bd',     # Purple
            'senary': '#8c564b',      # Brown
            'septenary': '#e377c2',    # Pink
            'octonary': '#7f7f7f',     # Gray
            'nonary': '#bcbd22',      # Yellow-green
            'denary': '#17becf'       # Cyan
        }

        # Gender-specific colors
        self.gender_colors = {
            'Male': '#1f77b4',        # Blue
            'Female': '#ff7f0e',       # Orange
            'Overall': '#2ca02c',      # Green
            'Postal': '#d62728'        # Red
        }

        # Year colors
        self.year_colors = {
            2014: '#1f77b4',          # Blue
            2019: '#ff7f0e',           # Orange
            2024: '#2ca02c'            # Green
        }

        # Default palette
        self.default_palette = Category10[10]

        # Colorblind-safe palette
        self.colorblind_palette = [
            '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
            '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
        ]

    def get_colors(self, category: str) -> Dict[str, str]:
        """
        Return color palette for specific category.

        Args:
            category: Category name ('gender', 'year', 'general')

        Returns:
            Dictionary mapping category values to colors
        """
        if category.lower() == 'gender':
            return self.gender_colors
        elif category.lower() == 'year':
            return self.year_colors
        else:
            return self.colorblind_safe

    def get_colorblind_safe(self) -> List[str]:
        """
        Return colorblind-friendly palette.

        Returns:
            List of colorblind-safe colors
        """
        return self.colorblind_palette

    def apply_theme(self, figure):
        """
        Apply color theme to Bokeh figure.

        Args:
            figure: Bokeh figure object

        Returns:
            Styled figure
        """
        # Apply consistent styling
        figure.background_fill_color = "#ffffff"
        figure.border_fill_color = "#ffffff"
        figure.outline_line_color = "#333333"
        figure.outline_line_width = 1

        # Style axes
        figure.xaxis.axis_line_color = "#333333"
        figure.xaxis.major_tick_line_color = "#333333"
        figure.xaxis.minor_tick_line_color = "#999999"
        figure.xaxis.axis_label_text_color = "#333333"
        figure.xaxis.major_label_text_color = "#333333"

        figure.yaxis.axis_line_color = "#333333"
        figure.yaxis.major_tick_line_color = "#333333"
        figure.yaxis.minor_tick_line_color = "#999999"
        figure.yaxis.axis_label_text_color = "#333333"
        figure.yaxis.major_label_text_color = "#333333"

        # Style grid
        figure.grid.grid_line_color = "#e0e0e0"
        figure.grid.grid_line_width = 1
        figure.grid.minor_grid_line_color = "#f5f5f5"

        return figure

