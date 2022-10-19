#Proof #Theoretical 
## Context
It turns out that all regular languages have a particular property, called the "pumping lemma". It then follows that we can prove a language is non-regular by proving that the language in question does not satisfy this property.

## What is it?
The property in question states that all strings in the language can be "pumped" if they are at least as long as a certain special value called the "**pumping length**".
- i.e. each such string contains a section that can be repeated any number of times with the resulting string remaining in the language.

### Formally,
If $A$ is a regular language, then there is a number $p$ (the pumping length) where if $s$ is any string in $a$ of length at least $p$, then $s$ may be divided into three pieces, $s=xyz$, satisfying the following conditions:
1. for each $i \geq 0$, $xy^iz \in A$,
2. $|y| > 0$, and 
3. $|xy| \leq p|$.

Note that $x$ or $z$ may be $\varepsilon$, but not $y$. Furthermore note that condition 3 is added as it is useful for...

Note that the pumping lemma *does not prove regularity*! It is just a property that regular languages have. 

## Strategy
Proving a language is non-regular with the pumping lemma is a proof by way of contradiction.
1. Assume to the contrary that $C$ is regular. Let $p$ be the pumping length given by the pumping lemma.
2. Choose ANY SINGLE string $s$ longer than length $p$, usually with parts whose lengths are factors of $p$.
3. Select ANY ONE valid partition of $s$ into $xyz$ such that $xy$ isn't longer than $p$.
4. Now, for **EVERY POSSIBLE** parition of $y$ (given the partition set up previously), prove that for **even one** $i$ in $xy^iz$, it breaks the original rules of $C$.
	- We must consider all partitions of $y$ because it is more than likely that $x$ and $y$ were defined ambiguously, and thus we consider all possible $y$'s in this ambiguous partition.
5. Conclude.