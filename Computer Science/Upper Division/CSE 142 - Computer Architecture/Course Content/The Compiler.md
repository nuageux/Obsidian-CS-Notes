#Practical #Computer-Architecture  
# The Compiler
- **Control Flow Graphs** show how assembly moves from one section to another.
- **Call Graphs** show how functions call other functions (and how many times).
- **Linking** is the final step in compiling a program.
	- Usually, programs are spread across multiple source files that are compiled one-at-a-time into *object files* (with the extension `.o`) that contain binary instructions and static data.
	- So linking is when the compiler takes all these `.o` files and copies their contents into a single executable file, resolving the undefined references within the files.
- Name **Mangling** in C++ is when the linker creates a long, messed up function names as aliases for a program's functions.
	- Must be done because functions in C++ can have the same name with different return types.
- **Aliases** refer to when two or more pointers refer to the same values.
	- Because the compiler cannot tell whether the value beyond the reference has been changed, it can't optimize the section in question.
	- We can use the `__restrict__` keyword to let the compiler know there isn't any problem with optimizing the section of code with pointers.

# Program Optimization Strategies
- **Register Assignment**, where the compiler puts local variables into available registers right away.
	- Saves `mov` instructions and memory accesses.
- **Common Sub-Expression Elimination**, where the compiler avoids calculating things twice and simply reuse the instances seen before.
- **Loop Invariants**, where the compiler identifies computations in the body of a loop that don't change from one iteration to the next.
	- The compiler "hoists" that code out of the loop, saving instructions.
- **Strength Reduction**, where the compiler converts a "stronger" (read: more complex) operation into a "weaker" (read: simpler) operation.
	- A common example is converting multiplication and division by powers of two into left and right shifts.
- **Constant Propagation**, where the compiler identifies the value of constant expressions at compile time and uses those constant values to simplify computations.
	- Usually this involves loops without variables in them.
- **Loop Unrolling**, where the compiler "unrolls" a loop so that the loop body contains the computation for multiple iterations of the loop.
	- This is probably the most useful strategy here.
- **Function Inlining**, where we just write in the code back into the function that is calling it.
	- This drastically reduces the call graph size.

### Optimization Flags
- `-O0` means to perform no optimizations. Don't use this.
- `-O1` means the compiler "tries to reduce code size and execution time without performing any optimizations that take a great deal of compilation time".
- `-O2` means that "GCC performs nearly all supported optimizations that do not involve a space-speed tradeoff".
- `-O3` means to optimize a bit more than `-O2`.
- `-Og` means to optimize *the debugging experience*.
- We can use the `-march=native` flag to indicate the specific version of the processor we're compiling for.