#
# Created on Mon Jan 26 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 06: Variables, Constant and Keywords - Biến, hằng số và từ khóa

x = 1
print(x)

y = 10
y = 12
print(y)

x, y, z = 1, 2, 'Variables'
print(x, y, z)
print(x, y, end = ': ')
print(z)

PI = 3.14
print(PI)

PI = 3.1415
print(PI)

import math
print(math.pi)

fullName = input('Enter Full Name: ')
age = input('Enter age: ')
print('FullName: {0}, Age: {1}'.format(fullName,age))