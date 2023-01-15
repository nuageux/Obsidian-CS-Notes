#Math 
## Matrix Algebra Review
- 3D Model
	- Has an array of position vectors describing its shape
	- Each vector has 3 components: $x, y, z$
- A **translation** is a movement of the model.
	- Compute a new array of positions representing the new location.
	- If $d$ represents an offset, we simply add that vector $d$ to our position array.
	- Remember that this is effectively a loop over the $n$ vertices.
- Rotation by angle $\theta$:
	- ![[Pasted image 20230112170616.png]]
	- ![[Pasted image 20230112170650.png]]
	- i.e. the rotation matrix times the 3D vector.