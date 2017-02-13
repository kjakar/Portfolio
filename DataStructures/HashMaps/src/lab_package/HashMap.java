package lab_package;

/**
 * Created by Alex on 10/19/2016.
 */
public class HashMap<E, T> // key first then value
{
    protected float mCapacity ;
    protected tuple<E, T>[] mData;
    protected int mSize;
    private int mUsed = 0;

    // this is done
    public HashMap(float capacity, int size)
    {
        mCapacity = capacity;
        mData = new tuple[size];
        mSize = size;
    }

    //this is done
    public void set(E key, T value)
    {
        // this re-sizes the hashMap
        if(mUsed/mSize >= mCapacity)
        {
            tuple<E, T>[] temp = mData;
            mData = new tuple[mSize * 2];
            mSize = mSize * 2;
            mUsed = 0;

            for(int i = 0; i < mSize / 2; i++)
            {
                if(temp[i] != null)
                {
                    E tempKey = temp[i].getOne();
                    T tempVal = temp[i].getTwo();

                    tuple<E, T> tempTup = new tuple<E, T>(tempKey, tempVal);
                    int where = tempKey.hashCode() % mSize;

                    addHelp(tempTup, where);
                }
            }
        }

        tuple<E, T> temp = new tuple<E, T>(key, value);
        int where = key.hashCode() % mSize;

        addHelp(temp, where);
    }

    // this is done, we use this in set
    private void addHelp(tuple t, int where)
    {
        //this rolls to the front of the list
        if(where > mSize)
            where -= mSize;

        if(mData[where] != null)
        {
           addHelp(t, where +1);
        }

        else
            mData[where] = t; mUsed ++;
    }

    //this is done.
    public int getSize(){return mUsed;}


    // I think this is done
    public T get(E key)
    {
        int where = key.hashCode() % mSize;

        if(mData[where] != null)
        {
            if (mData[where].getOne() == key)
                return mData[where].getTwo();

            else
            {
                // this is how the for loop would have looked for the set method if I didn't use the helper. so bam, best of both worlds
                for (int i = where + 1; i < mSize + 1; i ++)
                {
                    //this rolls over the list
                    if(i == mSize)
                        i -= mSize;
                    // this moves through the list until it finds the right key, or a null spot.
                    if(mData[where] == null)
                        {return null;}
                    else if (mData[where].getOne() == key)
                        return mData[where].getTwo();
                }
                return null;
            }
        }
        else
            return null;
    }


    public HashMapIterator<E, T> iterator(iteratorType it)
    {
        HashMapIterator<E, T> t = new HashMapIterator(it, this);
        return t;
    }

    //this is done
    public void remove(E key)
    {
        int where = key.hashCode() % mSize;

        if(mData[where].getOne() == key)
        {
            mData[where] = null;
        }

        else
            for(int i = where + 1; i < mData.length; i++)
            {
                if(mData[i] != null && mData[i].getOne() == key)
                    mData[i] = null;
                else if(mData[i] == null)
                    break;
            }
    }

    //this needs tested
    @Override
    public String toString()
    {
        String tempString = "{";

        for (int i = 0; i < mData.length; i++)
        {
            if(mData[i] != null)
            {
                tempString += mData[i].getOne().toString() + " : " + mData[i].getTwo().toString() + ", ";
            }
        }

        String tempTwo = tempString.substring(0, tempString.length() -3);
        tempTwo += "}";

        return tempTwo;
    }

    protected tuple[] getData(){return mData;}

    public enum iteratorType {Key,Value;}

}
