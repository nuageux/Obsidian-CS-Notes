# Linear Algebra
Covered in [[MATH 18 - Linear Algebra]] and [[MATH 20C - Calculus & Analytic Geometry]].

## Linear Algebra in Graphics
- Because we are dealing with the 3D world.
- What's related to graphics?
	- Distinctions between positions and directions.
	- In 3D, a 4th coordinate is needed to unify the algebra to preserve perspective.
- To learn:
	- Matrix Algebra
	- Vectors, change of basis, linear transformations
	- 3D rotations
	- Affine geometry
	- Projective geometry

## Matrix Algebra
- A matrix is a rectangular array of objects (numbers).
	- $m$ rows and $n$ columns
	- In GLSL or GLM, note that arrays are column based, **thus we declare elements of an array by column-row**.
- We are allowed to add matrices of the same size.
- We can multiply matrices if the number of columns in $A$ matches the number of rows in $B$ (and not vice-versa!).
	- The size of the resulting matrix is the number of rows in $A$ by the number of columns in $B$.
	- Row multiply Columns!
- Allows us to write linear systems of equations concisely.
- Associativity
	- We can move parentheses and brackets around within a multiplication operation.
	- Matrix multiplication is **not** commutative, i.e. order matters!
- Transpose
	- The matrix columns and rows swap.
	- Think of it as a diagonal reflection from the lower left corner of the matrix.
	- Note that transposition of a multiplication operation reverses its order.
- Identity Matrix
	- The $n$-by-$n$ matrix where 1 is the element down the diagonal from the top left to the bottom right.
	- Thus, multiplying by any other matrix gives back that same matrix.
- Matrix Inversion
	- If a matrix is invertable, it is unique such that the matrix times its inverse grants the identity matrix.
	- *Not all matrices have an inverse!*
	- Inverses also reverse the order of multiplication.

## Vectors
- Geometrically, a vector is an arrow with a magnitude and a direction.
	- An arrow over the top signifies that a vector is geometric.
- Algebraically, a vector is an array of numbers, an $n$-by-1 matrix ("column vector").
	- **Bold** signifies a vector is algebraic.
- *If you have both an arrow over the top and bolding*, then you have **an array of vectors**!
- Either way, both definitions work together to form a structured space called **vector space** sharing the same rules.
	- Geometric and algebraic vectors are mapped to each other using an array of vectors called **basis**.
		- A list of vectors forms a basis for a vector space if:
			- for each vector in the vector space, it can be created by multiplying the basis vector's members by a unique array of numbers.
		- Must be linearly independent (i.e. you can't make up a vector in the basis with the other vectors in the basis).
		- The number of vectors in the basis matches the dimension of the space.
	- A vector space is a set of objects (called vectors) with two operations:
		- Addition
			- Which must be associative and commutative
			- And there must exist a "zero vector" and the "unary inverse".
		- Scaling, such that multiplying by a constant grants another vector in vector space
			- Which must be distributive
	- These rules allow us to use **linear combination**.
	- **Note how the basis bridges the geometric and algebraic parts!**

## Change of Basis
- i.e. how to change the coefficient to compensate for a change in basis.
- See slides for the math!

## Linear Transformations
- A linear transformation A on a real vector space V is a map that preserves linear combinations.
	- It must map the origin to the same origin.
	- Consider A to be transforming the basis before the vector.
		- *A* is the operation, **A** is the matrix, and **A** always is multiplied after the basis.
- We don't change numbers in the geometry spreadsheet to make transformations, we just change the basis.
- All bases are stored by matrices represetning the interrelations betwen bases.
- An inner product space is defined as such:
	- symmetric
	- bilinear
	- positive-definite
- So a Euclidean vector space is where we can measure the length of a vector and measure the angles between vectors.
	- length/norm is the square root of the inner product with itself.
	- normalization is the vector divided by its norm (make the length 1).
	- the angle between vectors is cos(theta) = the inner product of the normalized vectors,
		- and theta is the arccos of the inner product of the normalized vectors.

### Rotations and Reflections
- are linear isometries (don't change the length and angles of vectors).
- 2D rotation matrix