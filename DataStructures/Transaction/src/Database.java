/**
 * Created by Alex Jones on 8/24/2016.
 */
import java.io.*;
import java.util.Scanner;

public class Database
{

    //the array of transactions
    protected static Transaction[] mTransactions = new Transaction[20];

    //the over all size of the array | I use this to expand the array
    protected static int mSize = 0;

    //I use this to hold the database text file
    protected String mFileName = "base.txt";

    private static int sSiveIncrement = 0;


    //this will never be done
    public static void main(String[] args) throws IOException
    {
        Scanner user_input = new Scanner(System.in);
        loadFile("dBase.txt");

        printMainMenu();

        boolean running = true;
        while(running)
        {
            int input = user_input.nextInt();
            if (input == 1) {
                input = 0;
                System.out.print("How many records would you like to display? | ");
                int num = user_input.nextInt();
                printTransactions(num);
                printMainMenu();

            }

            if (input == 2)
            {
                input = 0;
                removeNull();
                printSortMenu();
                int num = user_input.nextInt();
                sortTransaction(num);
                printTransactions(0);
                printMainMenu();
            }

            if (input == 3)
            {
                System.out.print("what is the account number? | ");
                int acc = user_input.nextInt();
                System.out.print("what is the amount? | ");
                String amount = user_input.next();
                System.out.print("Would you like to make a note? (press enter for none) | ");
                String notes = user_input.next();

                addTransation(Integer.toString(acc), amount, notes);
                printMainMenu();
            }

            if (input == 4)
            {
                System.out.print("what is the ID of the transaction you would like to remove? | ");
                int id = user_input.nextInt();
                removeTransaction(id);
                printMainMenu();
            }

            if (input == 5)
            {
                System.out.println("Bank: we don't take care of that here, use your check book...");
                System.out.println("User: but why wouldn't the bank take ca...");
                System.out.println("Bank: hey hey hey, we ask the questions here not you. -.-");
                printMainMenu();
            }

            if (input == 9) {System.out.print("bye bye!"); running = false;}
        }
    }

    //done
    public static void addTransation(String account, String amount, String notes)
    {
        boolean hasRun = false;
        int transNum = 0;

        // this checks for the highest ID number
        for(int i = 0; i < mTransactions.length; i++)
        {
            if (mTransactions[i] != null)
            {
                if(mTransactions[i].mID >= transNum)
                {
                    transNum = mTransactions[i].mID + 1;
                }
            }
        }

        String transNumStr = Integer.toString(transNum);
        Transaction t = new Transaction(transNumStr, account, amount, notes);

        for(int i =0; i < mTransactions.length; i++)
        {
            if( mTransactions[i] == null)
            {
                mTransactions[i] = t;
                hasRun = true;
                break;
            }
        }

        if(hasRun == false)
        {
            Transaction[] temp = new Transaction[mTransactions.length + 20];
            System.arraycopy(mTransactions, 0, temp, 0, mTransactions.length);
            mTransactions = temp;



        }
        mSize++;
    }

    //done
    public static void sortTransaction(int option)
    {
        // sort by ID
        //<editor-fold desc="sort by ID">
        if(option == 1)
        {
            Boolean sorted = false;
            while(!sorted)
            {
                sorted = true;

                for(int i =0; i < mSize - 1; i++)
                {

                    if(mTransactions[i].mID > mTransactions[i + 1].mID && mTransactions[i+1] != null)
                    {
                        Transaction copy = mTransactions[i];
                        mTransactions[i] = mTransactions[i + 1];
                        mTransactions[i + 1] = copy;
                        sorted = false;
                        break;
                    }
                }
            }
        }
        //</editor-fold>

        //sort but ACCOUNT
        //<editor-fold desc="sort by ACCOUNT">
        if(option == 2)
        {
            Boolean sorted = false;
            while(!sorted)
            {
                sorted = true;

                for(int i =0; i < mSize - 1; i++)
                {

                    if(mTransactions[i].mAccount > mTransactions[i + 1].mAccount && mTransactions[i+1] != null)
                    {
                        Transaction copy = mTransactions[i];
                        mTransactions[i] = mTransactions[i + 1];
                        mTransactions[i + 1] = copy;
                        sorted = false;
                        break;
                    }
                }
            }
        }
        //</editor-fold>

        //SORT BY AMOUNT
        //<editor-fold desc="sort by AMOUNT">
        if(option == 3)
        {
            Boolean sorted = false;
            while(!sorted)
            {
                sorted = true;

                for(int i =0; i < mSize - 1; i++)
                {

                    if(mTransactions[i].mAmount > mTransactions[i + 1].mAmount && mTransactions[i+1] != null)
                    {
                        Transaction copy = mTransactions[i];
                        mTransactions[i] = mTransactions[i + 1];
                        mTransactions[i + 1] = copy;
                        sorted = false;
                        break;
                    }
                }
            }
        }
        //</editor-fold>

        //sort by NOTES
        //<editor-fold desc="sort by Notes">
        if(option == 4)
        {
            Boolean sorted = false;
            while(!sorted)
            {
                sorted = true;

                for(int i =0; i < mSize - 1; i++)
                {

                    if(mTransactions[i].mNotes.length() > mTransactions[i + 1].mNotes.length() && mTransactions[i+1] != null)
                    {
                        Transaction copy = mTransactions[i];
                        mTransactions[i] = mTransactions[i + 1];
                        mTransactions[i + 1] = copy;
                        sorted = false;
                        break;
                    }
                }
            }
        }
        //</editor-fold>
    }

    //done
    public static void removeTransaction(int transID)
    {
        for(int i = 0; i < mTransactions.length; i++)
        {
            if(mTransactions[i] != null)
            {
                if (mTransactions[i].mID == transID)
                {
                    mTransactions[i] = null;
                    mSize --;
                }
            }
        }
    }

    //done
    public static void saveDBase(String outFile) throws IOException
    {
        File export = new File(outFile);
        if(!export.exists())
        {
            export.createNewFile();
        }


        FileWriter fWriter = new FileWriter(export);
        PrintWriter pWriter = new PrintWriter(fWriter);


        for(int i =0; i < mTransactions.length; i++)
        {
            if(mTransactions[i] != null)
            {
                pWriter.println("[" + mTransactions[i].mID + ":" + mTransactions[i].mAccount + ":$" + mTransactions[i].mAmount + ":" + mTransactions[i].mNotes + "]");
            }
        }

        pWriter.close();
    }

    //done : could be reworked
    public static void loadFile(String fileName) throws FileNotFoundException
    {

        File file = new File(fileName);

        Scanner scnr = new Scanner(file);

        int lineNumber = 1;
        while(scnr.hasNextLine())
        {
            //this does the file reading
            String line = scnr.nextLine();
            String line2 = line.substring(1, line.length());
            String[] parts = line2.split(":");
            // this removes the $ sign so that I can turn the amount into an int
            parts[2] = parts[2].substring(1, parts[2].length());
            //this creates a new transaction to add to the list mTransactions
            Transaction temp = new Transaction(parts[0], parts[1], parts[2], parts[3]);

            //this is the for loop that adds the transaction to the first empty slot
            for(int i =0; i < mTransactions.length; i++)
            {
                if( mTransactions[i] == null)
                {
                    mTransactions[i] = temp;
                    mSize++;
                    break;
                }

            }

            //System.out.println(line + parts[0] + parts[1] + parts[2] + parts[3]);
            lineNumber++;
        }

        //System.out.println(mTransactions[0].mID + "   " + mTransactions[1].mID + "   " + mTransactions[2].mID + "  " + mTransactions[3].mID);
        /*

            //this is all you need for text splitting
        String q = "[a:bb:2:5]";
        String q1 = q.substring(1, q.length());
        String[] qparts = q1.split(":");
        int qnum = Integer.valueOf(qparts[2]);

        */
    }

    //done
    public static void printMainMenu()
    {
        System.out.println(" ****************\n * Main Menu    *\n ****************\n 1. Display Records\n 2. Sort Records\n 3. Add Record\n 4. Remove Record\n 5. Show account balance\n 9. Quit\n");
    }

    //done
    public static void printSortMenu()
    {
        System.out.println("Sort by:\n" +
                "       1: ID\n" +
                "       2: Account#\n" +
                "       3: Amount\n" +
                "       4: Note-length");
    }


    //done | array needs colapsing for this to work perfect
    public static void printTransactions(int ammount)
    {

        //this handles how many you should print
        int val = ammount;

        //this lowers the value to the total amount of transactions if the value is above the total amount of transactions
        if(val > mTransactions.length + 1)
        {
            val = mTransactions.length - 1;
        }
        else if(val == 0){val = mTransactions.length - 1;}

        //this prints the transactions
        for(int i =0; i < val; i++)
        {
            //this makes sure it doesn't try and print a null slot in the mTransactions array
            if(mTransactions[i] != null)
            {
                System.out.println(i + "[" + mTransactions[i].mID + ":" + mTransactions[i].mAccount + ":$" + mTransactions[i].mAmount + ":" + mTransactions[i].mNotes + "]");
            }
        }

    }

    public static void removeNull()
    {
        Boolean sorted = false;
        while(!sorted)
        {
            sorted = true;

            for(int i =0; i < mTransactions.length - 1; i++)
            {

                if(mTransactions[i] == null && mTransactions[i + 1] != null)
                {
                    mTransactions[i] = mTransactions[i + 1];
                    sorted = false;
                    break;
                }
            }
        }
    }
}


