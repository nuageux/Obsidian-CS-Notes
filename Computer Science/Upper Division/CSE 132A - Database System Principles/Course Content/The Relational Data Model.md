# Relational Model
 - Consists of a collection of tables, each assigned a unique name.
	- Tables are called **relations**. ^40a3c5
	- Consider a **tuple**, an unordered sequence of values, which refers to a row in a relation.
		- See slides for tuple notation.
	- **Attributes** refer to columns.
		- There is a set of permitted values, the **domain**.
			- A domain is **atomic** if elements are discrete, mathematical units.
			- Null values exist in relational models, but we wish to avoid them if possible.
- A **relation instance** refers to a specific instance of a relation, containing a specific set of rows.

## Database Schema
- The logical design of the database.
	- Programming Analogy: If relations are variables, relation schemas are types.
		- So, **relation schemas** consist of a list of attributes and their corresponding domains.
		- e.g. `CUSTOMER(CustUD, Name, Street, City)`
- A **database instance** is a snapshot of the data in the DB at a given instance in time.
- We don't store all the info as a single relation because it results in repetition of information and the need for null values. We prefer to separate data into multiple relations instead.

### Keys
- Are used to uniquely identify tuples (rows).
- A **superkey** is a set of one or more attributes (columns) that allow us to uniquely identify a tuple in a relation.
	- Formally, we let $R$ denote the set of attributes in the schema of relation $r$.
		- If we say that a subset $L$ of $R$ is a superkey for $r$, then
			- if $t_1$ and $t_2$ are in $r$ and $t_1 \neq t_2$, then $t_1.K \neq t_2.K$.
	- For all tuples in our superkey subset, they are unique.
	- Note that logically, if $K$ is a superkey, so is any superset of $K$.
		- We want superkeys for which no proper subset is a superkey, called **candidate keys**.
			- In other words, the smallest possible superkey set.
	- We call the candidate key chosen as the main method of identification the **primary key**.
		- It is common notation to put the primary key first in the tuple. They are also underlined.
		- Should be chosen such that its attribute values rarely change.
			- e.g. a person's address is a bad choice, as it changes not uncommonly. Social Security Numbers, however, do not, so are a good choice.
- Note that keys are are properties of the entire relation, not just of the individual tuples.
- A **foreign-key constraint** ensures that all values in a tuple are valid entries.
	- Formally, a foreign-key constraint from attribute(s) $A$ of relation $r_1$ to the primary-key $B$ of relation $r_2$ states that on any DB instance, the value of $A$ for each tuple in $r_1$ must also be the value of $B$ for some tuple in $r_2$.
		- $A$ is the foreign key from $r_1$.
		- $r_1$ is the **referencing relation** and $r_2$ is the **referenced relation**.
- A **referential integrity constraint** requires that the values appearing in specified attributes of any tuple in the referncing relation also appear in specified attributes of at least one tuple in the referenced relation.
	- i.e. preventing "dangling references"
- The **entity integrity constraint** specifies that the primary key attributes of each relation scheme cannot have null values in any tuple!