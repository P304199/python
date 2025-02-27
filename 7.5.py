import math
class Shape:
    def area(self):
        """Method to calculate area (To be overridden in derived classes)."""
        raise NotImplementedError("Subclasses should implement this method")

    def perimeter(self):
        """Method to calculate perimeter (To be overridden in derived classes)."""
        raise NotImplementedError("Subclasses should implement this method")

#rectangle:
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Override area method for rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Override perimeter method for rectangle."""
        return 2 * (self.width + self.height)
    

#circle:
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Override area method for circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Override perimeter method for circle."""
        return 2 * math.pi * self.radius

# Driver Code
if __name__ == "__main__":
    print("Choose a shape to calculate area and perimeter:")
    print("1. Rectangle")
    print("2. Circle")
    choice = input("Enter the choice (1/2): ")

    if choice == '1':
        # For Rectangle
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        rectangle = Rectangle(width, height)

        print(f"\nRectangle Area: {rectangle.area()}")
        print(f"Rectangle Perimeter: {rectangle.perimeter()}")

    elif choice == '2':
        # For Circle
        radius = float(input("Enter the radius of the circle: "))
        circle = Circle(radius)

        print(f"\nCircle Area: {circle.area()}")
        print(f"Circle Perimeter: {circle.perimeter()}")

    else:
        print("Invalid choice! Please enter 1 for Rectangle or 2 for Circle.")
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
