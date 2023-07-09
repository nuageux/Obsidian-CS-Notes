#Algorithm 
- The goal of Dijkstra's Algorithm is to [[Graph Search|find shortest paths in a graph]] given that there are "weights" on the edges of the graph.

### Idea
- Assume that nodes have a "distance" value which indicates the cost to get to that node.
- We use a [[Priority Queues|priority queue]] that sorts by weight to efficiently get the next cheapest option.
- If we visit a node for the first time, we assume the distance travelled to it so far is the shortest path to that node.
	- If we happen to visit that node again with a better (shorter) distance, we will update that node's distance value with the new, shorter distance.
- By repeating this systematically through all of a graph's nodes, we can find the least costly path to a node from a start node.
	- We keep track of the `prev` node from a node to remember the shortest path we find.
	- Working backwards from a goal node, simply follow the `prev` nodes back to the start node to get the shortest path.
- The algorithm pseudocode for finding the shortest paths from one node to all other nodes is as follows:
```python
# initialize
start node distance = 0
other node distances = INFINITY

# priority queue sorted by d
distances = PriorityQueue()
distances.offer(0, start_node)
visited = []

# algorithm
while not distances.empty():
	dist, curNode = distances.poll()
	visited.add(curNode)
	
```

### [[Time and Space Complexity|Time Complexity]]
If $|V|$ is the number of nodes (vertices) and $|E|$ is the number of edges, the time complexity of Dijkstra's Algorithm is $O(|V| + |E|\log |E|)$.
- Dijkstra's with:
	- Array (better for dense)
		- Sparse graphs where E = O(V), O(V^2)
		- Dense graphs where E = O(V^2), also O(V^2)
	- Binary Heap (better for sparse)
		- Sparse is O(V log(V))
		- Dense is O(V^2 log(v))

### Proof of Correctness
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

## Uniform Cost Search (UCS)

^3864c1

- UCS is another application of Dijkstra's, where we begin at a starting point and attempt to find the shortest path to a goal point.
- The algorithm pseudocode is as follows:
```python
# nodes have costs and actions (directed edges)
# prio queue ordered by distance for (dist, node)
frontier = PriorityQueue()
frontier.push(0, START)
explored = []
# unexplored is implicitly all the nodes not in frontier or explored

while True:
	if frontier.empty():
		return Failure
	curDist, curNode = frontier.pop()
	if curNode is GOAL:
		return Success
		
	explored.add(curNode)
	for a in curNode.actions:
		child = curNode.a()
		if child not in (explored or frontier):
			frontier.push(dist+child.cost, child)
		# elif we find a better path
		elif child in frontier [with higher path cost]:
			frontier.remove(child)
			frontier.push(dist+child.cost, child)
```



