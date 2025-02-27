class Customer:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdrawn. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """Check the current balance of the account."""
        return self.balance

    def display_account_info(self):
        """Display customer account details."""
        print(f"Customer Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.customers = {}  

    def add_customer(self, name, account_number, balance=0):
        """Create a new customer account."""
        if account_number not in self.customers:
            self.customers[account_number] = Customer(name, account_number, balance)
            print(f"Account for {name} with account number {account_number} created successfully.")
        else:
            print(f"Account number {account_number} already exists.")

    def get_customer(self, account_number):
        """Retrieve customer by account number."""
        return self.customers.get(account_number)

    def remove_customer(self, account_number):
        """Remove a customer account."""
        if account_number in self.customers:
            del self.customers[account_number]
            print(f"Account number {account_number} removed successfully.")
        else:
            print(f"Account number {account_number} not found.")

    def display_all_customers(self):
        """Display information for all customers."""
        if not self.customers:
            print("No customers available.")
        else:
            for customer in self.customers.values():
                customer.display_account_info()


# Driver Code
if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\n--- Bank Menu ---")
        print("1. Add Customer")
        print("2. View Customer Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Remove Customer")
        print("6. Display All Customers")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            # Add Customer
            name = input("Enter customer name: ")
            account_number = int(input("Enter account number: "))
            balance = float(input("Enter initial balance: "))
            bank.add_customer(name, account_number, balance)

        elif choice == '2':
            # View Customer Account
            account_number = int(input("Enter account number: "))
            customer = bank.get_customer(account_number)
            if customer:
                customer.display_account_info()
            else:
                print("Customer not found.")

        elif choice == '3':
            # Deposit Money
            account_number = int(input("Enter account number: "))
            customer = bank.get_customer(account_number)
            if customer:
                amount = float(input("Enter amount to deposit: "))
                customer.deposit(amount)
            else:
                print("Customer not found.")

        elif choice == '4':
            # Withdraw Money
            account_number = int(input("Enter account number: "))
            customer = bank.get_customer(account_number)
            if customer:
                amount = float(input("Enter amount to withdraw: "))
                customer.withdraw(amount)
            else:
                print("Customer not found.")

        elif choice == '5':
            # Remove Customer
            account_number = int(input("Enter account number to remove: "))
            bank.remove_customer(account_number)

        elif choice == '6':
            # Display All Customers
            bank.display_all_customers()

        elif choice == '7':
            # Exit
            print("Exiting the bank system.")
            break

        else:
            print("Invalid choice. Please try again.")
