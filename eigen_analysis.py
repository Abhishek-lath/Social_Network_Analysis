
import numpy as np
import pandas as pd


def analyze_eigenvalues(users, adjacency):
    """Analyze eigenvalues and eigenvectors of a
    symmetric adjacency matrix."""
    if adjacency.size == 0:
        return np.array([]), np.empty((0, 0))

    # The adjacency matrix of an undirected graph is symmetric.
    values, vectors = np.linalg.eigh(adjacency)

    # Display eigenvalues from largest to smallest.
    order = np.argsort(values)[::-1]

    return values[order], vectors[:, order]


def calculate_centrality(users, adjacency):
    """Calculate eigenvector centrality from the
    principal eigenvector."""
    if len(users) == 0:
        return pd.DataFrame(
            columns=["User", "Centrality"]
        )

    values, vectors = np.linalg.eigh(adjacency)
    largest_index = np.argmax(values)

    # The principal eigenvector represents eigenvector centrality.
    scores = np.abs(vectors[:, largest_index])

    # Normalize scores so the maximum is 1.
    maximum = scores.max()
    if maximum > 0:
        scores = scores / maximum

    result = pd.DataFrame({
        "User": users,
        "Centrality": scores
    })

    return result.sort_values(
        "Centrality", ascending=False
    ).reset_index(drop=True)


def get_eigenvalue_table(values):
    """Format eigenvalues for display."""
    return pd.DataFrame({
        "Eigenvalue": [
            f"λ{i + 1}" for i in range(len(values))
        ],
        "Value": values
    })
