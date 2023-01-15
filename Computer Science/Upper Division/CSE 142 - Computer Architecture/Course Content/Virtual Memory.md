#Practical #Computer-Architecture 
# Virtual Memory
- It's really just another level in the cache/memory hierarchy.
- *Virtual Memory* is the name of the technique that allows us to view main memory as a cache of a larger memory space (on disk).
	- Think of it as *a mapping function* from *VM addresses* to *physical memory locations*.
	- If you read an address in C, we get back virtual addresses.
- Solves a number of problems...
	- What happens if another program in the processor uses the same addresses that yours does?
	- What happens if your program uses addresses that don't exist in the machine?
	- What happens to "holes" in the address space your program uses?
	- Can someone else's program touch your data (or vice versa)?
- We use **page tables** to do the mapping. Here's the method:
	- Say we have a 64-bit virtual address, split into 52-bits for a virtual page number and 12-bits (4KB, the standard) for a page offset.
		- The page offset remains the same for the physical address (which probably has a different number of bits for the entire physical address).
		- The virtual page number indexes to a location in the page table, which shows which physical page to access.
		- *The physical address is $log_2(RAM)$*. *The page offset is $log_2$(page size)*.
	- All page mappings are in the page table, so hit/miss is determined solely by the valid bit (there is no tag).
		- Each mapping tells us whether an address is in disk or in physical memory.
		- Valid bit of 1 means that the address is in memory.
			- A valid bit of 0 means that it's not in memory, and thus triggers a **page fault**.
	- All programs have their own page tables.

## Translation Lookaside Buffer (TLB)
- Because we don't want to go to memory everytime we want to do a page lookup/translation, we'll actually cache the page table entries themselves!

#### Conclusions
- Virtual memory provides protection, sharing, performance, and an illusion of large main memory.
- Requires twices as many memory accesses, so we cache page table entries in the TLB.
- Three things can go wrong: cache miss, TLB miss, page fault.
- Page faults... are really expensive.