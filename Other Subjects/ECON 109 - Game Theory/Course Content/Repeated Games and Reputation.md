#Economics #Game-Theory
# Finitely Repeated Games
Think of a timeline with discrete periods of time.
- In each period, both players will participate in a "stage game", which for our purposes, is exactly the same as a simultaneous, normal-form game.
	- The payoff table for each stage game is the same!
- At the end of each period, players observe what happened.

The payoff of this repeated game is the sum of all of the stage games that have taken place. 

The interesting takeaway from repeated games is that players may choose actions in an equilibrium that seem irrational if we were only to consider the stage game in isolation.
- The history of play *conditions* player behavior in the future.
- We write succeeding strategies as a function based on the strategy taken in preceeding stage games.
- Player $j$ can choose to reward or punish Player $i$ based on how $i$ has played in the previous stage game(s).
- If there are more than one NE to choose from in the last stage play, the player who has the choice of strategy in the last stage can reward or punish.
	- If there is a unique NE, there is no way to reward or punish prior behavior (and thus only one SPNE, where the stage-game NE is played in every period).
	
# Infinitely Repeated Games (Grim-trigger)
With the same timeline with discrete periods of time, but with an infinite horizon (the game never ends).
- The payoff function is now likely very complicated.
	- The simplest functions are those that play a certain strategy regardless of the history.
- We also assume that the players are impatient and discount the future.
- We look for "reputation"-based equilibria.
	- Players might be punished for tarnishing their reputation.

We look at the infinitely repeated "Prisoner's Dilemma" game.
- Recall that $CC$ (cooperate-cooperate) is a more efficient outcome than $DD$ (defect-defect), but the Nash Equilibrium (in a one-shot stage game) rests at $DD$.
	- But, if we are in an infinitely repeated game, there is a way to motivate the prisoners to play $CC$(!)

"**Reputation**"
- The "Grim-trigger" strategy:
	- Select $C$ in the first period.
	- In later periods, select $C$ if and only if $CC$ was always played previously; otherwise select $D$.
		- If someone deviates, it **triggers** a permanently bad (**grim**) outcome for both players.

So, when is the Grim-trigger strategy a SPNE for both players?
- If $D$ has been chosen at any point, there is an equilibrium point from then on ($DD$).
- In general, if the discount factor is high enough (greater than some value), the conclusion is that neither player will want to deviate from the Grim-trigger strategy. Ergo, it is a SPNE.
	- i.e. if a player cares about having future payoffs, they'll cooperate. If they don't give a damn about the future, they'll defect right away!

### How to Identify when the Grim-trigger is the SPNE
1. Calculate the players' payoff for the scenario where the Grim-trigger is not set off.
	1. Note that we get the payoff = $C *\frac{1}{1-\delta}$.
2. Next, calculate the players' payoff for the scenario where the Grim-trigger is set off immediately (first stage). 
	1. Typically, the player who set off the trigger will have a payoff of (deviation payoff) + (payoff of Grim-trigger SPNE) where the second part of the sum is usually $\frac{D\delta}{1-\delta}$ where $D$ is the payoff of the Grim-trigger SPNE.
3. Set up an inequality and solve for $\delta$.


# Folk Theorem for Repeated Game Theory
A collection of mathematical results that indicate that in a repeated game, if players are very patient, there will be many SPNE that cover a wide range of possible payoffs.
- i.e. there are much more scenarios where players can rationally play unexpected (appears irrational) strategies.

What does this mean?
- When we find the NE of the generic stage game on a graph:
	- Draw lines up and to the right from that point. Shade in the top-right section, and it turns out that every point in this section is a payoff vector of a (Grim-trigger) SPNE.
	- How do we get this supposed strategy? We alternate strategies to create a new sort of strategy for the scenario where the Grim-trigger isn't set off (which subtly messes with the payoff).