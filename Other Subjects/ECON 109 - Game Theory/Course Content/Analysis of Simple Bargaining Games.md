#Economics #Game-Theory
## The Ultimatum-Offer Bargaining Game

^db40ba

The game where the first player offers $m$ to the second player.
- The first player gets $1-m$ and the second player gets $m$, but only if the second player accepts the offer.
	- If the second player rejects, the payoff vector is (0, 0).

Note that in the proper subgames, 
- if $m > 0$, then the second player will rationally accept the offer ("yes").
- if $m= 0$, then the second player is indifferent.

For clarity's sake, we assume that the second player will accept in the indifference case. 

This means that the first player has a lot of negotiating power and should always take the lion’s share, since the second player will always accept.
## The Basics of Discounting
How should we account for "discounting" across discrete periods of time?
- Typically, people are impatient with regard to gains (and opposite with regard to losses).
	- i.e. we want good things *now* and bad things *later*.
- Because we are impatient, if we are supposedly indifferent between getting $x$ in period $t$ versus getting $y$ in period $t+1$, $x$ will always be an (absolute) value less than $y$.
- The discount factor is the ratio derived from the values of x and y that we are indifferent between.
	- $\delta=x/y$. Multiplying $y$ by $\delta$ will give you $x$ (showing how you are indifferent between the two values).
		- So if you anticipate receiving $y$ in period $t+1$, it’s the same as receiving $\delta y$ in period $t$.
	- Note that if there are more than 1 period of time separating the balues, $\delta$ is compounded exponentially.

If we receive $x$ in each period (forever), our sum is,
- with clever factoring, $v= \frac{x}{1-\delta}$.
## Finite-Period Alternating-Offer Bargaining Games
This is where players play the ultimatum-offer game, back-to-back, where each offer is separated by one unit of time period.

Continuation values are therefore modified by $\delta$ as appropriate.

The deciding player says **yes** if $m^1 \geq \delta_2$, **no** otherwise.
- Why? Because if the offering player *doesn’t* offer $\delta_2$, the deciding player can simply wait until the next period where they can take the lion’s share, which is worth $\delta_2$ in the current period's value.

Consider the general $T$ period game:
- $m^1=\delta_2w^{T-1}_2$; the offer in the current period should be the discount factor of the receiving player times their continuation value (in a $T-1$ period game). 
- $w^T_1=1-\delta_2w^{T-1}_2$; the continuation value of a $T$ period game is what's left after offering $m_1$ (what should be offered).
	- Note the continuation value is also the SPNE for that period's subgame.

To find the continuation value of a certain period, create a table for both players and cross over the substitutions until finding the needed continuation value. [[Analysis of Simple Bargaining Games#^db40ba|The base case of T=1 grants continuation values of 1 for both]].

Note that patience yields a player a higher payoff.

Note also that the equilibirum is efficient.
## Infinite-Horizon Alternating-Offer Bargaining Game
$T$ is now infinite. How does the game analysis change?

We have two sets, $G_1$ and $G_2$, which denote the subgames which are infinite-horizon, alternating-offer, and have their respective subscripts having the first offer.
- This makes the optimal offer for the offering player $i$ to be $m^t = \delta_jv_j$.
- Generically, the continuation value of the current player $i$ is in terms of player $j$. $$v_i = 1-\delta_jv_j$$
- Another round of substitution leads us to $$v_i = \frac{1-\delta_j}{1-\delta_i\delta_j}$$
	- Which, incidentally, is the *unique* SPNE.