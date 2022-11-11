#SQL #Database 
# SQL
- Structured Query Language, pronounced "sequel".
- Parts:
	- **Data-definition language (DDL)**
		- Defines, deletes, and modifies relation schemas.
	- **Data-manipulation language (DML)**
		- Queries info from the database .
		- Inserts, deletes, and modifies tuples in the database.

## Data Definition
- Allows specification of the DB schema.
- Types include:
	- char(n): a fixed-length character string with user-spcified length n.
	- varchar(n): variable-length character.
	- int
	- smallint
	- numeric(p, d): fixed-point number with p digits and d of the p digits are to the right of the decimal.
	- real, double precision
	- float(n) with precision of at least n digits
- Types may have the null value (undesirable).
- Define a relation with the `CREATE TABLE` command.
	- See slides for formatting.
- Delete information of a relation with the `drop table` command.
	- We prefer `delete from [relation]` as it preserves the table itself (but deletes the contained data).
- We add a new attribute (column) with the command `alter table [relation] add [attribute] [type of attribute]`.
	- The new values in the column are filled by null values.

### Integrity Constraints
- NOT NULL
	- Specifies that an attribute does not accept null values
- UNIQUE
	- Specifies that a set of attributes form a candidate key
	- May be null!
- CHECK
	- Enforce a predicate (condition)
	- Can be named
- Referential Integrity
	- We can use PRIMARY KEY, UNIQUE KEY, and/or FOREIGN KEY

## Data Manipulation
- Recall SQL is a declarative query language.
- Starts with relational calculus (first-order predicate logic).
	- Relational algebra follows.

### SQL Queries
- Mainly consists of `select`, `from`, and `where`. See slides for formatting.
	- `where` is basically where the conditionals go, and is an optional clause.
	- When different relations share names for an attribute, we refer to the attribute by preceeding it with the name of the relation it came from (separating with a period).
- We can use "tuple variables" to rename our relations. ...kinda just to save on typing.
- `*` is to select all attributes.
- The `LIKE` keyword is used to express pattern matching conditions.
	- e.g. select * from Movie where Title LIKE 'Ta%'
- The `DISTINCT` keyword is used to eliminate returning duplicate information.
- The `ORDER BY` clause is used to order the display of tuples in the result.
- The `AS` keyword is used to rename attributes in the result.

#### Aggregate Functions
- Operate on the multiset of values of a column of a relation, and return a single value.
- Includes:
	- abg
	- min
	- max
	- sum
	- count

- Grouping allows us to apply the aggregate functions *to subgroups of tuples in a relation*.
	- The `GROUP BY` clause divides the tuples in the from clause into groups. 
- The `HAVING` clause is for when we want to retrieve the values of aggregate functions for only those groups that satisfy certain conditions.
	- We use this with *groups*.

#### Nesting
- We can... nest queries. Weird, but see slides for formatting.
- Queries involving *nesting but no negation* can always be *unnested*, in contrast to queries *with nesting* **and** *negation*.
- Two queries are said to be "correlated" if a condition in the WHERE clause of a nested query references an attribute of a relation declared in the outer query.
