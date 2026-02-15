from collections import Counter

# Create tuple has 3 element and print
tuple_3_element = (1,5,5)
print(f'Tuple 3 element: {tuple_3_element}')

# Create tuple has 5 element and print element second,last
tuple_5_element = (3,5.6,'python',True,tuple_3_element,None)
print(f'Tuple 5 element: {tuple_5_element}')

# Create tuple has 4 element and print it by for
tuple_4_element = (3.4,'python',tuple_5_element,None)
for item in tuple_4_element:
    print(f'Tuple 4 element: {item}')

# Check object has in tuple
object_find = 5
if object_find in tuple_4_element:
    print(f'{object_find} có trong tuple_4_element')
else:
    print(f'Không có {object_find} trong tuple_4_element')

# Count the number appear element
tuple_count = (3,6,8,3,9,3,5,3,7,8,5,4)
count = tuple_count.count(3)
print(f'Đối tượng 3 xuất hiện {count} lần trong tuple_count')
counts = Counter(tuple_count)
print(f'Số lần xuất hiện của các phần tử trong tuple_count là: {counts}')
