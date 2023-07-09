#Project #Management 
# a.k.a. Development
Importantly, the work to do is *more granular* than our user stories. The user stories were *for the user*, but in reality, user stories are a collection of specific **tasks**, small bits of functionality that combine together to make a user story.
- A task is done by *one developer*. A task has a:
	- Title to refer to
	- Rough description with details
	- Estimate
- When [[Planning|estimating]], rely on the task estimates to make the user story estimates.
- Performed by *one* person, typically the one most technically oriented to the job (or someone who stands to learn the most from the experience!).
- Are the "leaves" of the Agile development "tree"!
- Manages the tradeoff between cost of shipping and value of feedback.

**Back-end** work tends to be the most difficult. E.g.
- Interfacing to APIs
- Database Schema
- Complex multi-threading
- etc.

Typically, we want a task each for
- Core feature code
- UI
- Back-end (and highball the estimate!)
	- Can even include a task for learning the API
	- If we identify multiple skills in a back-end task, it's probably two tasks!
- Writing Story tests

The **Big-Board** and [[Planning#^d67e24|Burn-Down]] charts referenced before *are only for a single iteration*. 
- In the *In Progress* area of the Big-Board, only tasks that are *actually being worked on* belong there.
- Sometimes two tasks should be worked on at once, as they complement one another.

# Agile Planning/Execution
How do we split up work?
- We could split stories up, but it's also very valuable at the beginning of a project for all developers to work on the same story to gain momentum.

Again, *Effective Measurement requires Visibility*.

### Standup Meetings
A quick, frequent meeting of all members of the team where we:
- Track progress
- Update the burn-down rate
- Update tasks
- Talk about what happened yesterday and what's going to happen today
- Bring up any issues
- Last between 5-15 minutes.
- What was accomplished and *learned*, what were/are obstacles and goals.

#### Post-Mortem
What we learned from the iteration after it's done.
- Adjust velocity for next iteration
- Recognize successes and failures
- Tweaking the process