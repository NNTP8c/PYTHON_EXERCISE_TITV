#
# Created on Wed Jan 28 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 24: Data type Tuple - Kiểu dữ liệu tuple

Class = (1,2,3,4,5,6,7,8,9,10,11,12)
fruit = ('apple', 'banana', 'apple', 'watermelon', 'pineapple', 'orange')

# Output Tuple - Xuất Tuple
print(fruit)
print(fruit[1])
print(fruit[2:4])
for x in fruit:
    print(x)

# Add and Multiply tuple - Cộng và nhân Tuple
add = (1,2,3) + (4,5,6)
print(add)
multiply = (1,2,3) * 2
print(multiply)

# Count and calculate length Tuple - Đếm và tính độ dài Tuple
print('Đếm số lượng từ apple: ', fruit.count('apple'))
print('Đếm độ dài của tuple fruit: ', len(fruit))

# Arrange Tuple - Sắp xếp tuple
print('Sort tuple: ', sorted(fruit))
print('Sort tuple: ', sorted(fruit, reverse = True))

# Find object in tuple - Tìm đối tượng trong tuple
print('watermelon' in fruit)
print('Cherry' in fruit)

# Min, Max, Sum
print('Nhỏ nhất trong fruit', min(fruit))
print('Lớn nhất trong Class:', max(Class))
print('Total Class: ', sum(Class))

