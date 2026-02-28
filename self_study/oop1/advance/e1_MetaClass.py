class MyMeta(type):
    def __new__(cls, name, bases, dct):
        if 'run' not in dct:
            raise TypeError(f'{name} phải có phương thức run')
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass = MyMeta):
    def run(self):
        return 'Chạy phương thức'
    
try:
    class NoRun(metaclass = MyMeta):
        pass
except TypeError as e:
    print(e)

mycls = MyClass()
print(mycls.run())