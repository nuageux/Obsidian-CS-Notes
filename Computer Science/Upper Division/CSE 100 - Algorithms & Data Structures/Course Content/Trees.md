#Data-Structure 
## What are Trees?

- First, **Graphs**: A collection of nodes and edges.
    - Linked Lists are examples of graphs.
- **Trees** have two properties:
    - 1. They have no undirected cycles.
        
        - No loops.
        - If you turned the directed edges into undirected edges, there should still be no loops.
    - 2. Are connected.
        
        - There should be a (when undirected) path from any node to any other node.

### Special Cases of Valid Trees

- Empty (”Null”) tree, which has 0 nodes and 0 edges.
- Single node tree, which just has one node.

### Rooted Trees

- Hierarchical structure of top-to-bottom
- Parent-Child relationships going down the tree
- One node doesn’t have a parent, the **root**.
- Some nodes don’t have children, and are called **leaves**.
- **Internal nodes** are the nodes that have children.

### Unrooted Trees

- No hierarchical structure, more of an inside-out structure.
- Concepts of **neighbors**, the nodes that are directly connected to the current node.
- **Leaves** here are nodes with only 1 neighbor.
- **Internal nodes** here have more than 1 neighbor.

## Rooted Binary Trees

- Any node has at most up to 2 children.
- _Perfect_ binary trees are trees where every node has 0 or 2 children.

## Tree Traversals

- We need an algorithm to iterate over the nodes stored in our trees.

Depth First Search (DFS)

- Preorder Traversal
    - Visit, Left, Right
    - Guarantee that ancestors were visited before the node we’re on now
- In-Order Traversal
    - Left, Visit, Right
    - Only really makes sense in the case of a binary tree
- Postorder Traversal
    - Left, Right, Visit
    - Guaranteed that before visiting any node, all of that node’s descendants were already visited.

Breadth First Search (BFS)

- Level-Order Traversal
    - 1st level (left-to-right), 2nd level (left-to-right), ...
    - Traversing with respect to distance away from the root