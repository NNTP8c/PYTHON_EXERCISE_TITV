#
# Created on Tue Jan 27 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 14: If else statement - Câu lệnh if else

a = float(input('Nhập a: '))

# For example 1
if a>0:
    print(a, 'là số dương')
else:
    print(a, 'là số âm')

# For example 2:
if a>=9:
    print('Xếp loại: Xuất sắc')
elif a>=8:
    print('Xếp loại: Giỏi')
elif a>=7:
    print('Xếp loại: Khá')
elif a>=5:
    print('Xếp loại: Trung bình')
elif a>=3:
    print('Xếp loại: Yếu')
else:
    print('Không xếp loại')
