#Theoretical 
# Coding Trees and Entropy

## Message Encoding

Everything is stored in binary in a computer.

Convert (**encode**) media into binary strings and similarly revert (**decode**) it back to the original media.

ASCII is a common way to encode characters of the latin alphabet.

A mapping helps us encode and decode.

## Coding Trees

We use a trie to show what sequence of digits leads to the character we want to en/decode.

## Information vs. Data

Information is the content of some message.

-   It tells us detail(s) about some systems(s).

Data is a raw unit of information.

-   It is a representation (or encoding) of information.

## Entropy

-   It is a measure of disorder (non-uniformity) of a system.

Then, Shannon Entropy is the expected value (average) of the information contained in some data.

-   If there are $n$ possible outcomes, we get $\log_2(n)$ ceiling bits of information.

Uniformity is the lack of variation among symbols in a message.

-   The more uniform data is, there is less entropy and less information.