#Parallel-Computing 
### Processing an Image with a 2D Grid
- The most likely case is that the image we are working with is smaller than the bounds of the thread grid we are using (as opposed to fitting perfectly coincidentally).
	- Thus, we need to check when accessing threads whether the thread we are accessing is within bounds.
		- e.g. testing if the thread col is < image width, or if the thread row is < the image height.
- In-class example: Grayscale conversion

## Image Blur
- It is the simplest type of **convolution**.