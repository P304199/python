# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: ")) #input


if num < 0:  #check for negative no.s
    print("Factorial not defined.")
else:
   
    result = factorial(num)
    print(f"Factorial of {num} = {result}.")