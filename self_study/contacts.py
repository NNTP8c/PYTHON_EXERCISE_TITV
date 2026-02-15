#
# Created on Mon Feb 09 2026
#
# Copyright (c) 2026 Your Company
#

import os
from unidecode import unidecode

FILENAME = 'contact.txt'

def load_contact():
    contact = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r',encoding = 'utf8') as file:
            for line in file:
                name,phone = line.strip().split(':')
                contact[name] = phone
    return contact

def save_contact(contact):
    existing_contact = load_contact()

    with open(FILENAME,'w',encoding='utf8') as file:
        for name,phone in existing_contact.items():
            file.write(f'{name}:{phone}\n')
    
        for name,phone in contact.items():
            if name not in existing_contact:
                file.write(f'{name}:{phone}\n')
   
def add_contact(contact):
    name = input('\nNhập tên: ')
    phone = input('Nhập số điện thoại: ')
    print('\n')
    if name in contact:
        print('Có 1 tên tương tự trong danh bạ')
        choice_add = input(f'Bạn có muốn đổi số của {name} không (Y/N): ')
        if choice_add == 'Y' or choice_add == 'y':
            contact[name] = phone
            print(f'Đã đổi số của {name}\n')
        else:
            print('')
    else:
        contact[name] = phone
        print(f"Đã thêm {name} vào danh bạ\n")

def display_all_contact(contact):
    if contact:
        print('\nTất cả danh bạ:')
        for name,phone in contact.items():
            print(f'{name}:{phone}')
        print('\n')
    else:
        print('\nDanh bạ trống!\n')
    
def delete_contact(contact):
    name = input('\nNhập tên muốn xóa: ')
    name_find = unidecode(name).replace(' ','').lower()
        
    if name in contact:
        del contact[name]
        print(f'Đã xóa {name} khỏi danh bạ\n')
    else:
        for key in contact:
            key_find = unidecode(key).replace(' ','').lower()
            if key_find == name_find:
                print(f'Tìm thấy tên tương tự: {key}')
                choice_del = input(f'Bạn có muốn xóa {key} không (Y/N): ')
                if choice_del == 'y' or choice_del == 'Y':
                    del contact[key]
                    print(f'Đã xóa {key} khỏi danh bạ\n')
                else:
                    break
            else:
                print(f'Không tìm thấy {name}\n')

def search_contact(contact):
    name = input('Nhập tên hoặc số cần tìm: ')
    name_find = unidecode(name).replace(' ','').lower()
    for key,value in contact.items():
        key_find = unidecode(key).replace(' ','').lower()
        if name_find == key_find or name_find == value:
            print(f'Số cần tìm là {key}:{value}\n')

def run():
    contact = load_contact()

    while True:
        print('0. Lưu và Thoát!')
        print('1. Hiển thị tất cả')
        print('2. Thêm số mới')
        print('3. Xóa số khỏi danh bạ')
        print('4. Tìm kiếm số điện thoại')
        
        choice = input('Lựa chọn của bạn: ')
        if choice == '1':
            display_all_contact(contact)
        elif choice == '2':
            add_contact(contact)
        elif choice == '3':
            delete_contact(contact)
        elif choice == '4':
            search_contact(contact)
        elif choice == '0':
            save_contact(contact)
            print('Đã lưu và thoát!')
            break 
        else:
            print('Vui lòng nhập số hợp lệ!')
         
if __name__ == '__main__':
    run()