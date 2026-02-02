#
# Created on Tue Jan 27 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 20: Data type string - Kiểu dữ liệu string

s1 = 'hello'
s2 = 'price'
s3 = s1 + ' ' + s2
print(s3)

# Multi line string - Chuỗi nhiều dòng
# Method 1 - Cách 1
multiString1 = '''Line 0
Line 1
Line 2
Line 3'''
print(multiString1)

# String repeat - Lặp lại chuỗi
repeat = 'goodbye\n'
repeatString = repeat * 10
print(repeatString)

# Supstring - kiểm tra chuỗi có thuộc chuỗi khác không
string1 = 'Multi line string'
string2 = 'string'
string3 = 'goodbye'
if string2 in string1:
    print('string2 là chuỗi con string1')
else:
    print('string2 không là chuỗi con string1')
if string3 in string1:
    print('string3 is a supstring string1')
else:
    print('string3 not a supstring string1')

# Capitalize the firt letter - Viết hoa từ đầu tiên
capitalize = 'hôm nay trời đẹp quá'
capitalize = str.capitalize(capitalize)
print(capitalize)

# Capitalize the entire string - Viết hoa toàn bộ chuỗi
capitalize = capitalize.upper()
print(capitalize)

# Viết thường toàn bộ chuỗi
capitalize = capitalize.lower()
print(capitalize)

# Find and count character in string - Tìm và đếm ký tự trong chuỗi
string4 = 'Lập trình python, học python'
print(string4.find('python'))
print(string4.count('python'))

# Replace string - Thay đổi chuỗi
print(string4.replace('python','PYTHON'))

# Split a string into a list - Tách chuỗi thành danh sách
print(string4.split())