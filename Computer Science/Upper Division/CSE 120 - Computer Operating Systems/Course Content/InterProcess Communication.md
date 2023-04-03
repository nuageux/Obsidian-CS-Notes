#OS 
# IPC
## Cooperating Processes
- Why structure a computation as a set of cooperating processes?
	- For performance and speed, allowing us to exploit inherent parallelism of compuation and allowing some parts to proceed while others depend on I/O.
	- For modularity, to create reusable, self-contained programs.
		- Each of which may do a useful task on its own, or may be useful as a sub-task for others.
- Examples of cooperating processes are pipelines, client/server relationships, parent/child relationships, etc.

### Monitors
- A progamming language construct for IPC.
	- Variables are shared but are only accessable in a very controlled way.
	- Accessed via procedures (mutex)
	- Condition variables (general syncing)
- Only one process can be active inside a monitor.

### Message Passing
- What is used today.
- "send" and "receive" data transfer into and out of kernel message buffers.
	- The synchronization required is the receiving block must wait on the message.
- No shared memory!