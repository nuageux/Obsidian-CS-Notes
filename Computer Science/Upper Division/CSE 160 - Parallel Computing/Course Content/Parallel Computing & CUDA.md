#Parallel-Computing
- Challenge: Design scalable and portable software that will last through many hardware generations.
### CPU Latency Oriented Design
- Compiler/Architecture finds parallelism and maps it to the hardware.
	- High Clock Frequency
	- Large Caches
		- Reduces memory latency
		- O(100) cycles -> O(1) cycle
	- Sophisticated control
		- Reduces branch latency via prediction
		- Reduces data latency via data forwarding
	- Powerful ALUs
		- Reduces operation latency
### GPU Throughput Oriented Design
- Programmer finds the parallelism and maps it to the hardware.
	- Moderate Clock Frequency
	- Small Caches
		- Boosts memory thoughput
	- Simple control
		- No branch prediction nor data forwarding
	- Energy-efficient ALUs
		- Many operations with potentially long latency, but are heavily pipelined for high throughput

## Heterogeneity
- Use CPUs for sequential code! Use GPUs for parallel code!
	- Note that the CPU is referred to as the "host" and the GPU is referred to as the "device".
- Thus, the parallel programming workflow is as follows:
	- Identify compute-intensive parts of an application
	- Adopt or create scalable algorithms
	- Optimize data arrangements to maximize locality
	- Performance tuning
	- **Code portability, scalability, and maintainability**
- Remember that "Regularity facilitates Parallelism".
	- Also remember that the total amount of time to complete a parallel job is limited by the thread that takes the longest to finish. "Irregularity" *inhibits* parallelism.
		- Conflicting data accesses cause serialization and delays.
			- Massively parallel execution can't afford serialization!
		- Contentions in accessing critical data causes serialization