#Model
# DFA Formal Definition

^ccb750

A 5-tuple $(Q, \Sigma, \delta, q_0, F)$ where
- $Q$ is a finite set called the "states",
- $\Sigma$ is a finite set called the "alphabet",
- $\delta: Q \times \Sigma \rightarrow Q$ is the transition function,
	- Which we can use a table to describe
	- For NFA's, $\delta: Q \times \Sigma_{\varepsilon} \rightarrow \mathcal{P}(Q)$ (a combination of states, since we can nondeterministically branch to multiple different states)
- $q_0 \in Q$ is the start state, and
- $F \subseteq Q$ is the set of accept states. 

## Key Concepts
If we consider the generic string $w = w_1w_2w_3...w_n$ where each $w_i \in \Sigma$ and we have a DFA $M$ with the generic definition as specified above, $M$ *accepts* $w$ if a sequence of states $r_0, r_1, ..., r_n$ (where $r_i \in Q$) exists such that
- $r_0 = q0$,
	- i.e. the DFA starts at the start state
- $\delta(r_i, w_{i+1}) = r_{i+1}$ for $i = 0, 1, ..., (n-1)$, and
	- i.e. the states move according to the machine's transition function; in other words, follows the arrows in the DFA diagram
	- For NFA's: $r_{i+1} \in \delta (r_i, y_{y+1})$ for $i = 0, 1, ..., (n-1)$, generating potentially more than one state(!)
- $r_n \in F$.
	- i.e. $r_n$ is an accept state

$M$ **recognizes** "*language*" $A$ if $A = \{w\hspace{.25cm} | \hspace{.25cm} M$ accepts $w\}$.
- i.e. if $A$ is the collection of all the strings that $M$ can accept.

A language is **regular** *iff* there is some finite automaton that recognizes *exactly* it.
- Note that to prove this statement (as indicated by the "*if and only if*"), a bidirectional proof is necessary: ^8a2318
	- Proof of Construction (if the language has this property, prove that the machine exists), where the formal definition is specified.
		- A state diagram is often used to describe the transition function.
	- Proof of Correctness (if the machine exists, prove that it recognizes exactly the language), where the machine is proven to cover all $w \in A$.

## Regular Operations
Regular languages are closed under (but not limited to) the following operations:
- **Complementation**: $A^c=\{w: w \notin A\} = \{w: \delta^*(q_0,w) \notin F\}$ 
- **Union**: $A \cup B = \{x \mid x \in A$ or $x \in B \}$ 
	- The state diagram is constructed by creating an NFA with a new initial state that has $\varepsilon$ transitions to the initial states of $M_A$ and $M_B$.
- **Concatenation**: $A \circ B = \{xy \mid x\in A$ and $y \in B \}$
	- The state diagram is constructed by creating an NFA where the accept states of $M_A$ have $\varepsilon$ transitions to the initial states of $M_B$.
- **Kleene Star**: $A^* = \{x_1x_2...x_k \mid k \geq0$ and each $x_i \in A \}$
	- The state diagram is constructed by creating an NFA with a new accepting initial state which has an $\varepsilon$ transition to the initial state of $M_A$ and putting $\varepsilon$ transitions from the accept states of $M_A$ to the initial state of $M_A$.

That is to say, using the above operations on regular languages results in another regular language.

## How to Construct a DFA from an [[Nondeterministic Finite Automata (NFA)|NFA]]
1. If the NFA has $n$ states, create $2^n$ states for the DFA (as the power set has $2^n$ members by definition). Remember that one of these states is the trap state $\emptyset$.
2. Mark every state that contains an accept state from the NFA as an accept state also.
3. Trace through the NFA. Remember that $\varepsilon$ means to trace again when encountered.
4. Eliminate all states without any ingoing arrows.