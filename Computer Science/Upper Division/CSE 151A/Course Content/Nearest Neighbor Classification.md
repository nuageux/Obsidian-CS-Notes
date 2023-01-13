#Machine-Learning
### Machine Learning Approach
- To contextualize, the problem to be solved will be the classic "identify handwritten numbers" problem.
	- "Given an image of a handwritten digit, say which digit it is."
	- The U.S. Post Office was interested in this!	
- For classification problems, specify the problem through examples!

## Nearest Neighbor Classification
- The famous MNIST data set of handwritten digits
	- Assume a **training set** of 60k images and their labels.
	- Assume a **test set** of 10k images and their labels.
- We'll call training images $x^i$, where $i$ is a number from 1 to 60k (i.e. a value in the training set). Furthermore we'll call the label (the "answer") $y^i$.
	- In this example, the labels are numbers in the range 0-9 (the *label space*).
- Idea: For a new image, just find within the 60k images the image that looks the closest to this new image and label it the same.
	- ...what does "closeness" mean? Let's define it:
		- Note that each pixel is grayscale from 0-255. The images in MNIST are 28 by 28, or 784 total pixels.
		- We rearrange the 784 pixels into one vector with 784 elements (the *data space*). Therefore, each vector element contains a greyscale value.
		- Use Euclidean distance, an extension of the Pythagorean theorem.
	- Finally, note that this algorithm is simple to implement; it's really just a bunch of for-loops.
	- The error rate on the training points is 0%, obviously.
		- In general, don't use the training error as a predictor of future performance.
	- Instead, we'll use the test error on the 10k images we specified earlier.
		- Turns out, it was 3.09% for this implementation and test set.

### Improving the Performance of NN
- 3.09% is too much.
- Let's try a "better" distance function.
	- Look for distance measures that are invariant under small translations and rotations (tangent distance).
	- Look for a broader family of natural deformations (shape context).
- Let's try $k$-NN.
	- Find the $k$ closest images, then take the most common label from among them. Weight the closest images to break ties, perhaps.
	- It turns out for the test set, the best choice of $k$ was 3.
	- Turns out, in settings where there isn't a clear answer, $k$-NN is good. Here, not so much.

## Cross-Validation
- In real life, there is no test-set!
- Looking back at $k$-NN, how do we decide which value of $k$ is best?
	- Let's try a "hold-out set".
		- Choose a subset of the training set as a "validation set".
			- The validation set should be a certain absolute size, not a percentage of the training set. 
				- It is related to how the absolute size of the sample matters, but not the percentage of the population (from statistics).
		- The problem is, it weakens our prediction (because we have less examples to work off of). Common-sense is correct here.
	- Let's try "leave-one-out" cross-validation.
		- For each image in the training set, find the $k$-NN *excluding the image itself*. This also extends from common-sense.
- Extend this idea: **10-fold** cross-validation.
	- Divide the training set into 10 equal pieces. Rotate one set to be the test set, 10 times.
	- Take the average of the errors found to get estimated error for a certain $k$.

### Speeding Up NN Methods
- The naive search takes $O(n)$ time for a training set of size $n$. That's slow.
- There are data structures for speeding this up and are included in standard Python libraries for NN, including: 
	- Locality sensitive hashing
	- Ball trees
	- $k$-d trees