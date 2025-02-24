import mysql.connector

# Connect to MySQL (XAMPP)
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Default XAMPP MySQL user
    password="",  # Default is empty (no password)
)

if conn.is_connected():
    print("connection successful")

cursor = conn.cursor()

command = """
CREATE DATABASE mydb;
USE mydb;
CREATE TABLE users(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
	age INT
);
"""
cursor.execute(command)
for table in cursor.fetchall():
    print(table)

cursor.close()
conn.close()

