#Database #Data-Science 
# Query Processing
- The query processor turns user queries and data modificaiton commands into a *query plan*.
	- A sequence of operations (or algorithm) on the database, from high-level queries to low level commands.
- Types of decisions that the query processor takes include:
	- Which of the algebraically equivalent forms of a query will lead to the most efficient algorithm?
	- For each algebraic operator what algorithm should we use to run the operator?
	- How should the operators pass data from one to the other? (e.g. main memory buffers, disk buffers)

### Drawing an Execution Plan
- Drawn like a **tree**, traversing *bottom-up*!
	- Because nested entries are children of another entry (its parent).
- **Scan & Fly** method:
	- Scan from the tables and output anything that satisfies the given conditions on the fly.
		- Scan $R$.
		- For each tuple $r$ of $R$ scan $S$.
		- For each $(r, s)$, where $s$ in $S$, select and project on the fly.
	- It is the default plan.
- **Hash Join** method:
	- Using natural join...
		- Scan $R$ & $S$.
		- Perform on the fly selections.
		- Do a hash join.
		- Project.
	- Notice how this cuts out most of the Cartesian Product from before.
- **Right Index Join** method:
	- We create and use*indices* $R_A$ and $S_C$.
		- Use $R_A$ index to select $R$ tuples with $R_A$ = "c".
		- For each $R_C$ value found, use the $S_C$ index to find matching join tuples.
		- Eliminate join tuples $S_E \neq 2$.
		- Project $B, D$ attributes.