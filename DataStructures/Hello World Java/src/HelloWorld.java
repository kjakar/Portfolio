/**
 * Created by Alex Jones on 8/22/2016.
 */

import java.util.Scanner;

public class HelloWorld {

    public static void main(String[] args) {
        System.out.println("hello Alex!");

        Scanner s = new Scanner(System.in);  // this is an instance of the scanner class

        System.out.print("Tell me your name: "); //print vs print line | print, does not move the curser to the next line

        String name; // this is a var

        name = s.nextLine();

        int age;

        System.out.print("tell me your age? : ");

        age = s.nextInt();

        System.out.println("Hello " + name + " you're really " + age + " years old???");
    }

}
