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
	- The word comes from a flexible piece of wood sailors used to draw smooth shapes.
- In computations, the spline curves are almost always parameterized by *polynomials*.
	- Linear: $f(t) = p_0 + td$
	- Quadratic: $f(t) = at^2 + bt + c$
		- We can use 3x1 matrices to represent homogeneous coordinates for the coefficiencts of quadratic polynomial curves.
	- Cubic: $f(t) = at^3 + bt^2 + ct + d$
		- An approximate solutions to elastic curves.
- With higher degree polynomials, we have more variety of curves, but the behavior of higher degree polynomials are hard to control.
	- Therefore for spline interpolation, we use **piecewise** lower order polynomials.
- There are two techniques...
	- The Bézier curve, which passes through a subset of control points at the junctions.
	- The Basis spline (B-spline), where the curve does not pass through the control points and the transition between polynomial curves is smoother.
## Bézier Curve
- Bézier was the one who popularized de Casteljau's technique when he applied it to the bodywork of Renault cars.
- Provides intuitive control where the endpoints are passed through while the intermediate points are approximated.
- We commonly use a cubic Bézier curve with 4 control points.
![[image - spline concept.png]]
### de Casteljau's Algorithm
- Essentially, it is recursive linear interpolation.
	- We will refer to linear interpolation between to points by the **lerp** function (refered to as `mix` in OpenGL.
```c++
point lerp(point p, point q, float t) {
	return (1-t)p + tq;
}
```
- Going over an example, we are given 4 points, $p_0$ to $p_3$ and a value $t$ between 0 and 1.
	- Get 3 points with lerp: $q_0(t) = lerp(p_0, p_1, t)$, ... , $q_2(t) = lerp(p_2, p_3, t)$
	- Then 2 points with the $q$ values from the previous step.
	- Finally, we get our interpolated point by lerping the 2 points from the last step.
#### In Code
- We simply use a copy of the array input to save memory.

### Bernstein Polynomials
- It's essentially the explicit form of the lerping.
	- Long story short, with 4 points and $s = 1-t$ and $t$, the equation is $s^3p_0 + 3s^2tp_1 + 3st^2p_2+t^3p_3$.
	- Notice something? Its format is the same as binomials.
		- $(1-t)^kt^{n-k}p_k$ times $n$ choose $k$, sum from $k=0$ to $n$ = number of points - 1.
- Notice futher that the equation is a linear combination of $t^3, t^2, t, 1$, so we can use matrix notation.
	- We can apply this Bernstein basis on a set of points.

### Cubic Blossom
- To "blossom" means to reverse-engineer a polynomial curve back to its control points.
- We want a cubic blossom, a function of 3 variables, with the following properties:
	- Symmetric
	- Tri-Affine
	- Diagonal Consistency
- In general... $$ F(t_1, t_2, t_3) = at_1t_2t_3 + b *(t_1t_1+t_2t_3 + t_1t_3)/3 + c*(t_1 + t_2 + t_3) /3 + d$$
## B-Spline
- 
## Subdivision