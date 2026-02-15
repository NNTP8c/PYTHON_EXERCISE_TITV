from collections import Counter
# Filter even/odd in the list
listInt = [1,67,4,8,9,4,2,3,6,3,23,543,234,563,4]
even = [number for number in listInt if number%2==0]
odd = [number for number in listInt if number%2!=0]
# for number in listInt:
#     if number%2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)
print(f'Danh sách số nguyên: {listInt}')
print(f'Danh sách số chẵn: {even}')
print(f'Danh sách các số lẻ: {odd}')

# Calcution total elements in list
total = sum(listInt)
print(f'Tổng các phần tử trong listInt: {total}')

# calcution average elements in list
average = float(total/len(listInt))
print(f'Trung bình cộng các phần tử trong: {average}')

# Delete duplicate element in list
listInt = list(set(listInt))
print(f'Danh sách sau khi xóa các phần tử trùng: {listInt}')

# Sort descenting element in list
listInt.sort(reverse=True)
print(f'Danh sách sau khi sắp xếp giảm dần: {listInt}')

# common elements in 2 list
list2 = [1,2,3,4,5,5,6,7,8,9,10]
common_elements =  list(set(listInt) & set(list2))
print(f'Danh sách có các phần tử trùng nhau của hai list: {common_elements}')

# Creat even lits by list comprehension
list3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
evenList = [value for value in list3 if value%2==0]
print(f'Danh sách số chẵn tạo từ list comprehention: {evenList}')

# 2d list
lits_2d = [listInt,list2,evenList,even,odd]
total_2d = sum([sum(row) for row in lits_2d])
print(f'Tổng của danh sách hai chiều là: {total_2d}')