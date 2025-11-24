"""Vector extraction from Weaviate."""

import numpy as np
from typing import List, Dict, Optional, Tuple, Union
import weaviate


def _is_v4_client(client) -> bool:
    """Check if client is v4 WeaviateClient."""
    return hasattr(client, 'collections') and hasattr(client.collections, 'list_all')


class VectorExtractor:
    """Extracts vectors and metadata from Weaviate collections."""

    def __init__(self, client: Union[weaviate.Client, 'weaviate.WeaviateClient']):
        """
        Initialize vector extractor.

        Args:
            client: Connected Weaviate client instance (v3 or v4)
        """
        self.client = client
        self.is_v4 = _is_v4_client(client)

    def get_collections(self) -> List[str]:
        """
        Get list of available collections in Weaviate.

        Returns:
            List of collection names
        """
        if self.is_v4:
            # v4 API
            collections = self.client.collections.list_all()
            return [col.name for col in collections]
        else:
            # v3 API
            schema = self.client.schema.get()
            return [collection['class'] for collection in schema.get('classes', [])]

    def extract_vectors(
        self,
        collection_name: str,
        limit: Optional[int] = None,
        batch_size: int = 100
    ) -> Tuple[np.ndarray, List[Dict]]:
        """
        Extract all vectors from a Weaviate collection.

        Args:
            collection_name: Name of the collection to extract from
            limit: Maximum number of vectors to extract (None for all)
            batch_size: Number of vectors to fetch per batch

        Returns:
            Tuple of (vectors array, metadata list)
            - vectors: numpy array of shape (n_samples, n_features)
            - metadata: List of dictionaries containing chunk info
        """
        if self.is_v4:
            return self._extract_vectors_v4(collection_name, limit, batch_size)
        else:
            return self._extract_vectors_v3(collection_name, limit, batch_size)

    def _extract_vectors_v4(
        self,
        collection_name: str,
        limit: Optional[int] = None,
        batch_size: int = 100
    ) -> Tuple[np.ndarray, List[Dict]]:
        """Extract vectors using v4 API."""
        vectors = []
        metadata = []

        # Get collection
        collection = self.client.collections.get(collection_name)

        # Get total count using aggregation
        total_count = float('inf')  # Default to fetching all
        try:
            # Try v4 aggregation API
            result = collection.aggregate.over_all(total_count=True).do()
            if hasattr(result, 'total_count'):
                total_count = result.total_count
            elif isinstance(result, dict) and 'total_count' in result:
                total_count = result['total_count']
        except Exception as e:
            # If aggregation fails, we'll fetch until no more results
            print(f"Warning: Could not get total count: {e}. Will fetch until no more results.")

        if limit and total_count != float('inf'):
            total_count = min(total_count, limit)
        elif limit:
            total_count = limit

        # Get property names from collection config
        property_names = []
        try:
            config = collection.config.get()
            if hasattr(config, 'properties'):
                property_names = [prop.name for prop in config.properties]
            elif isinstance(config, dict) and 'properties' in config:
                property_names = [prop.get('name', prop) for prop in config['properties']]
        except Exception as e:
            print(f"Warning: Could not get property names from config: {e}")

        # Fallback to common field names if schema not available
        if not property_names:
            property_names = ["chunk", "content", "text"]

        # Fetch vectors in batches
        offset = 0
        fetched_count = 0

        while fetched_count < total_count:
            batch_limit = min(batch_size, total_count - fetched_count) if total_count != float('inf') else batch_size

            # Fetch objects with vectors
            try:
                # Try with include_vector parameter
                response = collection.query.fetch_objects(
                    limit=batch_limit,
                    offset=offset,
                    include_vector=True
                )
            except TypeError:
                # If include_vector is not supported, try without it
                response = collection.query.fetch_objects(
                    limit=batch_limit,
                    offset=offset
                )
            except Exception as e:
                raise ValueError(f"Failed to fetch objects: {e}")

            # Handle different response structures
            objects = []
            if hasattr(response, 'objects'):
                objects = response.objects
            elif isinstance(response, list):
                objects = response
            elif isinstance(response, dict) and 'objects' in response:
                objects = response['objects']
            else:
                # Try to get objects from response directly
                objects = response if response else []

            if not objects:
                break

            for obj in objects:
                # Get vector - handle different object structures
                vector = None
                if hasattr(obj, 'vector'):
                    vector = obj.vector
                elif isinstance(obj, dict):
                    if 'vector' in obj:
                        vector = obj['vector']
                    elif '_additional' in obj and 'vector' in obj['_additional']:
                        vector = obj['_additional']['vector']

                # Handle vector format (could be dict with 'default' key or direct list)
                if vector:
                    if isinstance(vector, dict):
                        vector = vector.get('default', list(vector.values())[0] if vector else None)

                    if vector:
                        vectors.append(vector)

                        # Extract metadata - get first available text property
                        chunk_text = ''
                        properties = {}

                        if hasattr(obj, 'properties'):
                            properties = obj.properties
                        elif isinstance(obj, dict):
                            properties = {k: v for k, v in obj.items() if k not in ['_additional', 'vector']}

                        for prop_name in property_names:
                            if prop_name in properties and properties[prop_name]:
                                chunk_text = str(properties[prop_name])
                                break

                        # Get ID
                        obj_id = ''
                        if hasattr(obj, 'uuid'):
                            obj_id = str(obj.uuid)
                        elif isinstance(obj, dict):
                            obj_id = obj.get('id', obj.get('_additional', {}).get('id', ''))

                        meta = {
                            'chunk': chunk_text,
                            'id': obj_id,
                        }
                        metadata.append(meta)

            fetched_count += len(objects)
            offset += batch_limit

            if len(objects) < batch_limit:
                break

        if not vectors:
            raise ValueError(f"No vectors found in collection '{collection_name}'. "
                           f"Make sure the collection exists and contains vectors.")

        vectors_array = np.array(vectors)
        print(f"Extracted {len(vectors)} vectors of dimension {vectors_array.shape[1]} from '{collection_name}'")

        return vectors_array, metadata

    def _extract_vectors_v3(
        self,
        collection_name: str,
        limit: Optional[int] = None,
        batch_size: int = 100
    ) -> Tuple[np.ndarray, List[Dict]]:
        """Extract vectors using v3 API."""
        vectors = []
        metadata = []

        # Get total count
        result = self.client.query.aggregate(collection_name).with_meta_count().do()
        total_count = result.get('data', {}).get('Aggregate', {}).get(collection_name, [{}])[0].get('meta', {}).get('count', 0)

        print(f"Debug: Total count from aggregation: {total_count}")

        if limit:
            total_count = min(total_count, limit)

        # Get schema to determine available properties
        schema = self.client.schema.get()
        collection_schema = next(
            (c for c in schema.get('classes', []) if c['class'] == collection_name),
            None
        )

        # Get property names (common text fields)
        property_names = []
        if collection_schema:
            property_names = [prop['name'] for prop in collection_schema.get('properties', [])]

        # Fallback to common field names if schema not available
        if not property_names:
            property_names = ["chunk", "content", "text"]

        # Fetch vectors in batches
        offset = 0
        while offset < total_count:
            batch_limit = min(batch_size, total_count - offset)

            # Try to get vectors - use property_names if available, otherwise get all
            if property_names:
                query = (
                    self.client.query
                    .get(collection_name, property_names)
                    .with_additional(["vector"])
                    .with_limit(batch_limit)
                    .with_offset(offset)
                    .do()
                )
            else:
                # If no properties, just get the vector
                query = (
                    self.client.query
                    .get(collection_name)
                    .with_additional(["vector"])
                    .with_limit(batch_limit)
                    .with_offset(offset)
                    .do()
                )

            results = []
            if 'data' in query and 'Get' in query['data']:
                results = query['data']['Get'][collection_name]
                if offset == 0:
                    print(f"Debug: Query returned {len(results)} results")
                    if results:
                        print(f"Debug: First result keys: {list(results[0].keys())}")
            else:
                if offset == 0:
                    print(f"Debug: Query structure - top level keys: {list(query.keys())}")
                    if 'data' in query:
                        print(f"Debug: Query data keys: {list(query['data'].keys())}")

            # Process results
            for item in results:
                # Try different possible locations for vector data
                vector = None
                if '_additional' in item:
                    if 'vector' in item['_additional']:
                        vector = item['_additional']['vector']
                    elif offset == 0 and len(vectors) == 0:
                        # Debug: show what's in _additional
                        print(f"Debug: _additional keys: {list(item['_additional'].keys())}")
                        print(f"Debug: _additional content: {item['_additional']}")

                if 'additional' in item and not vector:
                    if 'vector' in item['additional']:
                        vector = item['additional']['vector']
                    elif offset == 0 and len(vectors) == 0:
                        print(f"Debug: additional keys: {list(item['additional'].keys())}")

                if vector:
                    vectors.append(vector)

                    # Extract metadata - get first available text property
                    chunk_text = ''
                    for prop_name in property_names:
                        if prop_name in item and item[prop_name]:
                            chunk_text = str(item[prop_name])
                            break

                    # Get ID from various possible locations
                    obj_id = ''
                    if '_additional' in item:
                        obj_id = item['_additional'].get('id', '')
                    elif 'additional' in item:
                        obj_id = item['additional'].get('id', '')

                    meta = {
                        'chunk': chunk_text,
                        'id': obj_id,
                    }
                    metadata.append(meta)
                else:
                    # Debug: print structure if vector not found (only for first item)
                    if offset == 0 and len(vectors) == 0:
                        print(f"Debug: Vector not found in first item. Item keys: {list(item.keys())}")
                        if '_additional' in item:
                            print(f"Debug: _additional type: {type(item['_additional'])}")
                            print(f"Debug: _additional content: {item['_additional']}")

            offset += batch_limit

            if len(results) < batch_limit:
                break

        if not vectors:
            raise ValueError(f"No vectors found in collection '{collection_name}'. "
                           f"Make sure the collection exists and contains vectors.")

        vectors_array = np.array(vectors)
        print(f"Extracted {len(vectors)} vectors of dimension {vectors_array.shape[1]} from '{collection_name}'")

        return vectors_array, metadata

