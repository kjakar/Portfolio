

import java.util.Random;

import static org.lwjgl.glfw.GLFW.*;
import static org.lwjgl.opengl.GL11.*;
import static org.lwjgl.opengl.GL15.*;
import static org.lwjgl.opengl.GL20.*;
import static org.lwjgl.opengl.GL30.*;

public class Model3D {
	public static void main(String[] args) {
		GLWindow window = GLWindow.getInstance(600, 600);
		
		// turn on depth testing
		glEnable(GL_DEPTH_TEST);
		
		// set background color
		glClearColor(0.25f, 0.25f, 1.0f, 0.0f);
		
		// read model data for non-indexed rendering
		float[] verts = OBJReader.readVerticesFromOBJ("monkey.obj");
		System.out.println("non-index size (in bytes): " + verts.length * 4);
		
		// read model data for indexed rendering
		OBJVertexData vdata = OBJReader.readFromOBJ("monkey.obj");
		System.out.println("index size (in bytes): " +
			(vdata.vertices.length * 4 + vdata.indices.length * 4));
		
		// Setup vertex array object for storing vertex buffer object
		// binding points, which array attributes are enabled, etc.
		int vertexArrayObject = glGenVertexArrays();
		glBindVertexArray(vertexArrayObject);
		
		// Create a new vertex buffer object and check if it
		// was created without error.
		int positionVBO = glGenBuffers();
		if (positionVBO == -1) {
			System.err.println("ERROR HAPPENED, VBO NOT CREATED");
		}
		
		// Bind VBO to ARRAY_BUFFER target and copy our vertex
		// position data.
		glBindBuffer(GL_ARRAY_BUFFER, positionVBO);
		glBufferData(GL_ARRAY_BUFFER, vdata.vertices, GL_STATIC_DRAW);
		
		// point our position VBO to attribute array location 0
		glVertexAttribPointer(0, 3, GL_FLOAT, false, 0, 0);
		
		// enable vertex attribute array location 0
		glEnableVertexAttribArray(0);
		
		// setup color vertex buffer object
		int colorVBO = glGenBuffers();
		glBindBuffer(GL_ARRAY_BUFFER, colorVBO);
		
		// random color values
		Random r = new Random();
		float[] colorValues = new float[vdata.vertices.length];
		for (int i = 0; i < vdata.vertices.length; ++i)
			colorValues[i] = r.nextFloat();
		
		// bind and copy color data
		glBufferData(GL_ARRAY_BUFFER, colorValues, GL_STATIC_DRAW);
		glVertexAttribPointer(1, 3, GL_FLOAT, false, 0, 0);
		
		// enable location 1 (color data)
		glEnableVertexAttribArray(1);
		
		// setup index vbo and copy data
		int indexVBO = glGenBuffers();
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indexVBO);
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, vdata.indices, GL_STATIC_DRAW);
		
		// monkey's angle of rotation about the z-axis
		float angle = 0.0f;
		float otherAngle = 0.0f;
		float thatLastAngle = 0.0f;
		float size = 1.8f;
		float angularVelocity = 360.0f / 1000.0f; // 360 degrees in 1 second
		float monkeyX = 0.0f;
		float monkeyY = 0.0f;
		float monkeyZ = 0.0f;
		float transformSpeed = 5.0f / 1000.0f;

		System.out.println("Controls : Rotate with arrow keys and 'e'/'r' | move with WASD | Scale with z/x | quit with escape or q");


		long startTime = System.currentTimeMillis();
		
		// main loop
		while (!window.shouldClose()) {
			
			long stopTime = System.currentTimeMillis();
			long elapsedTime = stopTime - startTime;
			startTime = stopTime;
			
			// handle input
			if (window.isPressed(GLFW_KEY_ESCAPE) || window.isPressed(GLFW_KEY_Q)) {
				window.close();
			}
			
			if (window.isPressed(GLFW_KEY_LEFT)) {
				angle += angularVelocity * elapsedTime;
				if (angle >= 360.0f)
					angle -= 360.0f;
			}
			if (window.isPressed(GLFW_KEY_RIGHT)) {
				angle -= angularVelocity * elapsedTime;
				if (angle < 0.0f)
					angle += 360.0f;
			}

			if (window.isPressed(GLFW_KEY_UP)) {
				otherAngle -= angularVelocity * elapsedTime;
				if (otherAngle >= 360.0f)
					otherAngle -= 360.0f;
			}
			if (window.isPressed(GLFW_KEY_DOWN)) {
				otherAngle += angularVelocity * elapsedTime;
				if (otherAngle < 0.0f)
					otherAngle += 360.0f;
			}
			if (window.isPressed(GLFW_KEY_E)) {
				thatLastAngle += angularVelocity * elapsedTime;
				if (thatLastAngle >= 360.0f)
					thatLastAngle -= 360.0f;
			}
			if (window.isPressed(GLFW_KEY_R)) {
				thatLastAngle -= angularVelocity * elapsedTime;
				if (thatLastAngle < 0.0f)
					thatLastAngle += 360.0f;
			}
			if (window.isPressed(GLFW_KEY_A)) {
				monkeyX -= transformSpeed * elapsedTime;
				if (otherAngle >= 360.0f)
					otherAngle -= 360.0f;
			}
			if (window.isPressed(GLFW_KEY_D)) {
				monkeyX += transformSpeed * elapsedTime;
				if (otherAngle < 0.0f)
					otherAngle += 360.0f;
			}
			if (window.isPressed(GLFW_KEY_S)) {
				monkeyY -= transformSpeed * elapsedTime;
				if (otherAngle >= 360.0f)
					otherAngle -= 360.0f;
			}
			if (window.isPressed(GLFW_KEY_W)) {
				monkeyY += transformSpeed * elapsedTime;
				if (otherAngle < 0.0f)
					otherAngle += 360.0f;
			}
			if (window.isPressed(GLFW_KEY_Z)) {
				size -= transformSpeed * elapsedTime;
				if (otherAngle >= 360.0f)
					otherAngle -= 360.0f;
			}
			if (window.isPressed(GLFW_KEY_X)) {
				size += transformSpeed * elapsedTime;
				if (otherAngle < 0.0f)
					otherAngle += 360.0f;
			}


			// update objects
			
			// clear buffers
			glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
			
			// render
			
			// bind VAO to render the monkey
			glBindVertexArray(vertexArrayObject);
			
			// set the model matrix to rotate and then translate
			// the model
			ShaderProgram.getDefaultProgram().setModelMatrix(
					Matrix4.getScale(size,size,size).multiply(
						Matrix4.getRotation(otherAngle, angle, thatLastAngle).multiply(
							Matrix4.getTranslation(monkeyX, monkeyY, monkeyZ))));

			// draw monkey
			
			// use glDrawArrays for non-indexed rendering
			//glDrawArrays(GL_TRIANGLES, 0, verts.length / 3);
			
			// use glDrawElements for indexed rendering
			glDrawElements(GL_TRIANGLES, vdata.indices.length,
				GL_UNSIGNED_INT, 0);
			
			window.swapBuffers();
			window.pollEvents();
		}
	}
}
