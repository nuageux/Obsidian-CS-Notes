#Algorithm 
- The two simplest [[Graph Search|graph search]] algorithms.
- Both have a worst case [[Time and Space Complexity|time complexity]] of $O(V+E)$, where $V$ is the number of vertices (nodes) and $E$ is the number of edges.
# DFS: Depth-First Search

^95b370

^e10739
- Searches by traversing all the way down a path before repeating for the next unsearched path (from the start node).
- Implemented with a [[Stacks and Queues|stack]]. The DFS algorithm is as follows:
```python
# nodes have edges/neighbors
visited = []
frontier = Stack()
frontier.push(START)
while not frontier.empty():
	curNode = frontier.pop()
	if curNode not in visited:
		visited.add(curNode)
		for n in curNode.neighbors:
			if n not in visited:
				frontier.push(n)
# to see which nodes in the resultant path:
return visited
```
- Observe that:
	- The array *visited* contains $X \cup F$ (eXplored and Frontier).
	- The outer loop runs at most $|V|$ times.
	- The inner loop takes $O(1+ deg(v))=O(|V|)$ (since a node could potentially be connected to all other nodes).
		- Putting the inner and outer loops together, the [[Time and Space Complexity|time complexity]] is $O(|V|^2)$, so that is the **loose** upper-bound.
			- It is a loose bound because most large graphs are *sparse*.
- The **tight** bound on time complexity is actually $O(\sum\limits^v(1 + deg(v)))=O(|V|+|E|)$ because in reality we only count all the edges twice (once, if they are directed edges).
	- i.e. $\sum\limits^{u\in V}(deg(u)) = 2|E|$

### Recursive DFS
- There is a short recursive variant of DFS:
```python
visited = [false for all nodes in graph]
def DFS_explore(graph, node):
	visited[node] = True
	for n in node.neighbors:
		if not visited[n]:
			DFS_explore(G, n)
DFS_explore(graph, start_node)
```
- Note that recursion implicitly uses a stack implementation and is therefore DFS.

## Usages of DFS
- There are many usages of DFS, especially if DFS is [[Algorithm Mining|augmented]] to keep track of additional variables. Some examples include:
	- Finding the connected components of an unconnected graph
		- Since DFS only costs the number of *reachable* nodes and *reachable* edges, unreachable nodes/edges cost nothing.
		- So we can divide an undirected graph into its connected components.
	- Ancestor-Descendant Relationships
		- We can add in `pre` and `post` arrays for our nodes to indicate the first time we encounter a node and the last time we leave it.
			- We add in a tracking variable in our arrays to indicate at which step of DFS the node was encountered (pre or post).
			- $u$ is below *v* in the DFS tree *iff* `pre[v]` < `pre[u]` < `post[u]` < `post[v]`.
	- Finding cycles
	- Finding sinks and sources in a [[Directed Acyclic Graphs (DAGs)|DAG]]
	- Topologically sorting a DAG
- DFS is **not** good for finding the shortest distance between vertices.

# BFS: Breadth-First Search

^2327c0

^e9e38a
- Searches by traversing one unit on all possible paths for each node before repeating the procedure.
	- Does this "layer by layer".
- Implemented with a [[Stacks and Queues|queue]]. The BFS algorithm is as follows:
	- Is as simple as changing the DFS algorithm above to use a queue instead.
```python
# nodes have edges/neighbors
visited = []
frontier = Queue()
frontier.push(START)
while not frontier.empty():
	curNode = frontier.pop()
	if curNode not in visited:
		visited.add(curNode)
		for n in curNode.neighbors:
			if n not in visited:
				frontier.push(n)
# to see which nodes in the resultant path:
return visited
```
- Observe that:
	- BFS will find the shortest path to all other nodes (given the weights of the edges are 1).
	- Has the same time complexity as DFS for very similar reasons.