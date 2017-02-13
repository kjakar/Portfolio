package lab_package;

/**
 * Created by Alex on 10/19/2016.
 */

public class HashMapIterator<E, T>
{
    tuple[] mData;
    HashMap.iteratorType mType;
    int mIndex = 0;


    public HashMapIterator(HashMap.iteratorType type,HashMap map)
    {
        mData = map.getData();
        mType = type;
    }

    public boolean hasNext()
    {

        for(int i = mIndex + 1; i < mData.length; i++)
        {
            if(mData[i] != null)
                return true;
        }

        return false;
    }

    public Object Next()
    {
        if(this.hasNext())
        {
            if (mType == HashMap.iteratorType.Key)
            {
                if (mData[mIndex] != null)
                    return mData[mIndex].getOne();
                else
                {
                    mIndex++;
                    return this.Next();
                }
            }
            else if (mType == HashMap.iteratorType.Value)
            {
                if (mData[mIndex] != null)
                    return mData[mIndex].getTwo();
                else
                {
                    mIndex++;
                    return this.Next();
                }
            }

            else return null;
        }

        else return null;
    }
}
