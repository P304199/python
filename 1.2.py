#write a program that generates 100 random integers that are either 0 or 1.
import random

# Generate a list of 100 random integers (0 or 1)
random_list = [random.randint(0, 1) for _ in range(100)]

print(random_list)

# Function to find the longest run of 0s
def longest_run_of_zeroes(lst):
    max_run = 0
    current_run = 0
    for num in lst:
        if num == 0:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    return max_run

# Find and print the longest run of 0s
longest_run = longest_run_of_zeroes(random_list)
print("The longest run of 0s is:", longest_run)