# Magic methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f'Vector({self.x}, {self.y})'
    
if __name__ == '__main__':
    print('*Lớp Vector với toán tử cộng*')
    v1 = Vector(2,3)
    v2 = Vector(4,5)
    v3 = v1 + v2
    print(f'{v3}\n')

# Composition
class Engine:
    def start(self):
        print('Động cơ đã khởi động!')
class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        self.engine.start()

if __name__ == '__main__':
    car = Car()
    car.start()