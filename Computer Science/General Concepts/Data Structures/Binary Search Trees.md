#Data-Structure 
## Properties of a Binary Search Tree (BST)
- Rooted Binary Tree
- Every node is larger than all nodes in its left subtree
- Every node is smaller than all nodes in its right subtree

## BST Find Algorithm
- Start at root
- If query == current, success
- Else, if query > current, traverse right and go to second step
- Else, if query < current, traverse left and go to second step
- If you ever try to traverse left/right but the child doesn’t exist, **fail**

## BST Insert Algorithm
- Perform “find” from the root
- If find is true, it’s a duplicate. **Fail**
- Else, insert new element at site of failure.

## BST Successor Algorithm
- The next largest node.
- If node has a right child, traverse right once, then all the way left
- Otherwise, travel up the tree. The first time the current node is its parent’s left child, the parent is our successor

## BST Remove Algorithm
Case 1: No Children
- Just delete the node
Case 2: One Child
- Just directly connect child to parent
Case 3: Two Children
- Swap with the successor value, and remove the original node.
- Searching for the successor guarantees that the swapped node won’t have a left child (goes as far left as possible).

## BST Time Complexity
- Height of a node: Longest distance (# edges) from node to a leaf
- Height of a tree: Height of the root

### Describing Time Complexity with _Tree Balance_
- Perfectly Unbalanced (a line) to Perfectly Balanced
    - Perfectly balanced minimizes the required height of the tree
    - Unbalanced: height = n - 1, worst case = O(n)
    - Balanced: height = log2(n + 1) - 1, balanced case = O(log(n))

### Best vs Worst vs Average Cases
- Best: query is the root
- Worst: perfectly unbalanced, query not found
- Average: Theoretical expected value over all trees and queries
    - $E(Y) = \sum_y y*P(Y=y)$
    - All n elements are equally likely to be searched for
    - All n! possible insertion orders are equally likely
- Depth
    - The number of nodes in the path from that node to the root. Root is depth=1.
    - Used because it’s equivalent to the number of expected comparisons