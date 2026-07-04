# Product Management System

A desktop CRUD application built from scratch using Python, Tkinter, and MySQL.

## Features
- Secure login with SHA-256 password hashing
- Add, Update, Delete products
- View all products in a tabular format
- Input validation and error handling
- Modular architecture with separate files for each operation

## Tech Stack
- Python 3
- Tkinter (GUI)
- MySQL (Database)
- mysql-connector-python

## Project Structure
- login1.py — Login screen and authentication
- dbcon.py — Database connection and shared functions
- addproduct.py — Add new products
- updateproduct.py — Update existing products
- deleteproduct.py — Delete products
- showyourproducts.py — View all products in table format
- loginscrn2.py — Main dashboard after login

## Setup
1. Install dependencies:
   pip install mysql-connector-python

2. Create MySQL database and tables:
   CREATE DATABASE project_work;
   USE project_work;
   CREATE TABLE login (username VARCHAR(50), password VARCHAR(100));
   CREATE TABLE products (product_id INT PRIMARY KEY, product_name VARCHAR(100), product_price INT);

3. Insert admin credentials:
   INSERT INTO login VALUES ('admin', SHA2('admin123', 256));

4. Update dbcon.py with your MySQL password

5. Run:
   python login1.py

## Screenshots
Login Screen — Enter username and password to access the system
Dashboard — Choose between Add, Update, Delete, or View products
Product Table — View all products in a structured table
