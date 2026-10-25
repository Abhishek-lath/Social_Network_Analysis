
import numpy as np
import networkx as nx
from sklearn.cluster import SpectralClustering


def calculate_laplacian(adjacency):
    """Calculate L = D - A."""
    degrees = np.sum(adjacency, axis=1)
    degree_matrix = np.diag(degrees)
    laplacian = degree_matrix - adjacency

    return degree_matrix, laplacian


def perform_spectral_clustering(
    users, adjacency, number_of_clusters=3
):
    """Assign every user to a spectral cluster."""
    n = len(users)

    if n == 0:
        return {}

    k = max(1, min(int(number_of_clusters), n))

    if k == 1:
        return {user: 0 for user in users}

    # If there are no edges, there is no community
    # structure to infer from the graph.
    if adjacency.sum() == 0:
        return {user: 0 for user in users}

    model = SpectralClustering(
        n_clusters=k,
        affinity="precomputed",
        assign_labels="kmeans",
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(adjacency)

    return {
        user: int(label)
        for user, label in zip(users, labels)
    }


def get_laplacian_eigenvalues(laplacian):
    """Return sorted eigenvalues of the graph Laplacian."""
    if laplacian.size == 0:
        return np.array([])

    return np.linalg.eigvalsh(laplacian)
