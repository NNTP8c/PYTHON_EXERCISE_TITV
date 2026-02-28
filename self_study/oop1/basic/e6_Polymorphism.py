class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print('Gâu gâu')

class Cat(Animal):
    def speak(self):
        print('Meo meo')

class Duck(Animal):
    def speak(self):
        print('Quack quack')

animal = [Dog(), Cat(), Duck()]
for a in animal:
    a.speak()

