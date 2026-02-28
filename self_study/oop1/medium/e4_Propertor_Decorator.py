class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value > 10:
            self._age = value
        else:
            print('Tuổi phải lớn hơn 10')
        
p = Person(12)
print(p.age)
p.age = 13
print(p.age)