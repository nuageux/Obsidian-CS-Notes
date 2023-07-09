#Data-Structure 
## Hash Functions
- As a function, hash functions take an input object `x` and output an integer representation of `x`.
- Hash functions also display the following two properties:
	- Property of Equality: If $x=y$, $h(x) = h(y)$.
	- Property of Inequality: If $x \neq y$, it would be nice (_but not necessary_) if $h(x)\neq h(y)$.

## Hash Tables and Hash Maps
- We commonly use hashing for `find`, `insert`, and `remove` operations.
    - These are trivial if we do not consider collisions.
- Hash tables implement the Set [[Data Structures vs. Abstract Data Types#^412b3e|ADT]].
- Hash maps implement the Map ADT.

## Probability of Collisions

^dbb89b

- Let us consider the probability of collision occurrence. Reviewing some basic probability, consider that:
	- It is certain that event $A$ occurs or $A$ doesn't occur. $P(A)+P(A^c)=1$, and therefore, $P(A) = 1-P(A^c)$.
	- If events $A$ and $B$ are [[Independent and Dependent Events|independent events]], the probability they both occur is $P(A \cap B)=P(A)*P(B)$.
	- If events $A$ and $B$ are [[Independent and Dependent Events#^5838e6|mutually exclusive]], The probability that either occurs is $P(A \cup B)=P(A)+P(B)$.
- We can then apply this logic to collisions:
	- $P_{N,M}(\geq 1$ collision$) = 1-P_{N,M}($no collisions$)$, where $N$ is the number of keys and $M$ is the number of slots.
		- We prefer to calculate the probability of *no* collisions, as *it is easier than calculating the probability of $n$ collisions*.
	- This is a clear application of the [[Birthday Paradox]], which reveals that collisions are more likely than we would assume.

### Load Factor
- The above sections lead us to the concept of a "load factor", an indication of how many elements a hash table can support.
	- The load factor is defined as $LF = \frac{N}{M} = \alpha$, where $N$ is still the number of keys and $M$ is still the number of slots. $\alpha$ is the symbol for load factor.
	- A higher load factor indicates slower retrieval, but we make full use of the hash table's space.
		- $\alpha=1$ means that at least one collision has occurred already or one is guaranteed on the next insertion ([[Pigeonhole Principle]]).
	- A smaller load factor indicates faster retrieval, but we leave much of the hash table's space unused (we "waste" it).
	- ==0.75== is a common load factor value.

#### Some Math
- The expected total number of collisions is $$\mathbb{E}(C) = \sum\limits_{i=1}^{N-1} \frac{i}{M} =\frac{N(N-1)}{2M}$$where $C$ is the total number of collisions.
- We can rearrange the above equation in terms of the load factor to get $$\mathbb{E}(C)=\frac{1}{2}(1+\frac{1}{1-\alpha})$$
	- As $\alpha$ grows, the expected number of collisions grows exponentially.