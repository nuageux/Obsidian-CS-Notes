#Data-Structure #Algorithm 
## Burrows-Wheeler Transform (BWT)
A database sequence of length $n$ and a set of $m$ query sequences each roughly length $k$.

But for the BWT, add a null-termination character at the end of the string.

- Then, we list all “rotations” of the database string (like a circular array).
- Then, we sort these rotations in alphabetical order. The null-terminating character comes first.
- _**The BWT is the last column of this sorted matrix**_.

Remember we only care about the first and last columns to construct the BWT.

## Inverting the BWT
We can reconstruct the original string from the BWT.

- First, sort the BWT in alphabetical order to get the original first column.
- Then for both columns, travel down both and subscript each letter based on how many times it has appeared so far. This order is the same!
    - Then, note that the first column of the same row as the last column indicates which character comes directly after the last column. Reconstruct by tracing.
    - When we encounter the top right character again, we’ve finished tracing.

Everything is $O(n)$.

## Pattern Matching Using the BWT

In order to find queries, we need to keep track of a few more things.

- The index of the rows
- The “last-to-first” index mapping. “When does what appears in the last column appear in the first column?”

Steps:
- Start with the top at index 0 and bottom at the last index.
- Search backwards. Find the first and last instance of the last character in the last column, then shift top and bottom to the mapped indexes.
- Repeat going backwards in the string with the new boundaries until done.