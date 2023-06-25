#CogSci 
Presented by Dr. Gary Cottrell

#### Intro
The brain is made up of $10^{11}$ to $10^{12}$ neurons which make up about $10^{14}$ to $10^{15}$ connections, and all these neurons do is send and receive simple electrical symbols. So how does it make a mind?
- We can try to take measurements:
	- Measuring behavior by getting an idea of the way the brain takes input and turns it into output.
	- Measure brain waves using electrode caps.
	- Measure brain activation with magnets.
	- Record neurons while the brain is performing some task.
	- Record neurons of surgery patients.
- We can try to build a working model with the data above ($\rightarrow$ computational cogsci!).

**The "Halle Berry" Neuron**, which somehow identifies Halle Berry in most forms presented where a computer would have difficulty. A high-order, specific neuron.

### The 3 Axioms of CogSci
1. The mind is what the brain does.
2. What the brain does (thinking) is a kind of computation.
3. The kind of computation the brain does is *probabilistic* (which corresponds to the uncertain nature of the world).

### What is a "Working Model"?
These models won't replace what they simulate (yet), but they can still work and do useful things.
- Ex: AI's can do stuff like facial or language recognition, even if not as well as a human.

## Motivation
People are still "smarter" than machines, not because we have faster hardware or better software, but because of our **brains**, which are parallel machines capable of operating on a *massive* scale.
- Brains are different than computers, so we have to make computer programs that emulate the brain.
- A neural net is a *brain-like* computational model! ^3762a0
	- We can then therefore "train" these neural nets, and the ability to learn is incredibly useful.

## Human-Style Computation
People can combine **lots** of different kinds of knowledge **quickly**!
- Ex: Understanding the relationships in an English sentence.
- Ex: How the most frequent words (in any language) turn out to be the most **ambiguous**!
- Ex: Filling in the gaps in images!
- Ex: Recognizing faces!
	- Incidentally, we are better at recognizing upright faces than upside down faces (the Thatcher Effect).

## Neural Nets
Represented as nodes that accept inputs and transmit outputs (in terms of firing frequency) which have connection strengths (or "weights").

Are networks of simple units connected by weighted links which compute by spreading activation and inhibition.

#### The Interactive Activation Model
- Word Level
	- Is activated by letters that are compatible.
	- i.e. a letter will vote for words that contain it and will vote against words that don't.
	- Furthermore, word level nodes feed *back* to the letter nodes which "voted" for them, explaining us guessing letters based on context.
- Letter Level
	- The features below excite compatible letters and *inhibit* incompatible ones with inhibitory links (marked by circle heads) and excitatory links (marked by pointed heads).
	- Whatever letter gets the highest excitatory value is expressed.
- Feature Level
	- Little "bar detectors" which we know exist in the first stop in the visual parts of our brain.
	- There are enough of these to represent every letter, and are copied to make bar detectors for each letter in a word.

"*Stable Coalitions*" are when *context influences perception* and an unexpected result wins the "election" in the neural network and makes it to consciousness.

The "word superiority effect" describes how we as humans are better at seeing letters when they are part of a word than when they are in a non-word letter string.