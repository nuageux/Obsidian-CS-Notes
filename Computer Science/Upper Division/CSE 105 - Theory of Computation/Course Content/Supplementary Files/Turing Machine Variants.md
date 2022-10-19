#Model #Theoretical 
## Multitape Turing Machines
Where there are multiple tapes, but only the first one carries the initial input while the others start out blank.
- Transition function allows reading, writing, and moving the heads on some or all of the tapes simultaneously.
- Note that any number of tapes can still be represented by a single tape.

## Nondeterministic Turing Machines
Exactly as it sounds, a TM where the machine may proceed according to several possibilities.
- Using the original TM, we need only examine each branch in a breadth-first manner to simulate a nondeterministic TM.

## Enumerators
A TM where, when the TM wants to add a string to the (one and only) list (read: set), it prints the string using a printer.
- We can show that if an enumerator enumerates a language, there is a TM that recognizes that language.
- A language is Turing-recognizable if and only if some enumerator enumerates it.
	- If we have an enumerator that enumerates a language, a TM recognizes that language.
		- Create a TM that runs the enumerator for every input, and if the input appears in the enumerator's list, accept that input.
	- If we have a TM that recognizes a language, there exists an enumerator that enumerates this language.
		- Say we have a list of all possible strings for a given language.
	```java
for (int i = 0; i < infinity; i++) {
	run enumerator i times for every possible string
	if (any string is accepted)
		print that string
}
	```
	- Follow the above algorithm.

#### Equivalence with Other Models
It turns out that any model with unrestricted access to unlimited memory are equivalent in power (so long as they satisfy reasonable requirements).
- One such requirement is the machine may only perform a finite amount of work in a single step.