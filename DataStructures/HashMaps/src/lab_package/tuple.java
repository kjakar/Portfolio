package lab_package;

/**
 * Created by Alex on 10/19/2016.
 */
public class tuple <E, T>
{
    E mVal1;
    T mVal2;

    public tuple(E valueOne, T valueTwo)
    {
        mVal1 = valueOne;
        mVal2 = valueTwo;
    }


    public E getOne()
    {
        return mVal1;
    }

    public T getTwo()
    {
        return mVal2;
    }


}
