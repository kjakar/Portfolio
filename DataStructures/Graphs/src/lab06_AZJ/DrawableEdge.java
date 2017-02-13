package lab06_AZJ;

import org.newdawn.slick.Color;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;

/**
 * Created by Alex on 11/11/2016.
 */
public class DrawableEdge{

    float mX1;
    float mY1;
    float mX2;
    float mY2;
    float mSize;

    //example of edge text e 12 11 78.0


    public DrawableEdge(float x1, float y1,float x2, float y2, float size)
    {
        mX1 = x1;
        mY1 = y1;
        mX2 = x2;
        mY2 = y2;

        mSize = size;
    }

    public void draw(GameContainer gc, Graphics g)
    {
        g.setColor(new Color(1f,1f,1f));
        g.drawLine(mX1,mY1,mX2,mY2);
    }
}
