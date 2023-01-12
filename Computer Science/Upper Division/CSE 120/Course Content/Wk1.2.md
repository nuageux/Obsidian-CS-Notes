- the operating system refers to the "kernel", the part of the OS that all other programs depend on and that can be accessed via "system calls"
	- so OS is software that makes computers easier to use
	- kernel can access hardware device registers, can respond to hardware interrupts
	- allocates basic resources like cpu time, memory space, and the use of i/o devices. 
- the OS "defines the basic laws of physics" of the "computer system universe".
- "abstract machine" what the programmer sees and is limited to seeing
	- goals: simplicity and convenience
	- the target is the programmer
- manage resources, anything that allows work to get done (something that provides functionality)
	- ex: memory space, cpu time
	- "manage"
	- goals: performance (speed, efficiency), reliability (correctness, fault tolerance), security (privacy, authenticity, integrity)
- "turns the undesirable into the desirable", the undesirable inconvenience (reality) into desriable conveniences (illusions). i.e. limits are "removed" and masked.
	- reality
		- complexity of hardware
		- limited number and amount of processors and memory
	- illusion
		- simple resources
		- unlimited processors and memory
- abstraction, mechanism, and policy
	- A is the what is the desired illution?
		- the abstract machine provides an interface for the programmer
	- M is how is this illusion created?
		- mechanisms are fixed; it works one way and only that way.
	- P is which way should the M be used, to meet a goal?
		- a policy is variable and depends on the goals of the system

# Processes
- are an abstraction of a running program. "a program in **execution**"
	- it's dynamic, has states and changes as time passes
	- a program on the other hand is static
- basic resources for processes
	- cpu
		- processing cycles (time)
		- to execute instructions
	- memory
		- bytes or words (space)
		- to maintain states
	- etc.
- context of a process: machine and kernel-related state
	- cpu context is the values of the registers
		- pc is the **program counter**, sp is the **stack poitner**, fp is the frame pointer, gp is general, etc.
	- memory context: pointers to memory areas
		- like code, static variables, heap, shared
		- stack of activation records(?)
			- an activation record is all the information we need for keeping track of a procedure (method or function) that was called.
			- we find
				- where to return to
				- link to the previous record
					- so we know how much to pop off the stack
				- automatic (local) variables
				- other (like register values)
			- stack pointer points to the top of the stack
	- memory is composed of three parts. we need this abstraction to create the mechanism for the abstraction of multiple cpus.
	- text, data, stack
	- "what does memory look like to a process?"
- SO THE GOALLL is to **support multiple processes**
	- users would like to run multiple programs "simultaneously"
	- not all actively using the cpu
	- some are waiting for input, devices, etc
- how to do this given a single cpu?

### Multiprogramming
Given a running process
- at some point needs a resource
- and if resource is busy, process can't proceed
- "voluntarily" gives up cpu to another process
**"Yield"** (p) function
- is a kernel call
- Let process p run (voluntarily...)
- requires context switching(?)
	- the ability to save the context of the current process and to restore the context of another process that we want to yield to that we now want to run.

### Context-Switching
- first save the context of currently running process
- next restore (load) context of next process to run
to load the context
- load general registers, stack pointer, etc.
- load program counter (must be last instruction(?))
	- so we gotta do all our context-saving before restoring the program counter, bc we can't backtrack after loading the pc

The kernel is code that supports processes and runs as an extension of the current process
- has text, data, and **multiple** stacks (one for each process/program that's running)!