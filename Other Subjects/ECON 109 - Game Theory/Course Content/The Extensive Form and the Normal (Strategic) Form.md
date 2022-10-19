#Economics #Game-Theory 
# The Extensive Form and Normal (Strategic) Form

## Normal-Form Representation

-   The simplest way of formally describing a game. a.k.a. strategic form.

Informally defined by the _players_, _strategies_, and _payoff functions_.

Formal Definition:

-   A _strategy_ is a **complete contigent plan of action** for a player.
-   The _strategy space_ for player $_i_$ is denoted by $_S_i_$.
    -   i.e. the set of every possible strategy for player $i$.
    -   $s_i$ represents one player $i$’s strategies in $S_i$.
-   Space of strategy profiles: $_S = S_1 \times S_2 \times ... \times S_n_$.
    -   i.e. every possible strategy combination of all $n$ players.
    -   $s$ represents one such strategy combination of a game.
        -   Ex: $s = (s_1, s_2, ..., s_n)$
-   Player $_i_$’s payoff function is denoted by $_u_i : S → \mathbb{R}_$
    -   Ex: $_u_i(s)=3$_ means that the payoff for player $_i_$ is 3 when strategy $_s_$ is played.

The normal-form representation is very useful for _static games_, where all actions are effectively taken at the same time.

-   **If** the number of moves is **finite** and the strategy spaces are **finite**, then the normal-form representation can be described with a **matrix**.

## Extensive-Form Representation

-   A way of describing the sequential structure of a strategic setting.
-   It is a graph describing all of the possible sequences the players can take.
    -   We will use a **tree structure**.
        -   Has **nodes**, represented by dots.
            -   Describes where the game begins, where decisions are made, and where the game ends.
        -   Has **branches**, represented by arrows.
            -   Describes the different possible actions the player has.
-   We put the **payoff numbers** at the ends of the branches (the ends of the game)
    -   Payoffs are written in order of the player numbers, and are comma-separated.

## The Formal Definition of a Strategy and Game Forms

Remember that _strategy_ is a **complete contingent plan of action for a player**.

-   When writing the strategy space, you write _**all**_ the combination of choices, even if a certain choice would end the game there.
    -   This is to either account for the possibility that the game ending move couldn’t happen for whatever reason (mistake, bad luck, etc.)...
    -   Or to describe why one would choose the game ending choice in the first place! (Looking at future moves!)
-   $_s_{-i}_$ represents every _other_ player’s strategy in the game (besides player $_i_$).

## Information Sets and the Strategy Definition

-   Information Sets: nodes where a player doesn’t know which node they are at. These nodes are linked with a dotted line in an EFD.
    -   Represents a “**contingency**” (= information set).
-   A “trivial information set” is where there is only one node to distinguish from (and therefore the player knows which node they are at). No dashed line.
-   How many strategies?
    -   = (# options in first info set) * (# options in second info set) * ... * (# options in $n$th info set)
-   T: When there are 3 players, we can use 2 tables for the normal-form matrix representation.
-   Think: A player _can_ have more decision nodes than information sets, because information sets can cover more than 1 decision node.
-   Think: It is **not** possible for the player on the move to pick different actions at two nodes connected in the same information set. They don’t have the info to make different contingent decisions!

## Representing Simultaneous Moves in the Extensive Form

-   What is critical to consider is that _when we say “simultaneous”, that’s equivalent to saying “lack of information”!_
-   So we use information sets to represent simultaneous moves.

## Translating from Extensive Form to Normal Form

-   Determine the set of strategies for each player and the set of strategy profiles
-   Determine payoff functions ($_u_i : S → \mathbb{R}_$) for each player $_i_$, and for each strategy profile $_s_$, trace the unique path through the game tree that $_s$_ induces, and record the payoff at the terminal node reached
-   Put the information into a matrix representation

## Games with Infinite Spaces

-   Means that some component of the game may be infinite, such as players, strategies, actions, time, stages of play, etc.
-   Ex: Cournot duopoly game
    -   Payoff: $u_1(q_1, q_2) = (c - q_1 - q_2)*q_1 - C(q_1)$, where $c$ is a constant for the consumer demand function, $q_1$ and $q_2$ are quantities selected by firms 1 and 2, and $C(q)$ is the cost of production for a given quantity $q$.
-   We will draw representative branches, maybe the minimum and maximum branches, with an arc connecting the ends of these branches.
    -   We will then put a representative node somewhere on this arc.
    -   It’s like a pizza slice!
    -   We will put another dashed line after the arc to denote a lack of information.