# Class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f'Xin chào, tôi là {self.name}, tôi {self.age} tuổi'
    
person1 = Person('Aclice', 30)
person2 = Person('Bod', 25)
print('Lớp Person')
print(person1.introduce())
print(person2.introduce())
print('\n')

# Class Student
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def is_passed(self):
        if self.score >=5:
            return f'{self.name} đã đậu'
        else:
            return f'{self.name} đã rớt'
        
# Create student objects and test the is passed mothod - - Tạo đối tượng student và kiểm tra phương thức is_passed
student1 = Student('Peter', 8)
student2 = Student('Mary', 4)
print('Lớp Student')
print(student1.is_passed())
print(student2.is_passed())
print('\n')

class Emloyee:
    company_name = 'ABC Company'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_info(self):
        return f'{self.name} làm việc tại {Emloyee.company_name} với mức lương {self.salary}'
    
# Creat emloyee objects and test the get_info method - Tạo đối tượng employee và kiểm tra phương thức get_info
employee1 = Emloyee('John', 5000)
employee2 = Emloyee('Jane', 6000)
print('Lớp Employee')
print(employee1.get_info())
print(employee2.get_info())
Emloyee.company_name = 'XYZ Company'
print(employee1.get_info())
print(employee2.get_info())
print('\n')

# Create a class BankAccount with private attribute balance and methods to deposit, withdraw and check balance - Tạo lớp BankAccount với thuộc tính balance riêng tư và các phương thức để nạp tiền, rút tiền và kiểm tra số dư
class BankAccount:
    def __init__(self, initial_balance = 0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f'Bạn đã nạp {amount} vào tài khoản. Số dư hiện tại: {self.__balance}'
        else:
            return 'Số tiền nạp phải lớn hơn 0'
    
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                return f'Bạn đã rút {amount} từ tài khoản. Số dư hiện tại: {self.__balance}'
            else:
                return 'Số dư không đủ để rút'
        else:
            return 'Số tiền rút phải lớn hơn 0'
    
    def get_balance(self):
        return f'Số dư hiện tại của bạn là: {self.__balance}'
    
acconut1 = BankAccount()
print('Lớp BankAccount')
print(acconut1.deposit(1000))
print(acconut1.withdraw(400))
print(acconut1.get_balance())


