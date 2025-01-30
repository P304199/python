#equivalence classes validity

equivalence_classes = {0: [], 1: [], 2: [], 3: [], 4: []}

#numbers from 1 to 1000
for num in range(1, 1001):
    remainder = num % 5  
    equivalence_classes[remainder].append(num)  


for i in range(5):
    print(f"Equivalence Class {i} (mod 5): {equivalence_classes[i][:10]}...") 