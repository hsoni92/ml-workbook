"""
Visualization functions for creating the four required charts.
"""

import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, Legend
from bokeh.transform import factor_cmap
try:
    from .styling import create_figure
    from .color_scheme import (
        COLOR_OVERALL, COLOR_MALE, COLOR_FEMALE, COLOR_POSTAL,
        COLOR_2014, COLOR_2019, COLOR_2024,
        PALETTE_GENDER, PALETTE_YEARS
    )
except ImportError:
    from styling import create_figure
    from color_scheme import (
        COLOR_OVERALL, COLOR_MALE, COLOR_FEMALE, COLOR_POSTAL,
        COLOR_2014, COLOR_2019, COLOR_2024,
        PALETTE_GENDER, PALETTE_YEARS
    )


def create_visualization_a(aggregated_data):
    """
    Visualization A: Change in voter turnout ratio over time (aggregate).

    Args:
        aggregated_data: DataFrame with Year and Overall_Turnout columns

    Returns:
        Bokeh figure
    """
    # Prepare data
    data = aggregated_data.sort_values('Year')

    source = ColumnDataSource(data={
        'Year': data['Year'].astype(str),
        'Turnout': data['Overall_Turnout'],
        'Year_num': data['Year']
    })

    # Create figure
    fig = create_figure(
        title='Change in Voter Turnout Ratio Over Time (Aggregate)',
        x_label='Election Year',
        y_label='Voter Turnout Ratio (%)',
        width=500,
        height=350,
        x_range=data['Year'].astype(str).tolist()
    )

    # Add line
    line = fig.line(
        x='Year',
        y='Turnout',
        source=source,
        line_width=3,
        line_color=COLOR_OVERALL,
        alpha=0.8
    )

    # Add markers
    fig.scatter(
        x='Year',
        y='Turnout',
        source=source,
        size=10,
        color=COLOR_OVERALL,
        alpha=0.9
    )

    # Add hover tool
    hover = HoverTool(
        tooltips=[
            ('Year', '@Year'),
            ('Turnout', '@Turnout{0.2f}%')
        ],
        mode='vline'
    )
    fig.add_tools(hover)

    return fig


def create_visualization_b(aggregated_data):
    """
    Visualization B: Change in voter turnout ratio across genders (aggregate).

    Args:
        aggregated_data: DataFrame with Year, Male_Turnout, Female_Turnout columns

    Returns:
        Bokeh figure
    """
    # Prepare data
    data = aggregated_data.sort_values('Year')
    years = data['Year'].astype(str).tolist()

    source = ColumnDataSource(data={
        'Year': years,
        'Male': data['Male_Turnout'],
        'Female': data['Female_Turnout'],
        'Year_num': data['Year']
    })

    # Create figure
    fig = create_figure(
        title='Change in Voter Turnout Ratio Across Genders (Aggregate)',
        x_label='Election Year',
        y_label='Voter Turnout Ratio (%)',
        width=500,
        height=350,
        x_range=years
    )

    # Add lines for Male and Female
    line_male = fig.line(
        x='Year',
        y='Male',
        source=source,
        line_width=3,
        line_color=COLOR_MALE,
        alpha=0.8,
        legend_label='Male'
    )

    line_female = fig.line(
        x='Year',
        y='Female',
        source=source,
        line_width=3,
        line_color=COLOR_FEMALE,
        alpha=0.8,
        legend_label='Female'
    )

    # Add markers
    fig.scatter(x='Year', y='Male', source=source, size=10, color=COLOR_MALE, alpha=0.9)
    fig.scatter(x='Year', y='Female', source=source, size=10, color=COLOR_FEMALE, alpha=0.9)

    # Add hover tool
    hover = HoverTool(
        tooltips=[
            ('Year', '@Year'),
            ('Male Turnout', '@Male{0.2f}%'),
            ('Female Turnout', '@Female{0.2f}%')
        ],
        mode='vline'
    )
    fig.add_tools(hover)

    # Legend
    fig.legend.location = 'top_left'
    fig.legend.label_text_font_size = '10pt'

    return fig


def create_visualization_c(dataset):
    """
    Visualization C: Distribution of voter turnout across constituencies and time.

    Args:
        dataset: DataFrame with PC_NAME, Year, Overall_Turnout columns

    Returns:
        Bokeh figure
    """
    # Prepare data for grouped bar chart
    pivot_data = dataset.pivot_table(
        values='Overall_Turnout',
        index='PC_NAME',
        columns='Year',
        aggfunc='mean'
    ).fillna(0)

    constituencies = pivot_data.index.tolist()
    years = sorted(pivot_data.columns)

    # Create data sources for each year
    from bokeh.transform import dodge
    from bokeh.models import FactorRange

    # Create figure with FactorRange for categorical x-axis
    fig = create_figure(
        title='Distribution of Voter Turnout Across Constituencies and Time',
        x_label='Constituency',
        y_label='Voter Turnout Ratio (%)',
        width=800,
        height=400,
        x_range=FactorRange(*constituencies)
    )

    # Color mapping for years
    colors = {2014: COLOR_2014, 2019: COLOR_2019, 2024: COLOR_2024}

    # Create bars for each year
    offsets = [-0.2, 0, 0.2]
    for i, year in enumerate(years):
        year_data = pivot_data[year].tolist()
        source = ColumnDataSource(data={
            'Constituency': constituencies,
            'Turnout': year_data
        })

        offset = offsets[i] if i < len(offsets) else (i - 1) * 0.2
        fig.vbar(
            x=dodge('Constituency', offset, range=fig.x_range),
            top='Turnout',
            source=source,
            width=0.2,
            color=colors[year],
            alpha=0.8,
            legend_label=str(year)
        )

    # Rotate x-axis labels
    fig.xaxis.major_label_orientation = 45

    # Add hover tool
    hover = HoverTool(
        tooltips=[
            ('Constituency', '@Constituency'),
            ('Turnout', '@Turnout{0.2f}%')
        ]
    )
    fig.add_tools(hover)

    fig.legend.location = 'top_right'
    fig.legend.label_text_font_size = '10pt'

    return fig


def create_visualization_d(dataset):
    """
    Visualization D: Distribution of voter turnout across constituencies and genders.

    Args:
        dataset: DataFrame with PC_NAME, Male_Turnout, Female_Turnout columns

    Returns:
        Bokeh figure
    """
    # Aggregate by constituency (average across years)
    constituency_avg = dataset.groupby('PC_NAME').agg({
        'Male_Turnout': 'mean',
        'Female_Turnout': 'mean'
    }).reset_index()

    constituencies = constituency_avg['PC_NAME'].tolist()

    source = ColumnDataSource(data={
        'Constituency': constituencies,
        'Male': constituency_avg['Male_Turnout'],
        'Female': constituency_avg['Female_Turnout']
    })

    # Grouped bars
    from bokeh.transform import dodge
    from bokeh.models import FactorRange

    # Create figure with FactorRange for categorical x-axis
    fig = create_figure(
        title='Distribution of Voter Turnout Across Constituencies and Genders',
        x_label='Constituency',
        y_label='Voter Turnout Ratio (%)',
        width=800,
        height=400,
        x_range=FactorRange(*constituencies)
    )

    # Male bars
    fig.vbar(
        x=dodge('Constituency', -0.15, range=fig.x_range),
        top='Male',
        source=source,
        width=0.3,
        color=COLOR_MALE,
        alpha=0.8,
        legend_label='Male'
    )

    # Female bars
    fig.vbar(
        x=dodge('Constituency', 0.15, range=fig.x_range),
        top='Female',
        source=source,
        width=0.3,
        color=COLOR_FEMALE,
        alpha=0.8,
        legend_label='Female'
    )

    # Rotate x-axis labels
    fig.xaxis.major_label_orientation = 45

    # Add hover tool
    hover = HoverTool(
        tooltips=[
            ('Constituency', '@Constituency'),
            ('Male Turnout', '@Male{0.2f}%'),
            ('Female Turnout', '@Female{0.2f}%')
        ]
    )
    fig.add_tools(hover)

    fig.legend.location = 'top_right'
    fig.legend.label_text_font_size = '10pt'

    return fig

