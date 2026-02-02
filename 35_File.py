#
# Created on Mon Feb 02 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 35: File

# Create file  - Tạo file
try:
    f = open('For_example_1.txt', 'x')
except Exception as e:
    print(e)
finally:
    print('Tạo thành công')
    f.close()

# Write data to a file - Ghi dữ liệu vào file
try:
    with open('For_example_1.txt', mode='a', encoding='utf-8') as f:
        f.write('\nXin chào')
        f.close()
except Exception as e:
    print(e)

# Read file
try:
    with open('For_example_1.txt', mode='r', encoding='utf-8') as f:
        content = f.readline()
        print(content)
        f.close()
except Exception as e:
    print(e)

try:
    with open('For_example_1.txt', mode='r', encoding='utf-8') as f:
        content = f.readlines()
        i=1
        for x in content:
            print(str(i) + ' ' + x)
            i+=1
        f.close()
except Exception as e:
    print(e)
