package Jasons_stuff;


import org.newdawn.slick.Color;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;

/**
 * Created by Alex Jones on 9/28/2016.
 */
public class Square extends Shape
{

    int mSize;
    float mRed;
    float mGreen;
    float mBlue;
    int mX;
    int mY;

    public Square(int x, int y, int size)
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
        g.fillRect(mX,mY,mSize,mSize);
    }

}

/*

package Jasons_stuff;

import java.util.LinkedList;
import java.util.logging.*;
import org.newdawn.slick.*;
import org.lwjgl.*;


public class MainProgram extends BasicGame
{

    int mouseX = 0;
    int mouseY = 0;
    boolean isSquare = true;
    int mSize = 50;
    Stack stack = new Stack();
    Queue queue = new Queue();
    LinkedList<Shape> mData = new LinkedList<Shape>();
    String s1 = "hello1";
    String s2 = "hello2";
    String s3 = "hello3";
    String s4 = "hello4";
    String s5 = "hello5";



    public MainProgram(String gamename)
    {
        super(gamename);
    }

    @Override
    public void init(GameContainer gc) throws SlickException {}

    @Override
    public void update(GameContainer gc, int i) throws SlickException
    {
        Input input = gc.getInput();
        mouseX = input.getMouseX();
        mouseY = input.getMouseY();
        if(input.isKeyPressed(input.KEY_UP))    // this changes the shape
            isSquare = !isSquare;
        if(input.isKeyPressed(input.KEY_DOWN))  // ^^^^^^^^^^^^^^^^^^^^^^
            isSquare = !isSquare;
        if(input.isKeyPressed(input.KEY_RIGHT)) // this changes the size
            mSize++;
        if(input.isKeyPressed(input.KEY_LEFT))  // ^^^^^^^^^^^^^^^^^^^^^
            mSize--;

        // these keep the size reasonable
        if(mSize > 50) mSize = 50;
        if(mSize < 5) mSize = 5;

        //this places the shapes onto the screen
        if(input.isMousePressed(input.MOUSE_LEFT_BUTTON))
        {
            if(isSquare){Square temp = new Square(mouseX, mouseY, mSize); mData.add(temp); queue.add(true, mouseX, mouseY);}
            if(! isSquare){Circle temp = new Circle(mouseX, mouseY, mSize); mData.add(temp);queue.add(false, mouseX, mouseY);}
        }


    }

    @Override
    public void render(GameContainer gc, Graphics g) throws SlickException
    {
        //g.drawString("Howdy!", 100, 100);

        //this renders all the shapes in the linked list
        for(int i =0; i < mData.size(); i++) {mData.get(i).draw(gc, g);}

        // these handle the shape outline drawing.
        if(! isSquare)
        {
            g.setColor(new Color(255, 255, 255));
            g.drawOval(mouseX - (mSize / 2), mouseY - (mSize / 2), mSize, mSize);
        }
        if(isSquare)
        {
            g.setColor(new Color(255, 255, 255));
            g.drawRect(mouseX - (mSize / 2), mouseY - (mSize / 2), mSize, mSize);
        }

        queue.draw(gc, g);

    }

    public static void main(String[] args)
    {
        try
        {
            AppGameContainer appgc;
            appgc = new AppGameContainer(new MainProgram("Album Title Goes Here"));
            appgc.setDisplayMode(1240, 720, false);
            appgc.start();
        }
        catch
                (SlickException ex)
        {
            Logger.getLogger(MainProgram.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
 */