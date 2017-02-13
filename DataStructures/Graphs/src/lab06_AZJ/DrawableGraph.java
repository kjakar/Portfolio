package lab06_AZJ;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

import org.lwjgl.Sys;
import org.newdawn.slick.*;

public class DrawableGraph
{
    ArrayList<DrawableNode> Nodes = new ArrayList();
    ArrayList<DrawableEdge> Edges = new ArrayList();

    public void draw(GameContainer gc, Graphics g)
    {
        for(int i = 0; i < Nodes.size(); i++)
        {
            if(Nodes.get(i) instanceof DrawableNode)
                Nodes.get(i).draw(gc, g);
        }

        for(int i = 0; i < Edges.size(); i++)
        {
            if(Edges.get(i) instanceof DrawableEdge)
                Edges.get(i).draw(gc, g);
        }


    }


    public void loadFile(String fileName) throws FileNotFoundException
    {

        File file = new File(fileName);

        Scanner scnr = new Scanner(file);

        while (scnr.hasNextLine()) {
            //this does the file reading
            String line = scnr.nextLine();
            String[] parts = line.split(" ");

            //n has a 5 item list
            if(parts[0].equals("n")) {DrawableNode temp = new DrawableNode(parts); Nodes.add(temp);}

            //e has a 4 item list
            if(parts[0].equals("e"))
            {
                int node1 = Integer.parseInt(parts[1]);
                int node2 = Integer.parseInt(parts[2]);
                float x1 = Nodes.get(node1).mX;
                float y1 = Nodes.get(node1).mY;
                float x2 = Nodes.get(node2).mX;
                float y2 = Nodes.get(node2).mY;
                float size = new Float(parts[3]).floatValue();

                DrawableEdge temp = new DrawableEdge(x1, y1, x2, y2, size); Edges.add(temp);}


        }
    }


    public void addNode(String name, float x, float y, float size)
    {
        String[] temp = new String[5];
        temp[0] = "n";
        temp[1] = name;
        temp[2] = Float.toString(x);
        temp[3] = Float.toString(y);
        temp[4] = Float.toString(size);

    }

    public void addEdge(float data1, float data2, float data3)
    {
        String[] temp = new String[4];
        temp[0] = "e";
        temp[1] = Float.toString(data1);
        temp[2] = Float.toString(data2);
        temp[3] = Float.toString(data3);
    }


    public void scale(int x, int y)
    {
        float bigX = 0;
        float bigY = 0;
        float scaleFactorX;
        float scaleFactorY;


        // find  the biggest x/y
        for(int i = 0; i < Nodes.size(); i++)
        {
            if(Nodes.get(i).mX > bigX)
                bigX = Nodes.get(i).mX;
            if(Nodes.get(i).mY > bigY)
                bigY = Nodes.get(i).mY;
        }

        scaleFactorX = (x - 100) / bigX;
        scaleFactorY = (y - 100) / bigY;

        // adjust the scale
        for(int i = 0; i < Nodes.size(); i++)
        {
            Nodes.get(i).mX = Nodes.get(i).mX * scaleFactorX;
            Nodes.get(i).mY = Nodes.get(i).mY * scaleFactorY;
        }

        for(int i = 0; i < Edges.size(); i++)
        {
            Edges.get(i).mX1 = Edges.get(i).mX1 * scaleFactorX;
            Edges.get(i).mX2 = Edges.get(i).mX2 * scaleFactorX;
            Edges.get(i).mY1 = Edges.get(i).mY1 * scaleFactorY;
            Edges.get(i).mY2 = Edges.get(i).mY2 * scaleFactorY;
        }

    }
}
