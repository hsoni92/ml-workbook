"""Main script for visualizing Weaviate embeddings."""

import argparse
import sys
from weaviate_connector import WeaviateConnection
from vector_extractor import VectorExtractor
from pca_reducer import PCAReducer
from visualizer import EmbeddingVisualizer


class EmbeddingVisualizationPipeline:
    """Complete pipeline for visualizing Weaviate embeddings."""

    def __init__(self, weaviate_url: str, api_key: str = None):
        """
        Initialize the visualization pipeline.

        Args:
            weaviate_url: Weaviate connection URL
            api_key: Optional API key for authentication
        """
        self.connector = WeaviateConnection(weaviate_url, api_key)
        self.extractor = None
        self.reducer = PCAReducer(n_components=3)
        self.visualizer = None

    def run(
        self,
        collection_name: str,
        limit: int = None,
        output_file: str = None,
        show_plot: bool = True,
        use_3d: bool = False
    ):
        """
        Run the complete visualization pipeline.

        Args:
            collection_name: Name of the Weaviate collection to visualize
            limit: Maximum number of vectors to extract (None for all)
            output_file: Optional HTML file to save visualization
            show_plot: Whether to display the plot in browser
            use_3d: If True, use Plotly for true 3D visualization (requires plotly).
                    If False, use Bokeh with 2D projections (default)
        """
        print("=" * 60)
        print("Weaviate Embedding Visualization Pipeline")
        print("=" * 60)

        # Step 1: Connect to Weaviate
        print("\n[1/4] Connecting to Weaviate...")
        client = self.connector.connect()
        print(f"✓ Connected to {self.connector.url}")

        # Step 2: Extract vectors
        print(f"\n[2/4] Extracting vectors from collection '{collection_name}'...")
        self.extractor = VectorExtractor(client)

        # List available collections if needed
        available_collections = self.extractor.get_collections()
        if collection_name not in available_collections:
            print(f"\n⚠ Warning: Collection '{collection_name}' not found.")
            print(f"Available collections: {available_collections}")
            response = input(f"\nContinue anyway? (y/n): ")
            if response.lower() != 'y':
                print("Aborted.")
                return

        vectors, metadata = self.extractor.extract_vectors(collection_name, limit=limit)
        print(f"✓ Extracted {len(vectors)} vectors")

        # Step 3: Reduce dimensions with PCA
        print(f"\n[3/4] Reducing dimensions with PCA...")
        reduced_vectors = self.reducer.fit_transform(vectors)
        print(f"✓ Reduced to 3D")

        # Step 4: Visualize
        print(f"\n[4/4] Creating visualization...")
        self.visualizer = EmbeddingVisualizer(reduced_vectors, metadata)

        title = f"Embeddings from '{collection_name}'"

        if use_3d:
            # Use Plotly for true 3D visualization
            if output_file:
                self.visualizer.save_3d(output_file, title)
                print(f"✓ Saved 3D visualization to {output_file}")

            if show_plot:
                print("✓ Opening 3D visualization in browser...")
                self.visualizer.show_3d(title)
        else:
            # Use Bokeh with 2D projections
            if output_file:
                self.visualizer.save(output_file, title)
                print(f"✓ Saved to {output_file}")

            if show_plot:
                print("✓ Opening visualization in browser...")
                self.visualizer.show(title)

        print("\n" + "=" * 60)
        print("Pipeline completed successfully!")
        print("=" * 60)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Visualize Weaviate embeddings using PCA and Bokeh"
    )
    parser.add_argument(
        '--url',
        type=str,
        required=True,
        help='Weaviate connection URL (e.g., http://localhost:8080)'
    )
    parser.add_argument(
        '--collection',
        type=str,
        required=True,
        help='Name of the Weaviate collection to visualize'
    )
    parser.add_argument(
        '--api-key',
        type=str,
        default=None,
        help='Optional API key for Weaviate authentication'
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=None,
        help='Maximum number of vectors to extract (default: all)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='Output HTML file path (default: show in browser only)'
    )
    parser.add_argument(
        '--no-show',
        action='store_true',
        help='Do not open visualization in browser (useful when saving to file)'
    )

    args = parser.parse_args()

    try:
        pipeline = EmbeddingVisualizationPipeline(args.url, api_key=args.api_key)
        pipeline.run(
            collection_name=args.collection,
            limit=args.limit,
            output_file=args.output,
            show_plot=not args.no_show
        )
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

