import pymysql
from .get_db import get_db, get_db_database_connection

def create_database():
    try:
        conn = get_db_database_connection()
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS auth_server")

        cursor.execute("USE auth_server")
    except pymysql.MySQLError as e:
        print(f"\nError: {e}\n")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def create_users_table():
    try:
        conn = cursor = None
        conn = get_db()

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

    except pymysql.MySQLError as e:
        print(f"\nError: {e}\n")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()