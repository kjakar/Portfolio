package etec2101;

import java.util.ArrayList;

/**
 * Created by Alex Jones on 10/3/2016.
 */

public class BinarySearchTree<E extends Comparable>
{
    BSTNode mRoot;
    int mSize = 0;

    public BinarySearchTree(){}

    // this is done
    public void add(E val)
    {
        if (mRoot == null)
        {mRoot = new BSTNode(val);}
        else
            mRoot.add(val);
        mSize ++;
    }

    // this is done
    public void remove(E val)
    {
        BinarySearchTreeIterator tempIter = iterator(TraversalType.in_order);
        ArrayList tempList = tempIter.getList();

        for(int i = 0; i < tempList.size()-1; i++)
        {
            if (tempList.get(i) == val)
                tempList.remove(i);
        }

        reset(tempList);
    }

    //I gave up on this
    @Override
    public String toString()
    {
        String tempString = "";
        BinarySearchTreeIterator tempIter = iterator(TraversalType.in_order);
        ArrayList tempList = tempIter.getList();

        for(int i = 0; i < tempList.size() -1; i ++)
        {
            tempString = tempString + tempList.get(i).toString() + " ";
        }
        return "temp string";
    }

    //this is done
    public int getHeight()
    {
        int height = 0;

        if (heightHelper(true).getHeight() > height)
            height = heightHelper(true).getHeight();
        if (heightHelper(false).getHeight() > height)
            height = heightHelper(false).getHeight();

        return height;
    }

    //this is done
    private BSTNode heightHelper(boolean left)
    {
        BSTNode curNode = mRoot;

        boolean done = false;

        while(done == false)
        {
            if(left)
            {
                if(curNode.mLeft != null)
                    curNode = curNode.mLeft;
                else
                    done = true;
            }

            if(left == false)
            {
                if(curNode.mRight != null)
                    curNode = curNode.mRight;
                else
                    done = true;
            }
        }

        return curNode;
    }

    //this is done
    public int count(E val)
    {
        BinarySearchTreeIterator<E> temp = iterator(TraversalType.in_order);
        ArrayList<E> tempList = temp.getList();
        int tempInt = 0;

        for(int i = 0; i < tempList.size() - 1; i++)
        {
            if (tempList.get(i).compareTo(val) == 0)
                tempInt ++;
        }

        return tempInt;
    }

    //this is done
    public BinarySearchTreeIterator iterator(TraversalType TT){return mRoot.iterator(TT, mRoot);}

    //this is done
    public enum TraversalType
    {
        post_order,
        pre_order,
        in_order,
    }

    //this is done
    public void rebalance()
    {
        BinarySearchTreeIterator<E> temp = iterator(TraversalType.post_order); // I use post order here to mix up the data so that it can build a tree not a line.

        ArrayList<E> tempList = temp.getList(); // this is a list of all the data

        int x = tempList.size(); //this is to make sure dividing gives and int
        int y = x/2 ; // this is to set the new root.

        // in the case that the list length is odd
        if(x % 2 != 0)
        {
            int z = tempList.size() - 1; //this is to work backwards
            mRoot = new BSTNode(tempList.get(y + 1)); //this sets the new root

            for(int i = 0; i < y; i++)
            {
                mRoot.add(tempList.get(i)); // this adds from the front
                mRoot.add(tempList.get(z)); // this adds from the back, to mix up the data a bit more
                z --;
            }
        }
        else if(x % 2 == 0)
        {
            int z = tempList.size() - 1; //this is to work backwards
            mRoot = new BSTNode(tempList.get(y)); //this sets the new root

            for(int i = 0; i < y; i++)
            {
                mRoot.add(tempList.get(i)); // this adds from the front
                mRoot.add(tempList.get(z)); // this adds from the back, to mix up the data a bit more
                z --;
            }

            mRoot.add(tempList.get(z)); // this gets the odd one out
        }

    }

    public void reset(ArrayList<E> list)
    {
        ArrayList<E> tempList = list;
        int x = tempList.size(); //this is to make sure dividing gives and int
        int y = x/2 ; // this is to set the new root.

        // in the case that the list length is odd
        if(x % 2 != 0)
        {
            int z = tempList.size() - 1; //this is to work backwards
            mRoot = new BSTNode(tempList.get(y + 1)); //this sets the new root

            for(int i = 0; i < y; i++)
            {
                mRoot.add(tempList.get(i)); // this adds from the front
                mRoot.add(tempList.get(z)); // this adds from the back, to mix up the data a bit more
                z --;
            }
        }
        else if(x % 2 == 0)
        {
            int z = tempList.size() - 1; //this is to work backwards
            mRoot = new BSTNode(tempList.get(y)); //this sets the new root

            for(int i = 0; i < y; i++)
            {
                mRoot.add(tempList.get(i)); // this adds from the front
                mRoot.add(tempList.get(z)); // this adds from the back, to mix up the data a bit more
                z --;
            }

            mRoot.add(tempList.get(z)); // this gets the odd one out
        }

    }

    /* ===========================================  This was in class work on recursion. ==========================
    public static boolean isPal(String s)
    {
        if(s.length() == 1)
            return true;
        else if(s.charAt(0) ==  s.charAt(s.length() - 1))
        {
            String temp = s.substring(1, s.length() - 1);
            return isPal(temp);
        }
        else return false;

    }
    public static void main(String[] args)
    {
        System.out.println(isPal("r"));
    }
    ============================================================================================================    */

}
