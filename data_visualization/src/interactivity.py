"""
Interactivity module for dashboard widgets and callbacks.
"""

from bokeh.models import Select, MultiSelect, CheckboxGroup, CustomJS
from bokeh.models import ColumnDataSource
import pandas as pd


def create_constituency_selector(constituencies, default_selection=None):
    """
    Create a multi-select widget for constituency selection.

    Args:
        constituencies: List of constituency names
        default_selection: List of default selected constituencies

    Returns:
        MultiSelect widget
    """
    if default_selection is None:
        default_selection = constituencies

    widget = MultiSelect(
        title="Select Constituencies:",
        value=default_selection,
        options=constituencies,
        width=200,
        height=150
    )

    return widget


def create_year_filter(years, default_selection=None):
    """
    Create a checkbox group for year filtering.

    Args:
        years: List of years
        default_selection: List of default selected years

    Returns:
        CheckboxGroup widget
    """
    if default_selection is None:
        default_selection = list(range(len(years)))

    widget = CheckboxGroup(
        labels=[str(y) for y in years],
        active=default_selection,
        width=150
    )

    return widget


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

