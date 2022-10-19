#Management #Project
What do we do when our [[Requirements#^80311d|estimates]] are too big?
- Stay customer-focused. [[The Customer]] sets the priorities.

### Milestone 1.0
It is the first major release of the software to the customer.
- Software is *actually delivered*.
- We are expected to be paid for Milestone 1.0.
- We must help the customer understand what can be done in the time available.
	- User stories that didn't make 1.0 aren't ignored, just postponed until the next milestone.
- If the features wanted can't fit in 1.0, the customer must reprioritize again.
	- Cut out more functionality.
	- Ship a milestone build ASAP.
	- Focus on *baseline* functionality (the *minimum viable product*).
		- Partly being clever to minimize the baseline.

Remember to have iterative product delivery, to be realistic, to be quantitative (have numbers), and to make measures visible.

## More People?
More people doesn't necessarily mean a (proportionately) shorter project time. 
- Each new team member needs to:
	- get up to speed
	- understand the software and technical decisions
	- how everything fits together
	- ...which all takes time.
- The recommended approach to increasing team size is to monitor the team, and when the team actually gets **less** productive despite more people, re-evaluate the amount of work to do or the amount of time to do it.
- Principle: Adding new members to a late project will make it even later.

## Ideals vs. Reality
Consider **velocity**. Given a number of days, how much of that time is productive work?
- It's common to initially assume a velocity of 0.7 and adjust upwards if the team shows greater productivity.
	- This implies that we must readjust our velocity for the next iteration estimate calculations!
	- Velocity typically *slows down* as iterations go by because the codebase gets more complex as a project progresses!
- (Days of Work) / (Velocity) = (Days required to get Work Done)
	- The Days required should always be BIGGER than the original days of work estimated!
	- Give yourselves more days in the iteration than this result to give you some (even more) leeway.

In reality, programmers give incredibly optimistic estimations of time required for a task. *Real life often gets in the way*, so make a more conservative estimate!
- Don't consider complete surprises when planning for delays in productivity (like natural disasters or freak coincidences).
- Don't consider missing skills; put in a "Developer story" to deal with the learning instead.
- Don't consider uncertainty.

At this point we can divide the days of work by the number of programmers to get an iteration/milestone estimate.
- Deal with velocity *before* breaking into iterations!
- Usually there's no shot you get 8 hours of work in a day, typically *3*.
- ...and the solution *isn't overtime!* That kills morale and causes more mistakes/burnout!

#### How to Manage Pissed ("Unhappy") Customers
We oftentimes can only be honest with the estimate that comes out. The customer makes the decision if they want to go through with the project or not.

We could try:
- Adding an iteration to Milestone 1.0 and ask the customer for more time
- Explain that the overflow work isn't lost, just postponed
- Be transparent about how the estimates were made.

*Promise and deliver rather than overpromise and fail.*

A **Burn-Down** graph plots the amount of days left until the deadline (x-axis) to the amount of work left in days (y-axis) (to get a line with negative slope). ^d67e24
- Plotting above the line means behind schedule (and vice-versa).
	- Just remember that "over" = bad.
- With every task completion, plot a point.
- Good for knowing when things are going poorly.