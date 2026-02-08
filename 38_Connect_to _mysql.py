#
# Created on Tue Feb 03 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 38: Connect to MySql

import mysql.connector
from mysql.connector import Error

def printquery(result):
    for row in result:
        print(row)

try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password =  '123456',
        database = 'quanlysinhvien'
    )
    if conn.is_connected():
        print('In tất cả sinh viên')
        my_cursor = conn.cursor()
        query_all_students = 'select * from sinhvien'
        my_cursor.execute(query_all_students)
        result = my_cursor.fetchall()
        printquery(result)
        print('\n')

        print('Thêm sinh viên 1')
        query_insert = 'insert into sinhvien (masinhvien,ten,diemtrungbinh) values (1, "Nguyễn Văn A", 9.8)'
        my_cursor.execute(query_insert)
        
        query_student_1 = 'select * from sinhvien where masinhvien = 1'
        my_cursor.execute(query_student_1)
        result = my_cursor.fetchall()
        printquery(result)
        print('\n')

        print('Sửa điểm sinh viên 2')
        query_update = 'update sinhvien set diemtrungbinh = diemtrungbinh + 1 where masinhvien = 2'
        my_cursor.execute(query_update)

        query_student_2 = 'select * from sinhvien where masinhvien = 2'
        my_cursor.execute(query_student_2)
        result = my_cursor.fetchall()
        printquery(result)
        print('\n')

        print('Xóa sinh viên 3')
        query_delete = 'delete from sinhvien where masinhvien = 3'
        my_cursor.execute(query_delete)

        query_student = 'select * from sinhvien'
        my_cursor.execute(query_student)
        result = my_cursor.fetchall()
        printquery(result)
except Error as e: 
    print(f'Error: {e}')
finally:
    if conn.is_connected():
        my_cursor.close()
        conn.close()