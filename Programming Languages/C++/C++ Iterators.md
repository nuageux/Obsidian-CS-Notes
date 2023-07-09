#C-plus-plus 
## Motivation for Iterators

```cpp
for (string name : names) {
	cout << name << endl;
}
```

- What kind of data structure is `names`? It doesn’t matter! Iterators make this possible.

## Iterating Over Arrays

```cpp
void print_inorder(int * p, int size) {
	for (int i = 0; i < size; ++i) {
		cout << *p << endl;    // dereferencing p
		++p;                   // pointer arithmetic. refer to CSE 30
	}
}
```

- Dereferenced pointer, used data, then incremented pointer.
- Works because the array is a contiguous structure (memory locations are back to back).

## Using Iterators

```cpp
vector<string> names;
/* populate with data */

vector<string>::iterator itr = names.begin();
vector<string>::iterator end = names.end();

while (itr != end) {    // the != is overloaded for the iterator class.
	cout << *itr << endl; // the dereference * is overloaded.
	++itr;                // the preincrement ++ is also overloaded.
}
```

- Linked List example, with lots of overloading

## Creating an Iterator Class

- We should be implementing Iterator classes within our data structures.

We must:

- Overload some operators in the Iterator class
    - `==`, should be true if the iterators are pointing to the same item.
    - `!=`, opposite of above
    - `*` (dereference) return a reference to the current data value
    - `++` (pre-increment) and `++` (post-increment) should move our iterator to the next item
- Implement some functions in the Data Structure class
    - `begin()`, which returns an iterator to the first element
    - `end()`, which returns an iterator to _**just after**_ the last element.