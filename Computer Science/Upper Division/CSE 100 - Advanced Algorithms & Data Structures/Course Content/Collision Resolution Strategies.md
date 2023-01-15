#Practical 
# Collision Resolution Strategies

## Open Addressing (Linear Probing)

A way to deal with collisions.

-   If the slot you want to insert in is already taken, just check the next slots (until you find an empty one).
-   For find, you linearly probe until you find the element or come to an empty slot (you would’ve found it in a consecutive non-empty spot had it existed in the table).
-   If the backing array is full, we have to create a new, larger array and reinsert the elements from the original array into the new, bigger array.
    -   We must remember to deallocate the original array once we’re done with it.
    -   In fact, we don’t want to resize when the array is full. We want to resize **when we hit the load factor**!
-   Big-$O(n)$ in the worst case, but is constant time in the average case provided we designed the hashing algorithm to have most likely a constant number of collisions.

## Double Hashing

We’ll call grouped elements that must be linearly probed through (in order to insert an element that is hashed somewhere within this group) a “clump”.

-   Clumps are bad for performance!
    -   The bigger the clump, the longer we have to iterate over it, and the higher the probability that we’ll land on the clump in the first place!
-   To try to minimize clumps, we use the “double hashing” technique. We will use a second hash function that is used to determine the “skip”, how many spaces over to travel when checking for the next empty slot.
    -   Notice how for linear probing, the skip was 1 slot.
    -   A _common_ double hash function is $h_2(x)=1+(h_1(k)/m)$ % $(m-1)$.

## Closed Addressing (Separate Chaining)

Where all the buckets of the Hash Table are another data structure (commonly a linked list).

Must be recognized that if there’s a non-empty structure at the hashed bucket, the bucket may already contain the element.

-   So, there must be a find operation to check before insertion. In the case of a linked list, this is in linear time.
-   As opposed to linear probing (where probability of collisions always goes up with insertion), having collisions do not increase the future probability of more collisions.