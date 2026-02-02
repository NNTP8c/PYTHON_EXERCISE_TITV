#
# Created on Mon Feb 02 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 34: Try Exception

try:
    n = int(input('Nhập số nguyên dương: '))
    print(str(n) + ' + 5 = ',n+5)
except:
    print('Nhập liệu không đúng')
else:
    print('Cộng thành công')
finally:
    print('Kết thúc')

try:
    n = int(input('Nhập số nguyên dương: '))
    print(str(n) + ' + 5 = ',n+5)
except Exception as e:
    print(e)
else:
    print('Cộng thành công')
finally:
    print('Kết thúc')