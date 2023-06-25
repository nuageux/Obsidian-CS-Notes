#Data-Structure #Algorithm 
## Matching a Query Set of Many Short Strings to a Long Database String

Notice how this is essentially the opposite of Aho-Corsick.

- The (potentially long) single sequence is generally unchanged (and is now the database), while the (now) long set of (now) queries can change.

We are given a database string that is length $n$ and a set of $m$ query strings each of length $k$. Similarly, the naive linear scan gives the (prohibitively slow) runtime of $O(nkm)$.

We still want to preprocess the database somehow to cleverly reduce runtime complexity.

## Suffix Arrays

Idea: Wherever a substring is found, it’s also the start of a suffix of the (long) database string.

A suffix array is then:

- Ordering all the suffixes of the database in alphabetical order.

Steps:

- Generate the list by index.
- Sort the list. We only need to store the start positions (index values) and generate the suffixes on the fly when needed (including when we are sorting this very list).

## Suffix Array Search

Do a binary search on your sorted suffix array!

- After we find the right `mid` value, we want to tighten the `low` and `high` values to only include our query (remember there may be overlap). This is a linear operation (one-by-one).

We sort a length $n$ list in $O(n\log n)$ time, but because compared strings can be up to length $n$, we combine these into $O(n^2\log n)$ to create our suffix array.

- Note that this only has to be done once!

To find queries, we know binary search is logarithmic, but we’re comparing strings of length $k$ so we get $O(k\log n)$ per query sequence, so for every query search, we get $O(mk\log n)$.

**Alternatively**, do 2 binary searches, one where there is a match to query _but there is a mismatch to_ `low - 1`, and another one where there is a match to query _but there is a mismatch to_ `high + 1`. Will give the precise range immediately. Same time complexity of roughly $O(k\log n)$.
