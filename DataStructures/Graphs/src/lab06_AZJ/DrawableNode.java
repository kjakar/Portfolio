package lab06_AZJ; /**
 * Created by Alex on 11/11/2016.
 */


import org.newdawn.slick.*;

public class DrawableNode
{

    String mName;
    float mX;
    float mY;
    float mSize;

    // example of node text n Room8_0 666 38 10

    public DrawableNode(String[] data)
    {
        mName = data[1];
        mX = new Float(data[2]).floatValue();
        mY = new Float(data[3]).floatValue();
        mSize = new Float(data[4]).floatValue();

    }

    public void draw(GameContainer gc, Graphics g)
    {
        g.setColor(new Color(1f,1f,1f));
        g.fillOval(mX - (mSize / 2),mY - (mSize / 2),mSize,mSize);
        g.setColor(new Color(255,0,0));
        g.drawString(mName,mX,mY);
    }

}
