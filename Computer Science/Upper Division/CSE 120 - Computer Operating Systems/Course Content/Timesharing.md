#OS 
- Timesharing is the multiplexing use of CPU over time.
	- There are multiple processes but only a single CPU (in a uniprocessor model).
	- Conceptually, each process makes progress over time.
	- In reality, each periodically gets "quantum" (the smallest fixed unit of time allocated) of CPU time.
	- The illusion of parallel progress is achieved by rapidly switching the CPU.

### Implementation
- The kernel keeps track of progress of each process.
	- Characterizations are as such:
		- Running: actually making progress, using the CPU
		- Ready: able to make progress, but not using the CPU
		- Blocked: not able to make progress, can't use the CPU
- So the kernel selects a ready process and lets it run.
	- When the kernel gets back control, it selects another ready process.
- There are state transitions:
	- Dispatch: allocates the CPU to a process
	- Preempt: takes the CPU away from a process
	- Sleep: process gives up CPU to wait for an event
	- Wakeup: event occurred, makes the process ready
- We don't want one process to run forever and hog all the resources.

### Process vs Kernel
- The kernel is code that supports processes, such as:
	- system calls like fork(), exit(), etc.
	- management, such as context switching, scheduling, etc.
- The kernel runs when a system call or **hardware interrupt** occurs.
- The kernel runs as a part of the running process.
- The kernel maintains a list of processes in a table.
	- Has the PID, the process states, the contents of CPU contexts, areas of memory being used, reasons to be blocked, etc. 

### Kernel Receiving Control
- A process can give up control voluntarily.
	- A system call that blocks, like read(), is called.
	- Then yield() is called to give up the CPU.
	- Then the kernel will select a ready process and dispatch it.
- The CPU can be forcibly taken away... "preemption"
	- An interrupt may have been generated when a hardware timer expired.
	- That interrupt will force control to the kernel.
	- While the kernel runs, it resets the timer for the next hardware interrupt.

#### How a Context Switch Occurs
- The process makes a system call or interrupt occurs.
- The hardware switches from user to kernel mode ("amplifying power" by allowing more types of instructions to be available and for kernel memory to be available) then goes to a fixed kernel location to trap/interrupt the handler.
- The software saves the context, selects a ready process and restores that process's context, then RTIs (returns from the trap/interrupt and "reduces power" by switching back to user mode).

## Threads
- A single, sequential path of execution.
- This abstraction is independent of memory (in contrast to a process, which has a path of execution AND memory).
- A thread *is part of a process*.
	- It lives in the memory of a process, and this distinction allows multiple threads in a process.
- To the user, this is a unit of parallelism. *To the kernel*, it's **a unit of schedulability**.
	- The smallest thing I can assign to a CPU.

#### Implementation
- Thread calls are system calls.
	- e.g. ForkThread(), like Fork(), but for threads.
- Thread management functions are in the kernel.
- Each thread requires a user and kernel stack.
	- Because each thread may independently call functions.
- The kernel can schedule threads on separate CPUs.

### User-Level Threads
- They are introduced via a thread library.
- Thread calls then happen at a user level, and so does the thread management.
- This way, threads are supported regradless of kernel support. *But*, this isn't "true" parallelism.
	- This is because if the kernel doesn't know what threads are, it can't schedule different threads on different CPUs.