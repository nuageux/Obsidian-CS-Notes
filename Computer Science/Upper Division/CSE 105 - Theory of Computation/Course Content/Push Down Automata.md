#Model 
## What is it?
A Pushdown Automaton is like an [[Nondeterministic Finite Automata (NFA)|NFA]] but has a **stack** at its disposal to use. This, in effect, gives our model some "memory" for use.
- The PDA accepts an input string based on whether the stack meets certain conditions.
- Note that we use an NFA because it gives us the power to prove a language being context-free.

A language is [[Context Free Grammar|context free]] *[[Deterministic Finite Automata (DFA)#^8a2318|iff]]* a PDA recognizes it (with all of the same implications for a bidirectional proof).

## Formally
A pushdown automaton is a 6-tuple $(Q, \Sigma, \Gamma, \delta, q_0, F)$ where $Q, \Sigma, \Gamma,$ and $F$ are all finite sets, and
- $Q$ is the set of states, 
- $\Sigma$ is the input alphabet, 
- $\Gamma$ is the stack alphabet, 
- $\delta: Q \times \Sigma_{\varepsilon} \times \Gamma_{\varepsilon} \rightarrow \mathcal{P}(Q \times \Gamma_{\varepsilon})$ is the transition function, 
- $q_0 \in Q$ is the start state, and
- $F \subseteq Q$ is the set of accept states.

The PDA always starts with an empty stack and can only accpet with an empty stack. The PDA moves according to the current state, input symbol, and stack symbol.

### How to Read the Transition Function
$a, b \rightarrow c$ signifies that when the machine is reading input $a$, it must replace the symbol $b$ which must be at the top of the stack with a $c$. Otherwise, the current branch of nondeterminism dies.

**Common Notation**
- $\varepsilon, \varepsilon \rightarrow \$$ is the most common way to initialize the stack by marking the bottom of the stack with a $\$$.
- $\varepsilon, \$ \rightarrow \varepsilon$ is the most common way to check if we are done reading input, by nondeterministically guessing we are at the bottom of our stack, popping $\$$ to confirm this.
- $\varepsilon, \varepsilon \rightarrow \varepsilon$ indicates a nondeterministic guess without changing anything.

- $a, \varepsilon \rightarrow c$ indicates to push $c$ onto the stack when reading the input $a$.
- $a, b \rightarrow \varepsilon$ indicates to pop $b$ off of the stack when reading input $a$, else, the current branch dies.

- $a, \varepsilon \rightarrow \varepsilon$ indicates to read input $a$ but ignore the stack.
- $\varepsilon, b \rightarrow \varepsilon$ indicates to nondeterministically pop $b$'s off the stack (without reading anything).
- $\varepsilon, \varepsilon \rightarrow c$ indicates to nondeterministically push $c$'s onto the stack (without reading anything).