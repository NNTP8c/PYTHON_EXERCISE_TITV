#
# Created on Tue Jan 27 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 15: Exercise on solving quadratic equation - Bài tập giải phương trình bậc 2

# Declaration Library - Khai báo thư viện
import math

# Enter data
print('Solving quadratic equation: ax² + bx + c = 0')
a = float(input('Nhập a: '))
b = float(input('Nhập b: '))
c = float(input('Nhập c: '))
print('{0}x² + {1}x + {2} = 0'.format(a, b, c))

# Processing - Print
delta = b**2 - 4*a*c
if (a!=0):
    if (delta<0):
        print('Phương trình vô nghiệm')
    elif (delta == 0):
        x = -b / (2*a)
        print('Phương trình có 2 nghiệm kép x1 = x2 = {0}'.format(x))
    else:
        x1 = (-b - math.sqrt(delta))/ (2*a)
        x2 = (-b + math.sqrt(delta))/ (2*a)
        print('Phương trình có 2 nghiệm phân biệt: x1 = {0}, x2 = {1}'.format(x1, x2))
else:
    print('Phương trình không đúng')