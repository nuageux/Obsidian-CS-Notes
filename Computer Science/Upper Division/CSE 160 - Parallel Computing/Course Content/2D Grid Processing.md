#Parallel-Computing 
### Processing an Image with a 2D Grid
- The most likely case is that the image we are working with is smaller than the bounds of the thread grid we are using (as opposed to fitting perfectly coincidentally).
	- Thus, we need to check when accessing threads whether the thread we are accessing is within bounds.
		- e.g. testing if the thread col is < image width, or if the thread row is < the image height.
- In-class example: Grayscale conversion, a type of loop unrolling

## Image Blur
- It is the simplest type of **convolution**.
- For each pixel, take a window around it and take the weighted average of the color to assign a new color for that pixel.
	- For a blur, that weight is 1 (no weight).
	- Those weights are what a neural network learns.
- Within a convolution, we take advantage of locality, because we reuse pixel memory locations within our calculations.

## Balancing FLOPS and Memory Bandwidth

