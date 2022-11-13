#Graphics #OpenGL
# Modern OpenGL
Which allows us to program the GPU.
- OpenGL is a specification of what functions should exist, an API.
	- The actual implementations are up to the graphics card manufacturers.
- Enables a [[Graphics Pipeline#^40b7df||rasterization]] pipeline.
- Usually not open-source.
- Binareis come with the graphics card driver.

## OpenGL Utility Toolkit (GLUT)
- Has a list of functions that control the window and monitor mouse & keyboard events.

OpenGL is a state machine. It simulates a graphics "factory".
- It is described as a state machine because it always uses the same function (draw elements) for producing any image.
	- So the only thing that affects final output are the buffers and shaders selected.
	- A lot of the functions in the C code is just for switching states.
- The factory takes as input a spreadsheet of numbers that describe the geometries.
- The output is an array of pixel colors to be shown on the display.
- The inner workings of the factory is called the **rendering pipeline**.

The `GL_TRIANGLES` is the main mode in graphics production.

**Single Instruction, Multiple Data (SIMD)** indicates that despite having the same instruction, different workers (parts) of the GPU have different inputs, leading to different outputs.
- **Uniform variables** are used when the same data is used in many places.
- Single Instruction, Single Data is the realm of the CPU.

### Objects
- There are four main OpenGL objects we interact with:
	- Buffer object
		- A reminder that a **buffer** is an allocated part in the memory for storing data for later access.
	- **Vertex array** object, as a set of  [[The Relational Data Model#^40a3c5||tables]]
		- One table where rows represent vertices and columns represent attributes
			- `GL_ARRAY_BUFFER`
		- Another table to describe connectivity among the vertices to charaacterize the triangle mesh.
			- `GL_ELEMENT_ARRAY_BUFFER`
		- Called a "**geometry spreadsheet**".
			- To simplify further, it really is just a set of pointers that redirect the reader to the correct locations of the correct buffer objects!
	- Shader object
	- Program object
		- A "binder" that collects all shader objects.
		- It is the final target of the linking of the shader programs we write.

- The last buffer we interact with is the frame buffer, where the output is stored for display.
	- There is a front buffer and a back buffer, which swap to change the image on the screen. It is called "double buffering" and causes a flashing effect.
- We also use a depth buffer to keep track of the "depth" of the current fragment in the current geometry.

## Projecting with Rasterization!
- There is a **Viewing Box** in the "normalized device coordinate system" in the 3D window
	- $V_{3D} := [-1, 1] \times [-1, 1] \times [-1, 1] \in R^3$
- The corresponding **Viewport** in the "normalized screen coordinate" is the planar square region
	- $V_{2D} := [-1, 1] \times [-1, 1] \in R^2$
- So when we map 3 dimensions to 2, we use the $z$ coordinate as a *depth* measure to determine what gets shown.
- Note that rasterization does not give us perspective foreshortening!

# Code Structure
- `glDrawElements(...);`
	- Takes the geometric data and sends it through the [[Graphics Pipeline]] which produces pixel colors to store in a frame buffer.
- We need some global variables because we are using a state machine.
	- The vertex array object, buffers, program object, and uniform variable locations.
	- Declare these variables as `static`.
- In our initialization step, 
	- We build our vertex array object
		- write values into buffer objects
		- configure the buffer objects as vertex attributes
	- and write and compile shader programs
		- declare in, out, uniform variables
		- write the GLSL program
- To display, we select a VAO and a shader program, set the uniform variables, and run `glDrawElements`.
- `GLuint` is the same as an unsigned integer in C++.
