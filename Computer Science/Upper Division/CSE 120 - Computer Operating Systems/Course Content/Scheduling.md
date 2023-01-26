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