#OS
# Operating Systems
- The operating system refers to the "kernel", the part of the OS that all other programs depend on and that can be accessed via "system calls".
	- In other words, OS is software that makes computers easier to use.
	- The kernel can do exclusive actions such as accessing hardware device registers or responding to hardware interrupts.
	- It furthermore allocates basic resources like CPU time, memory space, and the use of I/O devices.
- The OS "defines the basic laws of physics" of the "computer system universe".
- Consider an "abstract machine"; what the programmer sees and is limited to seeing.
	- The goals of such a concept are *simplicity* and *convenience*.
- "Resources" refers to anything that allows work to get done (something that provides functionality).
	- e.g. memory space, CPU time
	- The goals include: **performance** (speed, efficiency), **reliability** (correctness, fault tolerance), and **security** (privacy, authenticity, integrity).
- The OS "turns the undesirable into the desirable"; the undesirable inconvenience (reality) into desriable conveniences (illusions), i.e. limits are "removed" and masked.
	- What's the Reality?
		- Complexity of hardware
		- A limited number and amount of processors and memory
	- What's the Illusion?
		- Simple resources
		- Unlimited processors and memory
#### Three Key Ideas
- **Abstraction**, **Mechanism**, and **Policy**
	- A: What is the desired illusion?
		- The "abstract machine" provides an interface for the programmer.
	- M: How is this illusion created?
		- Mechanisms are fixed; it works one way and only that way.
	- P: Which way should the M be used, to meet a goal?
		- A policy is variable and depends on the goals of the system.

# Processes
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