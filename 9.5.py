import numpy as np

array = np.array(['apple', 'banana', 'cherry', 'date'])


centered_array = np.array([str(item).center(15, '_') for item in array])  
left_justified_array = np.array([str(item).ljust(15, '_') for item in array])  
right_justified_array = np.array([str(item).rjust(15, '_') for item in array])  



print("Centered Alignment:")
print(centered_array)

print("\nLeft-Justified Alignment:")
print(left_justified_array)

print("\nRight-Justified Alignment:")
print(right_justified_array)
