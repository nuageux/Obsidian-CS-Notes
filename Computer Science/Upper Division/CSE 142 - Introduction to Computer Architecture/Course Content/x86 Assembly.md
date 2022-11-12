#Assembly #x86
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
	- ISAs define the instruction formats, instruction operations, and interactions with memory.
- x86 is... a poorly-designed ISA.

# Basics of Assembly
- We use AT&T syntax for this class, a.k.a. the gnu assember ("gas") syntax.
	- As opposed to "Intel Syntax". When you see examples online, make sure you know what the syntax is.
	- So for AT&T, it is generally `<instruction> <src2> <src1/dst>`.
## Key Operations
### Arithmetic
- Basic Arithmetic
	- add, sub, inc, dec, neg, imul, idiv
- Bit Shifts
	- sal, shl, sar, shr
- Bitwise
	- and, or, xor, not
### Loads & Stores
- There are no loads or stores in x86, only `mov`.
	- Move what's in the first argument to the second.
### Branches & Jumps
- x86 uses "condition codes" for branches.
	- Condition codes are special-purpose, 1-bit registers.
	- Arithmetic operations set the flags register.
		- carry, parity, zero, sign, overflow, etc.
	- Note that when comparing two values, they are flipped...
		- e.g. `cmp %eax, %ebx` represents `$ebx >= $eax`.
		- 


#### Registers
- "opcodes" with "operands"
	- $ signs signify constant values (literals).
	- Then there are registers,
	- and there are memory addresses.

## Key Operands
- '%' refers to a register, '$' refers to an immediate. No symbol indicates a label.
### Registers
- A word-sized storage unit on the CPU.
- There are 16 registers, and the latter half is registers  `%r8-%r15`.
	- The other relevant ones are
		- `%rsp`, which is the stack pointer, which points to the top of the stack.
		- `%rbp`, which is the frame pointer.
			- This points to the base of the active stack frame, to reference parameters.
		- `%rip`, which is the intruction pointer (or the program counter).
- Since we are dealing with 64-bit, to access the lower 32 bits, we replace the `r` with an `e` in the above commands.
### Memory
### Immediate Values
### Complex Addressing Modes
- `%eax` simply means to access the value in register eax.
- `(%eax)` means to access the **memory** location *at the value* in register eax.
- `n(%eax)` means to add `n` to the value in register eax, then access that memory location.
- `m(%eax %ebx n)` means to multiply the value in ebx by `n`, add the value in eax to it, add `m` to it, then access that memory location.

## Common Instructions

- mov S, D
- add S, D
- sub S, D
- The **call stack** maintains the organization of the program stack.
	- The stack actually "grows" from the "ceiling" of memory, so to pop something we add to the memory address and vice-versa.
- push S
- pop D