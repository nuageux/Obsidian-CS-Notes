#Parallel-Computing 
# CUDA Execution Model
- The CUDA/OpenCL/SYCL Execution Model is:
	- An "integrated **host** + **device** app C program".
		- The device is also known as a "kernel".
		- The pattern is run sequential code, then run parallel code, wait for the parallel code to finish, then get back to your sequential code, repeat.
	- A CUDA kernel is executed by a grid (array) of threads.
		- All threads in a grid run the same kernel code.
		- "Single Program, Multiple Data" (SPMD)
		- Threads don't execute at the same rate. So we group them in "warps" of 32 in order to force exeuction in lockstep (i.e. all threads will wait for the slowest thread to finish its instruction before they all move on to the next).
			- Warps are the scheduling units in a streaming multiprocessor.
			- SM implements zero-overhead warp scheduling. So the warp whose next instruction has its operands ready for consumption are eligible for execution.
			- The pitfall of warps are control/branch divergence.
				- GPUs can use predicated execution, where each thread computes a yes/no answer for each path, so multiple paths are executed serially.
		- Each thread has an index that it uses to compute memory addresses and make control decisions.
		- The hierarchy is as follows: kernel -> grid -> block -> thread
			- So to access an index in the device, it is `i = blockIdx.x * blockDim.x + threadIdx.x;`
	- We can furthermore divide the thread array into multiple blocks.
		- Threads within a block cooperate via a shared memory, atomic operations, and barrier synchronization.
		- Threads in different blocks cooperate less.
	- We (programmers) define the dimensions of grids and blocks (there are 3 each, each is 1 by default).
- See Vector Addition example.
- As for function declarations:
	- ![[Pasted image 20230117125747.png]]
- ![[Pasted image 20230117130712.png]]
- `cudaMalloc`, `cudaFree`, and `cudaMemcpy`

### Program Flow
- In the Host Code...
	- Do sequential stuff
	- Prepare for kernel launch
	- Allocate memory on device (GPU)
	- Copy data to the device (GPU)
- Launch the kernel code (GPU code)
	- GPU code is CUDA code
- ...back to the Host Code...
	- Copy the data from the device to the host