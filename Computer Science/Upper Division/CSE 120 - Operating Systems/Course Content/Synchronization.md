#OS 
- To synchronize means that events happen at the same time.
- Process synchronization
	- Events in processes that occur "at the same time"...
	- ...in actuality one process waits for another. Otherwise they might overwrite one another.
	- Think of it as "lockstep" like in parallel computing.
- Uses?
	- Prevent race conditions
		- Identify *critical sections*, i.e. sections of code that are executed by different processes, which must run *atomically (should not be divided), with respect to each other!*
			- We seek *effective* ataomicity, not actual atomicity. We're allowed to interrupt processes in critical section, so long as there is no other effect on other processes.
		- The above (^) enforces mutual exclusion, where only one process is active in a critical section.
	- Wait for resources to become available.

### Achieving Mutual Exclusion
- Processes should "mutually exclude" each other.
	- If one process is in its critical section, no other process should be in theirs.
- Surround critical section with "entry/exit" code.
	- The entry code functions as a barrier; if another process is in a critical section, block it. Otherwise, allow it to proceed.
	- The exit code should release other entry barriers.
- Indivisible, relative to each other. 
- A good solution has 4 requirements; given multiple cooperating processes, where each process has a critical section and all critical sections are to be mutually exclusive,
	- 1. At most one in a critical section at a time
	- 2. Can't prevent entry if no others are in theirs
	- 3. Should eventually be able to enter
	- 4. No assumptions about CPU speed or number
- Disabling interrupts is not a solution because it is an assumption about the CPU(s)

## Peterson's Solution
- Use both "taking turns" and "stating intentions".
- If there's competition, take turns. Otherwise assume free entry.

## Test-and-Set Lock Instruction: TSL
- This is a hardware-developed instruction to aid with mutual exclusion.
- [test if mem == 0 AND set mem = 1]
	- These operations occur without interruption. The memory bus is locked so it isn't affected by hardware interrupts.
- We bring back lock!

# Semaphores
- Invented by Djikstra!
- A "synchronization variable". They *only* provide a mechanism to provide synchronization. *There is no way for a process to tell it is blocked*.
	- They take on integer values and can cause a process to block/unblock.
	- There are only two operators:
		- wait, which decrements and **blocks** if < 0
		- signal, which increments and unblocks a process if any are blocked.
	- No other operations are allowed. We can't test the value of a semaphore!
- wait and signal must both themselves be atomic, however!
	- Use the hardware TSL solution or Peterson's solution.
	- We can't get rid of busy-waiting. But we at least moved it to a lower level, within semaphores.
		- Thus the occurrence is limited to brief and known periods of time.