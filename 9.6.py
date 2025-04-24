import numpy as np
import matplotlib.pyplot as plt


def f(x):

    return x**3 - 4*x**2 + 6*x - 24


def bisection_method(f, a, b, tol=1e-6, max_iter=100):

    if f(a) * f(b) > 0:
        print("Error: f(a) and f(b) must have opposite signs.")
        return None
    
    
    
    midpoints = []


    for i in range(max_iter):

        c = (a + b) / 2
        midpoints.append(c)


        if abs(f(c)) < tol:
            print(f"Root found at c = {c} after {i+1} iterations.")
            break

        if f(a) * f(c) < 0:
            b = c  
        else:
            a = c  
    return np.array(midpoints)

a = 2  
b = 6  

midpoints = bisection_method(f, a, b)


if midpoints is not None:
    
    x_vals = np.linspace(a, b, 400)
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals, label="f(x)", color='b')
    plt.axhline(0, color='black',linewidth=0.5)  
    

    plt.scatter(midpoints, f(midpoints), color='r', label="Midpoints", zorder=5)
    

    plt.scatter(midpoints[-1], f(midpoints[-1]), color='g', label="Approximated Root", zorder=6)


    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Bisection Method for Root Finding")
    plt.legend()
    plt.grid(True)
    plt.show()
