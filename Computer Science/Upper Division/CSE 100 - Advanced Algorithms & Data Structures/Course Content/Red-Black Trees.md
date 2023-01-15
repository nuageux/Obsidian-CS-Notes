#Data-Structure 
# Red-Black Trees

## Red-Black Trees

1.  All nodes must be red or black
    
2.  The root must be black
    
3.  If a node is red, all of its children must be black
    

-   Can’t have a red node with a red child

4.  For every node u, every possible path from u to a null reference must have the same # of black nodes

*Null references are black, because if we have a red leaf, both children should be black.

## Red-Black Trees vs. AVL Trees

Basically, Red-Black Trees aren’t necessarily AVL Trees.

Red-Black Trees typically has a larger height in practice. AVL Trees have a stricter balancing factor.

AVL Trees find elements faster, but Red-Black Trees can remove elements faster.

## Proof of Red-Black Tree Worst-Case Time Complexity

O(log(n)). Proof:

bh(x) is the number of black nodes from x to a leaf, excluding itself.

-   Leaves has bh(x) = 0

Claim: Any subtree rooted at x has at least 2^{bh(x)}-1 internal nodes.

Base Case: bh(x) = 0, when x is a leaf, by definition.

-   2^0 - 1 = 1 - 1 = 0, and leaves have at least 0 nodes.

Case 1: x is black, both children are black

-   both children have black height bh(x) - 1

Case 2: x is black, at least one red child

-   red child has the same black height, bh(x)

Case 3: x is red

-   both children are black by definition, so both children have bh(x) - 1

So, the number of internal nodes in a tree is 2^{bh(x) - 1} - 1 + 2^{bh(x) - 1} **-** 1 +1 ≥ 2^{bh(x)} - 1.

h: height of tree

-   bh(x) ≥ h/2 and n ≥ 2^{h/2} - 1
-   mess around and ull see the height is less than log(n)

## Red-Black Tree Insertion

Insertion Case 1: Empty Tree

-   Insert new node as the root
-   Color it black

Insertion Case ≠ 1: Non-Empty

-   Perform regular bst insertion
    -   if you see a black node w/ 2 red children, recolor all 3 (flip colors)
        -   if the parent is the root, color it black
-   color new node red
-   potentially fix tree for red-black tree properties

Insertion Case 2: Child of Black Node

-   done

Insertion Case 3: Child of red node, straight line

-   insert, single rotation, recolor

Insertion Case 4: Child of red node, kink

-   rotate to make straight, then case 3