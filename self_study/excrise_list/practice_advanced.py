# Create multiplication table by list 2d
multiplication_list = []
for num1 in range(1,10):
    multiplication_list_num1 = []
    for num2 in range(1,11):
        result = num1 * num2
        str_result = str(f'{num1} * {num2} = {result}')
        multiplication_list_num1.append(str_result)
    multiplication_list.append(multiplication_list_num1)
for item in multiplication_list:
    print(item)

# Find element max in list
listFindMax = [7,34,2,35,67,34.4,8,9,34,17,3.4,2.3,6.7]
max = 0
for item in listFindMax:
    if item > max:
        max = item
print(f'Phần tử lớn nhất là: {max}')

# Classify list even/odd
even = []
odd = []
for item in listFindMax:
    if isinstance(item,int):
        if item%2==0:
            even.append(item)
        else:
            odd.append(item)
print(f'Danh sách số chẵn: {even}')
print(f'Danh sách số lẻ: {odd}')

# Encoding
str_encoding = input('Nhập chuỗi muốn mã hóa (unicode): ')

def encoding(str_encoding):
    list_encoding = []
    for item in str_encoding:
        list_encoding.append(ord(item))
    return list_encoding

def decoding(encoding):
    decoding_str = ''
    for item in encoding:
        decoding_str += chr(item)
    return decoding_str

encoding = encoding(str_encoding)
decoding = decoding(encoding)
print(f'Chuỗi sau khi mã hóa unicode: {encoding}')
print(f'Chuỗi sau khi giải mã unicode: {decoding}')
