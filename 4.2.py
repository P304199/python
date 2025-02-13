# Sherlock and Squares
sqlist = []
low = int(input("Enter the low value: "))
upper = int(input("Enter the upper value: "))

print("Squares are -> ")

for i in range(low + 1, upper):
    square = i ** 2
    if low <= square <= upper:
        sqlist.append(square)

if not sqlist:
    print("NULL")
else:
    print(sqlist)