#Theoretical 
# Regular Expressions
$R$ is a regular expression if $R$ is any of the following:
- $a$ for some $a\in\Sigma$
- $\varepsilon$
- $\emptyset$ (the empty language)
- $(R_1 \cup R_2)$, where $R_1$ and $R_2$ are regular expressions
- $(R_1 \circ R_2)$, where $R_1$ and $R_2$ are regular expressions
- $(R_1^*)$, where $R_1$ is a regular expression

The **operator precedence rules** state that $^*$ precedes $\circ$ which precedes $\cup$, unless parentheses group them elsewise.

$R^+$ is shorthand for $RR^*$, the key point being that it does not include the empty string, while Kleene Star does.

$L(R)$ is defined to be the *language* of $R$, and furthermore, a language is regular *[[Deterministic Finite Automata (DFA)#^8a2318|iff]]* some regular expression describes it.
- To prove, construct the regular expression, then prove that the regex made covers all strings in the language.

### Intuitive Identities
- $R^k$ is shorthand for the concatenation of $k$ $R$’s with each other.
- Concatenating $\emptyset$ to any set yields $\emptyset$.
- $\emptyset ^*= {\varepsilon}$, because *Kleene Star always adds the empty string to any set*.
- $R \cup \emptyset = R$ (but $R \cup \varepsilon$ does not necessarily equal $R$).
- $R \circ \varepsilon = R$ (but $R \circ \emptyset$ does not necessarily equal $R$ (see second bullet)).

### How to Convert a [[Deterministic Finite Automata (DFA)|DFA]] into a Regular Expression
Using the $q_{rip}$ state method:
1. Construct the Generalized NFA by adding a new start state with an $\varepsilon$ transition to the old start state and a new accept state with $\varepsilon$ transitions coming in from the old accept states.
	- If any arrows in the DFA had multiple labels, we replace these with a single arrow whose label is the union of the previous labels.
	- Arrows labeled with $\varepsilon$ are added but may be omitted for clarity's sake.
2. The idea is to continuously remove states and reconstruct labels **until only the newly added initial and accept states are left, connected by one arrow labeled by our regular expression**.
	- Mark a state from the old DFA as $q_{rip}$, then if:
		- $q_i$ goes to $q_{rip}$ with an arrow labeled $R_1$, 
		- $q_{rip}$ goes to itself with an arrow labeled $R_2$, 
		- $q_{rip}$ goes to $q_j$ with an arrow labeled $R_3$, and/or
		- $q_i$ goes to $q_j$ with an arrow labeled $R_4$, then...
	- ...the new arrow from $q_i$ to $q_j$ gets the label $(R_1)(R_2)^*(R_3)\cup(R_4)$.
		- Note that the pattern is the non-relevant transitions are unioned with the relevant transition, where the regex is concatenated sequentially and the self-loops on $q_{rip}$ are Kleene Star'ed.
3. Repeat.