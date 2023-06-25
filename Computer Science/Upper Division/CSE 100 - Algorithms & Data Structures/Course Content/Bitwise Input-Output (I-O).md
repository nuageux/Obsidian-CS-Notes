#Practical 
# Bytewise I/O
Disk access is super slow, so it wouldn't be smart to write to disk one byte at a time.

Here's the model we will use instead:
Memory --bytes-> Output Stream --bytes-> Buffer --4KB-> Disk
- The buffer is only written to disk when it is full (to minimize the number of disk accessing actions).
- Reading from disk uses a very similar process.

When writing to disk, we have to do one last flush of the buffer, just in case there is still data within it.

# Bitwise I/O
The smallest unit in a computer is a byte. How can we work around this to use bits?
- Just make another bitwise buffer before sending to the output stream (which requires bytes)!
 
Again, reading is similar. We read the conventional 4 kilobytes from disk, send to bytewise buffer, to input stream, to bitwise buffer from where we read 1 bit at a time.
- When the bytewise buffer is empty, read from disk again.

# Reading from a Bitwise Buffer
How to read the byte in the bitwise buffer from left (most significant bit) to right (least significant bit):
- Have a "current" value to track the index (starting from 0).
- To get the value, we will right-shift the bit according to the current index:
	- `buf >> (7-c)`
	- Then just increment the index storing variable, and when `current == 8`, we read in the next byte then reset current to 0.

# Writing to a Bitwise Buffer
Same deal: we want to write to the buffer from left to right.
- This time, we want to left-shift our bit to the correct position in the buffer. `b << (7-c)`, then OR `b` with whatever's in `buf`.
	- i.e. `buf = buf | (b << (7-c)` 
	- Then increment the index variable as usual.
	- When the buffer is full, write to disk and then reset the buffer to `0000_0000`. Reset index variable.