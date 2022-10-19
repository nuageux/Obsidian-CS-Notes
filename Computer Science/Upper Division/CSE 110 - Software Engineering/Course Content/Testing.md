### Black-Box Testing
*Users* see the system from the *outside*; this is a **black box** concerned with functionality.

Look for:
- Functionality
- User Input validation
	- Make sure users are entering valid inputs, and if necessary help the users with making valid input.
- Output results
- State transitions
- Boundary cases and off-by-one errors (edge cases)

### Grey-Box Testing
*Testers* look into the code slightly; this is a **grey box** concerned with checking whether code makes the system crashes, uses too much memory, or something else.

Use for:
- Verifying auditing and logging
	- making sure behind-the-scenes values are correct
- Data destined for other systems
	- if data is being transfered to other systems, make sure that they're correct.
- System-added information
	- human verify this.
- Scraps left laying around
	- make sure all data to be cleared/deleted after use are actually removed (security risks).

### White-Box Testing
*Developers* are fully invested in the code; this is a **white box** that is concerned with all of the implementation, but the sheer scope of it all may make developers miss something critical that slipped under their radar.

Considering the inside knowledge available, look for:
- Testing all the different branches of code
	- such as testing all the if/else statements
- Proper error handling
	- intentionally send bad input and see if you get the right error message
- Working as documented
- Proper handling of resource constraints
	- if a method needs resources but can't get them, does it handle it gracefully?


## Test Libraries
A test library full of tests should be run all at the same time to test the software completely every tiem we run a **test suite**.
- Helps detect **software regression**, when a new change to the software introduces bugs in the older code.

## Mock Objects
Are simulated objects that mimic the behavior or real objects in controlled ways.
- e.g. a car designer uses a crash test dummy to simulate the behavior of a human in vehicle impacts.
- Useful to use if:
	- the object supplies non-deterministic results (e.g. current time or the current temperature)
	- has states that are difficult to create or reproduce (e.g. network error)
	- it is slow (e.g. a complete database)
	- doesn't exist yet or may change behavior

Mocks, fakes, or stubs are described as a fake object that helps decide whether a test failed or passed by verifying whether an interaction with an object occurred.