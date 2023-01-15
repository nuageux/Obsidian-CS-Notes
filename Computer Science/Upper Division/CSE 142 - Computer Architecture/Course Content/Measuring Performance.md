#Practical #Computer-Architecture 
# Performance
There are different ways to define computer performance.
- **Response Time**, or execution time, is the total time required for the computer to complete a task.
- **Bandwidth**, or throughput, is the number of tasks completed per unit time.
	- For example, data managers are concerned with this metric.
- Changing one of these metrics often affects the other.

**Performance of X = 1 / Execution Time of X**
- It then follows that if the performance of computer X is greater than that of Y, then
	- Y's execution time is greater than X's.
- The phrase "X is $n$ times faster than Y" or "X is $n$ times as fast as Y" means
	- **Performance of X / Performance of Y = n**
		- We put the better performing computer on top!
	- **Execution Time of Y / Execution Time of X = n**
		- We put the slower computer on top!
- Think of it as, if Y takes a long time, Y is objectively worse, right?
- **Speedup = $S$ = $B$ / $A$**, where $B$ is always the greater number (assuming we talk about improving performance). 

We want to measure time in terms of **clock time / response time / elapsed time** (all different names for the same thing).
- More specifically, **CPU (execution) time** is the time the CPU spends on a specific task (and doesn't include time waiting for I/O or other programs).
	- Divided further into *user* CPU time and *system* CPU time.
- Consider system performance vs CPU performance.

### Clock Cycles
are discrete time intervals, a.k.a. clock ticks or periods.
- Can be measured as the time for a complete cycle, in picoseconds, or as a rate (the inverse of a period), in gigahertz.
- Consider the following 2 equations:
	- **Execution Time = \# Clock Cycles * Cycle Time**
	- **Execution Time = \# Clock Cycles / Clock Rate**
- Cycles per Instruction is affected by the ISA Designer, Compiler, Programmer, and Hardware Designer.
	- Thus, CPI is the most complex term in the PE, since many things affect it.
	- Note that different instructions require different amounts of work, so instructions that do more work generally increease CPI.
- Cycle Time is affected by the Hardware Designer, and sometimes a little by the ISA Designer.
	- Processor design, manufacturing variation, and software policy affect CT.

### Instruction Performance
- The number of clock cycles required for a program can be represented as
	- **\# Clock Cycles = \# Instructions * Average \# Cycles per Instruction (CPI)**
- The instruction count is affected by the ISA Designer, the Compiler, and the Programmer.
- *Dynamic* instruction count is what is represented in the performance equation.
	- Has to do with the execution of the program or counted at run time.
	- As opposed to *static* instructions, which are fixed at compile time or referring to the program as it was compiled.

## The Performance Equation
So, **CPU time = Instruction Count \* CPI \* Clock Cycle Time.**
- Alternatively **CPU time = Instruction Count * CPI / Clock Rate**.
- What differentiates the CPU time equations are that they are dependent on the number of instructions in a *specific* program.

# Ahmdahl's Law
- A common mistake is to expect that improving one aspect of a computer will improve the overall performance of a computer by a proportional amount.
	- Sounds weird, but it is intuitive.
	- Make the *common case* fast! The opportunity for improvement is affected by how much time the event consumes.
	- Keep in mind that the common case *is hard to pin down!* Engineers miss it all the time.
		- Look for what is *time-consuming* overall, **not** for the frequency!

## Amdahl's Law:
- **Execution Time After Improvement = ( ExeTime Affected by Improvement / Amount or Factor of Improvement ) + ExeTime Unaffected by Change**
	- In other words, **Total Speedup = 1 / ( ( x / S ) + ( 1 - x ) )**
		- Where $x$ is the fraction of the program being optimized, and $S$ is the speedup provided.
- In other words, the performance enhancement possible with a given improvement is limited by the amount that the improved feature is used.
	- Think of the law of diminishing returns!
- Use it in conjunction with the CPU performance equation.

#### Discussion on the practical limits to the number of parallel processors
- There is a "serial" constant time operation that can't be optimized.
	- This means there is a limit to how much we can speed up parallizable operations.
- The reason we do keep adding cores to processors is when we don't care about the time of the operation anymore, but rather the detail and precision of the calculations.
	- For example, there is no point in going above 120fps in first-person shooter video games, as the human eye cannot perceive further than that.
		- Instead, we wish to improve the quality of the gameplay, e.g. in the details with ray tracing
	- In physics simulations, the time it takes to generate the simulation will remain the same, but scientists certainly appreciate a higher order of detail whenever they can get it.

# Power
- Remember that **watts = Joules / second**.
- Energy and power constrain modern processors.
	- Energy is expensive!
	- Power creates heat, and cooling costs thus cost money.
### Power Equation
- Power is $P = V^2 * F * a * C + P_{idle}$.
	- $V$ is the processor core voltage
		- Is usually a similar value to $F$.
	- $F$ is the processor frequency
	- $a$ is the activity factor, or the fraction of transistors switching each cycle.
	- $C$ is the capacitance of the chip
	- $P_{idle}$ is the power consumed when the processor is doing nothing.
- $Energy = Power * Time$
	- So the power equation * ET = energy.

**All of these metrics can be compared to (fairly) impartial benchmark tests.**