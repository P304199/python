#utopian tree
def utopian_tree_growth(n):
    height = 1  
    for cycle in range(1, n + 1):
        if cycle % 2 == 1:  
            height *= 2
        else:  
            height += 1
    return height

# Example 
n = int(input("Enter the number of growth cycles: "))  # Input number of growth cycles
result = utopian_tree_growth(n)
print(f"Height of the tree after {n} cycles: {result} meters")
