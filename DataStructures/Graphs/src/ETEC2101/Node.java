package ETEC2101;

import java.util.ArrayList;

/**
 * Created by Alex on 11/11/2016.
 */
public class Node
{

    String mName;
    float mX;
    float mY;
    float mSize;

    // example of node text n Room8_0 666 38 10

    Node(){}
    public Node(String[] data)
    {
        mName = data[1];
        mX = new Float(data[2]).floatValue();
        mY = new Float(data[3]).floatValue();
        mSize = new Float(data[4]).floatValue();



    }



}
