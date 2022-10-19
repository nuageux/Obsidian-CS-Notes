#Proof #Theoretical 
# Undecidability
## Diagonalization
## Turing-Unrecognizable Language
Let us show that the set of all Turing machines is countable.
- Note that the set of all strings for any alphabet is countable, by forming a (inherently finite) list of strings for length 1, then length 2, and so on.
	- Since all Turing machines can be encoded into a string somehow (that uses a certain, shared language), it follows that we can obtain a countable list of all Turing machines.
- However, it is more important to observe that the set of all *languages* is uncountable.
	- First, observe that the set of all infinite binary sequences is uncountable.
		- Let $\mathcal{B}$ be the set of all infinite binary sequences. It is uncountable, much like how real numbers are uncountable.
		- Let $\mathcal{L}$ be the set of all languages over alphabet $\Sigma$.
		- Let us set up a correspondence with $\mathcal{B}$ (showing that $\mathcal{L}$ is also uncountable!).
			- Show that by encoding language $A \in \mathcal {L}$ into its characteristic (binary) sequence, we can map every unique language into its unique binary string, clearly showing an injective and surjective relationship.

Since the set of all Turing machines is countable but the set of all languages is uncountable, we can only conclude that some languages are not recognized by Turing machines.

### Examples of Undecidable Languages.
Language $A_{TM}$ is undecidable.
- Assume that $A_{TM}$ *is* decidable. Suppose we have TM $H$ that is a decider for $A_{TM}$.
	- So, given an input $\langle M, w \rangle$, $H$ will always halt.
- Next, construct TM $D$, which takes one input, a TM $M$.
	- $D$ runs $H$ with input $\langle M, \langle M \rangle \rangle$, then outputs the opposite of what $H$ outputs.

## Proof of Undecidability by Reduction
