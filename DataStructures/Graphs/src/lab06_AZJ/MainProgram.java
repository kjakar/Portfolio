package lab06_AZJ;

import java.io.FileNotFoundException;
import java.util.logging.*;
import org.newdawn.slick.*;



public class MainProgram extends BasicGame {

    DrawableGraph G = new DrawableGraph();


    public MainProgram(String gamename) {
        super(gamename);
    }

    @Override
    public void init(GameContainer gc) throws SlickException {
        try {
            G.loadFile("map04.txt");
        }
        catch(FileNotFoundException e){System.out.println("File was not found");}
        G.scale(1800, 950);
        System.out.println(G.Nodes.size());
    }

    @Override
    public void update(GameContainer gc, int i) throws SlickException {
    }

    @Override
    public void render(GameContainer gc, Graphics g) throws SlickException {
        //g.drawString("Howdy!", 10, 10);
        G.draw(gc, g);
    }



    public static void main(String[] args) throws FileNotFoundException
    {
        try {
            AppGameContainer appgc;
            appgc = new AppGameContainer(new MainProgram("Simple Slick Game"));
            appgc.setDisplayMode(1800, 950, false);
            appgc.start();
        } catch (SlickException ex) {
            Logger.getLogger(MainProgram.class.getName()).log(Level.SEVERE, null, ex);
        }

        // game code =======================================================================================================



    }
}