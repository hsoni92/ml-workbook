"""
Interactivity module for dashboard widgets and callbacks.
"""

from bokeh.models import Select, MultiSelect, CheckboxGroup, CustomJS, Button, Paragraph
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
import pandas as pd


def create_constituency_selector(constituencies, default_selection=None):
    """
    Create a checkbox group widget for constituency selection.

    Args:
        constituencies: List of constituency names
        default_selection: List of default selected constituencies

    Returns:
        tuple: (CheckboxGroup widget, container column with label)
    """
    if default_selection is None:
        default_selection = constituencies

    # Convert default_selection to indices
    default_indices = [i for i, const in enumerate(constituencies) if const in default_selection]

    widget = CheckboxGroup(
        labels=constituencies,
        active=default_indices,
        width=250
    )

    # Simple container with label
    label = Paragraph(
        text="Select Constituencies:",
        styles={
            'font_size': '15pt',
            'font_weight': 'bold',
        },
        width=250
    )
    container = column(
        label,
        widget,
        width=250,
        sizing_mode='scale_width'
    )

    return widget, container


def create_year_filter(years, default_selection=None):
    """
    Create a checkbox group for year filtering.

    Args:
        years: List of years
        default_selection: List of default selected years

    Returns:
        tuple: (CheckboxGroup widget, container column with label)
    """
    if default_selection is None:
        default_selection = list(range(len(years)))

    widget = CheckboxGroup(
        labels=[str(y) for y in years],
        active=default_selection,
        width=200
    )

    # Simple container with label
    label = Paragraph(
        text="Select Years:",
        styles={
            'font_size': '15pt',
            'font_weight': 'bold',
        },
        width=200)
    container = column(
        label,
        widget,
        width=200,
        sizing_mode='scale_width'
    )

    return widget, container


def filter_data_by_selection(dataset, selected_constituencies=None, selected_years=None):
    """
    Filter dataset based on selected constituencies and years.

    Args:
        dataset: Full dataset DataFrame
        selected_constituencies: List of selected constituency names
        selected_years: List of selected years

    Returns:
        Filtered DataFrame
    """
    filtered = dataset.copy()

    if selected_constituencies:
        filtered = filtered[filtered['PC_NAME'].isin(selected_constituencies)]

    if selected_years:
        filtered = filtered[filtered['Year'].isin(selected_years)]

    return filtered

