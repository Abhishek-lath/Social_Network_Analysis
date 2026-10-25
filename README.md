# Social Networks, Clustering, and Eigenvalue Problems

## 📌 Project Overview

This project analyzes social networks using graph theory, linear algebra, and clustering algorithms. It represents users and their connections as a graph, identifies influential users using eigenvector centrality, and discovers communities using spectral clustering.

The project includes an interactive dashboard that visualizes the network and displays mathematical analysis results.

## 🎯 Objectives

- Represent a social network using graph theory.
- Construct and analyze an adjacency matrix.
- Calculate eigenvalues and eigenvectors.
- Identify influential users using eigenvector centrality.
- Construct the degree matrix and graph Laplacian.
- Detect communities using spectral clustering.
- Visualize network connections and detected communities.
- Observe how changes in connections affect network analysis.

## ✨ Features

- **Social Network Visualization:** Display users as nodes and friendships as edges.
- **Interactive Connections:** Add or remove connections between users.
- **Adjacency Matrix:** Display the numerical representation of the network.
- **Eigenvalue Analysis:** Calculate and visualize adjacency matrix eigenvalues.
- **Influential User Ranking:** Rank users using eigenvector centrality.
- **Community Detection:** Group users using spectral clustering.
- **Graph Laplacian:** Calculate and display the degree matrix and graph Laplacian.
- **Interactive Dashboard:** Explore results through a Streamlit web application.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Matrix operations and eigenvalue calculations |
| NetworkX | Graph creation and network analysis |
| scikit-learn | Spectral clustering |
| Matplotlib | Graph and chart visualization |
| Streamlit | Interactive web dashboard |
| Pandas | Tabular data representation |

## 📂 Project Structure

```text
Social_Network_Analysis/
│
├── app.py
├── network.py
├── eigen_analysis.py
├── clustering.py
├── visualization.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🧮 Mathematical Concepts

### 1. Graph Representation

Users are represented as vertices, and friendships are represented as edges in an undirected graph.

### 2. Adjacency Matrix

The adjacency matrix represents the connections between users.

A value of `1` indicates a connection, while `0` indicates no connection.

### 3. Eigenvalues and Eigenvectors

Eigenvalues and eigenvectors are calculated using:

**Av = λv**

These are used to analyze the mathematical structure of the network.

### 4. Eigenvector Centrality

Eigenvector centrality estimates a user's structural importance based on the importance of their connected users.

### 5. Graph Laplacian

The graph Laplacian is calculated using:

**L = D − A**

Where:
- `L` is the graph Laplacian.
- `D` is the degree matrix.
- `A` is the adjacency matrix.

### 6. Spectral Clustering

Spectral clustering uses eigenvector-based representations of the network to identify groups of closely connected users.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or newer
- Git
- Visual Studio Code or another Python editor (optional)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Abhishek-lath/Social_Network_Analysis
cd Social_Network_Analysis
```

### Step 2: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python -m streamlit run app.py
```

### Step 4: Open the Dashboard

Streamlit will display a local URL in the terminal, usually:

```text
http://localhost:8501
```

Open this URL in your browser to use the application.

## 🚀 How to Use

1. Launch the application.
2. Explore the generated social network.
3. View the adjacency matrix and network statistics.
4. Examine eigenvalues and eigenvector centrality rankings.
5. Change the requested number of clusters.
6. Add or remove connections using the sidebar.
7. Observe how the network, matrices, centrality scores, and clusters change.
8. Reset the sample network to restore the original configuration.

## 📊 Expected Results

The application provides:

- A visual representation of the social network.
- Adjacency, degree, and graph Laplacian matrices.
- Eigenvalues of the adjacency matrix and graph Laplacian.
- A ranking of users based on eigenvector centrality.
- Community assignments from spectral clustering.
- Visualizations of network structure and eigenvalues.

The default network uses fictional users and synthetic connections.

## 🔮 Future Enhancements

- Upload custom social network datasets.
- Support directed and weighted networks.
- Compare different centrality measures.
- Evaluate community quality using clustering metrics.
- Export analysis results and visualizations.
- Explore larger social networks.

## 👨‍💻 Conclusion

This project demonstrates how graph theory, matrix operations, eigenvalues, eigenvectors, and spectral clustering can be applied to social network analysis. The interactive dashboard makes the mathematical results easier to explore and understand.

---

**Project Title:** Social Networks, Clustering, and Eigenvalue Problems  
**Domain:** Mathematical Foundations, Linear Algebra, and Graph Theory
