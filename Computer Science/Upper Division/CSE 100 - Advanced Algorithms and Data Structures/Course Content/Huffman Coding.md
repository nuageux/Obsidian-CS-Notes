#Algorithm #Data-Structure #Theoretical 
# Data Compression
Can we make the data size smaller while maintaining the same or similar information?
- Lossless compression
	- What is covered in this course
	- Can perfectly reconstruct the original data given the compressed data
	- We can use what we learned from entropy to compress data as much as possible
		- In a DNA string, although it could be represented as ASCII, note that there are only 4 letters in the alphabet.
			- Therefore, $$\log_24 = 2 $$ and only 2 bits are required per letter.
- Lossy compression
	- Compresses more than lossless, but sacrifices some of the original data
	- What is reconstructed is hopefully similar enough to the original data
# Prefix Codes

^4fd4d2

An encoding in which no symbol is represented by a code that is a prefix of the code representing another symbol.
- Essentially, if no encodings are prefixes of other encodings, we can encode different lengths for different characters and still be able to unambiguously decode a compressed string.
- i.e. there is no overlapping decodings when we're decoding!

A given code is a prefix code _**iff**_ we can construct a coding tree (where symbols may only be leaves) for the code.

# A Lower-Bound on Data Compression
The equation for Shannon Entropy is $$\Sigma_x p_x \log_2(\frac{1}{p_x}) $$
- Summing over all unique symbols $x$ the probability $p$ of seeing that symbol times the corresponding logarithmic function.
- This requires we compute the frequency of characters in the string we wish to encode. 
# Huffman Tree Construction
This algorithm allows us to always achieve the lower-bound for bits per message for a specific message.
1. Compute frequencies of symbols in message
2. Start with a "forest" of single-node trees (symbol, frequency)
	- May be considered as the current "top layer" being considered
3. While there is more than 1 tree in the forest:
	1. Remove 2 trees with the lowest frequency ($T_1$ and $T_2$) from the forest
	2. Create new node with frequency = $T_1$'s frequency + $T_2$'s frequency to be their parent
	3. Insert this new node into the forest

# Huffman Encoding
Simply follow the Huffman Tree as we would for a normal coding tree.

A way to implement this could be to somehow map symbols to the leaves on the tree, push the encoding characters as we travel up the tree to the root, then pop all the characters from the stack to get the encoding for that symbol.

# Huffman Decoding
Similarly trivial; because our Huffman encoding is a [[Huffman Coding#^4fd4d2 |prefix code]], all we have to do is traverse down the tree for each input, record the leaf symbol, then repeat (traversing again from the root) until we are done reading input.


