#Data-Structure
# Aho-Corasick Automatons

## Matching a Database of Many Short Strings to a Long Query String

-   Suppose we have a database of $m$ strings each of length $k$. Suppose also that we have one string query of length $n$, such that $n$ is much greater than $k$.
-   We want to check for each of our $m$ strings in the database to see if it is a substring of $n$.
-   There are $n-k+1$ start positions (if you think about the nature of substrings).
    -   Simplifies to $O(n)$ start positions (since $n >>k$).
-   For each string in the database, we get $O(nk)$ (start positions * a $k$ string comparision).
    -   So for $m$ strings, we get a total of $O(nkm)$. _This is too slow!_
    -   We need to preprocess the database to speed things up.

## The Aho-Corasick Automaton

Built from the database with $m$ strings of length $k$ each.

-   Firstly, construct the multiway trie for the database.
-   Now, we create many **“failure links”**.
    -   Every node in the MWT should be thought of as some string that is the concatenation of all the edge labels from the root to that node.
    -   Connect every node to the longest suffix of an actual word in the MWT (excluding itself (besides the root)).
    -   Critically, there is only one outgoing failure link from any given note.

Using this, we’ve reduced the time complexity to $O(n)$ (not including the time to actually build the automaton)! Sweet.

## Aho-Corasick Dictionary Links

The case where some words in the database are substrings of other words in the database.

-   We need **“dictionary links”**, too.
    -   Links between every single node and the first word node we encounter when we traverse over failure links until we hit a word node.
    -   No link is created if following the failure links leads us to the root!
    -   When traversing, consider dictionary links as epsilon transitions in an NFA.