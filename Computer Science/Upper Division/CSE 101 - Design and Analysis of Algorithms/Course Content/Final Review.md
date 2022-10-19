Problems are of the form Instance, Solution Format, Constraints, and Objective.

## Graph Searching Techniques
- Adjacency Matrix
	- Check edge in O(1) time, but uses O(V^2) space
- Adjacency List
	- Check edge in O(V) time, but uses O(V+E) space
	- Easy to search neighbors
- DFS and BFS take O(V+E) for Graph Search
- Pre (moment of first discovery) and Post (moment of final departure) numbers
	- (u, v) is a back edge if Pre(v) < Pre(u) < Post(u) < Post(v)
		- Which indicates a cycle.
	- We can find a Directed Acyclic Graph by sorting the nodes by decreasing post number after a DFS (topological order).
	- Find Strongly Connected Components by contructing the reverse graph, linearizing the DFS result in decreasing order, then doing explore one by one removing the nodes in that SCC.
- Dijkstra's with:
	- Array (better for dense)
		- Sparse graphs where E = O(V), O(V^2)
		- Dense graphs where E = O(V^2), also O(V^2)
	- Binary Heap (better for sparse)
		- Sparse is O(V log(V))
		- Dense is O(V^2 log(v))

## Greedy Algorithms and Proofs
- Modify-the-Solution aka Exchange Argument
	- Let g be the first greedy choice the algorithm makes
	- Let OS be a solution achieved by not choosing g
	- Show how to transform OS into some solution OS' that chooses g, and that is at least as good as OS
		- Show OS' is valid *and* that OS' is better than OS
	- Use the above steps to form an inductive proof
- Greedy-Stays-Ahead: Show GS is at least as good as OS, every step of the way.
	- Define progress measure
	- Order decisions in OS to line up with GS
	- Prove by induciton that the progress after the ith decision in GS is at least as big as after ith decision in OS
	- Conclude that GS is at least as good as OS
- Kruskal's algorithm is a Greedy Algorithm

## Divide & Conquer
- Master Theorem
	- If T(n) = aT(n/b) + O(n^d) where a > 0, b > 1, d >= 0, 
		- if a < b^d, O(n^d)
		- if a = b^d, O(n^d log(n))
		- if a > b^d, O( n^(log_b(a)) )

## Backtracking

## Dynamic Programming

## Reduction
- If problem A reduces to B:
	- It means that to solve A, we use B.
		- Implies that B is "as hard" as A could possibly be, its "upper-bound".
		- Note that all hard problems solve easy problems.
	- If A is hard, B is hard.
	- If B is easy, A is easy.
	- The other two cases tell us nothing.