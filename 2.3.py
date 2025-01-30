#To count the number of positions where N is divisible
def count_divisible_digits(N):
    count = 0
    for digit in str(N):  # Convert N to a string 
        if digit != '0':  # Skip zero 
            if N % int(digit) == 0:  # Check if N is divisible by the digit
                count += 1
    return count

# Input 
N = int(input("Enter a number: "))


result = count_divisible_digits(N)
print(f"The number of positions where digits exactly divide {N} is: {result}")