#
# Created on Wed Feb 04 2026
#
# Copyright (c) 2026 Your Company
#
# Lesson 39: Create table for database using Python - Tạo bảng cho cơ sở dữ liệu bằng python

import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '123456',
        database = 'quanlysinhvien'
    )

    if conn.is_connected():
        c = conn.cursor()
        
        c.execute('DROP TABLE IF EXISTS class')
        query_create_table_class = '''
            CREATE TABLE class (
            classid VARCHAR(20) NOT NULL PRIMARY KEY,
            classname VARCHAR(50)
            );
        ''' 
        c.execute(query_create_table_class)

        c.execute('DROP TABLE IF EXISTS students')
        query_create_table_students = '''
            CREATE TABLE students (
            studentid varchar(20) NOT NULL PRIMARY KEY,
            studentname VARCHAR(50),
            classid VARCHAR(20),
            FOREIGN KEY (classid) REFERENCES class(classid)
            );
        '''
        c.execute(query_create_table_students)
except Error as e:
    print(f'Error: {e}')
finally:
    if conn.is_connected():
        conn.close()