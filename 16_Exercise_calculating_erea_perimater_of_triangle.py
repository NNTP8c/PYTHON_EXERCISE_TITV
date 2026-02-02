#
# Created on Tue Jan 27 2026
#
# Copyright (c) 2026 Your Company
#
# Lession 16: Exercise calculating perimeter and area of a triangle - Bài tập tính chu vi và diện tích của tam giác
#
# Yêu cầu bài:
# 1. Nhập vào tọa độ 3 điểm
# 2. Xác định 3 điểm nhập vào có là tam giác không
# 3. Tính chu vi và diện tích nếu là tam giác

# Library declaration - Khai báo thư viện
import math

# Enter data
xa = float(input('Nhập vào tọa độ diểm xA: '))
ya = float(input('Nhập vào tọa độ điểm yA: '))
xb = float(input('Nhập vào tọa độ điểm xB: '))
yb = float(input('Nhập vào tọa độ điểm yB: '))
xc = float(input('Nhập vào tọa độ điểm xC: '))
yc = float(input('Nhập vào tọa độ điểm yC: '))

# Processing
# Calculating the three side length of triangle
ab = math.sqrt((xb-xa)**2 + (yb-ya)**2)
ac = math.sqrt((xc-xa)**2 + (yc-ya)**2)
bc = math.sqrt((xc-xb)**2 + (yc-yb)**2)

# Determine if it a triangle
if (ab < ac+bc) and (ac < ab+bc) and (bc < ab+ac):
    # Kiểm tra có trùng điểm không
    if (ab == 0 or ac == 0 or bc == 0):
        # Calculation perimeter the triangle
        pe = ab + ac + bc
        print('Perimeter is ', pe)
        # Calculation area the triangle
        p = pe/2
        s = math.sqrt(p*(p-ab)*(p-ac)*(p-bc))
        print('Area is ', s)
    else:
        print('Not a triangle')
else:
    print('Not is triangle')