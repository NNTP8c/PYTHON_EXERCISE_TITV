#
# Created on Sat Jan 31 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 32: Object oriented exercise - Bài tập về hướng đối tượng

# Create simple class - Tạo class đơn giản
class simpleClass:

    # attribute - Thuộc tính
    i=1 # Class attribute - Thuộc tính lớp
    def __init__(self):
        self.j=4    # instance attribute - Thuộc tính thể hiện

    # Method - Phương thức
    def printself(self):
        print(self.j)
    

objectA = simpleClass()
objectB = simpleClass()
objectA.printself()
print(objectB.i)

objectA.i = 100
print(objectA.i)
objectB.j = 400
objectB.printself()

class simpleClass2():
    def __init__(self):
        self.name = 'Hao'
    # method
    def hello(self):
        print('Hello ' + self.name)
    # static method
    @staticmethod
    def hi(name):
        print('hi ' + name)

objectC = simpleClass2()
objectD = simpleClass2()
objectC.hello()
objectD.hi('peter')
# flase simpleClass2.hi('Hao')
simpleClass2.hi('peter')

class date():
    # constructor - hàm khởi tạo
    def __init__(self,value_day,value_month,value_year):
        self.day = value_day
        self.month = value_month
        self.year = value_year
    @staticmethod
    def the_number_of_days(month,year):
        if (month in [1,3,5,7,8,10,12]):
            return 31
        elif (month in [4,6,9,11]):
            return 30
        elif (month == 2):
            if (year%400==0 or (year%4==0 and year%100!=0)):
                return 29
            else:
                return 28
    def the_number_of_year(self):
        thenumberofyear = 0
        for x in range(1,self.month):
            if (x>0):
                thenumberofyear += self.the_number_of_days(x,self.year)
        thenumberofyear += self.day
        return thenumberofyear

date1 = date(1,2,2026)
print(date1.the_number_of_year())