#Economics #Game-Theory 
## Rationalizability
1. Players have beliefs.
2. They best respond.
3. The above facts are common knowledge.

- 1) and 2) are referred to as “rationality”.
- This implies that players will select strategies from a subset of the strategy space. Some strategies don’t make sense.
- The best response/undominated formulas from before can then be summarized as follows:
    - “Restricting the other players to only their rational strategies (that attempt to maximize payoff), consider _**all**_ of player $i$’s strategies and whether they are best responses and/or undominated.”
- Consider $B(X) = B_1(X) \times B_2(X) \times ... \times B_n(X)$. This is a subset of $S$ and represents the rational strategy profiles.

## Iterated Dominance/Best Response Algorithm
1. We start with $S, B(S) \equiv R^1$, where $R^1 \subset S$.
or
1. Remove all the dominated strategies in the game (which gives $UD(S)$).  
2. Incorporating common knowledge, we know that players must select from $R^1$, so now, $B(R^1)=R^2$.
3. So on and so forth, until we get to set $R$, the “most rational” strategy space, the **rationalizable set**.