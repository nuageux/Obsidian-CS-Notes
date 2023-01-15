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

# CUDA Execution Model
- We examine an example of a conversion of a color image to a grayscale image.
- The CUDA/OpenCL/SYCL Execution Model is:
	- An "integrated **host** + **device** app C program".
		- The device is also known as a "kernel".
		- The pattern is run sequential code, then run parallel code, wait for the parallel code to finish, then get back to your sequential code, repeat.
	- A CUDA kernel is executed by a grid (array) of threads.
		- All threads in a grid run the same kernel code.
		- "Single Program, Multiple Data" (SPMD)
		- Each thread has an index that it uses to compute memory addresses and make control decisions.
		- The hierarchy is as follows: kernel -> grid -> block -> thread
			- So to access an index in the device, it is `i = blockIdx.x * blockDim.x + threadIdx.x;`
	- We can furthermore divide the thread array into multiple blocks.
		- Threads within a block cooperate via a shared memory, atomic operations, and barrier synchronization.
		- Threads in different blocks cooperate less.



- vector addition:
	- 1. allocate device memory for A, B, and C. Copy A and B to the device memory.
	- 2. kernal launch code - do the actual vector addition
	- 3. copy C from the device memory then free the memory from 1.

- device refers to the kernel and device code can:
	- read write per thread registers
	- read write per grid global memory
- host code can transfer data to/from per grid global memory.

SOOOO
- cudaMalloc()
	- allocates an object in the device global memory
	- two parameters
		- address of a pointer to the allocated obj
		- size of the allocated obj in terms of bytes
- cudaFree()
	- well... frees it...
	- parameter: pointer to obj to be freed
- cudaMemcpy()
	- transfers data from host memory space to device memory space
		- so it's the step 1 in vector addition
	- four parameters
		- pointer to destination
		- pointer to source
		- number of bytes copies
		- type/direction of transfer