#
# Created on Thu Jan 29 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 28: Dictionary exercise - Bài tập từ điển

dictionary = {}
while (True):
    print('''
        1. Thêm từ vựng mới\n
        2. Tra cứu từ điển\n
        3. Cập nhật từ cũ\n
        4. Xóa 1 từ trong từ điển\n
        5. Xóa hết từ điển\n
        6. In ra toàn bộ từ vựng\n
        7. In ra từ điển (Từ : Ý nghĩa)\n
        8. Kết thúc
    ''')
    choice = int(input('Nhập lựa chọn: '))

    if (choice == 1):
        vocabulary = input('Nhập từ vựng mới: ')
        meaning = input('Nhập ý nghĩa: ')
        dictionary[vocabulary] = meaning
        print('Thêm thành công!')
    elif (choice == 2):
        vocabulary = input('Nhập từ muốn tra cứu: ')
        print(vocabulary, ' : ', dictionary[vocabulary])
    elif (choice == 3):
        vocabulary = input('Nhập từ muốn cập nhật: ')
        meaning = input('Nhập ý nghĩa: ')
        dictionary[vocabulary] = meaning
        print(dictionary)
        print('Cập nhật thành công!')
    elif (choice == 4):
        vocabulary = input('Nhập từ muốn xóa: ')
        dictionary.pop(vocabulary)
        print(dictionary)
        print('Xóa thành công: ')
    elif (choice == 5):
        dictionary.clear()
        print(dictionary)
        print('Đã xóa tất cả các từ trong từ điển!')
    elif (choice == 6):
        print('Các từ trong từ điển: ')
        for x in dictionary:
            print(x)
    elif (choice == 7):
        for x,y in dictionary.items():
            print(x,y)
    elif (choice == 8):
        break
    else:
        print('Lựa chọn sai vui lòng nhập lại!')
    input('Nhấn phím bất kỳ để tiếp tục!')
