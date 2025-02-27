class BankAccount:
    def __init__(self, account_number, balance=0):
        """Initialize bank account with account number and balance."""
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposit funds into the account."""
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw funds from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdrawn. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def display(self):
        """Display account details."""
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")


# Driver Code
if __name__ == "__main__":
    # Take user input for account creation
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))

    # Create a BankAccount object
    account = BankAccount(account_number, initial_balance)

    while True:
        # Display menu options for user
        print("\n--- Bank Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Account Details")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Deposit funds
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == '2':
            # Withdraw funds
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == '3':
            # Display account details
            account.display()

        elif choice == '4':
            # Exit the program
            print("Exiting the bank system.")
            break

        else:
            print("Invalid choice! Please enter a valid option (1-4).")
