#Design
# Thoughtful Design
Well-designed classes are *singularly focused*.
- Consider the **single responsibility princple** of object oriented design.
	- Every object in our system should have a single responsibility, and all the object's services should be focused on carrying out that single responsibility.

Here is a method to spot multiple responsibilities within our designs:
1. Write a list of "The (blank) (blanks) itself" for every method in the class we are testing.
2. In the first blank of each line, write down the class name. In the second blank, write down one of the methods in the class.
3. Now ask: does our class really have the responsibility that the method indicates it does? Does it make sense?
	- i.e. there are no associations with other classes when a method tries to do something.

We want to avoid the **ripple effect**, where one small change to our software can cause a ripple of changes throughout our code.
- Follow **DRY**, *Don't Repeat Yourself*.

## Object and Class Hierarchies
*It is generally good practice/design to pass in entire objects as arguments instead of constructing an object within another object class*.
- Use subclassing for subtyping... "is-a"
- Use within a class for a "has-a" relationship

Interfaces allow more flexibility for testing!

If you encounter an unplanned task as a result of redesign, you make it a planned event by putting it up on the Big Board.

Remember that one of the tasks is demoing the software itself!

## Refactoring
It is the process of modifying the structure of our code *without* modifying its behavior, and is likely related to a specific improvement in our design.
- Usually we refactor in order to follow the SRP.

# Scenarios
Are in non-technical language for the customer.
- Helps us uncover requirements and ambiguity.
- Implicitly highlights benefits of app features.
- Exhibits common real-world progressions.
	- Emphasize what gets tested...
	- ...and omit the tons of things that don't need to be tested.
- "End-to-End" stories are where there are 2+ scenarios within a story.

**Personas** complement scenarios. They're different than *roles*.
- e.g. a "networking nancy" or a "shy sam"

#### Good Practices
- Visiting the customer/user locations to observe real scenarios and interview participants.

# Behavior-Driven Development (BDD)
Two parts: the [[Requirements#^5775c3|User Story]] and its [[Requirements#^cc8c13|BDD Scenarios]].
- BDD scenarios aren't *Scenarios*.
Compare this format to the user story format:
- BDD Scenario: what's different
	- Given context,
	- when event,
	- then outcome.
- Remove all vagueness present in a user story in the BDD scenarios!
- Also known as *Acceptance Tests*
- There are as many BDD Scenarios as the number of unique progressions *into* and *out of* the feature. 
	- Consider that two "givens" may be functionally identidal for a certain "when/then"
	- *Each Scenario should be covered by at least one matching automated story test*.

Might hire a **UI Design** specialist to draw up a plausible screenshot of our application.
- Also known as User Experience Design (UXD). Not called "usability" anymore