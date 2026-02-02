#
# Created on Tue Jan 27 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 13: Conditional Operator - Toán tử điều kiện

import math

a = int(input('a: '))
b = int(input('b: '))
print('{0} là số chẵn'.format(a)) if(a%2==0) else print('{0} là số lẻ'.format(a))
print('{0} và {1} là các số nguyên tô cùng nhau'.format(a, b)) if (math.gcd(a,b) == 1) else print('{0} và {1} không là các số nguyên tố cùng nhau'.format(a, b))
