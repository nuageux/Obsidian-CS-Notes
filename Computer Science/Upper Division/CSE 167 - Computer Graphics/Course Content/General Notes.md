ivan sutherland father of computer graphics

learn:
- modern opengl
- foundation of 3d computer graphics
	- how to drwa pictures algorithmically?
		- rasterizaiton vs ray tracing
		- graphics pipeline
		- hardware gpu
- foundation of vector graphics
- perception of color
- physics-based animation
- optics
- geometry processing

# algorithm for drawing pictures
- input
	- geometries (triangle mesh)
	- color, material
	- light
	- camera (angles, pov)
- output
	- color per pixel in the screen
- algorithm
	- 1: determine which triangle corresponds to which pixel (main algorithm)
		- 3d <- screen -< center of projection (eye)
		- viewing frustum: there is always a transformation that normalizes the frustum into a standard box
		- scene screen incidence relation
			- determining which triangles is incident to pixels
			- ...like a function? but each triangle maps to multiple pixels, so not exactly a function
			- fragment is a triangle pixel pair so that the pixel is incident to (covered by) the triangle
			- each fragment knows which triangle it came from
	- 2: color each pixl in according to inputs

rasterization vs ray tracing

fragments vs buffers vs shaders

how to describe a shape

what is gpu