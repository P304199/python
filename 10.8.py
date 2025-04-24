import numpy as np

arr = np.array(['apple', 'banana', 'cherry', 'date'])

centered = np.array([s.center(15, '_') for s in arr])
left_justified = np.array([s.ljust(15, '_') for s in arr])
right_justified = np.array([s.rjust(15, '_') for s in arr])

print("Centered:")
print(centered)
print("\nLeft-Justified:")
print(left_justified)
print("\nRight-Justified:")
print(right_justified)
