#Algorithm #Data-Structure 
# Spanning Trees
A spanning tree of a graph:
- Contains all the nodes of the graph.
- Contains a subset of the edges of the graph.
- Has no cycles.
- Is connected.

A Minimum Spanning Tree is a spanning tree such that the sum of the edge weights is the smallest it can possibly be.

# Minimum Spanning Tree: Prim's Algorithm
1. Start at any node.
2. Repeat |v|-1 times:
	1. Find the smallest weight-edge (u, v, c)
		1. Such that u is in our growing MST and v is not.
	2. Add the edge (u, v, c) to our growing MST.

# Minimum Spanning Tree: Kruskal's Algorithm
1. Repeat |E| times:
	1. Find the smallest-weight edge (u, v, c) such that adding it to our growing subgraph will not cause a cycle.
	2. Add the edge to our growing subgraph.

# MST Time Complexity
Both Prim's and Kruskal's Algorithm take $O(|E| \log|E|)$. 