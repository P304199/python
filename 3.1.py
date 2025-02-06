#digital root of a number n
def digital_root(n):
    while n >= 10:  # till n is single digit 
        n = sum(int(digit) for digit in str(n))  
    return n

# input
number = 1147
result = digital_root(number)
print(f"The digital root of {number} is {result}")
