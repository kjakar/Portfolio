package lab_package;

/**
 * Created by Alex on 10/19/2016.
 */
public class HashSet<E> extends HashMap<E, Integer>
{

    public HashSet(float capacity, int size)
    {
        super(capacity, size);
    }

    public void add(E value)
    {
        super.set(value, new Integer(1));
    }

    @Override
    public String toString()
    {
        String tempString = "{";

        for (int i = 0; i < mData.length; i++)
        {
            if(mData[i] != null)
            {
                tempString += mData[i].getOne().toString() + ", ";
            }
        }

        String tempTwo = tempString.substring(0, tempString.length() -3);
        tempTwo += "}";

        return tempTwo;
    }

    public HashSet union(HashSet<E> compare)
    {
        HashSet tempHash = new HashSet(mCapacity, mSize + compare.mSize);

        //this goes through all the self data and adds it to the new list
        for(int i = 0; i < mSize; i++)
        {
            if (mData[i] != null)
                tempHash.add(mData[i].getOne());
        }

        //this goes through all the compare data and adds it to the new list, and because add doesn't allow copies
        // we have no problem with having more than one of the same key in this list.
        for(int i = 0; i < compare.mSize; i++)
        {
            if (compare.mData[i] != null)
                tempHash.add(compare.mData[i].getOne());
        }

        //returns a new hashSet instead of changing the current one
        return tempHash;
    }


    public HashSet intersection(HashSet<E> compare)
    {
        HashSet tempHash = new HashSet(mCapacity, mSize);

        //because the keys have to be in both list, there is no need to go through and check 1 to 2 and then 2 to 1.
        for(int i = 0; i < mSize; i++)
            if(helper(mData[i], compare))
                tempHash.add(mData[i].getOne());

        return tempHash;
    }


    public HashSet relativeDifference(HashSet<E> compare)
    {
        HashSet tempHash = new HashSet(compare.mCapacity, compare.mSize);

        // all we need is the objects in the right side that aren't in the left side
        for(int i = 0; i < compare.mSize; i++)
            //if it's NOT in the left side add it.
            if(helper(compare.mData[i], this) == false)
                tempHash.add(compare.mData[i].getOne());

        return tempHash;
    }

    public HashSet symmetricDifference(HashSet<E> compare)
    {
        HashSet tempHash = new HashSet(compare.mCapacity, compare.mSize);

        //this goes through the right side
        for(int i = 0; i < compare.mSize; i++)
            //if it's NOT in the left side add it.
            if(helper(compare.mData[i], this) == false)
                tempHash.add(compare.mData[i].getOne());

        //this goes through the left side
        for(int i = 0; i < mSize; i++)
            //if it's NOT in the right side add it.
            if(helper(mData[i], compare) == false)
                tempHash.add(mData[i].getOne());

        return tempHash;
    }


    // returns true if the object is in both sets
    private boolean helper(tuple t, HashSet set)
    {
        for(int i = 0; i < set.mData.length; i++)
        {
            if(set.mData[i] == t )
                return true;
        }

        return false;
    }
}
