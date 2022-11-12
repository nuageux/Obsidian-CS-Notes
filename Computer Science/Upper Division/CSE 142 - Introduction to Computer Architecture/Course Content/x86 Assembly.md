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
	- x86 is a **CISC** ISA, a complex instruction set computer. It's more human readable (better interface), and is under constant pressure to add more features.
		- Varying amount of work per instruction
		- Variavle length instructions
		- No limitations on how instructions interact with memory
	- As opposed to **RISC** ISAs, reduced instruction set computers. 
		- There's a fixed amount of work per instruction
		- Fixed *length* instructions
		- Forced behavior with memory.
		- Better for implementation.
- x86 is... a poorly-designed ISA.
	- Switching ISAs is difficult because it requires new binaries.
	- x86 is still alive because it had a lot of momentum when it came out.

# Basics of Assembly
- We use AT&T syntax for this class, a.k.a. the gnu assember ("gas") syntax.
	- As opposed to "Intel Syntax". When you see examples online, make sure you know what the syntax is.
	- So for AT&T, it is generally `<instruction> <src2> <src1/dst>`.
- The **call stack** maintains the organization of the program stack.
	- The stack actually "grows" from the "ceiling" of memory, so to pop something we add to the memory address and vice-versa.
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
- The basic principle is that registers are fast, while memory is slow.
	- This should incentivize us to access memory infrequently.
### Immediate Values
### Complex Addressing Modes
- `%eax` simply means to access the value in register eax.
- `(%eax)` means to access the **memory** location *at the value* in register eax.
- `n(%eax)` means to add `n` to the value in register eax, then access that memory location.
- `m(%eax %ebx n)` means to multiply the value in ebx by `n`, add the value in eax to it, add `m` to it, then access that memory location.
- `lea` stands for "load effective address". It never actually accesses memory but instead works with the memory addresses.