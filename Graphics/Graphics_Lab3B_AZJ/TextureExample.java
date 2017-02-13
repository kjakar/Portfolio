// Filename: TextureExample.java
// By: Andrew Holbrook
// Date: 11/14/2016

import java.util.Random;
import javax.imageio.ImageIO;
import java.awt.image.*;
import java.io.*;

import static org.lwjgl.glfw.GLFW.*;
import static org.lwjgl.opengl.GL11.*;
import static org.lwjgl.opengl.GL12.*;
import static org.lwjgl.opengl.GL13.*;
import static org.lwjgl.opengl.GL15.*;
import static org.lwjgl.opengl.GL20.*;
import static org.lwjgl.opengl.GL30.*;

public class TextureExample {


	public static float distance(Vector4 one, Vector4 two)
	{
		float data = 0.0f;

		float dx = two.data[0] - one.data[0]; //x2 - x1
		float dy = two.data[2] - one.data[2]; //y2 - y1
		data = (float)Math.sqrt(dx*dx + dy*dy);

		return data;
	}





	public static void main(String[] args) {
		
		BufferedImage chestImg = null;
		try {
			File f = new File("treasure_chest/treasure_chest.png");
			chestImg = ImageIO.read(f);
			
		} catch (Exception e) {
			System.err.println("NO");
		}
		
		GLWindow window = GLWindow.getInstance(800, 600);
		
		glActiveTexture(GL_TEXTURE0);
		
		int texobj = glGenTextures();
		glBindTexture(GL_TEXTURE_2D, texobj);
		
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, chestImg.getWidth(),
			chestImg.getHeight(), 0, GL_BGRA, GL_UNSIGNED_BYTE,
			chestImg.getRGB(0, 0, chestImg.getWidth(), chestImg.getHeight(),
				null, 0, chestImg.getWidth()));
		
		glGenerateMipmap(GL_TEXTURE_2D);
		
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
			GL_LINEAR);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
			GL_LINEAR_MIPMAP_LINEAR);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S,
			GL_REPEAT);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,
			GL_REPEAT);
		
		// turn on depth testing
		glEnable(GL_DEPTH_TEST);
		
		// turn on backface culling
		glEnable(GL_CULL_FACE);
		
		// set background color
		glClearColor(0f, 0f, 0f, 0f);
		
		ShaderProgram.getDefaultProgram().setProjectionMatrix(
			Matrix4.getPerspective(60, window.getAspect(), 1, 10));
		
		long startTime = System.currentTimeMillis();
		
		int vao = glGenVertexArrays();
		glBindVertexArray(vao);
		
		// load vertex data for non-indexed rendering
		OBJVertexData data = OBJReader.readFromOBJ(
			"treasure_chest/treasure_chest.obj", true);
		
		int positionVBO = glGenBuffers();
		glBindBuffer(GL_ARRAY_BUFFER, positionVBO);
		
		glBufferData(GL_ARRAY_BUFFER, data.vertices, GL_STATIC_DRAW);
		glVertexAttribPointer(0, 3, GL_FLOAT, false, 0, 0);
		glEnableVertexAttribArray(0);
		
		int uvVBO = glGenBuffers();
		glBindBuffer(GL_ARRAY_BUFFER, uvVBO);
		
		glBufferData(GL_ARRAY_BUFFER, data.textureCoordinates, GL_STATIC_DRAW);
		glVertexAttribPointer(1, 2, GL_FLOAT, false, 0, 0);
		glEnableVertexAttribArray(1);
		
		float angle = 0.0f;
		
		Camera camera = new Camera();
		float dpos = 1.0f / 500.0f;
		float camYRot = 270.0f;
		
		MegaMan megaMan = new MegaMan();
		megaMan.modelMatrix.setBasis((Matrix4.getScale(10.0f, 10.0f, 0.0f).multiply(Matrix4.getRotation(-90.0f, 0, 0.0f))).multiply(Matrix4.getTranslation(new Vector4(0, 0, 0.0f, 1.0f))));
		//megaMan.modelMatrix.setPosition(new Vector4(0, 0, -5.5f, 1.0f));
		//megaMan.modelMatrix.setBasis(Matrix4.getRotation(-90.0f, 0, 0.0f));
		//megaMan.setCamera(camera);
		
		Arm arm = new Arm();
		Enemy bot01 = new Enemy();
		Enemy bot02 = new Enemy();

		
		ShaderProgram colorOnlyShader = new ShaderProgram();
		colorOnlyShader.setVertexShaderSource("colorshader.vert");
		colorOnlyShader.setFragmentShaderSource("colorshader.frag");
		if (!colorOnlyShader.compileAndLink()) {
			System.exit(0);
		}

		arm.program = colorOnlyShader;
		bot01.program = colorOnlyShader;
		bot02.program = colorOnlyShader;

		//setting objects starting points =======================================================
		Vector4 chestPos = new Vector4(3, 0, -6, 1);
		camera.setPosition(new Vector4(0, 3, 0, 1));
		bot01.position = new Vector4(-5, 0, 5, 1);
		bot02.position = new Vector4(-5, 0, 0, 1);


		boolean moveChestLeft = true;
		
		//camera.setLookAt(chestPos);
		//==============================================================================================================
		// main loop
		//==============================================================================================================
		while (!window.shouldClose()){


			arm.orientation = new Vector4(0.0f, camYRot + 90, 0.0f, 0.0f);
			arm.position = new Vector4(camera.getPosition().data[0], 0.0f, camera.getPosition().data[2], 1);

			//System.out.println("bot1 " + bot01.dead  + " bot2 " + bot02.dead);
			if (distance(chestPos, camera.getPosition()) < 1.9f && bot01.dead && bot02.dead) {
				System.exit(0);
			}


			if(distance(bot01.position, camera.getPosition()) < 5 && arm.punching)
				bot01.dead = true;
			if(distance(bot02.position, camera.getPosition()) < 5 && arm.punching)
				bot02.dead = true;


			long stopTime = System.currentTimeMillis();
			long elapsedTime = stopTime - startTime;
			startTime = stopTime;
			
			//angle += (360.0f / 5000.0f) * elapsedTime;
			while (angle >= 360) angle -= 360;
			
			// handle input
			if (window.isPressed(GLFW_KEY_ESCAPE)) {
				window.close();
			}
			
			if (window.isPressed(GLFW_KEY_A)) {
				Vector4 camPos = camera.getPosition();
				Vector4 camDir = camera.getLeft();
				camDir = camDir.multiply(dpos * elapsedTime);
				camera.setPosition(camPos.add(camDir));
			}
			
			if (window.isPressed(GLFW_KEY_D)) {
				Vector4 camPos = camera.getPosition();
				Vector4 camDir = camera.getRight();
				camDir = camDir.multiply(dpos * elapsedTime);
				camera.setPosition(camPos.add(camDir));
			}
			
			if (window.isPressed(GLFW_KEY_W)) {
				Vector4 camPos = camera.getPosition();
				Vector4 camDir = camera.getForward();
				camDir = camDir.multiply(dpos * elapsedTime);
				camera.setPosition(camPos.add(camDir));
			}
			
			if (window.isPressed(GLFW_KEY_S)) {
				Vector4 camPos = camera.getPosition();
				Vector4 camDir = camera.getBackward();
				camDir = camDir.multiply(dpos * elapsedTime);
				camera.setPosition(camPos.add(camDir));
			}
			
			if (window.isPressed(GLFW_KEY_UP)) {
				Vector4 camPos = camera.getPosition();
				Vector4 camDir = camera.getUp();
				camDir = camDir.multiply(dpos * elapsedTime);
				camera.setPosition(camPos.add(camDir));
			}
			
			if (window.isPressed(GLFW_KEY_LEFT)) {
				camYRot += (360.0f / 2000.0f) * elapsedTime;
				while (camYRot >= 360) camYRot -= 360;
				
				camera.setBasis(Matrix4.getRotation(0, camYRot, 0));
			}
			
			if (window.isPressed(GLFW_KEY_RIGHT)) {
				camYRot -= (360.0f / 2000.0f) * elapsedTime;
				while (camYRot < 0) camYRot += 360;
				
				camera.setBasis(Matrix4.getRotation(0, camYRot, 0));
			}
			
			if (window.isPressed(GLFW_KEY_SPACE)) {
				arm.setPunch(true);
			} else {
				arm.setPunch(false);
			}
			
			// update objects
			
			// update coin to face camera (billboarded image)
			//megaMan.update();
			arm.update(elapsedTime);
			
			// clear buffers
			glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
			
			// render
			
			arm.program.use();
			arm.program.setViewMatrix(camera.getViewMatrix());
			arm.program.setProjectionMatrix(
				Matrix4.getPerspective(60, window.getAspect(), 1, 10));
			arm.render();
			if(bot01.dead == false)
				bot01.render();
			if(bot02.dead == false)
				bot02.render();
			
			ShaderProgram.useDefaultProgram();
			
			glBindVertexArray(vao);
			glBindTexture(GL_TEXTURE_2D, texobj);
			
			ShaderProgram.getDefaultProgram().setViewMatrix(
				camera.getViewMatrix());
			
			ShaderProgram.getDefaultProgram().setModelMatrix(
				Matrix4.getRotation(0, angle, 0).multiply(
					Matrix4.getTranslation(chestPos)));
			
			glDrawArrays(GL_TRIANGLES, 0, data.vertices.length / 3);
			
			megaMan.render();
			
			// swap buffers and poll for new events
			window.swapBuffers();
			window.pollEvents();
		}
	}
}
