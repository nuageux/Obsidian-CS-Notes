#Probability #Math 

**In a room with a decent number of people, the probability that two random people in that room will have the same birthday is rather high.**
- Let $N$ be the number of people, let $365$ be the number of days in a year.
- We are trying to find $P(\geq$ 1 collision). Calculating $P($no collisions) is far more trivial, so we calculate that first.
	- See that if we are choosing birthdays from the 365 days, the first one selected can land on any of the 365 days. The second, any *but* the one selected prior. The third, any besides the above two and so on and so forth, until:
		- $P($no collisions) = $\frac{365}{365}*\frac{364}{365}*\frac{363}{365}*\ldots*\frac{365-N+1}{365}=\sum\limits_{n=1}^{N}\frac{365-n+1}{365}$ 
	- $P(\geq$ 1 collision) = $1 - P($no collisions).

#### Examples
- If we plug in some numbers, we find that:
	- If there are 20 people, the probability two random people have the same birthday is 41%.
	- If there are 30 people, the probability is 71%.
	- If there are 60+ people, it’s practically guaranteed.

#### Observations
- Note that the birthday paradox doesn't imply that *you* (or any other *fixed* individual) are likely to have the same birthday as somebody else in a room. 
	- It indicates that *two people selected at random* from a room are likely to share a birthday.