"""PCA-based dimensionality reduction for embeddings."""

import numpy as np
from sklearn.decomposition import PCA
from typing import Tuple


class PCAReducer:
    """Reduces high-dimensional embeddings to 3D using PCA."""

    def __init__(self, n_components: int = 3):
        """
        Initialize PCA reducer.

        Args:
            n_components: Number of dimensions to reduce to (default: 3)
        """
        self.n_components = n_components
        self.pca = PCA(n_components=n_components)
        self.fitted = False

    def fit_transform(self, vectors: np.ndarray) -> np.ndarray:
        """
        Fit PCA and transform vectors to lower dimensions.

        Args:
            vectors: High-dimensional vectors of shape (n_samples, n_features)

        Returns:
            Reduced vectors of shape (n_samples, n_components)
        """
        if vectors.shape[1] < self.n_components:
            raise ValueError(
                f"Input dimension ({vectors.shape[1]}) must be >= "
                f"n_components ({self.n_components})"
            )

        reduced_vectors = self.pca.fit_transform(vectors)
        self.fitted = True

        # Print explained variance
        explained_variance = self.pca.explained_variance_ratio_
        total_variance = explained_variance.sum()
        print(f"PCA reduction: {vectors.shape[1]}D -> {self.n_components}D")
        print(f"Explained variance: {total_variance:.2%}")
        print(f"Per component: {explained_variance}")

        return reduced_vectors

    def transform(self, vectors: np.ndarray) -> np.ndarray:
        """
        Transform vectors using fitted PCA.

        Args:
            vectors: High-dimensional vectors to transform

        Returns:
            Reduced vectors
        """
        if not self.fitted:
            raise ValueError("PCA must be fitted before transform. Use fit_transform() first.")

        return self.pca.transform(vectors)

    def get_explained_variance_ratio(self) -> np.ndarray:
        """Get explained variance ratio for each component."""
        if not self.fitted:
            raise ValueError("PCA must be fitted first.")
        return self.pca.explained_variance_ratio_

