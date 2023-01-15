#Machine-Learning 
Picking the right distance function suited for the data one is working with makes all the difference.
## $l_p$ Norms
- Are a small set of distance functions that arise a lot in machine learning.
- $l_p$ refers to a distance metric.
- $p = 2$ refers to Euclidean distance.
- For every $p \geq 1$, there is an $l_p$ norm.
	- ![[Pasted image 20230113103746.png]]
- Note that $l_1$ is just summing up the absolute difference along each coordinate.
- $l_{\infty}$ just takes the coordinates where the difference is largest.

## Distance Metrics
- Let $\mathcal{X}$ be the space in which data lie.
- A distance function is a **metric** if it satisfies certain properties:
	- ![[Pasted image 20230113103157.png]]
	- i.e. the distance function can take any two objects and output a "distance" between them.
	- Making one's distance function as a metric is helpful because there are versions of the $k$-d tree (called ball-trees and cupboard-trees) that work on metrics.
	- Of course, all the $l_p$ norms are metrics.
- An example of a non-metric distance function is the **Kullback-Leibler divergence** ("relative entropy") is 
	- ![[Pasted image 20230113103448.png]]
	- This works on distances between probability distributions.
	 
