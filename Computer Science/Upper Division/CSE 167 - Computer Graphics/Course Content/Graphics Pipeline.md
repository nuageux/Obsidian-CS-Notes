#Graphics #OpenGL
# The Graphics Pipeline
## The Main Algorithm
- The inputs include:
	- Geometries (typically a triangle mesh) in the **scene** (the 3D we are trying to recreate)
		- Triangles consist of vertices and connectivities.
			- Vertices are recorded by coordinates in the **vertex buffer**.
			- Connectivities record 3 pointers in the **index buffer**.
				- A buffer is another word for an instance of memory allocation.
			- The two buffers describe a "geometry spreadsheet" (vertex array object).
	- Color, material, etc. of each geometry
	- Lighting
	- Camera angle (POV)
- The output is the
	- Color per Pixel in the **screen** (literally, the 2D computer screen)

- **Step 1** is to determine which triangle corresponds to which pixel
- **Step 2** is to actually color each pixel according to the other inputs.

### Scene-Screen Incidence Relation
Is used to determine which *triangles* of the *scene* are **incident** to which *pixels* of the *screen*.
- A **fragment** is a triangle-pixel pair so that the pixel is **incident to** (covered by) the triangle.
	- *Each fragment knows which triangle it came from!*
	- *Each fragment knows which pixel it lands on!*

When we construct a mapping between scene and screen, we can put the scene and its geometries (triangles) on the y-axis and the screen and its pixels on the x-axis.
- A mark on the coordinate plane means that a triangle is incident to a pixel.
- **Rasterization**
	- Going triangle by triangle, checking pixels in each triangle
	- Easy to speed up
	- Doesn't look that realistic, though
- **Ray Tracing/Casting**
	- Going pixel by pixel, checking what triangles cover that pixel
	- Is preferred in graphics because recursive ray tracing leads to photorealism
	- ...but it's hard to speed up, and the hardware has only been released recently

A **shader** is a program or a piece of code that runs on the GPU.

### The Raster Graphics Pipeline

^40b7df

- When calling the "draw elements" command, the following procedure takes place:
	- **Pre-rasterization**, where the 3D geometries are placed in a coordinate system.
		- The **vertex shader** we write is executed here, written in **GLSL**.
			- Manipulates the geometry spreadsheet as mentioned before, determining what is seen in the "viewing box".
	- **Rasterization**, which assembles the triangles, discards the non-consequential ones, and rasterizes the remaining elements into fragments.
		- (Usually) not programmable.
	- **Post-rasterization**, where the fragments are painted with colors which are then exported for storage and display.
		- The **fragment shader** we write is executed here, also written in GLSL.
	- Then, the depth resolution step (choosing which fragment color to show on the screen by choosing whatever fragment is closest to the screen) is also not programmable.
	- Finally, everything is sent to the frame buffer for display.