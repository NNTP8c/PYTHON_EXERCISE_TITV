#
# Created on Mon Jan 26 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 09: Basic mathematical operations in python - Các phép toán cơ bản trong python

a = input('Nhập số a: ')
print('Kiểu dữ liệu của a: ', type(a))
a = float(a)
print('Kiểu dữ liệu của a: ', type(a))

b = input('Nhập số b: ')
print('Kiểu dữ liệu của b: ', type(b))
b = float(b)
print('Kiểu dữ liệu của b: ', type(b))

print('{0} + {1} = {2}'.format(a, b, a+b))
print('{0} - {1} = {2}'.format(a, b, a-b))
print('{0} * {1} = {2}'.format(a, b, a*b))
print('{0} / {1} = {2}'.format(a, b, a/b))
print('{0} % {1} = {2}'.format(a, b, a%b))
print('{0} ** {1} = {2}'.format(a, b, a**b))
print('{0} // {1} = {2}'.format(a, b, a//b))