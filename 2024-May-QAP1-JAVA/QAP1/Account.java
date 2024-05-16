public class Account {
    private final String id;
    private final String name;
    private int balance = 0;

    // Constructor with id and name
    public Account(String id, String name) {
        this.id = id;
        this.name = name;
    }

    // Constructor with id, name, and balance
    public Account(String id, String name, int balance) {
        this.id = id;
        this.name = name;
        this.balance = balance;
    }

    // Getter for id
    public String getID() {
        return id;
    }

    // Getter for name
    public String getName() {
        return name;
    }

    // Getter for balance
    public int getBalance() {
        return balance;
    }

    // Method to credit an amount to the account
    public int credit(int amount) {
        balance += amount;
        return balance;
    }

    // Method to debit an amount from the account
    public int debit(int amount) {
        if (amount <= balance) {
            balance -= amount;
        } else {
            System.out.println("Amount exceeded balance");
        }
        return balance;
    }

    // Method to transfer amount to another account
    public int transferTo(Account another, int amount) {
        if (amount <= balance) {
            this.debit(amount);
            another.credit(amount);
        } else {
            System.out.println("Amount exceeded balance");
        }
        return balance;
    }

    // toString method to return account details
    @Override
    public String toString() {
        return "Account[id=" + id + ",name=" + name + ",balance=" + balance + "]";
    }
}
