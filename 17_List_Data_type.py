#
# Created on Tue Jan 27 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 17: List data type - Kiểu dữ liệu danh sách

# List declaration
emptyList = []
empty_List = emptyList
print(empty_List)

# Colors list
colorsList = ['red', 'yellow', 'green', 'orange']
print('Danh sách màu: ', colorsList)
print('Danh sách ở vị trí thứ 1: ', colorsList[1])

# Student list
studentsList = ['An', 'Bình', 'Nhật', 'Cường']
print('Danh sách sinh viên từ 2 đến 3: ', studentsList[2:3])
print('Danh sách sinh viên từ 0 đến 3: ', studentsList[0:3])

# Add to the end of list - Thêm vào cuối danh sách
studentsList.append('Thành')
print('Thêm "Thành" vào danh sách sinh viên: ', studentsList)
studentsList[len(studentsList):] = ['Lam']
print('Danh sách sinh viên từ 1 đến 3: ', studentsList[1:3])
# Add to any position of list - Thêm vào vị trí bất kỳ của danh sách
studentsList.insert(3, 'Long')
print('Thêm "Long" vào vị trí thứ 3: ', studentsList)

# Find the length of the list - Tìm độ dài của danh sách
print('Độ dài của danh sách: ', len(studentsList))

# Count element of the list - Đếm số lượng phần tử của danh sách
studentsList[len(studentsList):] = ['Thành']
print('Thành: ', studentsList.count('Thành'))
print('Nhật: ', studentsList.count('Nhật'))

# Remove element in the list - Xóa phần tử trong danh sách
if 'Thành' in studentsList:
    studentsList.remove('Thành')
    print(studentsList)
    print(len(studentsList))
# Remove element by position in the list - Xóa phần tử theo vị trí
print(studentsList)
studentsList.pop(1)
print(studentsList)

 # Increasing arrange element in the list - Sắp xếp tăng dần các element trong danh sách
print(studentsList)
studentsList.sort()
print(studentsList)

# Reverse the list - Đảo ngược danh sách
studentsList.reverse()
print(studentsList)

# Descreasing arrange element in the list - Sắp xếp giảm các phần tử trong danh sách
numbersList = [8,6,9,3,5,12,5]
numbersList.sort(reverse = True)
studentsList.sort(reverse = True)
print(numbersList)
print(studentsList)

# Clear list - Xóa sạch danh sách
studentsList.clear()
print(studentsList)