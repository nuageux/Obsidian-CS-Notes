#Economics #Game-Theory 
# Mixed-Strategy Nash Equilibrium

$\sigma^_=(\sigma_1^_, \sigma_2^_, ..., \sigma_n^_)$ is a **mixed strategy Nash qeuilibrium** if for each $i$ and every $s_i \in S_i$,

-   $u_i(\sigma_i^_, \sigma_{-i}^_) \geq u_i(s_i, \sigma_{-i}^*)$.
-   i.e. when playing this mixed strategy (of the set $\sigma^*$), it provides a better payoff than any pure strategy (given that the other players are also playing their corresponding mixed strategies).

To find the mixed strategy Nash equilibrium (in a two player game),

-   Find the rationalizable set with pure strategies.
-   Assign probabilities for each of the players’ strategies (with differing probability variables, of course).
-   Calculate one player at a time:
    -   For P2, if P1 is playing his mixed strategy, make payoff equations for each of P2’s strategies. Solve this equation for P1’s probability variable.
-   Combine both P1 and P2’s mixed strategy into the tuple $\sigma^*$.

## Nash’s Theorem on the Existence of Equilibrium

**Every _finite_ game** **has at least one Nash equilibrium** **in pure _or mixed_ strategies**.

-   “Finite” meaning a finite _number of players_ and a finite _strategy space._