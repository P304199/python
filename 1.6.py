#finding the nearest neighbour
import math

def distance(point_1, point_2):
    return math.sqrt(
        (point_1[0] - point_2[0])**2 +
        (point_1[1] - point_2[1])**2 +
        (point_1[2] - point_2[2])**2
    )

points = []
for i in range(10):
    x = float(input(f"Enter x coordinate  {i + 1}: "))
    y = float(input(f"Enter y coordinate  {i + 1}: "))
    z = float(input(f"Enter z coordinate  {i + 1}: "))
    points.append((x, y, z))
    # storing points as a tuple in list

for i in range(10):
    point = points[i]
    min_dist = float('inf')
    nearest_point = None 
    for j in range(10):
        if i != j:
            other_point = points[j]
            dist = distance(point, other_point)
            if dist < min_dist:
                min_dist = dist
                nearest_point = other_point

    print(f"Nearest neighbour of point {point} is {nearest_point}")


