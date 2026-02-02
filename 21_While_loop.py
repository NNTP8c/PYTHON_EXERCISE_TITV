#
# Created on Wed Jan 28 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 21: While loop - Vòng lập while

n = -1
while (n<=0):
    n = int(input('Nhập n: '))
    
tong = 0
j = 0
while (j<=n):
    tong += j
    j+=1
print(tong)

j = 0
while (j<=10):
    print(j, 'Bên trong vòng lập')
    j += 1
    if (j>=3):
        break
else:
    print(j, 'Bên ngoài vòng lập')