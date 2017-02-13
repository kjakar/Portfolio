package Jasons_stuff;


import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Color;
import org.newdawn.slick.*;
import org.lwjgl.*;

import static org.lwjgl.Sys.getTime;

/**
 * Created by Alex Jones on 9/28/2016.
 */
public class Queue
{
    // this handles delta time for the fading out
    long lastFrame = 0;
    public int getDelta()
    {
        long time = getTime();
        int delta = (int) (time - lastFrame);
        lastFrame = time;

        return delta;
    }

    // class vars ======================================================================================================
    String[] mStrings = new String[5];
    float[] mTrans = new float[5];
    int mSize = 0;


    public void draw(GameContainer gc, Graphics g)
    {
        int posX = 920;
        int posY = 700;
        for (int i = 4; i >= 0; i--)
        {
            mTrans[i] -= getTime();
            if(mStrings[i] != null)
            {

                Color temp = new Color(1,1,1, mTrans[i]);
                g.setColor(temp);
                g.drawString(mStrings[i],posX, posY); posY -= 30;
            }

        }
        posY = 500;
    }

    public void add(boolean square, int x, int y)
    {
        String temp = "";
        if(square) {temp = "User placed a square at " + x + "," + y;}
        if(! square) {temp = "User placed a circle at " + x + "," + y;}

        if(mSize <= 4)
        {
            mStrings[mSize] = temp;
            mTrans[mSize] = 1.0f;
            mSize++;
        }
        else if(mSize > 4)
        {
            mStrings[0] = mStrings[1];
            mStrings[1] = mStrings[2];
            mStrings[2] = mStrings[3];
            mStrings[3] = mStrings[4];
            mStrings[4] = temp;

            mTrans[0] = mTrans[1];
            mTrans[1] = mTrans[2];
            mTrans[2] = mTrans[3];
            mTrans[3] = mTrans[4];
            mTrans[4] = 1.0f;

        }

    }


}
