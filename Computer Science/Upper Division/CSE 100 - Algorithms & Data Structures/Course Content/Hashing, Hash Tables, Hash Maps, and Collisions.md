#Data-Structure 
# Hashing, Hash Tables, Hash Maps, and Collisions

## Hash Functions

-   Input: an object `x`
-   Output: An integer representation of `x`

Property of Equality: If x is equal to y, h(x) must equal h(y).

-   Property of Inequality: If x is not equal to y, it would be nice (_but not necessary_) if h(x) was not equal to h(y).

## Hash Tables and Hash Maps

-   Hash and modding for `find`, `insert`, and `remove`.
    -   Are trivial withoutconsidering collisions.
-   Hash tables implement the Set ADT.
-   Hash maps implement the Map ADT.

## Probability of Collisions

Three basic probability functions:

-   $P(A)+P(A^c)=1$, and therefore, $P(A) = 1-P(A^c)$.
-   $P(A \cap B)=P(A)*P(B)$ for independent events $A$ and $B$.
-   $P(A \cup B)=P(A)+P(B)$ for mutually exclusive events $A$ and $B$.
-   Think about the differences between independent and mutually exclusive.
    -   Independent means the outcome of one event does not affect the probability of the other event whatsoever.
    -   Mutually exclusive means that if one outcome happens, the other one cannot possibly happen (and vice-versa).
        -   This means that mutually exclusive events are _dependent_ events!
-   Apply like so: $P_{N,M}(\geq 1$ collision$) = 1-P_{N,M}($No collisions$)$, where $N$ is the number of keys and $M$ is the number of slots.

## The Birthday Paradox

Essentially the equation presented above, which leads to the conclusion that in a room with a decent number of people, the probability that two people will have the same birthday is actually super high.

-   $N$ is the number of people, $M$ is the number of days in a year.
-   If there are 20 people, the probability is 41%(!)
-   If there are 30 people, the probability is 71%.
-   If there are 60+ people, it’s practically guaranteed.
    -   The conclusion drawn from this is that 60/365 of a table with no collisions is commonly used. This is _bad_, because it means that we’re leaving about 84% of our table unused!

Load Factor $= LF = N/M = \alpha$.

-   $\alpha = 1$ means there is guaranteed to be a collision.

Expected total number of collisions = $\Sigma_{i=1}^{N-1} i/m =N(N-1)/2M$.

-   Note that the expected number of collisions with the first element is $(N-1)/M$.
-   Set this expression equal to 1 (collision on average) and solve for $M$, which turns out to make $M=O(N^2)$ (which is bad).

The expected number of operations to find an element is therefore

-   $1/2*(1+1/(1-\alpha))$
-   **Smaller load factor means faster but we are wasting more space** and vice-versa.
-   0.75 is a common load factor value.