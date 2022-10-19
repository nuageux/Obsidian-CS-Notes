#Economics #Game-Theory 
# Strictly Competitive Games and Security Strategies

## Security Strategies and MaxMin Strategies

-   Based on the notion of _**caution**_ and _**worst-case scenarios**_.
-   Define the worst playoff player $i$ gets as $w_i(s_i)=$ the lowest possible payoff for $i$ for any strategy $j$ chooses, given that $i$ chooses strategy $s_i$.
-   Define the security strategy $\underline s_i$ where $\underline s_i$ gives the maximum payoff for $i$ _**amongst the set of worst payoffs $i$ could get**_.
    -   i.e. $i$ will look through each of his strategies and gets $w_i$ for each strategy. $\underline s_i$ is then what gives the highest value out of these $w_i$’s.
    -   The value is called the _security payoff level_.
-   Is in terms of a **pure-strategy** choice.

**MaxMin strategies** are for **mixed** strategies.

-   Define as $\underline \sigma_i \in \Delta S_i$ if, similarly, it gives the maximum _**expected**_ payoff
    -   The value is called the _maxmin payoff level_.
        -   Will be at least as large as the security payoff level (can be more).
-   Think of it as when graphing the mixed strategy payoff functions in terms of probability variables, the lower triangle border is the region of worst payoffs, and the intersection point it the maxmin payoff level. Using a mixed strategy with the intersection probability is the safest strategy.

## Equilibria of Strictly Competitive Games

-   Formally, a two-player game is _**strictly competetive**_ if, for every pair of strategy profiles $s,s' \in S$, we have $u_i(s)>u_1(s')$ _iff_ $u_2(s) < u_2(s')$.
    -   i.e. the two players have exactly opposite rankings over the outcomes!
    -   For P1, list the lowest payoff in one column and the corresponding payoff for P2 in another. Find the next lowest payoff, etc. P1’s column should be in a strictly ascending order while P2’s column should be in a strictly descending order.
-   A _constant-sum_ game has the property that there is a number _y_ such that $u_1(s)+u_2(s)=y$ for every $s \in S$.
    -   A “zero-sum” game is when $y=0$.
-   Strict competition **does not** _generally_ extend from pure to mixed strategies.
    -   However, every constant-sum game remains strictly competitve in terms of mixed strategies.
-   If a two-player game is strictly competitive and has a Nash equilibrium $s^* \in S$, then $s_1^_$ is a security strategy for P1 and $s_2^_$ is a security strategy for P2.
    -   On top of this, the security level and maxmin level is the same in this case, so $s_1^_$ and $s_2^_$ are maxmin strategies as well.