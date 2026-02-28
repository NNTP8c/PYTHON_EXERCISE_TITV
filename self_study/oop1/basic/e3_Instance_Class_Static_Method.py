import math
from math import sqrt
class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def add(self):
        return self.number1 + self.number2
    
    @classmethod
    def create_object(cls, string):
        number1, number2 = map(int, string.split(','))
        return cls(number1, number2)
    
    @staticmethod
    def check_prime(number):
        if number > 1:
            for i in range(2, int(sqrt(number)) + 1):
                if number % i ==0:
                    return f'{number} không phải là số nguyên tố'
            return f'{number} là số nguyên tố'
        else:
            return f'{number} không phải là số nguyên tố'
        
cal1 = Calculator(10, 20)
print(cal1.add())
cal2 = Calculator.create_object('30,10')
print(cal2.add())
print(Calculator.check_prime(21))