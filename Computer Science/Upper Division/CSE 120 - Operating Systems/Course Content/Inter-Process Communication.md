#OS 
# IPC
## Cooperating Processes
- Why structure a computation as a set of cooperating processes?
	- For performance and speed, allowing us to exploit inherent parallelism of compuation and allowing some parts to proceed while others depend on I/O.
	- For modularity, to create reusable, self-contained programs.
		- Each of which may do a useful task on its own, or may be useful as a sub-task for others.
- Examples of cooperating processes are pipelines, client/server relationships, parent/child relationships, etc.
- We will examine the producer/consumer problem.

### Shared Memory + Semaphores
- Shared memory to communicate, semaphores to prevent the race conditions.

### Monitors
- A progamming language construct for IPC.
	- Variables are shared but are only accessable in a very controlled way.
	- Accessed via procedures (mutex)
	- Condition variables (general syncing)
		- *There is no memory for condition variables!*
- Only one process can be active inside a monitor.
- Consider the monitor "house" blueprint!
	- There is an entry door, which is open if no processes are *active* within the monitor.
	- This door closes when a process enters.
	- This door will reopen when a process exits (through an exit-only door) or the process in the active area waits *and no process in the waiting area is signalled*.
		- Note that when the active area process signals the waiting area, the signalling process must exit immediately.
- When using monitors, the signal must happen *just before returning*!
- Because condition variables have no memory, a signal without a corresponding wait is "lost"!

### Message Passing
- What is used today.
- `send (destination, &message)` and `receive (source, &message)`
- Data transfer into and out of kernel "message buffers".
	- Buffers are a "temporary holding area".
	- The synchronization required is that the receiving block must wait on the sending message.
- Does not utilize shared memory!
- An "asynchronous send" and a "synchronous receive" is the most common paradigm.
	- i.e. sender does not block, but the receiver *does* block (since it shouldn't continue until it has the information it needs).
- "Flow control" by limiting the number of messages in transit.
	- This is implemented by adding in another send-receive from consumer to producer.
- To fix some issues:
	- Messages should be addressed to "ports" rather than processes to support a wider network.
	- Processes should receive from anyone.
	- Outstanding messages?
- It is a good paradigm for IPC over networks and is safer than shared memory paradigms (since one process cannot affect the memory of another process).