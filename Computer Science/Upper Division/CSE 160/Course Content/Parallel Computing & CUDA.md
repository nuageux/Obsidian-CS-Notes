- challenge: design scalable and portable software that will last through many hardware generations
- CPU latency oriented design: compiler/architecture finds parallelism and maps to the hardware.
	- high clock frequency
	- large caches
		- to reduce memory latency
		- O(100) cycles -> O(1) cycle
	- sophisticated control
		- reduce branch latency via prediction
		- data forwarding for reduced data latency
	- powerful ALUs
		- reduced operation latency
- GPU throughput oriented design: programmer finds the parallelism and maps to the hardware
	- moderate clock freq
	- small caches
		- boost memory thoughput
	- simple control
		- no branch prediction nor data forwarding
	- energy efficient ALUs
		- many long latency but heavily pipelined for high throughput

 - So the winning strategy is "heterogeneity"
	 - cpus for sequential parts where latency matters
	 - gpus for parallel parts where throughput wins

- the workflow
	- identify compute intensive parts of an application
	- adopt create scalable algorithms
	- optimize data arrangements to maximize locality
	- performance tuning
	- **code portability, scalability, and maintainability**
- "regularity facilitates parallelism"
	- the total amount of time to complete a parallel job is limited by the thread that takes the longest to finish

- conflicting data accesses cause serialization and delays
	- massively parallel execution can't afford serialization
	- contentions in accessing critical data causes serialization

example: conversion of a color image to grey-scale image

- CUDA/OpenCL/SYCL Execution Model
	- Integrated host+device app C program
		- serial parts in host
		- parallel in device (kernel)
	- a CUDA kernel is executed by a grid (array) of threads
		- all threads in a grid run the same kernel code
		- single program, multiple data (SPMD)
		- and each thread has an index that it uses to compute memory addresses and make control decisions
	- so, divide the thread array into multiple blocks
		- threads within a block cooperate via shared memory, atomic operations, and barrier synchronization(?)
		- threads in different blocks cooperate less

- blockIDx and threadIDx
	- each thread uses indeces to decide what data to work on
	- allow programmer to express parallelism hierarchically

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