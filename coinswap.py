t = int(input("test cases :"))
N=int(input("number of boxes :"))
X=int(input("current position of coin :"))
for j in range(t):
    print("\nTEST CASE", j)
    S=int(input("\n no of swaps :"))
    for i in range(S):
        a=int(input("Enter first box to be swapped :"))
        b=int(input("Enter second box to be swapped :"))
        if X == a:
            X = b
        elif X == b:
            X = a
print("The current position of the coin is :",X)