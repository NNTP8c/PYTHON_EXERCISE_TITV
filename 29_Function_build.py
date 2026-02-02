#
# Created on Fri Jan 30 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 29: Function build - Xây dựng function

def student(name,age):
    print('Name: {0}, Age: {1}'.format(name,age))
student('Jhon',23)

def timeTable(*subject):
    print('Subject 1: ' + subject[0])
    print('Subject 2: ' + subject[1])
timeTable('Math','Chemistry','literature')

def totalcalculation(*total):
    sum = 0
    for x in total:
        sum += x
    print(sum)
totalcalculation(1,2,3)

def name(**fullname):
    print('Fullname: '+ fullname['firtname'] + ' ' + fullname['lastname'])
name(firtname='Nguyễn', lastname='Phú')

def product (*value):
    result = 1
    for x in value:
        result *= x
    return result
product1 = product(2,3)
product2 = product(2,2)
print(product1+product2)

def ucln(a,b):
    while (a != b):
        if (a>b):
            a -= b
        else:
            b -= a
    return a
print('Ước chung lớn nhất: ', ucln(12,17))


n = -1
number_list = []

while (n<1):
    n = int(input('Nhập n: '))

def enter(n,number_list):
    for x in range(n):
        value = int(input('Nhập giá trị vào vị trí ' + str(x) + ' : '))
        number_list.append(value)
    
def total(number_list):
    sum = 0
    for x in number_list:
        sum += x
    return sum

enter(n, number_list)
print('Tổng: ', total(number_list))