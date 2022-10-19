#Algorithm 
# Dijkstra's Algorithm
When looking at a weighted graph (where there are values on the edges), Dijkstra's Algorithm is as follows:
0. Set all nodes' distances to $\infty$ and the start node's to 0.
1. Add (0, start) to the priority queue.
2. While the priority queue is not empty:
	1. Pop (d, curr) from the priority queue.
	2. If curr is not done:
		1. Mark it as done.
		2. For all edges (curr, w, e):
			1. If d+e < w's current distance:
				1. w's current distance = d + e.
				2. w's previous node is curr.
				3. Add (d+e, w) to the priority queue.

### What?
Essentially, put all of the edges and their weights of the current node into a priority queue.
- If you're visiting a node for the first time, then that's the current shortest path to that node. If you visit that node again with a different path, we check whatever path is shorter and make that the length to beat.
- By repeating this systematically through all of a graph's nodes, we can find the least costly path to a node from the start node:
	- Working backwards from the end node, just follow the prev nodes to the start node.
- We keep track of the "prev" node to remember the shortest path we find.

# Time Complexity
If $|V|$ is the number of nodes (vertices) and $|E|$ is the number of edges, the time complexity of Dijkstra's Algorithm is $O(|V| + |E|\log |E|)$.