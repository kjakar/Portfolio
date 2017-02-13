package ETEC2101;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by Alex on 11/11/2016.
 */
public class Graph
{
    ArrayList<Node> Nodes = new ArrayList();
    ArrayList<Edge> Edges = new ArrayList();


    public void loadFile(String fileName) throws FileNotFoundException
    {

        File file = new File(fileName);

        Scanner scnr = new Scanner(file);

        while (scnr.hasNextLine()) {
            //this does the file reading
            String line = scnr.nextLine();
            String[] parts = line.split(" ");

            //n has a 5 item list
            if(parts[0].equals("n")) {Node temp = new Node(parts); /*Nodes.add(temp);*/}

            //e has a 4 item list
            if(parts[0].equals("e")) {Edge temp = new Edge(parts); Edges.add(temp);}

            //L has a 5 item list
            if(parts[0].equals("L")) {}

            /* this removes the $ sign so that I can turn the amount into an int
            parts[2] = parts[2].substring(1, parts[2].length());
            //this creates a new transaction to add to the list mTransactions

            //this is the for loop that adds the transaction to the first empty slot
            for (int i = 0; i < mTransactions.length; i++) {
                if (mTransactions[i] == null) {
                    mTransactions[i] = temp;
                    mSize++;
                    break;
                }

            }

            //System.out.println(line + parts[0] + parts[1] + parts[2] + parts[3]);
            */
        }
    }

    public void main(String[] args) throws FileNotFoundException
    {
        loadFile("map02.txt");
        System.out.println(Nodes.size() + "  " + Edges.size());
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

}
