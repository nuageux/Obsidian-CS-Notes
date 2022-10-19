#Project #Management 
*Blueskying* is the industry buzzword for brainstorming. The general rule is to have as many people involved in the brainstorming process as possible and record any and all ideas. This includes the customer and stakeholders!
- The book recommends role-playing how the customer imagines users interacting with the software or simply observing how people work to see how the software would fit in.

# User Stories

^5775c3

Are written in the customer's language and is a story about how the users interact with the software being built.
- *From the customer's perspective!*
- The customer must be able to understand the user story!
- Each user story describes *one thing* the software needs to do.
- Should be short and concise.
- Keep the customer involved here.

Also can be referred to as a "*Behavior-Driven Development* (BDD) Story".
- The narrative is as follows:
	- "As a [role], 
	- I want [feature]
	- So that [benefit]."
- The acceptance criteria is presented as a series of **BDD Scenarios** which are structured as follows: ^cc8c13
	- Given [context] (and [some more context])...
	- When [event]
	- Then [outcome] (and [another outcome]).

### Estimating

^80311d

Estimates must be defined for each user story for how long it will take to implement each one.
- To generate as accurate estimates as possible, have the development team independently come up with their own estimates for each user story (*Planning Poker*).
	- The larger the difference between estimates, the less confident the team is in the estimates. This means that there are more assumptions that must be rooted out.
- Remember that iterations are often about 20 working days; try to keep user stories to a fraction of an iteration to fit in multiple user stories.
- The team should feel **confident** in the final estimate and **comfortable** with the assumptions made.

For the purposes of this class, estimate in hours *in powers of 2*.
- If the estimate is > 32 hours, consider splitting it up further.

**Assumptions are very, very bad, and as many should be eliminated as possible.**
- Any surviving assumptions become **risks**.
- Although we should talk with the customer often, we must also *respect their time*.