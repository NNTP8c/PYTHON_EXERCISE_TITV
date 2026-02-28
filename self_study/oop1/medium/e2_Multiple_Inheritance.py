class Flyable:
    def flyable(self):
        return 'Có thể bay'
    
class Swimable:
    def swimable(self):
        return 'Có thể bơi'
    
class Duck(Flyable, Swimable):
    pass

print(Duck().swimable())
print(Duck().flyable())
print(Duck.mro())