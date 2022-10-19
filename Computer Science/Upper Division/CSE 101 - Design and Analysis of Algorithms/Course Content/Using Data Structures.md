#Algorithm #Theoretical 
Consider how we can implement [[Graph Search]].

For reference,
procedure graphSearch (*G*: directed graph, *s*: vertex/node)
initialize *X* = **empty**
*F* = {*s*}
*U* = *V - F*
while *F* is not **empty**:
	**pick** *v* in *F*
	for each **neighbor** *u* of *v*:
		if *u* is not **in** *X* or *F*:
			**move** *u* from *U* to *F*
	**move** *v* from *F* to *X*
return *X*

# [[Graphs and Graph Traversal#^b7e7ab|Depth-First Search]]
- We will use a stack *F* and a boolean array *visited*.

procedure DFS (*G*: directed graph, *v*: vertex/node)
initialize array *visited* = false
initialize stack of vertices *F*
push *v* on *F*
*visited[v]* = true
while *F* is not **empty**:
	v = pop off *F*
	for each **neighbor** *u* of *v* (in reverse order):
		if not *visited[u]*:
			push *u* on *F*
			*visited[u]* = true
return *visited*

- Note that the array *visited* contains $X \cup F$.
- Initialization takes $O(|V|)$; setting up the first node takes $O(1)$.
- The outer loop takes at most $|V|$ times.
	- The inner loop takes $O(1+ deg(v))=O(|V|)$.
- The dominating term is $O(|V|^2)$, so that is the (loose) upper-bound.
	- It is a loose bound because most large graphs are *sparse*.
- Total (tight) time is actually $O(\Sigma_v(1 + deg(v)))=O(|V|+|E|)$, because when we only count the relevant neighbors, we count all the edges (twice, incidentally, if the relation is undirected).$$\Sigma_{u\in V}(deg(u)) = 2|E|$$ where $deg(u)$ is the number of neighbors $u$ has.
- Remember that the outdegree of a node is the number of edges out of that node (and vice-versa for indegree). *The sum of the outdegrees and indegrees of all nodes in the graph is the same.*
- Keep in mind this is an efficient algorithm.
- Remember that algorithms find all reachable vertices, NOT all *paths*! It would be terribly inefficient.
## DFS Recursively
procedure DFS_explore (*G*, *v*)
	*visited[v]* = true
	for each **edge** (*v*, *u*) in *E*:
		if not *visited[u]*: DFS_explore(*G*, *u*)

- There is a calling function for DFS_explore, which returns *visited* for our recursive function. *G* contains *E* (and *V*), incidentally.
- Note that recursion implicitly uses a stack implementation and is therefore DFS.

## Usages of DFS
Using [[Algorithm Mining|Augmentation]], we can use our DFS algorithm for other problems:
	- *Finding the Connected Components of an Unconnected Graph*
		- Note that DFS only costs the number of *reachable* nodes and *reachable edges*, and unreachable nodes or edges cost nothing.
		- So, the number of times DFS_explore is called is the number of connected components.
			- Remember to call DFS_explore in a member of *visited* that is false. 
		- The total time is $O(|V|+|E|)$.
	- *The Paths to all Reachable Nodes*
		- A simple path is at most $|V|-1$, and so is the most number of paths to all reachable nodes (a separate path for each node).
		- We can store all paths in $|V|$ space.
			- For DFS, paths overlap and form a $|V|-1$ edge tree.
			- `if not visited[u]: parent[u] = v; DFS_explore(G, u)`, where we add in the `parent` part of the code in the recursive algorithm.
	- *Ancestor Descendant Relationships*
		- We can add in "pre" and "post" arrays for our nodes to indicate the first time we encounter a node and the last time we leave it.
			- We list a "count" in our arrays to indicate when the event occurred.
			- *$u$ is below $v$ in the DFS tree* *iff* pre($v$) < pre($u$) < post($u$) < post($v$).

## Edge Types in a Graph
- Tree edges: solid edge included in the DFS output tree
- **Back edges**: leads to an ancestor
	- (u,v) is a back edge *iff* pre(v) < pre(u) < post(u) < post(v)
- Forward edges: leads to a non-child descendant
	- (u, v) is a tree/forward edge *iff* pre(u) < pre(v) < post(v) < post(u) 
- Cross edges: leads to neither ancestor nor descendant
	- (u, v) is a cross edge *iff* pre(v) < post(v) < pre(u) < post(u)

### Cycles
A cycle in a directed graph is a path that starts and ends with the same vertex.
- Generally, life is easier without cycles.
- So how do we check for cycles?
	- Easy: A directed graph has a directed cycle *iff* its DFS output tree has *even one* back edge.
	- Proof: Remember to be explicit!
		- If we choose any node in a cycle, then all the other nodes in the cycle are reachable from that node. However, one of the nodes in that DFS tree leads back to the original node, proving there is a back edge.
		- If we have a back edge ($b$, $a$): $b$ is reachable from $a$ (the path from $a$ to $b$ in the search tree) then combines with the back edge to lead directly back to $a$ (a cycle).
	- Therefore the algorithm simply checks the back edge condition for every edge $\in E$ within the graph. Because performing DFS is $O(V+E)$ and checking for back edges is $O(E)$, the runtime is $O(V+E)$.

We will use the acronym **DAG** to indicate a **directed acyclic graph**, a graph with no cycles.
- This means that $G$ is a $DAG$ *iff* its DFS output tree doesn't have any back edges. 

## Linearization / Topological Sort
A technique that gives at least one vertex ordering (path) such that all edges go in only one direction.
- At least one, because there can be exponentially many paths.

**Theorem**: every edge in a DAG goes from a higher post number to a lower post number.
- Suppose $(u, v)$ is an edge in a DAG. 
- Note that DAGs have no back edges. Forward, Tree, and Cross edges all have the property that post(v) < post(u)!
- Therefore, *sorting by decreasing post numbers is a topological sort.*

Using DFS with GraphSort allows us to topologically order a graph.
- Simply put nodes at the start of the list when their post number is assigned.

### Sources and Sinks
Sources have no incoming edges and sinks have no outgoing edges.
- *All DAGs have at least one source and one sink.*

## Strongly Connected Vertices
Two vertices $u$ and $v$ in a directed graph are strongly connected if there exists a path from $u$ to $v$ and from $v$ to $u$.
- So a strongly connected graph has this property for every pair of vertices it has.
- We can draw a "meta-graph", a graph made up of **Strongly Connected Components (SCCs)**. (see slides). 
	- All meta-graphs are DAGs.

Some SCCs are sinks and some are sources.
- If *explore* is performed on a vertex that is in a sink SCC, then only the vertices from that SCC will be visited.
	- So let us start at a sink SCC, visit the SCC and take it out from the graph, then repeat.

How do we find the sink?
- We find the source SCC of the reverse graph; the vertex with the largest post number in any DFS output tree belongs to a source SCC.
	- This is because the smallest post number doesn't necessarily belong to a sink SCC.

*Note that $G^R$ is the reverse of $G$ and the sources and sinks are swapped.*
- We reverse the graph in linear time. DFS also takes linear time.
- Order by the highest post number, then search the node in $G$ and remove all of those nodes from where we stored the post numbers (perhaps store them elsewhere if you need to keep track).
	- This takes linear time.

### DFS is useful for...
- Find what vertices can be reached by a vertex
- Divide an undirected graph into connected components
- Find cycles
- Find sinks and sources in a DAG
- Topologically sort a DAG
- Make a directed graph into a DAG of SCCs
- **But isn't good for finding the shortest distance between vertices.**

# [[Graphs and Graph Traversal#^c4b4b1|Breadth-First Search]]
Distance is defined as the distance of the shortest path between vertices.
- No path = infinite distance
- Self-loop = 0 distance

For BFS, the GraphSearch is the same except we implement the frontier set with a queue.

**Algorithm**
procedure BFS (*G*: directed graph, *s*: vertex/node)
for each **vertex** *u* in *V*:
	*dist(u)* = $\infty$ 
*dist(s)* = 0
**queue** *Q* = *[s]*
while *Q* is not **empty**:
	*u* = *eject(Q)*
	for each **neighbor** *u* of *v*:
		if *dist(v)* = $\infty$:
			*inject(Q, v)*
			*dist(v)* = *dist(u)* + 1

- Time analysis:
	- Each vertex is injected at most once and ejected at most once. $V+E$ time.
- Correctness: 
	- We know that it finds all the reachable nodes since it's a type of Graph Search. We want to show that BFS assigns *dist()* correctly to all vertices reachable from *s*.
- **Inductive lemma**: 
	- the queue contains exactly of those vertices with *D(v)* = *k*
	- all vertices with *D(v)* $<=$ *k* have been assigned *dist(v) = D(v)*
	- no vertex with distance *D(v) > k* has *dist(v)* defined.
- Compare actual distance *D(v)* to the BFS distance *dist(v)*. **WTS D(v) = dist(v) for all v.**

# [[Dijkstra's Algorithm]] and Weighted Edges
Sometimes we assign edges values like distance, cost, and time.

### Proving Dijkstra's Algorithm
The claim should be that when Dijkstra's is done, *dist(v)* is the length of the shortest path from *s* to *v*.

We need a lot of little things.
- (1) After every iteration, dist(v) is the length of *some* path (not necessarily the shortest).
	- the only time we change a dist value is when we find a path to that node! enough to prove existence.
	- we are iterating on the loop number.
- (2) dist(v) is non-decreasing in the order we add v to X/
	- say we add v to X in one iteration, and u to X in the next.
- (3) when dijkstra's is done, dist(v) contains the shortest path from s t ov for all vertices in V.
	- contradiction: suppose that for some vertex v, there is a path p from s to v such that the length of p < dist(v) (dijkstra's fucks up).
		- idea: examine the first  time something goes wrong. it's trivially impossible for anything to go wrong.

using negative edge weights will violate lemma 2

We use a priority queue.
- has a set of objects with adjustable key values (priorities)
- has the following operations:
	- insert(H, u, value), a new element 

binary min heap
- use bubble down formula when removing



