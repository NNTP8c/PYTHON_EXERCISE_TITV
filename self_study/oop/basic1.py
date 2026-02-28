# OOP - Object Oriented Programming - Lập trình hướng đối tượng
# 1. Class and Object - Lớp và đối tượng
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'Tôi tên là {self.name}, tôi {self.age} tuổi')
print('Lớp Person')
p1 = Person('john', 20)
p1.introduce()
print('\n')

# Create a class Person with attributes name and age, and a method introduce that returns a string introducing the person - Tạo lớp Person với thuộc tính name và age, và phương thức introduce trả về một chuỗi giới thiệu về người đó
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def is_passed(self):
        if self.score>=5:
            print(f'{self.name} đã đậu')
        else:
            print(f'{self.name} đã rớt')
print('Lớp Student')
st1 = Student('Emily', 8)
st2 = Student('David', 4)
st1.is_passed()
st2.is_passed()
print('\n')

# Create a class Employee with attributes name and salary, and a method get_info that returns a string with the employee's information - Tạo lớp Employee với thuộc tính name và salary, và phương thức get_info trả về một chuỗi với thông tin của nhân viên
class Emloyee:
    company_name = 'ABC Company'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_info(self):
        print(f'{self.name} làm việc tại {Emloyee.company_name} với mức lương {self.salary}')
print('Lớp Employee')
e1 = Emloyee('Oscar', 5000)
e1.get_info()
e2 = Emloyee('Sophia', 6000)
Emloyee.company_name = 'XYZ Company'
e2.get_info()
print('\n')

class BankAccount:
    def __init__(self, balance = 0):
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Bạn đã nạp {amount} vào tài khoản. Số dư hiện tại: {self.__balance}')
        else:
            print('Số tiền cần nạp phải lớn hơn 0')
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f'Bạn vừa rút {amount} từ tài khoản. Số dư hiện tại: {self.__balance}')
            else:
                print('Số dư không đủ để rút')
        else:
            print('Số tiền cần rút phải lớn hơn 0')
    def get_balance(self):
        print(f'Số dư hiện tại của bạn là: {self.__balance}')
print('Lớp BankAccount')
ba1 = BankAccount()
ba1.deposit(1000)
ba1.withdraw(600)
ba1.withdraw(500)
ba1.get_balance()
print('\n')