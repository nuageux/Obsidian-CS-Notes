#Data-Structure
## Data Structures

- Collections containing:
    - Data values
    - Relationships amongst the data
    - Operations applied to the data
- Describes _exactly_ **how** the data are organized and **how** tasks are performed
- BSTs, Heaps, and Linked Lists are all Data Structures

## Abstract Data Types

- Defined by its behavior from the view of the _user_
    - i.e. what operations _must it have_?
- Describes only what _needs_ to be done, **not** _how_ it is done
- Stacks and Queues are examples of Abstract Data Types

### DS Ex: ArrayList

- ArrayLists need to have a backing array of some sort
- needs to have a count that keeps track of how many items that are added to the ArrayList
- Basically, the ArrayList defines how it’s gonna do all the stuff the List ADT requires a List to do

### ADT Ex: List

- **add** elements
- **find** an element in the List
- **access** a specific element in the List
    - perhaps by index
- **remove** elements
- know the **size** of the List
- should be ordered