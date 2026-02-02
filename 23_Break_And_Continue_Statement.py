#
# Created on Wed Jan 28 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 23: Break and Continue statement - Câu lệnh break và continue

# Break
for i in range(10):
    if (i>4):
        break
    print(i)
   
print('Chia lấy nguyên')
n=100
while (n>0):
    print(n)
    n = n // 2
    if (n<30):
        break

print('Bảng cửu chương:')
for i in range(1,10):
    for j in range(1,11):
        if (j>3):
            break
        print('{0} * {1} = {2}'.format(i, j, i*j))
    print('\n')

# Continue
for i in range(10):
    if(i%2!=0):
        continue
    print(i)