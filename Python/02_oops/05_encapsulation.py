class Account:
    def __init__(self, owner: str, balance: float) -> None:
        self.__owner = owner       # Private attribute
        self.__balance = balance   # Private attribute

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, amount: float) -> None:
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount")

    def show(self) -> None:
        print(f"Owner: {self.__owner}, Balance: {self.__balance}")

# Test
acc = Account("Alice", 1000)
acc.show()               # Output: Owner: Alice, Balance: 1000
print(acc.balance)       # Output: 1000
acc.balance = 1200
print(acc.balance)       # Output: 1200
acc.balance = -500       # Output: Invalid amount


"""
Java Equivalent:

public class Account {
    private String owner;
    private double balance;

    public Account(String owner, double balance) {
        this.owner = owner;
        this.balance = balance;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double amount) {
        if (amount >= 0) {
            this.balance = amount;
        } else {
            System.out.println("Invalid amount");
        }
    }

    public void show() {
        System.out.println("Owner: " + owner + ", Balance: " + balance);
    }

    public static void main(String[] args) {
        Account acc = new Account("Alice", 1000);
        acc.show();
        System.out.println(acc.getBalance());
        acc.setBalance(1200);
        System.out.println(acc.getBalance());
        acc.setBalance(-500);
    }
}
"""
