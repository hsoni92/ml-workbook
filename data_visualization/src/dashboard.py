"""
Dashboard builder module for creating the main dashboard layout.
"""
from bokeh.plotting import figure
from bokeh.layouts import layout, column, row
from bokeh.models import Div
from typing import Dict
from visualizations import VisualizationGenerator
from data_processor import DataProcessor
from styling import DashboardStyler


class DashboardBuilder:
    """Builds the main dashboard layout."""

    def __init__(self, visualization_generator: VisualizationGenerator,
                 data_processor: DataProcessor):
        """
        Initialize with visualization generator and data processor.

        Args:
            visualization_generator: VisualizationGenerator instance
            data_processor: DataProcessor instance
        """
        self.visualization_generator = visualization_generator
        self.data_processor = data_processor
        self.styler = DashboardStyler()
        self.dashboard_layout = None

    def create_layout(self) -> layout:
        """
        Arrange four visualizations in a grid layout using Bokeh's layout.

        Returns:
            Bokeh layout object
        """
        # Get all plots
        plots = self.visualization_generator.get_all_plots()

        if not plots:
            print("No plots available")
            return column()

        # Get individual plots
        plot_time = plots.get('time_series')
        plot_gender = plots.get('gender_comparison')
        plot_const_time = plots.get('constituency_time')
        plot_const_gender = plots.get('constituency_gender')

        # Create 2x2 grid layout
        top_row = row([plot_time, plot_gender], sizing_mode='scale_both')
        bottom_row = row([plot_const_time, plot_const_gender], sizing_mode='scale_both')

        self.dashboard_layout = column([top_row, bottom_row], sizing_mode='scale_both')

        return self.dashboard_layout

    def add_title_and_description(self) -> layout:
        """
        Add dashboard title and description.

        Returns:
            Layout with title and description
        """
        title = Div(
            text="""
            <h1 style="text-align: center; color: #333333; font-family: Arial, sans-serif;
                       font-size: 28pt; margin-bottom: 10px;">
                Voter Turnout Dashboard
            </h1>
            <p style="text-align: center; color: #666666; font-family: Arial, sans-serif;
                      font-size: 12pt; margin-bottom: 20px;">
                Analysis of Voter Turnout Changes Across 10 Selected Constituencies<br>
                General Elections: 2014, 2019, 2024
            </p>
            """,
            width=1600,
            height=100
        )

        if self.dashboard_layout is None:
            self.create_layout()

        full_layout = column([title, self.dashboard_layout], sizing_mode='scale_both')

        return full_layout

    def apply_styling(self) -> layout:
        """
        Apply consistent styling across all visualizations.

        Returns:
            Styled layout
        """
        if self.dashboard_layout is None:
            self.create_layout()

        # Get all plots and apply styling
        plots = self.visualization_generator.get_all_plots()
        figures = list(plots.values())

        # Apply styling
        self.styler.apply_color_scheme(figures)
        self.styler.style_figures(figures)
        self.styler.add_annotations(figures)

        return self.dashboard_layout

    def build(self):
        """
        Build complete dashboard and return Bokeh document.

        Returns:
            Complete dashboard layout
        """
        # Create layout
        self.create_layout()

        # Apply styling
        self.apply_styling()

        # Add title and description
        final_layout = self.add_title_and_description()

        return final_layout


