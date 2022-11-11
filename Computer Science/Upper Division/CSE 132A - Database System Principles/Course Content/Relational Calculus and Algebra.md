#Math #Database 
# Relational Calculus
- Models data manipulation core of SQL, specifying the "what" (but not the "how").
- General form: $\{t \space | \space property(t)\}$, where the property is described by a language based on predicate calculus (a.k.a. first-order logic).
- To say that "tuple $m$ is in relation $R$", you'd write $m \in R$.
- Let's say we want to find the directors and actors of currently playing movies...
	- $$\{t: director, actor \space | \space \exists m \in Movie \space\exists s \in Schedule \space [t(director) = m(director) \land t(actor) = m(actor) \land m(title) = s(title)] \space \}$$
	- Note that the beginning section is the `SELECT` clause, the middle the `FROM`, and the last the `WHERE`.
- We are allowed to use both the existential *and* universal quantifier in relational calculus!
	- Order matters though: see slide 23.
- Recall the "if-then" operator ("if $p$ then $q$").
- **"Free variables"** are not in the scope of any quantifier. 
- i.e. the moment we specify that a variable is in a relation (such that... [something]), it is no longer free.
	- If a statement evaluates to either true or false, all the variables are free. Hence if the statement returns a set, then at least one of the variables is not free.
- The *active domain* is a set of values that are either in the database or mentioned in the query result.
	- Tuple variables "range over the active domain".
- When translating to SQL, the basic rule is to introduce one level of nesting for each "doesn't exist".

# Relational Algebra
- Is a simple set of algebraic operations on relations.
- The basic ones are as follows:
	- $\pi_X(R)$ indicates to display only attributes $X$ of relation $R$.
		- Note that $\pi$ is like $\exists$.
	- $\sigma_{cond}(R)$ indicates to select tuples of $R$ satisfying the condition.
	- $R \cup S$ indicates the union of sets of tuples in $R$ and $S$.
	- $R-S$ indicates the difference of sets of tuples in $R$ and $S$.
	- $R \bowtie S$ indicates the natural join of $R$ and $S$.
	- $\delta_{A_1 \rightarrow A_2}(R)$ indicates to change the name of attribute $A_1$ in $R$ to $A_2$.
- Some other useful operations:
	- $R \times S$ is the Cartesian Product of $R$ and $S$.
		- Note that when $R$ and $S$ have no common attributes, the Cartesian Product is equivalent to the natural join.
		- If there is a shared attribute name between $R$ and $S$, they are renamed.
	- $R \cap S$ indicates the intersection of sets of tuples in $R$ and $S$.
	- $R \div S$ indicates the division (quotient) of two sets $R$ and $S$.
		- Specifically, using the shared relations between $R$ and $S$, the operation returns all distinct tuples from the unshared attributes in $R$ such that the tuple existed in $R$ with all tuples in $S$.
		- Note that this requires that $a \space | \space <a, b>\space \in R \space for \space every \space b \in S$.
		- Note that $\div$ is like $\forall$ .

**Conclude that Relational Calculus and Relational Algebra are Equivalent.**