import math

# Class for representing 2D Vector
class Vector2D:
    def __init__(self, x, y):
        """Initialize 2D vector with x and y components."""
        self.x = x
        self.y = y

    def magnitude(self):
        """Calculate the magnitude of the 2D vector."""
        return math.sqrt(self.x**2 + self.y**2)

    def rotation(self):
        """Calculate the angle of the vector with respect to the X-axis (in degrees)."""
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        """Calculate the distance between two 2D vectors."""
        if isinstance(other, Vector2D):
            return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        else:
            raise TypeError("The other object must be an instance of Vector2D")

    def dot_product(self, other):
        """Calculate the dot product of two 2D vectors."""
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("The other object must be an instance of Vector2D")

    def cross_product(self, other):
        """Calculate the cross product of two 2D vectors (result is a scalar)."""
        if isinstance(other, Vector2D):
            return self.x * other.y - self.y * other.x
        else:
            raise TypeError("The other object must be an instance of Vector2D")

    def display(self):
        """Display the 2D vector components."""
        print(f"Vector: ({self.x}, {self.y})")


# Class for representing 3D Vector (Inherits from Vector2D)
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        """Initialize 3D vector with x, y, and z components."""
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        """Override magnitude method for 3D vector."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def rotation(self):
        """Override rotation method for 3D vector (angle in XY plane)."""
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        """Override distance method for 3D vector."""
        if isinstance(other, Vector3D):
            return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
        else:
            raise TypeError("The other object must be an instance of Vector3D")

    def dot_product(self, other):
        """Override dot product method for 3D vector."""
        if isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("The other object must be an instance of Vector3D")

    def cross_product(self, other):
        """Override cross product method for 3D vector."""
        if isinstance(other, Vector3D):
            cx = self.y * other.z - self.z * other.y
            cy = self.z * other.x - self.x * other.z
            cz = self.x * other.y - self.y * other.x
            return Vector3D(cx, cy, cz)
        else:
            raise TypeError("The other object must be an instance of Vector3D")

    def display(self):
        """Override display method for 3D vector."""
        print(f"Vector: ({self.x}, {self.y}, {self.z})")


# Driver Code
if __name__ == "__main__":
    # User input for 2D vector
    x2d = float(input("Enter the x-component of the 2D vector: "))
    y2d = float(input("Enter the y-component of the 2D vector: "))

    vector2d = Vector2D(x2d, y2d)

    # User input for another 2D vector
    x2d_2 = float(input("Enter the x-component of the second 2D vector: "))
    y2d_2 = float(input("Enter the y-component of the second 2D vector: "))
    
    vector2d_2 = Vector2D(x2d_2, y2d_2)

    # Display the vector and calculate distance, dot product, and cross product for 2D
    print("\nFirst 2D Vector:")
    vector2d.display()
    print(f"Magnitude: {vector2d.magnitude()}")
    print(f"Rotation (with respect to X-axis): {vector2d.rotation()} degrees")
    
    print("\nSecond 2D Vector:")
    vector2d_2.display()
    print(f"Magnitude: {vector2d_2.magnitude()}")
    print(f"Rotation (with respect to X-axis): {vector2d_2.rotation()} degrees")

    print(f"\nDistance between the two 2D vectors: {vector2d.distance(vector2d_2)}")
    print(f"Dot Product of the two 2D vectors: {vector2d.dot_product(vector2d_2)}")
    print(f"Cross Product of the two 2D vectors: {vector2d.cross_product(vector2d_2)}")

    # User input for 3D vector
    x3d = float(input("\nEnter the x-component of the 3D vector: "))
    y3d = float(input("Enter the y-component of the 3D vector: "))
    z3d = float(input("Enter the z-component of the 3D vector: "))

    vector3d = Vector3D(x3d, y3d, z3d)

    # User input for another 3D vector
    x3d_2 = float(input("Enter the x-component of the second 3D vector: "))
    y3d_2 = float(input("Enter the y-component of the second 3D vector: "))
    z3d_2 = float(input("Enter the z-component of the second 3D vector: "))
    
    vector3d_2 = Vector3D(x3d_2, y3d_2, z3d_2)

    # Display the vector and calculate distance, dot product, and cross product for 3D
    print("\nFirst 3D Vector:")
    vector3d.display()
    print(f"Magnitude: {vector3d.magnitude()}")
    print(f"Rotation (in XY plane, with respect to X-axis): {vector3d.rotation()} degrees")
    
    print("\nSecond 3D Vector:")
    vector3d_2.display()
    print(f"Magnitude: {vector3d_2.magnitude()}")
    print(f"Rotation (in XY plane, with respect to X-axis): {vector3d_2.rotation()} degrees")

    print(f"\nDistance between the two 3D vectors: {vector3d.distance(vector3d_2)}")
    print(f"Dot Product of the two 3D vectors: {vector3d.dot_product(vector3d_2)}")
    
    cross_product_result = vector3d.cross_product(vector3d_2)
    print(f"Cross Product of the two 3D vectors: ({cross_product_result.x}, {cross_product_result.y}, {cross_product_result.z})")
