"""
Dashboard styling module for consistent visual appearance.
"""
from typing import List
from bokeh.plotting import figure
from bokeh.layouts import layout, column, row


class DashboardStyler:
    """Applies consistent styling to dashboard elements."""

    def __init__(self, theme: str = 'default'):
        """
        Initialize with theme name.

        Args:
            theme: Theme name ('default', 'colorblind_safe', etc.)
        """
        self.theme = theme
        self.font_family = "Arial, sans-serif"

    def apply_color_scheme(self, figures: List[figure]) -> List[figure]:
        """
        Apply consistent color scheme throughout.

        Args:
            figures: List of Bokeh figures

        Returns:
            Styled figures
        """
        for fig in figures:
            # Ensure consistent background
            fig.background_fill_color = "#ffffff"
            fig.border_fill_color = "#ffffff"

        return figures

    def style_figures(self, figures: List[figure]) -> List[figure]:
        """
        Style all figures with consistent fonts, sizes, spacing.

        Args:
            figures: List of Bokeh figures

        Returns:
            Styled figures
        """
        for fig in figures:
            # Title styling
            fig.title.text_font = self.font_family
            fig.title.text_font_size = "16pt"
            fig.title.text_font_style = "bold"
            fig.title.text_color = "#333333"

            # Axis label styling
            fig.xaxis.axis_label_text_font = self.font_family
            fig.xaxis.axis_label_text_font_size = "12pt"
            fig.xaxis.axis_label_text_color = "#333333"

            fig.yaxis.axis_label_text_font = self.font_family
            fig.yaxis.axis_label_text_font_size = "12pt"
            fig.yaxis.axis_label_text_color = "#333333"

            # Tick label styling
            fig.xaxis.major_label_text_font = self.font_family
            fig.xaxis.major_label_text_font_size = "10pt"
            fig.yaxis.major_label_text_font = self.font_family
            fig.yaxis.major_label_text_font_size = "10pt"

            # Legend styling
            if fig.legend:
                fig.legend.label_text_font = self.font_family
                fig.legend.label_text_font_size = "10pt"
                fig.legend.background_fill_alpha = 0.9
                fig.legend.border_line_color = "#cccccc"

            # Grid styling
            fig.grid.grid_line_color = "#e0e0e0"
            fig.grid.grid_line_width = 1
            fig.grid.minor_grid_line_color = "#f5f5f5"
            fig.grid.minor_grid_line_alpha = 0.5

            # Consistent spacing
            fig.min_border_left = 60
            fig.min_border_right = 60
            fig.min_border_top = 60
            fig.min_border_bottom = 60

        return figures

    def add_annotations(self, figures: List[figure]) -> List[figure]:
        """
        Add descriptive titles and annotations.

        Args:
            figures: List of Bokeh figures

        Returns:
            Figures with annotations
        """
        # Titles are already set in visualization generation
        # This method can be extended for additional annotations
        return figures

    def ensure_responsive(self, dashboard_layout) -> layout:
        """
        Ensure responsive layout for different screen sizes.

        Args:
            dashboard_layout: Bokeh layout object

        Returns:
            Responsive layout
        """
        # Bokeh layouts are responsive by default
        # Additional responsive settings can be added here
        return dashboard_layout


