"""
Common styling functions for Bokeh visualizations.
"""

from bokeh.models import Title
from bokeh.plotting import figure
try:
    from .color_scheme import BG_COLOR, GRID_COLOR
except ImportError:
    from color_scheme import BG_COLOR, GRID_COLOR


def apply_common_style(fig, title, x_label, y_label):
    """
    Apply common styling to a Bokeh figure.

    Args:
        fig: Bokeh figure object
        title: Plot title
        x_label: X-axis label
        y_label: Y-axis label
    """
    fig.title = Title(text=title, text_font_size='14pt', text_font_style='bold')
    fig.xaxis.axis_label = x_label
    fig.yaxis.axis_label = y_label

    # Styling
    fig.background_fill_color = BG_COLOR
    fig.border_fill_color = BG_COLOR
    fig.grid.grid_line_color = GRID_COLOR
    fig.grid.grid_line_alpha = 0.3

    # Axis styling
    fig.xaxis.axis_label_text_font_size = '11pt'
    fig.yaxis.axis_label_text_font_size = '11pt'
    fig.xaxis.major_label_text_font_size = '10pt'
    fig.yaxis.major_label_text_font_size = '10pt'

    return fig


def create_figure(title, x_label, y_label, width=400, height=300, **kwargs):
    """
    Create a styled Bokeh figure.

    Args:
        title: Plot title
        x_label: X-axis label
        y_label: Y-axis label
        width: Figure width
        height: Figure height
        **kwargs: Additional arguments for figure()

    Returns:
        Styled Bokeh figure
    """
    fig = figure(width=width, height=height, **kwargs)
    return apply_common_style(fig, title, x_label, y_label)

