class Employee:
    company_name = 'TechCrop'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        return f'Tên: {self.name}, Lương: {self.salary}, Công ty: {Employee.company_name}'
    
emp1 = Employee('Alice', 5000)
emp2 = Employee('Bob', 6000)    
emp3 = Employee('Charlie', 5500)
print(emp1.display_info())
print(emp2.display_info())
print(emp3.display_info())
Employee.company_name = 'InvoTech'
print(emp1.display_info())
print(emp2.display_info())
print(emp3.display_info())
