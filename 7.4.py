class Employee:
    def __init__(self, name, salary):
        """Initialize employee with name and salary."""
        self.name = name
        self.salary = salary

    def __add__(self, other):
        """Overload + operator to combine salaries of two employees."""
        if isinstance(other, Employee):
            combined_salary = self.salary + other.salary
            return Employee(f"Combined: {self.name} & {other.name}", combined_salary)
        else:
            return NotImplemented

    def __sub__(self, other):
        """Overload - operator to find the difference in salaries between two employees."""
        if isinstance(other, Employee):
            salary_diff = abs(self.salary - other.salary)
            return salary_diff
        else:
            return NotImplemented

    def __lt__(self, other):
        """Overload < operator to compare employees based on salary (less than)."""
        if isinstance(other, Employee):
            return self.salary < other.salary
        return NotImplemented

    def __gt__(self, other):
        """Overload > operator to compare employees based on salary (greater than)."""
        if isinstance(other, Employee):
            return self.salary > other.salary
        return NotImplemented

    def __eq__(self, other):
        """Overload == operator to check if two employees have equal salaries."""
        if isinstance(other, Employee):
            return self.salary == other.salary
        return NotImplemented

    def display(self):
        """Display employee information."""
        print(f"Name: {self.name}, Salary: {self.salary}")


# Driver Code
if __name__ == "__main__":
    # Take user input for employees
    name1 = input("Enter the name of the first employee: ")
    salary1 = float(input(f"Enter the salary of {name1}: "))
    
    name2 = input("Enter the name of the second employee: ")
    salary2 = float(input(f"Enter the salary of {name2}: "))

    # Create Employee objects
    employee1 = Employee(name1, salary1)
    employee2 = Employee(name2, salary2)

    # Display the employees' details
    print("\nEmployee 1 details:")
    employee1.display()
    print("\nEmployee 2 details:")
    employee2.display()

    # Combine employees using overloaded +
    combined_employee = employee1 + employee2
    print("\nCombined Employee details:")
    combined_employee.display()

    # Compare salaries using overloaded -
    salary_difference = employee1 - employee2
    print(f"\nSalary difference between {employee1.name} and {employee2.name}: {salary_difference}")

    # Compare using <, >, ==
    if employee1 < employee2:
        print(f"{employee1.name} has a lower salary than {employee2.name}")
    elif employee1 > employee2:
        print(f"{employee1.name} has a higher salary than {employee2.name}")
    else:
        print(f"{employee1.name} and {employee2.name} have equal salaries")
