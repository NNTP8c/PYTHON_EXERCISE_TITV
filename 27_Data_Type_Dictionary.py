#
# Created on Thu Jan 29 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 27: Data type Dictionary - Kiểu dữ liệu Dictionary

# Create Dictionary
student = {
    'fullName' : "Nguyễn Thanh Phú",
    'age' : 64,
    'class' : 12
}

# Output
print(student)
print(student['fullName'])

# Update
student['fullName'] = 'Nguyễn Ngô Thanh Phú'
print(student)
student.update({'age':12, 'class':13})
print(student['age'])
print(student['class'])

# Add
student['address'] = 'TP.Hồ Chí Minh'
print(student)
student.update({'department':'math', 'birth':1997})
print(student)

# Delete
student.pop('department')
print(student)
student.popitem()
print(student)
del student['address']
print(student)
#student.clear()
#print(student)
#del student
#print(student)

# Traverse - Duyệt
for x in student:
    print(x)
print('\n')
for x in student.values():
    print(x)
print('\n')
for x in student.keys():
    print(x)
print('\n')
for x,y in student.items():
    print(x,y)

