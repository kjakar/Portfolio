package etec2101;

import java.util.ArrayList;
import java.util.Iterator;

/**
 * Created by Alex Jones on 10/3/2016.
 */
public class BinarySearchTreeIterator<E extends Comparable> implements Iterator<E>
{
    ArrayList<E> mValues = new ArrayList<>();
    int mCurIndex = 0;

    // in order traversal is visit left visit self, visit right.
    // or add left to a list (if left has a left start over at that left) add self to a list, add right to a list (if right has a left restart on the node) basically restart on ever child node to move down the list

    protected BinarySearchTreeIterator(BinarySearchTree.TraversalType TT, BSTNode node)
    {
        // building the array in order
        if(TT == BinarySearchTree.TraversalType.in_order) // in order is left middle right
        {initHelperIn(node);}

        //building the array in pre order
        if(TT == BinarySearchTree.TraversalType.pre_order) //pre order is middle left right
        {initHelperPre(node);}

        // building the array in post
        if(TT == BinarySearchTree.TraversalType.post_order) //post is left right middle
        {initHelperPost(node);}

        // cleaning up
        mCurIndex = 0; // because the init helpers use this to assign all the values to the array list
    }

    @Override
    public boolean hasNext() {return mCurIndex < mValues.size();}

    @Override
    public E next()
    {
        E temp = mValues.get(mCurIndex);
        mCurIndex++;
        return temp;
    }

    private void initHelperIn(BSTNode<E> node)
    {
        //moves left,
        if (node.mLeft != null) {initHelperIn(node.mLeft);}

        // adds the center (or left or right node when it gets to the end)
        mValues.add(mCurIndex, node.mData);
        mCurIndex++;

        // moves to the right (which gets added by the middle
        if (node.mRight != null) {initHelperIn(node.mRight);}
    }

    private void initHelperPre(BSTNode<E> node)
    {
        // adds the center (or left or right node when it gets to the end)
        mValues.add(mCurIndex, node.mData);
        mCurIndex++;

        //moves left,
        if (node.mLeft != null) {initHelperPre(node.mLeft);}

        // moves to the right
        if (node.mRight != null) {initHelperPre(node.mRight);}
    }

    private void initHelperPost(BSTNode<E> node)
    {
        //moves left,
        if (node.mLeft != null) {initHelperPost(node.mLeft);}

        // moves to the right
        if (node.mRight != null) {initHelperPost(node.mRight);}

        // adds the center (or left or right node when it gets to the end)
        mValues.add(mCurIndex, node.mData);
        mCurIndex++;
    }

    public ArrayList getList()
    {
        return mValues;
    }
}

// I know this could be a little cleaner, but it works and I don't want to mess it up.
