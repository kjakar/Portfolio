// Filename: OBJReader.java
// By: Andrew Holbrook
// Date: 9/26/2016

import java.io.*;

import java.util.ArrayList;
import java.nio.FloatBuffer;

public class OBJReader {
	
	// readFromOBJ will read all vertex and index data from an obj file
	public static OBJVertexData readFromOBJ(String filename) {
		ArrayList<Float> vertexList = new ArrayList<Float>();
		ArrayList<Integer> indexList = new ArrayList<Integer>();
		
		try {
			BufferedReader reader = new BufferedReader(
				new FileReader(filename));
			
			String line = reader.readLine();
			while (line != null) {
				String[] tokens = line.split(" ");
				if (tokens[0].equals("v")) {
					vertexList.add(Float.valueOf(tokens[1]));
					vertexList.add(Float.valueOf(tokens[2]));
					vertexList.add(Float.valueOf(tokens[3]));
				} else if (tokens[0].equals("f")) {
					if (tokens.length != 4) {
						reader.close();
						System.err.println("Error reading model : " +
							"only triangulated meshes are supported");
						return null;
					}
					
					indexList.add(Integer.valueOf(tokens[1]) - 1);
					indexList.add(Integer.valueOf(tokens[2]) - 1);
					indexList.add(Integer.valueOf(tokens[3]) - 1);
				}
				
				line = reader.readLine();
			}
			
			reader.close();
			
		} catch (Exception e) {
			System.err.println(e);
			return null;
		}
		
		OBJVertexData vertexData = new OBJVertexData();
		vertexData.vertices = new float[vertexList.size()];
		vertexData.indices = new int[indexList.size()];
		
		// copy data into the OBJVertexData object
		for (int i = 0; i < vertexList.size(); ++i)
			vertexData.vertices[i] = vertexList.get(i);
		for (int i = 0; i < indexList.size(); ++i)
			vertexData.indices[i] = indexList.get(i);
		
		return vertexData;
	}
	
	// readVerticesFromOBJ will read all vertex data from an obj file,
	// flattening the data into an array
	public static float[] readVerticesFromOBJ(String filename) {
		ArrayList<Float> vertexList = new ArrayList<Float>();
		ArrayList<Integer> indexList = new ArrayList<Integer>();
		
		try {
			BufferedReader reader = new BufferedReader(
				new FileReader(filename));
			
			String line = reader.readLine();
			while (line != null) {
				String[] tokens = line.split(" ");
				if (tokens[0].equals("v")) {
					vertexList.add(Float.valueOf(tokens[1]));
					vertexList.add(Float.valueOf(tokens[2]));
					vertexList.add(Float.valueOf(tokens[3]));
				} else if (tokens[0].equals("f")) {
					if (tokens.length != 4) {
						reader.close();
						System.err.println("Error reading model : " +
							"only triangulated meshes are supported");
						return null;
					}
					
					indexList.add(Integer.valueOf(tokens[1]) - 1);
					indexList.add(Integer.valueOf(tokens[2]) - 1);
					indexList.add(Integer.valueOf(tokens[3]) - 1);
				}
				
				line = reader.readLine();
			}
			
			reader.close();
			
		} catch (Exception e) {
			System.err.println(e);
			return null;
		}
		
		// flatten data for non-indexed rendering
		int i = 0;
		float[] vertices = new float[indexList.size() * 3];
		for (Integer index : indexList) {
			vertices[i] = vertexList.get(index * 3);
			vertices[i + 1] = vertexList.get(index * 3 + 1);
			vertices[i + 2] = vertexList.get(index * 3 + 2);
			i += 3;
		}
		
		return vertices;
	}
}
