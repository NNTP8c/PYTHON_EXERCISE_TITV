#
# Created on Tue Jan 27 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 18: Loop if - Vòng lập for


n = int(input('Nhập n: '))
for i in range(n):
    print(i)

tong = 0
for i in range(n):
    tong += i
print('Tổng từ o->{0}: '.format(n), tong)

print('In ra các số chẳn dưới 12:')
for i in range(0,12,2):
    print(i)

print('In các số từ 10 đến 1:')
for i in range(10,0,-1):
    print(i)

colors = ['red','green','yellow','orange','bule']
print('In ra danh sách màu:')
for i in range(len(colors)):
    print(colors[i])

for color in colors:
    print(color)