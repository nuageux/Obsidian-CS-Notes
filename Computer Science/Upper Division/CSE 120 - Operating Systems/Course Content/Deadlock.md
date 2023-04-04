- There are 4 necessary conditions for deadlock to be *possible* (**not** guaranteed!).
	- Mutual exclusion
		- Only one process may use a resource at a time
	- Hold and wait
		- process hold resource while waiting for another
	- No preemption
		- can't take a resource away from a process
	- Circular wait
		- the waiting processes form a cycle

### How to attack the deadlock problem
- Deadlock prevention
	- make deadlock impossible by removing a condition
- deadlock avoidance
	- avoid getting into situations that lead to deadlock
- deadlock detection
	- dont try to stop them, rather, if they happen, detect and resolve