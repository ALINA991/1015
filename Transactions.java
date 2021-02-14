import java.util.Scanner;

// class to manage bank transactions as defined in Devoir 1 IFT1025
public class Transactions {

    public static void main( String[] args ) {
	// Scanner connected to the System.in
	Scanner myScanner = new Scanner( System.in );

	// String for each transaction line
	String line = "Go!";

	// Bank instance to be implemented
	Bank bank = new Bank();

	// while there are transactions,
	//     read the line
	//     process the corresponding transaction
	while( ! line.equals( "end" ) ) {
	    line = myScanner.nextLine();
	    bank.processTransaction( line );
	}
    }
}
