package ETEC2101;

/**
 * Created by Alex on 11/11/2016.
 */
public class Edge
{

    float data1;
    float data2;
    float data3;

    //example of edge text e 12 11 78.0

    Edge(){}


    public Edge(String[] data)
    {
        data1 = new Float(data[1]).floatValue();
        data2 = new Float(data[2]).floatValue();
        data3 = new Float(data[3]).floatValue();
    }

}
