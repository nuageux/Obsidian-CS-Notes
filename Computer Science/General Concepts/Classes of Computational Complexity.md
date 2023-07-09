#Theoretical 
What if we wanted to describe the (time/space) complexity of a **problem**, irregardless of the algorithms we may or may not use as a solution?

# Classes of Computational Complexity
There are 4 main classes of computational complexity:
- **P**: Problems that can be **solved** in $O(n^c)$ (***polynomial*** time)
- **NP**: Problems that can be **verified** in $O(n^c)$
	- Given an answer, we can see whether it's a valid or invalid answer in polynomial time.
	- Note that **P** is a subset of **NP**; we can solve a problem and compare answers to the solution to verify their legitmacy.
- **NP-Hard**: Problems that are *at least as hard as the hardest problem* in **NP**
- **NP-Complete**: The intersection of **NP** and **NP-Hard**
	- i.e. the hardest problems that we can still verify. **NP-Hard** might include unverifiably difficult problems (in polynomial time).
# P vs. NP
The statement above refers to the currently unsolved (Millenium Prize!) problem that asks whether $P$ is the same as $NP$, i.e. "are all verifiable problems also solvable"?

$P \neq NP$ means that there is likely no overlap between $P$ and $NP$-Complete; i.e. just because a problem is verifiable in polynomial time does not imply that it is also solvable in polynomial time.
- This is the more likely scenario.
- Implies that for incredibly difficult problems, no (reasonable) solution may exist.
- Implies that our current methods of cryptography are robust and can continue to be used securely. Postive.
- Implies that we may never solve very complex biological or medical problems. Negative.

$P = NP$ means that all verifiable problems are also solvable, implying that all $NP$-Complete problems are solvable in polynomial time.
- Has the opposite implications as those for $\neq$.

Whichever turns out to be true, the impact on the world will be massive.