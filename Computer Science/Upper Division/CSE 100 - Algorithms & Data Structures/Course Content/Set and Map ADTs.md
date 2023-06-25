#Data-Structure 
## The Set ADT

- Stores multiple elements (keys)
    - `find(x)`: True if `x` exists in the set, otherwise false
    - `insert(x)`: Add `x` to the set
    - `remove(x)`: Remove `x` from the set
- Lexicon is a type of set that stores strings (words)

## The Map ADT

- Stores multiple `(key, value)` pairs
    - `get(k)`: Returns the value associated the key `k` if `k` exists in the map
    - `put(k, v)`: Map the key `k` to the value `v`
    - `remove(k)`: Remove key `k` and its value from the map

## Implementing the Set and Map ADTs

- Use anything... think of the time complexities for yourself
- In C++, `set`s are implemented with Red-Black trees, while `unordered_set`s are implemented with hash tables.