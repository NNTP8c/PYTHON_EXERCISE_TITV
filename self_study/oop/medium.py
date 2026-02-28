# OOP - Medium
from abc import ABC, abstractmethod
# Create a base class called "Animal" with a method "speak" that returns a generic sound - Tạo một lớp cơ sở có tên "Animal" với một phương thức "speak" trả về một âm thanh chung.
# Then, create two subclasses "Dog" and "Cat" that inherit from the "Animal" class and override the "speak" method to return specific sounds for each animal - Sau đó, tạo hai lớp con "Dog" và "Cat" kế thừa từ lớp "Animal" và ghi đè phương thức "speak" để trả về âm thanh cụ thể cho mỗi loài động vật.
# Finally, create instances of each class and call their "speak" methods to see the output - Cuối cùng, tạo các instance của mỗi lớp và gọi phương thức "speak" của chúng để xem kết quả.
class Animal:
    def speak(self):
        return 'Animal makes a sound'
    
class Dog(Animal):
    def speak(self):
        return 'Chó sủa: Gâu gâu'
    
class Cat(Animal):
    def speak(self):
        return 'Mèo kêu: Meo meo'
    
if __name__ == '__main__':
    animal = Animal()
    dog = Dog()
    cat = Cat()
    print('*Lớp Animal*')
    print(animal.speak())
    print(dog.speak())
    print(cat.speak())
    print('\n')

# Create a base class called "Vehicle" with a method "start" that prints a message indicating the vehicle is starting - Tạo một lớp cơ sở có tên "Vehicle" với một phương thức "start" in ra một thông điệp cho biết phương tiện đang khởi động.
# Then, create a subclass "Car" that inherits from the "Vehicle" class and overrides

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print(f'Hãng {self.brand} đang bắt đầu khởi động')
    
class Car(Vehicle):
    def __init__(self,brand, model):
        super().__init__(brand)
        self.model = model
    def start(self):
        super().start()
        print (f'Mẫu xe {self.model} đã sẵn sàn ra mắt')

if __name__ == '__main__':
    print('*Lớp Vehicle và Car*')
    toyota = Car('Toyota', 'Corolla')
    toyota.start()
    print('\n')

# Polymorphism
def make_sound(animals):
    print(animals.speak())

if __name__ == '__main__':
    print('*Đa hình*')
    make_sound(dog)
    make_sound(cat)
    print('\n')

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Retangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
if __name__ == '__main__':
    print('*Lớp Shape, Retangle và Circle*')
    rectangle = Retangle(5, 3)
    circle = Circle(4)
    print(f'Diện tích hình chữ nhật là: {rectangle.area()}')
    print(f'Diện tích hình tròn là: {circle.area()}')
    print('\n')