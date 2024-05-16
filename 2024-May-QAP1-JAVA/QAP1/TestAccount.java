public class TestAccount {
    public static void main(String[] args) {
        // Create two accounts
        Account acc1 = new Account("A123", "John Doe", 5000);
        Account acc2 = new Account("B456", "Jane Smith", 4000);

        // Display balance of both accounts
        System.out.println("Account 1 balance: " + acc1.getBalance());
        System.out.println("Account 2 balance: " + acc2.getBalance());

        // Transfer $1000 from account 1 to account 2
        acc1.transferTo(acc2, 1000);

        // Display balance of both accounts again
        System.out.println("After transfer:");
        System.out.println("Account 1 balance: " + acc1.getBalance());
        System.out.println("Account 2 balance: " + acc2.getBalance());
    }
}
