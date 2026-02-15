# Create and print list
list1 =[1,45,9,6,3]
print(f'In tất cả phần tử: {list1}')

# print first element,last element,position 3
print(f'In phần tử ở vị trí đầu: {list1[0]}')
print(f'In phần tử ở vị trí cuối cùng: {list1[len(list1)-1]}')
print(f'In phần tử ở vị trí thứ 3: {list1[2]}')

# Create empty list and add 5 elements to lits
emptyList = []
emptyList.append(1)
emptyList.append(65)
emptyList.append('chào')
emptyList.append('apple')
emptyList.append(34.6)

# Delete element first in list
print(f'In danh sách trống trước khi xóa đầu: {emptyList}')
del emptyList[0]
print(f'In danh sách trống sau khi xóa đầu: {emptyList}')
del emptyList[len(emptyList)-1]
print(f'In danh sách trống sau khi xóa vị trí cuối: {emptyList}')

# sort list
list1_sorted = sorted(list1)
print(f'Sắp xếp list1 tăng dần {list1_sorted}')

# Print length of list
len_emptyList = len(emptyList)
print(f'Đọ dài list emptyList: {len_emptyList}')

