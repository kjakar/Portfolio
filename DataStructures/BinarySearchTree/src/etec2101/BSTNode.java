package etec2101;

import java.util.ArrayList;

/**
 * Created by Alex Jones on 10/3/2016.
 */

class BSTNode <E extends Comparable>
{

    protected static int heightHelper = 0;
    protected E mData;
    protected BSTNode mLeft;
    protected BSTNode mRight;
    protected BSTNode mParent;
    protected BinarySearchTreeIterator iterator;
    String s = "go;";
    String t = "g";

    public BSTNode(E value){mData = value;} // this is for making the root

    public BSTNode(E value, BSTNode parent){mData = value; mParent = parent;} // this is for making all other BSTNodes

    // this is done
    public void add(E val)
    {
        BSTNode temp = new BSTNode(val, this);
        if(mLeft == null && val.compareTo(mData) < 0)
            mLeft = temp;
        else if (mRight == null && val.compareTo(mData) > 0)
            mRight = temp;
        else if (mLeft != null && val.compareTo(mData) > 0)
            mLeft.add(val);
        else if (mRight != null && val.compareTo(mData) > 0)
            mRight.add(val);
    }

    // this is done.
    public int getHeight()
    {
        // I feel like this is cheating xD, #breakTheSystem
        if (mParent != null) {heightHelper++; return mParent.getHeight();}
        else
        {
            int temp = heightHelper;
            heightHelper = 0;
            return temp;
        }

    }

    // this is done
    public int compareTo(E val){return mData.compareTo(val);}

    //this is done
    public BinarySearchTreeIterator iterator(BinarySearchTree.TraversalType TT, BSTNode node)
    {
        iterator = new BinarySearchTreeIterator(TT, node);
        return iterator;
    }

    /* this was to test things
    public static void main(String[] args)
    {
        int x = 4;
        int y = 5;
        int z = 2;

        System.out.print(y/z + "  " + x/z + "  " + y%z + "  " + x%z);
    }
    */
}
