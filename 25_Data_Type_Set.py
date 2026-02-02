#
# Created on Wed Jan 28 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 25: Data type Set - Kiểu dữ liệu set

# Create Set - Tạo set
subject = {'math', 'history', 'physics', 'geography', 'literature'}
print(subject)

# Add Set - Thêm set
subject.add('chemistry')
add = {'biology', 'music', 'music'}
print(subject)
subject.update(add)
print(subject)

# Delete set
subject.remove('music')
subject.discard('music')
print(subject)
subject.pop()
print(subject)
subject.clear()
print(subject)
del subject
print(subject)