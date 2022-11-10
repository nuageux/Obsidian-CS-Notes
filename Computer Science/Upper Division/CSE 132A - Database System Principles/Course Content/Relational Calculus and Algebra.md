# Relational Calculus
- Models data manipulation core of SQL, specifying the "what" (but not the "how").
- General form: $\{t \space | \space property(t)\}$, where the property is described by a language based on predicate calculus (a.k.a. first-order logic).
- To say that "tuple $m$ is in relation $R$", you'd write $m \in R$.
- Let's say we want to find the directors and actors of currently playing movies...
	- $\{t: Director, Actor \}$ 