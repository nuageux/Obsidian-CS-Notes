#Data-Structure 
# Disjoint Set ADT
- The **Union** operation, given two elements $u$ and $v$, merges their sets.
- The **Find** operation, given an element $u$, returns its set.

# Up-Trees
Where some nodes are regular nodes while some are **sentinel** nodes.
- Sentinel nodes represent their respective sets and are the roots of their respective trees. Connections point *up* the tree.
	- Note that nodes can have any number of children.
- We implement the **find** method by moving *up the tree* until we reach our representative sentinel node.
- We implement the **union** method by finding the respective sentinel nodes of both sets, then making one the child of the other.
# Representing Up-Trees Using Arrays
Note that there are only either sentinel nodes or regular nodes, and nodes either have an outgoing parent pointer or don't.
- This makes things easy. For each entry in the array, store the node value and where its parent pointer goes (null if the node has no parent).
