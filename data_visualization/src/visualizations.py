"""
Visualization generation module using Bokeh.
"""
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from typing import Dict, Optional
from color_scheme import ColorScheme


class VisualizationGenerator:
    """Generates Bokeh visualizations for voter turnout data."""

    def __init__(self, data_processor, color_scheme: Optional[ColorScheme] = None):
        """
        Initialize with DataProcessor and color scheme.

        Args:
            data_processor: DataProcessor instance
            color_scheme: ColorScheme instance (optional)
        """
        self.data_processor = data_processor
        self.color_scheme = color_scheme or ColorScheme('colorblind_safe')
        self.plots = {}

    def _apply_gestalt_principles(self, fig):
        """
        Apply Gestalt principles to figure (proximity, similarity, continuity).

        Args:
            fig: Bokeh figure

        Returns:
            Styled figure
        """
        # Proximity: Group related elements with consistent spacing
        fig.min_border_left = 60
        fig.min_border_right = 60
        fig.min_border_top = 60
        fig.min_border_bottom = 60

        # Similarity: Use consistent styling for similar elements
        fig.title.text_font_size = "16pt"
        fig.title.text_font_style = "bold"
        fig.title.align = "center"

        # Continuity: Smooth visual flow
        fig.xaxis.major_label_orientation = 0
        fig.yaxis.major_label_orientation = 0

        return fig

    def _setup_figure(self, title: str, x_label: str, y_label: str,
                     width: int = 800, height: int = 500) -> figure:
        """
        Create base figure with consistent styling.

        Args:
            title: Figure title
            x_label: X-axis label
            y_label: Y-axis label
            width: Figure width
            height: Figure height

        Returns:
            Styled Bokeh figure
        """
        fig = figure(
            title=title,
            x_axis_label=x_label,
            y_axis_label=y_label,
            width=width,
            height=height,
            tools="pan,wheel_zoom,box_zoom,reset,save,hover"
        )

        # Apply color scheme theme
        self.color_scheme.apply_theme(fig)

        # Apply Gestalt principles
        self._apply_gestalt_principles(fig)

        return fig

    def plot_turnout_over_time(self, data: Optional[pd.DataFrame] = None) -> figure:
        """
        Create line chart showing aggregate voter turnout ratio over time.

        Args:
            data: Time series data (optional, will fetch from processor if not provided)

        Returns:
            Bokeh figure
        """
        if data is None:
            data = self.data_processor.get_aggregated_data('time_series')

        if data is None or data.empty:
            print("No data available for time series plot")
            return figure()

        # Prepare data
        if 'year' not in data.columns or 'turnout_overall' not in data.columns:
            print("Required columns not found in data")
            return figure()

        source = ColumnDataSource(data)

        # Create figure
        fig = self._setup_figure(
            title="Voter Turnout Ratio Over Time (Aggregate)",
            x_label="Year",
            y_label="Turnout Ratio (%)"
        )

        # Add line
        fig.line(
            x='year',
            y='turnout_overall',
            source=source,
            line_width=3,
            line_color=self.color_scheme.get_colors('general')['primary'],
            legend_label="Overall Turnout"
        )

        # Add markers
        fig.scatter(
            x='year',
            y='turnout_overall',
            source=source,
            size=10,
            color=self.color_scheme.get_colors('general')['primary'],
            fill_alpha=0.8
        )

        # Add hover tool
        hover = HoverTool(
            tooltips=[
                ("Year", "@year"),
                ("Turnout", "@turnout_overall{0.2f}%")
            ]
        )
        fig.add_tools(hover)

        fig.legend.location = "top_left"
        self.plots['time_series'] = fig

        return fig

    def plot_turnout_by_gender(self, data: Optional[pd.DataFrame] = None) -> figure:
        """
        Create multi-line chart for gender comparison.

        Args:
            data: Gender comparison data (optional)

        Returns:
            Bokeh figure
        """
        if data is None:
            data = self.data_processor.get_aggregated_data('gender_comparison')

        if data is None or data.empty:
            print("No data available for gender comparison plot")
            return figure()

        if 'year' not in data.columns or 'gender' not in data.columns or 'turnout' not in data.columns:
            print("Required columns not found in data")
            return figure()

        # Create figure
        fig = self._setup_figure(
            title="Voter Turnout Ratio by Gender Over Time (Aggregate)",
            x_label="Year",
            y_label="Turnout Ratio (%)"
        )

        # Get gender colors
        gender_colors = self.color_scheme.get_colors('gender')

        # Plot line for each gender
        genders = data['gender'].unique()
        for gender in genders:
            gender_data = data[data['gender'] == gender].sort_values('year')
            source = ColumnDataSource(gender_data)

            color = gender_colors.get(gender, self.color_scheme.colorblind_palette[0])

            fig.line(
                x='year',
                y='turnout',
                source=source,
                line_width=3,
                line_color=color,
                legend_label=gender
            )

            fig.scatter(
                x='year',
                y='turnout',
                source=source,
                size=10,
                color=color,
                fill_alpha=0.8
            )

        # Add hover tool
        hover = HoverTool(
            tooltips=[
                ("Year", "@year"),
                ("Gender", "@gender"),
                ("Turnout", "@turnout{0.2f}%")
            ]
        )
        fig.add_tools(hover)

        fig.legend.location = "top_left"
        self.plots['gender_comparison'] = fig

        return fig

    def plot_constituency_time_distribution(self, data: Optional[pd.DataFrame] = None) -> figure:
        """
        Create heatmap/grouped bar for constituency-time distribution.

        Args:
            data: Constituency-time data (optional)

        Returns:
            Bokeh figure
        """
        if data is None:
            data = self.data_processor.get_aggregated_data('constituency_time')

        if data is None or data.empty:
            print("No data available for constituency-time distribution plot")
            return figure()

        if 'constituency' not in data.columns or 'year' not in data.columns or 'turnout' not in data.columns:
            print("Required columns not found in data")
            return figure()

        # Check for duplicates and handle them
        duplicates = data.duplicated(subset=['constituency', 'year'], keep=False)
        if duplicates.any():
            print(f"Warning: Found {duplicates.sum()} duplicate entries for (constituency, year) combinations. Aggregating using mean.")
            # Group by constituency and year, taking the mean of turnout to handle duplicates
            data = data.groupby(['constituency', 'year'], as_index=False)['turnout'].mean()

        # Pivot data for heatmap
        try:
            pivot_data = data.pivot(index='constituency', columns='year', values='turnout')
        except ValueError as e:
            # If pivot still fails, use pivot_table with aggregation
            print(f"Pivot failed, using pivot_table with aggregation: {e}")
            pivot_data = data.pivot_table(index='constituency', columns='year', values='turnout', aggfunc='mean')

        pivot_data = pivot_data.fillna(0)

        # Prepare data for plotting
        constituencies = pivot_data.index.tolist()
        years = pivot_data.columns.tolist()

        # Create figure
        fig = self._setup_figure(
            title="Voter Turnout Distribution: Constituencies Across Time",
            x_label="Year",
            y_label="Constituency",
            width=800,
            height=max(500, len(constituencies) * 40)
        )

        # Get color palette
        colors = self.color_scheme.get_colorblind_safe()
        year_colors = self.color_scheme.get_colors('year')

        # Create heatmap using rect glyphs
        x = []
        y = []
        colors_list = []
        alphas = []
        turnouts = []

        for i, const in enumerate(constituencies):
            for j, year in enumerate(years):
                turnout = pivot_data.loc[const, year]
                x.append(year)
                y.append(i)
                turnouts.append(turnout)

                # Map turnout to color (normalize to 0-1)
                max_turnout = pivot_data.max().max()
                min_turnout = pivot_data.min().min()
                if max_turnout > min_turnout:
                    normalized = (turnout - min_turnout) / (max_turnout - min_turnout)
                else:
                    normalized = 0.5

                # Use color from palette based on year
                color = year_colors.get(year, colors[j % len(colors)])
                colors_list.append(color)
                alphas.append(0.6 + normalized * 0.4)

        source = ColumnDataSource(dict(
            x=x,
            y=y,
            colors=colors_list,
            alphas=alphas,
            turnouts=turnouts,
            constituencies=[constituencies[int(yi)] for yi in y],
            years=x
        ))

        # Draw rectangles
        fig.rect(
            x='x',
            y='y',
            width=0.8,
            height=0.8,
            source=source,
            fill_color='colors',
            fill_alpha='alphas',
            line_color='white',
            line_width=1
        )

        # Set y-axis labels
        fig.yaxis.ticker = list(range(len(constituencies)))
        fig.yaxis.major_label_overrides = {i: const for i, const in enumerate(constituencies)}

        # Add hover tool
        hover = HoverTool(
            tooltips=[
                ("Constituency", "@constituencies"),
                ("Year", "@years"),
                ("Turnout", "@turnouts{0.2f}%")
            ]
        )
        fig.add_tools(hover)

        self.plots['constituency_time'] = fig

        return fig

    def plot_constituency_gender_distribution(self, data: Optional[pd.DataFrame] = None) -> figure:
        """
        Create grouped bar chart for constituency-gender distribution.

        Args:
            data: Constituency-gender data (optional)

        Returns:
            Bokeh figure
        """
        if data is None:
            data = self.data_processor.get_aggregated_data('constituency_gender')

        if data is None or data.empty:
            print("No data available for constituency-gender distribution plot")
            return figure()

        if 'constituency' not in data.columns or 'gender' not in data.columns or 'turnout' not in data.columns:
            print("Required columns not found in data")
            return figure()

        # Prepare data for grouped bars
        constituencies = sorted(data['constituency'].unique())
        genders = sorted(data['gender'].unique())

        # Create figure
        fig = self._setup_figure(
            title="Voter Turnout Distribution: Constituencies by Gender",
            x_label="Constituency",
            y_label="Turnout Ratio (%)",
            width=max(800, len(constituencies) * 60),
            height=500
        )

        # Get gender colors
        gender_colors = self.color_scheme.get_colors('gender')

        # Create grouped bars
        x_positions = []
        turnouts = []
        colors_list = []
        gender_labels = []
        constituency_labels = []

        bar_width = 0.25
        for i, const in enumerate(constituencies):
            const_data = data[data['constituency'] == const]
            for j, gender in enumerate(genders):
                gender_data = const_data[const_data['gender'] == gender]
                if not gender_data.empty:
                    x_pos = i + (j - len(genders)/2 + 0.5) * bar_width
                    x_positions.append(x_pos)
                    turnouts.append(gender_data['turnout'].iloc[0])
                    colors_list.append(gender_colors.get(gender, self.color_scheme.colorblind_palette[j]))
                    gender_labels.append(gender)
                    constituency_labels.append(const)

        source = ColumnDataSource(dict(
            x=x_positions,
            y=turnouts,
            colors=colors_list,
            genders=gender_labels,
            constituencies=constituency_labels
        ))

        # Draw bars
        fig.vbar(
            x='x',
            top='y',
            width=bar_width,
            source=source,
            fill_color='colors',
            fill_alpha=0.8,
            line_color='white',
            line_width=1,
            legend_field='genders'
        )

        # Set x-axis labels
        fig.xaxis.ticker = list(range(len(constituencies)))
        fig.xaxis.major_label_overrides = {i: const for i, const in enumerate(constituencies)}
        fig.xaxis.major_label_orientation = 1.2

        # Add hover tool
        hover = HoverTool(
            tooltips=[
                ("Constituency", "@constituencies"),
                ("Gender", "@genders"),
                ("Turnout", "@y{0.2f}%")
            ]
        )
        fig.add_tools(hover)

        fig.legend.location = "top_right"
        self.plots['constituency_gender'] = fig

        return fig

    def get_all_plots(self) -> Dict[str, figure]:
        """
        Return dictionary of all four plots.

        Returns:
            Dictionary mapping plot names to Bokeh figures
        """
        if not self.plots:
            # Generate all plots
            self.plot_turnout_over_time()
            self.plot_turnout_by_gender()
            self.plot_constituency_time_distribution()
            self.plot_constituency_gender_distribution()

        return self.plots


