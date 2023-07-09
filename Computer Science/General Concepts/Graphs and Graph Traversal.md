#Algorithm #Data-Structure 
# Graphs

^4382bb

**Graphs** are collections of **nodes** and **edges**.
- **Nodes (a.k.a. Vertices)** are single entities.
- **Edges** are relationships between a pair of nodes.

#### Directed vs. Undirected Graphs
- **Directed** graphs have **one-way** edges.
	- An edge $(u, v)$ is from $u$ to $v$, not $v$ to $u$.
- **Undirected** graphs have **two-way** edges.
	- So, an edge $(u, v)$ is from $u$ to $v$ *and* from $v$ to $u$.

#### Weighted vs. Unweighted Graphs
- A **weighted** graph has edges that have "weights" (or "costs") associated with each edge.
- An **unweighted** graph simply does not have these "weights" on its edges.

A **cycle** is a valid path starting and ending at the same node. ^69784f

#### Classes of Graphs
- "**Unconnected**" graphs have a *disconnected* collection of nodes.
	- Ex: A set
- "**Sequential**" graphs have an *ordered* collection of *connected* nodes.
	- Ex: A linked list
- "**Hierarchical**" graphs have a *ranked* collection of *connected* nodes.
	- Ex: A tree
- "**Structured**" graphs have a collection of both *connected and disconnected* nodes. ^14f34a

#### Multigraphs
Graphs in which a pair of nodes may have multiple distinct edges. Are uncommon, but have their uses.
# Graph Representation
How should we represent graphs in memory?
### Adjacency Matrices

^a0afa3

A square 2-D array which has rows and columns corresponding to the nodes in our graph.
- A row-column pair $(r,c)$ indicates that there is a directed edge from $r$ to $c$.
- Consider dense vs. sparse graphs; an adjacency matrix will make full use of its space if the original graph was dense, but will waste much of its space if the original graph was sparse.
- Note that lookup has constant speed, but the space complexity is $O(n^2)$.
### Adjacency Lists

^c8fe3b

For each node in the graph, we make a list structure to keep track of all of the outgoing edges.
- Note that lookup has linear speed, but the space complexity is more manageable (linear in terms of nodes and edges). This makes it good for sparse graphs.
- Also note that we can tell how many outgoing edges a node has faster with a list.

### Searching
- Both [[DFS and BFS]] are commonly used algorithms for graph searching.
- If the graph has weighted edges, [[Dijkstra's Algorithm]] is also appropriate.

