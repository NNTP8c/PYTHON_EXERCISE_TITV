# Find min,max of list
listInt = [1,7,8,5,34,5]
listInt_Min = min(listInt)
listInt_Max = max(listInt)
print(f'Phần tử nhỏ nhất danh sách: {listInt_Min}')
print(f'Phần tử lớn nhất danh sách: {listInt_Max}')

# Check element in list
check = int(input('Nhập phần tử muốn kiểm tra có trong listInt không: '))
if check in listInt:
    print(f'Có {check} trong listInt')
else:
    print(f'Không tìm thấy {check} trong listInt')

# Reverse list
listInt.reverse()
print(f'ListInt sau khi đảo ngược: {listInt}')

# Concatenate 2 list
list2 = [1,34,2.5,'fg','apple']
listInt.extend(list2)
print(f'Nối hai list: {listInt}')

# Count element in list
print(f'5 đã xuất hiện {listInt.count(5)} trong listInt')