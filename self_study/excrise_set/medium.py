# Intersection set
set1 = {3,4,6,7}
set2 = {3,7,8,9}
# set3 = set1 & set2
set3 = set1.intersection(set2)
print(f'Giao của set1 và set2 là: {set3}')

# Difference set
# set4 = set1 - set2
set4 = set1.difference(set2)
print(f'Có trong set1 nhưng không có trong set2(trừ hai set): {set4}')

# Issubset set
set5 = {4,5,6}
set6 = {2,4,6,8,5}
if (set5.issubset(set6)) & (set5<=set6):
    print(f'{set5} là con {set6}')
else:
    print(f'{set5} không là con {set6}')

# Issuperset set
if (set6>=set5) & (set6.issuperset(set5)):
    print(f'{set6} là bao của {set5}')
else:
    print(f'{set6} không là bao của {set5}')

# Function remove duplicate in list by set
list1 = [1,5,5,7,7,4,4,7,8,3,9]
def remove_duplicate(list_duplicate):
    return set(list_duplicate)
print(f'Chuyển list thành set xóa trùng list: {remove_duplicate(list1)}')
