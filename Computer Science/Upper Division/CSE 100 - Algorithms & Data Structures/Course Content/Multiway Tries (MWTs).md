#Data-Structure 
## Tries

- A [[Trees|tree]] structure in which elements are represented by paths.
    - Nodes have no values! No labels!
    - Edges are labeled. _A path represents an element_ based on the labels concatenated going down the path!
    - “Word nodes” are where paths can stop.
- Name comes from “retrieval” (but pronounce “try”).

## Multiway Tries

- Trie in which nodes can have more than 2 children (and can thus represent many more strings).

## MWT Insert, Find, and Remove

- An initialized MWT is just the root.
- Inserting a string is as follows:
    - Check to see if first character has a path or not
        - If not, then create a path for the first character.
        - If it has a path, then follow that path and repeat.
- If, while following an existing path, the string is covered, then just make the current node a word node.
- To find, follow the path corresponding to the node, and if the full path exists and ends on a word node, return `true`.
- To remove is simple; just find the word in the trie, and if it exists, change the node from a word node to not a word node.

## MWT [[Time and Space Complexity|Time Complexity]]

- If $n$ = number of words and $k$ = length of the longest word entered:
- It actually doesn’t matter how big $n$ is, but is instead dependent on how big $k$ is, giving $O(k)$ time.

## MWT Space Complexity

- Every node in the trie must have an array (with the size of the alphabet) to represent whether edges exist or not.
    - We use pointers to represent whether edges exist, and because we commonly use a lot of null pointers, _there’s a lot of wasted space!_
    - So if the trie is dense, the space complexity is good. If it’s sparse, that’s bad.

## Algorithms of Use on MWTs

- Iterate in increasing order
    - Preorder traversal and output if it is a word node
- Iterate in descending order
    - Similarly, postorder traversal and output if word node
- Iterate in increading order of length
    - Level order traversal
- Autocomplete
    - Perform `find`, then traverse from that node in any manner you deem appropriate.