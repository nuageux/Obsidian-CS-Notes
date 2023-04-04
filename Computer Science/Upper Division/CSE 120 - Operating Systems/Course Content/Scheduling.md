#OS 
- **Scheduling** defines which process gets the CPU, and when.
	- We have multiple processes, but only one CPU, so how much CPU time does each process get?
	- Possibilities:
		- Keep CPU 'til done
		- Each process uses the CPU a bit then passes it on
		- Each process gets proportional to what they pay
		- Decisions, decisions... it's a *policy decision*!
- Some terminology:
	- Arrival time: time that process is created
	- Service time: CPU time needed to complete
	- Turnaround time: from arrival to departure
		- i.e. process arrives, waits for CPU, then uses (in bursts)
		- ...and departs after CPU usage equals service time
		- So we are interested in what order minimizes average turnaround time.
- We'll look at different types of schedulers.
	- **Shortest-First** is always better than **Longest-First**.
	- **First Come, First Served**: Allocate CPU to the proceses in order of their arrival.
		- It's non-preemptive, simple, no starvation, but is poor for short processes.
	- **Round Robin**: Time-slice: each process gets a quantum in turn.
		- This *is* a preemptive algorithm. It's simple though and doesn't starve either.
			- Because it's preemptive, we need an interrupting clock!
		- Each process waits at most $(n - 1) * quantum$.
		- In *general*, RR is better than FCFS (because shortest-first is best!).
	- **Shortest Process Next**: Select the process in the queue with the shortest service time.
		- This is optimal (shortest-first) for non-preemptive algorithms, but it allows starvation.
		- Assumes service times are known.
	- **Shortest Remaining Time**: It's a preemptive version of SPN. Select the process with the shortest remaining time.
		- Optimal (shortest-first) for preemptive, but allows starvation.
		- Assumes service times are known.

## Priority Scheduling
- Select the process with the highest "priority". Processes are labeled with a priority beforehand.
- This allows scheduling based on external criteria.
	- We can create a priority function!
- The different types of priority scheduling are as follows:

### Multi-Level Feedback Queues
- Implementation: Select from highest queue *k*, run $2^k$ quantums.
	- "Priority queues": 0 (high), ..., *N* (low)
	- New processes enter queue 0
	- Select from the highest priority queue
	- Run for $T=2^k$ quantums, where $k$ is the number of the queue the process came from
		- Used T: move to next lower queue, FIFO
		- Used < T: back to the same queue, RR
			- Due to yield or higher priority arrival
	- Periodically boost (e.g. all to the highest queue)
- Basically, as we go down, we get less attention but more time.
- Through this system, the scheduler is trying to learn what the shortest processes are.
- It's complex, adaptive, and highly responsive.
- It favors shorter over longer (and thus opens up to the possibility of starvation).

### Fair/Proportional Share
- Each process requests time CPU utilization.
	- "Utilization" refers to what percentage of a time resource is used.
	- Each process "has an expectation" of how much CPU time they should be getting.
- The goal is for utilization over the long run, the actual amount of CPU time they get is approximately equal to their requested CPU time.
- Implementation 1: For each quantum, we select the process with the minimum actual/request ratio.
	- See slides: it's pretty confusing.
	- It's inefficient because we have to make a computation at the end of every quantum.

- Implementation 2: 
#### Stride Scheduling
- Given declared percentages of CPU times from processes, we calculate "strides", which are the reciprocal of the request percentage.
- For each process, maintain a **pass value** (initially 0).
- Then repeat for every quantum as follows:
	- Select the process with the minimum pass value
	- Increment pass value by stride value
- The optimization lies in the face we use integer operations instead of floating point.

## Real Time Scheduling
- The correctness of a real-time system depends on
	- the *logical result* of computations
	- *and* the timing of these results.
- There are two types of real-time systems
	- **hard** and **soft** real-time
		- These adjectives refer to the severity of missing a deadline.
		- Deadlines refer to the end of a period.
	- **periodic** and **a-periodic** real-time
		- Describes whether processes do things cyclically.
- Each process is given some values:
	- C = CPU burst = how much CPU time the process *must* get per period
	- T = period
	- U = C / T = utilization = how much time spent doing "useful" work
- Usually, it's impossible to predict whether a program will meet deadlines or not until it is run.
- However, when constaints are put on the problem, we *can* know.

#### Earliest Deadline First
- Just schedule the process with the earliest deadline.
- This *guarantees that all deadlines will be met!*
- If an earlier deadline process appears, preempt.
- Works for both periodic and aperiodic time.
- Achieves 100% utilization(!) (ignoring overhead)
	- The overhead is what it takes to *find* the earliest deadline.
	- When we ignore overhead, we need to *bound* the number of processes we are working with to realistically consider EDF.
- *Expensive!* Requires ordering by deadlines! $O(n)$ (bad)!

#### Rate Monotonic Scheduling
- Only works for periodic processes.
- Prioritize based on rates (the reciprocal of the periods (which were given)) of the periodic processes given.
	- Priorities won't ever change (unlike deadlines)!
- At the start of any period, select the highest priority.
- Preempt if necessary. When the burst is done, we put it aside until the next period.
- If the sum of $n$ utilizations $U_1 + U_2 + ... + U_N\leq n(2^{1/n}-1)$, all deadlines have been met.
	- If that bound is not met, it doesn't necessarily mean that the problem will fail to meet deadlines, it just means we cannot guarantee what will happen.
		- i.e. might *happen* to work perfectly. We just didn't know until we ran the program.
- A *lot* less overhead than EDF.
- **RMS is Optimal but Limited**.
	- It's simple and efficient; note the static priority scheduling based on rates.
	- It's optimal for static priority algorithms; no other static priority algorithm can schedule if RMS can't.
	- But it's limited in what it guarantees by its bound test. It's also bound to periodic processes.
			- The bound test is incidentaly always > ln(2) = 69%. We can thus test with 69% instead.