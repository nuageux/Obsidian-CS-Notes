#Algorithm 
# Union-by-Size
Whichever sentinel node in the union operation has more descendant nodes becomes the parent.

# Union-by-Height
Whichever sentinel node in the union operation has a larger height becomes the parent.

# Path Compression
Note that nodes in the same set have the same sentinel node, regardless of their position or depth in their respective up-tree.
- Idea: As we travel up an up-tree, we will "compress" that path by making all the nodes on the path upwards directly connect to the sentinel node at the root.
	- Simple to implement: Just make the parent pointer point to the appropriate sentinel node for all the nodes we have kept track of along the find operation.

# Up-Tree Time Complexity
Is equal to the time complexity of a find function, which, with path compression and one of the union techniques above, is amortized to a *constant* time worst-case.
- The initial find is slow, but afterwards is constant time.
- We typically use Union-by-Size because it is easier to implement.
- Remember that *union calls find* for each of its members in order to use their sentinel nodes!