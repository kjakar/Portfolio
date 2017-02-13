import java.util.Iterator;

/**
 * Created by Alex Jones on 9/7/2016.
 */


public class LinkedList<E> // the 'E' here assigns the type of data that can be held by this class
{
    //==================================================================================================================
    //      this is the node class its job is to hold different data types to put into our list
    //==================================================================================================================
    protected class Node<T>
    {
        Node<T> mNext = null;
        Node<T> mLast = null;
        T mData;

        //constructor 1
        public Node(T data, Node next, Node last)
        {
            mData = data;
            mNext = next;
            mLast = last;
        }
        // constrictor 2
        public Node(T data){mData = data;}

        @Override
        public String toString()
        {
            String s;
            if (mData instanceof String)
            {
                s = (String) mData;
                return s;
            }
            else if (mData instanceof Integer)
            {
                s = Integer.toString((Integer) mData);
                return s;
            }
            else if (mData instanceof Float)
            {
                s = Float.toString((Float) mData);
                return s;
            }
            else return null;

        }

    }
    //--------------------------------- this is the end of the node class ----------------------------------------------


    //==================================================================================================================
    //   this is the iterator, it is basically the indexer, it moves a pointer from the first slot to the last slot
    //==================================================================================================================
    public class LinkedListIterator<T>
    {
        Node current;
        Boolean move = true; // true moves forward false moves backwards

        public LinkedListIterator(Node n){current = n;}
        public LinkedListIterator(Node n, boolean direction){current = n; move = direction;}

        public boolean hasNext()
        {
            if (move)
            {
                if (current.mNext == null)
                    return false;
                else return true;
            }
            else
            {
                if (current.mLast == null)
                    return false;
                else return true;
            }
        }

        public void next()
        {
            if(move){current = current.mNext;}
            else{current = current.mLast;}
        }

        public void last()
        {
            if(move){current = current.mLast;}
            else{current = current.mNext;}
        }
        public void remove()
        {
            current.mNext.mLast = current.mLast;
            current.mLast.mNext = current.mNext;
        }
        public void addAfter(T data)
        {
            Node<T> n = new Node<>(data);
            n.mNext = current.mNext;
            n.mLast = current;
            current.mNext = n;
        }
        public void addBefore(T data)
        {

            Node<T> n = new Node<>(data);
            n.mNext = current;
            n.mLast = current.mLast;
            current.mLast.mNext = n;
        }

    }
    // --------------------------------   this is the end of the iterator class ----------------------------------------


    Node<E> mHead = null; // this is the start of the linked list
    Node<E> mTail= null; // this is the end of the linked list
    int mSize = 0; //this is how big the linked list is

    @Override
    //Done! (works with int strings and floats!)
    public String toString()
    {

        String s = "< ";
        LinkedListIterator<E> LI;

        if(mHead != null)
        {LI = new LinkedListIterator<>(mHead);}
        else if( mTail != null)
        {LI = new LinkedListIterator<>(mTail);}
        else {s = "<Empty>"; return s;}

        if(mSize == 0)
        {
            s = "<Empty>";
            return s;
        }
        else
        {

            for(int i = 0; i < mSize; i++)
            {
                s = s + "[" + LI.current + "] ";
                if(LI.hasNext())
                    LI.next();

            }

            s = s + ">";
            return s;
        }
    }
    //done
    public void addToEnd(E data)
    {
        Node<E> n = new Node<>(data);

        if(mSize == 0)
        {
            mTail = n;
            mSize++;
            //System.out.print("3");
        }
        else if(mTail == null)
        {
            if (mSize == 1)
            {
                if (mTail == null)
                {
                    mTail = n;
                    n.mLast = mHead;
                    mHead.mNext = mTail;
                    mSize++;
                    //System.out.print("2");
                }
                else
                {
                    mHead = mTail;
                    mHead.mNext = n;
                    n.mLast = mHead;
                    mTail = n;
                    mSize++;
                    //System.out.print("1");
                }
            }
            else
            {
                LinkedListIterator<E> LI = new LinkedListIterator<>(mHead);
                for(int i = 0; i < mSize -1; i++){LI.next();}
                mTail = n;
                mTail.mLast = LI.current;
                LI.current.mNext = n;
                mSize ++;
            }
        }
        else
        {
            mTail.mNext = n;
            n.mLast = mTail;
            mTail = n;
            mSize++;
            //System.out.print("4");
        }
    }
    //done
    public void addToBegin(E data)
    {
        Node<E> n = new Node<>(data);
        if(mSize == 0)
        {
            mHead = n;
            mSize++;
            //System.out.print("-2");
        }
        else if(mSize == 1)
        {
            if (mHead == null) {
                mHead = n;
                n.mNext = mTail;
                mTail.mLast = mHead;
                mSize++;
                //System.out.print("-1");

            }
            else
            {
                n.mNext = mHead;
                mHead.mLast = n;
                mHead = n;
                mSize++;
                //System.out.print("-3");
            }
        }
        else
        {

            n.mNext = mHead;
            mHead.mLast = n;
            mHead = n;
            mSize++;
            //System.out.print("-4");
        }
    }
    //done
    public String length(){return Integer.toString(mSize);} // this returns the length of the linked list as a string
    //done!
    public E at(int index, boolean side)
    {
        if(side)
        {
        LinkedListIterator<E> LI = new LinkedListIterator<>(mHead);

        for(int i = 0; i < index; i++)
        {
            LI.next();
        }

        return (E) LI.current;
        }
        else
        {
            LinkedListIterator<E> LI = new LinkedListIterator<>(mTail);

            for(int i = 0; i < index; i++)
            {
                LI.last();
            }

            return (E) LI.current;
        }
    }
    // done!
    public E at(int index)
    {
        LinkedListIterator<E> LI = new LinkedListIterator<>(mHead);

        for(int i = 0; i < index; i++)
        {
            LI.next();
        }

        return (E) LI.current;
    }
    public int removeAll(E data)
    {
        int count = 0;
        LinkedListIterator<E> LI = new LinkedListIterator<>(mHead);

        for(int i = 0; i < mSize; i++)
        {
            if(LI.current.mData == data) {LI.remove(); count++; mSize--;}
            LI.next();
        }

        return count;
    }
    public void insert(int index, E data)
    {

        if(index > mSize-1){System.out.println("maybe try a smaller size love...");}
        else if(index == 0){addToBegin(data);}
        else if(index == mSize -1){addToEnd(data);}
        else
            {
                LinkedListIterator<E> LI = new LinkedListIterator<>(mHead);

                for(int i = 0; i < index; i++)
                {
                    LI.next();
                }

                LI.addBefore(data);
                mSize++;

            }



    }
    //done
    public int count(E data)
    {
        int count = 0;
        LinkedListIterator<E> LI = new LinkedListIterator<>(mHead);

        for(int i = 0; i < mSize; i++)
        {
            if(LI.current.mData == data) {count++;}
            LI.next();
        }

        return count;
    }
    //done
    public LinkedListIterator iterator(){ LinkedListIterator<E> LI = new LinkedListIterator<>(mHead, true); return LI;}
    //done
    public LinkedListIterator riterator(){LinkedListIterator<E> LI = new LinkedListIterator<>(mTail, false); return LI;}


    public static void main(String[] args)
    {

        LinkedList<Integer> L = new LinkedList<>();
        //LinkedListIterator<Integer> LI = new LinkedListIterator<>(L.mHead);

        L.addToBegin(3);
        System.out.println(L);
        L.addToBegin(2);
        System.out.println(L);
        L.addToBegin(1);
        System.out.println(L);
        L.addToEnd(4);
        System.out.println(L);
        L.addToEnd(5);
        System.out.println(L);
        L.addToEnd(6);
        System.out.println(L);
        L.addToEnd(7);
        System.out.println(L);
        L.addToEnd(8);
        System.out.println(L);
        //these work oddly? as long as there is at least 4 objects in the LL printing works like normal,
        // but if there are less it prints a copy of the last item? I have no clue how I managed that
        // @@@@@@ NOTE @@@@ I seemed to have fixed this~~~~~~~~~~~~~


        L.insert(0,7);         // insert works fine
        System.out.println(L); // so does print :P
        L.insert(6, 13);
        System.out.println(L);

        System.out.println(L.at(6));        // the 'at' method works fine in both directions and has two constructors
        System.out.println(L.at(6, false)); // one with and without the true/false input
                                            // I was also going to make this work with -6 but I didn't have time

        System.out.println(L.count(3)); // count works fine
        L.removeAll(3);                 // removeAll only works if the item being removed is not the first
        System.out.println(L.count(3)); // or last item in the LL

        System.out.println(L);
        System.out.println(L.length()); // length works fine

        LinkedList<String>.LinkedListIterator<String> LI = L.iterator();
        LinkedList<String>.LinkedListIterator<String> LI2 = L.riterator();
        if(LI.hasNext()){System.out.println("LI works!");}
        if(LI2.hasNext()){System.out.println("LI2 works!");}
        //these confused me a bit, I couldn't work out what they did at first:
        //after trying to make an iterator to debug I realized that I couldn't and this was a way to use
        //the iterator out side of this class.
        //if the iterator isn't causing any of the other problems in this code, these should work fine

    }



}
