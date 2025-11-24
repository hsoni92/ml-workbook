"""Example usage of the embedding visualization pipeline."""

from main import EmbeddingVisualizationPipeline
from weaviate_connector import WeaviateConnection
from vector_extractor import VectorExtractor

# Example 1: Simple usage with just URL and collection name
if __name__ == "__main__":
    # Replace with your Weaviate URL
    weaviate_url = "http://localhost:8080"

    # Optional: API key if needed
    api_key = None  # or "your-api-key-here"

    # Create pipeline
    pipeline = EmbeddingVisualizationPipeline(
        weaviate_url=weaviate_url,
        api_key=api_key
    )

    # Connect to Weaviate and get all collections
    print("Fetching available collections...")
    connector = WeaviateConnection(weaviate_url, api_key)
    client = connector.connect()
    extractor = VectorExtractor(client)
    collections = extractor.get_collections()

    if not collections:
        print("No collections found in Weaviate. Please create a collection first.")
        exit(1)

    # Pick the first collection by default
    collection_name = collections[0]
    print(f"Found {len(collections)} collection(s): {collections}")
    print(f"Using first collection: '{collection_name}'")

    # Run visualization
    pipeline.run(
        collection_name=collection_name,
        limit=None,  # Set to a number to limit vectors, or None for all
        output_file="embedding_visualization.html",  # Optional: save to file
        show_plot=True,  # Display in browser
        use_3d=True  # Set to True for true 3D Plotly visualization, False for Bokeh 2D projections
    )

