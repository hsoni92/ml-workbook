"""
Interactivity module for dashboard widgets and callbacks.
"""

from bokeh.models import Select, MultiSelect, CheckboxGroup, CustomJS, Button, Div
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
import pandas as pd


def create_constituency_selector(constituencies, default_selection=None):
    """
    Create a checkbox group widget for constituency selection enclosed in a styled box.

    Args:
        constituencies: List of constituency names
        default_selection: List of default selected constituencies

    Returns:
        tuple: (CheckboxGroup widget, styled container Div)
    """
    if default_selection is None:
        default_selection = constituencies

    # Convert default_selection to indices
    default_indices = [i for i, const in enumerate(constituencies) if const in default_selection]

    widget = CheckboxGroup(
        labels=constituencies,
        active=default_indices,
        width=230,
        margin=(0, 15, 0, 15)
    )

    # Create a container column that visually wraps the title and checkbox in a box
    container = column(
        # Top section with title and top border
        Div(
            text="""
            <div style="
                border: 2px solid #e0e0e0;
                border-bottom: none;
                border-radius: 5px 5px 0 0;
                background-color: #f9f9f9;
                padding: 15px 15px 10px 15px;
            ">
                <h4 style="
                    margin: 0;
                    padding: 0;
                    color: #333;
                    font-weight: bold;
                ">Select Constituencies</h4>
            </div>
            """,
            width=260,
            height=50,
            margin=(0, 0, 0, 0)
        ),
        # Middle section: wrapper div with side borders, containing the checkbox group
        column(
            Div(
                text="<div style='border-left: 2px solid #e0e0e0; border-right: 2px solid #e0e0e0; background-color: #f9f9f9; padding: 10px 0;'></div>",
                width=260,
                height=10,
                margin=(0, 0, 0, 0)
            ),
            widget,
            Div(
                text="<div style='border-left: 2px solid #e0e0e0; border-right: 2px solid #e0e0e0; background-color: #f9f9f9; padding: 10px 0;'></div>",
                width=260,
                height=10,
                margin=(0, 0, 0, 0)
            ),
            width=260,
            margin=(0, 0, 0, 0)
        ),
        # Bottom border
        Div(
            text="<div style='border: 2px solid #e0e0e0; border-top: none; border-radius: 0 0 5px 5px; background-color: #f9f9f9; padding: 10px 15px 15px 15px; margin-bottom: 10px;'></div>",
            width=260,
            height=35,
            margin=(0, 0, 0, 0)
        ),
        width=260,
        sizing_mode='fixed',
        margin=(0, 0, 10, 0)
    )

    return widget, container


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

