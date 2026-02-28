class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print('Gâu gâu')

class Cat(Animal):
    def speak(self):
        print('Meo meo')

cat = Cat()
cat.speak()
dog = Dog()
dog.speak()
