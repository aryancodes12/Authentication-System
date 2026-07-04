import pymysql
import bcrypt
from .get_db import get_db


#Insert Admin credentials into the database on the start of the program if the database is empty
def admin_data():
    try:
        conn = cursor = None
        conn = get_db()
        cursor = conn.cursor()

        admin_name = "Admin"
        admin_username = "admin"
        admin_password = "admin123"
        admin_email = "admin@example.com"

        hashed_password = bcrypt.hashpw(admin_password.encode('utf-8'), bcrypt.gensalt())
        query = """INSERT INTO users (name, username, email, password)
                VALUES(%s, %s, %s, %s)"""
        values = (admin_name, admin_username, admin_email, hashed_password.decode('utf-8'))
        cursor.execute(query, values)

    except pymysql.MySQLError as e:
        print(f"\nError: {e}\n")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


def insert_user(name, username, email, password):
    try:
        conn = cursor = None
        conn = get_db()
        cursor = conn.cursor()

        query = """INSERT INTO users (name, username, email, password)
                VALUES(%s, %s, %s, %s)"""
        
        values = (name, username, email, password)
        cursor.execute(query, values)
    
    except pymysql.MySQLError as e:
        print(f"\nError: {e}\n")

    finally:
        if cursor: cursor.close()
        if conn: conn.close()
