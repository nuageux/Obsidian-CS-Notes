#Economics #Game-Theory 
# Beliefs, Mixed Strategies, and Expected Payoffs

## Randomness

-   How does randomness arise in a game?
    -   One player’s belief about the other’s choice in strategy.
        -   When we convert this belief into a mathematical object, it becomes a **probability distribution**.
        -   Greek letters with a subscript $_i_$ will denote the other player’s beliefs about player $_i_$’s strategy. Set this letter equal to a tuple, where each entry in the tuple corresponds to the probability of a strategy of player $i$.
            -   i.e. $\theta_i=(p, 1-p)$ is the belief that player $i$ will play their first strategy with $p$ probability.
    -   When players are _actively randomizing_ over their choice in strategy.
        -   Called a **mixed** strategy. _Mixing_ between “pure” strategies.
        -   Use lowercase Greek sigma to denote the probability distribution.
            -   i.e. $\sigma_i = (q, 1-q)$ is player $i$’s mixed strategy.

### Evaluating Payoffs

-   To calculate, we _weight_ (multiply) outcomes with the probabilities (then sum them together).

## The Meaning of Payoffs

Can be thought of as “**abstract utilities**”.

-   The payoff “ranking numbers” we use are _just an abstraction_ to show player preference.
-   The **ranking** is what’s important.

Can also be thought of as “_attitudes toward risk_”.

-   i.e. how a player ranks a chance of getting an outcome versus a sure chance of getting another outcome.
-   _**Adjusting the payoff numbers**_ while _**maintaining the same ranking**_ can represent different attitudes toward risk.
-   “Risk-tolerant” vs. “Risk-averse”.

## General Assumptions and Methodology

-   “Conventional analysis of behavior requires that players have a _shared understanding of the entire game_”.
    -   The players know the extensive-form game they are playing, including the recognition that sometimes, certain players will be unable to distinguish between nodes in the same info set.
-   A fact _F_ is _**common knowledge**_ between players if each player knows _F_, each player knows that the others know _F_, each player knows that every other player knows that each player knows _F_, so on and so forth.
    -   Ex: players are around a table where _F_ is displayed, so that each player knows that everybody has seen _F_.
    -   _**Doesn’t imply**_ that during play, players have common knowledge of where they are in the extensive-form!
-   Analysis of rational behavior aims to:
    -   Precisely define concepts of rational behavior, leading to theories of how games are or should be played, that is to say, “solution concepts”.
-   A player is **rational** if:
    -   he forms a belief about the strategies of the others.
    -   given this belief, he selects a strategy to maximize his expected payoff.
-   The _rationalizability_ solution concept combines this definition with the assumption that the game and player rationality are common knowledge.
    -   _Nash equilibrium_ solution concept adds an assumption that social institutions help coordinate the players so that their beliefs and actual behavior are consistent.
-   Sometimes we aren’t always rational! Just something to consider.