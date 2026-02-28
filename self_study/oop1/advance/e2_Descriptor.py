class ScoreDescriptor:
    def __get__(self, instance, owner):
        return instance._score if hasattr(instance, '_score') else None
    
    def __set__(self, instance, value):
        if not 0<= value <=10:
            raise ValueError('Điểm phải từ 0 đến 10')
        instance._score = value
        
    def __delete__(self, instance):
        del instance._score

class Student():
    score = ScoreDescriptor()
    def __init__(self, name):
        self.name = name
        self._score = None
    
student = Student('Fib')
student.score = 8
print(student.score)

try:
    student.score = 11
except ValueError as e:
    print(e)

del student.score
print(student.score)