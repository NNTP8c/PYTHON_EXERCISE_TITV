from time import time
# Tuple parent
tuple_parent = (
    ('Tên: Hòa','Lớp: cd123','Điểm: 15'),
    ('Tên: Thành','Lớp: cd234','Điểm: 16'),
    ('Tên: Hiếu', 'Lớp: cd456', 'Điểm: 13')
)
print(f'Lấy ra điểm sinh viên thành: {tuple_parent[1][2]}')

# Tuple Unpacking
tuple_unpacking = (1,8,4,7.7)
a,b,c,d = tuple_unpacking
print(a)
print(b)
print(c)
print(d)

# Sort tuple
print(f'Sắp xếp tăng: {sorted(tuple_unpacking)}')
print(f'Sắp xếp giảm: {sorted(tuple_unpacking,reverse=True)}')

# Combine 2 tuple
tuple1 = (1,2,3)
tuple2 = ('a','b','c')
print(f'Sau khi dùng zip kết hợp hai tuple: {list(zip(tuple1,tuple2))}')

# Create function print even number from tuple
def even_tuple(tuple_enter):
    even = []
    for item in tuple_enter:
        if isinstance(item,int):
            if item %2 == 0:
                even.append(item)
    return tuple(even)
print(f'In ra tuple chẵn: {even_tuple(tuple_unpacking)}')

# Tuple make key
keys = ('name','class','age')
student = {
    keys[0] : 'Thành',
    keys[1] : 'FB46',
    keys[2] : 18
}
print(f'In ra lớp của sinh viên: {student[keys[1]]}')

# Make function add element into tuple
def add_tuple(tuple_,element):
    list_tuple = list(tuple_)
    list_tuple.append(element)
    tuple_added = tuple(list_tuple)
    return tuple_added

tuple5 = (1,7,4.5,'d')
print(f'Tuple5 chưa thêm: {tuple5}')
print(f'Tuple5 đã thêm: {add_tuple(tuple5,'python')}') 

# Compare efficiency of list and tuple
start_time = time()
list_efficiency = []
for item in range(1000):
    list_efficiency.append(item)
print(f'Thời gian thêm 1000 phần tử vào list: {time() - start_time:.6f} giây')

start_time = time()
tuple_efficiency = ()
for item in range(1000):
    tuple_efficiency += (item,)
print(f'Thời gian thêm 1000 phần tử vào tuple: {time() - start_time:.6f} giây')

start_time = time()
for item in range(1000):
    list_efficiency.remove(item)
print(f'Thời gian xóa 1000 phần tử của list: {time() - start_time:.6f} giây')

start_time = time()
tuple_efficiency = list(tuple_efficiency)
for item in range(1000):
    tuple_efficiency.remove(item)
tuple_efficiency = tuple(tuple_efficiency)
print(f'Thời gian xóa 1000 phần tử của tuple: {time() - start_time:.6f} giây')
print(f'{tuple_efficiency}')






