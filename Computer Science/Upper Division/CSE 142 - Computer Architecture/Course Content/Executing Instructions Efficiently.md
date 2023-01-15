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
- Improving on that idea, we will forward the value at the current execute cycle to the next execute file. This takes a bunch of logic, but it's worth it.
	- We do this by adding hardware connections to bypass the register file in the pipeline.

# Micro-Ops
- A main issue with pipelining x86 is that each instruction can have different amounts of work.
	- The solution is to translate all complex instructions into a bunch of modular, simple ones.
- So now we separate our pipeline into a front end and back end...
	- Frontend
		- Fetch: Retrieve the instruction from memory using PC, predict the next PC
		- Decode: *Decompose instruction into uOps, enqueue the resulting uOps in the decode queue*
	- Backend
		- RF Read: *Dequeue a uOp from the decode queue and read the register operants for the instruction*
		- Execute: *Perform uOp* operations
		- RF Write: Update register file
		- Compute Next PC: Detect mispredictions

# Pushing for More...?
### Deeper Pipelining
- The idea is to split the pipeline instructions.
![[image - split pipeline.png]]
- Because all that matters is the longest stage of the pipeline (the critical path), if splitting the hardware means we have shorter circuitry somewhere, it means we reduce cycle time (at the cost of more circuitry, of course).
	- This circuitry translates into power problems.
- Theoretically, CT should drop by half if we double the number of stages.
	- However, there is an overhead between each stage of just reading and writing to pipeline registers. Recall combinational and sequential logic from [[CSE 140 - Components & Design Techniques for Digital Systems]].
	- Furthermore, it requires all stages to be balanced.
- Right now, 14 seems to be the "right" number of pipeline stages.
### Instructional Level Paralellism
- It's possible to reduce the CPI below 1.
	- We need to execute more than one instruction per cycle...
		- Multiple or "wide" issue
		- Out-of-Order Execution
##### Multiple Issue
- We will learn the hardware method, the "superscalar" method (then the out-of-order version.
	- Superscaler means several instructions are loaded at once and executed simultaneously.
- Literally just do 2 instructions per step instead of one.
	- It usually stops at 2, because data dependencies become a mess the more we push this.
- More challenges:
	- Forwarding doesn't help, so it must stall.
	- Lock-step execution lets instructions interfere with each other.
	- Long-latency instructions mess with the pipeline too.
	- ...so CPI gains suffer.
- **The key terminology is n-issue, where the processor can start n instructions simultaneously.**

#### Out-of-Order Execution
- The modern solution...
	- Exploits ILP (so CPI < 1), manages data dependencies, and deals with long-latency instructions.
- **3 Steps**
	- **Register Dependencies**
		- Write-after-Write (WAW)
			- Where B writes to edx after A writes to edx...
				- So reordering gives the wrong result.
			- A *false* dependency on edx, since *no data flows from A to B*, but *A must execute before B*.
			- We can just put the result of A in a different register to break the dependency.
		- Write-after-Read (WAR)
			- Where B writes to edx after A reads edx...
				- So reordering gives the wrong result.
			- A *false* dependency on edx for the same reason in WAW.
			- We can just put the result of B in a different register to break the dependency.
		- Read-after-Write (RAW)
			- Where B reads eax after A writes to eax...
				- We cannot even reorder! Otherwise the value that B needs doesn't even exist!
			- This is a **true** dependency on eax, since data flows from A to B!
		- We need to look at the **dependency graph**.
			- Nodes are instructions and edges represent dependencies between them.
			- We need to identify the critical path with the *longest sequence of RAW, WAW, and/or WAR dependent instructions.*
				- The length of this path is the minimum execution time.
				- Assuming each instruction takes one cycle:
					- Ideal CPI = Critical Path / \# instructions
					- Avg ILP = 1 / CPI = IC / CP
				- So... ET = CP \* CT
				- We'll call the instruction's contribution to the CP its "effective latency".
					- If not on the CP, it's 0. If on, it's the number of added cycles.
	- **Register Renaming**
		- We can break false dependencies by renaming registers used (and thus use out-of-order execution).
		- *There can be many more physical registers than architectural registers*!
		- We will use the **Register Alias Table (RAT)**.
			- It renames architectural registers to physical registers.
	- **Out-of-Order Issue**
		- **Tomasulo's Algorithm**: Issuing instructions with reservation stations
		- The **Reorder Buffer (ROB)**: Has a retirement frontier, a fetch frontier, and a speculation frontier.



- Our pipeline is then as follows:
	- Frontend
		- Fetch: Retrieve the instruction from memory using PC, predict the next PC
		- Decode: *Decompose instruction into uOps, enqueue the resulting uOps in the decode queue*
	- Backend
		- *Dequeue: Move uOps from the decode queue to the ROB*
		- RF Read: *Rename the registers for those uOps*
		- *Schedule uOps: Select uOps whose inputs are available, issue them*
		- Execute: *Perform uOp* operations
		- RF Write: *Broadcast results to the scheduler; update the physical register file*
		- Compute Next PC: Detect mispredictions, send results to front end.