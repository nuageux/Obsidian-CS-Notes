#Course #CSE #C
Prerequisites: [[CSE 30 - Computer Organization & Systems Programming]], [[CSE 101 - Design and Analysis of Algorithms]], [[CSE 110 - Software Engineering]]

Winter 2023
Instructor: Prof. Joseph Pasquale

#### Course Description:  
"Basic functions of operating systems, including basic kernel structure, concurrency, memory management, virtual memory, file systems, process scheduling, security, and protection."

## Operating Systems
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
- The OS "turns the undesirable into the desirable"; the undesirable inconvenience (reality) into desirable conveniences (illusions), i.e. limits are "removed" and masked.
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
## Course Content
- [[Processes]]
- [[Timesharing]]
- [[Scheduling]]
- [[Synchronization]]
- [[InterProcess Communication]]
- [[Deadlock]]
- [[Memory Management]]
- [[Logical Memory]]
- [[Virtual Memory]]
- [[File Systems]]
- [[Input-Output (I-O)]]