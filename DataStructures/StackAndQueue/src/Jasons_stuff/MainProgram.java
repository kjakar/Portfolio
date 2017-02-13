package Jasons_stuff;

        import java.util.logging.*;
        import org.newdawn.slick.*;
public class MainProgram extends BasicGame {
    public MainProgram(String gamename) {
        super(gamename);
    }

    @Override
    public void init(GameContainer gc) throws SlickException {
    }

    @Override
    public void update(GameContainer gc, int i) throws SlickException {
    }

    @Override
    public void render(GameContainer gc, Graphics g) throws SlickException {
        g.drawString("Howdy!", 10, 10);
    }

    public static void
    main(String[] args) {
        try {
            AppGameContainer appgc;
            appgc = new AppGameContainer(new MainProgram("Simple Slick Game"));
            appgc.setDisplayMode(640, 480, false);
            appgc.start();
        } catch (SlickException ex) {
            Logger.getLogger(MainProgram.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}