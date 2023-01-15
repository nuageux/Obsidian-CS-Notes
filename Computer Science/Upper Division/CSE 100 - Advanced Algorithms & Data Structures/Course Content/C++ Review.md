#C-plus-plus
# C++ Review

## C++ Data Types

-   Can be signed or unsigned
-   5 Integer types
    -   char [1 byte]
    -   short [2 bytes]
    -   int [4 bytes]
    -   long [8 bytes]
    -   long long [16 bytes]
-   3 Floating Point types
    -   float [4 bytes]
    -   double [8 bytes]
    -   long double [16 bytes]
-   1 Boolean type
    -   bool [1 byte]
-   The byte sizes listed are **not** guaranteed! They are _usually_ those sizes.

### `string` type in C++

-   Is mutable! (as opposed to Java)
-   We can only concatenate other strings, though (unlike Java)
    -   Gotta convert other things into strings or use a “stringstream”.
-   The substring method is different, too.
    -   `s.substr(beginIndex, lengthOfSubstring)`

### Comparing Objects in C++

-   We can use the relational operators `==`, `<`, etc. to compare objects!
    -   This is because unlike Java, the operators are overloaded.

## C++ Variables

-   Variable initialization **isn’t** checked in C++!
    -   `int fast; int furious; int fastFurious = fast + furious;` Wouldn’t cause a compile error but will still ruin your code! We will get undefined behavior.
-   “Narrowing” **isn’t** checked in C++!
    -   It will let us put an integer value in a short without typecasting, but there will be overflow.
    -   We must typecast (valid) values ourselves.
-   We can declare variables outside of a class.
    -   These are **global variables**. Anything in the file can access it.
    -   Is poor practice.

## C++ Classes, Source Code, and Headers

### Classes

```cpp
class Student {
	public:
		static int numStudents;
		
		Student(string n);

		void setName(string n);
		string getName() const;

	private:
		string name;
};

int Student::numStudents = 0;

Student::Student(string n) { /* CODE */ }

void Student::setName(string n) { /* CODE */ }
string Student::getName() { /* CODE */ }
```

-   Note the `public` and `private` “regions”.
    -   We can declare constructors or methods in this region without defining their code/implementation!
-   Outside the `class` curly braces, we can implement methods and also initialize static variables.

### Member Initializer List

-   A fast way to write the constructor.
-   Ex, when there are `private` instance variables `int x;` and `int y;`: `Point::Point(int i, int j) : x(i), y(j) {/* EMPTY */}`

### Source vs. Header Files

-   `.cpp` for source files and `.h` for header files.
-   The header file contains just the class and declarations.
-   The source file contains all the static initialization and method implementation.
-   We can just send the header file to someone for them to get an idea of how the program works _without_ having to see any of the source code!

## C++ Memory Diagrams

-   Objects in C++ can contain other objects!
    -   As opposed to Java, whose objects can only contain references to other objects.
-   Furthermore, when naming an object during creation in C++, the name _is_ the object.
-   Ex: `Student s1("Niema");`
    -   `s1` _is_ the `Student` object here!
-   Ex: `Student s2 = s1;`
    -   This creates a brand new `Student` object named `s2` that is a copy of `s1`!

### References

-   Totally different from Java.
-   “Another name for the exact same object.”
    -   Creating a reference to an object means the reference _is_ the object now, too, just as above.
-   `[type] & [var name] = [...];` is how to create a reference.

### Pointers

-   _Are_ similar to Java references.
-   `[type]* [var name] = &[object name];` is how to create a pointer to an object, where the `&` here means “get the memory address of this object”.
-   We can nest pointers within each other.
    -   Ex: `Student** ptrPtr = &ptr;`, where `ptr` is a pointer to a `Student` object.
    -   “A pointer to a pointer to a `Student`.”
-   **Pointers are objects, too!**
-   We can _**dereference**_ pointers.
    -   Ex: `*ptr` is equal to whatever `ptr` was pointing to.
    -   “Arrow Dereferencing”
        -   Ex: `ptr -> name` is equal to the name instance object of whatever `ptr` was pointing to.

### Memory Management

-   If we create an object without the `new` keyword, memory is automatically allocated on the runtime stack.
    -   So once the method containing a constructing command without `new` finishes, it is destroyed (as the runtime stack clears out).
-   If we _do_ use the new keyword, we are using “_**dynamic memory allocation**_”.
    -   We have to use `[type]*` with the `new` keyword, because using `new` returns the memory address of the object we created.
    -   _**We are responsible for destroying objects we make with**_ `new` _**when the method returns!**_
        -   Otherwise we get a **memory leak**.
        -   We use `delete [pointer]` to keep our memory management pristine.

## C++: The `const` Keyword

-   Means “this variable can never be reassigned”.
-   Examples:
    -   `const int a = 42;`
        -   `a = 41;` would **not** work! [compile error]
    -   `int const b = 42;`
        -   Is actually functionally identical to the format above.

### `const` and Pointers

-   `const int * ptr1 = &a;` means that `a` cannot be modified!
    -   i.e. whatever a `const` pointer is pointing to cannot be modified.
    -   We can actually change what the pointer is pointing to! (And thus what cannot be modified.)
        -   Like a lock.
    -   `int const * ptr2 = &a;` is the same thing.
-   `int * const ptr3 = &a;` means that we can’t change what `ptr3` points to!
    -   We can, however, change the value of what is being pointed to.
-   `const int * const ptr4 = &a;` is combining the two above concepts.

### `const` and References

-   `const int & ref1 = a;` means we cannot modify the variable _through_ the `const` reference.
    -   i.e. we can’t use `ref1`, the variable name, to alter `a`.
-   `int const & ref2 = a;` is the same as above.

### `const` Functions

-   Comes after the method declaration. Ex: `string getName() const;`
    -   Means this function **cannot** modify the object (as a rule).
    -   Means this function can **only** call other `const` functions.

## C++ Functions

### Global Functions

-   Functions implemented outside of a class!
-   There must always be a `main` (global) function with return type `int`.
    -   The returned integer signifies the exit status.
        -   0 means we’re good, anything else means something went wrong.

### Passing by Value vs Passing by Reference

-   2 ways of passing variables into a function.
-   by Value:
    -   Copies of the arguments are created for use in the method.
    -   The original variables will be unaltered after method return.
-   by Reference:
    -   Takes in references to variables (the actual object!), which lets us make lasting changes to variables within our method.
    -   Directly modifies the previous stack frame (not copies).

## C++ Vectors

-   Basically “the best of both worlds from Java’s arrays and `ArrayLists`.”
-   A dynamic array, initialized by `vector<[type]> [name];` which is initially empty.
-   Add values with the `[vector name].push_back([value]);` method.
-   Remove values with the `[vector name].pop_back();` which removes the last element in the vector.
-   Element access is the same as Java arrays, with brackets with the index in between them. Ex: `a[0]` accesses the first element.
-   There are no “out of bounds” errors for accessing an index beyond the length of the vector.
    -   We will, however, end up accessing the next memory location(s), which contains god-knows-what (lol) or an illegal memory address (which is probably reserved for important things).
-   Are stored one after the other in memory (contiguous).
-   Assigning a vector to another vector will create a new vector and copy all the elements of the former to the new vector.

## C++ Input/Output

Hopefully we’re familiar with input streams, output streams, `stdin`, `stdout`, and `stderr`.

-   To access `stdout`, we use `cout << [what to output];`.
-   To access `stdin`, we use `cin >> [what to input];`.
-   To access `stderr`, we use `cerr << [error message] << endl;`.
-   In C++, the input stream is `istream` and the output stream is `ostream`.
    -   `stdin` is an example of an `istream`, and `stdout` and `stderr` are examples of `ostream`s.
-   We use the `getline(cin, message);` to read an entire line from `stdin`.
-   We use `cin.fail()` to check if the prior command caused some sort of error.

All of these keywords are part of the `std` ”namespace”.

-   Without `using namespace std`, we’d have to include `std::` in front of all of these keywords.
    -   Ex: `std::cout`

## C++ Templates

We want the freedom to use any data type within the data structures we implement in this course.

-   We will use “generic programming”.

```cpp
template<typename Data>
class Node {
	public:
		Data const data;
		Node(const Data & d): data(d) {}
};

// ** //

// examples of Nodes with chosen data types
Node<string> a(s);
Node<int> b(n);
```

-   Hopefully what is going on here is apparent.