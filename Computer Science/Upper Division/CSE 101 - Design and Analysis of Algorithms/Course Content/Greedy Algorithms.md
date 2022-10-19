## Bipartite Graphs
The graph is "two colorable", that between two groups of nodes, edges only go between groups (not within groups)
- if there is even one odd length cycle, then graph isn't bipartite. IFF
- if there are no odd cycles, then the graph is bipartite. (the other direction)

red blue argument, in a graph with no odd cycles, choose one node x in a cc then for each y in the cc, label them as even or odd reachable from x

odd even reachability
- using polarity in explore doesn't work because some nodes might be reachable by both even and odd paths
- same argument where we find the point where we fuck up and try to prove why it's kinda impossible to fuck up at that point in the middle

reduction? instead of fucking with the algorithm, try changing the input instead. then you don't have to make a whole new proof of correctness or a new time analysis
- make 2 copies of each node, one even and one odd... use the bipartite graph principle with 2 edges for each edge that existed in the original graph with the 2 sets of nodes!


Max bandwidth path problem
- write down new problems precisely.
- messing with dijkstra's?

decision problem, optimization problem



Optimization problems, there is a format
instance, solution format, constraint, objective

for max bandwidth, the instance (input) was the directed graph, edge weights, and starting and end nodes
the solution format was a path (list of edges)
constaint was that edges must from a path from start to end
objective was maximizing the minimum of the path we make

there are too many paths (exponential) to just list em all out

global search vs local search... break the huge solution set into a series of simpler local searches for part of the solution... (what's the first edge? the second?)

the "greedy" solution is just picking what seems like the obvious best solution.
- it doesn't always work, of course.

in order to use greedy, we need to prove the correctness of the algorithm. else, we need a counter example. although it is often wrong, it is crazy efficient when it works so we look for these greedy algorithms.

furthermore, there may be more than one potential greedy strategy... so if one is shot down, don't quite give up on the other ones.

event scheduling example has a space that is exponentially large

proving correctness.
we want to show that our greedy algorithm is better... either minimizes cost or maximizes value.

modify the solution aka exchange argument
1. let g be the first greedy choice the algo makes
2. let OS be a solution achieved by not choosing g
3. show how to transform os into some solution os' that chooses g and that is at least as good as os... os' is a valid solution and os' os
	1. in our case, we replace os's first choice s with g and they are guaranteed to not overlap by definition
4. use induction



------------------
strategies for greedy algorithm proofs
intuitive arguments are usually incorrect

maximize value or minimize cost

techniques
- modify the generic solution (use)
	- as shown above
	- define OS' from OS, d, g
	- prove OS' is a valid solution, using the knowledge that OS is valid
	- prove OS' is optimal with an objective function (didn't reduce the quality of OS)
	- if there are multiple cases, you gotta do the three steps above for each case.
- greedy-stays-ahead
	- show GS is as good as OS in some suitable sense, *every step of the way*.
	- define the progress measure
	- order the decisions in OS to line up with GS
	- prove by induction that the progress after the ith decision in GS is at least as big as after ith decision in OS
	- conclude that GS is at least as good as OS
- greedy achieves the bound
	- show the time where every room is required
- unique local optimum (don't use)


a whole thing on minimum spanning trees and kruskal's algorithm; definitions of trees etc

array called "leader"

idea: use doubly linked lists to store sets, so now union only takes the size of the set itself instead of the whole node list

union by size: the worst case size n/2 can only possibly happen as the last operation. -> leads to an nlogn union over time.


charging argument; giving each of the n elements (leaves of the binary tree) log n tokens is enough (or more than enough!) to cover the cost over all of the union operations



