#Data-Structure ^5653b2
## Data Structures

^7728a3

- Collections containing:
    - Data values
    - Relationships amongst the data
    - Operations applied to the data
- Describes _exactly_ **how** the data are organized and **how** tasks are performed
- [[Binary Search Trees|BSTs]], [[Heaps]], and [[Linked Lists]] are all Data Structures
#### DS Ex: ArrayList
- ArrayLists need to have a backing array of some sort
- They need to have a count that keeps track of how many items are added to the ArrayList
- Defines *how* it will implement the functionality the List ADT requires

## Abstract Data Types (ADTs)

^412b3e

- Defined by its behavior from the view of the _user_
    - i.e. what operations _must it have_?
- Describes only what _needs_ to be done, **not** _how_ it is done
- [[Stacks and Queues]] are examples of Abstract Data Types

#### ADT Ex: List
- **add** elements
- **find** an element in the List
- **access** a specific element in the List
    - possibly by index
- **remove** elements
- know the **size** of the List
- should be ordered