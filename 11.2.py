import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

# Convert to uppercase
upper_case = s.str.upper()

# Convert to lowercase
lower_case = s.str.lower()

# Find the length of the string values
length_of_strings = s.str.len()

print("Original Series:")
print(s)

print("\nUppercase:")
print(upper_case)

print("\nLowercase:")
print(lower_case)

print("\nLength of strings:")
print(length_of_strings)
