import numpy as np

def cartesian_to_polar(cartesian_points):

    x = cartesian_points[:, 0]
    y = cartesian_points[:, 1]
    
    r = np.sqrt(x**2 + y**2)  
    theta = np.arctan2(y, x)


    polar_points = np.column_stack((r, theta))
    return polar_points


N = 10  
cartesian_points = np.random.rand(N, 2) * 10  

print("Cartesian Coordinates (x, y):")
print(cartesian_points)


polar_points = cartesian_to_polar(cartesian_points)

print("\nPolar Coordinates (r, theta):")
print(polar_points)
