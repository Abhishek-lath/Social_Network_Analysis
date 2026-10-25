
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from network import (
    create_sample_network,
    get_adjacency_matrix,
    get_network_stats,
    get_edges_dataframe,
)
from eigen_analysis import (
    analyze_eigenvalues,
    calculate_centrality,
    get_eigenvalue_table,
)
from clustering import (
    calculate_laplacian,
    perform_spectral_clustering,
    get_laplacian_eigenvalues,
)
from visualization import draw_network, draw_eigenvalues


st.set_page_config(
    page_title="Social Network Analyzer",
    page_icon="🔗",
    layout="wide"
)

st.title("Social Networks, Clustering, and Eigenvalue Problems")
st.caption(
    "A mathematical social network simulator using graph theory "
    "and linear algebra."
)

# Keep the network in session state between interactions.
if "graph" not in st.session_state:
    st.session_state.graph = create_sample_network()

graph = st.session_state.graph

st.sidebar.header("Network Controls")

if st.sidebar.button("Reset Sample Network"):
    st.session_state.graph = create_sample_network()
    st.rerun()

st.sidebar.subheader("Add a connection")

users_now = sorted(graph.nodes())

if len(users_now) >= 2:
    with st.sidebar.form("add_edge_form"):
        user_a = st.selectbox(
            "First user", users_now, key="add_a"
        )
        user_b = st.selectbox(
            "Second user", users_now, key="add_b"
        )
        add_submitted = st.form_submit_button(
            "Add Connection"
        )

    if add_submitted:
        if user_a == user_b:
            st.sidebar.error("Choose two different users.")
        elif graph.has_edge(user_a, user_b):
            st.sidebar.warning("Connection already exists.")
        else:
            graph.add_edge(user_a, user_b)
            st.session_state.graph = graph
            st.rerun()

st.sidebar.subheader("Remove a connection")

edges_now = sorted(
    (min(a, b), max(a, b)) for a, b in graph.edges()
)

if edges_now:
    edge_options = [
        f"{a} — {b}" for a, b in edges_now
    ]

    with st.sidebar.form("remove_edge_form"):
        chosen_edge = st.selectbox(
            "Connection", edge_options
        )
        remove_submitted = st.form_submit_button(
            "Remove Connection"
        )

    if remove_submitted:
        a, b = chosen_edge.split(" — ", 1)
        graph.remove_edge(a, b)
        st.session_state.graph = graph
        st.rerun()
else:
    st.sidebar.info("There are no connections to remove.")

st.sidebar.subheader("Community settings")
number_of_clusters = st.sidebar.slider(
    "Number of clusters",
    min_value=1,
    max_value=max(1, min(6, graph.number_of_nodes())),
    value=min(3, max(1, graph.number_of_nodes()))
)

# Build the matrices in a consistent node order.
users, adjacency = get_adjacency_matrix(graph)
stats = get_network_stats(graph)

# Calculate all analyses.
eigenvalues, eigenvectors = analyze_eigenvalues(
    users, adjacency
)

centrality = calculate_centrality(users, adjacency)

degree_matrix, laplacian = calculate_laplacian(
    adjacency
)

clusters = perform_spectral_clustering(
    users, adjacency, number_of_clusters
)

laplacian_values = get_laplacian_eigenvalues(laplacian)

# Overview cards.
c1, c2, c3, c4 = st.columns(4)
c1.metric("Users", stats["users"])
c2.metric("Connections", stats["connections"])
c3.metric("Network Density", f'{stats["density"]:.3f}')
c4.metric("Connected Components", stats["components"])

st.divider()

# Main network graph.
st.subheader("1. Social Network Visualization")
st.write(
    "Each node is a user, each edge is a connection, "
    "and node colors represent the detected clusters."
)

fig = draw_network(graph, clusters, centrality)
st.pyplot(fig)
plt.close(fig)

# Matrix displays.
st.subheader("2. Adjacency Matrix")
st.write(
    "A value of 1 indicates a connection; 0 indicates no connection."
)
st.dataframe(
    pd.DataFrame(adjacency, index=users, columns=users),
    use_container_width=True
)

with st.expander("View degree matrix D"):
    st.dataframe(
        pd.DataFrame(
            degree_matrix, index=users, columns=users
        ),
        use_container_width=True
    )

with st.expander("View graph Laplacian L = D - A"):
    st.dataframe(
        pd.DataFrame(
            laplacian, index=users, columns=users
        ),
        use_container_width=True
    )

# Eigenvalue analysis.
st.subheader("3. Eigenvalue and Eigenvector Analysis")

left, right = st.columns(2)

with left:
    st.write("Adjacency matrix eigenvalues")
    st.dataframe(
        get_eigenvalue_table(eigenvalues),
        use_container_width=True
    )

with right:
    fig2 = draw_eigenvalues(eigenvalues)
    st.pyplot(fig2)
    plt.close(fig2)

st.latex(r"Av = \lambda v")

st.write(
    "The equation above defines an eigenvalue and eigenvector. "
    "The displayed values are calculated from the current adjacency matrix."
)

# Centrality ranking.
st.subheader("4. Most Influential Users")
st.write(
    "Eigenvector centrality rewards users connected to other "
    "well-connected users. Scores are normalized to a maximum of 1."
)

st.dataframe(
    centrality.style.format({"Centrality": "{:.4f}"}),
    use_container_width=True
)

if not centrality.empty:
    top_user = centrality.iloc[0]
    st.success(
        f"Highest eigenvector centrality: {top_user['User']} "
        f"({top_user['Centrality']:.4f})"
    )

# Clustering results.
st.subheader("5. Community Detection")

community_table = pd.DataFrame({
    "User": users,
    "Cluster": [
        f"Cluster {clusters[user] + 1}"
        for user in users
    ]
})

st.dataframe(
    community_table,
    use_container_width=True
)

st.write("Graph Laplacian eigenvalues")
st.dataframe(
    pd.DataFrame({
        "Index": range(1, len(laplacian_values) + 1),
        "Eigenvalue": laplacian_values
    }).style.format({"Eigenvalue": "{:.4f}"}),
    use_container_width=True
)

st.info(
    "For an undirected graph, the number of zero eigenvalues "
    "of the graph Laplacian equals the number of connected "
    "components. Spectral clustering can also reveal communities "
    "inside a connected graph."
)

# Raw edge list.
with st.expander("View all network connections"):
    st.dataframe(
        get_edges_dataframe(graph),
        use_container_width=True
    )

st.divider()
st.caption(
    "Mini-project: Social Networks, Clustering, and Eigenvalue Problems"
)
