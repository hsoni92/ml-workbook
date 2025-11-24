"""Weaviate connection handler."""

import weaviate
from typing import Optional, Union
import sys


def _get_weaviate_version() -> int:
    """Detect Weaviate client version."""
    version_str = weaviate.__version__
    major_version = int(version_str.split('.')[0])
    return major_version


class WeaviateConnection:
    """Handles connection to Weaviate vector database."""

    def __init__(self, url: str, api_key: Optional[str] = None):
        """
        Initialize Weaviate connection.

        Args:
            url: Weaviate connection URL (e.g., 'http://localhost:8080')
            api_key: Optional API key for authentication
        """
        self.url = url
        self.api_key = api_key
        self.client = None
        self.client_version = _get_weaviate_version()
        self.is_v4 = self.client_version >= 4

    def connect(self) -> Union[weaviate.Client, 'weaviate.WeaviateClient']:
        """
        Establish connection to Weaviate.

        Returns:
            Connected Weaviate client instance (v3 or v4)
        """
        if self.is_v4:
            # Use v4 API
            try:
                # Check if it's a local connection
                if self.url in ["http://localhost:8080", "http://127.0.0.1:8080"]:
                    self.client = weaviate.connect_to_local()
                else:
                    # Remote connection with optional API key
                    auth_credentials = None
                    if self.api_key:
                        auth_credentials = weaviate.auth.AuthApiKey(api_key=self.api_key)

                    self.client = weaviate.connect_to_remote(
                        url=self.url,
                        auth_credentials=auth_credentials
                    )

                # Test connection
                if not self.client.is_ready():
                    raise ConnectionError(f"Failed to connect to Weaviate at {self.url}")
            except Exception as e:
                # If v4 connection fails (e.g., old Weaviate server), fall back to v3
                if "Weaviate version" in str(e) or "not supported" in str(e):
                    print(f"Warning: v4 client not compatible with server. Falling back to v3 API.")
                    self.is_v4 = False
                    return self._connect_v3()
                raise
        else:
            # Use v3 API
            return self._connect_v3()

        return self.client

    def _connect_v3(self):
        """Connect using v3 API."""
        auth_config = None
        if self.api_key:
            auth_config = weaviate.AuthApiKey(api_key=self.api_key)

        self.client = weaviate.Client(
            url=self.url,
            auth_client_secret=auth_config
        )

        # Test connection
        if not self.client.is_ready():
            raise ConnectionError(f"Failed to connect to Weaviate at {self.url}")

        return self.client

    def get_client(self) -> Union[weaviate.Client, 'weaviate.WeaviateClient']:
        """
        Get the Weaviate client instance.

        Returns:
            Weaviate client instance (v3 or v4)
        """
        if self.client is None:
            return self.connect()
        return self.client

    def is_connected(self) -> bool:
        """Check if connection is established."""
        return self.client is not None and self.client.is_ready()

