# Weaviate Embedding Visualization

A modular Python tool for visualizing high-dimensional embeddings from Weaviate using PCA reduction and Bokeh interactive plots.

## Overview

This tool helps you visualize embeddings stored in Weaviate by:
1. Extracting vectors from a Weaviate collection
2. Reducing dimensions from high-D (e.g., 768) to 3D using PCA
3. Creating interactive Bokeh visualizations with multiple 2D projections

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Command Line

```bash
python main.py --url http://localhost:8080 --collection YourCollectionName
```

**Options:**
- `--url`: Weaviate connection URL (required)
- `--collection`: Collection name to visualize (required)
- `--api-key`: Optional API key for authentication
- `--limit`: Maximum number of vectors to extract (default: all)
- `--output`: Save visualization to HTML file
- `--no-show`: Don't open browser (useful when saving to file)

**Examples:**

```bash
# Basic usage
python main.py --url http://localhost:8080 --collection Documents

# With API key
python main.py --url https://your-instance.weaviate.network --collection Documents --api-key YOUR_KEY

# Limit to 1000 vectors and save to file
python main.py --url http://localhost:8080 --collection Documents --limit 1000 --output visualization.html

# Save without opening browser
python main.py --url http://localhost:8080 --collection Documents --output viz.html --no-show
```

### Programmatic Usage

```python
from main import EmbeddingVisualizationPipeline

# Initialize pipeline
pipeline = EmbeddingVisualizationPipeline(
    weaviate_url="http://localhost:8080",
    api_key=None  # Optional
)

# Run visualization
pipeline.run(
    collection_name="YourCollectionName",
    limit=1000,  # Optional: limit number of vectors
    output_file="visualization.html",  # Optional: save to file
    show_plot=True  # Display in browser
)
```

### Using Individual Modules

```python
from weaviate_connector import WeaviateConnection
from vector_extractor import VectorExtractor
from pca_reducer import PCAReducer
from visualizer import EmbeddingVisualizer

# Connect to Weaviate
connector = WeaviateConnection("http://localhost:8080")
client = connector.connect()

# Extract vectors
extractor = VectorExtractor(client)
vectors, metadata = extractor.extract_vectors("YourCollectionName")

# Reduce dimensions
reducer = PCAReducer(n_components=3)
reduced_vectors = reducer.fit_transform(vectors)

# Visualize
visualizer = EmbeddingVisualizer(reduced_vectors, metadata)
visualizer.show()
```

## Module Structure

- **`weaviate_connector.py`**: Handles Weaviate connection and authentication
- **`vector_extractor.py`**: Extracts vectors and metadata from Weaviate collections
- **`pca_reducer.py`**: Applies PCA to reduce high-dimensional embeddings to 3D
- **`visualizer.py`**: Creates interactive Bokeh visualizations
- **`main.py`**: Complete pipeline and CLI interface

## Visualization Features

The visualization shows three 2D projections of the 3D reduced embeddings:
- **XY Projection**: Principal Component 1 vs Principal Component 2
- **XZ Projection**: Principal Component 1 vs Principal Component 3
- **YZ Projection**: Principal Component 2 vs Principal Component 3

Each plot is interactive with:
- Pan and zoom
- Hover tooltips showing chunk text and coordinates
- Linked axis ranges for easier comparison

## Notes

- Bokeh doesn't natively support 3D plots, so the visualization uses three 2D projections
- PCA reduction may not perfectly represent high-dimensional relationships, but provides useful insights
- The tool automatically handles batch extraction for large collections
- Explained variance ratio is printed to help assess how well 3D represents the original space

