from itertools import *
# Find Symmetric difference - Đồng dư
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
symmetric_difference = set1 ^ set2
print(set1)
print(set2)
print(f'Đồng dư của set1 và set2 là: {symmetric_difference}')

# Create set from 1 to 1000000 and print elements not 3 divisible
set3 = set()
for n in range (1,1001):
    set3.add(n)
print(set3)
set_not_divisible_3 = [item for item in set3 if item%3!=0]
print(set_not_divisible_3)

# Function enter 2 list and create set contain element difference
list1 = [1,5,8,9]
list2 = [1,5,7,6]
def set_difference(list1,list2):
    set_diff = set(list1).difference(list2)
    return set_diff
print(f'list1: {list1}')
print(f'list2: {list2}')
print(f'Có trong list1 nhưng không có trong list2: {set_difference(list1,list2)}')

# Remove duplicate in list has many tuple
list_tuple = [(1, 'a'), (2, 'b'), (3, 'c'), (1, 'a'), (2, 'b')]
list_tuple = set(list_tuple)
print(f'Danh sách tuple sau khi xóa trùng chuyển thành set: {list_tuple}')

# Cartesian Product - Tích cartesian
set4 = {1,2}
set5 = {'a','b'}
set6 = set(product(set4,set5))
print(f'set4: {set4}')
print(f'set5: {set5}')
print(f'Nhân cartesian set4 và set5: {set6}')

# Function check string duplicate
def check_string_duplicate(text):
    works = text.split()
    seen = set()
    for work in works:
        if work in works:
            return True
        seen.add(work)
    return False
text = 'Xin chào con bò con'
if check_string_duplicate(text):
    print(f'{text}: có từ trùng')
else:
    print(f'{text}: không có từ trùng')

# Function create set divisible by 2 or 3 from list
def set_divisible_by_2_3(list_enter):
    set_divi_by_2_3 = set(item for item in list_enter if item%2==0 or item%3==0)
    return set_divi_by_2_3
list3 = [1,2,3,4,5,6,7,8,9]
print(f'List3: {list3}')
print(f'Chuyển list1 thành set chia hết cho 2 hoặc 3: {set_divisible_by_2_3(list3)}')

# Cartesian Product not duplicate
list4 = [1,2,3,4]
list5 = [3,4,5,6]
set7 = set(product(list4,list5))
print(f'{set7}')
