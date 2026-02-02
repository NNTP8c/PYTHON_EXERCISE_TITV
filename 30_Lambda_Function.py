#
# Created on Sat Jan 31 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 30: Lambda function

def even(a):
    if (a%2==0):
        return 'Chẵn'
    else:
        return 'Lẻ'
print(even(5))
odd = lambda a : a%2!=0
print(odd(4))

def total(a,b):
    return a+b
print(total(5,5))
total = lambda a,b : a+b
print(total(4,8))

def exponent(a):
    return lambda b : b**a
print((exponent(3))(2))