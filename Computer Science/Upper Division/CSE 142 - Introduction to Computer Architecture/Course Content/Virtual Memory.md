#Practical #Computer-Architecture 
# Virtual Memory
- It's really just another level in the cache/memory hierarchy.
- *Virtual Memory* is the name of the technique that allows us to view main memory as a cache of a larger memory space (on disk).
	- So main (physical) memory *is the cache* for the disk.
	- Think of it as *a mapping function* from *VM addresses* to *physical memory locations*.
	- If you read an address in C, we get back virtual addresses.
- Solves a number of problems...
	- What happens if another program in the processor uses the same addresses that yours does?
	- What happens if your program uses addresses that don't exist in the machine?
	- What happens to "holes" in the address space your program uses?
	- Can someone else's program touch your data (or vice versa)?
- We use **page tables** to do the mapping. Here's the method:
	- Say we have a 64-bit virtual address, split into 52-bits for a virtual page number and 12-bits for a page offset.

SLIDE 9