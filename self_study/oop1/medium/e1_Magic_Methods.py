class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return 'Chưa cộng được 2 Vector'
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return 'Chưa so sánh hai Vector'
    
    def __str__(self):
        return f'Vector({self.x}, {self.y})'

v1 = Vector(2,3)
v2 = Vector(1,5)
print(v1 + v2)
print(v1 == v2)
print(v2 == (v1+v2))