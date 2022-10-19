#Data-Structure 
# Ternary Search Trees (TSTs)
## Ternary Search Trees

-   BST: $O(klog(n))$, memory efficient
-   MWT: $O(k)$, memory ineffiecient
-   TST: Somewhere in between
    -   Has “word nodes” like a trie, but the nodes store values like a BST.
    -   If we want to “use” a node, we travel down the downwards edge.
    -   Otherwise, we travel down a side branch, indicating that we don’t want to use that node.

## TST `Find`

-   `current node = root`
-   `c = first letter of query`
-   `if c > current node’s letter:`
    -   `Traverse to right child`
-   `else if c < current node’s letter:`
    -   `Traverse to left child`
-   `else`
    -   `if c is last letter of query and current node is “word” node:`
        -   Success
    -   `else`
        -   `Traverse to middle child and go to next letter in query`
-   If there is any failure, word is not in TST

## TST `Insert` and `Remove`

-   Perform TST `Find`
    -   If you ever need to traverse a child that doesn’t exist, simply create it and traverse
    -   Make the last node in the traversal a “word” node
-   Perform TST `Find`
    -   Make the last node in the traversal “not” a word node.

## TST Time Complexity

-   Dependent on time complexity of a BST. Think of the middle nodes as the values themselves.
-   $O(n)$ worst case, $O(log n)$ avg case.
-   Works very well if the words have similar prefixes.