- Use of a right-handed coordinate system.
- Recall that **a** refers to a vector aligned vertically (or a transposed horizontal vector).
- Recall that the *magnitude* of a vector is $|v| = \sqrt{v^2_x + v^2_y + v^2_z}$.
	- A vector with length 1 is called a unit vector.
	- Normalize a vector to generate a unit vector by dividing the vector by the magnitude.
- Dot Product
	- $a \cdot b = a_xb_x + a_yb_y + a_zb_z$ 
	- $a \cdot b = |a||b|\cos{\theta}$ 
		- Caveat: angle between two vectors is $\theta = \cos^{-1}(\frac{a \cdot b} {|a||b|})$ 
	- $a \cdot b = a^Tb$
	- If the dot product is positive, it's an acute angle between the vectors
		- negative means obtuse
		- and 0 indicates a right angle
	- If one of the vectors **u** has length one, then the dot product with vector **a** is the length of the "projection" of **a** onto **u**.
- Cross Product
	- ![[Pasted image 20230111105634.png]]
	- The result is a vector perpendicular to both a and b in the direction specified in the right hand rule.
	- It's asymmetric.  $a \times b = -b \times a$.
	- The magnitude is: ![[Pasted image 20230111130044.png]]
	- 