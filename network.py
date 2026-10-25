import numpy as np
import networkx as nx
import pandas as pd


def create_sample_network():
    """Create a reproducible example network."""
    graph = nx.Graph()

    users = [f"User {i}" for i in range(1, 13)]
    graph.add_nodes_from(users)

    groups = [
        users[0:4],
        users[4:8],
        users[8:12],
    ]

    # Connect users within each initial group.
    for group in groups:
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                graph.add_edge(group[i], group[j])

    # Add bridges between groups.
    graph.add_edges_from([
        ("User 4", "User 5"),
        ("User 8", "User 9"),
    ])

    return graph


def get_adjacency_matrix(graph):
    """Return adjacency matrix and consistent user ordering."""
    users = sorted(graph.nodes())
    matrix = nx.to_numpy_array(
        graph, nodelist=users, dtype=float
    )
    return users, matrix


def get_network_stats(graph):
    """Calculate basic graph statistics."""
    return {
        "users": graph.number_of_nodes(),
        "connections": graph.number_of_edges(),
        "density": nx.density(graph),
        "components": nx.number_connected_components(graph),
    }


def get_edges_dataframe(graph):
    """Return connections in a table."""
    edges = sorted(
        (min(a, b), max(a, b))
        for a, b in graph.edges()
    )
    return pd.DataFrame(edges, columns=["User 1", "User 2"])
