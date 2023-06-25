#Data-Structure
# Bloom Filters
An attempt to save space while maintaining the time complexity of a hash table.
- Probabilistic data structure
    - We’re not actually totally sure what’s in the data structure!
- Memory-efficient
- No false negatives
    - If the filter tells us an element doesn’t exist, then it definitely doesn’t exist.
- Can have false positives
    - But, if the filter tells us an element exists, it might not necessarily be true.

A bloom filter is a hash table of `bool`eans, all initialized to `false`.
- There are multiple hash functions, $k$ of them.
    - When inserting a new element, we will compute the hash value of this element for all $k$ hash functions.
    - Then, flip all the values of the filter that are in the given hash values to `true`.
    - When _finding_ an element, if any one of the hash functions returns `false`, then we know that the element definitely isn’t in our bloom filter (when inserting, all hashed indexes are set to true).
        - Should be intuitive as to why false positives exist.
- The bloom filter has $m$ slots.

## Designing an Optimal Bloom Filter
- We need to calculate the probability of a false positive in a bloom filter.
We make 2 assumptions:
- Each hash function uniformly distributes across the array
    - By this assumption, the probability of setting a specific bit to `true` is $\frac{1}{m}$.
        - Conversely, the probability of not setting a value in the array to `true` is $\frac{m-1}{m}$.
        - Then, for $k$ hash functions, we get $(\frac{m-1}{m})^k$.
    - Remember from calculus that $\lim_{m\to\infty} (\frac{m-1}{m})^m = \frac{1}{e} = e^{-1}$.
        - Rewriting the expression, we get $((\frac{m-1}{m})^m)^{\frac{k}{m}}$. Taking this to infinity, we get $e^{-\frac{k}{m}}$, the probability that one specific bit, after 1 insertion with $k$ hash functions, was _**not**_ set to `true` (stayed `false`).
        - So for $n$ insertions, the probability that a certain bit stays `false` is $e^{-\frac{kn}{m}}$.
        - Taking the complement and considering the $k$ hash functions gives us the **probability of a false positive**, $(1-e^{-\frac{kn}{m}})^k$
- Each insertion is independent.

We want to minimize the probability of a false positive.
- We have power over $k$ and $m$.
- Set $k=\frac{m}{n}\ln(2) = -\log_2(P(FP))$ .
- Set $m=-\frac{n\ln(P(FP))}{\ln(2)^2}$.

Steps:
- Estimate $n$.
- Pick an appropriate false positive probability.
- Find $k$.
- Find $m$.

# Count-Min Sketches
- Another Probabilistic data structure.
    - So, provides an _estimate_ of counts.
- Also memory-efficient.
    - Doesn’t grow in memory, is constant!
- Provides an upper-bound on counts.
    - So, commonly used for input streams that are too large to store.

Also has multiple, $k$ hash functions.
- Each hash function should correspond to one row of a 2-D array, each row a bloom filter.
- There are, of course, $m$ columns. All slots are initialized as 0.

To retrieve the value of count, find the hash value of the element in each of the corresponding rows.
- The minimum value among those $k$ values is the upper-bound on the count of the element we are searching for.

## Designing an Optimal Count-Min Sketch
Where:
- $n=$ # elements in the input stream.
- $c_x =$ true count of element `x`.
- $\hat{c}_x =$ estimated count of element `x`, where $c_x \leq \hat{c}_x$.

We want $\hat{c}_x \leq c_x + \varepsilon n$ with probability $1-\delta$. We want to minimize $\varepsilon$ and $\delta$.

Steps:
- Guess value of $n$, lean to an overestimate
- Pick a reasonable upper bound ($\hat{c}_x-c_x$).
- Pick a reasonable probability of being in this range ($1-\delta$).
- $m=\frac{e}{\varepsilon}$, $k=\ln(\frac{1}{\delta})$, take the ceiling of these both.

For a smaller range of error, we need bigger $m$, and for a higher chance of success, we need bigger $k$.