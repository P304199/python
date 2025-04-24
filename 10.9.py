import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 6*x**2 + 11*x - 6  # Example polynomial

def bisection_method(f, a, b, tol=1e-5, max_iter=100):
    updates = []
    if f(a) * f(b) > 0:
        print("The bisection method cannot be applied.")
        return None
    
    for i in range(max_iter):
        c = (a + b) / 2
        updates.append(c)
        
        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return np.array(updates)

a, b = 1, 3  # Example interval where the root is expected
updates = bisection_method(f, a, b)

plt.plot(updates, f(updates), marker='o', linestyle='-', color='b')
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.title("Root Finding Process Using Bisection Method")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
