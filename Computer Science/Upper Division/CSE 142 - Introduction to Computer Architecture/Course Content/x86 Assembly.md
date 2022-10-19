# x86 Assembly
- This is a throwback to **assembly language** from [[CSE 30 - Computer Organization and Systems Programming]].
	- Is a readable form of **machine code**.
- A **compiler** translates a human-readable programming language into a language that a computer understands.
- Reasons to learn machine code:
	- Higher-level abstraction hides valuable program details
	- Some computing systems are too resource-constrained for compilers
	- Vulnerability analysis
	- Critical code sequences in system-level software
- x86 is a 64-bit **ISA (Instruction Set Architecture)**.

## Basics of Assembly
#### Registers
- A word-sized storage unit on the CPU.
- There are 16 registers, and the latter half is registers  `%r8-%r15`.
	- The other relevant ones are
		- `%rsp`, which is the stack pointer, which points to the top of the stack.
		- `%rbp`, which is the frame pointer.
			- This points to the base of the active stack frame, to reference parameters.
		- `%rip`, which is the intruction pointer (or the program counter).
- Since we are dealing with 64-bit, to access the lower 32 bits, we replace the `r` with an `e` in the above commands.
- "opcodes" with "operands"
	- $ signs signify constant values (literals).
	- Then there are registers,
	- and there are memory addresses.

## Common Instructions
- mov S, D
- add S, D
- sub S, D
- The **call stack** maintains the organization of the program stack.
	- The stack actually "grows" from the "ceiling" of memory, so to pop something we add to the memory address and vice-versa.
- push S
- pop D