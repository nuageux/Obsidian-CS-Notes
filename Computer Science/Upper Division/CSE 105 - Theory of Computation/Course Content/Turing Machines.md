#Model #Theoretical 
# Turing Machines
First proposed by Alan Turing in 1936.
- A theoretical model where we have a computer with unlimited and unrestricted memory.
- This model allows us to say what sorts of problems are beyond the theoretical limits of computation.

Turing machines are different from finite automata in that:
1. A Turing machine can both write on the tape and read from it.
2. The read-write head can move both to the left and to the right.
3. The tape is infinite.
4. The special states for rejecting and accepting take effect immediately.
- An inifinite automata?

## Formal Definition
Usually not practical to write out in most cases (description is usually prohibitively long).

A Turing machine is a 7-tuple, $(Q, \Sigma, \Gamma, \delta, q_0, q_{accept}, q_{reject})$, where $Q, \Sigma, \Gamma$ are all finite sets and
1. $Q$ is the set of states, 
2. $\Sigma$ is the input alphabet *not* containing the ***blank symbol*** $\sqcup$, 
3. $\Gamma$ is the tape alphabet, where $\sqcup \in \Gamma$ and $\Sigma  \subseteq \Gamma$, 
4. $\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{L, R\}$ is the transition function, 
5. $q_0 \in Q$ is the start state, 
6. $q_{accept} \in Q$ is the accept state, and 
7. $q_{reject} \in Q$ is the reject state, where $q_{reject} \neq q_{accept}$.

The Turing machine will record the input $w$ on the leftmost squares of the tape, and the rest of the tape is blank (symbols), then starts on this leftmost square.
- Note that $\Sigma$ doesn't contain the blank symbol, so the first blank on the tape marks the end of the input.
- If the machine is at the leftmost square of the tape and tries to move off left, the head doesn't move and stays at the leftmost square.
- The computation goes on until reaching an accept or reject state. Otherwise, it goes on forever.

A **configuration** of a Turing machine includes the current state, the current tape content, and the current head location.
- It is represented by $uqv$, where $u$ is the preceding section of the tape, $q$ is the current state (and thus isn't recorded on the tape) and the head (a.k.a. pointer), which is situated right before $v$, the succeeding section of the tape.
- Configuration $C_1$ *yields* $C_2$ if the Turing machine can legally go from $C_1$ to $C_2$ in a single step.
- The start configuration is $q_0w$, where $w$ is the input string.

Turing machine $M$ **accepts** input $w$ if a sequence of configurations exists such that
1. The first configuration is $q_0w$, 
2. Each configuration yields the next, and 
3. The last configuration is an accepting configuration.

The collection of strings that $M$ accepts is (like the others) called the **language** of $M$ or the "language recognized by $M$", denoted by $L(M)$.
- A language is "**Turing-recognizable**" if some Turing machine recognizes it.

Turing machines *accept*, *reject*, or *loop* (doesn't halt).

A Turing machine that *does* halt on any and all inputs (never loops) is a "**decider**", and a language is called "[[Decidability|Turing-decidable]]" if some Turing machine decides it.
- It should be obvious that *all decidable languages are also Turing-recognizable*.

## How to read the transition function $\delta$
Read $\delta(q_i, b) = (q_j, c, R)$ as "when we are at $uaq_ibv$, change $b$ to $c$, then shift $q_i$ to the $R$ight, then change state $q_i$ to $q_j$ (to get $uacq_jv$)", where $u$ and $v$ represent the ends of the tape (the contents of which is unnecessary to know).
- Note that whatever is in front of the state in the configuration is what is modified at each step, **then** we move the state/head.
- For $\delta(q_i, b) = (q_j, c, L)$, notice how the configuration $uaq_ibv$ yields $uq_jacv$.
- Left-hand end special case:
	- Move left (off the edge?!): $q_ibv$ yields $q_jcv$ (where the variable at the tape changes but not the head position).
- Right-hand end notation:
	- Note that $uaq_i$ is equivalent to $uaq_i\textvisiblespace$, because blank space represents the infinite nature of the right-hand side of the tape. 
- The state diagram follows similar logic.
	- The transition $0 \rightarrow x, R$ represents when changing states, replace $0$ with $x$ and then shift the iterating head $R$ight.
	- $x \rightarrow R$ is shorthand for "if reading $x$, no replacement of tape necessary, but shift $R$ight."

## [[Turing Machine Variants]]
There are different ways to represent Turing Machines, but they all have the same power/functionality as the one described above.
- To show that two models are equivalent, we only need to show that one can simulate the other.


### The Church-Turing Thesis
The intuitive notion of algorithms being equivalent to algorithms described by a Turing-machine.



