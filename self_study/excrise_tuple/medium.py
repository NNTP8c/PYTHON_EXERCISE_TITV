# Connect 2 tuple
tuple1 = (1,5,7,8,7)
tuple2 = (1,2,3,4,5)
tuple3 = tuple1 + tuple2
print(f'Sau khi nối hai tuple: {tuple3}')

# Multiplication tuple with 3
print(f'Nhân tuple2 với 3: {tuple2*3}')

# Convert tuple to list
tuple3_list = list(tuple3)
print(f'Chuyển đổi tuple thành list: {tuple3_list}')

# Slicing tuple
tuple_slicing = (1,5,7,8,9,5,4,6,3,34,5,3,543,7,4)
print(f'Tuple slicing: {tuple_slicing}')
print(f'Cắt từ đầu đến vị trí thứ 5: {tuple_slicing[0:5]}')
print(f'Cắt từ vị trí thứ 2 đến vị trí thứ 9: {tuple_slicing[2:10]}')
print(f'Cắt từ đầu dến vị trí thứ 4: {tuple_slicing[:5]}')
print(f'Cắt từ vị trí thứ 6 đến cuối: {tuple_slicing[6:]}')
print(f'Bước nhảy 3: {tuple_slicing[::3]}')
print(f'Bước nhảy 4 từ sau lên trước: {tuple_slicing[::-4]}')

# Find min,max in tuple
print(f'Phần tử lớn nhất tuple slicing: {max(tuple_slicing)}')
print(f'Phần tử nhỏ nhất tuple slicing: {min(tuple_slicing)}')