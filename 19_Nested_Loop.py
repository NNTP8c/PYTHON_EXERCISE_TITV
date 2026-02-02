#
# Created on Tue Jan 27 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 19: Nested loop - Vòng lập lòng nhau

print('In ra bảng cửu chương')
for i in range(1,10):
    print('Bảng cửu chương', i)
    for j in range(1,11):
        print('{0} * {1} = {2}'.format(i, j, i*j))