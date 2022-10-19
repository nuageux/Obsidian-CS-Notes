#Theoretical 
# Decidability
 Note that showing that a language is decidable is the same as showing that the [[Classes of Computational Complexity|computational problem is verifiable]].
## For Regular Languages
**Testing whether**
- A finite automaton accepts a string:
	- Define the language $A_{DFA}$ which contains all the encodings of all DFAs paired with strings the respective DFA accepts.
	- $A_{DFA}$ *is a decidable language*.
		- This proof is simple. Construct a TM $M$ that:
			- Verifies that $B$ is a valid DFA.
			- Simulates $B$ on input $w$.
			- If the simulation ends in an accept state, *accept*. If it ends in a nonaccepting state, *reject*.
	- $A_{NFA}$ is also simple from here. Construct TM $N$ that:
		- Converts the NFA to a DFA, then runs $M$ from above.
	- $A_{REX}$ is a decidable language. Construct TM $R$ that:
		- Converts the regular expression $R$ to the equivalent NFA, then runs $N$ from above.
	- $E_{DFA}$ is a decidable language. the empty language.
	- $EQ_{DFA}$ is a decidable language. Determines whether two DFAs recognize the same language.
- A language of a finite automaton is empty:
- Two finite automata are equivalent:

### For Context-Free Languages

Some problems are **unsolvable**, and we refer to these problems (read: languages) as [[Undecidability|Undecidable]]. 