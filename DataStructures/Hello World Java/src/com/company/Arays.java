package com.company;

/**
 * Created by Alex Jones on 8/22/2016.
 */
public class Arays
{

    public static void printArray(int[] x)
    {
        System.out.println("Array\n======");

        for (int i = 0; i < x.length; i++)
            {
                System.out.println(i + "\t" + x[i]);
            }

    }

    public static void main(String[] args)
    {

        int[] intArray = new int[4];
        intArray[1] = 99;
        intArray[2] = 33;

        System.out.print(intArray);
        printArray(intArray);

        int[] theif = intArray;
        theif[0] = 1000;
        printArray(theif);
        printArray(intArray);

        theif = new int[8];
        System.arraycopy(intArray, 0, theif, 4, intArray.length);
        printArray(theif);

    }

}
