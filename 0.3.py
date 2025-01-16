#program to swap two variables without using third variable
a = int(input(" a: ")) #inputs
b = int(input(" b: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)