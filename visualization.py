
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def draw_network(graph, clusters=None, centrality=None):
    """Draw a network with colors based on community."""
    fig, ax = plt.subplots(figsize=(10, 6))

    if len(graph.nodes()) == 0:
        ax.text(0.5, 0.5, "No users in network",
                ha="center", va="center")
        ax.axis("off")
        return fig

    # Fixed seed makes the layout reproducible.
    pos = nx.spring_layout(graph, seed=42, k=0.9)

    if clusters:
        colors = [
            clusters.get(user, 0)
            for user in graph.nodes()
        ]
        nx.draw_networkx_nodes(
            graph, pos, node_color=colors,
            cmap=plt.cm.Set2, node_size=850,
            ax=ax
        )
    else:
        nx.draw_networkx_nodes(
            graph, pos, node_size=850, ax=ax
        )

    nx.draw_networkx_edges(
        graph, pos, width=1.6,
        edge_color="gray", ax=ax
    )

    nx.draw_networkx_labels(
        graph, pos,
        labels={
            user: user.replace("User ", "U")
            for user in graph.nodes()
        },
        font_size=9, ax=ax
    )

    ax.set_title("Social Network and Detected Communities")
    ax.axis("off")
    fig.tight_layout()

    return fig


def draw_eigenvalues(values, title="Adjacency Matrix Eigenvalues"):
    """Plot eigenvalues as a bar chart."""
    fig, ax = plt.subplots(figsize=(9, 4))

    if len(values) > 0:
        indices = np.arange(1, len(values) + 1)
        ax.bar(indices, values)
        ax.axhline(0, linewidth=0.8)
        ax.set_xlabel("Eigenvalue index")
        ax.set_ylabel("Eigenvalue")
        ax.set_xticks(indices)

    ax.set_title(title)
    fig.tight_layout()

    return fig
