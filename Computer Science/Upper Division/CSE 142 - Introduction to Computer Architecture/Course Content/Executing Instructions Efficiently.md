#Practical #Computer-Architecture 
# Pipelining
- We will look at a high-level model of instruction execution with **six stages**:
	- Fetch, Decode, Read, Execute, Write, (compute) Next instruction (**FDREWN**).
- The CPU has a "program counter" (PC) that holds the address of the current instruction.
	- The CPU then executes the instruction at the PC, then either
		- increments the PC to the point of the next instruction
		- OR (for a branch or jump) sets the PC to a new value
- All instructions go through each stage per cycle.
	- Each stage takes 1 clock cycle, so a single instruction executes in 6 cycles.
 ![[image - 6 stage multi cycle processor.png]]
 - We'll feed in instructions every cycle, so at the beginning it will take 6 cycles for the first instruction but will eventually become 1 instruction completed per cycle.
	 - This idea of **functional parallelism** is possible due to **pipelining**, setting up a pathway for execution because we know the process is the same every time.
### Hazards
- Unfortunately, the best case CPI of 1 isn't the reality.
- Sometimes a stage of the processor doesn't have something it needs to process an instruction. These are called **hazards**.
	- **Control** hazards are when the fetch stage doesn't know which instruction to fetch.
	- **Data** hazards are when the execute stage doesn't have an operand it requires.
- We will use a table notation with FDREWN.

# Speculation
- Our first solution to control hazards is to "pre-decode" the instruction just to determine if it's a branch, and if so, stall. Else, fetch it!
- The next, better solution is to simply guess where the branch is going to go.
	- Program behavior is predictable! e.g. loops, if statements that check for unlikely error conditions, unconditional branches, etc.
	- The processor will guess in the fetch stage. But how does it guess, and what does it do when the guess is wrong?
- For now, note that the updates are that *in the fetch stage, we will predict the next PC* and that *in the N (compute) stage, we will detect mispredictions*.
- One method was a "branch predictor" that made predictions based on prior branch outcomes.
	- We will use a dynamic, 2-bit local predictor.
		- 11 will indicate a "strong" prediction of branch taken, while 00 means "strong" prediction it won't. 
		- Every time a branch is taken, increment this two bit number, while if it is not, decrement it.
		- It's fairly resistant to "flipping" its prediction too often.
	- However, it's not a good branch predictor. Modern branch predictors are carefully guarded trade secrets.
- On an incorrect prediction, the processor will "squash" the path when the branch "resolves" (when the next correct PC is known).
	- Discard/rollback/suppress register and memory updates.
	- This is called "flushing" the pipeline, and the CPU flushes all instructions that are newer than the mis-predicted branch.
- What's the cost?
	- IC is unchanged, since the flushed instructions don't count.
	- CPI increases, since the processor wasted cycles.
	- CT is unchanged. 
	- Energy goes up due to CPI, but it's negligable.
- **So speculation adds complexity and hardware, but improves efficiency by a significant amount.**

# Forwarding
- Our first solution for data hazards is to stall, but that's undesirable.
- Our second solution is also to stall, but to also include register file "forwarding".
	- Immediately passing values to the next read cycle from the current write cycle.
	- The way we will forward is to take the value at the current execute cycle to the next execute file. This takes a bunch of logic, but it's worth it.

# Micro-Ops


# Pushing for More...?
