"""
Main application module for orchestrating the dashboard pipeline.
"""
from pathlib import Path
import sys
import os

# Add parent directory to path for config import
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))

# Add src to path for imports
sys.path.insert(0, str(current_dir))

# Import config from parent directory
from config import Config

# Import from src package (relative imports)
from explore_data import DataExplorer
from data_loader import DataLoader
from select_constituencies import ConstituencySelector
from create_dataset import DatasetCreator
from data_processor import DataProcessor
from color_scheme import ColorScheme
from visualizations import VisualizationGenerator
from dashboard import DashboardBuilder
from interactivity import InteractivityManager
from bokeh.io import save, curdoc, output_notebook, show
from bokeh.resources import CDN
import json


class DashboardApplication:
    """Main application class for the voter turnout dashboard."""

    def __init__(self, config: Config = None):
        """
        Initialize with configuration.

        Args:
            config: Config instance (optional, will create default if not provided)
        """
        self.config = config or Config()
        self.data_loader = None
        self.dataset_creator = None
        self.data_processor = None
        self.visualization_generator = None
        self.dashboard_builder = None
        self.interactivity_manager = None

    def run_pipeline(self):
        """
        Orchestrate the entire pipeline:
        1. Load and process data
        2. Create visualizations
        3. Build interactive dashboard
        4. Save as HTML file
        """
        print("=" * 80)
        print("VOTER TURNOUT DASHBOARD - PIPELINE EXECUTION")
        print("=" * 80)

        # Step 1: Explore data
        print("\n[Step 1] Exploring data structure...")
        file_paths = self.config.get_file_paths()
        explorer = DataExplorer(file_paths)
        explorer.load_sample()
        explorer.examine_structure()
        explorer.check_data_quality()

        # Step 2: Load and clean data
        print("\n[Step 2] Loading and cleaning data...")
        self.data_loader = DataLoader(file_paths)
        loaded_data = self.data_loader.load_all_years()

        if not loaded_data:
            print("Error: Failed to load data")
            return

        # Step 3: Select constituencies
        print("\n[Step 3] Selecting constituencies...")
        selector = ConstituencySelector(loaded_data)
        selector.find_common_constituencies()
        selector.analyze_geographic_distribution()
        selected = selector.select_diverse_constituencies(n=self.config.num_constituencies)
        selector.validate_selection()

        if not selected:
            print("Error: Failed to select constituencies")
            return

        # Step 4: Create consolidated dataset
        print("\n[Step 4] Creating consolidated dataset...")
        self.dataset_creator = DatasetCreator(loaded_data, selected)
        self.dataset_creator.filter_by_constituencies()
        self.dataset_creator.merge_data()
        self.dataset_creator.add_year_column()
        self.dataset_creator.calculate_aggregates()
        self.dataset_creator.validate_dataset()

        # Export dataset
        output_paths = self.config.get_output_paths()
        self.dataset_creator.export_to_csv(output_paths['dataset'])

        # Step 5: Process data for visualizations
        print("\n[Step 5] Processing data for visualizations...")
        dataset = self.dataset_creator.get_dataset()
        self.data_processor = DataProcessor(dataset)
        self.data_processor.prepare_time_series_data()
        self.data_processor.prepare_gender_comparison_data()
        self.data_processor.prepare_constituency_time_data()
        self.data_processor.prepare_constituency_gender_data()

        # Step 6: Create visualizations
        print("\n[Step 6] Creating visualizations...")
        viz_settings = self.config.get_visualization_settings()
        color_scheme = ColorScheme(viz_settings.get('color_scheme', 'colorblind_safe'))
        self.visualization_generator = VisualizationGenerator(self.data_processor, color_scheme)
        self.visualization_generator.get_all_plots()

        # Step 7: Build dashboard
        print("\n[Step 7] Building dashboard...")
        self.dashboard_builder = DashboardBuilder(self.visualization_generator, self.data_processor)
        dashboard_layout = self.dashboard_builder.build()

        # Step 8: Add interactivity
        print("\n[Step 8] Adding interactive features...")
        self.interactivity_manager = InteractivityManager(self.dashboard_builder, self.data_processor)
        interactivity = self.interactivity_manager.apply_interactivity()

        # Step 9: Export dashboard
        print("\n[Step 9] Exporting dashboard...")
        self.export_notebook(output_paths['notebook'])

        print("\n" + "=" * 80)
        print("PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 80)
        print(f"Dataset exported to: {output_paths['dataset']}")
        print(f"Dashboard exported to: {output_paths['notebook']}")

    def export_html(self, filepath: Path):
        """
        Export dashboard as HTML file.

        Args:
            filepath: Path to save HTML file
        """
        try:
            if self.dashboard_builder is None:
                print("Error: Dashboard not built yet")
                return

            # Ensure output directory exists
            filepath.parent.mkdir(parents=True, exist_ok=True)

            # Get dashboard layout
            dashboard_layout = self.dashboard_builder.build()

            # Save to HTML
            save(dashboard_layout, filepath, title="Voter Turnout Dashboard", resources=CDN)

            print(f"Dashboard exported to {filepath}")

        except Exception as e:
            print(f"Error exporting dashboard: {e}")
            import traceback
            traceback.print_exc()

    def export_notebook(self, filepath: Path):
        """
        Export visualizations as Jupyter notebook.

        Args:
            filepath: Path to save notebook file
        """
        try:
            if self.visualization_generator is None:
                print("Error: Visualizations not generated yet")
                return

            # Ensure output directory exists
            filepath.parent.mkdir(parents=True, exist_ok=True)

            # Get all plots
            plots = self.visualization_generator.get_all_plots()

            if not plots:
                print("Error: No plots available")
                return

            # Create notebook structure
            notebook = {
                "cells": [],
                "metadata": {
                    "kernelspec": {
                        "display_name": "Python 3",
                        "language": "python",
                        "name": "python3"
                    },
                    "language_info": {
                        "name": "python",
                        "version": "3.13.0"
                    }
                },
                "nbformat": 4,
                "nbformat_minor": 4
            }

            # Cell 1: Title and description (Markdown)
            title_cell = {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Voter Turnout Dashboard\n",
                    "\n",
                    "## Analysis of Voter Turnout Changes Across Selected Constituencies\n",
                    "\n",
                    "**General Elections: 2014, 2019, 2024**\n",
                    "\n",
                    "This notebook contains interactive visualizations analyzing voter turnout patterns across different constituencies, years, and demographics."
                ]
            }
            notebook["cells"].append(title_cell)

            # Cell 2: Imports and setup
            imports_code = """# Import required libraries
import sys
from pathlib import Path
import pandas as pd

# Add src directory to path
current_dir = Path().absolute()
src_dir = current_dir / 'src'
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.layouts import row, column

# Configure Bokeh to output in notebook
output_notebook()"""

            imports_cell = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": imports_code.split('\n')
            }
            notebook["cells"].append(imports_cell)

            # Cell 3: Load dataset
            load_data_code = """# Load the processed dataset
dataset_path = Path('output') / 'voter_turnout_dataset.csv'
if dataset_path.exists():
    dataset = pd.read_csv(dataset_path)
    print(f"✓ Loaded dataset with {len(dataset)} rows and {len(dataset.columns)} columns")
else:
    print("⚠ Warning: Dataset file not found at:", dataset_path)
    print("Please run 'python src/main.py' first to generate the dataset.")"""

            load_cell = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": load_data_code.split('\n')
            }
            notebook["cells"].append(load_cell)

            # Cell 4: Setup visualization generator
            setup_code = """# Setup visualization components
from data_processor import DataProcessor
from color_scheme import ColorScheme
from visualizations import VisualizationGenerator

# Initialize components
if 'dataset' in locals() and not dataset.empty:
    data_processor = DataProcessor(dataset)
    data_processor.prepare_time_series_data()
    data_processor.prepare_gender_comparison_data()
    data_processor.prepare_constituency_time_data()
    data_processor.prepare_constituency_gender_data()

    color_scheme = ColorScheme('colorblind_safe')
    viz_generator = VisualizationGenerator(data_processor, color_scheme)
    plots = viz_generator.get_all_plots()
    print("✓ Visualizations generated successfully")
    print(f"  Available plots: {', '.join(plots.keys())}")
else:
    print("⚠ Dataset not loaded. Please run the previous cell first.")"""

            setup_cell = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": setup_code.split('\n')
            }
            notebook["cells"].append(setup_cell)

            # Add cells for each visualization
            plot_titles = {
                'time_series': '## 1. Voter Turnout Over Time (Aggregate)',
                'gender_comparison': '## 2. Voter Turnout by Gender Over Time',
                'constituency_time': '## 3. Voter Turnout Distribution: Constituencies Across Time',
                'constituency_gender': '## 4. Voter Turnout Distribution: Constituencies by Gender'
            }

            plot_order = ['time_series', 'gender_comparison', 'constituency_time', 'constituency_gender']

            for plot_key in plot_order:
                if plot_key not in plots:
                    continue

                # Add markdown cell for plot title
                title_md = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [plot_titles.get(plot_key, f"## {plot_key}")]
                }
                notebook["cells"].append(title_md)

                # Add code cell to display the plot
                plot_code = f"""# Display {plot_key.replace('_', ' ').title()} visualization
if 'plots' in locals() and '{plot_key}' in plots:
    show(plots['{plot_key}'])
else:
    print("⚠ Plot not available. Please run the setup cells above first.")"""

                plot_cell = {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": plot_code.split('\n')
                }
                notebook["cells"].append(plot_cell)

            # Add a final markdown cell with notes
            notes_cell = {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "---\n",
                    "\n",
                    "## Notes\n",
                    "\n",
                    "- All visualizations are interactive. Use the toolbar tools to zoom, pan, and explore the data.\n",
                    "- Hover over data points to see detailed information.\n",
                    "- The dataset used for these visualizations is available in `output/voter_turnout_dataset.csv`."
                ]
            }
            notebook["cells"].append(notes_cell)

            # Write notebook to file
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, indent=2, ensure_ascii=False)

            print(f"Notebook exported to {filepath}")

        except Exception as e:
            print(f"Error exporting notebook: {e}")
            import traceback
            traceback.print_exc()


def main():
    """Main entry point for the application."""
    config = Config()
    app = DashboardApplication(config)
    app.run_pipeline()


if __name__ == "__main__":
    main()


