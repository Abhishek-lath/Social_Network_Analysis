
# Social Networks, Clustering, and Eigenvalue Problems

## Overview
This project models a social network using graph theory and
linear algebra. It analyzes connections, calculates eigenvalues
and eigenvectors, ranks influential users, and detects communities
using spectral clustering.

## Features
- Generate a sample social network
- Add and remove user connections
- Display the adjacency matrix, degree matrix, and graph Laplacian
- Calculate adjacency matrix eigenvalues and eigenvectors
- Rank users using eigenvector centrality
- Detect communities using spectral clustering
- Visualize the network and its communities
- Display graph Laplacian eigenvalues

## Technologies
- Python
- NumPy
- NetworkX
- Matplotlib
- scikit-learn
- Streamlit
- Pandas

## Setup on Windows
1. Install Python 3.10 or newer.
2. Open a terminal in the project folder.
3. Create a virtual environment:

   python -m venv .venv

4. Activate it:

   .venv\Scripts\activate

5. Install dependencies:

   python -m pip install -r requirements.txt

6. Start the dashboard:

   python -m streamlit run app.py

7. Open the local URL shown in the terminal.

## Mathematical concepts
- Graphs and adjacency matrices
- Eigenvalues and eigenvectors
- Eigenvector centrality
- Degree matrix
- Graph Laplacian: L = D - A
- Spectral clustering

## Data
The default network uses fictional users and synthetic
connections. No real personal data is required.
    