#Theoretical #Algorithm 
[[Graphs and Graph Traversal|Graphs]] are collections of nodes and edges used to represent data, and oftentimes provide a useful perspective on a problem.

## Graph Coloring Problem
Where nodes of a graph are colored with as few colors as possible while there is no edge between nodes of the same color. Examples include:
- Cartographer's problem
	- node = country
	- edge = neighbors
- Exam Scheduling
	- node = class/exam
	- edge = some student is taking both classes
	- color = time slot
- Animal Crossing riddle
	- node = animal
	- edge (directed) = one endpoint-animal will eat the other
	- color = boat
- Storage Container problem
	- node = container
	- edge = if neither container fits inside the other
	- color = a stack
- Covering Points
	- ?

Note that the graph isn't necessarily connected; there can be multiple, separate components.

## How Graphs are Stored on a Computer
Typically graphs are represented as [[Graphs and Graph Traversal#^a0afa3|adjacency matrices]] or [[Graphs and Graph Traversal#^c8fe3b|adjacency lists]]. 
- Matrices can check for an edge in constant time, but take up $O(V^2)$ space.
- Lists can easily iterate through a node's neighbors and only take up $O(V+E)$ space, but has a slower edge lookup time of $O(V)$.

# Graph Reachability and DFS
Graph reachability: Given a directed graph $G$ and a starting vertex $s$, return an array that specifies for each vertex $u$ whether $u$ is reachable from $s$.
- We could use [[Graphs and Graph Traversal#^b7e7ab|Depth-First Search]] or [[Graphs and Graph Traversal#^c4b4b1|Breadth-First Search]] for the traversal algorithm.
- Idea: When we have pinpointed a single node, the only action we can feasibly take is to examine all of its neighbors.

### Generic Graph Search
At each point in the algorithm, the vertices/nodes are partitioned into $X$ (eXplored), $F$ (Frontier), and $U$ (Unreached).
- $X$ indicates all outgoing edges have been examined while $F$ indicates that we have merely seen the node (and haven't checked its neighbors).
- At the end of the procedure, $F$ will be empty and $U$ will contain all the unreachable nodes.

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

#### Proof of Correctness
We must prove two things to show that our algorithm solves reachability correctly:
1. All vertices $v \in X$ are reachable from $s$; i.e. everything returned in set $X$ is reachable from $s$.
	- We prove this using loop invariants.
2. All vertices that are reachable from $s$ are returned in set $X$.
	- We use proof by contradiction.
	- In general, the strategy is to think about the case where the output is incorrect and the first place in the where the algorithm messes up (assuming everything up to that point was done correctly). We then show that it's impossible to mess up at that point.

#### Loop Invariants
Where if a claim is true at the start of a loop, it will still be true at the end of the loop.
- We use the special case of the invariant when the loop *stops* to show correctness.

#### The Induction Step
1. Assume the invariant is true after $t$ iterations
2. How does the loop define the new values of the same variables?
3. Why is the invariant statement true for these new values?

Graph Search can be implemented in many different ways; the above is just the general procedure.
- Generally, we want to use an adjacency list, since it's likely to be a sparse graph.
- We will often iterate through the neighbors using the list.