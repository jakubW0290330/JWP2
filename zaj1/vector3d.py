import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def dlugosc(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def przesun(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
    
    def setZ(self, z):
        self.z = z

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    
    
    def dot(self, vector1):
        return (self.x - vector1.x) + (self.y + vector1.y) + (self.z - vector1.z)

    def cross(self, vector1):
        return Vector3D((self.y*vector1.z)-(self.z*vector1.y), 
                        (self.z*vector1.x)-(self.x*vector1.z), 
                        (self.x*vector1.y)-(self.y*vector1.x))

    

    @staticmethod
    def odleglosc(punkt1, punkt2):
        return math.sqrt((punkt1.x - punkt2.x) ** 2 + (punkt1.y - punkt2.y) ** 2 + (punkt1.y - punkt2.y) ** 2)

    @staticmethod
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @staticmethod
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y)
    
    @staticmethod
    def __add__(vector1, vector2):
        return vector1 + vector2
    
    @staticmethod
    def __sub__(vector1, vector2):
        return vector1 - vector2
    
    @staticmethod
    def __mul__(vector1, vector2):
        return vector1 * vector2
    
    @staticmethod
    def are_orthogonal(vector1, vector2):
        return True if vector1.dot(vector2) == 0 else False


# Przykłady użycia:
punkt1 = Vector3D(3, 4, 5)
punkt2 = Vector3D(3, 4, 5)
print(Vector3D.are_orthogonal(punkt1,punkt2))  
