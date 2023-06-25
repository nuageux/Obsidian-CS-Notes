#Economics #Game-Theory 
## Best Response
A behavioral definition.
- Refers to a player optimally choosing their strategy to maximize their (expected) payoff.
- The best response depends on what the other players will do:
    - Player $i$ will set up beliefs (probabilities) for opposing player actions, then calculate his expected payoff (given those probabilities).
    - Then, set up an inequality such that one option has a higher payoff than the other, then solve for $p$ to determine when the first option has a higher payoff.
    - If payoffs are equal, then both options are best responses.
- A strategy $s_i$ for player $i$ is a best response to $\theta_{-i}$ if $u_i(s_i, \theta_{-i}) ≥ u_i(s_i’, \theta_{-i})$ for all $s_i’ \in S_i$.
    - “Strategy $s_i$ gives me the best possible payoff if $\theta_{-i}$ is my belief. There can be more than one such strategy $s_i$.”

## Dominance
- One player’s strategy _**dominates**_ another if it gives a _strictly_ better payoff than the other, no matter what strategies the _other_ players choose.
- Formally, for player $i$, $s_i'$ dominates $s_i$ if $u_i(s_i', s_{-i}) > u_i(s_i, s_{-i})$ for all $s_{-i}\in S_i$.
    - Note that we have to make the comparison between $s_i'$ and $s_i$ for every possible strategy the _other_ players could choose.
    - This is “strong” dominance. “Weak” dominance uses a ≥ sign.
- A common question is how to generate a mixed strategy that can deliver a higher expected payoff than one of the pure strategies.
    - To do that, set up payoff inequalities.

## Relationship between Best Response and Dominance
- A strategy is either dominated or undominated, never a best response (for any belief) or is a best response (for some belief).
    - So for best response, we will hold $s_i$ fixed and find some belief where the strategy is a best response.
- **The set of strategies that are dominated _is the same_ as the set of strategies that are never a best response!**
- **The set of strategies that are undominated _is the same_ as the set of strategies that are a best response (for some belief)!**
- If a strategy yields the highest payoff for another player’s strategy, it is _undominated_.

## Technical Notes on Distributions, Best Response, and Dominance
### Probability Distributions, $\Delta$
- For any set $Y$, let $\Delta Y$ denote the set of probability distributions over $Y$.
    - Ex: $\Delta S_i$ is the set of mixed strategies for player $i$.
    - Ex: $\Delta S_{-i}$ is the set of beliefs player $i$ has about the other players.
### Best-Response Sets, $BR_i(\theta_{-i})$
- There may be more than one best response to a given belief.
- $BR_i(\theta_{-i})$ denotes the set of best responses for a given belief held by player $i$.

### BR/Dominance in a Subset of a Strategy Space
- We will constrain the strategy space $S$ into a smaller subset $X$.
- For any $X=X_1 \times X_2 \times ... \times X_n \subset S$ and $s_i \in X_i$,
    - “$s_i$ is a best response in $X$” **if and only if**:
        - There is a belief $\theta_{-i} \in \Delta X_{-i}$ such that $u_i(s_i, \theta_{-i}) \geq u_i(s_i', \theta_{-i})$ for every $s_i' \in X_i$.
    - “$s_i$ is dominated in $X$” **if and only if**:
        - There is a mixed strategy $\sigma_i \in \Delta X_i$ such that $u_i(\sigma_i, s_{-i})>u_i(s_i,s_{-i})$ for every $s_{-i} \in X_{-i}$.
- $B_i(X)=\{s_i \in S_i \mid s_i$ is a best response in $S_i \times X_{-i} \}$.
- $B_i(X)=\{s_i \in S_i \mid s_i$ is not dominated in $S_i \times X_{-i} \}$.
- $B_i(X) = UD_i(X)$, generally.

### Algorithm to find Undominated Strategies/Best Responses

## Efficiency
- How we determine welfare in any economic setting.
- Strategy profile $s_i' \in S$ is called **more efficient** profile $s \in S$ if the payoff for $s'$ is better than or equal to strategy $s$, and strictly so for at least one player.
    - “When moving from one square in the matrix to another, at least one payoff improves and no payoffs decrease.”
- Strategy profile $s$ is called **efficient** if there is no strategy profile that is more efficient.
    - There is no way to make a player’s payoff go up without harming the payoff of the other players.
- Think of it as “group optimality”. This often conflicts with players’ own self-interest.
    - The **First Strategic Tension**, individual vs group incentives.
    - Ex: Prisoner’s Dilemma, which has an efficient outcome that can’t be reached as a rational strategy profile.