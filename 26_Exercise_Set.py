#
# Created on Wed Jan 28 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 26: Exercise set - Bài tập về set

import random
winPrize = set()

while (True):
    print('==========Menu==========')
    print('1. Nhập số điện thoạn nhận thưởng')
    print('2. Xóa số điện thoại nhận thưởng')
    print('3. Quay trúng thưởng các số điện thoại')
    print('4. Kết thúc')
    
    choice = int(input('Nhập lựa chọn: '))
    
    if (choice == 1):
        phoneNumber = input('Nhập số điện thoại quay thưởng: ')
        winPrize.add(phoneNumber)
        print(winPrize)
    elif (choice == 2):
        winPrize.discard(input('Nhập số cần xóa: '))
    elif (choice == 3):
        winner = random.choice(list(winPrize))
        print('Chúc mừng số điện thoại ' + winner + ' đã trúng thưởng')
        winPrize.discard(winner)
    else:
        break
    
    input('Nhập phím bất kỳ để tiếp tục: ')