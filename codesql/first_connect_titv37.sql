CREATE DATABASE QuanLySinhVien;

USE QuanLySinhVien;

CREATE TABLE SinhVien (
    MaSinhVien INT PRIMARY KEY,  
    Ten VARCHAR(100),             
    DiemTrungBinh DECIMAL(5,2) 
);

INSERT INTO SinhVien (MaSinhVien, Ten, DiemTrungBinh) 
VALUES
    (1, 'Nguyễn Văn A', 8.5),
    (2, 'Trần Thị B', 7.0),
    (3, 'Lê Minh C', 9.2);
