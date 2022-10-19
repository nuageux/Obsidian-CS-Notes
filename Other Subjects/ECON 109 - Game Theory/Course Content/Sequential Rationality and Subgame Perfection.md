#Economics #Game-Theory 
# Sequential Rationality and Subgame Perfection

## Sequential Rationality and Incredible Threats

-   Sequential Rationality involves:
    -   Evaluating rationality at _every contingency_ (information set)
    -   Testing whether a player’s strategy specifies rational behavior from every point in the game where this player is on the move
    -   A refinement of best response: it is more stringent.
-   Incredible threats are proposed strategies that are not _sequentially_ rational.
    -   This implies that static rationality does not rule out incredible threats.
    -   So, we will now create dominance and Nash equilibrium models that incorporate sequential rationality.

## Backward Induction and Continuation Value

-   Apply to games of perfect information.
    -   Seqeuntial-move games where moves are observed by all players (no simultaneous moves).
-   Backward Induction analysis
    -   Start with decision nodes that lead only to terminal nodes (game-ending moves).
    -   Work backward toward the initial node.
    -   Express consequences of actions in terms of _continuation values_.

## Subgame-Perfect Nash Equilibrium

-   Adds conditions to the Nash equilibrium definition
-   Subgame: a mini game within a game
    -   if you erase everything but a node (and what comes after it) and it’s still a valid game (must have payoff vectors!), then it’s a subgame.
    -   the full game is also technically a subgame; so, a proper subgame is a subgame that’s smaller than the full game.
    -   we can’t make a subgame out of a node that is part of a non-trivial information set.
        -   furthermore, nodes that lead to non trivial information sets can’t spawn subgames for similar reasons.
        -   i.e. players must know that they’re in a subgame.
-   subgame perfect Nash equilibrium
    -   a strat profile that specifies a nash equilibrium at every subgame
    -   stronger definition
    -   whatever is a nash equilibrium in all normal form tables.
    -   if there are no dashed lines, background induction may be used.
-   Games being sequential means that we must substitute (Nash equilibrium) equations backwards whenever we see backwards induction.

## Technical Notes on Backward Induction, SPNE, Continuation Value

-   if there are payoff ties or imperfect information, there isn’t a unique SPNE.
-   For every finite game of perfect information, backward induction identifies at least one solution in pure strategies, and this strategy profile is a subgame perfect Nash equilibrium.
-   one deviation property for games _with perfect information_
    -   it’s a check for rationality: if by changing an action at any node the continuation value increases for a player, the current strategy is not currently a Nash equilibrium.