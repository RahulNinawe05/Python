class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other): # this is _ the problem __
        return Vector(self.x + other.x , self.y + other.y , self.z + other.z) # Return a new Vector instance
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z     # Dot product
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v2)  # Vector addition
print(v1 * v2)  # Dot product

print(v1 + v3)  # Vector addition
print(v1 * v3)  # Dot product

