## Vector Graphics
- We *could* use a low-level geometry representation, with lines, triangles, etc...
	- It's easy to store and render.
	- But it's hard to make, edit, or design.
- We use a high-level representation instead, where we generate lines and triangles mathematically with a small number of control points.
## Parametric Curves
- We can describe a curve with a function that maps from 1D to 2D (or 3D).
	- A "position-valued function of one variable".
- We can make simple structures easily, such as straight lines or circles.
- We can also make the curve defined piecewise, with multiple functions.
- Remember that velocity and acceleration are the first and second derivatives of position, respectively.
	- Furthermore remember that the velocity divided by the magnitude of that same velocity is the *tangent*.
- A curve $f$ is thus called:
	- $C^0$ if $f$ is continuous.
	- $C^1$ if $f'$ is continuous.
	- $C^2$ if $f''$ is continuous.
	- ...and so on and so forth, where higher order curves are subsets of smaller order curves.
	- Furthermore note that these are not all guaranteed if one is true. Ex: a passenger in a car can feel smooth and continuous accelration, but the trajectory can still feature cusps and kinks.
![[image - continuity counterexample.png]]
- To ensure the smoothness of a curve, we require that $f'(t) \neq 0$, and a curve with a non-vanishing first derivative is called a *regular curve*, and uses $G$ instead of $C$.
## Spline Curves
- We now introduce "control points", which are the parameters for curve generation. The resulting curves are known as **splines**.
## Bezier Curve
## B-Spline
## Subdivision