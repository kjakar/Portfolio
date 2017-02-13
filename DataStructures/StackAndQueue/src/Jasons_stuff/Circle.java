package Jasons_stuff;


/**
 * Created by Alex Jones on 9/28/2016.
 */
import org.newdawn.slick.*;

public class Circle extends Shape
{

    int mSize;
    float mRed;
    float mGreen;
    float mBlue;
    int mX;
    int mY;

    public Circle(int x, int y, int size)
    {
        mSize = size;
        mX = (int)(x - Math.floor(size / 2));
        mY = (int)(y - Math.floor(size / 2));
        mRed = (float) (Math.random());
        mGreen = (float) (Math.random());
        mBlue = (float) (Math.random());

    }

    public void draw(GameContainer gc, Graphics g)
    {
        g.setColor(new Color( mRed, mGreen, mBlue));
        g.fillOval(mX,mY,mSize,mSize);
    }

}
