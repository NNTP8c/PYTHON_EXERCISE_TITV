#
# Created on Wed Jan 28 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 22: Convert decimal to binary - Chuyển đổi thập phân sang nhị phân

# Enter a positive integer - Nhập số nguyên dương
n = -1
while (n<=0):
    n = int(input('Nhập n: '))

# Convert decimal to binary - Chuyển thập phân sang nhị phân
result = ''
while (n>0):
    result = str(n%2) + result
    print('n // 2 = ', n//2)
    print('n % 2 = ', n%2)
    n = n//2
print(result)