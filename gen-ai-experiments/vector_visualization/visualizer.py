"""Bokeh-based visualization for reduced embeddings."""

import numpy as np
from bokeh.plotting import figure, show, output_file, save
from bokeh.layouts import row, column
from bokeh.models import HoverTool, ColumnDataSource, Div
from bokeh.io import curdoc
from typing import List, Dict, Optional
import os

try:
    import plotly.graph_objects as go
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False


class EmbeddingVisualizer:
    """Creates interactive Bokeh visualizations for 3D embeddings."""

    def __init__(self, reduced_vectors: np.ndarray, metadata: List[Dict]):
        """
        Initialize visualizer.

        Args:
            reduced_vectors: 3D vectors of shape (n_samples, 3)
            metadata: List of metadata dictionaries for each vector
        """
        if reduced_vectors.shape[1] != 3:
            raise ValueError("reduced_vectors must have 3 dimensions for visualization")

        self.reduced_vectors = reduced_vectors
        self.metadata = metadata

    def _prepare_data_source(self):
        """Prepare a fresh ColumnDataSource for Bokeh plotting."""
        # Extract chunk text (truncate for display)
        chunks = []
        for meta in self.metadata:
            chunk_text = str(meta.get('chunk', ''))[:100]  # Truncate to 100 chars
            chunks.append(chunk_text)

        # Create a fresh ColumnDataSource each time to avoid document conflicts
        return ColumnDataSource(data={
            'x': self.reduced_vectors[:, 0],
            'y': self.reduced_vectors[:, 1],
            'z': self.reduced_vectors[:, 2],
            'chunk': chunks,
            'index': list(range(len(self.reduced_vectors)))
        })

    def create_plots(self, title: str = "Embedding Visualization") -> column:
        """
        Create interactive Bokeh plots showing 3D embeddings.

        Since Bokeh doesn't natively support 3D, we create three 2D projections:
        - XY plane
        - XZ plane
        - YZ plane

        Args:
            title: Title for the visualization

        Returns:
            Bokeh layout with all plots
        """
        # Create a fresh data source for this visualization
        source = self._prepare_data_source()

        # Define common tooltips
        tooltips = [
            ("Index", "@index"),
            ("Chunk", "@chunk"),
            ("X", "@x{0.00}"),
            ("Y", "@y{0.00}"),
            ("Z", "@z{0.00}")
        ]

        # XY Projection
        plot_xy = figure(
            width=500,
            height=500,
            title="XY Projection (PC1 vs PC2)",
            tools="pan,wheel_zoom,box_zoom,reset,save,hover",
            tooltips=tooltips
        )
        plot_xy.scatter('x', 'y', source=source, size=5, alpha=0.6, color='blue')
        plot_xy.xaxis.axis_label = "Principal Component 1"
        plot_xy.yaxis.axis_label = "Principal Component 2"

        # XZ Projection
        plot_xz = figure(
            width=500,
            height=500,
            title="XZ Projection (PC1 vs PC3)",
            tools="pan,wheel_zoom,box_zoom,reset,save,hover",
            tooltips=tooltips,
            x_range=plot_xy.x_range  # Share X axis range
        )
        plot_xz.scatter('x', 'z', source=source, size=5, alpha=0.6, color='green')
        plot_xz.xaxis.axis_label = "Principal Component 1"
        plot_xz.yaxis.axis_label = "Principal Component 3"

        # YZ Projection
        plot_yz = figure(
            width=500,
            height=500,
            title="YZ Projection (PC2 vs PC3)",
            tools="pan,wheel_zoom,box_zoom,reset,save,hover",
            tooltips=tooltips
        )
        plot_yz.scatter('y', 'z', source=source, size=5, alpha=0.6, color='red')
        plot_yz.xaxis.axis_label = "Principal Component 2"
        plot_yz.yaxis.axis_label = "Principal Component 3"

        # Create title div
        title_div = Div(
            text=f"<h2>{title}</h2><p>3D Embedding Visualization (PCA Reduced) - Three 2D Projections</p>",
            width=1500,
            height=50
        )

        # Layout: title on top, plots in a row
        layout = column(
            title_div,
            row(plot_xy, plot_xz, plot_yz)
        )

        return layout

    def show(self, title: str = "Embedding Visualization"):
        """
        Display the visualization in a browser.

        Args:
            title: Title for the visualization
        """
        layout = self.create_plots(title)
        show(layout)

    def save(self, filename: str, title: str = "Embedding Visualization"):
        """
        Save the visualization to an HTML file.

        Args:
            filename: Output HTML filename
            title: Title for the visualization
        """
        output_file(filename)
        layout = self.create_plots(title)
        save(layout)
        print(f"Visualization saved to {filename}")

    def create_3d_plot(self, title: str = "Embedding Visualization"):
        """
        Create a true 3D scatter plot using Plotly (if available).

        Args:
            title: Title for the visualization

        Returns:
            Plotly figure object
        """
        if not PLOTLY_AVAILABLE:
            raise ImportError(
                "Plotly is required for 3D visualization. "
                "Install it with: pip install plotly>=5.0.0"
            )

        # Extract chunk text for hover tooltips
        chunks = []
        for meta in self.metadata:
            chunk_text = str(meta.get('chunk', ''))[:200]  # Truncate to 200 chars
            chunks.append(chunk_text)

        # Create 3D scatter plot
        fig = go.Figure(data=go.Scatter3d(
            x=self.reduced_vectors[:, 0],
            y=self.reduced_vectors[:, 1],
            z=self.reduced_vectors[:, 2],
            mode='markers',
            marker=dict(
                size=5,
                color=self.reduced_vectors[:, 2],  # Color by Z value
                colorscale='Viridis',
                opacity=0.8,
                colorbar=dict(title="PC3")
            ),
            text=chunks,
            hovertemplate=(
                '<b>Index:</b> %{customdata[0]}<br>'
                '<b>PC1:</b> %{x:.2f}<br>'
                '<b>PC2:</b> %{y:.2f}<br>'
                '<b>PC3:</b> %{z:.2f}<br>'
                '<b>Chunk:</b> %{text}<br>'
                '<extra></extra>'
            ),
            customdata=list(range(len(self.reduced_vectors)))
        ))

        fig.update_layout(
            title=title,
            scene=dict(
                xaxis_title='Principal Component 1',
                yaxis_title='Principal Component 2',
                zaxis_title='Principal Component 3',
                camera=dict(
                    eye=dict(x=1.5, y=1.5, z=1.5)
                )
            ),
            width=1000,
            height=800
        )

        return fig

    def show_3d(self, title: str = "Embedding Visualization"):
        """
        Display a true 3D scatter plot in browser using Plotly.

        Args:
            title: Title for the visualization
        """
        fig = self.create_3d_plot(title)
        fig.show()

    def save_3d(self, filename: str, title: str = "Embedding Visualization"):
        """
        Save a true 3D scatter plot to HTML file using Plotly.

        Args:
            filename: Output HTML filename
            title: Title for the visualization
        """
        fig = self.create_3d_plot(title)
        fig.write_html(filename)
        print(f"3D visualization saved to {filename}")

