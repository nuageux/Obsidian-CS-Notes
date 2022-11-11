#Data-Science #Design #Database
# Database Management Systems (DBMS)
## Top-Level Goals / Purpose of DBMSs
## Core Database Issues
- Data Models & Query Languages
	- Models are a way to *logically* represent data, without considering any of the physical implementation.
	- Includes:
		- Relational Model, which uses a collection of tables to represent data and the relationships among data.
			- Tables are also known as **relations**.
			- Is a *record-based* model. Each record type defines a fixed number of fields, a.k.a. **attributes**.
		- Entity-Relationship
		- Object-Eelational
		- XML
	- **SQL** is a query language for relational databases.
		- Is declarative (non-procedural), meaning that you specify the desired result but not how to compute it.
- Database Design
- Query Processing
	- Parsing & Translation
	- Optimization
	- Evaluation
	- It is the black box. The optimizer wants to make a guess of the most efficient method without actually running all the methods to compare.
- Storage Management
	- A module that provides the interface between the low-level data and the apps and queries provided to the system.
- Transaction Management
- Concurrency Control

## Database Architecture
Is influenced by the underlying computer system on which the database is running.
- Centralized
	- Applicable to shared-memory server architectures, which have multiple CPUs and use parallel processing but access a common shared memory.
- Distributed
	- Allows data storage and query processing across multiple geographically separated machines.
- Parallel Multi-Processor
	- Map-Reduce