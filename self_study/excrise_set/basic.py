# Create set has 5 element from 1 to 5
set_1 = set()
for item in range(1,6):
    set_1.add(item)
print(f'Set có 5 phần tử từ 1 đến 5: {set_1}')

# Find element in set
if 3 in set_1:
    print(f'Có 3 trong {set_1}')
else:
    print(f'Không có 3 trong {set_1}')

# Delete element in set
set_1.discard(2)
print(f'Set_1 sau khi xóa giá trị 2: {set_1}')

# Union set
set_2 = {3,4,7,8}
set_3 = set_1 | set_2
# set_3 = set_1.union(set_2)
print(f'Set_3 khi hợp set_1 và set_2: {set_3}')