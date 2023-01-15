#Practical #Computer-Architecture
## Locality
- The tendency to reference data items that are near other recently referenced data items or that were recently referenced themselves.
	- This is a good thing. Usually the program will run faster!
- Two forms:
	- Temporal locality, where a memory location that is referenced once is likely to be referenced again multiple times in the near future.
	- Spatial locality, where if a memory location that is referenced once, the program is likely to reference a nearby memory location in the near future. 
- Locality allows us to use **cache memories** that hold blocks of the most recently referenced instructions and data items.
- It also allows the OS to use main memory to cache the most recently used disk blocks in the disk file system.
- A function that visits each element of a vector sequentially is called a *stride-1 reference pattern*, or a *sequential reference pattern*.
	- 1 refers to the step size.
	- e.g. row-major traversal enjoys good stride-1 locality, but *a col-major traversal ends up with stride-n* locality.
### Temporal Locality
- Again, temporal locality exists when a program accesses the same memory multiple times within a short time frame.

## Memory Hierarchy
- As follows, smallest/fastest/expensive to largest/slowest/cheapest: Registers, L1 Cache, L2 Cache, L3 Cache, Main Memory, Local Secondary Storage, Remote Secondary Storage.
- So SRAM is much faster with a greater bandwidth than DRAM.
	- We have small and fast OR large and slow.

# Caches
- A **cache** is a small, fast storage device that acts as a staging area for the data objects stored in a larger, slower device.
- The general idea is that each level in the hierarchy caches data objects from the next lower level.
- Cache "hits" refer to successful cache searches, i.e. the item we were looking for was in the cache.
- Cache "misses", on the other hand, refer to problems.
	- *Compulsory* misses result from trying to access an empty cache.
	- *Conflict* misses refer to when restrictive placement policies, such as mapping blocks to a singular block.
	- *Capacity* misses result from when the cache is simply too small to be working with a particular data set.
	- To decide what data to throw out, we usually select the Least Recently Used (**LRU**)... the dustiest book in the shelf (cuz nobody's reading it).
- Some terminology:
	- Hit: an access where the data is found in the cache.
	- Miss: an access where the data isn't found in the cache.
	- Hit Time: time to access the cache
	- Miss Penalty: time to move data from further level to closer, then to CPU
	- Hit Ratio: percentage of time the data is found in the cache
	- Block Size: the amount of data that gets transferred on a cache miss.
	- Instruction Cache: only holds instructions
	- Data Cache
	- Unified Cache: holds both.
- Example on how it affects the PE on slide 56.
- Compiler uses "prefetching", getting a size of block that will cover the next few access instances. Of course, it's just a guess.
- Remember that you have to access both the I-cache and the D-cache for every load instruction.

### Direct-Mapped Caches
- A cache that can put a block of data in exactly one place is called Direct Mapped.
- Bigger caches have higher hit rates, since they can store more data!
	- Our code works best when our data fits in our cache.
- Computations?
	- Associativity = 1
	- \#offset_bits = log_2(block_size)
	- \#entries = cache_size / block_size
	- \#index_bits = log_2(\# entries)
	- \#tag_bits = address_size - \#index_bits - \#offset_bits
- Ex: Run a loop that covers the addresses close to each other, then a second loop for the other group.
- Larger cache *blocks* help reduce misses by lowering spatial locality misses
	- The tradeoff is, the larger the block size, the fewer blocks we can store in the same size cache.
	- 64 byte block size is common (16 words).

### Fully-Associative Cache
- No rules on what data can go where.
	- To know where to look?
	- To decide what to remove?
- LRU is kind of a pain to keep track of. Need log N bits per block to store the order, and you need to update all the bits on every access.

### n-Way Associative Cache
- There are rules, but for each index, there are n multiple blocks that can be stored.
	- All blocks that share an index are part of a "set".
- The "middle ground". Decent hit times, decent use of cache space. Hit rates are therefore higher.
- Computations?
	- **Associativity = n**
	- \#offset_bits = log_2(block_size)
	- **\#entries = cache_size / (block_size \* n)**
	- \#index_bits = log_2(\# entries)
	- \#tag_bits = address_size - \#index_bits - \#offset_bits 

## Handling Stores
- Fundamentally different than loads:
	- Are *non-blocking*, meaning we can just write to a store buffer.
- Store miss policies:
	- Write Allocate: brings the cache block into the cache, then use the store hit policy.
	- Write No-Allocate: just notifies the lower levels of the cache about what was changed.
- Store hit policies:
	- Write Through: tell lower levels cache what was changed immediately.
		- Uses bandwidth
	- Write Back: mark the block as dirty as tell lower levels of cache about the change when the block is evicted.

# Measuring Cache Performance
- *Performance Counters* allow us to measure cache performance.
	- They are hardware components in the CPU that measure performance-related events, such as instructions executed, cache misses, branch mispredictions, etc.
- **Tensors** are multi-dimensional arrays.
- Prof. Swanson has created the **Miss-Machine**, a #Data-Structure that forces the cache to constantly miss by randomly iterating through a linked list.
- **Data-alignment** describes the behavior of the compiler to assign data to sections of the cache that match its size (by a multiple).
	- *Width-alignment* is when a value is aligned to its own size in bytes in memory.
	- So interestingly, within `structs` in C++, if a data member is not as big as the struct itself, the compiler will "pad" the member with empty memory to allow clean cache accesses.
		- The lesson is to organize your struct members by size, largest to smallest.
	- If data were not to be aligned, it would cause more cache misses than necessary.