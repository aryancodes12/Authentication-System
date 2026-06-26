import pymysql
from .get_db import get_db

try:
    conn = cursor = None
    conn = get_db()
    print(f"\nConnection Successfull!\n")

    cursor = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""
    
    cursor.execute(query)
    print(f"\nTable Created Successfully!\n")

except pymysql.MySQLError as e:
    print(f"\nError: {e}\n")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()