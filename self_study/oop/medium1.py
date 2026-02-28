from abc import ABC, abstractmethod

class Animal:
    def speak(self):
        print('Tiếng động vật')
class Dog(Animal):
    def speak(self):
        print('Gâu gâu')
class Cat(Animal):
    def speak(self):
        print('Meo meo')

if __name__ == '__main__':
    print('*Lớp Animal*')
    a1 = Animal()
    dg = Dog()
    ct = Cat()
    a1.speak()
    dg.speak()
    ct.speak()
    print('\n')

# Super()
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print(f'Hãng {self.brand} bắt đầu khởi động')
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def start(self):
        super().start()
        print(f'Mẫu xe {self.model} đã sẵn sàng ra mắt')

if __name__ == '__main__':
    print('*Lớp Vehicle và Car*')
    toyota = Car('Toyota', 'Corolla')
    toyota.start()
    print('\n')

# Polymorphism
def make_sound(animals):
    animals.speak()
if __name__ == '__main__':
    print('*Đa hình*')
    make_sound(dg)
    make_sound(ct)
    print('\n')

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width =  width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
if __name__ == '__main__':
    print('*Lớp Shape, Rectangle và Circle*')
    rectangle = Rectangle(5,4)
    circle = Circle(3)
    print(f'Diện tích hình chữ nhật: {rectangle.area()}')
    print(f'Diện tích hình tròn: {circle.area()}')