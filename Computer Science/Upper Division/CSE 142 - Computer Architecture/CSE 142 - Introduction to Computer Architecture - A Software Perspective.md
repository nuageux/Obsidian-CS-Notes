#Course #CSE #CPP #Computer-Architecture #x86
Prerequisites: [[CSE 30 - Computer Organization & Systems Programming]], [[CSE 100 - Algorithms & Data Structures]]

Fall 2022
Instructor: Prof. Leo Porter & Prof. Steven Swanson

#### Course Description:  
"The operation, structure, and programming interfaces of modern CPUs with an emphasis on exploiting processor features to improve software performance and efficiency. Includes performance, energy, x86 assembly, compiler optimizations, pipelining, instruction-level parallelism, caches, memory-level parallelism, multi-threading, multi-core processors, and SIMD."

## Course Content
- [[Measuring Performance]]
- [[x86 Assembly]]
- [[The Compiler]]
- [[Caches]]
- [[Virtual Memory]]
- [[Executing Instructions Efficiently]]
- Memory Level Parallelism

## 142L: Software Project for Computer Architecture
Accompanying lab course. "Provides hands-on experience in using the features of modern CPUs to increase the performance and efficiency of programs."

- How CPUs work and how software interacts with them.
	- How do programs *really* behave?
	- What impact do caches *really* have?
	- How can I make my code run faster?
- The goal of the classes is to improve our intuition.

# Lab 1
How we can measure performance and what can we learn
- The performance equation
- Work done on "bare metal" servers, no virtualization, which gives full access to underlying processors
- cse142 is a command line tool for us to use.


What the compiler does to code and how smart it is

Why memory is slow and how to write programs that access memory efficiently

Why memory is really important, and more

How threads and vectors improve performance and why they aren't quite as helpful as we want them to be
