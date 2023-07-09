#OS
- The most basic kernel function is to run a program. Following this train of thought, the user will want the ability to run multiple programs simultaneously. 
	- ...this isn't possible! But how can we create an illusion as if it is?
- Introducing the **process**, an abstraction of a running program. 
	- It is a program in **execution**.
	- A process is *dynamic*, it has states and changes as time passes.
		- A program, on the other hand, is static.
- The basic resources for a process are:
	- The CPU
		- processing cycles (time)
		- to execute instructions
	- Memory
		- bytes or words (space)
		- to maintain states
	- etc.
- The **context** of a process is the machine and kernel-related state.
	- The CPU context is the values of the registers.
		- e.g. the PC is the **program counter**, the SP is the **stack pointer**, the FP is the frame pointer, etc.
	- The memory context refers to pointers to memory areas.
		- The areas are:
			- Text
				- The literal code/text files.
			- Data
				- Global variables and the heap, which is dynamically allocated.
			- Stack
				- Contains "activation records" and automatically grows and shrinks.
- The goal is to **support multiple processes**.
	- Not all processes will actively use the CPU.
	- Some are waiting for input, devices, etc.

### Multiprogramming
Given a running process:
- At some point, it will need a resource.
- If that resource is busy, the process can't proceed.
- Thus, the process will "voluntarily" give up the CPU resource to another process.

Consider the **"Yield"** (p) function.
- It is a kernel call.
- "Let process p run (voluntarily)"!
- Requires context switching.
	- The ability to save the context of the current process and to restore the context of another process that we want to yield to that we now want to run.
- The code for Yield is put in the kernel, and so are the process contexts.
	- This way they are "protected".

### Context-Switching
- It is allocating CPU from one process to another.
- First save the context of the currently running process.
- Next, restore (load) the context of next process to run.
	- Load the general registers, stack pointer, etc.
	- Load the program counter. This must be done last.
- Switch text and data.
- Switch stacks. Note that the PC is still in the middle of Yield.
- Context-Switching is then the *mechanism* that reassigns CPU between processes.

So, the kernel is code that supports processes and runs as an extension of the current process. It has text, data, and multiple stacks.

See the *extensive* example within the lecture slides.