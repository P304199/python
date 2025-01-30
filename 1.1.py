#using for loop
#a)a list of numbers from 0 to 49
numbers=range(50)

for numbers in numbers:
    print(numbers)

#b)a list containing squares of integers in range 1 to 50.
n=int(input("n="))
squares= [x**2 for x in range(n)]
print(squares)

#c)the list['a','bb','ccc',....] that ends with 26 copies of letter z.
L=[]
for i in range(1, 27):
    L.append(chr(96 + i) * i)
print(L)





