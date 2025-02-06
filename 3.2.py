#to check if a number is fibo or not fibo
import math

def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# input
n = int(input("Enter a number: "))
if is_fibonacci(n):
    print("IsFibo")
else:
    print("IsNotFibo")
