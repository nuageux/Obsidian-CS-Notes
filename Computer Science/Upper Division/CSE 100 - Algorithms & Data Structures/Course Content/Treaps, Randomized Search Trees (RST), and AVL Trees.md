#Data-Structure 
## Treaps

- Tree + Heap
- Stores `(key, priority)` pairs.

1. **BST** properties apply to keys.
    
2. **Heap** properties apply to priorities (top priorities are at the top).
    

## AVL Rotations

- Think of it as scales shifting.
- In either type of rotation, the leftmost and rightmost subtrees remain unchanged.
- In a **left** rotation, the inner subtree (the **left** child of the **right** child of the pivot node [**L-R-L**]) becomes the **right** child of the original pivot node.

## Treap Insertion

1. Insert via BST insert algorithm with respect to keys.
    
2. Use AVL Rotations to “bubble up” to fix the heap with respect to priorities.
    

## Randomized Search Trees (RSTs)

- The average-case time complexity for BSTs (the most efficient time complexity of O(log(n)) ) requires that all queries are equally likely to be searched for and that all insertion orders were equally likely.
    - This isn’t realistic.
    - RSTs try to alleviate the randomness conditions required for the average-case.

1. Use elements as keys.
    
2. Randomly generate priorities.
    

- Results in pretty balanced trees.
- Still O(n) worst case, though. Just more unlikely.

## AVL Trees

- **Balance Factor**: [height of right subtree] - [height of left subtree]
- **AVL Tree**: BST in which every node has a balance factor of -1, 0, or 1

Basically forces a balanced tree, which makes the worst case O(log(n)), what we’ve wanted all along.

## Proof of AVL Tree Worst-Case Time Complexity

Let $N_h$ be the minimum number of nodes that can form an AVL Tree with height $h$.

If the tree has height $h$, it has $N_h$ nodes and at least one of the subtrees must have height $h-1$.

Furthermore, this subtree must have $N_{h-1}$ nodes within it (following the original assumption).

The other subtree, in the worst case scenario, has height $h-2$ (due to the definition of an AVL tree). This subtree then would have $N_{h-2}$ nodes.

This introduces a recurrence relation, namely $N_h = N_{h-1} + N_{h-2} + 1$ (the root).

(Note that for this proof, height is defined as the number of nodes as opposed to the number of edges.)

$N_1 = 1$, $N_2 = 2$.

$N_{h-1} = N_{h-2} + N_{h-3} + 1$

$N_h = (N_{h-2} + N_{h-3} + 1) + N_{h-2} + 1$

Note that $N_h > 2N_{h-2}$.

$N_h > 2^{h/2}$

$2logN_h > h$

Therefore, $h$ is $O(logN_h)$.

## AVL Tree Insertion

1. Regular BST insertion
    
2. Update the Balance Factors
    
3. Fix broken Balance Factors using AVL rotation
    

- If we encounter a “kink” (alternating left-right or right-left subtrees) we have to use **two** AVL rotations, starting from the lower subtree.
    - When looking for “kinks”, note the heavier child then the heavier **grandchild**. If they’re the same direction, one rotation. Otherwise two.