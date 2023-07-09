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


