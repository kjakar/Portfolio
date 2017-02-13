/**
 * Created by Alex Jones on 8/24/2016.
 */
public class Transaction
{

    protected int mID;
    protected int mAccount;
    protected float mAmount;
    protected String mNotes;

    public Transaction(String ID, String account, String ammount, String notes)
    {
        mID = Integer.parseInt(ID);
        mAccount = Integer.parseInt(account);
        mAmount = Float.parseFloat(ammount);
        mNotes = notes.substring(0, notes.length()-1);
    }


    //done not tested
    public boolean compare(Transaction t, int option)
    {

        if(option == 1)
        {
            if (t.mID < mID) {return true;}
            else if(t.mID > mID){return false;}
        }
        else if(option == 2)
        {
            if (t.mAccount < mAccount) {return true;}
            else if(t.mAccount > mAccount){return false;}
        }
        else if(option == 3)
        {
            if (t.mAmount < mAmount) {return true;}
            else if(t.mAmount > mAmount){return false;}
        }

        return false;

    }



}
