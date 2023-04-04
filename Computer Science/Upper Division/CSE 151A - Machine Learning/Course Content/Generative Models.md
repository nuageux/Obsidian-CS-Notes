#Machine-Learning 
# Classification using Generative Models
- Requires background in probability and linear algebra.
- The learning process:
	- Fit a probability distribution to each class, individually.
	- Look at just one set of points at a time and fit a distribution to each of them.
- To classify a new point, we ask which one of the distributions was the new point most likely to have came from?
	- Which distribution *assigns higher probability* for this new point?
- So for each class, we need the probability of that class *and* its distribution of data within itself.
	- These two pieces of information gives us the **joint distribution**.

## Generative Modeling in 1 Dimension
- Example: Identifying the winery of a bottle of wine.
- The **univariate Gaussian**.
	- ![[Gaussian Equation.png]]
	- It's the normal bell curve.

## The Multivariate Gaussian
- We want probability distributions over $d$ dimensions.
- We simply extend the mean and covariance matrix to cover those $d$ dimensions.
- Estimate class probabilities, then fit a Gaussian to each class. 